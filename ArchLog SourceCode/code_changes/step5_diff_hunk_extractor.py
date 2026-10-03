from __future__ import annotations

import logging
import re
import subprocess
from dataclasses import dataclass, field
from fnmatch import fnmatch
from pathlib import Path
from typing import List, Optional, Sequence, Tuple

from .constants import DEFAULT_LOGGER_NAME, PATCH_HEADER_PREFIX
from .models import DiffHunk, DiffHunksOutput, DiffLine, PipelineConfig


LOGGER = logging.getLogger(DEFAULT_LOGGER_NAME)


SUPPORTED_CPP_EXTENSIONS = {
    ".c",
    ".cc",
    ".cpp",
    ".cxx",
    ".h",
    ".hh",
    ".hpp",
    ".hxx",
}

HUNK_HEADER_RE = re.compile(
    r"^@@\s*-(?P<src_start>\d+)(?:,(?P<src_len>\d+))?\s+\+(?P<tgt_start>\d+)(?:,(?P<tgt_len>\d+))?\s*@@(?P<tail>.*)$"
)


@dataclass
class PatchCommit:
    commit_id: str
    author_name: Optional[str] = None
    author_email: Optional[str] = None
    authored_date: Optional[str] = None
    subject: str = ""
    body: str = ""
    patch_lines: List[str] = field(default_factory=list)


@dataclass
class FilePatch:
    old_path: Optional[str]
    new_path: Optional[str]
    lines: List[str] = field(default_factory=list)


def run_diff_hunk_extractor(config: PipelineConfig) -> DiffHunksOutput:
    """
    Extract diff hunks from:
        git log -p base_ref..new_ref

    Each hunk is associated with a concrete commit_id and file paths.
    C/C++ source/header hunks are retained in ``hunks`` for method alignment.
    Build/config/docs/CI/release/test-resource hunks are retained separately in
    ``file_level_hunks`` for file-level fallback commits.

    Important fix:
    - hunk_id is now globally unique within each commit.
    - Different file patches under the same commit no longer restart hunk numbering.
    """
    repo_path = config.repo_path
    version_range = f"{config.base_ref}..{config.new_ref}"

    raw_log = _run_git_log_patch(repo_path, config.base_ref, config.new_ref)
    commits = _parse_git_log_output(raw_log)

    all_hunks: List[DiffHunk] = []
    file_level_hunks: List[DiffHunk] = []
    for commit in commits:
        file_patches = _split_commit_into_file_patches(commit.patch_lines)

        cpp_hunk_counter = 0
        file_level_hunk_counter = 0

        for file_patch in file_patches:
            if _is_supported_cpp_patch(file_patch):
                hunks, cpp_hunk_counter = _extract_hunks_from_file_patch(
                    commit_id=commit.commit_id,
                    old_path=file_patch.old_path,
                    new_path=file_patch.new_path,
                    patch_lines=file_patch.lines,
                    start_hunk_index=cpp_hunk_counter,
                    hunk_id_prefix="hk",
                )
                all_hunks.extend(hunks)
                continue

            if _is_supported_file_level_fallback_patch(config, file_patch):
                hunks, file_level_hunk_counter = _extract_hunks_from_file_patch(
                    commit_id=commit.commit_id,
                    old_path=file_patch.old_path,
                    new_path=file_patch.new_path,
                    patch_lines=file_patch.lines,
                    start_hunk_index=file_level_hunk_counter,
                    hunk_id_prefix="fhk",
                )
                file_level_hunks.extend(hunks)

    LOGGER.info(
        "Step5 diff hunk extraction finished: %d C/C++ hunks and %d file-level hunks extracted from %d commit(s) in %s.",
        len(all_hunks),
        len(file_level_hunks),
        len(commits),
        version_range,
    )

    return DiffHunksOutput(
        repo_path=repo_path,
        version_range=version_range,
        hunks=all_hunks,
        file_level_hunks=file_level_hunks,
    )


# ============================================================
# Git helpers
# ============================================================

def _run_git_log_patch(repo_path: Path, base_ref: str, new_ref: str) -> str:
    """
    Use a machine-friendly pretty format to simplify parsing.

    --reverse keeps commits in chronological order, which is often easier for debugging.
    """
    pretty = (
        "__ARCRN_COMMIT__:%H%n"
        "__ARCRN_AUTHOR_NAME__:%an%n"
        "__ARCRN_AUTHOR_EMAIL__:%ae%n"
        "__ARCRN_AUTHOR_DATE__:%aI%n"
        "__ARCRN_SUBJECT__:%s%n"
        "__ARCRN_BODY_START__%n%b%n__ARCRN_BODY_END__"
    )

    cmd = [
        "git",
        "log",
        "--reverse",
        "--date=iso-strict",
        f"--pretty=format:{pretty}",
        "-p",
        "--find-renames",
        f"{base_ref}..{new_ref}",
    ]
    result = subprocess.run(
        cmd,
        cwd=str(repo_path),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Git command failed: {' '.join(cmd)}\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )
    return result.stdout


# ============================================================
# Commit-level parsing
# ============================================================

def _parse_git_log_output(raw_text: str) -> List[PatchCommit]:
    lines = raw_text.splitlines()
    commits: List[PatchCommit] = []

    current: Optional[PatchCommit] = None
    in_body = False
    body_lines: List[str] = []
    patch_lines: List[str] = []

    def _flush_current() -> None:
        nonlocal current, body_lines, patch_lines, in_body
        if current is None:
            return
        current.body = "\n".join(body_lines).strip()
        current.patch_lines = list(patch_lines)
        commits.append(current)
        current = None
        body_lines = []
        patch_lines = []
        in_body = False

    for line in lines:
        if line.startswith("__ARCRN_COMMIT__:"):
            _flush_current()
            current = PatchCommit(commit_id=line.split(":", 1)[1].strip())
            continue

        if current is None:
            continue

        if line.startswith("__ARCRN_AUTHOR_NAME__:"):
            current.author_name = line.split(":", 1)[1].strip()
            continue

        if line.startswith("__ARCRN_AUTHOR_EMAIL__:"):
            current.author_email = line.split(":", 1)[1].strip()
            continue

        if line.startswith("__ARCRN_AUTHOR_DATE__:"):
            current.authored_date = line.split(":", 1)[1].strip()
            continue

        if line.startswith("__ARCRN_SUBJECT__:"):
            current.subject = line.split(":", 1)[1]
            continue

        if line == "__ARCRN_BODY_START__":
            in_body = True
            continue

        if line == "__ARCRN_BODY_END__":
            in_body = False
            continue

        if in_body:
            body_lines.append(line)
        else:
            patch_lines.append(line)

    _flush_current()
    return commits


# ============================================================
# File-level patch splitting
# ============================================================

def _split_commit_into_file_patches(patch_lines: List[str]) -> List[FilePatch]:
    """
    Split commit patch into file patches using lines that start with:
      diff --git a/... b/...
    """
    patches: List[FilePatch] = []
    current: Optional[FilePatch] = None

    for line in patch_lines:
        if line.startswith("diff --git "):
            if current is not None:
                patches.append(current)
            old_path, new_path = _parse_diff_git_header(line)
            current = FilePatch(old_path=old_path, new_path=new_path, lines=[line])
            continue

        if current is not None:
            current.lines.append(line)

    if current is not None:
        patches.append(current)

    return patches


def _parse_diff_git_header(line: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Example:
      diff --git a/src/foo.cpp b/src/foo.cpp
    """
    match = re.match(r"^diff --git a/(.+?) b/(.+)$", line.strip())
    if not match:
        return None, None
    return match.group(1), match.group(2)


def _is_supported_cpp_patch(file_patch: FilePatch) -> bool:
    paths = [p for p in [file_patch.old_path, file_patch.new_path] if p]
    return any(Path(p).suffix.lower() in SUPPORTED_CPP_EXTENSIONS for p in paths)


def _is_supported_file_level_fallback_patch(config: PipelineConfig, file_patch: FilePatch) -> bool:
    if not bool(getattr(config, "file_level_fallback_enabled", True)):
        return False

    paths = [_normalize_path(p) for p in [file_patch.old_path, file_patch.new_path] if p]
    if not paths:
        return False

    patterns = getattr(config, "file_level_fallback_patterns", None) or []
    normalized_patterns = [_normalize_path(str(pattern)) for pattern in patterns if str(pattern).strip()]

    return any(
        _path_matches_any_pattern(path, normalized_patterns)
        for path in paths
        if path
    )


def _path_matches_any_pattern(path: str, patterns: Sequence[str]) -> bool:
    normalized = _normalize_path(path)
    basename = Path(normalized).name
    return any(
        fnmatch(normalized, pattern) or fnmatch(basename, pattern)
        for pattern in patterns
    )


# ============================================================
# Hunk extraction
# ============================================================

def _extract_hunks_from_file_patch(
    commit_id: str,
    old_path: Optional[str],
    new_path: Optional[str],
    patch_lines: List[str],
    start_hunk_index: int = 0,
    hunk_id_prefix: str = "hk",
) -> Tuple[List[DiffHunk], int]:
    """
    Parse unified diff hunks from one file patch.

    Returns:
    - hunks parsed from this file patch
    - updated commit-level hunk counter
    """
    effective_old_path = old_path
    effective_new_path = new_path

    # Prefer explicit --- / +++ headers if present, especially for add/delete/rename.
    for line in patch_lines:
        if line.startswith("--- "):
            effective_old_path = _parse_patch_path_header(line, prefix="--- ")
        elif line.startswith("+++ "):
            effective_new_path = _parse_patch_path_header(line, prefix="+++ ")

    hunks: List[DiffHunk] = []
    current_hunk_lines: List[str] = []
    current_header: Optional[str] = None
    commit_hunk_counter = start_hunk_index

    def _flush_current_hunk() -> None:
        nonlocal current_hunk_lines, current_header, commit_hunk_counter
        if current_header is None:
            return

        # Commit-level global increment
        commit_hunk_counter += 1

        parsed = _build_diff_hunk(
            commit_id=commit_id,
            old_path=effective_old_path,
            new_path=effective_new_path,
            header_line=current_header,
            hunk_lines=current_hunk_lines,
            hunk_index=commit_hunk_counter,
            hunk_id_prefix=hunk_id_prefix,
        )
        hunks.append(parsed)
        current_hunk_lines = []
        current_header = None

    for line in patch_lines:
        if line.startswith(PATCH_HEADER_PREFIX):
            _flush_current_hunk()
            current_header = line
            current_hunk_lines = [line]
            continue

        if current_header is not None:
            # Stop only when a new file patch starts; caller already split by file.
            current_hunk_lines.append(line)

    _flush_current_hunk()
    return hunks, commit_hunk_counter


def _parse_patch_path_header(line: str, prefix: str) -> Optional[str]:
    raw = line[len(prefix):].strip()
    if raw == "/dev/null":
        return None
    if raw.startswith("a/") or raw.startswith("b/"):
        return raw[2:]
    return raw


def _build_diff_hunk(
    commit_id: str,
    old_path: Optional[str],
    new_path: Optional[str],
    header_line: str,
    hunk_lines: List[str],
    hunk_index: int,
    hunk_id_prefix: str = "hk",
) -> DiffHunk:
    match = HUNK_HEADER_RE.match(header_line)
    if not match:
        raise ValueError(f"Invalid hunk header: {header_line}")

    source_start = int(match.group("src_start"))
    source_length = int(match.group("src_len") or "1")
    target_start = int(match.group("tgt_start"))
    target_length = int(match.group("tgt_len") or "1")

    added_lines: List[DiffLine] = []
    deleted_lines: List[DiffLine] = []

    old_line_cursor = source_start
    new_line_cursor = target_start

    for line in hunk_lines[1:]:
        if not line:
            # empty line inside patch body is treated as context line with empty text
            old_line_cursor += 1
            new_line_cursor += 1
            continue

        if line.startswith("\\"):
            # \ No newline at end of file
            continue

        prefix = line[0]
        body = line[1:] if len(line) >= 1 else ""

        if prefix == " ":
            old_line_cursor += 1
            new_line_cursor += 1
        elif prefix == "-":
            deleted_lines.append(DiffLine(line_no=old_line_cursor, text=body))
            old_line_cursor += 1
        elif prefix == "+":
            added_lines.append(DiffLine(line_no=new_line_cursor, text=body))
            new_line_cursor += 1
        else:
            # unexpected line, keep parser resilient
            old_line_cursor += 1
            new_line_cursor += 1

    hunk_id = f"{hunk_id_prefix}_{commit_id[:8]}_{hunk_index:04d}"

    return DiffHunk(
        hunk_id=hunk_id,
        commit_id=commit_id,
        file_path_old=_normalize_path(old_path) if old_path else None,
        file_path_new=_normalize_path(new_path) if new_path else None,
        source_start=source_start,
        source_length=source_length,
        target_start=target_start,
        target_length=target_length,
        diff_header=header_line,
        diff_text="\n".join(hunk_lines),
        added_lines=added_lines,
        deleted_lines=deleted_lines,
    )


def _normalize_path(path: str) -> str:
    return path.replace("\\", "/").strip()
