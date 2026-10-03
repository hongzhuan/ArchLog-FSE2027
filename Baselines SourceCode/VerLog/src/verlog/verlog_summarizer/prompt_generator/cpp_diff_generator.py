from __future__ import annotations

import json
import re
import subprocess
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

from unidiff import PatchSet


CPP_EXTENSIONS = {
    ".c",
    ".cc",
    ".cpp",
    ".cxx",
    ".h",
    ".hh",
    ".hpp",
    ".hxx",
}

SOURCE_EXTENSIONS = {".c", ".cc", ".cpp", ".cxx"}
HEADER_EXTENSIONS = {".h", ".hh", ".hpp", ".hxx"}

CALLABLE_CATEGORIES = {
    "Function",
    "Method",
    "Constructor",
    "Destructor",
}

RELATION_CONTEXT_LABELS = {
    "reads": "reads",
    "sets": "sets",
    "type": "uses type",
    "has type": "has type",
    "macro use": "uses macro",
    "parameter use": "uses parameter",
    "addr parameter use": "uses address parameter",
    "parameter use field reference": "uses field",
    "flow to": "data flow",
    "cast": "casts",
    "declares": "declares",
    "extern declare": "extern declares",
    "embed": "embeds",
}

CONTEXT_MODES = {"callee", "callers-callees", "full"}
MAX_CALLEE_CONTEXT = 32
MAX_CALLER_CONTEXT = 32
MAX_RELATION_CONTEXT_PER_KIND = 8
MAX_TOTAL_DEPENDENCY_CONTEXT = 96


@dataclass(frozen=True)
class FunctionEntity:
    entity_id: int
    qualified_name: str
    file_path: str
    start_line: int
    end_line: int
    category: str

    @property
    def signature(self) -> str:
        return f"<{self.file_path}: {self.qualified_name}>"

    @property
    def line_number(self) -> str:
        return f"{self.start_line}-{self.end_line}"


@dataclass
class EnreIndex:
    functions_by_id: Dict[int, FunctionEntity]
    functions_by_file: Dict[str, List[FunctionEntity]]
    outgoing_calls: Dict[int, List[int]]
    incoming_calls: Dict[int, List[int]]
    relation_context: Dict[int, List[str]]
    file_context_by_path: Dict[str, List[str]]

    def callees_for(self, function_id: int) -> List[str]:
        callees = []
        seen = set()
        for callee_id in self.outgoing_calls.get(function_id, []):
            callee = self.functions_by_id.get(callee_id)
            if callee is None or callee.signature in seen:
                continue
            seen.add(callee.signature)
            callees.append(callee.signature)
        return callees

    def callers_for(self, function_id: int) -> List[str]:
        callers = []
        seen = set()
        for caller_id in self.incoming_calls.get(function_id, []):
            caller = self.functions_by_id.get(caller_id)
            if caller is None or caller.signature in seen:
                continue
            seen.add(caller.signature)
            callers.append(caller.signature)
        return callers

    def dependency_context_for(self, function_id: int, context_mode: str) -> List[str]:
        if context_mode not in CONTEXT_MODES:
            raise ValueError(f"Invalid C/C++ context mode: {context_mode}")

        function = self.functions_by_id[function_id]
        context: List[str] = []
        seen: Set[str] = set()

        def add(value: str) -> None:
            if value in seen or len(context) >= MAX_TOTAL_DEPENDENCY_CONTEXT:
                return
            seen.add(value)
            context.append(value)

        for callee in self.callees_for(function_id)[:MAX_CALLEE_CONTEXT]:
            add(callee)

        if context_mode in {"callers-callees", "full"}:
            for caller in self.callers_for(function_id)[:MAX_CALLER_CONTEXT]:
                add(f"[caller] {caller}")

        if context_mode == "full":
            for item in self.relation_context.get(function_id, []):
                add(item)
            for item in self.file_context_by_path.get(function.file_path, []):
                add(item)

        return context

    def functions_in_file(self, file_path: Optional[str]) -> List[FunctionEntity]:
        if not file_path:
            return []
        return list(self.functions_by_file.get(_normalize_path(file_path), []))


@dataclass
class FileChange:
    status: str
    old_path: Optional[str]
    new_path: Optional[str]

    @property
    def display_path(self) -> str:
        return self.new_path or self.old_path or ""

    @property
    def is_cpp(self) -> bool:
        return any(
            Path(path).suffix.lower() in CPP_EXTENSIONS
            for path in (self.old_path, self.new_path)
            if path
        )


@dataclass
class FilePatchInfo:
    old_path: Optional[str]
    new_path: Optional[str]
    old_changed_lines: Set[int] = field(default_factory=set)
    new_changed_lines: Set[int] = field(default_factory=set)
    hunk_texts: List[str] = field(default_factory=list)


@dataclass
class FunctionPair:
    old: Optional[FunctionEntity]
    new: Optional[FunctionEntity]
    change_type: str


def generate_cpp_diff(
    *,
    repo_path: Path,
    ref_version: str,
    tgt_version: str,
    ref_enre_json: Path,
    tgt_enre_json: Path,
    output_path: Optional[Path] = None,
    context_mode: str = "full",
) -> Dict[str, object]:
    if context_mode not in CONTEXT_MODES:
        raise ValueError(f"context_mode must be one of {sorted(CONTEXT_MODES)}")

    ref_index = load_enre_index(ref_enre_json)
    tgt_index = load_enre_index(tgt_enre_json)
    file_changes = _git_diff_name_status(repo_path, ref_version, tgt_version)
    patch_map = _collect_patch_info(repo_path, ref_version, tgt_version)

    added_classes = []
    modified_classes = []
    deleted_classes = []
    non_function_changes = []

    for file_change in file_changes:
        patch_info = _lookup_patch_info(patch_map, file_change)

        if not file_change.is_cpp:
            non_function_changes.append(_non_function_record(file_change, patch_info, "non_cpp_file"))
            continue

        old_functions = ref_index.functions_in_file(file_change.old_path)
        new_functions = tgt_index.functions_in_file(file_change.new_path)

        if file_change.status.startswith("A"):
            added_methods = [_method_info(func, tgt_index, context_mode) for func in new_functions]
            if added_methods:
                added_classes.append(
                    {
                        "class_name": file_change.new_path,
                        "ADDED_METHOD_IN_ADDED_CLASS": added_methods,
                    }
                )
            else:
                non_function_changes.append(_non_function_record(file_change, patch_info, "cpp_file_without_functions"))
            continue

        if file_change.status.startswith("D"):
            deleted_methods = [_method_info(func, ref_index, context_mode) for func in old_functions]
            if deleted_methods:
                deleted_classes.append(
                    {
                        "class_name": file_change.old_path,
                        "DELETED_METHOD_IN_DELETED_CLASS": deleted_methods,
                    }
                )
            else:
                non_function_changes.append(_non_function_record(file_change, patch_info, "cpp_file_without_functions"))
            continue

        function_pairs, covered_old_lines, covered_new_lines = _detect_changed_function_pairs(
            old_functions=old_functions,
            new_functions=new_functions,
            patch_info=patch_info,
        )

        class_record = {
            "class_name": file_change.new_path or file_change.old_path,
            "ADDED_METHOD_IN_MODIFIED_CLASS": [],
            "MODIFIED_METHOD_IN_REF_CLASS": [],
            "MODIFIED_METHOD_IN_TGT_CLASS": [],
            "DELETED_METHOD_IN_MODIFIED_CLASS": [],
        }

        for pair in function_pairs:
            if pair.change_type == "added" and pair.new is not None:
                class_record["ADDED_METHOD_IN_MODIFIED_CLASS"].append(_method_info(pair.new, tgt_index, context_mode))
            elif pair.change_type == "deleted" and pair.old is not None:
                class_record["DELETED_METHOD_IN_MODIFIED_CLASS"].append(_method_info(pair.old, ref_index, context_mode))
            elif pair.change_type == "modified" and pair.old is not None and pair.new is not None:
                class_record["MODIFIED_METHOD_IN_REF_CLASS"].append(_method_info(pair.old, ref_index, context_mode))
                class_record["MODIFIED_METHOD_IN_TGT_CLASS"].append(_method_info(pair.new, tgt_index, context_mode))

        if any(class_record[key] for key in class_record if key != "class_name"):
            modified_classes.append(class_record)

        old_left = set(patch_info.old_changed_lines) - covered_old_lines
        new_left = set(patch_info.new_changed_lines) - covered_new_lines
        if old_left or new_left or not function_pairs:
            non_function_changes.append(
                _non_function_record(
                    file_change,
                    patch_info,
                    "cpp_file_level_or_unmapped_change",
                    old_unmapped_lines=sorted(old_left),
                    new_unmapped_lines=sorted(new_left),
                )
            )

    result = {
        "schema": "verlog-cpp-diff-v1",
        "ref_version": ref_version,
        "tgt_version": tgt_version,
        "added_classes": added_classes,
        "modified_classes": modified_classes,
        "deleted_classes": deleted_classes,
        "non_function_changes": non_function_changes,
        "metadata": {
            "repo_path": str(repo_path),
            "ref_enre_json": str(ref_enre_json),
            "tgt_enre_json": str(tgt_enre_json),
            "changed_file_count": len(file_changes),
            "changed_function_count": _count_changed_functions(added_classes, modified_classes, deleted_classes),
            "non_function_change_count": len(non_function_changes),
            "context_mode": context_mode,
        },
    }

    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    return result


def load_enre_index(path: Path) -> EnreIndex:
    with path.open("r", encoding="utf-8") as f:
        raw = json.load(f)

    raw_entities = raw.get("variables") or raw.get("entities") or raw.get("entity") or []
    raw_relations = raw.get("relations") or raw.get("relation") or []

    file_lookup: Dict[int, str] = {}
    for entity in raw_entities:
        if str(entity.get("category") or "") != "File":
            continue
        entity_id = _safe_int(entity.get("id"))
        qualified_name = _safe_str(entity.get("qualifiedName"))
        if entity_id is not None and qualified_name:
            file_lookup[entity_id] = _normalize_path(qualified_name)

    functions_by_id: Dict[int, FunctionEntity] = {}
    functions_by_file: Dict[str, List[FunctionEntity]] = {}

    for entity in raw_entities:
        category = str(entity.get("category") or "").strip()
        if category not in CALLABLE_CATEGORIES:
            continue

        entity_id = _safe_int(entity.get("id"))
        start_line = _safe_int(entity.get("startLine"))
        end_line = _safe_int(entity.get("endLine"))
        qualified_name = _safe_str(entity.get("qualifiedName"))
        file_path = _resolve_entity_file_path(entity, file_lookup)

        if entity_id is None or start_line is None or not qualified_name or not file_path:
            continue
        if end_line is None or end_line < start_line:
            end_line = start_line

        func = FunctionEntity(
            entity_id=entity_id,
            qualified_name=qualified_name,
            file_path=_normalize_path(file_path),
            start_line=start_line,
            end_line=end_line,
            category=category,
        )
        functions_by_id[entity_id] = func
        functions_by_file.setdefault(func.file_path, []).append(func)

    for functions in functions_by_file.values():
        functions.sort(key=lambda item: (item.start_line, item.end_line, item.qualified_name))

    outgoing_calls: Dict[int, List[int]] = {}
    incoming_calls: Dict[int, List[int]] = {}
    pending_relation_context: Dict[int, List[Tuple[str, str, int]]] = {}
    relation_context_counts: Dict[Tuple[int, str, str], int] = {}
    needed_context_entity_ids: Set[int] = set()
    file_context_by_path: Dict[str, List[str]] = {}
    function_ids = set(functions_by_id)
    for relation in raw_relations:
        relation_type = _relation_type(relation)
        src, dst = _relation_endpoints(relation)
        if src is None or dst is None:
            continue

        if relation_type == "includes":
            _append_file_include_context(file_context_by_path, file_lookup, src, dst)
            continue

        if "call" in relation_type and src in function_ids and dst in function_ids:
            outgoing_calls.setdefault(src, []).append(dst)
            incoming_calls.setdefault(dst, []).append(src)
            continue

        context_label = RELATION_CONTEXT_LABELS.get(relation_type)
        if context_label is None:
            continue

        if src in function_ids and dst not in function_ids:
            if _append_pending_relation_context(
                pending_relation_context,
                relation_context_counts,
                src,
                context_label,
                "out",
                dst,
            ):
                needed_context_entity_ids.add(dst)
        elif dst in function_ids and src not in function_ids:
            if _append_pending_relation_context(
                pending_relation_context,
                relation_context_counts,
                dst,
                context_label,
                "in",
                src,
            ):
                needed_context_entity_ids.add(src)

    entity_labels = _collect_entity_labels(raw_entities, file_lookup, functions_by_id, needed_context_entity_ids)
    relation_context = _materialize_relation_context(pending_relation_context, entity_labels)
    _add_companion_file_context(file_context_by_path, set(functions_by_file))

    return EnreIndex(
        functions_by_id=functions_by_id,
        functions_by_file=functions_by_file,
        outgoing_calls=outgoing_calls,
        incoming_calls=incoming_calls,
        relation_context=relation_context,
        file_context_by_path=file_context_by_path,
    )


def _detect_changed_function_pairs(
    *,
    old_functions: Sequence[FunctionEntity],
    new_functions: Sequence[FunctionEntity],
    patch_info: FilePatchInfo,
) -> Tuple[List[FunctionPair], Set[int], Set[int]]:
    old_hits = [
        func for func in old_functions
        if _range_hits_lines(func.start_line, func.end_line, patch_info.old_changed_lines)
    ]
    new_hits = [
        func for func in new_functions
        if _range_hits_lines(func.start_line, func.end_line, patch_info.new_changed_lines)
    ]

    pairs: List[FunctionPair] = []
    covered_old_lines: Set[int] = set()
    covered_new_lines: Set[int] = set()
    paired_old_ids: Set[int] = set()
    paired_new_ids: Set[int] = set()

    for old_func, new_func in _pair_modified_candidates(old_hits, new_hits):
        pairs.append(FunctionPair(old=old_func, new=new_func, change_type="modified"))
        paired_old_ids.add(old_func.entity_id)
        paired_new_ids.add(new_func.entity_id)
        covered_old_lines.update(_covered_lines(old_func, patch_info.old_changed_lines))
        covered_new_lines.update(_covered_lines(new_func, patch_info.new_changed_lines))

    for func in old_hits:
        if func.entity_id in paired_old_ids:
            continue
        pairs.append(FunctionPair(old=func, new=None, change_type="deleted"))
        covered_old_lines.update(_covered_lines(func, patch_info.old_changed_lines))

    for func in new_hits:
        if func.entity_id in paired_new_ids:
            continue
        pairs.append(FunctionPair(old=None, new=func, change_type="added"))
        covered_new_lines.update(_covered_lines(func, patch_info.new_changed_lines))

    pairs.sort(key=lambda pair: _pair_sort_key(pair))
    return pairs, covered_old_lines, covered_new_lines


def _method_info(function: FunctionEntity, index: EnreIndex, context_mode: str) -> Dict[str, object]:
    return {
        "method_name": function.signature,
        "line_number": function.line_number,
        "reachable_methods": index.dependency_context_for(function.entity_id, context_mode),
        "callee_methods": index.callees_for(function.entity_id),
        "caller_methods": index.callers_for(function.entity_id),
        "context_mode": context_mode,
        "source_language": "cpp",
        "file_path": function.file_path,
        "qualified_name": function.qualified_name,
        "entity_id": function.entity_id,
    }


def _relation_type(relation: Dict[str, object]) -> str:
    return str(
        relation.get("category")
        or relation.get("type")
        or relation.get("relation")
        or relation.get("kind")
        or ""
    ).strip().lower()


def _relation_endpoints(relation: Dict[str, object]) -> Tuple[Optional[int], Optional[int]]:
    src = _safe_int(
        relation.get("from")
        or relation.get("src")
        or relation.get("source")
        or relation.get("srcID")
        or relation.get("fromID")
    )
    dst = _safe_int(
        relation.get("to")
        or relation.get("dst")
        or relation.get("target")
        or relation.get("dstID")
        or relation.get("toID")
    )
    return src, dst


def _append_pending_relation_context(
    pending_relation_context: Dict[int, List[Tuple[str, str, int]]],
    relation_context_counts: Dict[Tuple[int, str, str], int],
    function_id: int,
    relation_label: str,
    direction: str,
    other_entity_id: int,
) -> bool:
    counter_key = (function_id, relation_label, direction)
    if relation_context_counts.get(counter_key, 0) >= MAX_RELATION_CONTEXT_PER_KIND:
        return False
    relation_context_counts[counter_key] = relation_context_counts.get(counter_key, 0) + 1
    pending_relation_context.setdefault(function_id, []).append((relation_label, direction, other_entity_id))
    return True


def _collect_entity_labels(
    raw_entities: Sequence[Dict[str, object]],
    file_lookup: Dict[int, str],
    functions_by_id: Dict[int, FunctionEntity],
    needed_entity_ids: Set[int],
) -> Dict[int, str]:
    labels = {entity_id: function.signature for entity_id, function in functions_by_id.items() if entity_id in needed_entity_ids}
    remaining = needed_entity_ids - set(labels)
    if not remaining:
        return labels

    for entity in raw_entities:
        entity_id = _safe_int(entity.get("id"))
        if entity_id not in remaining:
            continue
        labels[entity_id] = _entity_context_label(entity, file_lookup)
        remaining.remove(entity_id)
        if not remaining:
            break
    return labels


def _entity_context_label(entity: Dict[str, object], file_lookup: Dict[int, str]) -> str:
    category = str(entity.get("category") or "Entity").strip() or "Entity"
    qualified_name = _safe_str(entity.get("qualifiedName") or entity.get("name")) or "<anonymous>"
    if category == "File":
        return f"File: {_normalize_path(qualified_name)}"
    if category == "Macro":
        return f"Macro: {qualified_name}"
    if category in {"Struct", "Union", "Enum", "Typedef"}:
        return f"Type: {qualified_name}"
    if category in {"Variable", "Parameter Variable"}:
        return f"Variable: {qualified_name}"
    if category == "Function Pointer":
        return f"Function pointer: {qualified_name}"
    entity_file_id = _safe_int(entity.get("entityFile"))
    file_suffix = ""
    if entity_file_id is not None and entity_file_id in file_lookup:
        file_suffix = f" in {file_lookup[entity_file_id]}"
    return f"{category}: {qualified_name}{file_suffix}"


def _materialize_relation_context(
    pending_relation_context: Dict[int, List[Tuple[str, str, int]]],
    entity_labels: Dict[int, str],
) -> Dict[int, List[str]]:
    result: Dict[int, List[str]] = {}
    for function_id, pending_items in pending_relation_context.items():
        seen = set()
        items = []
        for relation_label, direction, other_entity_id in pending_items:
            target_label = entity_labels.get(other_entity_id)
            if not target_label:
                continue
            prefix = relation_label if direction == "out" else f"referenced by {relation_label}"
            item = f"[{prefix}] {target_label}"
            if item in seen:
                continue
            seen.add(item)
            items.append(item)
        result[function_id] = items
    return result


def _append_file_include_context(
    file_context_by_path: Dict[str, List[str]],
    file_lookup: Dict[int, str],
    src: int,
    dst: int,
) -> None:
    src_path = file_lookup.get(src)
    dst_path = file_lookup.get(dst)
    if not src_path or not dst_path:
        return
    _append_limited_context(file_context_by_path, src_path, f"[includes] {dst_path}")
    _append_limited_context(file_context_by_path, dst_path, f"[included by] {src_path}")


def _append_limited_context(context_by_path: Dict[str, List[str]], path: str, value: str, limit: int = 16) -> None:
    items = context_by_path.setdefault(_normalize_path(path), [])
    if value not in items and len(items) < limit:
        items.append(value)


def _add_companion_file_context(file_context_by_path: Dict[str, List[str]], file_paths: Set[str]) -> None:
    by_stem: Dict[str, List[str]] = {}
    for file_path in file_paths:
        path = Path(file_path)
        by_stem.setdefault(str(path.with_suffix("")).replace("\\", "/"), []).append(file_path)

    for file_path in file_paths:
        path = Path(file_path)
        extension = path.suffix.lower()
        if extension not in SOURCE_EXTENSIONS and extension not in HEADER_EXTENSIONS:
            continue
        stem = str(path.with_suffix("")).replace("\\", "/")
        for companion in sorted(by_stem.get(stem, [])):
            if companion == file_path:
                continue
            companion_extension = Path(companion).suffix.lower()
            if extension in SOURCE_EXTENSIONS and companion_extension in HEADER_EXTENSIONS:
                _append_limited_context(file_context_by_path, file_path, f"[header/source companion] {companion}", 6)
            elif extension in HEADER_EXTENSIONS and companion_extension in SOURCE_EXTENSIONS:
                _append_limited_context(file_context_by_path, file_path, f"[header/source companion] {companion}", 6)


def _git_diff_name_status(repo_path: Path, ref_version: str, tgt_version: str) -> List[FileChange]:
    output = _run_git(repo_path, ["diff", "--name-status", "--find-renames", ref_version, tgt_version])
    changes: List[FileChange] = []
    for raw_line in output.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        parts = line.split("\t")
        status = parts[0]
        if status.startswith("R") or status.startswith("C"):
            if len(parts) >= 3:
                changes.append(FileChange(status=status, old_path=parts[1], new_path=parts[2]))
            continue
        if len(parts) < 2:
            continue
        path = parts[1]
        if status.startswith("A"):
            changes.append(FileChange(status=status, old_path=None, new_path=path))
        elif status.startswith("D"):
            changes.append(FileChange(status=status, old_path=path, new_path=None))
        else:
            changes.append(FileChange(status=status, old_path=path, new_path=path))
    return changes


def _collect_patch_info(repo_path: Path, ref_version: str, tgt_version: str) -> Dict[str, FilePatchInfo]:
    patch_text = _run_git(
        repo_path,
        [
            "diff",
            "--ignore-blank-lines",
            "--ignore-all-space",
            "--find-renames",
            "--unified=3",
            ref_version,
            tgt_version,
        ],
    )
    # Some C/C++ test fixtures intentionally contain bare carriage returns.
    # They appear inside hunk context lines and make unidiff split one logical
    # diff line into two physical lines, which breaks hunk-count validation.
    patch_text = patch_text.replace("\r", "")
    patch_set = PatchSet(patch_text)
    result: Dict[str, FilePatchInfo] = {}

    for patched_file in patch_set:
        old_path = _strip_git_prefix(str(patched_file.source_file))
        new_path = _strip_git_prefix(str(patched_file.target_file))
        if old_path == "/dev/null":
            old_path = None
        if new_path == "/dev/null":
            new_path = None

        info = FilePatchInfo(old_path=old_path, new_path=new_path)
        for hunk in patched_file:
            info.hunk_texts.append(str(hunk))
            for line in hunk:
                if line.is_removed and line.source_line_no is not None:
                    info.old_changed_lines.add(int(line.source_line_no))
                elif line.is_added and line.target_line_no is not None:
                    info.new_changed_lines.add(int(line.target_line_no))

        for key in {path for path in (old_path, new_path) if path}:
            result[_normalize_path(key)] = info

    return result


def _lookup_patch_info(patch_map: Dict[str, FilePatchInfo], file_change: FileChange) -> FilePatchInfo:
    for path in (file_change.new_path, file_change.old_path):
        if path and _normalize_path(path) in patch_map:
            return patch_map[_normalize_path(path)]
    return FilePatchInfo(old_path=file_change.old_path, new_path=file_change.new_path)


def _non_function_record(
    file_change: FileChange,
    patch_info: FilePatchInfo,
    reason: str,
    *,
    old_unmapped_lines: Optional[List[int]] = None,
    new_unmapped_lines: Optional[List[int]] = None,
) -> Dict[str, object]:
    return {
        "status": file_change.status,
        "file_path_old": file_change.old_path,
        "file_path_new": file_change.new_path,
        "reason": reason,
        "old_changed_line_count": len(patch_info.old_changed_lines),
        "new_changed_line_count": len(patch_info.new_changed_lines),
        "old_unmapped_lines": old_unmapped_lines or [],
        "new_unmapped_lines": new_unmapped_lines or [],
        "hunk_count": len(patch_info.hunk_texts),
        "hunks": _truncate_hunks(patch_info.hunk_texts),
    }


def _index_functions_by_name(functions: Sequence[FunctionEntity]) -> Dict[str, List[FunctionEntity]]:
    result: Dict[str, List[FunctionEntity]] = {}
    for function in functions:
        key = _function_match_key(function)
        result.setdefault(key, []).append(function)
    return result


def _pair_modified_candidates(
    old_hits: Sequence[FunctionEntity],
    new_hits: Sequence[FunctionEntity],
) -> List[Tuple[FunctionEntity, FunctionEntity]]:
    pairs: List[Tuple[FunctionEntity, FunctionEntity]] = []
    paired_old_ids: Set[int] = set()
    paired_new_ids: Set[int] = set()

    def add_pair(old_func: FunctionEntity, new_func: FunctionEntity) -> None:
        if old_func.entity_id in paired_old_ids or new_func.entity_id in paired_new_ids:
            return
        paired_old_ids.add(old_func.entity_id)
        paired_new_ids.add(new_func.entity_id)
        pairs.append((old_func, new_func))

    _pair_by_group_key(old_hits, new_hits, _function_match_key, add_pair, paired_old_ids, paired_new_ids)
    _pair_by_group_key(old_hits, new_hits, _function_stable_name_key, add_pair, paired_old_ids, paired_new_ids)
    _pair_by_similarity(old_hits, new_hits, add_pair, paired_old_ids, paired_new_ids)
    return pairs


def _pair_by_group_key(
    old_hits: Sequence[FunctionEntity],
    new_hits: Sequence[FunctionEntity],
    key_func,
    add_pair,
    paired_old_ids: Set[int],
    paired_new_ids: Set[int],
) -> None:
    old_by_key: Dict[str, List[FunctionEntity]] = {}
    new_by_key: Dict[str, List[FunctionEntity]] = {}
    for function in old_hits:
        if function.entity_id not in paired_old_ids:
            old_by_key.setdefault(key_func(function), []).append(function)
    for function in new_hits:
        if function.entity_id not in paired_new_ids:
            new_by_key.setdefault(key_func(function), []).append(function)

    for key in sorted(set(old_by_key) & set(new_by_key)):
        if not key:
            continue
        for old_func, new_func in _pair_functions_by_line(old_by_key[key], new_by_key[key]):
            add_pair(old_func, new_func)


def _pair_by_similarity(
    old_hits: Sequence[FunctionEntity],
    new_hits: Sequence[FunctionEntity],
    add_pair,
    paired_old_ids: Set[int],
    paired_new_ids: Set[int],
) -> None:
    remaining_old = [func for func in old_hits if func.entity_id not in paired_old_ids]
    remaining_new = [func for func in new_hits if func.entity_id not in paired_new_ids]

    candidates: List[Tuple[float, FunctionEntity, FunctionEntity]] = []
    for old_func in remaining_old:
        for new_func in remaining_new:
            score = _refactor_pair_score(old_func, new_func)
            if score >= 0.68:
                candidates.append((score, old_func, new_func))

    candidates.sort(key=lambda item: (-item[0], item[1].start_line, item[2].start_line))
    for _, old_func, new_func in candidates:
        add_pair(old_func, new_func)


def _refactor_pair_score(old_func: FunctionEntity, new_func: FunctionEntity) -> float:
    old_name = _function_stable_name_key(old_func)
    new_name = _function_stable_name_key(new_func)
    name_score = SequenceMatcher(None, old_name, new_name).ratio()
    same_file_score = 1.0 if old_func.file_path == new_func.file_path else 0.0
    old_length = max(1, old_func.end_line - old_func.start_line + 1)
    new_length = max(1, new_func.end_line - new_func.start_line + 1)
    length_score = 1.0 - (abs(old_length - new_length) / max(old_length, new_length))
    line_distance = abs(old_func.start_line - new_func.start_line)
    line_score = max(0.0, 1.0 - min(line_distance, 200) / 200)
    return (0.45 * name_score) + (0.25 * same_file_score) + (0.20 * line_score) + (0.10 * length_score)


def _function_match_key(function: FunctionEntity) -> str:
    return f"{function.file_path}|{function.qualified_name}"


def _function_stable_name_key(function: FunctionEntity) -> str:
    name = function.qualified_name
    name = re.sub(r"\(.*\)$", "", name)
    name = name.replace("operator ", "operator")
    name = name.split("::")[-1].split(".")[-1]
    return name.strip().lower()


def _pair_functions_by_line(
    old_group: Sequence[FunctionEntity],
    new_group: Sequence[FunctionEntity],
) -> List[Tuple[FunctionEntity, FunctionEntity]]:
    remaining_new = list(new_group)
    pairs: List[Tuple[FunctionEntity, FunctionEntity]] = []
    for old_func in old_group:
        if not remaining_new:
            break
        remaining_new.sort(key=lambda item: abs(item.start_line - old_func.start_line))
        new_func = remaining_new.pop(0)
        pairs.append((old_func, new_func))
    return pairs


def _range_hits_lines(start_line: int, end_line: int, changed_lines: Iterable[int]) -> bool:
    return any(start_line <= line <= end_line for line in changed_lines)


def _covered_lines(function: FunctionEntity, changed_lines: Iterable[int]) -> Set[int]:
    return {line for line in changed_lines if function.start_line <= line <= function.end_line}


def _pair_sort_key(pair: FunctionPair) -> Tuple[str, int, str]:
    func = pair.new or pair.old
    if func is None:
        return "", 0, pair.change_type
    return func.file_path, func.start_line, func.qualified_name


def _resolve_entity_file_path(entity: Dict[str, object], file_lookup: Dict[int, str]) -> Optional[str]:
    direct = _safe_str(
        entity.get("filePath")
        or entity.get("path")
        or entity.get("fullPath")
        or entity.get("file")
    )
    if direct:
        return direct
    entity_file_id = _safe_int(entity.get("entityFile"))
    if entity_file_id is not None:
        return file_lookup.get(entity_file_id)
    return None


def _run_git(repo_path: Path, args: Sequence[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=str(repo_path),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    stdout = result.stdout.decode("utf-8", errors="replace")
    stderr = result.stderr.decode("utf-8", errors="replace")
    if result.returncode != 0:
        raise RuntimeError(
            f"Git command failed: git {' '.join(args)}\nstdout:\n{stdout}\nstderr:\n{stderr}"
        )
    return stdout


def _strip_git_prefix(path: str) -> Optional[str]:
    if path in {"None", ""}:
        return None
    if path.startswith("a/") or path.startswith("b/"):
        return path[2:]
    return path


def _normalize_path(path: str) -> str:
    return str(path).replace("\\", "/").strip()


def _safe_int(value: object) -> Optional[int]:
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _safe_str(value: object) -> Optional[str]:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _truncate_hunks(hunks: Sequence[str], max_hunks: int = 8, max_lines_per_hunk: int = 30) -> List[str]:
    result = []
    for hunk in list(hunks)[:max_hunks]:
        lines = hunk.splitlines()
        if len(lines) > max_lines_per_hunk:
            lines = lines[:max_lines_per_hunk] + ["..."]
        result.append("\n".join(lines))
    return result


def _count_changed_functions(
    added_classes: Sequence[Dict[str, object]],
    modified_classes: Sequence[Dict[str, object]],
    deleted_classes: Sequence[Dict[str, object]],
) -> int:
    count = 0
    for item in added_classes:
        count += len(item.get("ADDED_METHOD_IN_ADDED_CLASS", []))
    for item in deleted_classes:
        count += len(item.get("DELETED_METHOD_IN_DELETED_CLASS", []))
    for item in modified_classes:
        count += len(item.get("ADDED_METHOD_IN_MODIFIED_CLASS", []))
        count += len(item.get("MODIFIED_METHOD_IN_TGT_CLASS", []))
        count += len(item.get("DELETED_METHOD_IN_MODIFIED_CLASS", []))
    return count
