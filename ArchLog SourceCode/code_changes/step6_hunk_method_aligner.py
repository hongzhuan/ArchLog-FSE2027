from __future__ import annotations

import hashlib
import logging
from collections import defaultdict
from typing import Dict, List, Optional, Sequence, Tuple

from .constants import (
    CHANGE_TYPE_ADDED,
    CHANGE_TYPE_DELETED,
    CHANGE_TYPE_MODIFIED,
    DEFAULT_LOGGER_NAME,
)
from .models import (
    MatchedHunk,
    MethodHunkPair,
    MethodHunkPairsOutput,
    PipelineConfig,
)


LOGGER = logging.getLogger(DEFAULT_LOGGER_NAME)


def run_hunk_method_aligner(
    config: PipelineConfig,
    commits_mapped_output,
    diff_hunks_output,
) -> MethodHunkPairsOutput:
    """
    Align diff hunks to changed methods.

    Inputs:
    - commits_mapped_output: changed methods already mapped to one or more commits
    - diff_hunks_output: concrete hunks extracted from git log -p

    Output:
    - MethodHunkPairsOutput
    """
    hunks_by_commit: Dict[str, List] = defaultdict(list)
    for hunk in diff_hunks_output.hunks:
        hunks_by_commit[hunk.commit_id].append(hunk)

    pairs: List[MethodHunkPair] = []
    for method in commits_mapped_output.changed_methods:
        candidate_hunks = _collect_candidate_hunks(method, hunks_by_commit, diff_hunks_output.hunks)
        matched_hunks = _align_single_method_to_hunks(method, candidate_hunks)

        pair = MethodHunkPair(
            pair_id=_make_pair_id(method.method_uid, matched_hunks),
            method_uid=method.method_uid,
            change_type=method.change_type,
            matched_hunks=matched_hunks,
            all_commit_ids=sorted({mh.commit_id for mh in matched_hunks}),
            primary_commit_id=matched_hunks[0].commit_id if matched_hunks else method.primary_commit_id,
        )
        pairs.append(pair)

    LOGGER.info(
        "Step6 hunk-method alignment finished: %d pairs, %d pairs with at least one matched hunk.",
        len(pairs),
        sum(1 for p in pairs if p.matched_hunks),
    )

    return MethodHunkPairsOutput(method_hunk_pairs=pairs)


# ============================================================
# Candidate collection
# ============================================================

def _collect_candidate_hunks(method, hunks_by_commit: Dict[str, List], all_hunks: Sequence) -> List:
    """
    Prefer method.commits as candidate scope.
    Fallback to all hunks if the method has no mapped commit.
    """
    if method.commits:
        candidates: List = []
        seen_ids = set()
        for commit in method.commits:
            for hunk in hunks_by_commit.get(commit.commit_id, []):
                if hunk.hunk_id in seen_ids:
                    continue
                seen_ids.add(hunk.hunk_id)
                candidates.append(hunk)
        return candidates

    return list(all_hunks)


# ============================================================
# Alignment core
# ============================================================

def _align_single_method_to_hunks(method, candidate_hunks: Sequence) -> List[MatchedHunk]:
    matched: List[MatchedHunk] = []

    for hunk in candidate_hunks:
        if not _method_hunk_file_match(method, hunk):
            continue

        matched_hunk = _try_align_method_hunk(method, hunk)
        if matched_hunk is not None:
            matched.append(matched_hunk)

    matched.sort(key=lambda x: (-x.coverage_score, x.commit_id, x.hunk_id))
    return matched


def _try_align_method_hunk(method, hunk) -> Optional[MatchedHunk]:
    old_identity = method.old_identity
    new_identity = method.new_identity

    matched_old_lines: List[int] = []
    matched_new_lines: List[int] = []
    match_type = "none"
    coverage_score = 0.0

    if method.change_type == CHANGE_TYPE_ADDED:
        if new_identity is None:
            return None

        matched_new_lines = _overlap_new_lines(new_identity.start_line, new_identity.end_line, hunk)
        if matched_new_lines:
            match_type = "added_overlap"
            coverage_score = _compute_coverage_score(
                matched_count=len(matched_new_lines),
                method_span=_span_length(new_identity.start_line, new_identity.end_line),
                changed_side_count=len([x for x in hunk.added_lines if x.line_no is not None]),
            )
        else:
            if _range_overlap(
                new_identity.start_line,
                new_identity.end_line,
                hunk.target_start,
                hunk.target_start + max(hunk.target_length - 1, 0),
            ):
                match_type = "added_hunk_range_overlap"
                coverage_score = 0.15

    elif method.change_type == CHANGE_TYPE_DELETED:
        if old_identity is None:
            return None

        matched_old_lines = _overlap_old_lines(old_identity.start_line, old_identity.end_line, hunk)
        if matched_old_lines:
            match_type = "deleted_overlap"
            coverage_score = _compute_coverage_score(
                matched_count=len(matched_old_lines),
                method_span=_span_length(old_identity.start_line, old_identity.end_line),
                changed_side_count=len([x for x in hunk.deleted_lines if x.line_no is not None]),
            )
        else:
            if _range_overlap(
                old_identity.start_line,
                old_identity.end_line,
                hunk.source_start,
                hunk.source_start + max(hunk.source_length - 1, 0),
            ):
                match_type = "deleted_hunk_range_overlap"
                coverage_score = 0.15

    elif method.change_type == CHANGE_TYPE_MODIFIED:
        if old_identity is not None:
            matched_old_lines = _overlap_old_lines(old_identity.start_line, old_identity.end_line, hunk)
        if new_identity is not None:
            matched_new_lines = _overlap_new_lines(new_identity.start_line, new_identity.end_line, hunk)

        if matched_old_lines and matched_new_lines:
            match_type = "dual_side_overlap"
            coverage_score = max(
                _compute_coverage_score(
                    matched_count=len(matched_old_lines),
                    method_span=_span_length(old_identity.start_line, old_identity.end_line) if old_identity else 1,
                    changed_side_count=len([x for x in hunk.deleted_lines if x.line_no is not None]),
                ),
                _compute_coverage_score(
                    matched_count=len(matched_new_lines),
                    method_span=_span_length(new_identity.start_line, new_identity.end_line) if new_identity else 1,
                    changed_side_count=len([x for x in hunk.added_lines if x.line_no is not None]),
                ),
            ) + 0.10
        elif matched_old_lines:
            match_type = "old_side_overlap"
            coverage_score = _compute_coverage_score(
                matched_count=len(matched_old_lines),
                method_span=_span_length(old_identity.start_line, old_identity.end_line) if old_identity else 1,
                changed_side_count=len([x for x in hunk.deleted_lines if x.line_no is not None]),
            )
        elif matched_new_lines:
            match_type = "new_side_overlap"
            coverage_score = _compute_coverage_score(
                matched_count=len(matched_new_lines),
                method_span=_span_length(new_identity.start_line, new_identity.end_line) if new_identity else 1,
                changed_side_count=len([x for x in hunk.added_lines if x.line_no is not None]),
            )
        else:
            # fallback on whole hunk ranges
            old_range_hit = (
                old_identity is not None and
                _range_overlap(
                    old_identity.start_line,
                    old_identity.end_line,
                    hunk.source_start,
                    hunk.source_start + max(hunk.source_length - 1, 0),
                )
            )
            new_range_hit = (
                new_identity is not None and
                _range_overlap(
                    new_identity.start_line,
                    new_identity.end_line,
                    hunk.target_start,
                    hunk.target_start + max(hunk.target_length - 1, 0),
                )
            )
            if old_range_hit or new_range_hit:
                match_type = "hunk_range_overlap"
                coverage_score = 0.12

    if coverage_score <= 0.0:
        return None

    matched_diff_text = hunk.diff_text.splitlines()

    return MatchedHunk(
        hunk_id=hunk.hunk_id,
        commit_id=hunk.commit_id,
        match_type=match_type,
        coverage_score=round(min(1.0, coverage_score), 6),
        matched_old_lines=matched_old_lines,
        matched_new_lines=matched_new_lines,
        matched_diff_text=matched_diff_text,
    )


# ============================================================
# Overlap / scoring helpers
# ============================================================

def _method_hunk_file_match(method, hunk) -> bool:
    old_path = _normalize_path(method.old_identity.file_path) if method.old_identity else None
    new_path = _normalize_path(method.new_identity.file_path) if method.new_identity else None

    hunk_old = _normalize_path(hunk.file_path_old) if hunk.file_path_old else None
    hunk_new = _normalize_path(hunk.file_path_new) if hunk.file_path_new else None

    return (
        (old_path is not None and (old_path == hunk_old or old_path == hunk_new))
        or (new_path is not None and (new_path == hunk_new or new_path == hunk_old))
    )


def _overlap_old_lines(method_start: int, method_end: int, hunk) -> List[int]:
    deleted_line_nos = [x.line_no for x in hunk.deleted_lines if x.line_no is not None]
    return [ln for ln in deleted_line_nos if method_start <= ln <= method_end]


def _overlap_new_lines(method_start: int, method_end: int, hunk) -> List[int]:
    added_line_nos = [x.line_no for x in hunk.added_lines if x.line_no is not None]
    return [ln for ln in added_line_nos if method_start <= ln <= method_end]


def _compute_coverage_score(matched_count: int, method_span: int, changed_side_count: int) -> float:
    if matched_count <= 0:
        return 0.0

    method_span = max(1, method_span)
    changed_side_count = max(1, changed_side_count)

    method_ratio = matched_count / method_span
    changed_ratio = matched_count / changed_side_count

    # bias toward changed-line evidence, but still consider method coverage
    return 0.65 * changed_ratio + 0.35 * method_ratio


def _span_length(start_line: int, end_line: int) -> int:
    if end_line < start_line:
        return 1
    return end_line - start_line + 1


def _range_overlap(a_start: int, a_end: int, b_start: int, b_end: int) -> bool:
    return not (a_end < b_start or b_end < a_start)


def _make_pair_id(method_uid: str, matched_hunks: Sequence[MatchedHunk]) -> str:
    hunk_part = "|".join(f"{mh.hunk_id}:{mh.commit_id}" for mh in matched_hunks)
    raw = f"{method_uid}|{hunk_part}"
    digest = hashlib.md5(raw.encode("utf-8")).hexdigest()[:12]
    return f"mhp_{digest}"


def _normalize_path(path: Optional[str]) -> Optional[str]:
    if path is None:
        return None
    return path.replace("\\", "/").strip()