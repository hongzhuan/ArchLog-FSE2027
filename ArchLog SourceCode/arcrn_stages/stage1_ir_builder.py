from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any, Dict, List, Optional, Sequence

from .models import ChangeIR, ChangeUnitRecord, CommitChangeRecord, utc_now_iso
from .stage1_input_loader import Stage1LoadedInputs


UNKNOWN_CATEGORY = "unknown"


def build_stage1_change_ir(loaded_inputs: Stage1LoadedInputs) -> ChangeIR:
    summaries_by_unit_id = {
        str(item.get("unit_id")): item
        for item in loaded_inputs.summaries
        if item.get("unit_id")
    }

    commit_to_units: Dict[str, List[ChangeUnitRecord]] = defaultdict(list)
    commit_meta: Dict[str, Dict[str, Any]] = {}

    for raw_unit in loaded_inputs.change_units:
        unit_record = _build_change_unit_record(raw_unit, summaries_by_unit_id)
        commit_to_units[unit_record.commit_id].append(unit_record)

        raw_commit = raw_unit.get("commit") or {}
        commit_meta.setdefault(
            unit_record.commit_id,
            {
                "commit": raw_commit,
                "unit_ids": [],
            },
        )
        commit_meta[unit_record.commit_id]["unit_ids"].append(unit_record.change_unit_id)

    commit_records = [
        _build_commit_change_record(
            commit_id=commit_id,
            unit_records=unit_records,
            raw_commit=commit_meta.get(commit_id, {}).get("commit") or {},
        )
        for commit_id, unit_records in commit_to_units.items()
    ]

    commit_records.sort(key=lambda item: ((item.date or ""), item.commit_id))

    source_pipeline = {
        "pipeline_name": loaded_inputs.pipeline_report.get("pipeline_name"),
        "started_at": loaded_inputs.pipeline_report.get("started_at"),
        "finished_at": loaded_inputs.pipeline_report.get("finished_at"),
        "final_stats": loaded_inputs.pipeline_report.get("final_stats", {}),
    }

    return ChangeIR(
        generated_at=utc_now_iso(),
        input_dir=str(loaded_inputs.input_dir),
        source_files={key: str(path) for key, path in loaded_inputs.resolved_files.items()},
        source_pipeline=source_pipeline,
        commits=commit_records,
        stats=_build_change_ir_stats(commit_records),
    )


def _build_change_unit_record(
    raw_unit: Dict[str, Any],
    summaries_by_unit_id: Dict[str, Dict[str, Any]],
) -> ChangeUnitRecord:
    raw_commit = raw_unit.get("commit") or {}
    commit_id = str(raw_commit.get("commit_id") or "").strip()
    unit_id = str(raw_unit.get("unit_id") or "").strip()

    summary_record = summaries_by_unit_id.get(unit_id)

    changed_methods = raw_unit.get("changed_methods") or []
    method_hunk_pairs = raw_unit.get("method_hunk_pairs") or []
    method_context_graphs = raw_unit.get("method_context_graphs") or []
    raw_evidence = raw_unit.get("evidence") if isinstance(raw_unit.get("evidence"), dict) else {}
    evidence_granularity = str(raw_evidence.get("evidence_granularity") or "method_level")
    change_detection_status = str(raw_evidence.get("change_detection_status") or "method_level_change")

    changed_files = _sorted_unique(
        list(_collect_changed_files(raw_commit, changed_methods))
        + _collect_files_from_fallback_hunks(raw_evidence.get("fallback_diff_hunks") or [])
        + _collect_files_from_fallback_hunks(raw_evidence.get("fallback_file_hunks") or [])
        + [str(item) for item in raw_evidence.get("files") or [] if str(item).strip()]
    )
    changed_method_names = _collect_changed_method_names(changed_methods)
    change_types = sorted(
        {
            str(method.get("change_type") or "").strip()
            for method in changed_methods
            if method.get("change_type")
        }
    )
    if evidence_granularity == "file_level" and not change_types:
        change_types = ["file_only"]
    elif evidence_granularity != "method_level" and not change_types:
        change_types = ["hunk_only"]
    matched_hunk_ids = _sorted_unique(
        _collect_matched_hunk_ids(method_hunk_pairs)
        + _collect_fallback_hunk_ids(raw_evidence.get("fallback_diff_hunks") or [])
        + _collect_fallback_hunk_ids(raw_evidence.get("fallback_file_hunks") or [])
        + [str(item) for item in raw_evidence.get("hunk_ids") or [] if str(item).strip()]
    )
    diff_snippets = _collect_diff_snippets(method_hunk_pairs)
    diff_snippets.extend(_collect_fallback_diff_snippets(raw_evidence.get("fallback_diff_hunks") or []))
    diff_snippets.extend(
        _collect_fallback_diff_snippets(
            raw_evidence.get("fallback_file_hunks") or [],
            label="file_level_fallback",
        )
    )
    related_entities = _collect_related_entities(method_context_graphs)
    call_context = _render_call_context(method_context_graphs)

    category = _pick_first_non_empty(
        [
            summary_record.get("predicted_category") if summary_record else None,
            raw_unit.get("inferred_change_category"),
        ]
    )

    return ChangeUnitRecord(
        change_unit_id=unit_id,
        commit_id=commit_id,
        summary=(summary_record.get("summary") if summary_record else None),
        category=category,
        commit_url=_optional_text(summary_record.get("commit_url") if summary_record else None),
        pull_requests=_normalize_pull_requests(summary_record.get("pull_requests") if summary_record else []),
        changed_files=changed_files,
        changed_methods=changed_method_names,
        change_types=change_types,
        matched_hunk_ids=matched_hunk_ids,
        diff_snippets=diff_snippets,
        related_entities=related_entities,
        call_context=call_context,
        evidence_granularity=evidence_granularity,
        change_detection_status=change_detection_status,
        source_refs={
            "step7_unit_id": unit_id,
            "step10_unit_id": summary_record.get("unit_id") if summary_record else None,
            "evidence_granularity": evidence_granularity,
            "change_detection_status": change_detection_status,
            "fallback_from_diff_hunks": bool(raw_evidence.get("fallback_from_diff_hunks")),
            "fallback_from_file_diff": bool(raw_evidence.get("fallback_from_file_diff")),
            "method_uids": [
                str(method.get("method_uid"))
                for method in changed_methods
                if method.get("method_uid")
            ],
            "graph_ids": [
                str(graph.get("graph_id"))
                for graph in method_context_graphs
                if graph.get("graph_id")
            ],
            "hunk_pair_ids": [
                str(pair.get("pair_id"))
                for pair in method_hunk_pairs
                if pair.get("pair_id")
            ],
            "hunk_ids": matched_hunk_ids,
        },
    )


def _build_commit_change_record(
    commit_id: str,
    unit_records: Sequence[ChangeUnitRecord],
    raw_commit: Dict[str, Any],
) -> CommitChangeRecord:
    author = _pick_first_non_empty(
        [
            raw_commit.get("author_name"),
            raw_commit.get("committer_name"),
        ]
    )
    date = _pick_first_non_empty(
        [
            raw_commit.get("authored_date"),
            raw_commit.get("committed_date"),
        ]
    )
    commit_message = _compose_commit_message(raw_commit)
    commit_summary = _aggregate_commit_summary(unit_records, raw_commit)
    category = _aggregate_commit_category(unit_records)
    commit_url = next((unit.commit_url for unit in unit_records if unit.commit_url), None)
    pull_requests = _merge_pull_requests(unit_records)

    all_changed_files = _sorted_unique(
        file_path
        for unit in unit_records
        for file_path in unit.changed_files
    )
    all_changed_methods = _sorted_unique(
        method_name
        for unit in unit_records
        for method_name in unit.changed_methods
    )

    return CommitChangeRecord(
        commit_id=commit_id,
        commit_message=commit_message,
        author=author,
        date=date,
        change_units=list(unit_records),
        commit_summary=commit_summary,
        category=category,
        commit_url=commit_url,
        pull_requests=pull_requests,
        all_changed_files=all_changed_files,
        all_changed_methods=all_changed_methods,
        file_count=len(all_changed_files),
        method_count=len(all_changed_methods),
        change_unit_count=len(unit_records),
        has_diff=any(unit.diff_snippets for unit in unit_records),
        has_call_context=any(unit.call_context for unit in unit_records),
        debug_info={
            "commit_subject": raw_commit.get("subject") or "",
            "files_touched": _sorted_unique(raw_commit.get("files_touched") or []),
            "unit_ids": [unit.change_unit_id for unit in unit_records],
            "unit_categories": [unit.category for unit in unit_records if unit.category],
            "evidence_granularities": _sorted_unique(unit.evidence_granularity for unit in unit_records),
            "change_detection_statuses": _sorted_unique(unit.change_detection_status for unit in unit_records),
            "summary_sources": [
                unit.source_refs.get("step10_unit_id")
                for unit in unit_records
                if unit.source_refs.get("step10_unit_id")
            ],
        },
    )


def _collect_changed_files(raw_commit: Dict[str, Any], changed_methods: Sequence[Dict[str, Any]]) -> List[str]:
    files = set()

    for file_path in raw_commit.get("files_touched") or []:
        normalized = _normalize_path(file_path)
        if normalized:
            files.add(normalized)

    for method in changed_methods:
        old_identity = method.get("old_identity") or {}
        new_identity = method.get("new_identity") or {}
        for identity in (old_identity, new_identity):
            normalized = _normalize_path(identity.get("file_path"))
            if normalized:
                files.add(normalized)

    return sorted(files)


def _collect_changed_method_names(changed_methods: Sequence[Dict[str, Any]]) -> List[str]:
    method_names = set()
    for method in changed_methods:
        old_identity = method.get("old_identity") or {}
        new_identity = method.get("new_identity") or {}
        for identity in (new_identity, old_identity):
            qualified_name = str(identity.get("qualified_name") or "").strip()
            if qualified_name:
                method_names.add(qualified_name)
                break
    return sorted(method_names)


def _collect_matched_hunk_ids(method_hunk_pairs: Sequence[Dict[str, Any]]) -> List[str]:
    hunk_ids = set()
    for pair in method_hunk_pairs:
        for matched_hunk in pair.get("matched_hunks") or []:
            hunk_id = str(matched_hunk.get("hunk_id") or "").strip()
            if hunk_id:
                hunk_ids.add(hunk_id)
    return sorted(hunk_ids)


def _collect_fallback_hunk_ids(fallback_hunks: Sequence[Dict[str, Any]]) -> List[str]:
    hunk_ids = set()
    for hunk in fallback_hunks:
        if not isinstance(hunk, dict):
            continue
        hunk_id = str(hunk.get("hunk_id") or "").strip()
        if hunk_id:
            hunk_ids.add(hunk_id)
    return sorted(hunk_ids)


def _collect_files_from_fallback_hunks(fallback_hunks: Sequence[Dict[str, Any]]) -> List[str]:
    files = set()
    for hunk in fallback_hunks:
        if not isinstance(hunk, dict):
            continue
        for key in ("file_path_new", "file_path_old"):
            normalized = _normalize_path(hunk.get(key))
            if normalized:
                files.add(normalized)
    return sorted(files)


def _collect_diff_snippets(method_hunk_pairs: Sequence[Dict[str, Any]], max_snippets: int = 8) -> List[str]:
    snippets: List[str] = []
    seen_hunk_ids = set()

    for pair in method_hunk_pairs:
        for matched_hunk in pair.get("matched_hunks") or []:
            hunk_id = str(matched_hunk.get("hunk_id") or "").strip()
            if not hunk_id or hunk_id in seen_hunk_ids:
                continue
            seen_hunk_ids.add(hunk_id)
            snippet = _render_diff_snippet(matched_hunk)
            if snippet:
                snippets.append(snippet)
            if len(snippets) >= max_snippets:
                return snippets

    return snippets


def _collect_fallback_diff_snippets(
    fallback_hunks: Sequence[Dict[str, Any]],
    max_snippets: int = 8,
    label: str = "hunk_level_fallback",
) -> List[str]:
    snippets: List[str] = []
    seen_hunk_ids = set()

    for hunk in fallback_hunks:
        if not isinstance(hunk, dict):
            continue
        hunk_id = str(hunk.get("hunk_id") or "").strip()
        if not hunk_id or hunk_id in seen_hunk_ids:
            continue
        seen_hunk_ids.add(hunk_id)
        snippet = _render_fallback_diff_snippet(hunk, label=label)
        if snippet:
            snippets.append(snippet)
        if len(snippets) >= max_snippets:
            return snippets

    return snippets


def _render_fallback_diff_snippet(
    hunk: Dict[str, Any],
    max_lines: int = 12,
    max_chars: int = 1200,
    label: str = "hunk_level_fallback",
) -> str:
    hunk_id = str(hunk.get("hunk_id") or "").strip()
    file_path = str(hunk.get("file_path_new") or hunk.get("file_path_old") or "").strip()
    diff_text = str(hunk.get("diff_text") or "")
    if not diff_text.strip():
        return ""

    lines = diff_text.splitlines()
    trimmed_lines = [str(line) for line in lines[:max_lines]]
    if len(lines) > max_lines:
        trimmed_lines.append("... [truncated]")

    body = "\n".join(trimmed_lines).strip()
    if len(body) > max_chars:
        body = body[: max_chars - 15].rstrip() + "\n... [truncated]"

    if not body:
        return ""

    label = f"{hunk_id} ({label})"
    if file_path:
        label += f" {file_path}"
    return f"{label}\n{body}"


def _render_diff_snippet(matched_hunk: Dict[str, Any], max_lines: int = 12, max_chars: int = 1200) -> str:
    hunk_id = str(matched_hunk.get("hunk_id") or "").strip()
    match_type = str(matched_hunk.get("match_type") or "").strip()
    diff_lines = matched_hunk.get("matched_diff_text") or []

    if not isinstance(diff_lines, list):
        return ""

    trimmed_lines = [str(line) for line in diff_lines[:max_lines]]
    if len(diff_lines) > max_lines:
        trimmed_lines.append("... [truncated]")

    body = "\n".join(trimmed_lines).strip()
    if len(body) > max_chars:
        body = body[: max_chars - 15].rstrip() + "\n... [truncated]"

    if not body:
        return ""

    return f"{hunk_id} ({match_type})\n{body}"


def _collect_related_entities(method_context_graphs: Sequence[Dict[str, Any]], max_entities: int = 20) -> List[str]:
    entities = []
    seen = set()

    for graph in method_context_graphs:
        for node in graph.get("nodes") or []:
            qualified_name = str(node.get("qualified_name") or "").strip()
            if not qualified_name or qualified_name in seen:
                continue
            seen.add(qualified_name)
            entities.append(qualified_name)
            if len(entities) >= max_entities:
                return entities

    return entities


def _render_call_context(method_context_graphs: Sequence[Dict[str, Any]], max_graphs: int = 3) -> Optional[str]:
    blocks: List[str] = []

    for graph in method_context_graphs[:max_graphs]:
        graph_id = str(graph.get("graph_id") or "").strip()
        nodes = graph.get("nodes") or []
        edges = graph.get("edges") or []

        node_parts = []
        for node in nodes[:6]:
            qualified_name = str(node.get("qualified_name") or "").strip()
            role = str(node.get("role") or "context").strip()
            if qualified_name:
                node_parts.append(f"{qualified_name} ({role})")

        edge_parts = []
        for edge in edges[:8]:
            src = str(edge.get("src_entity_id") or "").strip()
            dst = str(edge.get("dst_entity_id") or "").strip()
            relation_type = str(edge.get("relation_type") or "").strip()
            if src and dst:
                edge_parts.append(f"{src}->{dst} ({relation_type})")

        if not node_parts and not edge_parts:
            continue

        block_lines = [f"graph_id={graph_id}" if graph_id else "graph"]
        if node_parts:
            block_lines.append("nodes: " + "; ".join(node_parts))
        if edge_parts:
            block_lines.append("edges: " + "; ".join(edge_parts))
        blocks.append("\n".join(block_lines))

    if not blocks:
        return None

    return "\n\n".join(blocks)


def _aggregate_commit_summary(unit_records: Sequence[ChangeUnitRecord], raw_commit: Dict[str, Any]) -> Optional[str]:
    summaries = _sorted_unique(
        unit.summary.strip()
        for unit in unit_records
        if unit.summary and unit.summary.strip()
    )

    if not summaries:
        subject = str(raw_commit.get("subject") or "").strip()
        return subject or None

    if len(summaries) == 1:
        return summaries[0]

    return "；".join(summaries[:3])


def _aggregate_commit_category(unit_records: Sequence[ChangeUnitRecord]) -> Optional[str]:
    categories = [
        unit.category
        for unit in unit_records
        if unit.category and unit.category != UNKNOWN_CATEGORY
    ]
    if not categories:
        return UNKNOWN_CATEGORY
    return Counter(categories).most_common(1)[0][0]


def _merge_pull_requests(unit_records: Sequence[ChangeUnitRecord]) -> List[Dict[str, Any]]:
    merged: List[Dict[str, Any]] = []
    seen = set()
    for unit in unit_records:
        for pull_request in unit.pull_requests:
            key = (pull_request.get("number"), pull_request.get("url"))
            if key in seen:
                continue
            merged.append(dict(pull_request))
            seen.add(key)
    return merged


def _normalize_pull_requests(value: Any) -> List[Dict[str, Any]]:
    if not isinstance(value, list):
        return []
    result: List[Dict[str, Any]] = []
    for raw in value:
        if not isinstance(raw, dict):
            continue
        url = _optional_text(raw.get("url"))
        try:
            number = int(raw.get("number"))
        except (TypeError, ValueError):
            continue
        if number > 0 and url:
            result.append({"number": number, "url": url})
    return result


def _optional_text(value: Any) -> Optional[str]:
    text = str(value or "").strip()
    return text or None


def _compose_commit_message(raw_commit: Dict[str, Any]) -> str:
    subject = str(raw_commit.get("subject") or "").strip()
    body = str(raw_commit.get("body") or "").strip()
    if subject and body:
        return f"{subject}\n{body}"
    return subject or body


def _build_change_ir_stats(commit_records: Sequence[CommitChangeRecord]) -> Dict[str, Any]:
    units = [unit for record in commit_records for unit in record.change_units]
    return {
        "commit_count": len(commit_records),
        "change_unit_count": sum(record.change_unit_count for record in commit_records),
        "total_file_references": sum(record.file_count for record in commit_records),
        "total_method_references": sum(record.method_count for record in commit_records),
        "commits_with_diff": sum(1 for record in commit_records if record.has_diff),
        "commits_with_call_context": sum(1 for record in commit_records if record.has_call_context),
        "method_level_change_units": sum(1 for unit in units if unit.evidence_granularity == "method_level"),
        "hunk_level_fallback_change_units": sum(1 for unit in units if unit.evidence_granularity == "hunk_level"),
        "file_level_fallback_change_units": sum(1 for unit in units if unit.evidence_granularity == "file_level"),
        "non_method_level_fallback_change_units": sum(1 for unit in units if unit.evidence_granularity != "method_level"),
    }


def _pick_first_non_empty(values: Sequence[Optional[Any]]) -> Optional[str]:
    for value in values:
        text = str(value or "").strip()
        if text:
            return text
    return None


def _normalize_path(path: Any) -> str:
    if path is None:
        return ""
    text = str(path).replace("\\", "/").strip()
    while text.startswith("./"):
        text = text[2:]
    return text


def _sorted_unique(values) -> List[str]:
    unique = {str(value).strip() for value in values if str(value).strip()}
    return sorted(unique)
