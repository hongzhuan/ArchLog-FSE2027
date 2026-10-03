from __future__ import annotations

import hashlib
import logging
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

from .constants import (
    CHANGE_TYPE_ADDED,
    CHANGE_TYPE_DELETED,
    CHANGE_TYPE_MODIFIED,
    DEFAULT_LOGGER_NAME,
)
from .models import ChangedMethod, ChangedMethodsOutput, MethodIdentity, PipelineConfig


LOGGER = logging.getLogger(DEFAULT_LOGGER_NAME)


# ============================================================
# Tree-sitter loader
# ============================================================

class TreeSitterFacade:
    """
    Wrapper that supports several common Python package layouts:

    1) tree_sitter + tree_sitter_languages
    2) tree_sitter + tree_sitter_cpp / tree_sitter_c
    """

    def __init__(self) -> None:
        self._parser_cache: Dict[str, object] = {}

    def get_parser(self, language_name: str):
        language_name = language_name.lower().strip()
        if language_name in self._parser_cache:
            return self._parser_cache[language_name]

        parser = self._build_parser(language_name)
        self._parser_cache[language_name] = parser
        return parser

    def _build_parser(self, language_name: str):
        try:
            from tree_sitter import Language, Parser  # type: ignore
        except ImportError as exc:
            raise RuntimeError(
                "tree_sitter is required for step1_method_change_localizer, "
                "but it is not installed."
            ) from exc

        # Option 1: tree_sitter_languages
        try:
            from tree_sitter_languages import get_language  # type: ignore

            lang = get_language(language_name)
            parser = Parser()
            try:
                parser.set_language(lang)
            except AttributeError:
                parser.language = lang
            return parser
        except Exception:
            pass

        # Option 2: tree_sitter_cpp / tree_sitter_c
        lang = None
        if language_name == "cpp":
            try:
                import tree_sitter_cpp  # type: ignore

                lang = Language(tree_sitter_cpp.language())
            except Exception:
                pass
        elif language_name == "c":
            try:
                import tree_sitter_c  # type: ignore

                lang = Language(tree_sitter_c.language())
            except Exception:
                pass

        if lang is None:
            raise RuntimeError(
                f"Unable to initialize tree-sitter parser for language '{language_name}'. "
                "Install either 'tree_sitter_languages' or the corresponding language binding."
            )

        parser = Parser()
        try:
            parser.set_language(lang)
        except AttributeError:
            parser.language = lang
        return parser


_TREE_SITTER = TreeSitterFacade()


# ============================================================
# Internal constants / models
# ============================================================

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


@dataclass
class GitFileChange:
    status: str
    path_old: Optional[str]
    path_new: Optional[str]


@dataclass
class FileDiffHunk:
    """
    File-level hunk for version diff (base_ref..new_ref), not commit-level.
    """
    file_path_old: Optional[str]
    file_path_new: Optional[str]
    source_start: int
    source_length: int
    target_start: int
    target_length: int
    diff_header: str
    diff_text: str
    hunk_id: str

    # exact changed lines parsed from hunk body
    changed_old_lines: List[int] = field(default_factory=list)
    changed_new_lines: List[int] = field(default_factory=list)


@dataclass
class ParsedCallable:
    """
    Occurrence-level callable definition.
    Important: do NOT assume (qualified_name, file_path) is unique.
    """
    callable_id: str
    qualified_name: str
    simple_name: str
    category: str
    file_path: str

    definition_start_line: int
    definition_end_line: int
    definition_start_offset: Optional[int]
    definition_end_offset: Optional[int]

    signature_start_line: Optional[int]
    signature_end_line: Optional[int]

    body_start_line: Optional[int]
    body_end_line: Optional[int]

    return_type: Optional[str]
    parameters: List[str]
    parent_qualified_name: Optional[str]

    raw_definition_text: Optional[str] = None
    raw_signature_text: Optional[str] = None
    raw_body_text: Optional[str] = None


@dataclass
class HunkHit:
    hunk_id: str
    overlap_kind: str  # body / signature / definition
    source_start: int
    source_length: int
    target_start: int
    target_length: int


@dataclass
class HunkHitInfo:
    hits: List[HunkHit] = field(default_factory=list)

    def add_hit(self, hit: HunkHit) -> None:
        self.hits.append(hit)

    @property
    def has_hit(self) -> bool:
        return bool(self.hits)

    def overlap_kinds(self) -> List[str]:
        return [h.overlap_kind for h in self.hits]

    def hunk_ids(self) -> List[str]:
        return [h.hunk_id for h in self.hits]


@dataclass
class CallableMatch:
    old_callable: Optional[ParsedCallable]
    new_callable: Optional[ParsedCallable]
    match_kind: str   # strong / medium / unmatched_old / unmatched_new
    match_score: float


# ============================================================
# Public entry
# ============================================================

def run_method_change_localizer(config: PipelineConfig) -> ChangedMethodsOutput:
    """
    New step1 skeleton:

    1. collect changed C/C++ files
    2. collect version-level file hunks (base_ref..new_ref)
    3. parse old/new callable definitions
    4. use hunk overlap to identify modified methods
    5. conservatively detect added / deleted
    6. merge same logical methods for output

    Current stage:
    - hunk-driven modified detection is implemented
    - added/deleted remains conservative
    - advanced strong/medium/weak callable matching is NOT implemented yet
    """
    repo_path = config.repo_path
    base_ref = config.base_ref
    new_ref = config.new_ref

    file_changes = _git_diff_name_status(repo_path, base_ref, new_ref)
    file_changes = [fc for fc in file_changes if _is_supported_cpp_file_change(fc)]

    # Version-level file hunks, used by step1 itself.
    file_hunks_map = _collect_file_hunks(repo_path, base_ref, new_ref, file_changes)

    all_changed_methods: List[ChangedMethod] = []

    for fc in file_changes:
        old_path, new_path = _resolve_old_new_paths(fc)

        old_content = _git_read_file(repo_path, base_ref, old_path) if old_path else None
        new_content = _git_read_file(repo_path, new_ref, new_path) if new_path else None

        effective_old_path = old_path or new_path
        effective_new_path = new_path or old_path

        old_callables = (
            _parse_callables_for_file(effective_old_path, old_content)
            if (effective_old_path and old_content is not None)
            else []
        )
        new_callables = (
            _parse_callables_for_file(effective_new_path, new_content)
            if (effective_new_path and new_content is not None)
            else []
        )

        file_hunks = _lookup_file_hunks(file_hunks_map, old_path, new_path)

        old_hit_map = _mark_hunk_hits_on_callables(old_callables, file_hunks, side="old")
        new_hit_map = _mark_hunk_hits_on_callables(new_callables, file_hunks, side="new")

        file_changed_methods = _detect_changed_methods_for_file(
            file_change=fc,
            old_callables=old_callables,
            new_callables=new_callables,
            old_content=old_content,
            new_content=new_content,
            old_hit_map=old_hit_map,
            new_hit_map=new_hit_map,
        )

        # Keep occurrence-level changed methods.
        # Do NOT merge same qualified_name across different occurrences,
        # because #if/#else may contain multiple changed definitions of the
        # same logical method and we need to preserve each occurrence.
        all_changed_methods.extend(file_changed_methods)

    all_changed_methods = _deduplicate_changed_methods(all_changed_methods)

    LOGGER.info(
        "Step1 method localization finished: %d changed method(s) found between %s and %s.",
        len(all_changed_methods),
        base_ref,
        new_ref,
    )

    return ChangedMethodsOutput(
        repo_path=repo_path,
        base_ref=base_ref,
        new_ref=new_ref,
        changed_methods=all_changed_methods,
    )


# ============================================================
# Git helpers
# ============================================================

def _run_git(repo_path: Path, args: Sequence[str]) -> str:
    cmd = ["git", *args]
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


def _git_diff_name_status(repo_path: Path, base_ref: str, new_ref: str) -> List[GitFileChange]:
    output = _run_git(
        repo_path,
        ["diff", "--name-status", "--find-renames", base_ref, new_ref],
    )

    changes: List[GitFileChange] = []
    for raw_line in output.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        parts = line.split("\t")
        status = parts[0]

        if status.startswith("R") or status.startswith("C"):
            if len(parts) >= 3:
                changes.append(GitFileChange(status=status, path_old=parts[1], path_new=parts[2]))
        else:
            if len(parts) < 2:
                continue
            path = parts[1]
            if status == "A":
                changes.append(GitFileChange(status=status, path_old=None, path_new=path))
            elif status == "D":
                changes.append(GitFileChange(status=status, path_old=path, path_new=None))
            else:
                changes.append(GitFileChange(status=status, path_old=path, path_new=path))

    return changes


def _git_read_file(repo_path: Path, ref: str, file_path: Optional[str]) -> Optional[str]:
    if not file_path:
        return None

    spec = f"{ref}:{file_path}"
    result = subprocess.run(
        ["git", "show", spec],
        cwd=str(repo_path),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        return None
    return result.stdout.decode("utf-8", errors="replace")


def _resolve_old_new_paths(change: GitFileChange) -> Tuple[Optional[str], Optional[str]]:
    return change.path_old, change.path_new


def _is_supported_cpp_file_change(change: GitFileChange) -> bool:
    paths = [p for p in (change.path_old, change.path_new) if p]
    return any(Path(p).suffix.lower() in SUPPORTED_CPP_EXTENSIONS for p in paths)


# ============================================================
# File-level hunks for step1 (version diff)
# ============================================================

def _collect_file_hunks(
    repo_path: Path,
    base_ref: str,
    new_ref: str,
    file_changes: List[GitFileChange],
) -> Dict[str, List[FileDiffHunk]]:
    """
    Collect version-level file hunks for step1.
    Keyed by normalized file path, so both old/new paths can retrieve them.
    """
    result: Dict[str, List[FileDiffHunk]] = {}

    for fc in file_changes:
        old_path, new_path = _resolve_old_new_paths(fc)
        target_path = new_path or old_path
        if not target_path:
            continue

        patch_text = _run_git(
            repo_path,
            ["diff", "--find-renames", "--unified=3", base_ref, new_ref, "--", target_path],
        )
        if not patch_text.strip():
            continue

        file_hunks = _extract_file_hunks_from_patch(
            patch_text=patch_text,
            path_old=old_path,
            path_new=new_path,
        )

        for key_path in {p for p in (old_path, new_path) if p}:
            result[_normalize_path(key_path)] = list(file_hunks)

    return result


def _lookup_file_hunks(
    file_hunks_map: Dict[str, List[FileDiffHunk]],
    old_path: Optional[str],
    new_path: Optional[str],
) -> List[FileDiffHunk]:
    keys = [_normalize_path(p) for p in (old_path, new_path) if p]
    for key in keys:
        if key in file_hunks_map:
            return file_hunks_map[key]
    return []


def _extract_file_hunks_from_patch(
    patch_text: str,
    path_old: Optional[str],
    path_new: Optional[str],
) -> List[FileDiffHunk]:
    """
    Parse unified diff hunks from git diff output for a single file.

    Important:
    - besides hunk header ranges, also parse exact changed old/new line numbers
      from hunk body
    """
    lines = patch_text.splitlines()
    hunks: List[FileDiffHunk] = []

    hunk_header_pattern = re.compile(
        r"^@@\s+\-(\d+)(?:,(\d+))?\s+\+(\d+)(?:,(\d+))?\s+@@"
    )

    i = 0
    hunk_index = 0
    while i < len(lines):
        line = lines[i]
        m = hunk_header_pattern.match(line)
        if not m:
            i += 1
            continue

        src_start = int(m.group(1))
        src_len = int(m.group(2) or "1")
        tgt_start = int(m.group(3))
        tgt_len = int(m.group(4) or "1")

        header = line
        body_lines = [line]
        i += 1
        while i < len(lines) and not hunk_header_pattern.match(lines[i]):
            body_lines.append(lines[i])
            i += 1

        hunk_index += 1
        hunk_raw = "\n".join(body_lines)
        hunk_id = _make_hunk_id(path_old, path_new, hunk_index, header)

        changed_old_lines, changed_new_lines = _parse_exact_changed_lines_from_hunk(
            source_start=src_start,
            target_start=tgt_start,
            hunk_lines=body_lines[1:],  # exclude header
        )

        hunks.append(
            FileDiffHunk(
                file_path_old=path_old,
                file_path_new=path_new,
                source_start=src_start,
                source_length=src_len,
                target_start=tgt_start,
                target_length=tgt_len,
                diff_header=header,
                diff_text=hunk_raw,
                hunk_id=hunk_id,
                changed_old_lines=changed_old_lines,
                changed_new_lines=changed_new_lines,
            )
        )

    return hunks


def _parse_exact_changed_lines_from_hunk(
    source_start: int,
    target_start: int,
    hunk_lines: List[str],
) -> Tuple[List[int], List[int]]:
    """
    Parse exact changed line numbers from a unified diff hunk body.

    Rules:
    - ' '  context line: old_line++, new_line++
    - '-'  deletion line: old_line changed, old_line++
    - '+'  addition line: new_line changed, new_line++
    - '\\ No newline at end of file' : ignore
    """
    old_line = source_start
    new_line = target_start

    changed_old: List[int] = []
    changed_new: List[int] = []

    for raw in hunk_lines:
        if not raw:
            # defensive fallback: treat as context
            old_line += 1
            new_line += 1
            continue

        if raw.startswith("\\"):
            # e.g. "\ No newline at end of file"
            continue

        prefix = raw[0]

        if prefix == " ":
            old_line += 1
            new_line += 1
        elif prefix == "-":
            changed_old.append(old_line)
            old_line += 1
        elif prefix == "+":
            changed_new.append(new_line)
            new_line += 1
        else:
            # defensive fallback: treat as context
            old_line += 1
            new_line += 1

    return changed_old, changed_new


def _make_hunk_id(
    path_old: Optional[str],
    path_new: Optional[str],
    index: int,
    header: str,
) -> str:
    raw = f"{path_old or ''}|{path_new or ''}|{index}|{header}"
    digest = hashlib.md5(raw.encode("utf-8")).hexdigest()[:12]
    return f"vh_{digest}"


# ============================================================
# Parsing
# ============================================================

def _parse_callables_for_file(file_path: str, content: str) -> List[ParsedCallable]:
    suffix = Path(file_path).suffix.lower()
    lang = "c" if suffix == ".c" else "cpp"
    parser = _TREE_SITTER.get_parser(lang)
    source_bytes = content.encode("utf-8", errors="replace")
    tree = parser.parse(source_bytes)

    results: List[ParsedCallable] = []
    _walk_tree_for_callables(
        node=tree.root_node,
        source_bytes=source_bytes,
        file_path=file_path,
        scope_stack=[],
        results=results,
    )
    return _deduplicate_callables(results)


def _walk_tree_for_callables(
    node,
    source_bytes: bytes,
    file_path: str,
    scope_stack: List[str],
    results: List[ParsedCallable],
) -> None:
    node_type = node.type
    new_scope_stack = list(scope_stack)

    if node_type in {"namespace_definition", "class_specifier", "struct_specifier", "union_specifier"}:
        scope_name = _extract_scope_name(node, source_bytes)
        if scope_name:
            new_scope_stack.append(scope_name)

    if node_type == "function_definition":
        parsed = _extract_callable_from_function_definition(
            node=node,
            source_bytes=source_bytes,
            file_path=file_path,
            scope_stack=new_scope_stack,
        )
        if parsed is not None:
            results.append(parsed)

    for child in node.children:
        _walk_tree_for_callables(
            node=child,
            source_bytes=source_bytes,
            file_path=file_path,
            scope_stack=new_scope_stack,
            results=results,
        )


def _extract_scope_name(node, source_bytes: bytes) -> Optional[str]:
    name_node = node.child_by_field_name("name")
    if name_node is not None:
        return _node_text(name_node, source_bytes).strip()

    text = _node_text(node, source_bytes)
    match = re.search(r"\b([A-Za-z_]\w*)\b", text)
    return match.group(1) if match else None


def _extract_callable_from_function_definition(
    node,
    source_bytes: bytes,
    file_path: str,
    scope_stack: List[str],
) -> Optional[ParsedCallable]:
    declarator = node.child_by_field_name("declarator")
    type_node = node.child_by_field_name("type")
    body_node = node.child_by_field_name("body")

    if declarator is None:
        declarator = _find_first_descendant_by_types(
            node,
            {
                "function_declarator",
                "pointer_declarator",
                "reference_declarator",
                "qualified_identifier",
                "identifier",
            },
        )
        if declarator is None:
            return None

    decl_text = _node_text(declarator, source_bytes).strip()
    if not decl_text:
        return None

    simple_name, explicit_scope, parameters = _extract_name_scope_params_from_declarator_text(decl_text)
    if not simple_name:
        return None

    category = "Method" if explicit_scope or scope_stack else "Function"
    if simple_name.startswith("~"):
        category = "Destructor"

    qualified_name = _compose_qualified_name(scope_stack, explicit_scope, simple_name)
    parent_qualified_name = _compose_parent_qualified_name(scope_stack, explicit_scope)
    return_type = _node_text(type_node, source_bytes).strip() if type_node is not None else None

    definition_start_line = node.start_point[0] + 1
    definition_end_line = node.end_point[0] + 1
    definition_start_offset = node.start_byte
    definition_end_offset = node.end_byte

    # Signature range: from function_definition start to body start - 1
    if body_node is not None:
        body_start_line = body_node.start_point[0] + 1
        body_end_line = body_node.end_point[0] + 1
        signature_start_line = definition_start_line
        signature_end_line = max(definition_start_line, body_start_line - 1)
        raw_body_text = _node_text(body_node, source_bytes)
    else:
        body_start_line = None
        body_end_line = None
        signature_start_line = definition_start_line
        signature_end_line = definition_end_line
        raw_body_text = None

    raw_definition_text = _node_text(node, source_bytes)
    raw_signature_text = _extract_source_slice(
        raw_definition_text,
        1,
        max(1, (signature_end_line or definition_end_line) - definition_start_line + 1),
    )

    callable_id = _make_callable_occurrence_id(
        file_path=file_path,
        qualified_name=qualified_name,
        start_line=definition_start_line,
        end_line=definition_end_line,
    )

    return ParsedCallable(
        callable_id=callable_id,
        qualified_name=qualified_name,
        simple_name=simple_name,
        category=category,
        file_path=file_path,
        definition_start_line=definition_start_line,
        definition_end_line=definition_end_line,
        definition_start_offset=definition_start_offset,
        definition_end_offset=definition_end_offset,
        signature_start_line=signature_start_line,
        signature_end_line=signature_end_line,
        body_start_line=body_start_line,
        body_end_line=body_end_line,
        return_type=return_type,
        parameters=parameters,
        parent_qualified_name=parent_qualified_name,
        raw_definition_text=raw_definition_text,
        raw_signature_text=raw_signature_text,
        raw_body_text=raw_body_text,
    )


def _make_callable_occurrence_id(
    file_path: str,
    qualified_name: str,
    start_line: int,
    end_line: int,
) -> str:
    raw = f"{_normalize_path(file_path)}|{qualified_name}|{start_line}|{end_line}"
    digest = hashlib.md5(raw.encode("utf-8")).hexdigest()[:12]
    return f"occ_{digest}"


def _find_first_descendant_by_types(node, type_names: Set[str]):
    stack = [node]
    while stack:
        current = stack.pop()
        if current.type in type_names:
            return current
        stack.extend(reversed(current.children))
    return None


def _extract_name_scope_params_from_declarator_text(
    declarator_text: str,
) -> Tuple[Optional[str], List[str], List[str]]:
    """
    Approximate parser for C/C++ declarator text.
    """
    text = " ".join(declarator_text.replace("\n", " ").split())

    match = re.search(r"(?P<head>.+?)\((?P<params>.*)\)", text)
    if not match:
        return None, [], []

    head = match.group("head").strip()
    params_text = match.group("params").strip()

    head = re.sub(r"^[*&\s]+", "", head).strip()

    name_match = re.search(
        r"(?P<full>(?:[A-Za-z_]\w*::)*~?[A-Za-z_]\w*|(?:[A-Za-z_]\w*::)*operator[^\s(]+)$",
        head,
    )
    if not name_match:
        tail = head.split()[-1] if head.split() else ""
        tail = tail.strip()
        if not tail:
            return None, [], _split_params(params_text)
        full_name = tail
    else:
        full_name = name_match.group("full").strip()

    parts = [p for p in full_name.split("::") if p]
    if not parts:
        return None, [], _split_params(params_text)

    simple_name = parts[-1]
    explicit_scope = parts[:-1]
    parameters = _split_params(params_text)
    return simple_name, explicit_scope, parameters


def _split_params(params_text: str) -> List[str]:
    if not params_text or params_text == "void":
        return []

    params: List[str] = []
    current: List[str] = []
    depth_angle = 0
    depth_paren = 0
    depth_bracket = 0

    for ch in params_text:
        if ch == "<":
            depth_angle += 1
        elif ch == ">":
            depth_angle = max(0, depth_angle - 1)
        elif ch == "(":
            depth_paren += 1
        elif ch == ")":
            depth_paren = max(0, depth_paren - 1)
        elif ch == "[":
            depth_bracket += 1
        elif ch == "]":
            depth_bracket = max(0, depth_bracket - 1)

        if ch == "," and depth_angle == 0 and depth_paren == 0 and depth_bracket == 0:
            param = "".join(current).strip()
            if param:
                params.append(param)
            current = []
            continue

        current.append(ch)

    tail = "".join(current).strip()
    if tail:
        params.append(tail)
    return params


def _compose_qualified_name(scope_stack: List[str], explicit_scope: List[str], simple_name: str) -> str:
    if explicit_scope:
        return "::".join([*explicit_scope, simple_name])
    if scope_stack:
        return "::".join([*scope_stack, simple_name])
    return simple_name


def _compose_parent_qualified_name(scope_stack: List[str], explicit_scope: List[str]) -> Optional[str]:
    if explicit_scope:
        return "::".join(explicit_scope)
    if scope_stack:
        return "::".join(scope_stack)
    return None


def _node_text(node, source_bytes: bytes) -> str:
    return source_bytes[node.start_byte:node.end_byte].decode("utf-8", errors="replace")


def _deduplicate_callables(callables: List[ParsedCallable]) -> List[ParsedCallable]:
    seen = set()
    result: List[ParsedCallable] = []
    for item in callables:
        key = (
            item.qualified_name,
            _normalize_path(item.file_path),
            item.definition_start_line,
            item.definition_end_line,
        )
        if key in seen:
            continue
        seen.add(key)
        result.append(item)
    return result


# ============================================================
# Hunk-driven modified detection
# ============================================================

def _mark_hunk_hits_on_callables(
    callables: List[ParsedCallable],
    hunks: List[FileDiffHunk],
    side: str,  # "old" or "new"
) -> Dict[str, HunkHitInfo]:
    """
    New policy:
    - use exact changed lines inside hunk body, not coarse hunk header range
    """
    result: Dict[str, HunkHitInfo] = {c.callable_id: HunkHitInfo() for c in callables}

    for hunk in hunks:
        changed_lines = hunk.changed_old_lines if side == "old" else hunk.changed_new_lines
        if not changed_lines:
            continue

        changed_line_set = set(changed_lines)

        for c in callables:
            overlap_kind = _classify_changed_lines_callable_overlap(changed_line_set, c)
            if overlap_kind is None:
                continue

            result[c.callable_id].add_hit(
                HunkHit(
                    hunk_id=hunk.hunk_id,
                    overlap_kind=overlap_kind,
                    source_start=hunk.source_start,
                    source_length=hunk.source_length,
                    target_start=hunk.target_start,
                    target_length=hunk.target_length,
                )
            )

    return result


def _classify_changed_lines_callable_overlap(
    changed_lines: Set[int],
    callable_item: ParsedCallable,
) -> Optional[str]:
    """
    Decide whether exact changed lines fall into callable body/signature/definition.
    Priority:
      body > signature > definition
    """
    if callable_item.body_start_line is not None and callable_item.body_end_line is not None:
        if _line_set_overlaps_range(changed_lines, callable_item.body_start_line, callable_item.body_end_line):
            return "body"

    if callable_item.signature_start_line is not None and callable_item.signature_end_line is not None:
        if _line_set_overlaps_range(
            changed_lines,
            callable_item.signature_start_line,
            callable_item.signature_end_line,
        ):
            return "signature"

    if _line_set_overlaps_range(
        changed_lines,
        callable_item.definition_start_line,
        callable_item.definition_end_line,
    ):
        return "definition"

    return None


def _line_set_overlaps_range(
    changed_lines: Set[int],
    start_line: int,
    end_line: int,
) -> bool:
    if not changed_lines:
        return False
    for ln in changed_lines:
        if start_line <= ln <= end_line:
            return True
    return False


def _get_hunk_line_range(hunk: FileDiffHunk, side: str) -> Tuple[Optional[int], Optional[int]]:
    if side == "old":
        start = hunk.source_start
        length = hunk.source_length
    else:
        start = hunk.target_start
        length = hunk.target_length

    if start <= 0:
        return None, None

    end = start + max(length, 1) - 1
    return start, end


def _classify_hunk_callable_overlap(
    hunk_start: int,
    hunk_end: int,
    callable_item: ParsedCallable,
) -> Optional[str]:
    if callable_item.body_start_line is not None and callable_item.body_end_line is not None:
        if _line_ranges_overlap(hunk_start, hunk_end, callable_item.body_start_line, callable_item.body_end_line):
            return "body"

    if callable_item.signature_start_line is not None and callable_item.signature_end_line is not None:
        if _line_ranges_overlap(
            hunk_start,
            hunk_end,
            callable_item.signature_start_line,
            callable_item.signature_end_line,
        ):
            return "signature"

    if _line_ranges_overlap(
        hunk_start,
        hunk_end,
        callable_item.definition_start_line,
        callable_item.definition_end_line,
    ):
        return "definition"

    return None


def _line_ranges_overlap(
    a_start: int,
    a_end: int,
    b_start: int,
    b_end: int,
) -> bool:
    return not (a_end < b_start or b_end < a_start)


# ============================================================
# Detect changes for a single file
# ============================================================

def _detect_changed_methods_for_file(
    file_change: GitFileChange,
    old_callables: List[ParsedCallable],
    new_callables: List[ParsedCallable],
    old_content: Optional[str],
    new_content: Optional[str],
    old_hit_map: Dict[str, HunkHitInfo],
    new_hit_map: Dict[str, HunkHitInfo],
) -> List[ChangedMethod]:
    """
    Improved policy:

    1. global callable matching:
       - strong match
       - medium match

    2. for matched old/new pairs:
       classify as modified if any of:
       - hunk overlap on old/new
       - signature changed
       - body changed

    3. for unmatched old/new:
       - deleted / added
       - but try to avoid converting signature-changed methods into add+delete
         (already mitigated by medium matching)
    """
    matches = _match_callables(old_callables, new_callables)

    changed: List[ChangedMethod] = []

    for match in matches:
        old_item = match.old_callable
        new_item = match.new_callable

        if old_item is not None and new_item is not None:
            old_hit = old_hit_map.get(old_item.callable_id, HunkHitInfo())
            new_hit = new_hit_map.get(new_item.callable_id, HunkHitInfo())

            mod_reasons: List[str] = []
            evidence_hunks: List[str] = []

            if old_hit.has_hit or new_hit.has_hit:
                mod_reasons.append("hunk_overlap")
                evidence_hunks.extend(old_hit.hunk_ids())
                evidence_hunks.extend(new_hit.hunk_ids())

            if _signature_changed(old_item, new_item):
                mod_reasons.append("signature_changed")

            if _body_changed(old_item, new_item):
                mod_reasons.append("body_changed")

            # conservative fallback:
            # if medium matched and definition changed, treat as modified
            if match.match_kind == "medium" and _definition_changed(old_item, new_item):
                mod_reasons.append("definition_changed")

            if mod_reasons:
                changed.append(
                    _build_changed_method_modified(
                        old_parsed=old_item,
                        new_parsed=new_item,
                        mod_reasons=sorted(set(mod_reasons)),
                        evidence_hunks=sorted(set(evidence_hunks)),
                        old_hit_info=old_hit,
                        new_hit_info=new_hit,
                        match_kind=match.match_kind,
                        match_score=match.match_score,
                    )
                )

        elif old_item is not None and new_item is None:
            old_hit = old_hit_map.get(old_item.callable_id, HunkHitInfo())

            changed.append(
                _build_changed_method_deleted(
                    parsed=old_item,
                    file_path_old=file_change.path_old or old_item.file_path,
                    old_hit_info=old_hit,
                )
            )

        elif old_item is None and new_item is not None:
            new_hit = new_hit_map.get(new_item.callable_id, HunkHitInfo())

            changed.append(
                _build_changed_method_added(
                    parsed=new_item,
                    file_path_new=file_change.path_new or new_item.file_path,
                    new_hit_info=new_hit,
                )
            )

    return changed


def _normalize_ws(text: str) -> str:
    return " ".join(text.split())


def _normalized_signature_key(item: ParsedCallable) -> str:
    """
    Strong-match key:
    qualified_name + normalized return type + normalized parameter list
    """
    return_type = _normalize_type_text(item.return_type or "")
    params = ",".join(_normalize_parameter_text(p) for p in item.parameters)
    return "::".join(
        [
            item.qualified_name.strip(),
            return_type,
            params,
        ]
    )


def _normalized_signature_shape(item: ParsedCallable) -> str:
    """
    Medium-match key:
    simple_name + parent scope + param count
    Used for signature-changed matching.
    """
    parent = (item.parent_qualified_name or "").strip()
    return "::".join(
        [
            parent,
            item.simple_name.strip(),
            str(len(item.parameters)),
        ]
    )


def _normalize_type_text(text: str) -> str:
    text = _normalize_ws(text)
    if not text:
        return ""

    # normalize spaces around symbols
    text = re.sub(r"\s*([*&,:<>()=\[\]])\s*", r"\1", text)
    text = text.replace("const&", "const &").replace("const*", "const *")
    text = _normalize_ws(text)

    # very lightweight normalization for attribute-like tokens / macros
    text = text.replace("[[ noreturn ]]", "[[noreturn]]")
    text = text.replace("[[noreturn ]]", "[[noreturn]]")
    text = text.replace("[[ noreturn]]", "[[noreturn]]")

    return text.strip()


def _normalize_parameter_text(text: str) -> str:
    text = text.strip()
    text = _normalize_ws(text)
    text = re.sub(r"\s*([*&,:<>()=\[\]])\s*", r"\1", text)
    text = text.replace("const&", "const &").replace("const*", "const *")
    return _normalize_ws(text)


def _signature_changed(old_item: ParsedCallable, new_item: ParsedCallable) -> bool:
    return _normalized_signature_key(old_item) != _normalized_signature_key(new_item)


def _body_changed(old_item: ParsedCallable, new_item: ParsedCallable) -> bool:
    old_body = _normalize_code_for_compare(old_item.raw_body_text or "")
    new_body = _normalize_code_for_compare(new_item.raw_body_text or "")
    return old_body != new_body


def _definition_changed(old_item: ParsedCallable, new_item: ParsedCallable) -> bool:
    old_def = _normalize_code_for_compare(old_item.raw_definition_text or "")
    new_def = _normalize_code_for_compare(new_item.raw_definition_text or "")
    return old_def != new_def


def _strong_match_score(old_item: ParsedCallable, new_item: ParsedCallable) -> float:
    """
    Strong match prefers exact normalized signature equality.
    """
    if old_item.qualified_name != new_item.qualified_name:
        return -1.0

    if _normalized_signature_key(old_item) == _normalized_signature_key(new_item):
        line_distance = abs(old_item.definition_start_line - new_item.definition_start_line)
        return 1000.0 - min(line_distance, 200)

    return -1.0


def _medium_match_score(old_item: ParsedCallable, new_item: ParsedCallable) -> float:
    """
    Medium match is for signature-changed but still same logical callable.
    """
    score = 0.0

    if old_item.simple_name != new_item.simple_name:
        return -1.0

    if (old_item.parent_qualified_name or "") == (new_item.parent_qualified_name or ""):
        score += 50.0

    if old_item.qualified_name == new_item.qualified_name:
        score += 40.0

    old_param_count = len(old_item.parameters)
    new_param_count = len(new_item.parameters)
    score += max(0.0, 20.0 - 5.0 * abs(old_param_count - new_param_count))

    if _normalized_signature_shape(old_item) == _normalized_signature_shape(new_item):
        score += 20.0

    line_distance = abs(old_item.definition_start_line - new_item.definition_start_line)
    score += max(0.0, 20.0 - min(line_distance, 20))

    # body similarity hint: if both have body and normalized body equal,
    # this strongly suggests signature-only change.
    if not _body_changed(old_item, new_item):
        score += 30.0

    # definition changed but body same often means signature-only change
    if _definition_changed(old_item, new_item) and not _body_changed(old_item, new_item):
        score += 10.0

    return score


def _match_callables(
    old_callables: List[ParsedCallable],
    new_callables: List[ParsedCallable],
) -> List[CallableMatch]:
    """
    Global matcher:
    1. strong matching
    2. medium matching
    3. unmatched_old / unmatched_new
    """
    matches: List[CallableMatch] = []

    unmatched_old = list(old_callables)
    unmatched_new = list(new_callables)

    # pass1: strong
    strong_pairs = _greedy_pair(
        unmatched_old,
        unmatched_new,
        score_fn=_strong_match_score,
        min_score=0.0,
        match_kind="strong",
    )
    matches.extend(strong_pairs)
    unmatched_old, unmatched_new = _remove_paired_items(unmatched_old, unmatched_new, strong_pairs)

    # pass2: medium
    medium_pairs = _greedy_pair(
        unmatched_old,
        unmatched_new,
        score_fn=_medium_match_score,
        min_score=45.0,
        match_kind="medium",
    )
    matches.extend(medium_pairs)
    unmatched_old, unmatched_new = _remove_paired_items(unmatched_old, unmatched_new, medium_pairs)

    # residual
    for item in unmatched_old:
        matches.append(
            CallableMatch(
                old_callable=item,
                new_callable=None,
                match_kind="unmatched_old",
                match_score=0.0,
            )
        )

    for item in unmatched_new:
        matches.append(
            CallableMatch(
                old_callable=None,
                new_callable=item,
                match_kind="unmatched_new",
                match_score=0.0,
            )
        )

    return matches


def _greedy_pair(
    old_items: List[ParsedCallable],
    new_items: List[ParsedCallable],
    score_fn,
    min_score: float,
    match_kind: str,
) -> List[CallableMatch]:
    candidates: List[Tuple[float, int, int]] = []

    for i, old_item in enumerate(old_items):
        for j, new_item in enumerate(new_items):
            score = score_fn(old_item, new_item)
            if score >= min_score:
                candidates.append((score, i, j))

    candidates.sort(reverse=True, key=lambda x: (x[0], -x[1], -x[2]))

    used_old: Set[int] = set()
    used_new: Set[int] = set()
    matches: List[CallableMatch] = []

    for score, i, j in candidates:
        if i in used_old or j in used_new:
            continue
        used_old.add(i)
        used_new.add(j)
        matches.append(
            CallableMatch(
                old_callable=old_items[i],
                new_callable=new_items[j],
                match_kind=match_kind,
                match_score=score,
            )
        )

    return matches


def _remove_paired_items(
    old_items: List[ParsedCallable],
    new_items: List[ParsedCallable],
    matches: List[CallableMatch],
) -> Tuple[List[ParsedCallable], List[ParsedCallable]]:
    used_old_ids = {
        m.old_callable.callable_id
        for m in matches
        if m.old_callable is not None
    }
    used_new_ids = {
        m.new_callable.callable_id
        for m in matches
        if m.new_callable is not None
    }

    rem_old = [x for x in old_items if x.callable_id not in used_old_ids]
    rem_new = [x for x in new_items if x.callable_id not in used_new_ids]
    return rem_old, rem_new


# ============================================================
# Compare callable texts (lightweight fallback)
# ============================================================

def _callable_body_changed_by_text(
    old_item: ParsedCallable,
    new_item: ParsedCallable,
    old_content: str,
    new_content: str,
) -> bool:
    old_slice = _extract_source_slice(
        old_content,
        old_item.definition_start_line,
        old_item.definition_end_line,
    )
    new_slice = _extract_source_slice(
        new_content,
        new_item.definition_start_line,
        new_item.definition_end_line,
    )
    return _normalize_code_for_compare(old_slice) != _normalize_code_for_compare(new_slice)


def _extract_source_slice(content: str, start_line: int, end_line: int) -> str:
    lines = content.splitlines()
    start_idx = max(0, start_line - 1)
    end_idx = min(len(lines), end_line)
    if start_idx >= end_idx:
        return ""
    return "\n".join(lines[start_idx:end_idx])


def _normalize_code_for_compare(code: str) -> str:
    lines = [ln.rstrip() for ln in code.splitlines()]
    return "\n".join(lines).strip()


# ============================================================
# Build ChangedMethod
# ============================================================

def _build_changed_method_added(
    parsed: ParsedCallable,
    file_path_new: str,
    new_hit_info: Optional[HunkHitInfo] = None,
) -> ChangedMethod:
    new_identity = _parsed_callable_to_identity(parsed, file_path_new)

    evidence = {
        "matched_by": ["tree_sitter_ast", "global_matcher_residue"],
        "occurrence_count": 1,
    }
    if new_hit_info is not None and new_hit_info.has_hit:
        evidence["new_overlap_kinds"] = sorted(set(new_hit_info.overlap_kinds()))
        evidence["evidence_hunks"] = sorted(set(new_hit_info.hunk_ids()))

    return ChangedMethod(
        method_uid=_make_method_uid("added", None, new_identity),
        change_type=CHANGE_TYPE_ADDED,
        old_identity=None,
        new_identity=new_identity,
        locator_confidence=0.92,
        evidence=evidence,
    )


def _build_changed_method_deleted(
    parsed: ParsedCallable,
    file_path_old: str,
    old_hit_info: Optional[HunkHitInfo] = None,
) -> ChangedMethod:
    old_identity = _parsed_callable_to_identity(parsed, file_path_old)

    evidence = {
        "matched_by": ["tree_sitter_ast", "global_matcher_residue"],
        "occurrence_count": 1,
    }
    if old_hit_info is not None and old_hit_info.has_hit:
        evidence["old_overlap_kinds"] = sorted(set(old_hit_info.overlap_kinds()))
        evidence["evidence_hunks"] = sorted(set(old_hit_info.hunk_ids()))

    return ChangedMethod(
        method_uid=_make_method_uid("deleted", old_identity, None),
        change_type=CHANGE_TYPE_DELETED,
        old_identity=old_identity,
        new_identity=None,
        locator_confidence=0.92,
        evidence=evidence,
    )


def _build_changed_method_modified(
    old_parsed: ParsedCallable,
    new_parsed: ParsedCallable,
    mod_reasons: List[str],
    evidence_hunks: List[str],
    old_hit_info: HunkHitInfo,
    new_hit_info: HunkHitInfo,
    match_kind: str,
    match_score: float,
) -> ChangedMethod:
    old_identity = _parsed_callable_to_identity(old_parsed, old_parsed.file_path)
    new_identity = _parsed_callable_to_identity(new_parsed, new_parsed.file_path)

    evidence = {
        "matched_by": ["tree_sitter_ast", "global_matcher", "diff_hunk_overlap"],
        "match_kind": match_kind,
        "match_score": match_score,
        "mod_reasons": sorted(set(mod_reasons)),
        "evidence_hunks": sorted(set(evidence_hunks)),
        "old_overlap_kinds": sorted(set(old_hit_info.overlap_kinds())),
        "new_overlap_kinds": sorted(set(new_hit_info.overlap_kinds())),
        "occurrence_count": 1,
    }

    confidence = 0.99 if match_kind == "strong" else 0.95

    return ChangedMethod(
        method_uid=_make_method_uid("modified", old_identity, new_identity),
        change_type=CHANGE_TYPE_MODIFIED,
        old_identity=old_identity,
        new_identity=new_identity,
        locator_confidence=confidence,
        evidence=evidence,
    )


def _parsed_callable_to_identity(parsed: ParsedCallable, file_path: str) -> MethodIdentity:
    return MethodIdentity(
        method_uid="",
        qualified_name=parsed.qualified_name,
        simple_name=parsed.simple_name,
        file_path=file_path,
        start_line=parsed.definition_start_line,
        end_line=parsed.definition_end_line,
        category=parsed.category,
        parent_qualified_name=parsed.parent_qualified_name,
        return_type=parsed.return_type,
        parameters=parsed.parameters,
        start_offset=parsed.definition_start_offset,
        end_offset=parsed.definition_end_offset,
    )


def _make_method_uid(
    prefix: str,
    old_identity: Optional[MethodIdentity],
    new_identity: Optional[MethodIdentity],
) -> str:
    raw = "|".join(
        [
            prefix,
            old_identity.qualified_name if old_identity else "",
            _normalize_path(old_identity.file_path) if old_identity else "",
            str(old_identity.start_line) if old_identity else "",
            str(old_identity.end_line) if old_identity else "",
            new_identity.qualified_name if new_identity else "",
            _normalize_path(new_identity.file_path) if new_identity else "",
            str(new_identity.start_line) if new_identity else "",
            str(new_identity.end_line) if new_identity else "",
        ]
    )
    digest = hashlib.md5(raw.encode("utf-8")).hexdigest()[:12]
    return f"cm_{digest}"


# ============================================================
# Merge / deduplicate logical methods
# ============================================================

def _merge_same_logical_methods(changed_methods: List[ChangedMethod]) -> List[ChangedMethod]:
    """
    Keep occurrence-level changed methods.

    Rationale:
    In C/C++, the same qualified_name may appear multiple times under
    conditional compilation branches (#if / #else). For step1 we want
    each changed occurrence to be preserved independently, rather than
    merged into one logical method.
    """
    return list(changed_methods)


def _deduplicate_changed_methods(items: List[ChangedMethod]) -> List[ChangedMethod]:
    """
    Deduplicate at occurrence level, not logical-method level.

    Key idea:
    - same qualified_name in different line ranges must be preserved
    - old/new ranges are both part of identity
    """
    seen = set()
    result: List[ChangedMethod] = []

    for item in items:
        old_id = item.old_identity
        new_id = item.new_identity

        key = (
            item.change_type,
            old_id.qualified_name if old_id else None,
            _normalize_path(old_id.file_path) if old_id else None,
            old_id.start_line if old_id else None,
            old_id.end_line if old_id else None,
            new_id.qualified_name if new_id else None,
            _normalize_path(new_id.file_path) if new_id else None,
            new_id.start_line if new_id else None,
            new_id.end_line if new_id else None,
        )

        if key in seen:
            continue
        seen.add(key)
        result.append(item)

    return result


# ============================================================
# Misc
# ============================================================

def _normalize_path(path: str) -> str:
    return path.replace("\\", "/").strip()