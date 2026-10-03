from __future__ import annotations

import json
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, List, Optional

from arcrn_llm_io_exporter import export_arch_label_llm_io, export_arch_module_assignment_llm_io, export_slot_entry_llm_io
from arcrn_metrics import elapsed_sec, mark_llm_metric_attempt, normalize_llm_metrics, start_timer
from arcrn_models import RELEASE_NOTE_SCHEMA, PhasePipelineResult, SCHEMA_SLOTS, utc_now_iso
from arcrn_output_layout import llm_io_dir
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
from phase3_llm_debug import phase3_debug_fail_fast, phase3_failure_output_dir, raise_phase3_llm_failure
from phase3_arch_component_assignment import assign_architecture_components_to_entries


DEFAULT_PROMPT = Path(__file__).resolve().parent / "prompts" / "phase3_slot_entry_prompt.txt"
DEFAULT_ARCH_LABEL_PROMPT = Path(__file__).resolve().parent / "prompts" / "phase3_2_arch_label_decision_prompt.txt"
PHASE2_ABLATION_NO_ARCH_RELEVANCE = "no_phase2_arch_relevance"
MAX_ARCH_LABEL_CANDIDATE_EVENTS = 3
MAX_ARCH_LABEL_PROFILE_TEXT_CHARS = 360
MAX_ARCH_LABEL_PROFILE_LIST_ITEM_CHARS = 220
_NON_COMMIT_HEX_LIKE_TOKENS = {
    "ed25519",
}


def run_phase3_slot_entry_generator(
    *,
    aggregation_plan_path: Path,
    attributed_change_records_path: Path,
    output_dir: Path,
    config=None,
) -> PhasePipelineResult:
    plan_payload = _load_json(aggregation_plan_path)
    records_payload = _load_json(attributed_change_records_path)
    plan = plan_payload.get("aggregation_plan") or {}
    groups_root = plan.get("groups") if isinstance(plan.get("groups"), dict) else plan
    records = {
        str(record.get("commit_id") or ""): record
        for record in records_payload.get("attributed_change_records") or []
        if isinstance(record, dict) and str(record.get("commit_id") or "")
    }

    llm_client = maybe_build_llm_client(config) if config is not None else None
    prompt_path = resolve_prompt_path(config, "phase3_slot_entry_prompt_path", DEFAULT_PROMPT) if config is not None else DEFAULT_PROMPT
    rate_limiter = TokenBucketRateLimiter(
        qps=getattr(config, "step10_rate_limit_qps", None) if config is not None else None,
        burst=int(getattr(config, "step10_rate_limit_burst", 1)) if config is not None else 1,
    )

    slot_jobs: List[Dict[str, Any]] = []
    for slot in SCHEMA_SLOTS:
        groups = list(_get_slot(groups_root, slot) or [])
        groups.extend(_low_priority_groups_for_slot(plan, slot, records))
        if not groups:
            continue
        slot_jobs.append(
            {
                "slot": slot,
                "chunk_index": 1,
                "chunk_count": 1,
                "groups": groups,
                "fallback_entries": _fallback_entries(slot, groups, records),
            }
        )
    slot_jobs = _chunk_slot_jobs(slot_jobs, config)

    job_results = _run_slot_jobs_parallel(
        slot_jobs=slot_jobs,
        records=records,
        llm_client=llm_client,
        prompt_path=prompt_path,
        rate_limiter=rate_limiter,
        config=config,
        output_dir=output_dir,
    )
    entries = [entry for result in job_results for entry in result["entries"]]
    audits = [result["audit"] for result in job_results]
    llm_count = sum(1 for audit in audits if audit.get("llm_used"))
    label_started_at, label_started_perf = start_timer()
    entries, label_audits = _maybe_apply_architecture_label_decisions(
        entries=entries,
        records=records,
        llm_client=llm_client,
        rate_limiter=rate_limiter,
        config=config,
        output_dir=output_dir,
    )
    entries, component_catalog, component_assignment_audits = assign_architecture_components_to_entries(
        entries=entries,
        records=records,
        llm_client=llm_client,
        rate_limiter=rate_limiter,
        config=config,
        output_dir=output_dir,
    )
    label_finished_at = utc_now_iso()
    label_duration_sec = elapsed_sec(label_started_perf)
    label_llm_count = sum(1 for audit in label_audits if audit.get("llm_used"))
    component_assignment_llm_count = sum(1 for audit in component_assignment_audits if audit.get("llm_used"))
    labeled_entry_count = sum(1 for entry in entries if entry.get("architecture_label_type") not in {"", None, "none"})
    component_entry_counts = _component_entry_counts(entries)

    output = {
        "generated_at": utc_now_iso(),
        "source_aggregation_plan_path": str(aggregation_plan_path),
        "source_attributed_change_records_path": str(attributed_change_records_path),
        "schema": RELEASE_NOTE_SCHEMA,
        "section_entries": entries,
        "stats": {
            "entry_count": len(entries),
            "slot_count": len({entry.get("slot") for entry in entries}),
            "llm_used_slot_count": llm_count,
            "arch_label_llm_used_slot_count": label_llm_count,
            "arch_module_assignment_llm_call_count": component_assignment_llm_count,
            "architecture_labeled_entry_count": labeled_entry_count,
            "component_count": len(component_catalog.get("components") or []),
            "unknown_count": sum(1 for entry in entries if entry.get("arch_component_assignment_type") == "unknown"),
            "cross_cutting_count": sum(1 for entry in entries if entry.get("arch_component_assignment_type") == "cross_cutting"),
            "component_entry_counts": component_entry_counts,
            "phase3_2_5_started_at": label_started_at,
            "phase3_2_5_finished_at": label_finished_at,
            "phase3_2_5_duration_sec": label_duration_sec,
            "generation_mode": "llm" if llm_count else "fallback",
        },
    }
    output_files = _export(output, audits, label_audits, component_assignment_audits, component_catalog, output_dir)
    return PhasePipelineResult(output_files=output_files, stats=output["stats"])


def _run_slot_jobs_parallel(
    *,
    slot_jobs: List[Dict[str, Any]],
    records: Dict[str, Dict[str, Any]],
    llm_client,
    prompt_path: Path,
    rate_limiter: TokenBucketRateLimiter,
    config,
    output_dir: Path,
) -> List[Dict[str, Any]]:
    if not slot_jobs:
        return []

    max_workers = _phase3_slot_concurrency(config, len(slot_jobs))
    progress_bar = progress_bar_for(config, "Phase3.2 slot entry generation progress") if llm_client is not None else None
    if progress_bar is not None:
        progress_bar.update(completed=0, total=len(slot_jobs))
    try:
        with suppress_noisy_llm_loggers(enabled=progress_bar is not None):
            if max_workers <= 1:
                results: List[Dict[str, Any]] = []
                for completed, job in enumerate(slot_jobs, start=1):
                    results.append(
                        _run_one_slot_job(
                            job=job,
                            records=records,
                            llm_client=llm_client,
                            prompt_path=prompt_path,
                            rate_limiter=rate_limiter,
                            config=config,
                            output_dir=output_dir,
                        )
                    )
                    if progress_bar is not None:
                        progress_bar.update(completed=completed, total=len(slot_jobs))
                return results

            results_by_slot: Dict[str, Dict[str, Any]] = {}
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                future_to_slot = {
                    executor.submit(
                        _run_one_slot_job,
                        job=job,
                        records=records,
                        llm_client=llm_client,
                        prompt_path=prompt_path,
                        rate_limiter=rate_limiter,
                        config=config,
                        output_dir=output_dir,
                    ): job["job_key"]
                    for job in slot_jobs
                }
                completed = 0
                for future in as_completed(future_to_slot):
                    job_key = future_to_slot[future]
                    try:
                        results_by_slot[job_key] = future.result()
                    except Exception:
                        raise
                    completed += 1
                    if progress_bar is not None:
                        progress_bar.update(completed=completed, total=len(slot_jobs))

            return [results_by_slot[job["job_key"]] for job in slot_jobs]
    finally:
        if progress_bar is not None:
            progress_bar.finish()


def _run_one_slot_job(
    *,
    job: Dict[str, Any],
    records: Dict[str, Dict[str, Any]],
    llm_client,
    prompt_path: Path,
    rate_limiter: TokenBucketRateLimiter,
    config,
    output_dir: Path,
) -> Dict[str, Any]:
    entries, audit = _maybe_generate_slot_entries(
        slot=job["slot"],
        job_key=str(job.get("job_key") or job["slot"]),
        chunk_index=int(job.get("chunk_index") or 1),
        chunk_count=int(job.get("chunk_count") or 1),
        groups=job["groups"],
        records=records,
        fallback_entries=job["fallback_entries"],
        llm_client=llm_client,
        prompt_path=prompt_path,
        rate_limiter=rate_limiter,
        config=config,
        output_dir=output_dir,
    )
    return {"slot": job["slot"], "entries": entries, "audit": audit}


def _chunk_slot_jobs(slot_jobs: List[Dict[str, Any]], config) -> List[Dict[str, Any]]:
    chunk_size = _phase3_slot_entry_group_batch_size(config)
    chunked_jobs: List[Dict[str, Any]] = []
    for job in slot_jobs:
        groups = list(job.get("groups") or [])
        fallback_entries = list(job.get("fallback_entries") or [])
        if len(groups) <= chunk_size:
            next_job = dict(job)
            next_job["job_key"] = str(job["slot"])
            chunked_jobs.append(next_job)
            continue
        chunk_count = (len(groups) + chunk_size - 1) // chunk_size
        for index in range(chunk_count):
            start = index * chunk_size
            end = start + chunk_size
            next_job = dict(job)
            next_job["chunk_index"] = index + 1
            next_job["chunk_count"] = chunk_count
            next_job["groups"] = groups[start:end]
            next_job["fallback_entries"] = fallback_entries[start:end]
            next_job["job_key"] = f"{job['slot']}#chunk{index + 1:03d}"
            chunked_jobs.append(next_job)
    return chunked_jobs


def _maybe_generate_slot_entries(
    *,
    slot: str,
    groups: List[Dict[str, Any]],
    records: Dict[str, Dict[str, Any]],
    fallback_entries: List[Dict[str, Any]],
    llm_client,
    prompt_path: Path,
    rate_limiter: TokenBucketRateLimiter,
    config,
    output_dir: Path,
    job_key: str = "",
    chunk_index: int = 1,
    chunk_count: int = 1,
) -> tuple[List[Dict[str, Any]], Dict[str, Any]]:
    job_key = job_key or slot
    audit = {
        "slot": slot,
        "job_key": job_key,
        "chunk_index": chunk_index,
        "chunk_count": chunk_count,
        "llm_used": False,
        "raw_response": None,
        "error_message": None,
        "attempts": [],
    }
    if config is None or llm_client is None:
        return _attach_entries_traceability(fallback_entries, records), audit

    system_prompt = (
        "You are a slot-level release-note entry generator. "
        "Return only valid JSON with group_id, text, and confidence. Do not include source_commits."
    )
    user_prompt = render_prompt_template(
        load_prompt_text(prompt_path),
        {
            "slot": slot,
            "groups_json": to_compact_json(_groups_for_prompt(groups)),
        },
    )
    audit.update({"system_prompt": system_prompt, "user_prompt": user_prompt})
    max_attempts = 1 + llm_output_validation_max_retries(config)
    last_error: Optional[Exception] = None
    for attempt in range(1, max_attempts + 1):
        raw: Optional[str] = None
        parsed: Optional[Dict[str, Any]] = None
        llm_metrics: Dict[str, Any] = {}
        try:
            request_name = f"phase3.2:{job_key}:attempt{attempt}"
            raw, llm_metrics = generate_chat_completion_with_retry(
                config=config,
                llm_client=llm_client,
                system_prompt=system_prompt,
                user_prompt=_retry_prompt(user_prompt, attempt, last_error),
                request_name=request_name,
                rate_limiter=rate_limiter,
                max_tokens=max(1400, int(getattr(config, "llm_max_tokens", 0) or 0)),
            )
            llm_metrics = mark_llm_metric_attempt(
                normalize_llm_metrics(llm_metrics),
                validation_attempt_count=attempt,
                is_validation_retry=attempt > 1,
            )
            parsed = _parse_json_strict(raw)
            entries = _normalize_minimal_entries(slot, parsed.get("entries"), groups)
            if not entries:
                raise ValueError("LLM slot response does not contain valid source-backed entries.")
            entries = _attach_entries_traceability(entries, records)
            audit["attempts"].append({"attempt": attempt, "ok": True, "raw_response": raw, "parsed_json_if_any": parsed or {}, "llm_metrics": llm_metrics})
            audit.update({"llm_used": True, "raw_response": raw, "error_message": None})
            return entries, audit
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
                    "error_message": str(exc),
                    "raw_response": raw,
                    "parsed_json_if_any": parsed or {},
                    "llm_metrics": failed_metric,
                }
            )
            if attempt >= max_attempts:
                _raise_phase3_2_failure(
                    output_dir=output_dir,
                    config=config,
                    slot=slot,
                    job_key=job_key,
                    prompt_path=prompt_path,
                    user_prompt=user_prompt,
                    raw=raw or "",
                    error_type=_phase3_2_error_type(exc),
                    error_message=str(exc),
                    exception=exc,
                    groups=groups,
                    parsed=parsed,
                    validation_attempts=audit["attempts"],
                )

    raise AssertionError("unreachable")


def _fallback_entries(slot: str, groups: List[Dict[str, Any]], records: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    entries = []
    for group in groups:
        source_commits = [str(item) for item in group.get("source_commits") or [] if str(item)]
        evidence = [records[item] for item in source_commits if item in records]
        top_record = max(evidence, key=lambda item: float(item.get("architecture_relevance_score") or 0.0), default={})
        text = _compose_fallback_text(group, top_record, slot)
        entries.append(
            {
                "slot": slot,
                "text": text,
                "source_commits": source_commits,
                "related_arch_events": [str(item) for item in group.get("related_arch_events") or [] if str(item)],
                "confidence": _group_confidence(evidence),
                "entry_style": group.get("entry_style") or "full",
                "release_note_value": group.get("release_note_value") or "include",
                "traceability": _entry_traceability(source_commits, records),
            }
        )
    return entries


def _groups_for_prompt(groups: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    prompt_groups: List[Dict[str, Any]] = []
    for group in groups:
        prompt_groups.append(
            {
                "group_id": group.get("group_id"),
                "entry_intent": group.get("entry_intent"),
                "source_commit_summaries": [
                    item.get("commit_summary")
                    for item in (group.get("traceability") or {}).get("source_commits") or []
                    if item.get("commit_summary")
                ],
                "evidence_granularity": _unique(
                    str(item.get("evidence_granularity") or "")
                    for item in (group.get("traceability") or {}).get("source_commits") or []
                    if str(item.get("evidence_granularity") or "")
                ),
                "entry_style": group.get("entry_style") or "full",
                "release_note_value": group.get("release_note_value") or "include",
            }
        )
    return prompt_groups


def _raise_phase3_2_failure(
    *,
    output_dir: Path,
    config,
    slot: str,
    job_key: str,
    prompt_path: Path,
    user_prompt: str,
    raw: str,
    error_type: str,
    error_message: str,
    exception: BaseException,
    groups: List[Dict[str, Any]],
    parsed: Optional[Dict[str, Any]],
    validation_attempts: Optional[List[Dict[str, Any]]] = None,
) -> None:
    raise_phase3_llm_failure(
        output_dir=phase3_failure_output_dir(config, output_dir),
        stage="phase3.2_slot_entry_generation",
        batch_or_bucket_or_slot=job_key,
        error_type=error_type,
        error_message=error_message,
        exception=exception,
        prompt_template_path=str(prompt_path),
        rendered_prompt=user_prompt,
        raw_llm_response=raw,
        cleaned_response_if_any=(raw or "").strip(),
        parsed_json_if_any=parsed or {},
        input_summary={"slot": slot, "job_key": job_key, "group_count": len(groups)},
        input_payload={"groups": groups},
        validation_attempts=validation_attempts or [],
    )


def _phase3_2_error_type(exc: BaseException) -> str:
    message = str(exc)
    if "Unknown group_id" in message or "missing group_id" in message or "Duplicate group_id" in message:
        return "source_backed_validation_error"
    if "Expecting" in message or "JSON" in message or "json" in message:
        return "json_parse_error"
    return "schema_validation_error"


def _maybe_apply_architecture_label_decisions(
    *,
    entries: List[Dict[str, Any]],
    records: Dict[str, Dict[str, Any]],
    llm_client,
    rate_limiter: TokenBucketRateLimiter,
    config,
    output_dir: Path,
) -> tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    if not entries or not _phase3_arch_label_llm_enabled(config):
        return entries, []

    _ensure_phase3_arch_label_llm_client(config, llm_client)
    prompt_path = resolve_prompt_path(config, "phase3_arch_label_prompt_path", DEFAULT_ARCH_LABEL_PROMPT)
    prompt_template = load_prompt_text(prompt_path)
    system_prompt = "You are a release-note architecture-label decision assistant. Return only valid JSON."

    indexed_entries = _assign_label_entry_ids(entries)
    batches = _label_batches_by_slot(indexed_entries, records, config)
    if not batches:
        return entries, []

    max_workers = _phase3_arch_label_concurrency(config, len(batches))
    audits_by_batch: Dict[str, Dict[str, Any]] = {}
    decisions_by_entry_id: Dict[str, Dict[str, Any]] = {}
    progress_bar = progress_bar_for(config, "Phase3.2.5 architecture label progress")

    def run_batch(batch: Dict[str, Any]) -> tuple[str, Dict[str, Any], List[Dict[str, Any]]]:
        slot = str(batch.get("slot") or "unknown")
        batch_key = str(batch.get("batch_key") or slot)
        cards = list(batch.get("cards") or [])
        user_prompt = render_prompt_template(prompt_template, {"entries_json": to_compact_json(cards)})
        audit = {
            "slot": slot,
            "batch_key": batch_key,
            "chunk_index": int(batch.get("chunk_index") or 1),
            "chunk_count": int(batch.get("chunk_count") or 1),
            "llm_used": False,
            "raw_response": None,
            "error_message": None,
            "attempts": [],
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
        }
        max_attempts = 1 + llm_output_validation_max_retries(config)
        last_error: Optional[Exception] = None
        for attempt in range(1, max_attempts + 1):
            raw = ""
            parsed: Optional[Dict[str, Any]] = None
            llm_metrics: Dict[str, Any] = {}
            try:
                request_name = f"phase3.2.5:{batch_key}:attempt{attempt}"
                raw, llm_metrics = generate_chat_completion_with_retry(
                    config=config,
                    llm_client=llm_client,
                    system_prompt=system_prompt,
                    user_prompt=_arch_label_retry_prompt(user_prompt, attempt, last_error),
                    request_name=request_name,
                    rate_limiter=rate_limiter,
                    max_tokens=max(1400, int(getattr(config, "llm_max_tokens", 0) or 0)),
                )
                llm_metrics = mark_llm_metric_attempt(
                    normalize_llm_metrics(llm_metrics),
                    validation_attempt_count=attempt,
                    is_validation_retry=attempt > 1,
                )
                parsed = _parse_json_strict(raw)
                decisions = _normalize_arch_label_decisions(parsed, cards)
                audit["attempts"].append({"attempt": attempt, "ok": True, "raw_response": raw, "parsed_json_if_any": parsed or {}, "llm_metrics": llm_metrics})
                audit.update({"llm_used": True, "raw_response": raw, "error_message": None})
                return batch_key, audit, decisions
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
                        "error_message": str(exc),
                        "raw_response": raw,
                        "parsed_json_if_any": parsed or {},
                        "llm_metrics": failed_metric,
                    }
                )
                if attempt >= max_attempts:
                    _raise_phase3_arch_label_failure(
                        output_dir=output_dir,
                        config=config,
                        slot=slot,
                        batch_key=batch_key,
                        prompt_path=prompt_path,
                        user_prompt=user_prompt,
                        raw=raw,
                        error_type=_phase3_arch_label_error_type(exc),
                        error_message=str(exc),
                        exception=exc,
                        cards=cards,
                        parsed=parsed,
                        validation_attempts=audit["attempts"],
                    )
        raise AssertionError("unreachable")

    if progress_bar is not None:
        progress_bar.update(completed=0, total=len(batches))
    try:
        with suppress_noisy_llm_loggers(enabled=progress_bar is not None):
            if max_workers <= 1:
                for completed, batch in enumerate(batches, start=1):
                    slot, audit, decisions = run_batch(batch)
                    audits_by_batch[slot] = audit
                    for decision in decisions:
                        decisions_by_entry_id[str(decision.get("entry_id") or "")] = decision
                    if progress_bar is not None:
                        progress_bar.update(completed=completed, total=len(batches))
            else:
                with ThreadPoolExecutor(max_workers=max_workers) as executor:
                    future_to_slot = {executor.submit(run_batch, batch): str(batch.get("batch_key") or batch.get("slot") or "unknown") for batch in batches}
                    completed = 0
                    for future in as_completed(future_to_slot):
                        batch_key = future_to_slot[future]
                        try:
                            resolved_batch_key, audit, decisions = future.result()
                        except Exception:
                            raise
                        audits_by_batch[resolved_batch_key or batch_key] = audit
                        for decision in decisions:
                            decisions_by_entry_id[str(decision.get("entry_id") or "")] = decision
                        completed += 1
                        if progress_bar is not None:
                            progress_bar.update(completed=completed, total=len(batches))
    finally:
        if progress_bar is not None:
            progress_bar.finish()

    labeled_entries: List[Dict[str, Any]] = []
    for item in indexed_entries:
        entry = dict(item["entry"])
        entry_id = item["entry_id"]
        decision = decisions_by_entry_id.get(entry_id) or _none_arch_label_decision(entry_id)
        entry["entry_id"] = entry_id
        entry["architecture_label_decision"] = decision
        entry["architecture_label_type"] = decision.get("label_type") or "none"
        entry["architecture_label"] = decision.get("label_text") or ""
        entry["architecture_label_event_id"] = decision.get("event_id") or ""
        entry["top_section"] = (
            "important"
            if str(decision.get("label_type") or "none").strip().lower() != "none" and str(decision.get("label_text") or "").strip()
            else "ordinary_changelog"
        )
        if decision.get("label_type") != "none" and decision.get("label_text"):
            entry["text"] = _append_architecture_label(str(entry.get("text") or ""), str(decision.get("label_text") or ""))
        labeled_entries.append(entry)

    audits = [audits_by_batch[str(batch.get("batch_key") or batch.get("slot") or "unknown")] for batch in batches if str(batch.get("batch_key") or batch.get("slot") or "unknown") in audits_by_batch]
    return _prioritize_architecture_labeled_entries(labeled_entries), audits


def _component_entry_counts(entries: List[Dict[str, Any]]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for entry in entries:
        top_section = str(entry.get("top_section") or "").strip().lower()
        label_type = str(entry.get("architecture_label_type") or "none").strip().lower()
        label_text = str(entry.get("architecture_label") or "").strip()
        is_important = top_section in {"important", "important_changes"} or (
            top_section not in {"ordinary", "ordinary_changelog", "regular_changelog", "changelog"}
            and bool(label_text)
            and label_type not in {"", "none"}
        )
        if not is_important:
            continue
        component = str(entry.get("display_arch_component") or "").strip()
        assignment_type = str(entry.get("arch_component_assignment_type") or "").strip()
        if assignment_type in {"cross_cutting", "unknown"} or not component:
            component = "Cross-cutting / Other Architecture-related Changes"
        counts[component] = counts.get(component, 0) + 1
    return dict(sorted(counts.items()))


def _phase3_arch_label_llm_enabled(config) -> bool:
    if config is None:
        return False
    return bool(getattr(config, "phase3_arch_label_llm_enabled", True))


def _ensure_phase3_arch_label_llm_client(config, llm_client) -> None:
    if llm_client is not None:
        return
    env_var = str(getattr(config, "llm_api_key_env_var", "") or "").strip()
    if not env_var:
        raise RuntimeError("Phase 3.2.5 architecture label LLM is enabled, but config.llm_api_key_env_var is empty.")
    if not os.getenv(env_var):
        raise RuntimeError(f"Phase 3.2.5 architecture label LLM is enabled, but environment variable {env_var} is not set.")
    raise RuntimeError("Phase 3.2.5 architecture label LLM is enabled, but no OpenAI-compatible LLM client could be created.")


def _assign_label_entry_ids(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    seen: set[str] = set()
    indexed: List[Dict[str, Any]] = []
    for index, entry in enumerate(entries, start=1):
        candidate = str(entry.get("group_id") or "").strip()
        if not candidate or candidate in seen:
            candidate = f"ENTRY-{index:04d}"
        seen.add(candidate)
        indexed.append({"entry_id": candidate, "entry": entry})
    return indexed


def _label_batches_by_slot(indexed_entries: List[Dict[str, Any]], records: Dict[str, Dict[str, Any]], config=None) -> List[Dict[str, Any]]:
    by_slot: Dict[str, List[Dict[str, Any]]] = {}
    for item in indexed_entries:
        entry = item["entry"]
        slot = str(entry.get("slot") or "others")
        by_slot.setdefault(slot, []).append(_architecture_label_card(item["entry_id"], entry, records, config=config))
    batches: List[Dict[str, Any]] = []
    for slot, cards in by_slot.items():
        if not cards:
            continue
        chunk_size = _phase3_arch_label_entry_batch_size(config)
        chunk_count = (len(cards) + chunk_size - 1) // chunk_size
        for index in range(chunk_count):
            start = index * chunk_size
            end = start + chunk_size
            batch_key = slot if chunk_count == 1 else f"{slot}#chunk{index + 1:03d}"
            batches.append(
                {
                    "slot": slot,
                    "batch_key": batch_key,
                    "chunk_index": index + 1,
                    "chunk_count": chunk_count,
                    "cards": cards[start:end],
                }
            )
    return batches


def _architecture_label_card(entry_id: str, entry: Dict[str, Any], records: Dict[str, Dict[str, Any]], config=None) -> Dict[str, Any]:
    source_commits = [str(item) for item in entry.get("source_commits") or [] if str(item)]
    phase2_arch_relevance_available = _phase2_arch_relevance_available(config)
    return {
        "entry_id": entry_id,
        "slot": str(entry.get("slot") or ""),
        "entry_text": str(entry.get("text") or ""),
        "entry_style": str(entry.get("entry_style") or "full"),
        "release_note_value": str(entry.get("release_note_value") or "include"),
        "phase2_architecture_relevance_available": phase2_arch_relevance_available,
        "source_commits": [
            _source_commit_for_arch_label_prompt(
                commit_id,
                records.get(commit_id) or {},
                phase2_arch_relevance_available=phase2_arch_relevance_available,
            )
            for commit_id in source_commits
        ],
        "candidate_arch_events": _candidate_arch_events_for_entry(source_commits, records),
    }


def _source_commit_for_arch_label_prompt(
    commit_id: str,
    record: Dict[str, Any],
    *,
    phase2_arch_relevance_available: bool = True,
) -> Dict[str, Any]:
    phase2_fields = (
        {
            "architecture_relevance_score": record.get("architecture_relevance_score"),
            "architecture_relevance_level": str(record.get("architecture_relevance_level") or ""),
            "architecture_relevance_labels": [str(item) for item in record.get("architecture_relevance_labels") or [] if str(item)],
            "architecture_relevance_reason": str(record.get("architecture_relevance_reason") or ""),
            "structure_role": str(record.get("structure_role") or ""),
        }
        if phase2_arch_relevance_available
        else {
            "architecture_relevance_score": None,
            "architecture_relevance_level": "",
            "architecture_relevance_labels": [],
            "architecture_relevance_reason": "",
            "structure_role": "",
        }
    )
    return {
        "commit_id": commit_id,
        "commit_summary": str(record.get("commit_summary") or ""),
        "functional_category": str(record.get("functional_category") or ""),
        "evidence_granularity": str(record.get("evidence_granularity") or ""),
        "changed_files": [str(item) for item in (record.get("changed_files") or [])[:12]],
        "changed_methods": [str(item) for item in (record.get("changed_methods") or [])[:8]],
        **phase2_fields,
        "primary_module": str(record.get("primary_module") or ""),
        "primary_component": str(record.get("primary_component") or ""),
    }


def _phase2_arch_relevance_available(config) -> bool:
    if config is None:
        return True
    return str(getattr(config, "phase2_ablation_mode", "full") or "full").strip() != PHASE2_ABLATION_NO_ARCH_RELEVANCE


def _candidate_arch_events_for_entry(source_commits: List[str], records: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    candidates: Dict[str, Dict[str, Any]] = {}
    profile_cards: Dict[str, Dict[str, Any]] = {}
    changed_files_by_commit = {
        commit_id: [str(item) for item in (records.get(commit_id) or {}).get("changed_files") or []]
        for commit_id in source_commits
    }

    for commit_id in source_commits:
        record = records.get(commit_id) or {}
        for card in _record_matched_arch_event_cards(record):
            event_id = str(card.get("event_id") or "")
            if event_id:
                profile_cards.setdefault(event_id, card)

    for commit_id in source_commits:
        record = records.get(commit_id) or {}
        for attribution in record.get("event_attributions") or []:
            if not isinstance(attribution, dict):
                continue
            event_id = str(attribution.get("event_id") or "")
            if not event_id:
                continue
            profile_card = profile_cards.get(event_id) or {}
            changed_files = changed_files_by_commit.get(commit_id) or []
            if not _is_strong_arch_event_candidate(attribution, profile_card, changed_files):
                continue
            merged = candidates.setdefault(event_id, _arch_event_candidate_base(attribution, profile_card))
            merged["source_commit_ids"] = _unique(list(merged.get("source_commit_ids") or []) + [commit_id])
            merged["matching_facts"] = _unique(
                list(merged.get("matching_facts") or [])
                + _candidate_matching_facts(attribution, profile_card, changed_files, commit_id)
            )[:12]
            merged["posterior_hint"] = max(_safe_float(merged.get("posterior_hint")), _safe_float(attribution.get("posterior")))

    for commit_id in source_commits:
        record = records.get(commit_id) or {}
        for card in _record_matched_arch_event_cards(record):
            event_id = str(card.get("event_id") or "")
            if not event_id or event_id in candidates:
                continue
            if not _is_strong_profile_card_candidate(card, changed_files_by_commit.get(commit_id) or []):
                continue
            merged = candidates.setdefault(event_id, _arch_event_candidate_base({}, card))
            merged["source_commit_ids"] = _unique(list(merged.get("source_commit_ids") or []) + [commit_id])
            merged["matching_facts"] = _unique(
                list(merged.get("matching_facts") or [])
                + [str(item) for item in card.get("matching_facts") or [] if str(item)]
            )[:12]
            merged["posterior_hint"] = max(_safe_float(merged.get("posterior_hint")), _safe_float(card.get("posterior_hint")))

    ordered = sorted(
        candidates.values(),
        key=lambda item: (-_safe_float(item.get("posterior_hint")), str(item.get("event_id") or "")),
    )
    return ordered[:MAX_ARCH_LABEL_CANDIDATE_EVENTS]


def _record_matched_arch_event_cards(record: Dict[str, Any]) -> List[Dict[str, Any]]:
    evidence = record.get("architecture_evidence") or {}
    if isinstance(evidence, dict):
        return [item for item in evidence.get("matched_arch_events") or [] if isinstance(item, dict)]
    if isinstance(evidence, list):
        return [item for item in evidence if isinstance(item, dict)]
    return []


def _is_strong_arch_event_candidate(
    attribution: Dict[str, Any],
    profile_card: Dict[str, Any],
    changed_files: List[str],
) -> bool:
    evidence = attribution.get("evidence") if isinstance(attribution.get("evidence"), dict) else {}
    role = str(attribution.get("role_in_event") or "").lower()
    file_overlap = _safe_float(evidence.get("file_overlap"))
    operation_match = _safe_float(evidence.get("operation_match"))
    module_match = _safe_float(evidence.get("module_match"))
    component_match = _safe_float(evidence.get("component_match"))
    posterior = _safe_float(attribution.get("posterior"))
    if role in {"core", "support"}:
        return True
    if max(file_overlap, operation_match) >= 0.20:
        return True
    if module_match >= 1.0 and component_match >= 1.0 and posterior >= 0.02:
        return True
    return _paths_overlap(changed_files, [str(item) for item in profile_card.get("key_files") or []])


def _is_strong_profile_card_candidate(card: Dict[str, Any], changed_files: List[str]) -> bool:
    role = str(card.get("role_in_event") or "").lower()
    if role in {"core", "support"}:
        return True
    if _safe_float(card.get("posterior_hint")) >= 0.05:
        return True
    return _paths_overlap(changed_files, [str(item) for item in card.get("key_files") or []])


def _arch_event_candidate_base(attribution: Dict[str, Any], profile_card: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "event_id": str(profile_card.get("event_id") or attribution.get("event_id") or ""),
        "event_type": str(profile_card.get("event_type") or attribution.get("event_type") or ""),
        "module": str(profile_card.get("module") or attribution.get("module") or ""),
        "component": str(profile_card.get("component") or attribution.get("component") or ""),
        "key_files": [str(item) for item in (profile_card.get("key_files") or [])[:12]],
        "arch_event_profile": _compact_arch_event_profile(profile_card.get("arch_event_profile") or {}),
        "matching_facts": [],
        "source_commit_ids": [],
        "posterior_hint": _safe_float(profile_card.get("posterior_hint") or attribution.get("posterior")),
        "event_significance": profile_card.get("event_significance", attribution.get("event_significance")),
        "role_in_event": str(profile_card.get("role_in_event") or attribution.get("role_in_event") or ""),
    }


def _compact_arch_event_profile(profile: Any) -> Dict[str, Any]:
    if not isinstance(profile, dict):
        return {}
    compact: Dict[str, Any] = {}
    for key in ("what_changed", "affected_architecture_area"):
        text = _truncate_prompt_text(profile.get(key), MAX_ARCH_LABEL_PROFILE_TEXT_CHARS)
        if text:
            compact[key] = text
    important_files = [str(item) for item in profile.get("important_files") or [] if str(item)]
    if important_files:
        compact["important_files"] = important_files[:5]
    for key, limit in (("why_it_may_matter", 2), ("not_enough_evidence_cases", 1)):
        values = [
            _truncate_prompt_text(item, MAX_ARCH_LABEL_PROFILE_LIST_ITEM_CHARS)
            for item in profile.get(key) or []
            if str(item).strip()
        ]
        values = [item for item in values if item]
        if values:
            compact[key] = values[:limit]
    return compact


def _truncate_prompt_text(value: Any, limit: int) -> str:
    text = " ".join(str(value or "").split()).strip()
    if len(text) <= limit:
        return text
    return text[: max(0, limit - 16)].rstrip() + " ... [truncated]"


def _candidate_matching_facts(
    attribution: Dict[str, Any],
    profile_card: Dict[str, Any],
    changed_files: List[str],
    commit_id: str,
) -> List[str]:
    facts = [f"source commit {commit_id} matched this event"]
    role = str(attribution.get("role_in_event") or profile_card.get("role_in_event") or "")
    if role:
        facts.append(f"role_in_event={role}")
    evidence = attribution.get("evidence") if isinstance(attribution.get("evidence"), dict) else {}
    for key in ("file_overlap", "module_match", "component_match", "operation_match"):
        value = _safe_float(evidence.get(key))
        if value > 0:
            facts.append(f"{key}={value:.3f}")
    key_files = [str(item) for item in profile_card.get("key_files") or []]
    overlap = _overlapping_paths(changed_files, key_files)
    if overlap:
        facts.append(f"changed event key files: {', '.join(overlap[:5])}")
    for fact in profile_card.get("matching_facts") or []:
        if str(fact).strip():
            facts.append(str(fact).strip())
    return facts


def _paths_overlap(left: List[str], right: List[str]) -> bool:
    return bool(_overlapping_paths(left, right))


def _overlapping_paths(left: List[str], right: List[str]) -> List[str]:
    right_set = {_normalize_path_for_compare(path) for path in right if path}
    result = []
    for path in left:
        normalized = _normalize_path_for_compare(path)
        if normalized and normalized in right_set:
            result.append(str(path))
    return result


def _normalize_path_for_compare(path: str) -> str:
    return str(path or "").replace("\\", "/").strip().lower()


def _normalize_arch_label_decisions(parsed: Dict[str, Any], cards: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    raw_decisions = parsed.get("decisions")
    if not isinstance(raw_decisions, list):
        raise ValueError("Phase 3.2.5 response must contain a decisions list.")
    expected_ids = [str(card.get("entry_id") or "") for card in cards]
    candidate_event_ids_by_entry = {
        str(card.get("entry_id") or ""): {
            str(event.get("event_id") or "")
            for event in card.get("candidate_arch_events") or []
            if isinstance(event, dict) and str(event.get("event_id") or "")
        }
        for card in cards
    }
    seen: set[str] = set()
    decisions: List[Dict[str, Any]] = []
    for raw in raw_decisions:
        if not isinstance(raw, dict):
            raise ValueError("Each Phase 3.2.5 decision must be a JSON object.")
        raw_entry_id = str(raw.get("entry_id") or "")
        entry_id = _resolve_unique_near_identifier(raw_entry_id, {entry_id: {} for entry_id in expected_ids}, seen)
        if entry_id not in expected_ids:
            raise ValueError(f"Unknown entry_id in Phase 3.2.5 response: {entry_id}")
        if entry_id in seen:
            raise ValueError(f"Duplicate entry_id in Phase 3.2.5 response: {entry_id}")
        seen.add(entry_id)
        label_type = str(raw.get("label_type") or "").lower()
        if label_type not in {"arch_event", "arch_knowledge", "none"}:
            raise ValueError(f"Invalid label_type for entry_id {entry_id}: {label_type}")
        event_id = str(raw.get("event_id") or "").strip()
        label_text = _clean_label_text(raw.get("label_text"))
        reason = " ".join(str(raw.get("reason") or "").split()).strip()
        if label_type == "arch_event":
            if not event_id:
                raise ValueError(f"arch_event decision for entry_id {entry_id} must provide event_id.")
            if event_id not in candidate_event_ids_by_entry.get(entry_id, set()):
                raise ValueError(f"arch_event decision for entry_id {entry_id} uses non-candidate event_id: {event_id}")
            if not label_text:
                raise ValueError(f"arch_event decision for entry_id {entry_id} must provide label_text.")
            label_text = _ensure_label_prefix(label_text, "Architecture event")
        elif label_type == "arch_knowledge":
            if event_id:
                raise ValueError(f"arch_knowledge decision for entry_id {entry_id} must not provide event_id.")
            if not label_text:
                raise ValueError(f"arch_knowledge decision for entry_id {entry_id} must provide label_text.")
            label_text = _ensure_label_prefix(label_text, "Architecture relevance")
        else:
            event_id = ""
            label_text = ""
        if label_text and _contains_commit_hash(label_text):
            raise ValueError(f"Architecture label text contains commit hash for entry_id {entry_id}.")
        decisions.append(
            {
                "entry_id": entry_id,
                "label_type": label_type,
                "event_id": event_id,
                "label_text": label_text,
                "reason": reason,
            }
        )
    missing = [entry_id for entry_id in expected_ids if entry_id not in seen]
    if missing:
        raise ValueError(f"Phase 3.2.5 response missing entry_id decisions: {missing}")
    return decisions


def _clean_label_text(value: Any) -> str:
    text = " ".join(str(value or "").split()).strip()
    return text.strip("()() ")


def _ensure_label_prefix(label_text: str, prefix: str) -> str:
    if label_text.startswith("Architecture event:") or label_text.startswith("Architecture relevance:"):
        return label_text
    return f"{prefix}: {label_text}"


def _none_arch_label_decision(entry_id: str) -> Dict[str, Any]:
    return {"entry_id": entry_id, "label_type": "none", "event_id": "", "label_text": "", "reason": ""}


def _append_architecture_label(text: str, label_text: str) -> str:
    clean_text = str(text or "").strip()
    clean_label = _clean_label_text(label_text)
    if not clean_text or not clean_label:
        return clean_text
    if clean_text.endswith(f"({clean_label})"):
        return clean_text
    if "(Architecture event:" in clean_text or "(Architecture relevance:" in clean_text:
        return clean_text
    return f"{clean_text} ({clean_label})"


def _prioritize_architecture_labeled_entries(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Keep slot order stable while showing LLM-selected architecture labels first."""
    label_rank = {"arch_event": 0, "arch_knowledge": 1, "none": 2}
    slot_order: List[str] = []
    entries_by_slot: Dict[str, List[tuple[int, Dict[str, Any]]]] = {}
    for index, entry in enumerate(entries):
        slot = str(entry.get("slot") or "")
        if slot not in entries_by_slot:
            slot_order.append(slot)
            entries_by_slot[slot] = []
        entries_by_slot[slot].append((index, entry))

    ordered: List[Dict[str, Any]] = []
    for slot in slot_order:
        slot_entries = sorted(
            entries_by_slot[slot],
            key=lambda indexed_entry: (
                label_rank.get(str(indexed_entry[1].get("architecture_label_type") or "none"), 2),
                indexed_entry[0],
            ),
        )
        ordered.extend(entry for _index, entry in slot_entries)
    return ordered


def _raise_phase3_arch_label_failure(
    *,
    output_dir: Path,
    config,
    slot: str,
    batch_key: str,
    prompt_path: Path,
    user_prompt: str,
    raw: str,
    error_type: str,
    error_message: str,
    exception: BaseException,
    cards: List[Dict[str, Any]],
    parsed: Optional[Dict[str, Any]],
    validation_attempts: Optional[List[Dict[str, Any]]] = None,
) -> None:
    raise_phase3_llm_failure(
        output_dir=phase3_failure_output_dir(config, output_dir),
        stage="phase3.2.5_arch_label_decision",
        batch_or_bucket_or_slot=batch_key,
        error_type=error_type,
        error_message=error_message,
        exception=exception,
        prompt_template_path=str(prompt_path),
        rendered_prompt=user_prompt,
        raw_llm_response=raw,
        cleaned_response_if_any=(raw or "").strip(),
        parsed_json_if_any=parsed or {},
        input_summary={"slot": slot, "batch_key": batch_key, "entry_count": len(cards)},
        input_payload={"entries": cards},
        validation_attempts=validation_attempts or [],
    )


def _phase3_arch_label_error_type(exc: BaseException) -> str:
    message = str(exc)
    if "Unknown entry_id" in message or "Duplicate entry_id" in message or "missing entry_id" in message:
        return "entry_id_validation_error"
    if "event_id" in message:
        return "event_id_validation_error"
    if "label text" in message.lower() or "label_text" in message:
        return "label_text_validation_error"
    if "Expecting" in message or "JSON" in message or "json" in message:
        return "json_parse_error"
    return "schema_validation_error"


def _compose_fallback_text(group: Dict[str, Any], record: Dict[str, Any], slot: str) -> str:
    intent = str(group.get("entry_intent") or "").strip()
    module = str(record.get("primary_module") or "").strip()
    score = float(record.get("architecture_relevance_score") or 0.0)
    if slot.startswith("architecture_changes") and module and score >= 0.65:
        return f"{module}: {intent}"
    if module and score >= 0.35 and not slot.startswith("non_functional_changes.documentation"):
        return f"{intent} (module context: {module})"
    return intent or "Aggregate changes supported by source commits."


def _group_confidence(evidence: List[Dict[str, Any]]) -> str:
    if any(item.get("confidence") == "high" for item in evidence):
        return "high"
    if any(item.get("confidence") == "medium" for item in evidence):
        return "medium"
    return "low"


def _normalize_entries(slot: str, raw_entries: Any, groups: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    valid_commits = {str(commit) for group in groups for commit in group.get("source_commits") or []}
    group_by_commit = _group_lookup(groups)
    if not isinstance(raw_entries, list):
        return []
    entries = []
    for raw in raw_entries:
        if not isinstance(raw, dict):
            continue
        source_commits = _resolve_commit_ids(raw.get("source_commits") or [], valid_commits)
        text = " ".join(str(raw.get("text") or "").split()).strip()
        if not source_commits or not text:
            continue
        confidence = str(raw.get("confidence") or "medium").lower()
        if confidence not in {"high", "medium", "low"}:
            confidence = "medium"
        related_arch_events = _related_events_for_entry(source_commits, group_by_commit)
        first_group = group_by_commit.get(source_commits[0], {}) if source_commits else {}
        entries.append(
            {
                "slot": slot,
                "text": text,
                "source_commits": source_commits,
                "related_arch_events": related_arch_events,
                "confidence": confidence,
                "entry_style": first_group.get("entry_style") or "full",
                "release_note_value": first_group.get("release_note_value") or "include",
            }
        )
    return entries


def _parse_entries_response(raw_text: str, slot: str, groups: List[Dict[str, Any]], *, debug: bool = False) -> List[Dict[str, Any]]:
    if debug:
        parsed = _parse_json_strict(raw_text)
        return _normalize_minimal_entries(slot, parsed.get("entries"), groups)
    try:
        parsed = parse_json_response(raw_text)
        entries = _normalize_minimal_entries(slot, parsed.get("entries"), groups)
        if entries:
            return entries
        entries = _normalize_entries(slot, parsed.get("entries"), groups)
        if entries:
            return entries
    except Exception:
        pass
    return _parse_entry_blocks_to_entries(raw_text, slot, groups)


def _parse_json_strict(raw_text: str) -> Dict[str, Any]:
    return parse_json_response_strict(raw_text)


def _normalize_minimal_entries(slot: str, raw_entries: Any, groups: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    if not isinstance(raw_entries, list):
        raise ValueError("entries must be a list.")
    group_by_id = {str(group.get("group_id") or ""): group for group in groups if str(group.get("group_id") or "")}
    seen: set[str] = set()
    entries: List[Dict[str, Any]] = []
    for raw in raw_entries:
        if not isinstance(raw, dict):
            raise ValueError("entries must contain JSON objects.")
        raw_group_id = str(raw.get("group_id") or "")
        group_id = _resolve_unique_near_identifier(raw_group_id, group_by_id, seen)
        if group_id not in group_by_id:
            raise ValueError(f"Unknown group_id in Phase 3.2 response: {group_id}")
        if group_id in seen:
            raise ValueError(f"Duplicate group_id in Phase 3.2 response: {group_id}")
        text = " ".join(str(raw.get("text") or "").split()).strip()
        if not text:
            raise ValueError(f"Empty text for group_id {group_id}")
        if _contains_cjk(text):
            raise ValueError(f"Entry text must be English for group_id {group_id}")
        if _contains_commit_hash(text):
            raise ValueError(f"Entry text contains commit hash for group_id {group_id}")
        if _contains_machine_field_name(text):
            raise ValueError(f"Entry text contains machine field name for group_id {group_id}")
        confidence = str(raw.get("confidence") or "medium").lower()
        if confidence not in {"high", "medium", "low"}:
            raise ValueError(f"Invalid confidence for group_id {group_id}: {confidence}")
        group = group_by_id[group_id]
        source_commits = [str(item) for item in group.get("source_commits") or [] if str(item)]
        if not source_commits:
            raise ValueError(f"Group {group_id} has no source_commits.")
        entries.append(
            {
                "group_id": group_id,
                "slot": group.get("slot") or slot,
                "text": text,
                "source_commits": source_commits,
                "related_arch_events": [str(item) for item in group.get("related_arch_events") or [] if str(item)],
                "confidence": confidence,
                "entry_style": group.get("entry_style") or "full",
                "release_note_value": group.get("release_note_value") or "include",
                "traceability": group.get("traceability") or {},
            }
        )
        seen.add(group_id)
    missing = [group_id for group_id in group_by_id if group_id not in seen]
    if missing:
        raise ValueError(f"Phase 3.2 response missing group_id entries: {missing}")
    return entries


def _resolve_unique_near_identifier(raw_id: str, valid_ids: Dict[str, Dict[str, Any]], seen: set[str]) -> str:
    group_id = str(raw_id or "").strip()
    if group_id in valid_ids:
        return group_id

    head, sep, suffix = group_id.rpartition("_")
    if not sep or len(suffix) < 6:
        return group_id

    candidates: List[str] = []
    for candidate in valid_ids:
        if candidate in seen:
            continue
        candidate_head, candidate_sep, candidate_suffix = candidate.rpartition("_")
        if not candidate_sep or candidate_head != head:
            continue
        if _similar_short_group_suffix(suffix, candidate_suffix):
            candidates.append(candidate)
    if len(candidates) == 1:
        return candidates[0]

    if _is_short_hash_suffix(suffix):
        exact_suffix_candidates = []
        for candidate in valid_ids:
            if candidate in seen:
                continue
            _candidate_head, candidate_sep, candidate_suffix = candidate.rpartition("_")
            if candidate_sep and candidate_suffix.lower() == suffix.lower():
                exact_suffix_candidates.append(candidate)
        if len(exact_suffix_candidates) == 1:
            return exact_suffix_candidates[0]
    return group_id


def _is_short_hash_suffix(value: str) -> bool:
    value = str(value or "").strip()
    return len(value) >= 7 and all(char in "0123456789abcdefABCDEF" for char in value)


def _similar_short_group_suffix(observed: str, expected: str) -> bool:
    observed = observed.strip()
    expected = expected.strip()
    if len(observed) < 6 or len(expected) < 6:
        return False
    if abs(len(observed) - len(expected)) > 1:
        return False
    if sorted(observed) == sorted(expected):
        return True
    return _bounded_edit_distance(observed, expected, limit=1) <= 1


def _bounded_edit_distance(left: str, right: str, *, limit: int) -> int:
    if abs(len(left) - len(right)) > limit:
        return limit + 1
    previous = list(range(len(right) + 1))
    for i, left_char in enumerate(left, start=1):
        current = [i]
        row_min = current[0]
        for j, right_char in enumerate(right, start=1):
            cost = 0 if left_char == right_char else 1
            value = min(previous[j] + 1, current[j - 1] + 1, previous[j - 1] + cost)
            current.append(value)
            row_min = min(row_min, value)
        if row_min > limit:
            return limit + 1
        previous = current
    return previous[-1]


def _contains_commit_hash(text: str) -> bool:
    for match in re.finditer(r"\b[0-9a-f]{7,40}\b", text or ""):
        token = match.group(0)
        if not token.isdigit() and token.lower() not in _NON_COMMIT_HEX_LIKE_TOKENS:
            return True
    return False


def _contains_cjk(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text or ""))


def _contains_machine_field_name(text: str) -> bool:
    return bool(
        re.search(
            r"\b(source_commits|confidence|related_arch_events|traceability|group_id)\b",
            text or "",
            flags=re.IGNORECASE,
        )
    )


def _parse_entry_blocks_to_entries(raw_text: str, slot: str, groups: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    valid_commits = {str(commit) for group in groups for commit in group.get("source_commits") or []}
    group_by_commit = _group_lookup(groups)
    entries: List[Dict[str, Any]] = []
    for block in re.findall(r"\[ENTRY\](.*?)\[/ENTRY\]", raw_text or "", flags=re.IGNORECASE | re.DOTALL):
        fields = _parse_block_fields(block)
        source_commits = _resolve_commit_ids(fields.get("source_commits") or "", valid_commits)
        text = " ".join(str(fields.get("text") or "").split()).strip()
        confidence = str(fields.get("confidence") or "medium").strip().lower()
        if confidence not in {"high", "medium", "low"}:
            confidence = "medium"
        if not source_commits or not text:
            continue
        first_group = group_by_commit.get(source_commits[0], {}) if source_commits else {}
        entries.append(
            {
                "slot": slot,
                "text": text,
                "source_commits": source_commits,
                "related_arch_events": _related_events_for_entry(source_commits, group_by_commit),
                "confidence": confidence,
                "entry_style": first_group.get("entry_style") or "full",
                "release_note_value": first_group.get("release_note_value") or "include",
            }
        )
    return entries


def _parse_block_fields(block: str) -> Dict[str, str]:
    fields: Dict[str, str] = {}
    current_key: Optional[str] = None
    for raw_line in block.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            current_key = key.strip().lower()
            fields[current_key] = value.strip()
        elif current_key:
            fields[current_key] = (fields[current_key] + " " + line).strip()
    return fields


def _split_values(value: Any) -> List[str]:
    if isinstance(value, list):
        raw_values = value
    else:
        raw_values = re.split(r"[,，\s]+", str(value or ""))
    return [str(item).strip() for item in raw_values if str(item).strip()]


def _resolve_commit_ids(values: Any, valid_commits: set[str]) -> List[str]:
    resolved: List[str] = []
    seen = set()
    for value in _split_values(values):
        commit_id = value if value in valid_commits else _resolve_commit_prefix(value, valid_commits)
        if not commit_id or commit_id in seen:
            continue
        resolved.append(commit_id)
        seen.add(commit_id)
    return resolved


def _resolve_commit_prefix(value: str, valid_commits: set[str]) -> str:
    if not value:
        return ""
    matches = [commit_id for commit_id in valid_commits if commit_id.startswith(value)]
    return matches[0] if len(matches) == 1 else ""


def _evidence_for_groups(groups: List[Dict[str, Any]], records: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    selected = []
    for group in groups:
        for commit_id in group.get("source_commits") or []:
            record = records.get(str(commit_id))
            if not record:
                continue
            selected.append(
                {
                    "commit_id": record.get("commit_id"),
                    "commit_summary": record.get("commit_summary"),
                    "functional_category": record.get("functional_category"),
                    "evidence_granularity": record.get("evidence_granularity"),
                    "change_detection_status": record.get("change_detection_status"),
                    "changed_files": record.get("changed_files"),
                    "changed_methods": record.get("changed_methods"),
                    "diff_hunks": (record.get("diff_hunks") or [])[:3],
                    "architecture_relevance_score": record.get("architecture_relevance_score"),
                    "architecture_relevance_level": record.get("architecture_relevance_level"),
                    "architecture_relevance_labels": record.get("architecture_relevance_labels"),
                    "architecture_relevance_reason": record.get("architecture_relevance_reason"),
                    "structure_role": record.get("structure_role"),
                    "primary_module": record.get("primary_module"),
                    "primary_component": record.get("primary_component"),
                    "architecture_evidence": record.get("architecture_evidence"),
                }
            )
    return selected


def _low_priority_groups_for_slot(
    plan: Dict[str, Any],
    slot: str,
    records: Dict[str, Dict[str, Any]],
) -> List[Dict[str, Any]]:
    by_reason: Dict[tuple[str, str], List[Dict[str, Any]]] = {}
    for release_note_value, key in (("deprioritize", "deprioritized_commits"), ("filter", "filtered_commits")):
        for item in plan.get(key) or []:
            if not isinstance(item, dict):
                continue
            suggested_slot = _suggested_slot_for_low_priority_item(item, release_note_value)
            if suggested_slot != slot:
                continue
            reason_code = str(item.get("reason_code") or "chore")
            by_reason.setdefault((release_note_value, reason_code), []).append(item)

    groups: List[Dict[str, Any]] = []
    for (release_note_value, reason_code), items in by_reason.items():
        source_commits = [str(item.get("commit_id") or "") for item in items if str(item.get("commit_id") or "")]
        if not source_commits:
            continue
        groups.append(
            {
                "group_id": f"low_priority_{slot.replace('.', '_')}_{release_note_value}_{reason_code}",
                "slot": slot,
                "entry_intent": _low_priority_intent(release_note_value, reason_code, len(source_commits)),
                "source_commits": source_commits,
                "related_arch_events": [],
                "primary_module": "",
                "primary_component": "",
                "aggregation_reason": "Aggregate low-priority commits into a brief entry.",
                "traceability": _entry_traceability(source_commits, records),
                "entry_style": "brief",
                "release_note_value": release_note_value,
                "priority_origin": "low_priority_backfill",
                "low_priority_reason_codes": [reason_code],
            }
        )
    return groups


def _suggested_slot_for_low_priority_item(item: Dict[str, Any], release_note_value: str) -> str:
    if release_note_value == "filter":
        return "others"
    suggested = str(item.get("suggested_slot") or "")
    if suggested:
        return suggested
    reason_code = str(item.get("reason_code") or "")
    if reason_code in {"docs_only", "trivial_docs_only"}:
        return "non_functional_changes.documentation"
    if reason_code in {
        "ci_only",
        "dependency_maintenance",
        "chore",
        "minor_maintenance",
        "formatting_only",
        "comments_only",
        "typo_only",
        "lockfile_only",
        "generated_only",
        "version_bump_only",
        "metadata_only",
    }:
        return "non_functional_changes.maintenance"
    if reason_code == "internal_refactoring":
        return "functional_changes.refactorings"
    return "others"


def _low_priority_intent(release_note_value: str, reason_code: str, count: int) -> str:
    labels = {
        "internal_refactoring": "Briefly describe internal refactoring.",
        "tests_only": "Briefly describe test maintenance.",
        "docs_only": "Briefly describe documentation maintenance.",
        "ci_only": "Briefly describe CI maintenance.",
        "dependency_maintenance": "Briefly describe dependency maintenance.",
        "chore": "Briefly describe routine maintenance.",
        "minor_maintenance": "Briefly describe minor maintenance.",
        "formatting_only": "Briefly describe formatting cleanup.",
        "typo_only": "Briefly describe spelling fixes.",
        "comments_only": "Briefly describe comment maintenance.",
        "lockfile_only": "Briefly describe lockfile maintenance.",
        "generated_only": "Briefly describe generated-file maintenance.",
        "version_bump_only": "Briefly describe version metadata maintenance.",
        "metadata_only": "Briefly describe metadata maintenance.",
        "duplicate_merge_commit": "Briefly describe merge or synchronization maintenance.",
        "trivial_docs_only": "Briefly describe minor documentation fixes.",
    }
    value_label = "filtered low-priority" if release_note_value == "filter" else "deprioritized"
    return f"{labels.get(reason_code, 'Briefly describe low-priority maintenance.')} ({count} {value_label} commits)."


def _attach_entries_traceability(
    entries: List[Dict[str, Any]],
    records: Dict[str, Dict[str, Any]],
) -> List[Dict[str, Any]]:
    normalized: List[Dict[str, Any]] = []
    for entry in entries:
        source_commits = [str(item) for item in entry.get("source_commits") or [] if str(item)]
        next_entry = dict(entry)
        next_entry["source_commits"] = source_commits
        next_entry.setdefault("related_arch_events", _related_events_from_records(source_commits, records))
        next_entry.setdefault("entry_style", "full")
        next_entry.setdefault("release_note_value", "include")
        next_entry["traceability"] = _entry_traceability(source_commits, records)
        normalized.append(next_entry)
    return normalized


def _entry_traceability(source_commits: List[str], records: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    return {
        "source_commit_count": len(source_commits),
        "source_commits": [
            {
                "commit_id": commit_id,
                "commit_url": str(records.get(commit_id, {}).get("commit_url") or ""),
                "pull_requests": [
                    dict(item)
                    for item in records.get(commit_id, {}).get("pull_requests") or []
                    if isinstance(item, dict) and item.get("number") and item.get("url")
                ],
                "commit_message": str(records.get(commit_id, {}).get("commit_message") or ""),
                "commit_summary": str(records.get(commit_id, {}).get("commit_summary") or ""),
                "evidence_granularity": str(records.get(commit_id, {}).get("evidence_granularity") or ""),
                "architecture_relevance_score": records.get(commit_id, {}).get("architecture_relevance_score"),
                "architecture_relevance_level": str(records.get(commit_id, {}).get("architecture_relevance_level") or ""),
                "architecture_relevance_labels": records.get(commit_id, {}).get("architecture_relevance_labels") or [],
                "architecture_relevance_reason": str(records.get(commit_id, {}).get("architecture_relevance_reason") or ""),
            }
            for commit_id in source_commits
        ],
    }


def _group_lookup(groups: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    lookup: Dict[str, Dict[str, Any]] = {}
    for group in groups:
        if not isinstance(group, dict):
            continue
        for commit_id in group.get("source_commits") or []:
            lookup[str(commit_id)] = group
    return lookup


def _related_events_for_entry(source_commits: List[str], group_by_commit: Dict[str, Dict[str, Any]]) -> List[str]:
    events: List[str] = []
    for commit_id in source_commits:
        group = group_by_commit.get(commit_id) or {}
        events.extend([str(item) for item in group.get("related_arch_events") or [] if str(item)])
    return _unique(events)


def _related_events_from_records(source_commits: List[str], records: Dict[str, Dict[str, Any]]) -> List[str]:
    events: List[str] = []
    for commit_id in source_commits:
        record = records.get(commit_id) or {}
        events.extend([str(item) for item in record.get("matched_arch_events") or [] if str(item)])
        architecture_evidence = record.get("architecture_evidence") or {}
        if isinstance(architecture_evidence, dict):
            events.extend([str(item) for item in architecture_evidence.get("matched_arch_event_ids") or [] if str(item)])
            for evidence in architecture_evidence.get("matched_arch_events") or []:
                if isinstance(evidence, dict) and evidence.get("event_id"):
                    events.append(str(evidence.get("event_id")))
        elif isinstance(architecture_evidence, list):
            for evidence in architecture_evidence:
                if isinstance(evidence, dict) and evidence.get("event_id"):
                    events.append(str(evidence.get("event_id")))
    return _unique(events)


def _safe_float(value: Any) -> float:
    try:
        result = float(value)
    except Exception:
        return 0.0
    return result if result == result else 0.0


def _unique(values: List[str]) -> List[str]:
    result: List[str] = []
    seen = set()
    for value in values:
        if value and value not in seen:
            result.append(value)
            seen.add(value)
    return result


def _get_slot(plan: Dict[str, Any], slot: str) -> Any:
    target: Any = plan
    for part in slot.split("."):
        if not isinstance(target, dict):
            return None
        target = target.get(part)
    return target


def _export(
    output: Dict[str, Any],
    audits: List[Dict[str, Any]],
    label_audits: List[Dict[str, Any]],
    component_assignment_audits: List[Dict[str, Any]],
    component_catalog: Dict[str, Any],
    output_dir: Path,
) -> Dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / "section_entries.json"
    debug_path = output_dir / "section_entries_debug.md"
    audit_path = output_dir / "phase3_slot_entry_llm_audit.json"
    label_audit_path = output_dir / "phase3_arch_label_llm_audit.json"
    component_catalog_path = output_dir / "architecture_module_catalog.json"
    component_assignment_audit_path = output_dir / "phase3_arch_module_assignment_llm_audit.json"
    _write_json(path, output)
    _write_json(audit_path, {"generated_at": output["generated_at"], "records": audits})
    _write_json(label_audit_path, {"generated_at": output["generated_at"], "records": label_audits})
    _write_json(component_catalog_path, component_catalog)
    _write_json(component_assignment_audit_path, {"generated_at": output["generated_at"], "records": component_assignment_audits})
    debug_path.write_text(_render_debug(output, audits), encoding="utf-8")
    llm_io_path = export_slot_entry_llm_io(audits, llm_io_dir(output_dir))
    label_llm_io_path = export_arch_label_llm_io(label_audits, llm_io_dir(output_dir))
    component_assignment_llm_io_path = export_arch_module_assignment_llm_io(component_assignment_audits, llm_io_dir(output_dir))
    return {
        "section_entries": str(path),
        "section_entries_debug": str(debug_path),
        "phase3_slot_entry_llm_audit": str(audit_path),
        "phase3_arch_label_llm_audit": str(label_audit_path),
        "architecture_module_catalog": str(component_catalog_path),
        "phase3_arch_module_assignment_llm_audit": str(component_assignment_audit_path),
        **({"phase3_2_llm_input_output_txt": llm_io_path} if llm_io_path else {}),
        **({"phase3_2_arch_label_llm_input_output_txt": label_llm_io_path} if label_llm_io_path else {}),
        **({"phase3_2_arch_module_assignment_llm_input_output_txt": component_assignment_llm_io_path} if component_assignment_llm_io_path else {}),
    }


def _render_debug(output: Dict[str, Any], audits: List[Dict[str, Any]]) -> str:
    return "\n".join(
        [
            "# Phase 3.2 Slot Entry Debug",
            "",
            f"- generation_mode: `{output['stats']['generation_mode']}`",
            f"- entry_count: `{output['stats']['entry_count']}`",
            f"- llm_used_slot_count: `{output['stats']['llm_used_slot_count']}`",
            f"- arch_label_llm_used_slot_count: `{output['stats'].get('arch_label_llm_used_slot_count', 0)}`",
            f"- arch_module_assignment_llm_call_count: `{output['stats'].get('arch_module_assignment_llm_call_count', 0)}`",
            f"- architecture_labeled_entry_count: `{output['stats'].get('architecture_labeled_entry_count', 0)}`",
            f"- component_count: `{output['stats'].get('component_count', 0)}`",
            f"- unknown_count: `{output['stats'].get('unknown_count', 0)}`",
            f"- cross_cutting_count: `{output['stats'].get('cross_cutting_count', 0)}`",
            f"- slots_attempted: `{len(audits)}`",
            "",
        ]
    )


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _phase3_slot_concurrency(config, job_count: int) -> int:
    if config is None:
        return 1
    configured = getattr(config, "phase3_slot_concurrency", None)
    if configured is None:
        configured = getattr(config, "step10_concurrency", 4)
    try:
        return max(1, min(job_count, int(configured)))
    except Exception:
        return min(job_count, 4)


def _phase3_slot_entry_group_batch_size(config) -> int:
    if config is None:
        return 40
    configured = getattr(config, "phase3_slot_entry_group_batch_size", 40)
    try:
        return max(1, int(configured))
    except Exception:
        return 40


def _phase3_arch_label_entry_batch_size(config) -> int:
    if config is None:
        return 40
    configured = getattr(config, "phase3_arch_label_entry_batch_size", 40)
    try:
        return max(1, int(configured))
    except Exception:
        return 40


def _phase3_arch_label_concurrency(config, job_count: int) -> int:
    if config is None:
        return 1
    configured = getattr(config, "phase3_arch_label_concurrency", None)
    if configured is None:
        configured = getattr(config, "step10_concurrency", 4)
    try:
        return max(1, min(job_count, int(configured)))
    except Exception:
        return min(job_count, 4)


def _retry_prompt(user_prompt: str, attempt: int, error: Optional[BaseException] = None) -> str:
    if attempt <= 1:
        return user_prompt
    return (
        user_prompt
        + "\n\nNote: the previous output failed entry validation: "
        + str(error or "output format or coverage relation error")[:500]
        + ". Regenerate from the same input, return only valid JSON, and ensure each input group_id has exactly one entry."
    )


def _arch_label_retry_prompt(user_prompt: str, attempt: int, error: Optional[BaseException] = None) -> str:
    if attempt <= 1:
        return user_prompt
    return (
        user_prompt
        + "\n\nNote: the previous output failed label validation: "
        + str(error or "output format or entry_id coverage error")[:500]
        + ". Regenerate from the same input and return only valid JSON. Each input entry_id must appear exactly once in decisions."
    )
