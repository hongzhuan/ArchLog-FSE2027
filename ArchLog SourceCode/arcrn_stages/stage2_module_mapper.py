from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .stage2_input_loader import ClusterComponentIndex, NamedClustersIndex


@dataclass
class CommitModuleMappingResult:
    changed_files: List[str] = field(default_factory=list)
    module_counts: Dict[str, int] = field(default_factory=dict)
    component_counts: Dict[str, int] = field(default_factory=dict)
    primary_module: Optional[str] = None
    primary_module_name: Optional[str] = None
    primary_component: Optional[str] = None
    secondary_modules: List[str] = field(default_factory=list)
    secondary_module_names: List[str] = field(default_factory=list)
    secondary_components: List[str] = field(default_factory=list)
    scope: str = "global"


def map_commit_to_modules(
    commit_record: Dict,
    *,
    named_new: NamedClustersIndex,
    named_old: NamedClustersIndex,
    comp_new: ClusterComponentIndex,
    comp_old: ClusterComponentIndex,
) -> CommitModuleMappingResult:
    changed_files = sorted(
        {
            _normalize_path(file_path)
            for file_path in (commit_record.get("all_changed_files") or [])
            if _normalize_path(file_path)
        }
    )

    module_counter: Counter[str] = Counter()
    component_counter: Counter[str] = Counter()

    for file_path in changed_files:
        module_uid = named_new.file_to_module_uid.get(file_path) or named_old.file_to_module_uid.get(file_path)
        if not module_uid:
            continue

        module_counter[module_uid] += 1

        component_name = (
            comp_new.module_uid_to_component.get(module_uid)
            or comp_old.module_uid_to_component.get(module_uid)
        )
        if component_name:
            component_counter[component_name] += 1

    ordered_modules = sorted(module_counter.items(), key=lambda item: (-item[1], item[0]))
    ordered_components = sorted(component_counter.items(), key=lambda item: (-item[1], item[0]))

    primary_module = _choose_primary_module(ordered_modules)
    primary_module_name = _resolve_module_name(primary_module, named_new=named_new, named_old=named_old)
    primary_component = _choose_primary_component(primary_module, comp_new=comp_new, comp_old=comp_old)

    if primary_module is None:
        secondary_modules = [module_uid for module_uid, _ in ordered_modules]
    else:
        secondary_modules = [module_uid for module_uid, _ in ordered_modules if module_uid != primary_module]

    secondary_components = sorted(
        {
            component_name
            for module_uid in secondary_modules
            for component_name in [
                comp_new.module_uid_to_component.get(module_uid)
                or comp_old.module_uid_to_component.get(module_uid)
            ]
            if component_name
        }
    )
    secondary_module_names = sorted(
        {
            module_name
            for module_uid in secondary_modules
            for module_name in [_resolve_module_name(module_uid, named_new=named_new, named_old=named_old)]
            if module_name
        }
    )

    scope = _infer_scope(changed_files, module_counter)

    return CommitModuleMappingResult(
        changed_files=changed_files,
        module_counts=dict(module_counter),
        component_counts=dict(component_counter),
        primary_module=primary_module,
        primary_module_name=primary_module_name,
        primary_component=primary_component,
        secondary_modules=secondary_modules,
        secondary_module_names=secondary_module_names,
        secondary_components=secondary_components,
        scope=scope,
    )


def _choose_primary_module(ordered_modules: List[tuple[str, int]]) -> Optional[str]:
    if not ordered_modules:
        return None
    if len(ordered_modules) == 1:
        return ordered_modules[0][0]

    top_module, top_count = ordered_modules[0]
    second_count = ordered_modules[1][1]
    if top_count > second_count:
        return top_module
    return None


def _choose_primary_component(
    primary_module: Optional[str],
    *,
    comp_new: ClusterComponentIndex,
    comp_old: ClusterComponentIndex,
) -> Optional[str]:
    if primary_module is None:
        return None
    return comp_new.module_uid_to_component.get(primary_module) or comp_old.module_uid_to_component.get(primary_module)


def _resolve_module_name(
    module_uid: Optional[str],
    *,
    named_new: NamedClustersIndex,
    named_old: NamedClustersIndex,
) -> Optional[str]:
    if module_uid is None:
        return None
    return named_new.module_uid_to_name.get(module_uid) or named_old.module_uid_to_name.get(module_uid)


def _infer_scope(changed_files: List[str], module_counter: Counter[str]) -> str:
    if not changed_files:
        return "global"

    if _all_supporting_files(changed_files):
        return "supporting"

    if not module_counter:
        return "global"

    if len(module_counter) == 1:
        return "single-module"

    return "cross-module"


def _all_supporting_files(changed_files: List[str]) -> bool:
    return all(_is_supporting_file(file_path) for file_path in changed_files)


def _is_supporting_file(file_path: str) -> bool:
    normalized = _normalize_path(file_path).lower()

    supporting_markers = (
        "/test/",
        "/tests/",
        "/doc/",
        "/docs/",
        "/script/",
        "/scripts/",
        "/cmake/",
        "/example/",
        "/examples/",
    )
    if any(marker in normalized for marker in supporting_markers):
        return True

    filename = normalized.rsplit("/", 1)[-1]
    if filename in {"cmakelists.txt", "meson.build", "meson_options.txt"}:
        return True

    return filename.endswith((".md", ".rst", ".txt"))


def _normalize_path(path: Optional[str]) -> str:
    if path is None:
        return ""
    text = str(path).replace("\\", "/").strip()
    while text.startswith("./"):
        text = text[2:]
    return text
