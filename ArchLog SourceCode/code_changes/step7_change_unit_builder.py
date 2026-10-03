from __future__ import annotations

import logging
from collections import defaultdict
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from .constants import (
    CATEGORY_BUGFIX,
    CATEGORY_FEATURE,
    CATEGORY_MAINTENANCE,
    CATEGORY_PERFORMANCE,
    CATEGORY_REFACTORING,
    CATEGORY_SECURITY,
    CATEGORY_UNKNOWN,
    COMMIT_KEYWORDS_BUGFIX,
    COMMIT_KEYWORDS_FEATURE,
    COMMIT_KEYWORDS_PERFORMANCE,
    COMMIT_KEYWORDS_REFACTORING,
    COMMIT_KEYWORDS_SECURITY,
    DEFAULT_LOGGER_NAME,
)
from .models import (
    ChangeUnit,
    ChangeUnitsOutput,
    CommitInfo,
    DiffHunksOutput,
    MethodContextGraphsOutput,
    MethodHunkPairsOutput,
    PipelineConfig,
)
from .step5_diff_hunk_extractor import _parse_git_log_output, _run_git_log_patch


LOGGER = logging.getLogger(DEFAULT_LOGGER_NAME)


# ============================================================
# Public entry
# ============================================================

def run_change_unit_builder(
    config: PipelineConfig,
    commits_mapped_output,
    method_context_graphs_output: MethodContextGraphsOutput,
    method_hunk_pairs_output: MethodHunkPairsOutput,
    diff_hunks_output: Optional[DiffHunksOutput] = None,
) -> ChangeUnitsOutput:
    """
    Build ChangeUnit objects where:
        commit = unit

    Sources:
    - Step2: changed methods + primary_commit_id / commits
    - Step4: method context graphs
    - Step6: method hunk pairs

    Output:
    - one method-level ChangeUnit per commit that has at least one changed method assigned
    - one hunk-level fallback ChangeUnit per commit that has C/C++ diff hunks but no changed method
    - one file-level fallback ChangeUnit per commit that only changed supported non-C/C++ files
    """
    changed_methods = commits_mapped_output.changed_methods

    graphs_by_method_uid = _index_graphs_by_method_uid(method_context_graphs_output)
    pairs_by_method_uid = _index_pairs_by_method_uid(method_hunk_pairs_output)

    methods_by_commit: Dict[str, List] = defaultdict(list)
    commit_info_by_id: Dict[str, CommitInfo] = {}

    for method in changed_methods:
        commit_id, commit_info = _resolve_primary_commit(method)
        if commit_id is None or commit_info is None:
            continue

        methods_by_commit[commit_id].append(method)
        commit_info_by_id[commit_id] = commit_info

    change_units: List[ChangeUnit] = []
    for commit_id, methods in methods_by_commit.items():
        commit_info = commit_info_by_id[commit_id]

        # stable ordering: by file, then start line, then method uid
        methods_sorted = sorted(
            methods,
            key=lambda m: (
                (m.new_identity or m.old_identity).file_path if (m.new_identity or m.old_identity) else "",
                (m.new_identity or m.old_identity).start_line if (m.new_identity or m.old_identity) else 0,
                m.method_uid,
            ),
        )

        changed_method_uids = [m.method_uid for m in methods_sorted]

        method_graphs = []
        for method_uid in changed_method_uids:
            method_graphs.extend(graphs_by_method_uid.get(method_uid, []))

        method_hunk_pairs = []
        for method_uid in changed_method_uids:
            pair = pairs_by_method_uid.get(method_uid)
            if pair is not None:
                method_hunk_pairs.append(pair)

        inferred_change_category = _infer_change_category_from_commit(commit_info)

        evidence = _build_unit_evidence(
            commit_info=commit_info,
            methods=methods_sorted,
            method_graphs=method_graphs,
            method_hunk_pairs=method_hunk_pairs,
        )

        unit = ChangeUnit(
            unit_id=_make_unit_id(commit_id),
            commit=commit_info,
            changed_method_uids=changed_method_uids,
            changed_methods=methods_sorted,
            method_context_graphs=method_graphs,
            method_hunk_pairs=method_hunk_pairs,
            inferred_change_category=inferred_change_category,
            evidence=evidence,
        )
        change_units.append(unit)

    hunk_fallback_units = _build_hunk_level_fallback_units(
        config=config,
        diff_hunks_output=diff_hunks_output,
        covered_commit_ids=set(methods_by_commit),
    )
    change_units.extend(hunk_fallback_units)

    file_fallback_units = _build_file_level_fallback_units(
        config=config,
        diff_hunks_output=diff_hunks_output,
        covered_commit_ids=set(methods_by_commit)
        | {unit.commit.commit_id for unit in hunk_fallback_units},
    )
    change_units.extend(file_fallback_units)

    # keep commit units in chronological order if possible based on authored_date,
    # fallback to input order by commit_id
    change_units.sort(
        key=lambda u: (
            u.commit.authored_date or "",
            u.commit.commit_id,
        )
    )

    LOGGER.info(
        "Step7 change unit building finished: %d commit-based change units built from %d changed methods (%d hunk-level fallback units, %d file-level fallback units).",
        len(change_units),
        len(changed_methods),
        len(hunk_fallback_units),
        len(file_fallback_units),
    )

    return ChangeUnitsOutput(change_units=change_units)


# ============================================================
# Index helpers
# ============================================================

def _index_graphs_by_method_uid(method_context_graphs_output: MethodContextGraphsOutput) -> Dict[str, List]:
    result: Dict[str, List] = defaultdict(list)
    for graph in method_context_graphs_output.graphs:
        result[graph.entry_method_uid].append(graph)
    return result


def _index_pairs_by_method_uid(method_hunk_pairs_output: MethodHunkPairsOutput) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for pair in method_hunk_pairs_output.method_hunk_pairs:
        result[pair.method_uid] = pair
    return result


def _index_hunks_by_commit(diff_hunks_output: Optional[DiffHunksOutput]) -> Dict[str, List[Any]]:
    result: Dict[str, List[Any]] = defaultdict(list)
    if diff_hunks_output is None:
        return result
    for hunk in diff_hunks_output.hunks:
        if hunk.commit_id:
            result[hunk.commit_id].append(hunk)
    return result


def _index_file_level_hunks_by_commit(diff_hunks_output: Optional[DiffHunksOutput]) -> Dict[str, List[Any]]:
    result: Dict[str, List[Any]] = defaultdict(list)
    if diff_hunks_output is None:
        return result
    for hunk in getattr(diff_hunks_output, "file_level_hunks", []) or []:
        if hunk.commit_id:
            result[hunk.commit_id].append(hunk)
    return result


# ============================================================
# Commit resolution
# ============================================================

def _resolve_primary_commit(method) -> Tuple[Optional[str], Optional[CommitInfo]]:
    """
    Priority:
    1. method.primary_commit_id
    2. first method.commits
    """
    if method.primary_commit_id and method.commits:
        for commit in method.commits:
            if commit.commit_id == method.primary_commit_id:
                return commit.commit_id, commit

    if method.primary_commit_id:
        # no exact CommitInfo found, but keep ID if possible
        return method.primary_commit_id, _build_minimal_commit_info(method.primary_commit_id)

    if method.commits:
        return method.commits[0].commit_id, method.commits[0]

    return None, None


def _build_minimal_commit_info(commit_id: str) -> CommitInfo:
    return CommitInfo(commit_id=commit_id, subject="", body="")


def _load_commit_infos_from_git_log(config: PipelineConfig) -> Dict[str, CommitInfo]:
    try:
        raw_log = _run_git_log_patch(config.repo_path, config.base_ref, config.new_ref)
        patch_commits = _parse_git_log_output(raw_log)
    except Exception as exc:
        LOGGER.warning("Failed to load commit metadata for hunk-level fallback units: %s", exc)
        return {}

    commit_infos: Dict[str, CommitInfo] = {}
    for patch_commit in patch_commits:
        commit_infos[patch_commit.commit_id] = CommitInfo(
            commit_id=patch_commit.commit_id,
            author_name=patch_commit.author_name,
            author_email=patch_commit.author_email,
            authored_date=patch_commit.authored_date,
            subject=patch_commit.subject,
            body=patch_commit.body,
            files_touched=[],
        )
    return commit_infos


def _build_hunk_level_fallback_units(
    *,
    config: PipelineConfig,
    diff_hunks_output: Optional[DiffHunksOutput],
    covered_commit_ids: set[str],
) -> List[ChangeUnit]:
    hunks_by_commit = _index_hunks_by_commit(diff_hunks_output)
    if not hunks_by_commit:
        return []

    fallback_commit_ids = [
        commit_id
        for commit_id in hunks_by_commit
        if commit_id not in covered_commit_ids
    ]
    if not fallback_commit_ids:
        return []

    commit_infos = _load_commit_infos_from_git_log(config)
    fallback_units: List[ChangeUnit] = []

    for commit_id in fallback_commit_ids:
        hunks = hunks_by_commit[commit_id]
        commit_info = commit_infos.get(commit_id) or _build_minimal_commit_info(commit_id)
        hunk_files = _files_from_hunks(hunks)
        commit_info.files_touched = sorted(set(commit_info.files_touched or []) | set(hunk_files))

        evidence = _build_hunk_level_evidence(commit_info=commit_info, hunks=hunks)
        fallback_units.append(
            ChangeUnit(
                unit_id=_make_unit_id(commit_id),
                commit=commit_info,
                changed_method_uids=[],
                changed_methods=[],
                method_context_graphs=[],
                method_hunk_pairs=[],
                inferred_change_category=_infer_change_category_from_commit(commit_info),
                evidence=evidence,
            )
        )

    return fallback_units


def _build_file_level_fallback_units(
    *,
    config: PipelineConfig,
    diff_hunks_output: Optional[DiffHunksOutput],
    covered_commit_ids: set[str],
) -> List[ChangeUnit]:
    if not bool(getattr(config, "file_level_fallback_enabled", True)):
        return []

    hunks_by_commit = _index_file_level_hunks_by_commit(diff_hunks_output)
    if not hunks_by_commit:
        return []

    fallback_commit_ids = [
        commit_id
        for commit_id in hunks_by_commit
        if commit_id not in covered_commit_ids
    ]
    if not fallback_commit_ids:
        return []

    commit_infos = _load_commit_infos_from_git_log(config)
    fallback_units: List[ChangeUnit] = []

    for commit_id in fallback_commit_ids:
        hunks = hunks_by_commit[commit_id]
        commit_info = commit_infos.get(commit_id) or _build_minimal_commit_info(commit_id)
        hunk_files = _files_from_hunks(hunks)
        commit_info.files_touched = sorted(set(commit_info.files_touched or []) | set(hunk_files))

        evidence = _build_file_level_evidence(commit_info=commit_info, hunks=hunks)
        fallback_units.append(
            ChangeUnit(
                unit_id=_make_unit_id(commit_id),
                commit=commit_info,
                changed_method_uids=[],
                changed_methods=[],
                method_context_graphs=[],
                method_hunk_pairs=[],
                inferred_change_category=_infer_change_category_from_commit(commit_info),
                evidence=evidence,
            )
        )

    return fallback_units


# ============================================================
# Change category inference
# ============================================================

def _infer_change_category_from_commit(commit_info: CommitInfo) -> str:
    text = (commit_info.full_message or "").lower()

    if _contains_any(text, COMMIT_KEYWORDS_SECURITY):
        return CATEGORY_SECURITY
    if _contains_any(text, COMMIT_KEYWORDS_PERFORMANCE):
        return CATEGORY_PERFORMANCE
    if _contains_any(text, COMMIT_KEYWORDS_BUGFIX):
        return CATEGORY_BUGFIX
    if _contains_any(text, COMMIT_KEYWORDS_FEATURE):
        return CATEGORY_FEATURE
    if _contains_any(text, COMMIT_KEYWORDS_REFACTORING):
        return CATEGORY_REFACTORING

    if text.strip():
        return CATEGORY_MAINTENANCE

    return CATEGORY_UNKNOWN


def _contains_any(text: str, keywords: Iterable[str]) -> bool:
    for kw in keywords:
        if kw in text:
            return True
    return False


# ============================================================
# Evidence construction
# ============================================================

def _build_unit_evidence(
    commit_info: CommitInfo,
    methods: Sequence,
    method_graphs: Sequence,
    method_hunk_pairs: Sequence,
) -> Dict[str, Any]:
    files = set()
    qualified_names = []
    change_type_counter: Dict[str, int] = defaultdict(int)

    for method in methods:
        identity = method.new_identity or method.old_identity
        if identity is not None:
            files.add(identity.file_path)
            qualified_names.append(identity.qualified_name)
        change_type_counter[method.change_type] += 1

    matched_hunk_count = 0
    matched_graph_count = 0
    total_graph_nodes = 0
    total_graph_edges = 0

    for pair in method_hunk_pairs:
        if pair.matched_hunks:
            matched_hunk_count += 1

    for graph in method_graphs:
        if graph.nodes or graph.edges:
            matched_graph_count += 1
        total_graph_nodes += len(graph.nodes)
        total_graph_edges += len(graph.edges)

    return {
        "commit_id": commit_info.commit_id,
        "commit_subject": commit_info.subject,
        "evidence_granularity": "method_level",
        "change_detection_status": "method_level_change",
        "fallback_from_diff_hunks": False,
        "files": sorted(files),
        "qualified_names": qualified_names,
        "method_count": len(methods),
        "change_type_distribution": dict(change_type_counter),
        "method_hunk_pair_count": len(method_hunk_pairs),
        "matched_hunk_pair_count": matched_hunk_count,
        "graph_count": len(method_graphs),
        "non_empty_graph_count": matched_graph_count,
        "total_graph_nodes": total_graph_nodes,
        "total_graph_edges": total_graph_edges,
    }


def _build_hunk_level_evidence(commit_info: CommitInfo, hunks: Sequence) -> Dict[str, Any]:
    files = _files_from_hunks(hunks)
    return {
        "commit_id": commit_info.commit_id,
        "commit_subject": commit_info.subject,
        "evidence_granularity": "hunk_level",
        "change_detection_status": "no_method_level_change",
        "fallback_from_diff_hunks": True,
        "files": files,
        "qualified_names": [],
        "method_count": 0,
        "change_type_distribution": {"hunk_only": len(hunks)},
        "method_hunk_pair_count": 0,
        "matched_hunk_pair_count": 0,
        "fallback_hunk_count": len(hunks),
        "hunk_ids": [str(hunk.hunk_id) for hunk in hunks if getattr(hunk, "hunk_id", None)],
        "fallback_diff_hunks": [_serialize_fallback_hunk(hunk) for hunk in hunks],
        "graph_count": 0,
        "non_empty_graph_count": 0,
        "total_graph_nodes": 0,
        "total_graph_edges": 0,
    }


def _build_file_level_evidence(commit_info: CommitInfo, hunks: Sequence) -> Dict[str, Any]:
    files = _files_from_hunks(hunks)
    return {
        "commit_id": commit_info.commit_id,
        "commit_subject": commit_info.subject,
        "evidence_granularity": "file_level",
        "change_detection_status": "non_cpp_file_change",
        "fallback_from_diff_hunks": False,
        "fallback_from_file_diff": True,
        "files": files,
        "qualified_names": [],
        "method_count": 0,
        "change_type_distribution": {"file_only": len(hunks)},
        "method_hunk_pair_count": 0,
        "matched_hunk_pair_count": 0,
        "fallback_file_hunk_count": len(hunks),
        "hunk_ids": [str(hunk.hunk_id) for hunk in hunks if getattr(hunk, "hunk_id", None)],
        "fallback_file_hunks": [_serialize_fallback_hunk(hunk) for hunk in hunks],
        "graph_count": 0,
        "non_empty_graph_count": 0,
        "total_graph_nodes": 0,
        "total_graph_edges": 0,
    }


def _files_from_hunks(hunks: Sequence) -> List[str]:
    files = set()
    for hunk in hunks:
        for value in (getattr(hunk, "file_path_new", None), getattr(hunk, "file_path_old", None)):
            text = str(value or "").strip()
            if text:
                files.add(text)
    return sorted(files)


def _serialize_fallback_hunk(hunk) -> Dict[str, Any]:
    return {
        "hunk_id": hunk.hunk_id,
        "commit_id": hunk.commit_id,
        "file_path_old": hunk.file_path_old,
        "file_path_new": hunk.file_path_new,
        "source_start": hunk.source_start,
        "source_length": hunk.source_length,
        "target_start": hunk.target_start,
        "target_length": hunk.target_length,
        "diff_header": hunk.diff_header,
        "diff_text": hunk.diff_text,
        "added_lines": [_serialize_diff_line(line) for line in hunk.added_lines],
        "deleted_lines": [_serialize_diff_line(line) for line in hunk.deleted_lines],
    }


def _serialize_diff_line(line) -> Dict[str, Any]:
    return {
        "line_no": getattr(line, "line_no", None),
        "text": str(getattr(line, "text", "") or ""),
    }


# ============================================================
# Utility helpers
# ============================================================

def _make_unit_id(commit_id: str) -> str:
    return f"cu_{commit_id[:12]}"

