from __future__ import annotations

import copy
import logging
from collections import defaultdict
from typing import Dict, List, Optional, Sequence, Tuple

from .constants import (
    CHANGE_TYPE_ADDED,
    CHANGE_TYPE_DELETED,
    CHANGE_TYPE_MODIFIED,
    DEFAULT_LOGGER_NAME,
)
from .models import ChangedMethod, CommitInfo, CommitsMappedOutput, PipelineConfig
from .step5_diff_hunk_extractor import (
    _parse_git_log_output,
    _run_git_log_patch,
    _split_commit_into_file_patches,
    _extract_hunks_from_file_patch,
    _is_supported_cpp_patch,
)


LOGGER = logging.getLogger(DEFAULT_LOGGER_NAME)


def run_commit_mapper(
    config: PipelineConfig,
    changed_methods_output,
) -> CommitsMappedOutput:
    """
    Map Step1 changed methods to concrete commits in base_ref..new_ref.

    Strategy:
    1. Parse commit history via `git log -p base..new`
    2. Reconstruct commit-level hunks
    3. For each changed method:
       - filter candidate hunks by file path
       - compute old/new line overlap against changed lines
       - attach one or more commits with relevance scores
    4. Set primary_commit_id as the highest-score commit
    """
    raw_log = _run_git_log_patch(config.repo_path, config.base_ref, config.new_ref)
    patch_commits = _parse_git_log_output(raw_log)

    commit_infos: Dict[str, CommitInfo] = {}
    commit_order: Dict[str, int] = {}
    commit_hunks_map: Dict[str, List] = defaultdict(list)

    for idx, patch_commit in enumerate(patch_commits):
        commit_order[patch_commit.commit_id] = idx
        commit_infos[patch_commit.commit_id] = CommitInfo(
            commit_id=patch_commit.commit_id,
            author_name=patch_commit.author_name,
            author_email=patch_commit.author_email,
            authored_date=patch_commit.authored_date,
            subject=patch_commit.subject,
            body=patch_commit.body,
            files_touched=[],
        )

        file_patches = _split_commit_into_file_patches(patch_commit.patch_lines)
        touched_files = set()
        commit_hunk_counter = 0

        for file_patch in file_patches:
            if not _is_supported_cpp_patch(file_patch):
                continue

            if file_patch.old_path:
                touched_files.add(_normalize_path(file_patch.old_path))
            if file_patch.new_path:
                touched_files.add(_normalize_path(file_patch.new_path))

            hunks, commit_hunk_counter = _extract_hunks_from_file_patch(
                commit_id=patch_commit.commit_id,
                old_path=file_patch.old_path,
                new_path=file_patch.new_path,
                patch_lines=file_patch.lines,
                start_hunk_index=commit_hunk_counter,
            )
            commit_hunks_map[patch_commit.commit_id].extend(hunks)

        commit_infos[patch_commit.commit_id].files_touched = sorted(touched_files)

    mapped_methods: List[ChangedMethod] = []
    for method in changed_methods_output.changed_methods:
        method_copy = copy.deepcopy(method)
        matched_commit_infos = _map_single_method_to_commits(
            method=method_copy,
            commit_infos=commit_infos,
            commit_hunks_map=commit_hunks_map,
            commit_order=commit_order,
        )
        method_copy.commits = matched_commit_infos
        method_copy.primary_commit_id = matched_commit_infos[0].commit_id if matched_commit_infos else None
        mapped_methods.append(method_copy)

    LOGGER.info(
        "Step2 commit mapping finished: %d/%d changed methods mapped to at least one commit.",
        sum(1 for m in mapped_methods if m.commits),
        len(mapped_methods),
    )

    return CommitsMappedOutput(changed_methods=mapped_methods)


# ============================================================
# Core mapping
# ============================================================

def _map_single_method_to_commits(
    method: ChangedMethod,
    commit_infos: Dict[str, CommitInfo],
    commit_hunks_map: Dict[str, List],
    commit_order: Dict[str, int],
) -> List[CommitInfo]:
    scores: List[Tuple[str, float]] = []

    for commit_id, hunks in commit_hunks_map.items():
        score = _score_method_commit_relevance(method, hunks)
        if score > 0.0:
            scores.append((commit_id, score))

    # sort by score desc, then chronological order asc
    scores.sort(key=lambda x: (-x[1], commit_order.get(x[0], 10**9)))

    results: List[CommitInfo] = []
    for commit_id, score in scores:
        base = commit_infos[commit_id]
        commit_info = copy.deepcopy(base)
        # attach lightweight evidence without changing model schema
        if not hasattr(method, "evidence") or method.evidence is None:
            method.evidence = {}
        method.evidence.setdefault("commit_mapping", {})
        method.evidence["commit_mapping"].setdefault(commit_id, {})
        method.evidence["commit_mapping"][commit_id]["method_relevance_score"] = round(score, 6)
        method.evidence["commit_mapping"][commit_id]["matched_by"] = [
            "file_path",
            "changed_lines_overlap",
        ]
        results.append(commit_info)

    return results


def _score_method_commit_relevance(method: ChangedMethod, hunks: Sequence) -> float:
    """
    Return a positive score if the commit is relevant to the method.

    Scoring principles:
    - file path must match first
    - then compare changed lines (added/deleted) to method line ranges
    - modified methods can match on old side and/or new side
    - added methods mainly rely on new side
    - deleted methods mainly rely on old side
    """
    old_identity = method.old_identity
    new_identity = method.new_identity

    total_score = 0.0

    for hunk in hunks:
        if not _method_hunk_file_match(method, hunk):
            continue

        hunk_score = 0.0

        if method.change_type == CHANGE_TYPE_ADDED:
            if new_identity is not None:
                new_overlap = _compute_new_side_overlap_score(
                    new_identity.start_line,
                    new_identity.end_line,
                    hunk,
                )
                hunk_score = max(hunk_score, new_overlap)

        elif method.change_type == CHANGE_TYPE_DELETED:
            if old_identity is not None:
                old_overlap = _compute_old_side_overlap_score(
                    old_identity.start_line,
                    old_identity.end_line,
                    hunk,
                )
                hunk_score = max(hunk_score, old_overlap)

        elif method.change_type == CHANGE_TYPE_MODIFIED:
            if old_identity is not None:
                old_overlap = _compute_old_side_overlap_score(
                    old_identity.start_line,
                    old_identity.end_line,
                    hunk,
                )
                hunk_score = max(hunk_score, old_overlap)

            if new_identity is not None:
                new_overlap = _compute_new_side_overlap_score(
                    new_identity.start_line,
                    new_identity.end_line,
                    hunk,
                )
                hunk_score = max(hunk_score, new_overlap)

            # reward dual-side support
            if old_identity is not None and new_identity is not None:
                old_overlap = _compute_old_side_overlap_score(
                    old_identity.start_line,
                    old_identity.end_line,
                    hunk,
                )
                new_overlap = _compute_new_side_overlap_score(
                    new_identity.start_line,
                    new_identity.end_line,
                    hunk,
                )
                if old_overlap > 0.0 and new_overlap > 0.0:
                    hunk_score += 0.15

        total_score += hunk_score

    return total_score


# ============================================================
# Overlap helpers
# ============================================================

def _method_hunk_file_match(method: ChangedMethod, hunk) -> bool:
    old_path = _normalize_path(method.old_identity.file_path) if method.old_identity else None
    new_path = _normalize_path(method.new_identity.file_path) if method.new_identity else None

    hunk_old = _normalize_path(hunk.file_path_old) if hunk.file_path_old else None
    hunk_new = _normalize_path(hunk.file_path_new) if hunk.file_path_new else None

    return (
        (old_path is not None and (old_path == hunk_old or old_path == hunk_new))
        or (new_path is not None and (new_path == hunk_new or new_path == hunk_old))
    )


def _compute_old_side_overlap_score(method_start: int, method_end: int, hunk) -> float:
    deleted_line_nos = [ln.line_no for ln in hunk.deleted_lines if ln.line_no is not None]
    if deleted_line_nos:
        overlap_count = _count_overlap_lines(method_start, method_end, deleted_line_nos)
        if overlap_count > 0:
            return min(1.0, 0.35 + 0.12 * overlap_count)

    # fallback: use source hunk range
    source_lines = _range_from_hunk(hunk.source_start, hunk.source_length)
    overlap_count = _count_overlap_lines(method_start, method_end, source_lines)
    if overlap_count > 0:
        return min(0.5, 0.18 + 0.05 * overlap_count)

    return 0.0


def _compute_new_side_overlap_score(method_start: int, method_end: int, hunk) -> float:
    added_line_nos = [ln.line_no for ln in hunk.added_lines if ln.line_no is not None]
    if added_line_nos:
        overlap_count = _count_overlap_lines(method_start, method_end, added_line_nos)
        if overlap_count > 0:
            return min(1.0, 0.35 + 0.12 * overlap_count)

    # fallback: use target hunk range
    target_lines = _range_from_hunk(hunk.target_start, hunk.target_length)
    overlap_count = _count_overlap_lines(method_start, method_end, target_lines)
    if overlap_count > 0:
        return min(0.5, 0.18 + 0.05 * overlap_count)

    return 0.0


def _count_overlap_lines(method_start: int, method_end: int, line_numbers: Sequence[int]) -> int:
    return sum(1 for ln in line_numbers if method_start <= ln <= method_end)


def _range_from_hunk(start: int, length: int) -> List[int]:
    if length <= 0:
        return []
    return list(range(start, start + length))


def _normalize_path(path: Optional[str]) -> Optional[str]:
    if path is None:
        return None
    return path.replace("\\", "/").strip()