from __future__ import annotations

import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from arcrn_llm_io_exporter import export_final_composition_llm_io
from arcrn_metrics import mark_llm_metric_attempt, normalize_llm_metrics
from arcrn_models import PhasePipelineResult, SCHEMA_SLOTS, utc_now_iso
from arcrn_output_layout import llm_io_dir
from arcrn_progress_logger import write_progress_event
from arcrn_stages.llm_utils import (
    TokenBucketRateLimiter,
    generate_chat_completion_with_retry,
    llm_output_validation_max_retries,
    load_prompt_text,
    maybe_build_llm_client,
    parse_json_response,
    parse_json_response_strict,
    progress_bar_for,
    render_prompt_template,
    resolve_prompt_path,
    suppress_noisy_llm_loggers,
    to_compact_json,
)
from code_changes.step8_prompt_builder import _resolve_github_owner_repo
from phase3_llm_debug import phase3_failure_output_dir, raise_phase3_llm_failure


DEFAULT_PROMPT = Path(__file__).resolve().parent / "prompts" / "phase3_final_composition_prompt.txt"
DEFAULT_OVERVIEW_PROMPT = Path(__file__).resolve().parent / "prompts" / "phase3_final_overview_prompt.txt"
FULL_COMMIT_SHA_RE = re.compile(r"^[0-9a-f]{40}$", re.IGNORECASE)
MIN_COMMIT_SHA_DISPLAY_LENGTH = 7

RELEASE_TITLE = "# Release Note"
IMPORTANT_TITLE = "## Important Changes"
CHANGELOG_TITLE = "## Routine Changes"
CROSS_CUTTING_TITLE = "Cross-cutting / Other Architecture-related Changes"
NO_SIGNIFICANT_CHANGES = "No significant changes."

CHANGELOG_SLOT_TITLES: List[Tuple[str, str]] = [
    ("functional_changes.new_features", "New features"),
    ("functional_changes.bug_fixes", "Bug fixes"),
    ("functional_changes.refactorings", "Refactoring and optimization"),
    ("functional_changes.tests", "Tests"),
    ("non_functional_changes.performance", "Performance optimization"),
    ("non_functional_changes.security", "Security"),
    ("non_functional_changes.documentation", "Documentation"),
    ("non_functional_changes.build_ci", "Build / CI"),
    ("non_functional_changes.maintenance", "Maintenance"),
    ("others", "Other changes"),
]


def run_phase3_release_note_composer(
    *,
    section_entries_path: Path,
    output_dir: Path,
    config=None,
) -> PhasePipelineResult:
    entries_payload = _load_json(section_entries_path)
    entries = _prepare_entries(entries_payload.get("section_entries") or [])
    github_repository_url = _github_repository_url(config)
    fallback_markdown = _render_organized_schema(
        entries,
        traceable=False,
        github_repository_url=github_repository_url,
        config=config,
    )
    markdown, traceable_entries, overview_text, audit = _maybe_compose_with_llm(
        entries=entries,
        fallback_markdown=fallback_markdown,
        config=config,
        output_dir=output_dir,
    )
    markdown = _ensure_fixed_schema(markdown, traceable_entries, config=config)
    markdown = _strip_public_traceability(markdown)
    traceable_markdown = _render_organized_schema(
        traceable_entries,
        traceable=True,
        github_repository_url=github_repository_url,
        overview_text=overview_text,
        config=config,
    )

    output = {
        "generated_at": utc_now_iso(),
        "source_section_entries_path": str(section_entries_path),
        "schema": {
            "title": "Release Note",
            "sections": {
                "overview": "Release overview",
                "important_changes": "Important Changes",
                "regular_changelog": "Routine Changes",
            },
        },
        "markdown": markdown,
        "traceable_markdown": traceable_markdown,
        "stats": {
            "entry_count": len(entries),
            "llm_used": 1 if audit.get("llm_used") else 0,
            "generation_mode": audit.get("generation_mode") or ("llm" if audit.get("llm_used") else "fallback"),
            "component_count": len(_important_groups(traceable_entries, config=config)),
            "important_grouping_mode": _phase3_important_grouping_mode(config),
            "unknown_count": sum(1 for entry in traceable_entries if entry.get("arch_component_assignment_type") == "unknown"),
            "cross_cutting_count": sum(1 for entry in traceable_entries if entry.get("arch_component_assignment_type") == "cross_cutting"),
            "component_entry_counts": _component_entry_counts(traceable_entries, config=config),
            "final_composition_llm_call_count": int(audit.get("llm_call_count") or 0),
        },
    }
    output_files = _export(output, audit, output_dir)
    return PhasePipelineResult(output_files=output_files, stats=output["stats"])


def _maybe_compose_with_llm(
    *,
    entries: List[Dict[str, Any]],
    fallback_markdown: str,
    config,
    output_dir: Path,
) -> tuple[str, List[Dict[str, Any]], str, Dict[str, Any]]:
    traceable_entries = _clone_entries(entries)
    fallback_overview = _overview(entries)
    audit = {
        "llm_used": False,
        "generation_mode": "fallback",
        "fallback_markdown": fallback_markdown,
        "overview_text": fallback_overview,
        "calls": [],
        "llm_call_count": 0,
        "error_message": None,
    }
    if config is None:
        return fallback_markdown, traceable_entries, fallback_overview, audit
    llm_client = maybe_build_llm_client(config)
    if llm_client is None:
        return fallback_markdown, traceable_entries, fallback_overview, audit

    rate_limiter = TokenBucketRateLimiter(
        qps=getattr(config, "step10_rate_limit_qps", None),
        burst=int(getattr(config, "step10_rate_limit_burst", 1) or 1),
    )
    calls: List[Dict[str, Any]] = []
    errors: List[str] = []

    overview_text = fallback_overview

    jobs = _final_composition_jobs(entries, config)
    progress_bar = progress_bar_for(config, "Phase3.3 final entry polishing progress") if jobs else None
    if progress_bar is not None:
        progress_bar.update(completed=0, total=len(jobs))

    polished_by_id: Dict[str, str] = {}
    try:
        with suppress_noisy_llm_loggers(enabled=progress_bar is not None):
            max_workers = _phase3_final_composition_concurrency(config, len(jobs))
            if max_workers <= 1:
                for completed, job in enumerate(jobs, start=1):
                    texts, call = _call_entry_batch_llm(
                        job=job,
                        config=config,
                        llm_client=llm_client,
                        rate_limiter=rate_limiter,
                        output_dir=output_dir,
                    )
                    calls.append(call)
                    polished_by_id.update(texts)
                    if progress_bar is not None:
                        progress_bar.update(completed=completed, total=len(jobs))
            else:
                with ThreadPoolExecutor(max_workers=max_workers) as executor:
                    future_to_job = {
                        executor.submit(
                            _call_entry_batch_llm,
                            job=job,
                            config=config,
                            llm_client=llm_client,
                            rate_limiter=rate_limiter,
                            output_dir=output_dir,
                        ): job
                        for job in jobs
                    }
                    completed = 0
                    for future in as_completed(future_to_job):
                        texts, call = future.result()
                        calls.append(call)
                        polished_by_id.update(texts)
                        completed += 1
                        if progress_bar is not None:
                            progress_bar.update(completed=completed, total=len(jobs))
    finally:
        if progress_bar is not None:
            progress_bar.finish()

    traceable_entries = _apply_polished_texts(entries, polished_by_id)
    markdown = _render_organized_schema(
        traceable_entries,
        traceable=False,
        overview_text=overview_text,
        config=config,
    )
    audit.update(
        {
            "llm_used": True,
            "generation_mode": "llm_batched",
            "overview_text": overview_text,
            "calls": calls,
            "llm_call_count": len(calls),
            "error_message": "; ".join(errors),
        }
    )
    return markdown, traceable_entries, overview_text, audit


def _call_overview_llm(
    *,
    entries: List[Dict[str, Any]],
    fallback_overview: str,
    config,
    llm_client,
    rate_limiter: TokenBucketRateLimiter,
    output_dir: Path,
) -> tuple[str, Dict[str, Any]]:
    prompt_path = resolve_prompt_path(config, "phase3_final_overview_prompt_path", DEFAULT_OVERVIEW_PROMPT)
    prompt_template = load_prompt_text(prompt_path)
    payload = _overview_prompt_payload(entries, config=config)
    system_prompt = "You write a concise release-note overview. Return only JSON."
    user_prompt = render_prompt_template(prompt_template, {"overview_input_json": to_compact_json(payload)})
    call = _json_llm_call(
        stage="phase3.3.final_overview",
        batch_key="overview",
        request_name_base="phase3.3:final_overview",
        prompt_path=prompt_path,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        input_payload=payload,
        expected_ids=[],
        config=config,
        llm_client=llm_client,
        rate_limiter=rate_limiter,
        output_dir=output_dir,
    )
    try:
        text = _normalize_overview_response(call["parsed_response"], fallback_overview)
    except Exception as exc:
        call["error_message"] = str(exc)
        raise
    call["overview_text"] = text
    return text, call


def _call_entry_batch_llm(
    *,
    job: Dict[str, Any],
    config,
    llm_client,
    rate_limiter: TokenBucketRateLimiter,
    output_dir: Path,
) -> tuple[Dict[str, str], Dict[str, Any]]:
    prompt_path = resolve_prompt_path(config, "phase3_final_composition_prompt_path", DEFAULT_PROMPT)
    prompt_template = load_prompt_text(prompt_path)
    prompt_entries, prompt_id_to_entry_id = _final_composition_prompt_entries(job["entries"])
    system_prompt = "You polish already-written release-note entries. Return only JSON."
    user_prompt = render_prompt_template(
        prompt_template,
        {
            "composition_input_json": to_compact_json(
                {
                    "group_key": job["group_key"],
                    "group_title": job["group_title"],
                    "section_type": job["section_type"],
                    "entries": prompt_entries,
                }
            )
        },
    )
    expected_ids = list(prompt_id_to_entry_id.keys())
    audit_payload = {**job, "entries": prompt_entries, "entry_id_map": prompt_id_to_entry_id}
    call = _json_llm_call(
        stage="phase3.3.entry_polishing",
        batch_key=job["batch_key"],
        request_name_base=f"phase3.3:entry_polishing:{job['batch_key']}",
        prompt_path=prompt_path,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        input_payload=audit_payload,
        expected_ids=expected_ids,
        config=config,
        llm_client=llm_client,
        rate_limiter=rate_limiter,
        output_dir=output_dir,
    )
    try:
        prompt_texts = _normalize_entry_text_response(call["parsed_response"], expected_ids)
    except Exception as exc:
        call["error_message"] = str(exc)
        raise
    texts = {prompt_id_to_entry_id[prompt_id]: text for prompt_id, text in prompt_texts.items()}
    call["entry_id_map"] = prompt_id_to_entry_id
    call["polished_entry_count"] = len(texts)
    return texts, call


def _final_composition_prompt_entries(entries: Sequence[Dict[str, Any]]) -> tuple[List[Dict[str, Any]], Dict[str, str]]:
    prompt_entries: List[Dict[str, Any]] = []
    prompt_id_to_entry_id: Dict[str, str] = {}
    for index, entry in enumerate(entries, start=1):
        prompt_id = f"E{index:03d}"
        entry_id = str(entry.get("entry_id") or "").strip()
        prompt_id_to_entry_id[prompt_id] = entry_id
        prompt_entry = dict(entry)
        prompt_entry["entry_id"] = prompt_id
        prompt_entries.append(prompt_entry)
    return prompt_entries, prompt_id_to_entry_id


def _json_llm_call(
    *,
    stage: str,
    batch_key: str,
    request_name_base: str,
    prompt_path: Path,
    system_prompt: str,
    user_prompt: str,
    input_payload: Dict[str, Any],
    expected_ids: List[str],
    config,
    llm_client,
    rate_limiter: TokenBucketRateLimiter,
    output_dir: Path,
) -> Dict[str, Any]:
    max_attempts = 1 + llm_output_validation_max_retries(config)
    audit = {
        "llm_used": True,
        "stage": stage,
        "batch_key": batch_key,
        "request_name": request_name_base,
        "prompt_path": str(prompt_path),
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
        "raw_response": None,
        "parsed_response": None,
        "error_message": None,
        "attempts": [],
    }
    last_error: Optional[BaseException] = None
    for attempt in range(1, max_attempts + 1):
        raw = None
        llm_metrics: Dict[str, Any] = {}
        rendered_prompt = _retry_json_prompt(user_prompt, attempt, last_error)
        try:
            raw, llm_metrics = generate_chat_completion_with_retry(
                config=config,
                llm_client=llm_client,
                system_prompt=system_prompt,
                user_prompt=rendered_prompt,
                request_name=f"{request_name_base}:attempt{attempt}",
                rate_limiter=rate_limiter,
            )
            llm_metrics = mark_llm_metric_attempt(
                normalize_llm_metrics(llm_metrics),
                validation_attempt_count=attempt,
                is_validation_retry=attempt > 1,
            )
            parsed = parse_json_response_strict(raw)
            if expected_ids:
                _normalize_entry_text_response(parsed, expected_ids)
            else:
                _normalize_overview_response(parsed, "")
            audit["attempts"].append({"attempt": attempt, "ok": True, "raw_response": raw, "llm_metrics": llm_metrics})
            audit.update({"raw_response": raw, "parsed_response": parsed, "error_message": None})
            return audit
        except Exception as exc:
            last_error = exc
            failed_metric = mark_llm_metric_attempt(
                normalize_llm_metrics(llm_metrics or getattr(exc, "llm_metrics", {})),
                validation_attempt_count=attempt,
                is_validation_retry=attempt > 1,
                success=False,
                error_type=type(exc).__name__,
                error_message=str(exc),
            )
            audit["attempts"].append(
                {
                    "attempt": attempt,
                    "ok": False,
                    "raw_response": raw,
                    "error_message": str(exc),
                    "llm_metrics": failed_metric,
                }
            )
            write_progress_event(
                config,
                "llm_output_validation_failure",
                stage=stage,
                request_name=f"{request_name_base}:attempt{attempt}",
                validation_attempt=attempt,
                max_validation_attempts=max_attempts,
                error_type=type(exc).__name__,
                error_message=str(exc),
                raw_response_chars=len(raw or ""),
                expected_entry_count=len(expected_ids),
            )

    audit["error_message"] = str(last_error or "Unknown final composition validation failure")
    _raise_final_composition_failure(
        config=config,
        output_dir=output_dir,
        stage=stage,
        batch_key=batch_key,
        prompt_path=prompt_path,
        rendered_prompt=_retry_json_prompt(user_prompt, max_attempts, last_error),
        raw_response=str((audit["attempts"][-1] if audit["attempts"] else {}).get("raw_response") or ""),
        validation_attempts=audit["attempts"],
        error=last_error,
        input_payload=input_payload,
    )
    raise RuntimeError(audit["error_message"])


def _render_organized_schema(
    entries: List[Dict[str, Any]],
    *,
    traceable: bool,
    github_repository_url: str = "",
    overview_text: str = "",
    config=None,
) -> str:
    important_groups = _important_groups(entries, config=config)
    changelog_groups = _regular_changelog_groups(entries)
    commit_display_ids = _commit_display_ids(entries) if traceable else {}
    lines = [
        "# Release Note",
        "",
        "## Important Changes",
        "",
    ]

    if not important_groups:
        lines.append(f"- {NO_SIGNIFICANT_CHANGES}")
    else:
        for title, group_entries in important_groups:
            lines.extend(
                [
                    f"### {title}",
                    *_bullet_lines(
                        group_entries,
                        traceable=traceable,
                        github_repository_url=github_repository_url,
                        commit_display_ids=commit_display_ids,
                    ),
                    "",
                ]
            )
        if lines and lines[-1] == "":
            lines.pop()

    lines.extend(["", "## Routine Changes", ""])
    for _slot, title, group_entries in changelog_groups:
        lines.extend(
            [
                f"### {title}",
                *_bullet_lines(
                    group_entries,
                    traceable=traceable,
                    github_repository_url=github_repository_url,
                    commit_display_ids=commit_display_ids,
                ),
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def _render_fixed_schema(
    entries: List[Dict[str, Any]],
    *,
    traceable: bool,
    github_repository_url: str = "",
) -> str:
    return _render_organized_schema(entries, traceable=traceable, github_repository_url=github_repository_url)


def _bullet_lines(
    entries: List[Dict[str, Any]],
    *,
    traceable: bool,
    github_repository_url: str = "",
    commit_display_ids: Dict[str, str] | None = None,
) -> List[str]:
    if not entries:
        return [f"- {NO_SIGNIFICANT_CHANGES}"]
    lines: List[str] = []
    for entry in entries:
        text = str(entry.get("text") or "").strip()
        if not text:
            text = NO_SIGNIFICANT_CHANGES
        lines.append(f"- {text}")
        if traceable:
            sources = {
                str(item.get("commit_id") or ""): item
                for item in (entry.get("traceability") or {}).get("source_commits") or []
                if isinstance(item, dict) and str(item.get("commit_id") or "")
            }
            traceability = _format_traceability_mapping(
                entry.get("source_commits") or [],
                sources,
                github_repository_url,
                commit_display_ids or {},
            )
            if traceability:
                lines.append(f"  ↳ {traceability}")
    return lines


def _important_groups(entries: List[Dict[str, Any]], config=None) -> List[Tuple[str, List[Dict[str, Any]]]]:
    mode = _phase3_important_grouping_mode(config)
    grouped: Dict[str, List[Dict[str, Any]]] = {}
    order: List[str] = []
    for entry in entries:
        if not _is_architecture_labeled(entry):
            continue
        title = _important_group_title(entry, mode)
        if title not in grouped:
            grouped[title] = []
            order.append(title)
        grouped[title].append(entry)
    return [(title, grouped[title]) for title in order]


def _regular_changelog_groups(entries: List[Dict[str, Any]]) -> List[Tuple[str, str, List[Dict[str, Any]]]]:
    by_slot = {slot: [] for slot in SCHEMA_SLOTS}
    for entry in entries:
        if _is_architecture_labeled(entry):
            continue
        slot = str(entry.get("slot") or "others")
        if slot not in by_slot:
            slot = "others"
        by_slot[slot].append(entry)
    return [(slot, title, by_slot.get(slot, [])) for slot, title in CHANGELOG_SLOT_TITLES]


def _display_component_title(entry: Dict[str, Any]) -> str:
    assignment_type = str(entry.get("arch_component_assignment_type") or "").strip()
    component = str(entry.get("display_arch_component") or "").strip()
    if assignment_type == "component" and component:
        return component
    return CROSS_CUTTING_TITLE


def _important_group_title(entry: Dict[str, Any], mode: str) -> str:
    if mode == "slot":
        return _slot_display_title(str(entry.get("slot") or "others"))
    if mode == "flat":
        return "Architecture-related Changes"
    return _display_component_title(entry)


def _slot_display_title(slot: str) -> str:
    normalized = slot if slot in SCHEMA_SLOTS else "others"
    for candidate, title in CHANGELOG_SLOT_TITLES:
        if candidate == normalized:
            return title
    return slot.replace("_", " ").replace(".", " / ").title()


def _is_architecture_labeled(entry: Dict[str, Any]) -> bool:
    top_section = str(entry.get("top_section") or "").strip().lower()
    if top_section in {"important", "important_changes"}:
        return True
    if top_section in {"ordinary", "ordinary_changelog", "regular_changelog", "changelog"}:
        return False
    label_type = str(entry.get("architecture_label_type") or "").strip().lower()
    label_text = str(entry.get("architecture_label") or "").strip()
    return bool(label_text) and label_type not in {"", "none"}


def _prepare_entries(entries: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    result: List[Dict[str, Any]] = []
    seen: set[str] = set()
    for index, raw in enumerate(entries, start=1):
        entry = dict(raw or {})
        entry_id = str(entry.get("entry_id") or entry.get("group_id") or "").strip()
        if not entry_id or entry_id in seen:
            entry_id = f"ENTRY-{index:04d}"
        seen.add(entry_id)
        entry["entry_id"] = entry_id
        if not entry.get("text"):
            entry["text"] = NO_SIGNIFICANT_CHANGES
        result.append(entry)
    return result


def _final_composition_jobs(entries: List[Dict[str, Any]], config) -> List[Dict[str, Any]]:
    groups: List[Tuple[str, str, str, List[Dict[str, Any]]]] = []
    for title, group_entries in _important_groups(entries, config=config):
        groups.append(("important", _safe_key(f"important-{title}"), title, group_entries))
    for slot, title, group_entries in _regular_changelog_groups(entries):
        if group_entries:
            groups.append(("changelog", _safe_key(f"changelog-{slot}"), title, group_entries))

    batch_size = _phase3_final_composition_batch_size(config)
    jobs: List[Dict[str, Any]] = []
    for section_type, group_key, group_title, group_entries in groups:
        chunk_count = (len(group_entries) + batch_size - 1) // batch_size if group_entries else 0
        for index in range(chunk_count):
            chunk = group_entries[index * batch_size : (index + 1) * batch_size]
            jobs.append(
                {
                    "section_type": section_type,
                    "group_key": group_key,
                    "group_title": group_title,
                    "batch_key": f"{group_key}#chunk{index + 1:03d}",
                    "chunk_index": index + 1,
                    "chunk_count": chunk_count,
                    "entries": _entries_for_final_prompt(chunk),
                }
            )
    return jobs


def _entries_for_final_prompt(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    prompt_entries: List[Dict[str, Any]] = []
    for entry in entries:
        prompt_entries.append(
            {
                "entry_id": str(entry.get("entry_id") or entry.get("group_id") or ""),
                "text": str(entry.get("text") or ""),
                "entry_style": str(entry.get("entry_style") or "full"),
                "release_note_value": str(entry.get("release_note_value") or "include"),
            }
        )
    return prompt_entries


def _overview_prompt_payload(entries: List[Dict[str, Any]], config=None) -> Dict[str, Any]:
    important_groups = _important_groups(entries, config=config)
    changelog_groups = _regular_changelog_groups(entries)
    representative_entries = []
    for entry in entries[:12]:
        representative_entries.append(
            {
                "text": str(entry.get("text") or "")[:260],
                "slot": str(entry.get("slot") or ""),
                "has_architecture_label": _is_architecture_labeled(entry),
                "display_arch_component": str(entry.get("display_arch_component") or ""),
            }
        )
    return {
        "entry_count": len(entries),
        "covered_commit_count": len({commit for entry in entries for commit in entry.get("source_commits") or []}),
        "important_change_count": sum(len(group_entries) for _title, group_entries in important_groups),
        "regular_changelog_count": sum(len(group_entries) for _slot, _title, group_entries in changelog_groups),
        "important_component_counts": {title: len(group_entries) for title, group_entries in important_groups},
        "changelog_slot_counts": {title: len(group_entries) for _slot, title, group_entries in changelog_groups if group_entries},
        "representative_entries": representative_entries,
    }


def _normalize_overview_response(parsed: Dict[str, Any], fallback_overview: str) -> str:
    text = str(parsed.get("overview") or "").strip()
    if not text:
        raise ValueError("Final overview response must contain a non-empty overview field.")
    return _single_paragraph(text) or fallback_overview


def _normalize_entry_text_response(parsed: Dict[str, Any], expected_ids: List[str]) -> Dict[str, str]:
    raw_items = parsed.get("entries")
    if isinstance(raw_items, dict):
        raw_items = [{"entry_id": key, "text": value} for key, value in raw_items.items()]
    if not isinstance(raw_items, list):
        raise ValueError("Final composition response must contain entries as a list or object.")

    expected = list(expected_ids)
    expected_set = set(expected)
    seen: set[str] = set()
    result: Dict[str, str] = {}
    for raw in raw_items:
        if not isinstance(raw, dict):
            raise ValueError("Each polished entry must be an object.")
        raw_entry_id = str(raw.get("entry_id") or "").strip()
        entry_id = _resolve_final_composition_entry_id(raw_entry_id, expected, seen)
        if entry_id not in expected_set:
            raise ValueError(f"Unknown entry_id in final composition response: {entry_id}")
        if entry_id in seen:
            raise ValueError(f"Duplicate entry_id in final composition response: {entry_id}")
        text = str(raw.get("text") or "").strip()
        if not text:
            raise ValueError(f"Empty text in final composition response for entry_id {entry_id}")
        seen.add(entry_id)
        result[entry_id] = text
    missing = [entry_id for entry_id in expected if entry_id not in seen]
    if missing:
        raise ValueError(f"Final composition response missing entry_id values: {missing}")
    return result


def _resolve_final_composition_entry_id(raw_entry_id: str, expected_ids: List[str], seen: set[str]) -> str:
    entry_id = str(raw_entry_id or "").strip()
    if entry_id in expected_ids:
        return entry_id
    if len(entry_id) < 6:
        return entry_id
    candidates = [
        expected_id
        for expected_id in expected_ids
        if expected_id not in seen and (expected_id.endswith(f"_{entry_id}") or expected_id.endswith(entry_id))
    ]
    if len(candidates) == 1:
        return candidates[0]
    near_hash_candidates = [
        expected_id
        for expected_id in expected_ids
        if expected_id not in seen and _is_unique_entry_hash_copy_error(entry_id, expected_id)
    ]
    if len(near_hash_candidates) == 1:
        return near_hash_candidates[0]
    return entry_id


def _is_unique_entry_hash_copy_error(raw_entry_id: str, expected_id: str) -> bool:
    raw_prefix, raw_suffix = _split_entry_hash_suffix(raw_entry_id)
    expected_prefix, expected_suffix = _split_entry_hash_suffix(expected_id)
    if not raw_prefix or raw_prefix != expected_prefix:
        return False
    if len(raw_suffix) != len(expected_suffix) or len(raw_suffix) < MIN_COMMIT_SHA_DISPLAY_LENGTH:
        return False
    if not _is_hex(raw_suffix) or not _is_hex(expected_suffix):
        return False
    if sorted(raw_suffix.lower()) == sorted(expected_suffix.lower()):
        return True
    distance = sum(1 for left, right in zip(raw_suffix.lower(), expected_suffix.lower()) if left != right)
    return 0 < distance <= 2


def _split_entry_hash_suffix(entry_id: str) -> Tuple[str, str]:
    prefix, separator, suffix = str(entry_id or "").strip().rpartition("_")
    if not separator:
        return "", ""
    return prefix, suffix


def _is_hex(value: str) -> bool:
    return bool(value) and all(char in "0123456789abcdefABCDEF" for char in value)


def _apply_polished_texts(entries: List[Dict[str, Any]], polished_by_id: Dict[str, str]) -> List[Dict[str, Any]]:
    result = _clone_entries(entries)
    for entry in result:
        entry_id = str(entry.get("entry_id") or "")
        if entry_id in polished_by_id:
            entry["text"] = polished_by_id[entry_id]
    return result


def _overview(entries: List[Dict[str, Any]]) -> str:
    total_commits = len({commit for entry in entries for commit in entry.get("source_commits") or []})
    important_count = sum(1 for entry in entries if _is_architecture_labeled(entry))
    changelog_count = len(entries) - important_count
    if not entries:
        return "This release has no changes suitable for release-note generation."
    return (
        f"This release note covers {len(entries)} changes linked to {total_commits} source commits; "
        f"{important_count} entries are listed under Important Changes and {changelog_count} entries under Routine Changes."
    )


def _ensure_fixed_schema(markdown: str, entries: List[Dict[str, Any]], config=None) -> str:
    if _has_fixed_schema(markdown):
        return markdown
    return _render_organized_schema(entries, traceable=False, config=config)


def _has_fixed_schema(markdown: str) -> bool:
    required = [RELEASE_TITLE, IMPORTANT_TITLE, CHANGELOG_TITLE]
    return all(item in markdown for item in required)


def _strip_public_traceability(markdown: str) -> str:
    lines: List[str] = []
    for line in markdown.splitlines():
        lower = line.lower()
        if (
            "source commits:" in lower
            or "source commit:" in lower
            or "source prs:" in lower
            or "source pr:" in lower
            or "(source:" in lower
            or line.strip().startswith("↳")
        ):
            continue
        lines.append(line)
    return "\n".join(lines).rstrip() + "\n"


def _format_traceability_mapping(
    source_commits: List[Any],
    sources: Dict[str, Dict[str, Any]],
    github_repository_url: str,
    commit_display_ids: Dict[str, str],
) -> str:
    groups: Dict[tuple[Any, str], List[str]] = {}
    group_order: List[tuple[Any, str]] = []
    commits_without_pr: List[str] = []
    for raw_commit_id in source_commits:
        commit_id = str(raw_commit_id or "").strip()
        if not commit_id:
            continue
        pull_requests = _valid_pull_requests(sources.get(commit_id, {}))
        if not pull_requests:
            if commit_id not in commits_without_pr:
                commits_without_pr.append(commit_id)
            continue
        for pull_request in pull_requests:
            key = (pull_request["number"], pull_request["url"])
            if key not in groups:
                group_order.append(key)
                groups[key] = []
            if commit_id not in groups[key]:
                groups[key].append(commit_id)

    chunks: List[str] = []
    for number, url in group_order:
        commits = ", ".join(
            _format_commit_reference(
                commit_id,
                sources.get(commit_id, {}),
                github_repository_url,
                commit_display_ids.get(commit_id, commit_id),
            )
            for commit_id in groups[(number, url)]
        )
        chunks.append(f"{_format_pull_request_reference({'number': number, 'url': url})}: {commits}")
    if commits_without_pr:
        commits = "、".join(
            _format_commit_reference(
                commit_id,
                sources.get(commit_id, {}),
                github_repository_url,
                commit_display_ids.get(commit_id, commit_id),
            )
            for commit_id in commits_without_pr
        )
        chunks.append(f"No PR: {commits}")
    return " | ".join(chunks)


def _format_commit_reference(
    commit_id: str,
    source: Dict[str, Any],
    github_repository_url: str = "",
    display_id: str = "",
) -> str:
    url = str(source.get("commit_url") or "").strip()
    if not url and github_repository_url and commit_id:
        url = f"{github_repository_url}/commit/{commit_id}"
    label = display_id or commit_id
    return f"[{label}]({url})" if url else label


def _valid_pull_requests(source: Dict[str, Any]) -> List[Dict[str, Any]]:
    result: List[Dict[str, Any]] = []
    seen = set()
    for raw in source.get("pull_requests") or []:
        if not isinstance(raw, dict):
            continue
        number = raw.get("number")
        url = str(raw.get("url") or "").strip()
        key = (number, url)
        if not number or not url or key in seen:
            continue
        result.append({"number": number, "url": url})
        seen.add(key)
    return result


def _format_pull_request_reference(pull_request: Dict[str, Any]) -> str:
    return f"[#{pull_request['number']}]({pull_request['url']})"


def _commit_display_ids(entries: List[Dict[str, Any]]) -> Dict[str, str]:
    commit_ids: List[str] = []
    for entry in entries:
        for raw_commit_id in entry.get("source_commits") or []:
            commit_id = str(raw_commit_id or "").strip()
            if commit_id and commit_id not in commit_ids:
                commit_ids.append(commit_id)

    display_ids: Dict[str, str] = {}
    lowered_ids = {commit_id: commit_id.lower() for commit_id in commit_ids}
    for commit_id in commit_ids:
        if not FULL_COMMIT_SHA_RE.match(commit_id):
            display_ids[commit_id] = commit_id
            continue
        length = MIN_COMMIT_SHA_DISPLAY_LENGTH
        while any(
            other_id != commit_id
            and lowered_ids[other_id].startswith(lowered_ids[commit_id][:length])
            for other_id in commit_ids
        ):
            length += 1
        display_ids[commit_id] = commit_id[:length]
    return display_ids


def _github_repository_url(config) -> str:
    repo_path = getattr(config, "repo_path", None) if config is not None else None
    if repo_path is None:
        return ""
    owner_repo = _resolve_github_owner_repo(repo_path)
    if owner_repo is None:
        return ""
    owner, repo = owner_repo
    return f"https://github.com/{owner}/{repo}"


def _component_entry_counts(entries: List[Dict[str, Any]], config=None) -> Dict[str, int]:
    mode = _phase3_important_grouping_mode(config)
    result: Dict[str, int] = {}
    for entry in entries:
        if not _is_architecture_labeled(entry):
            continue
        title = _important_group_title(entry, mode)
        result[title] = result.get(title, 0) + 1
    return dict(sorted(result.items(), key=lambda item: (-item[1], item[0])))


def _phase3_important_grouping_mode(config) -> str:
    mode = str(getattr(config, "phase3_important_grouping_mode", "component") or "component").strip().lower()
    supported = {"component", "slot", "flat"}
    if mode not in supported:
        raise ValueError(f"Unsupported phase3_important_grouping_mode: {mode}. Supported modes: {sorted(supported)}")
    return mode


def _phase3_final_composition_batch_size(config) -> int:
    try:
        return max(1, int(getattr(config, "phase3_final_composition_batch_size", 25) or 25))
    except Exception:
        return 25


def _phase3_final_composition_concurrency(config, job_count: int) -> int:
    try:
        configured = int(getattr(config, "phase3_final_composition_concurrency", 1) or 1)
    except Exception:
        configured = 1
    return max(1, min(configured, max(1, job_count)))


def _retry_json_prompt(user_prompt: str, attempt: int, error: Optional[BaseException]) -> str:
    if attempt <= 1:
        return user_prompt
    return (
        user_prompt
        + "\n\nThe previous response failed validation: "
        + str(error or "invalid JSON or missing item")[:500]
        + "\nReturn only a valid JSON object. Cover every required id exactly once."
    )


def _raise_final_composition_failure(
    *,
    config,
    output_dir: Path,
    stage: str,
    batch_key: str,
    prompt_path: Path,
    rendered_prompt: str,
    raw_response: str,
    validation_attempts: List[Dict[str, Any]],
    error: Optional[BaseException],
    input_payload: Dict[str, Any],
) -> None:
    raise_phase3_llm_failure(
        output_dir=phase3_failure_output_dir(config, output_dir),
        stage=stage,
        batch_or_bucket_or_slot=batch_key,
        error_type="final_composition_validation_error",
        error_message=str(error or "Final composition validation failed."),
        exception=error,
        prompt_template_path=str(prompt_path),
        rendered_prompt=rendered_prompt,
        raw_llm_response=raw_response,
        input_summary={"entry_count": len(input_payload.get("entries") or [])},
        input_payload=input_payload,
        validation_attempts=validation_attempts,
    )


def _single_paragraph(text: str) -> str:
    return " ".join(str(text or "").split())


def _safe_key(value: str) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "_", str(value or "").strip()).strip("_")
    return text[:80] or "group"


def _clone_entries(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return json.loads(json.dumps(entries, ensure_ascii=False))


def _export(output: Dict[str, Any], audit: Dict[str, Any], output_dir: Path) -> Dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "final_release_note.json"
    md_path = output_dir / "final_release_note.md"
    traceable_md_path = output_dir / "final_release_note_traceable.md"
    debug_path = output_dir / "final_release_note_debug.md"
    audit_path = output_dir / "phase3_final_composition_llm_audit.json"
    _write_json(json_path, output)
    _write_json(audit_path, audit)
    md_path.write_text(output["markdown"], encoding="utf-8")
    traceable_md_path.write_text(output["traceable_markdown"], encoding="utf-8")
    debug_path.write_text(_render_debug(output, audit), encoding="utf-8")
    llm_io_path = export_final_composition_llm_io(audit, llm_io_dir(output_dir))
    return {
        "final_release_note_json": str(json_path),
        "final_release_note_markdown": str(md_path),
        "final_release_note_traceable_markdown": str(traceable_md_path),
        "final_release_note_debug": str(debug_path),
        "phase3_final_composition_llm_audit": str(audit_path),
        **({"phase3_3_llm_input_output_txt": llm_io_path} if llm_io_path else {}),
    }


def _render_debug(output: Dict[str, Any], audit: Dict[str, Any]) -> str:
    stats = output.get("stats") or {}
    return "\n".join(
        [
            "# Phase 3.3 Final Composition Debug",
            "",
            f"- generation_mode: `{stats.get('generation_mode')}`",
            f"- entry_count: `{stats.get('entry_count')}`",
            f"- component_count: `{stats.get('component_count')}`",
            f"- unknown_count: `{stats.get('unknown_count')}`",
            f"- cross_cutting_count: `{stats.get('cross_cutting_count')}`",
            f"- final_composition_llm_call_count: `{stats.get('final_composition_llm_call_count')}`",
            f"- llm_error: `{audit.get('error_message') or ''}`",
            "",
        ]
    )


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _extract_markdown_response(raw_text: str) -> str:
    text = _strip_markdown_fences(raw_text).strip()
    if text.startswith("{"):
        try:
            parsed = parse_json_response(text)
            markdown = str(parsed.get("markdown") or "").strip()
            if markdown:
                return markdown
        except Exception:
            pass
    return text


def _markdown_from_json_entry_response(raw_text: str, expected_entry_count: int) -> str:
    text = _strip_markdown_fences(raw_text).strip()
    if not text.startswith("["):
        return ""
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        return ""
    if not isinstance(parsed, list) or len(parsed) < expected_entry_count:
        return ""
    entries = []
    for index, item in enumerate(parsed, start=1):
        if not isinstance(item, dict):
            return ""
        entries.append(
            {
                "entry_id": str(item.get("entry_id") or f"ENTRY-{index:04d}"),
                "slot": str(item.get("slot") or "others"),
                "text": str(item.get("text") or "").strip(),
                "entry_style": str(item.get("entry_style") or "full"),
                "release_note_value": str(item.get("release_note_value") or "include"),
            }
        )
    return _render_organized_schema(entries, traceable=False)


def _strip_markdown_fences(text: str) -> str:
    stripped = (text or "").strip()
    if not stripped.startswith("```"):
        return stripped
    lines = stripped.splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    return "\n".join(lines).strip()
