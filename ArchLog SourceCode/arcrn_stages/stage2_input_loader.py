from __future__ import annotations

import json
from collections import defaultdict, deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set


@dataclass
class NamedClustersIndex:
    file_to_module_uid: Dict[str, str] = field(default_factory=dict)
    module_uid_to_name: Dict[str, str] = field(default_factory=dict)
    module_uid_to_files: Dict[str, List[str]] = field(default_factory=dict)


@dataclass
class ClusterComponentIndex:
    module_uid_to_component: Dict[str, str] = field(default_factory=dict)
    component_to_module_uids: Dict[str, List[str]] = field(default_factory=dict)


@dataclass
class ArchChangeIndexEntry:
    change_id: str
    change_type: str
    module_name: Optional[str]
    module_uids: List[str] = field(default_factory=list)
    component_name: Optional[str] = None
    related_files: List[str] = field(default_factory=list)
    significance: float = 0.0
    summary: Optional[str] = None


@dataclass
class ArchChangeIndex:
    entries_by_id: Dict[str, ArchChangeIndexEntry] = field(default_factory=dict)
    file_to_change_ids: Dict[str, List[str]] = field(default_factory=dict)
    module_uid_to_change_ids: Dict[str, List[str]] = field(default_factory=dict)
    module_name_to_change_ids: Dict[str, List[str]] = field(default_factory=dict)


@dataclass
class Stage2LoadedInputs:
    change_ir: Dict[str, Any]
    change_ir_path: Path
    diff_ir_path: Path
    namedclusters_new_path: Path
    clustercomponent_new_path: Path
    namedclusters_old_path: Optional[Path] = None
    clustercomponent_old_path: Optional[Path] = None
    named_new: NamedClustersIndex = field(default_factory=NamedClustersIndex)
    named_old: NamedClustersIndex = field(default_factory=NamedClustersIndex)
    comp_new: ClusterComponentIndex = field(default_factory=ClusterComponentIndex)
    comp_old: ClusterComponentIndex = field(default_factory=ClusterComponentIndex)
    arch_index: ArchChangeIndex = field(default_factory=ArchChangeIndex)


def load_stage2_inputs(
    *,
    change_ir_path: Path,
    diff_ir_path: Path,
    namedclusters_new_path: Path,
    clustercomponent_new_path: Path,
    namedclusters_old_path: Optional[Path] = None,
    clustercomponent_old_path: Optional[Path] = None,
) -> Stage2LoadedInputs:
    change_ir = _load_json(change_ir_path)
    diff_ir = _load_json(diff_ir_path)

    named_new = parse_namedclusters(namedclusters_new_path)
    named_old = parse_namedclusters(namedclusters_old_path) if namedclusters_old_path else NamedClustersIndex()
    comp_new = parse_clustercomponent(clustercomponent_new_path, named_new)
    comp_old = (
        parse_clustercomponent(clustercomponent_old_path, named_old)
        if clustercomponent_old_path and namedclusters_old_path
        else ClusterComponentIndex()
    )
    arch_index = build_arch_change_index(
        diff_ir,
        named_new=named_new,
        named_old=named_old,
        comp_new=comp_new,
        comp_old=comp_old,
    )

    return Stage2LoadedInputs(
        change_ir=change_ir,
        change_ir_path=change_ir_path,
        diff_ir_path=diff_ir_path,
        namedclusters_new_path=namedclusters_new_path,
        clustercomponent_new_path=clustercomponent_new_path,
        namedclusters_old_path=namedclusters_old_path,
        clustercomponent_old_path=clustercomponent_old_path,
        named_new=named_new,
        named_old=named_old,
        comp_new=comp_new,
        comp_old=comp_old,
        arch_index=arch_index,
    )


def parse_namedclusters(json_path: Optional[Path]) -> NamedClustersIndex:
    if json_path is None:
        return NamedClustersIndex()
    data = _load_json(json_path)
    structure = data.get("structure") or []

    occurrence_counter: Dict[str, int] = defaultdict(int)
    file_to_module_uid: Dict[str, str] = {}
    module_uid_to_name: Dict[str, str] = {}
    module_uid_to_files: Dict[str, List[str]] = {}

    for node in structure:
        if not isinstance(node, dict) or node.get("@type") != "group":
            continue

        name = str(node.get("name") or "").strip()
        occurrence_counter[name] += 1
        occurrence = occurrence_counter[name]
        module_uid = f"{name}#{occurrence}"

        files: List[str] = []
        for nested in node.get("nested") or []:
            if not isinstance(nested, dict) or nested.get("@type") != "item":
                continue
            file_path = _normalize_path(nested.get("name"))
            if not file_path:
                continue
            files.append(file_path)
            file_to_module_uid.setdefault(file_path, module_uid)

        files_sorted = sorted(set(files))
        module_uid_to_name[module_uid] = name
        module_uid_to_files[module_uid] = files_sorted

    return NamedClustersIndex(
        file_to_module_uid=file_to_module_uid,
        module_uid_to_name=module_uid_to_name,
        module_uid_to_files=module_uid_to_files,
    )


def parse_clustercomponent(json_path: Path, named_index: NamedClustersIndex) -> ClusterComponentIndex:
    data = _load_json(json_path)
    structure = data.get("structure") or []

    name_to_uids_queue: Dict[str, deque[str]] = defaultdict(deque)
    for module_uid, module_name in named_index.module_uid_to_name.items():
        name_to_uids_queue[module_name].append(module_uid)

    module_uid_to_component: Dict[str, str] = {}
    component_to_module_uids: Dict[str, List[str]] = defaultdict(list)

    for component_node in structure:
        if not isinstance(component_node, dict) or component_node.get("@type") != "component":
            continue
        component_name = str(component_node.get("name") or "").strip()

        for nested in component_node.get("nested") or []:
            if not isinstance(nested, dict) or nested.get("@type") != "cluster":
                continue
            cluster_name = str(nested.get("name") or "").strip()
            queue = name_to_uids_queue.get(cluster_name)
            if not queue:
                continue
            module_uid = queue.popleft()
            module_uid_to_component[module_uid] = component_name
            component_to_module_uids[component_name].append(module_uid)

    return ClusterComponentIndex(
        module_uid_to_component=module_uid_to_component,
        component_to_module_uids={key: value for key, value in component_to_module_uids.items()},
    )


def build_arch_change_index(
    diff_ir_payload: Dict[str, Any],
    *,
    named_new: NamedClustersIndex,
    named_old: NamedClustersIndex,
    comp_new: ClusterComponentIndex,
    comp_old: ClusterComponentIndex,
) -> ArchChangeIndex:
    entries_by_id: Dict[str, ArchChangeIndexEntry] = {}
    file_to_change_ids: Dict[str, Set[str]] = defaultdict(set)
    module_uid_to_change_ids: Dict[str, Set[str]] = defaultdict(set)
    module_name_to_change_ids: Dict[str, Set[str]] = defaultdict(set)

    for raw_change in diff_ir_payload.get("changes") or []:
        if not isinstance(raw_change, dict):
            continue

        change_id = str(raw_change.get("id") or "").strip()
        change_type = str(raw_change.get("type") or "").strip()
        detail = raw_change.get("detail") or {}

        module_uids = _extract_module_uids(detail)
        module_name = _extract_module_name(detail)
        component_name = _extract_component_name(detail)
        related_files = _extract_related_files(detail)

        if not module_name:
            module_name = _resolve_module_name_from_uids(
                module_uids=module_uids,
                named_new=named_new,
                named_old=named_old,
            )
        if not component_name:
            component_name = _resolve_component_name_from_uids(
                module_uids=module_uids,
                comp_new=comp_new,
                comp_old=comp_old,
            )

        if not related_files:
            related_files = _supplement_related_files_from_namedclusters(
                module_uids=module_uids,
                change_type=change_type,
                named_new=named_new,
                named_old=named_old,
            )

        significance = _extract_significance(detail)
        entry = ArchChangeIndexEntry(
            change_id=change_id,
            change_type=change_type,
            module_name=module_name,
            module_uids=module_uids,
            component_name=component_name,
            related_files=sorted(set(related_files)),
            significance=significance,
            summary=str(raw_change.get("summary") or "").strip() or None,
        )
        entries_by_id[change_id] = entry

        for file_path in entry.related_files:
            file_to_change_ids[file_path].add(change_id)
        for module_uid in entry.module_uids:
            module_uid_to_change_ids[module_uid].add(change_id)
        if entry.module_name:
            module_name_to_change_ids[entry.module_name].add(change_id)

    return ArchChangeIndex(
        entries_by_id=entries_by_id,
        file_to_change_ids={key: sorted(value) for key, value in file_to_change_ids.items()},
        module_uid_to_change_ids={key: sorted(value) for key, value in module_uid_to_change_ids.items()},
        module_name_to_change_ids={key: sorted(value) for key, value in module_name_to_change_ids.items()},
    )


def _extract_module_uids(detail: Dict[str, Any]) -> List[str]:
    module_uids = []
    for key in ("module_uid", "from_module_uid", "to_module_uid"):
        value = str(detail.get(key) or "").strip()
        if value:
            module_uids.append(value)
    return sorted(set(module_uids))


def _extract_module_name(detail: Dict[str, Any]) -> Optional[str]:
    for key in ("module_name", "to_name", "from_name"):
        value = str(detail.get(key) or "").strip()
        if value:
            return value
    return None


def _extract_component_name(detail: Dict[str, Any]) -> Optional[str]:
    semantics = detail.get("semantics") or {}
    arch = semantics.get("arch") if isinstance(semantics, dict) else {}
    for key in ("to_component", "from_component"):
        value = str((arch or {}).get(key) or detail.get(key) or "").strip()
        if value:
            return value
    return None


def _extract_related_files(detail: Dict[str, Any]) -> List[str]:
    related_files: List[str] = []

    semantics = detail.get("semantics") or {}
    code = semantics.get("code") if isinstance(semantics, dict) else {}
    if isinstance(code, dict):
        for key in ("added_files", "removed_files"):
            for item in code.get(key) or []:
                if not isinstance(item, dict):
                    continue
                file_path = _normalize_path(item.get("path"))
                if file_path:
                    related_files.append(file_path)

    examples = detail.get("examples") or {}
    if isinstance(examples, dict):
        for key in ("added_files_top", "removed_files_top"):
            for file_path in examples.get(key) or []:
                normalized = _normalize_path(file_path)
                if normalized:
                    related_files.append(normalized)

    return sorted(set(related_files))


def _supplement_related_files_from_namedclusters(
    *,
    module_uids: List[str],
    change_type: str,
    named_new: NamedClustersIndex,
    named_old: NamedClustersIndex,
) -> List[str]:
    related_files: List[str] = []
    for module_uid in module_uids:
        if change_type == "module_removed":
            related_files.extend(named_old.module_uid_to_files.get(module_uid, []))
        else:
            related_files.extend(named_new.module_uid_to_files.get(module_uid, []))
            related_files.extend(named_old.module_uid_to_files.get(module_uid, []))
    return sorted(set(related_files))


def _extract_significance(detail: Dict[str, Any]) -> float:
    value = detail.get("architecture_significance")
    if value is None:
        value = detail.get("significance")
    try:
        return float(value)
    except Exception:
        return 0.0


def _resolve_module_name_from_uids(
    *,
    module_uids: List[str],
    named_new: NamedClustersIndex,
    named_old: NamedClustersIndex,
) -> Optional[str]:
    for module_uid in module_uids:
        module_name = named_new.module_uid_to_name.get(module_uid) or named_old.module_uid_to_name.get(module_uid)
        if module_name:
            return module_name
    return None


def _resolve_component_name_from_uids(
    *,
    module_uids: List[str],
    comp_new: ClusterComponentIndex,
    comp_old: ClusterComponentIndex,
) -> Optional[str]:
    for module_uid in module_uids:
        component_name = comp_new.module_uid_to_component.get(module_uid) or comp_old.module_uid_to_component.get(module_uid)
        if component_name:
            return component_name
    return None


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _normalize_path(path: Any) -> str:
    if path is None:
        return ""
    text = str(path).replace("\\", "/").strip()
    while text.startswith("./"):
        text = text[2:]
    return text
