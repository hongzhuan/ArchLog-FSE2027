from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set

from .models import ReleaseNotePlan, ReleaseSectionPlan, utc_now_iso
from .stage3_input_loader import Stage3ArchChange, Stage3LoadedInputs


ARCH_SECTION_ORDER = {
    "module_added": 0,
    "module_removed": 1,
    "module_changed": 2,
}


@dataclass
class _SectionDraft:
    section_id: str
    title: str
    section_type: str
    group_order: int
    sort_order: int
    primary_module: Optional[str] = None
    primary_module_name: Optional[str] = None
    primary_component: Optional[str] = None
    secondary_modules: List[str] = field(default_factory=list)
    secondary_module_names: List[str] = field(default_factory=list)
    secondary_components: List[str] = field(default_factory=list)
    commit_ids: List[str] = field(default_factory=list)
    arch_change_ids: List[str] = field(default_factory=list)
    arch_change_types: List[str] = field(default_factory=list)
    rationale_parts: List[str] = field(default_factory=list)
    significance: float = 0.0

    def to_plan(self) -> ReleaseSectionPlan:
        return ReleaseSectionPlan(
            section_id=self.section_id,
            title=self.title,
            section_type=self.section_type,
            primary_module=self.primary_module,
            primary_module_name=self.primary_module_name,
            primary_component=self.primary_component,
            secondary_modules=self.secondary_modules,
            secondary_module_names=self.secondary_module_names,
            secondary_components=self.secondary_components,
            commit_ids=self.commit_ids,
            arch_change_ids=self.arch_change_ids,
            arch_change_types=self.arch_change_types,
            rationale=" ".join(part for part in self.rationale_parts if part).strip() or None,
        )


def build_stage3_release_plan(loaded_inputs: Stage3LoadedInputs) -> ReleaseNotePlan:
    mapping_lookup = _build_mapping_lookup(loaded_inputs.mapping_output)
    commit_ids_in_order = [str(item.get("commit_id") or "") for item in loaded_inputs.change_ir.get("commits") or []]

    sections: List[_SectionDraft] = []
    seeded_by_module: Dict[str, _SectionDraft] = {}

    for arch_change in _sorted_arch_changes(loaded_inputs.arch_changes):
        section = _create_arch_section(arch_change)
        sections.append(section)
        if arch_change.module_uid:
            seeded_by_module[arch_change.module_uid] = section
        if arch_change.module_name:
            seeded_by_module[arch_change.module_name] = section

    fallback_by_module: Dict[str, _SectionDraft] = {}
    cross_module_section: Optional[_SectionDraft] = None
    supporting_section: Optional[_SectionDraft] = None
    assigned_commit_ids: Set[str] = set()

    for commit_id in commit_ids_in_order:
        if not commit_id:
            continue
        mapping = mapping_lookup.get(commit_id)
        if mapping is None:
            continue

        target_section: Optional[_SectionDraft]
        scope = str(mapping.get("scope") or "")

        if scope in {"supporting", "global"} or (
            not mapping.get("primary_module") and not mapping.get("primary_module_name") and scope != "cross-module"
        ):
            if supporting_section is None:
                supporting_section = _create_supporting_section()
                sections.append(supporting_section)
            target_section = supporting_section
        elif scope == "cross-module":
            if cross_module_section is None:
                cross_module_section = _create_cross_module_section()
                sections.append(cross_module_section)
            target_section = cross_module_section
        else:
            target_section = _find_seeded_module_section(mapping, seeded_by_module)
            if target_section is None:
                target_section = _get_or_create_fallback_module_section(mapping, fallback_by_module, sections)

        if target_section is None:
            continue

        _assign_commit_to_section(target_section, commit_id, mapping)
        assigned_commit_ids.add(commit_id)

    sections_sorted = [section.to_plan() for section in sorted(sections, key=_section_sort_key)]

    stats = _build_stage3_stats(
        sections=sections_sorted,
        total_commits=len(commit_ids_in_order),
        assigned_commits=len(assigned_commit_ids),
    )

    return ReleaseNotePlan(
        generated_at=utc_now_iso(),
        source_change_ir_path=str(loaded_inputs.change_ir_path),
        source_mapping_path=str(loaded_inputs.mapping_path),
        source_arch_diff_path=str(loaded_inputs.diff_ir_path),
        sections=sections_sorted,
        stats=stats,
    )


def _build_mapping_lookup(mapping_output: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    return {
        str(item.get("commit_id") or ""): item
        for item in mapping_output.get("mappings") or []
        if isinstance(item, dict) and str(item.get("commit_id") or "")
    }


def _sorted_arch_changes(arch_changes: List[Stage3ArchChange]) -> List[Stage3ArchChange]:
    return sorted(
        arch_changes,
        key=lambda item: (
            ARCH_SECTION_ORDER.get(item.change_type, 99),
            -item.significance,
            item.module_name or "",
            item.change_id,
        ),
    )


def _create_arch_section(arch_change: Stage3ArchChange) -> _SectionDraft:
    title_map = {
        "module_added": f"Module Added: {arch_change.module_name or arch_change.module_uid or arch_change.change_id}",
        "module_removed": f"Module Removed: {arch_change.module_name or arch_change.module_uid or arch_change.change_id}",
        "module_changed": f"Module Evolution: {arch_change.module_name or arch_change.module_uid or arch_change.change_id}",
    }
    section_type_map = {
        "module_added": "module-added",
        "module_removed": "module-removed",
        "module_changed": "module-evolution",
    }

    rationale_parts = []
    if arch_change.summary:
        rationale_parts.append(f"Seeded from architectural diff: {arch_change.summary}")
    else:
        rationale_parts.append("Seeded from architectural diff events.")
    if arch_change.related_files:
        rationale_parts.append(f"Related files: {', '.join(arch_change.related_files[:6])}.")

    return _SectionDraft(
        section_id=f"sec_arch_{_slugify(arch_change.change_id)}",
        title=title_map.get(arch_change.change_type, f"Architecture Change: {arch_change.change_id}"),
        section_type=section_type_map.get(arch_change.change_type, "architecture-change"),
        group_order=0,
        sort_order=ARCH_SECTION_ORDER.get(arch_change.change_type, 99),
        primary_module=arch_change.module_uid,
        primary_module_name=arch_change.module_name,
        primary_component=arch_change.component_name,
        arch_change_ids=[arch_change.change_id],
        arch_change_types=[arch_change.change_type],
        rationale_parts=rationale_parts,
        significance=arch_change.significance,
    )


def _create_cross_module_section() -> _SectionDraft:
    return _SectionDraft(
        section_id="sec_cross_module",
        title="Cross-Module Impacts",
        section_type="cross-module",
        group_order=1,
        sort_order=0,
        rationale_parts=[
            "Collects commits whose changes span multiple modules and therefore affect release-note organization at a higher scope."
        ],
    )


def _create_supporting_section() -> _SectionDraft:
    return _SectionDraft(
        section_id="sec_supporting_updates",
        title="Supporting Updates",
        section_type="supporting-updates",
        group_order=3,
        sort_order=0,
        rationale_parts=[
            "Collects supporting, documentation, test, build, or otherwise non-module-centric updates."
        ],
    )


def _find_seeded_module_section(
    mapping: Dict[str, Any],
    seeded_by_module: Dict[str, _SectionDraft],
) -> Optional[_SectionDraft]:
    for key in (
        str(mapping.get("primary_module") or ""),
        str(mapping.get("primary_module_name") or ""),
    ):
        if key and key in seeded_by_module:
            return seeded_by_module[key]
    return None


def _get_or_create_fallback_module_section(
    mapping: Dict[str, Any],
    fallback_by_module: Dict[str, _SectionDraft],
    sections: List[_SectionDraft],
) -> Optional[_SectionDraft]:
    module_key = str(mapping.get("primary_module") or mapping.get("primary_module_name") or "").strip()
    if not module_key:
        return None

    existing = fallback_by_module.get(module_key)
    if existing is not None:
        return existing

    module_name = str(mapping.get("primary_module_name") or mapping.get("primary_module") or "").strip() or None
    section = _SectionDraft(
        section_id=f"sec_module_{_slugify(module_key)}",
        title=f"Localized Updates: {module_name or module_key}",
        section_type="module-updates",
        group_order=2,
        sort_order=0,
        primary_module=str(mapping.get("primary_module") or "").strip() or None,
        primary_module_name=module_name,
        primary_component=str(mapping.get("primary_component") or "").strip() or None,
        rationale_parts=[
            "Created as a fallback module section so localized commits can be absorbed into the release-note structure."
        ],
    )
    fallback_by_module[module_key] = section
    sections.append(section)
    return section


def _assign_commit_to_section(section: _SectionDraft, commit_id: str, mapping: Dict[str, Any]) -> None:
    if commit_id not in section.commit_ids:
        section.commit_ids.append(commit_id)

    for arch_change_id in mapping.get("matched_arch_change_ids") or []:
        if arch_change_id not in section.arch_change_ids:
            section.arch_change_ids.append(str(arch_change_id))

    for arch_change_type in mapping.get("matched_arch_change_types") or []:
        if arch_change_type not in section.arch_change_types:
            section.arch_change_types.append(str(arch_change_type))

    _append_unique(section.secondary_modules, mapping.get("secondary_modules") or [])
    _append_unique(section.secondary_module_names, mapping.get("secondary_module_names") or [])
    _append_unique(section.secondary_components, mapping.get("secondary_components") or [])

    if section.primary_component is None:
        section.primary_component = str(mapping.get("primary_component") or "").strip() or None

    if section.primary_module is None and section.section_type == "module-updates":
        section.primary_module = str(mapping.get("primary_module") or "").strip() or None
    if section.primary_module_name is None and section.section_type == "module-updates":
        section.primary_module_name = str(mapping.get("primary_module_name") or "").strip() or None


def _section_sort_key(section: _SectionDraft) -> tuple[Any, ...]:
    return (
        section.group_order,
        section.sort_order,
        -section.significance,
        section.title.lower(),
        section.section_id,
    )


def _build_stage3_stats(
    *,
    sections: List[ReleaseSectionPlan],
    total_commits: int,
    assigned_commits: int,
) -> Dict[str, Any]:
    return {
        "section_count": len(sections),
        "architecture_section_count": sum(
            1 for section in sections if section.section_type in {"module-added", "module-removed", "module-evolution"}
        ),
        "module_updates_section_count": sum(1 for section in sections if section.section_type == "module-updates"),
        "cross_module_section_count": sum(1 for section in sections if section.section_type == "cross-module"),
        "supporting_section_count": sum(1 for section in sections if section.section_type == "supporting-updates"),
        "assigned_commit_count": assigned_commits,
        "unassigned_commit_count": max(0, total_commits - assigned_commits),
        "empty_section_count": sum(1 for section in sections if not section.commit_ids),
    }


def _append_unique(target: List[str], values: List[Any]) -> None:
    existing = set(target)
    for value in values:
        text = str(value or "").strip()
        if not text or text in existing:
            continue
        target.append(text)
        existing.add(text)


def _slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", value.strip().lower()).strip("_")
    return slug or "unknown"
