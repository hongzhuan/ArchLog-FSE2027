from __future__ import annotations

import json
import os
import re
from collections import Counter, defaultdict, deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

from arcrn_metrics import mark_llm_metric_attempt, normalize_llm_metrics
from arcrn_stages.llm_utils import (
    TokenBucketRateLimiter,
    generate_chat_completion_with_retry,
    llm_output_validation_max_retries,
    load_prompt_text,
    parse_json_response_strict,
    progress_bar_for,
    render_prompt_template,
    resolve_prompt_path,
    suppress_noisy_llm_loggers,
    to_compact_json,
)
from phase3_llm_debug import phase3_debug_fail_fast, phase3_failure_output_dir, raise_phase3_llm_failure


DEFAULT_PROMPT = Path(__file__).resolve().parent / "prompts" / "phase3_2_arch_module_assignment_prompt.txt"
CROSS_CUTTING_TITLE = "Cross-cutting / Other Architecture-related Changes"
GENERIC_COMPONENT_KEYWORDS = {
    "a",
    "an",
    "and",
    "as",
    "at",
    "by",
    "for",
    "from",
    "in",
    "into",
    "of",
    "on",
    "or",
    "the",
    "to",
    "with",
    "without",
    "action",
    "actions",
    "common",
    "component",
    "components",
    "core",
    "data",
    "execution",
    "filter",
    "filters",
    "framework",
    "hardware",
    "input",
    "layer",
    "layers",
    "management",
    "mode",
    "module",
    "modules",
    "output",
    "service",
    "services",
    "software",
    "system",
    "systems",
}
GENERIC_PATH_PREFIXES = {
    "app",
    "apps",
    "drivers",
    "drivers/bus",
    "drivers/common",
    "drivers/compress",
    "drivers/crypto",
    "drivers/event",
    "drivers/gpu",
    "drivers/net",
    "drivers/power",
    "drivers/raw",
    "examples",
    "lib",
    "test",
    "tests",
}


def assign_architecture_components_to_entries(
    *,
    entries: List[Dict[str, Any]],
    records: Dict[str, Dict[str, Any]],
    llm_client,
    rate_limiter: TokenBucketRateLimiter,
    config,
    output_dir: Path,
) -> tuple[List[Dict[str, Any]], Dict[str, Any], List[Dict[str, Any]]]:
    catalog = build_architecture_module_catalog(config)
    if not _phase3_arch_module_assignment_enabled(config):
        return entries, catalog, []

    indexed = _architecture_labeled_entries(entries)
    if not indexed:
        return entries, catalog, []
    _ensure_llm_client(config, llm_client)

    cards = [
        _assignment_card(item["entry_id"], item["entry"], records, catalog)
        for item in indexed
    ]
    batches = _assignment_batches(cards, config)
    prompt_path = resolve_prompt_path(config, "phase3_arch_module_assignment_prompt_path", DEFAULT_PROMPT)
    prompt_template = load_prompt_text(prompt_path)
    max_workers = _phase3_arch_module_assignment_concurrency(config, len(batches))
    progress_bar = progress_bar_for(config, "Phase3.2.6 architecture component assignment progress") if batches else None
    if progress_bar is not None:
        progress_bar.update(completed=0, total=len(batches))

    decisions_by_id: Dict[str, Dict[str, Any]] = {}
    audits: List[Dict[str, Any]] = []
    try:
        with suppress_noisy_llm_loggers(enabled=progress_bar is not None):
            if max_workers <= 1:
                for completed, batch in enumerate(batches, start=1):
                    decisions, audit = _run_assignment_batch(
                        batch=batch,
                        prompt_template=prompt_template,
                        prompt_path=prompt_path,
                        llm_client=llm_client,
                        rate_limiter=rate_limiter,
                        config=config,
                        output_dir=output_dir,
                    )
                    audits.append(audit)
                    for decision in decisions:
                        decisions_by_id[str(decision.get("entry_id") or "")] = decision
                    if progress_bar is not None:
                        progress_bar.update(completed=completed, total=len(batches))
            else:
                with ThreadPoolExecutor(max_workers=max_workers) as executor:
                    futures = {
                        executor.submit(
                            _run_assignment_batch,
                            batch=batch,
                            prompt_template=prompt_template,
                            prompt_path=prompt_path,
                            llm_client=llm_client,
                            rate_limiter=rate_limiter,
                            config=config,
                            output_dir=output_dir,
                        ): batch
                        for batch in batches
                    }
                    completed = 0
                    for future in as_completed(futures):
                        decisions, audit = future.result()
                        audits.append(audit)
                        for decision in decisions:
                            decisions_by_id[str(decision.get("entry_id") or "")] = decision
                        completed += 1
                        if progress_bar is not None:
                            progress_bar.update(completed=completed, total=len(batches))
    finally:
        if progress_bar is not None:
            progress_bar.finish()

    for item in indexed:
        entry = item["entry"]
        entry_id = item["entry_id"]
        decision = decisions_by_id.get(entry_id) or _unknown_decision(entry_id)
        entry["entry_id"] = entry_id
        entry["arch_component_assignment_type"] = decision.get("assignment_type") or "unknown"
        entry["display_arch_component"] = decision.get("display_arch_component") or ""
        entry["arch_component_assignment_reason"] = decision.get("reason") or ""

    return entries, catalog, audits


def build_architecture_module_catalog(config) -> Dict[str, Any]:
    paths = _semarc_paths(config)
    named = _load_json(paths["namedclusters"]) if paths["namedclusters"].exists() else {}
    cluster_component = _load_json(paths["clustercomponent"]) if paths["clustercomponent"].exists() else {}
    archsem = _load_json(paths["archsem"]) if paths["archsem"].exists() else {}

    cluster_files = _cluster_files(named)
    arch_descriptions = _archsem_descriptions(archsem)
    components = _components_from_clustercomponent(cluster_component, cluster_files, arch_descriptions)
    source_priority = ["ClusterComponent", "ArchSem", "NamedClusters"]
    if not components:
        components = _components_from_archsem(arch_descriptions)
        source_priority = ["ArchSem", "NamedClusters"]
    if not components:
        components = _components_from_namedclusters(cluster_files)
        source_priority = ["NamedClusters"]

    return {
        "schema_version": 1,
        "catalog_granularity": "component",
        "source_priority": source_priority,
        "source_files": {key: str(value) for key, value in paths.items()},
        "components": components,
        "stats": {
            "component_count": len(components),
            "cluster_count": len(cluster_files),
        },
    }


def _run_assignment_batch(
    *,
    batch: Dict[str, Any],
    prompt_template: str,
    prompt_path: Path,
    llm_client,
    rate_limiter: TokenBucketRateLimiter,
    config,
    output_dir: Path,
) -> tuple[List[Dict[str, Any]], Dict[str, Any]]:
    system_prompt = "You assign already-written release-note entries to architecture components. Return only JSON."
    user_prompt = render_prompt_template(prompt_template, {"entries_json": to_compact_json(batch["cards"])})
    audit = {
        "llm_used": True,
        "batch_key": batch["batch_key"],
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
        "raw_response": None,
        "error_message": None,
        "attempts": [],
    }
    last_error: Optional[BaseException] = None
    max_attempts = 1 + llm_output_validation_max_retries(config)
    for attempt in range(1, max_attempts + 1):
        raw = None
        llm_metrics: Dict[str, Any] = {}
        try:
            raw, llm_metrics = generate_chat_completion_with_retry(
                config=config,
                llm_client=llm_client,
                system_prompt=system_prompt,
                user_prompt=_retry_prompt(user_prompt, attempt, last_error),
                request_name=f"phase3.2.6:arch_component_assignment:{batch['batch_key']}:attempt{attempt}",
                rate_limiter=rate_limiter,
            )
            llm_metrics = mark_llm_metric_attempt(
                normalize_llm_metrics(llm_metrics),
                validation_attempt_count=attempt,
                is_validation_retry=attempt > 1,
            )
            parsed = parse_json_response_strict(raw)
            decisions = _normalize_assignment_decisions(parsed, batch["cards"])
            audit["attempts"].append({"attempt": attempt, "ok": True, "raw_response": raw, "llm_metrics": llm_metrics})
            audit.update({"raw_response": raw, "error_message": None})
            return decisions, audit
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
    audit["error_message"] = str(last_error or "Unknown architecture component assignment failure")
    _raise_assignment_failure(
        config=config,
        output_dir=output_dir,
        batch_key=batch["batch_key"],
        prompt_path=prompt_path,
        rendered_prompt=_retry_prompt(user_prompt, max_attempts, last_error),
        raw_response=str((audit["attempts"][-1] if audit["attempts"] else {}).get("raw_response") or ""),
        validation_attempts=audit["attempts"],
        error=last_error,
        input_payload={"entries": batch["cards"]},
    )


def _assignment_card(
    entry_id: str,
    entry: Dict[str, Any],
    records: Dict[str, Dict[str, Any]],
    catalog: Dict[str, Any],
) -> Dict[str, Any]:
    source_commits = [str(item) for item in entry.get("source_commits") or [] if str(item)]
    source_records = [records.get(commit_id) or {} for commit_id in source_commits]
    commit_summaries = _unique(
        str(record.get("commit_summary") or "").strip()
        for record in source_records
        if str(record.get("commit_summary") or "").strip()
    )[:3]
    changed_files = _unique(
        str(path)
        for record in source_records
        for path in (record.get("changed_files") or [])
        if str(path)
    )[:8]
    changed_methods = _unique(
        str(item)
        for record in source_records
        for item in (record.get("changed_methods") or [])
        if str(item)
    )[:5]
    candidates = _candidate_components_for_entry(entry, source_records, catalog)
    return {
        "entry_id": entry_id,
        "entry_text": str(entry.get("text") or ""),
        "slot": str(entry.get("slot") or ""),
        "architecture_label": str(entry.get("architecture_label") or ""),
        "commit_summary_hints": commit_summaries,
        "changed_file_hints": changed_files,
        "changed_method_hints": changed_methods,
        "candidate_components": candidates,
    }


def _candidate_components_for_entry(
    entry: Dict[str, Any],
    source_records: List[Dict[str, Any]],
    catalog: Dict[str, Any],
) -> List[Dict[str, Any]]:
    text_blob = " ".join(
        [
            str(entry.get("text") or ""),
            " ".join(str(record.get("commit_summary") or "") for record in source_records),
            " ".join(str(record.get("architecture_relevance_reason") or "") for record in source_records),
        ]
    ).lower()
    changed_files = _unique(
        _normalize_path(path)
        for record in source_records
        for path in (record.get("changed_files") or [])
        if str(path)
    )
    changed_path_blob = " ".join(changed_files).lower()
    primary_components = {
        _normalize_text(record.get("primary_component"))
        for record in source_records
        if str(record.get("primary_component") or "").strip()
    }
    scored: List[Dict[str, Any]] = []
    for component in catalog.get("components") or []:
        display_name = str(component.get("display_name") or "")
        evidence_hints: List[Dict[str, str]] = []
        score = 0.0

        for keyword in component.get("keywords") or []:
            keyword_text = str(keyword or "").strip()
            if keyword_text and keyword_text.lower() in text_blob:
                score += 0.45
                evidence_hints.append({"source": "entry_or_summary_text", "value": keyword_text})
                break
            if keyword_text and keyword_text.lower() in changed_path_blob:
                score += 0.35
                evidence_hints.append({"source": "changed_files_keyword", "value": keyword_text})
                break

        component_files = {_normalize_path(path) for path in component.get("representative_files") or [] if str(path)}
        component_prefixes = {
            _normalize_path(prefix)
            for prefix in component.get("file_prefixes") or []
            if str(prefix).strip()
        }
        matched_file = next((path for path in changed_files if path in component_files), "")
        if matched_file:
            score += 0.40
            evidence_hints.append({"source": "changed_files", "value": matched_file})
        else:
            matched_prefix = _best_path_prefix_match(changed_files, component_files, component_prefixes)
            if matched_prefix:
                score += 0.30
                evidence_hints.append({"source": "changed_files_prefix", "value": matched_prefix})

        if _normalize_text(display_name) in primary_components:
            score += 0.35
            evidence_hints.append({"source": "phase2_primary_component", "value": display_name})

        event_components = _event_components(source_records)
        if _normalize_text(display_name) in event_components:
            score += 0.25
            evidence_hints.append({"source": "architecture_event_component", "value": display_name})

        if score <= 0:
            continue
        scored.append(
            {
                "display_name": display_name,
                "description": str(component.get("description") or ""),
                "candidate_score": round(min(score, 1.0), 3),
                "evidence_hints": evidence_hints[:4],
            }
        )

    scored.sort(key=lambda item: (-float(item.get("candidate_score") or 0.0), str(item.get("display_name") or "")))
    return scored[:3]


def _best_path_prefix_match(
    changed_files: List[str],
    component_files: set[str],
    component_prefixes: Optional[set[str]] = None,
) -> str:
    all_component_prefixes = {
        _path_prefix(path)
        for path in component_files
        if _path_prefix(path)
    }
    if component_prefixes:
        all_component_prefixes.update(prefix for prefix in component_prefixes if prefix)
    if not all_component_prefixes:
        return ""
    best = ""
    best_depth = 0
    for changed_file in changed_files:
        changed_prefixes = _path_prefixes(changed_file)
        for prefix in changed_prefixes:
            if _is_broad_path_prefix(prefix):
                continue
            if prefix in all_component_prefixes:
                depth = prefix.count("/") + 1
                if depth > best_depth:
                    best_depth = depth
                    best = prefix
    return best


def _path_prefixes(path: str) -> List[str]:
    parts = [part for part in _normalize_path(path).split("/") if part]
    prefixes: List[str] = []
    for depth in range(min(len(parts) - 1, 3), 0, -1):
        prefixes.append("/".join(parts[:depth]))
    return prefixes


def _path_prefix(path: str) -> str:
    prefixes = _path_prefixes(path)
    return prefixes[0] if prefixes else ""


def _is_broad_path_prefix(prefix: str) -> bool:
    normalized = _normalize_path(prefix)
    if not normalized:
        return True
    if normalized in GENERIC_PATH_PREFIXES:
        return True
    return len([part for part in normalized.split("/") if part]) <= 1


def _normalize_assignment_decisions(parsed: Dict[str, Any], cards: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    raw_items = parsed.get("assignments")
    if not isinstance(raw_items, list):
        raise ValueError("Architecture component assignment response must contain an assignments list.")
    expected_ids = [str(card.get("entry_id") or "") for card in cards]
    valid_components = {
        str(card.get("entry_id") or ""): {
            str(component.get("display_name") or "")
            for component in card.get("candidate_components") or []
            if str(component.get("display_name") or "")
        }
        for card in cards
    }
    seen: set[str] = set()
    result: List[Dict[str, Any]] = []
    for raw in raw_items:
        if not isinstance(raw, dict):
            raise ValueError("Each architecture component assignment must be an object.")
        entry_id = str(raw.get("entry_id") or "").strip()
        if entry_id not in expected_ids:
            raise ValueError(f"Unknown entry_id in architecture component assignment: {entry_id}")
        if entry_id in seen:
            raise ValueError(f"Duplicate entry_id in architecture component assignment: {entry_id}")
        seen.add(entry_id)
        assignment_type = str(raw.get("assignment_type") or "").strip().lower()
        if assignment_type not in {"component", "cross_cutting", "unknown"}:
            raise ValueError(f"Invalid assignment_type for entry_id {entry_id}: {assignment_type}")
        display_component = " ".join(str(raw.get("display_arch_component") or "").split()).strip()
        if assignment_type == "component":
            if display_component not in valid_components.get(entry_id, set()):
                raise ValueError(f"Entry {entry_id} used non-candidate component: {display_component}")
        else:
            display_component = ""
        result.append(
            {
                "entry_id": entry_id,
                "assignment_type": assignment_type,
                "display_arch_component": display_component,
                "reason": " ".join(str(raw.get("reason") or "").split()).strip(),
            }
        )
    missing = [entry_id for entry_id in expected_ids if entry_id not in seen]
    if missing:
        raise ValueError(f"Architecture component assignment missing entry_id decisions: {missing}")
    return result


def _assignment_batches(cards: List[Dict[str, Any]], config) -> List[Dict[str, Any]]:
    batch_size = _phase3_arch_module_assignment_batch_size(config)
    result = []
    chunk_count = (len(cards) + batch_size - 1) // batch_size if cards else 0
    for index in range(chunk_count):
        start = index * batch_size
        end = start + batch_size
        result.append(
            {
                "batch_key": f"batch{index + 1:03d}",
                "chunk_index": index + 1,
                "chunk_count": chunk_count,
                "cards": cards[start:end],
            }
        )
    return result


def _components_from_clustercomponent(
    cluster_component: Dict[str, Any],
    cluster_files: Dict[str, List[str]],
    arch_descriptions: Dict[str, str],
) -> List[Dict[str, Any]]:
    components = []
    for index, node in enumerate(cluster_component.get("structure") or [], start=1):
        if not isinstance(node, dict) or node.get("@type") != "component":
            continue
        name = str(node.get("name") or "").strip()
        if not name:
            continue
        clusters = [str(item.get("name") or "").strip() for item in node.get("nested") or [] if isinstance(item, dict)]
        files = _unique(path for cluster in clusters for path in cluster_files.get(cluster, []) if path)
        description = _description_for_component(name, arch_descriptions)
        components.append(_component_record(index, name, description, clusters, files, ["ClusterComponent", "ArchSem", "NamedClusters"]))
    return components


def _components_from_archsem(arch_descriptions: Dict[str, str]) -> List[Dict[str, Any]]:
    return [
        _component_record(index, name, description, [], [], ["ArchSem"])
        for index, (name, description) in enumerate(arch_descriptions.items(), start=1)
        if name
    ]


def _components_from_namedclusters(cluster_files: Dict[str, List[str]]) -> List[Dict[str, Any]]:
    return [
        _component_record(index, name, "", [name], files, ["NamedClusters"])
        for index, (name, files) in enumerate(cluster_files.items(), start=1)
        if name
    ][:20]


def _component_record(
    index: int,
    display_name: str,
    description: str,
    clusters: List[str],
    files: List[str],
    evidence_sources: List[str],
) -> Dict[str, Any]:
    return {
        "component_id": f"COMP-{index:03d}",
        "display_name": display_name,
        "description": _truncate_sentence(description, 260),
        "clusters": clusters[:40],
        "representative_files": files[:120],
        "file_prefixes": _component_file_prefixes(files),
        "keywords": _component_keywords(display_name, clusters),
        "evidence_sources": evidence_sources,
    }


def _cluster_files(namedclusters: Dict[str, Any]) -> Dict[str, List[str]]:
    result: Dict[str, List[str]] = {}
    for node in namedclusters.get("structure") or []:
        if not isinstance(node, dict) or node.get("@type") != "group":
            continue
        name = str(node.get("name") or "").strip()
        files = [
            _normalize_path(item.get("name"))
            for item in node.get("nested") or []
            if isinstance(item, dict) and item.get("@type") == "item" and str(item.get("name") or "").strip()
        ]
        if name:
            result[name] = sorted(set(files))
    return result


def _archsem_descriptions(archsem: Dict[str, Any]) -> Dict[str, str]:
    result: Dict[str, str] = {}
    for component in archsem.get("components") or []:
        if not isinstance(component, dict):
            continue
        name = str(component.get("name") or "").strip()
        description = ""
        for nested in component.get("nested") or []:
            if isinstance(nested, dict) and nested.get("@type") == "indicator":
                description = str(nested.get("content") or "").strip()
                break
        if name:
            result[name] = description
    return result


def _description_for_component(name: str, descriptions: Dict[str, str]) -> str:
    normalized = _normalize_text(name)
    for candidate, description in descriptions.items():
        if _normalize_text(candidate) == normalized:
            return description
    for candidate, description in descriptions.items():
        candidate_norm = _normalize_text(candidate)
        if normalized in candidate_norm or candidate_norm in normalized:
            return description
    return ""


def _component_keywords(display_name: str, clusters: List[str]) -> List[str]:
    keywords: List[str] = []
    keywords.append(display_name)
    for match in re.findall(r"\(([^)]+)\)", display_name):
        keywords.append(match)
    for token in re.split(r"[^A-Za-z0-9_]+", display_name):
        if _is_component_keyword_token(token):
            keywords.append(token)
    keywords.extend(clusters[:20])
    return _unique(item.strip() for item in keywords if item and item.strip())


def _is_component_keyword_token(token: str) -> bool:
    normalized = str(token or "").strip().lower()
    if len(normalized) < 3:
        return False
    if normalized in GENERIC_COMPONENT_KEYWORDS:
        return False
    return True


def _component_file_prefixes(files: List[str]) -> List[str]:
    prefixes: List[str] = []
    for path in files:
        prefixes.extend(_path_prefixes(path))
    return _unique(prefixes)[:240]


def _event_components(records: List[Dict[str, Any]]) -> set[str]:
    result = set()
    for record in records:
        for attribution in record.get("event_attributions") or []:
            if isinstance(attribution, dict) and str(attribution.get("component") or "").strip():
                result.add(_normalize_text(attribution.get("component")))
        evidence = record.get("architecture_evidence") or {}
        if isinstance(evidence, dict):
            for event in evidence.get("matched_arch_events") or []:
                if isinstance(event, dict) and str(event.get("component") or "").strip():
                    result.add(_normalize_text(event.get("component")))
    return result


def _architecture_labeled_entries(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    seen: set[str] = set()
    result = []
    for index, entry in enumerate(entries, start=1):
        if not _is_important_entry(entry):
            continue
        entry_id = str(entry.get("entry_id") or entry.get("group_id") or "").strip()
        if not entry_id or entry_id in seen:
            entry_id = f"ENTRY-{index:04d}"
        seen.add(entry_id)
        entry["entry_id"] = entry_id
        result.append({"entry_id": entry_id, "entry": entry})
    return result


def _is_important_entry(entry: Dict[str, Any]) -> bool:
    top_section = str(entry.get("top_section") or "").strip().lower()
    if top_section in {"important", "important_changes"}:
        return True
    if top_section in {"ordinary", "ordinary_changelog", "regular_changelog", "changelog"}:
        return False
    label_type = str(entry.get("architecture_label_type") or "none").strip().lower()
    label_text = str(entry.get("architecture_label") or "").strip()
    return bool(label_text) and label_type not in {"", "none"}


def _semarc_paths(config) -> Dict[str, Path]:
    repo_name = Path(getattr(config, "repo_path", "")).name
    ref = str(getattr(config, "new_ref", "") or "")
    root = Path(getattr(config, "semarc_output_dir", "") or "outputs/external_artifacts/semarc_results")
    return {
        "archsem": _semarc_result_path(root, repo_name, ref, "ArchSem"),
        "namedclusters": _semarc_result_path(root, repo_name, ref, "NamedClusters"),
        "clustercomponent": _semarc_result_path(root, repo_name, ref, "ClusterComponent"),
    }


def _semarc_result_path(root: Path, repo_name: str, ref: str, suffix: str) -> Path:
    roots = [root, Path("outputs/external_artifacts/semarc_results"), Path("arch_changes-reports/sema_results")]
    seen = set()
    for candidate_root in roots:
        directory = candidate_root / f"{repo_name}-{ref}"
        for candidate in (
            directory / f"{repo_name}-{ref}_{suffix}.json",
            directory / f"{repo_name}_{ref}_{suffix}.json",
        ):
            key = str(candidate)
            if key in seen:
                continue
            seen.add(key)
            if candidate.exists():
                return candidate
    return roots[0] / f"{repo_name}-{ref}" / f"{repo_name}-{ref}_{suffix}.json"


def _ensure_llm_client(config, llm_client) -> None:
    if llm_client is not None:
        return
    env_var = str(getattr(config, "llm_api_key_env_var", "") or "").strip()
    if not env_var:
        raise RuntimeError("Phase 3 architecture component assignment is enabled, but config.llm_api_key_env_var is empty.")
    if not os.getenv(env_var):
        raise RuntimeError(f"Phase 3 architecture component assignment is enabled, but environment variable {env_var} is not set.")
    raise RuntimeError("Phase 3 architecture component assignment is enabled, but no OpenAI-compatible LLM client could be created.")


def _raise_assignment_failure(
    *,
    config,
    output_dir: Path,
    batch_key: str,
    prompt_path: Path,
    rendered_prompt: str,
    raw_response: str,
    validation_attempts: List[Dict[str, Any]],
    error: Optional[BaseException],
    input_payload: Dict[str, Any],
) -> None:
    if phase3_debug_fail_fast(config):
        raise_phase3_llm_failure(
            output_dir=phase3_failure_output_dir(config, output_dir),
            stage="phase3.2.6_arch_component_assignment",
            batch_or_bucket_or_slot=batch_key,
            error_type="component_assignment_validation_error",
            error_message=str(error or "Architecture component assignment failed."),
            exception=error,
            prompt_template_path=str(prompt_path),
            rendered_prompt=rendered_prompt,
            raw_llm_response=raw_response,
            input_summary={"entry_count": len(input_payload.get("entries") or [])},
            input_payload=input_payload,
            validation_attempts=validation_attempts,
        )
    raise RuntimeError(str(error or "Architecture component assignment failed."))


def _phase3_arch_module_assignment_enabled(config) -> bool:
    if config is None:
        return False
    return bool(getattr(config, "phase3_arch_module_assignment_enabled", True))


def _phase3_arch_module_assignment_batch_size(config) -> int:
    try:
        return max(1, int(getattr(config, "phase3_arch_module_assignment_batch_size", 20) or 20))
    except Exception:
        return 20


def _phase3_arch_module_assignment_concurrency(config, job_count: int) -> int:
    try:
        configured = int(getattr(config, "phase3_arch_module_assignment_concurrency", 1) or 1)
    except Exception:
        configured = 1
    return max(1, min(configured, max(1, job_count)))


def _retry_prompt(user_prompt: str, attempt: int, error: Optional[BaseException] = None) -> str:
    if attempt <= 1:
        return user_prompt
    return (
        user_prompt
        + "\n\nThe previous response failed validation: "
        + str(error or "invalid JSON or missing entry_id")[:500]
        + "\nReturn only a valid JSON object. Every input entry_id must appear exactly once."
    )


def _unknown_decision(entry_id: str) -> Dict[str, str]:
    return {"entry_id": entry_id, "assignment_type": "unknown", "display_arch_component": "", "reason": ""}


def _load_json(path: Path) -> Dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _normalize_path(value: Any) -> str:
    return str(value or "").replace("\\", "/").strip().lower()


def _normalize_text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip().lower())


def _truncate_sentence(text: str, limit: int) -> str:
    text = " ".join(str(text or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def _unique(values: Iterable[str]) -> List[str]:
    result = []
    seen = set()
    for value in values:
        text = str(value or "").strip()
        if not text or text in seen:
            continue
        result.append(text)
        seen.add(text)
    return result
