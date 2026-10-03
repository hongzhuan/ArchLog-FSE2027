from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Set

from .stage2_input_loader import ArchChangeIndex, ArchChangeIndexEntry
from .stage2_module_mapper import CommitModuleMappingResult


STRONG_ARCH_CHANGE_TYPES = {"module_added", "module_removed", "module_changed"}


@dataclass
class CommitArchClassificationResult:
    arch_label: str
    arch_confidence: str
    arch_reasons: List[str] = field(default_factory=list)
    impact_score: float = 0.0
    matched_arch_change_ids: List[str] = field(default_factory=list)
    matched_arch_change_types: List[str] = field(default_factory=list)


def classify_commit_arch(
    commit_record: Dict,
    mapping_result: CommitModuleMappingResult,
    *,
    arch_index: ArchChangeIndex,
) -> CommitArchClassificationResult:
    changed_files = mapping_result.changed_files
    matched_change_ids = _collect_matched_change_ids(
        changed_files=changed_files,
        touched_modules=set(mapping_result.module_counts.keys()),
        arch_index=arch_index,
    )
    matched_entries = [arch_index.entries_by_id[change_id] for change_id in matched_change_ids]
    matched_change_types = sorted({entry.change_type for entry in matched_entries})

    reasons: List[str] = []
    impact_score = 0.0
    max_significance = max((entry.significance for entry in matched_entries), default=0.0)

    if matched_entries:
        reasons.append(
            f"changed_files matched architecture diff events: {', '.join(matched_change_ids[:5])}"
        )
        impact_score += 0.55
        impact_score += min(0.20, max_significance * 0.20)

    touched_modules = list(mapping_result.module_counts.keys())
    if len(touched_modules) > 1:
        reasons.append(f"commit spans multiple modules: {', '.join(sorted(touched_modules))}")
        impact_score += min(0.15, 0.05 * (len(touched_modules) - 1))

    arch_modules_touched = _collect_arch_modules_touched(touched_modules, arch_index)
    if arch_modules_touched:
        reasons.append(f"touched modules appear in architecture diff: {', '.join(sorted(arch_modules_touched))}")
        impact_score += min(0.10, 0.05 * len(arch_modules_touched))

    file_count = int(commit_record.get("file_count") or 0)
    method_count = int(commit_record.get("method_count") or 0)
    impact_score += min(0.10, 0.02 * file_count)
    impact_score += min(0.05, 0.01 * method_count)

    if mapping_result.scope == "supporting":
        reasons.append("all changed files look like supporting/test/docs assets")
        impact_score -= 0.10

    impact_score = round(max(0.0, min(1.0, impact_score)), 4)

    if matched_entries and any(entry.change_type in STRONG_ARCH_CHANGE_TYPES for entry in matched_entries):
        arch_label = "A-type"
        arch_confidence = "high"
    elif matched_entries:
        arch_label = "A-type"
        arch_confidence = "medium"
    elif mapping_result.scope == "cross-module" and arch_modules_touched:
        arch_label = "A-type"
        arch_confidence = "medium"
    elif mapping_result.scope in {"cross-module", "global"} and impact_score >= 0.65:
        arch_label = "A-type"
        arch_confidence = "low"
        reasons.append("high heuristic impact score without direct diff match")
    else:
        arch_label = "L-type"
        arch_confidence = "medium" if impact_score < 0.25 else "low"
        if not reasons:
            reasons.append("no explicit architecture diff match; change remains localized")

    return CommitArchClassificationResult(
        arch_label=arch_label,
        arch_confidence=arch_confidence,
        arch_reasons=reasons,
        impact_score=impact_score,
        matched_arch_change_ids=matched_change_ids,
        matched_arch_change_types=matched_change_types,
    )


def _collect_matched_change_ids(
    *,
    changed_files: List[str],
    touched_modules: Set[str],
    arch_index: ArchChangeIndex,
) -> List[str]:
    matched_ids: Set[str] = set()

    for file_path in changed_files:
        for change_id in arch_index.file_to_change_ids.get(file_path, []):
            matched_ids.add(change_id)

    for module_uid in touched_modules:
        for change_id in arch_index.module_uid_to_change_ids.get(module_uid, []):
            matched_ids.add(change_id)
        module_name = _base_module_name(module_uid)
        for change_id in arch_index.module_name_to_change_ids.get(module_name, []):
            matched_ids.add(change_id)

    return sorted(matched_ids)


def _collect_arch_modules_touched(touched_modules: List[str], arch_index: ArchChangeIndex) -> Set[str]:
    matched: Set[str] = set()
    for module_uid in touched_modules:
        if module_uid in arch_index.module_uid_to_change_ids:
            matched.add(module_uid)
            continue
        module_name = _base_module_name(module_uid)
        if module_name in arch_index.module_name_to_change_ids:
            matched.add(module_uid)
    return matched


def _base_module_name(module_uid: str) -> str:
    if "#" in module_uid:
        return module_uid.split("#", 1)[0]
    return module_uid
