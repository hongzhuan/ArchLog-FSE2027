from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence

from .models import SectionSummariesOutput, SectionSummaryRecord, utc_now_iso
from .stage4_input_loader import Stage4ArchChange, Stage4LoadedInputs


@dataclass
class _CommitContext:
    section_order: int
    commit: Dict[str, Any]
    mapping: Dict[str, Any]


def build_stage4_section_summaries(loaded_inputs: Stage4LoadedInputs) -> SectionSummariesOutput:
    commit_lookup = _build_commit_lookup(loaded_inputs.change_ir)
    mapping_lookup = _build_mapping_lookup(loaded_inputs.mapping_output)
    arch_change_lookup = {item.change_id: item for item in loaded_inputs.arch_changes}

    summaries: List[SectionSummaryRecord] = []
    for section in loaded_inputs.release_plan.get("sections") or []:
        commit_contexts = _collect_commit_contexts(section, commit_lookup, mapping_lookup)
        arch_contexts = _collect_arch_contexts(section, arch_change_lookup)

        summary_text = _build_section_summary_text(section, commit_contexts, arch_contexts)
        supporting_details = _build_supporting_details(section, commit_contexts, arch_contexts)

        summaries.append(
            SectionSummaryRecord(
                section_id=str(section.get("section_id") or ""),
                title=str(section.get("title") or ""),
                section_type=str(section.get("section_type") or ""),
                summary=summary_text,
                primary_module_name=str(section.get("primary_module_name") or "").strip() or None,
                primary_component=str(section.get("primary_component") or "").strip() or None,
                commit_ids=[str(item) for item in section.get("commit_ids") or [] if str(item)],
                arch_change_ids=[str(item) for item in section.get("arch_change_ids") or [] if str(item)],
                supporting_details=supporting_details,
            )
        )

    stats = _build_stage4_stats(summaries)
    return SectionSummariesOutput(
        generated_at=utc_now_iso(),
        source_plan_path=str(loaded_inputs.release_plan_path),
        source_change_ir_path=str(loaded_inputs.change_ir_path),
        source_mapping_path=str(loaded_inputs.mapping_path),
        source_arch_diff_path=str(loaded_inputs.diff_ir_path),
        summaries=summaries,
        stats=stats,
    )


def _build_commit_lookup(change_ir: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    return {
        str(commit.get("commit_id") or ""): commit
        for commit in change_ir.get("commits") or []
        if isinstance(commit, dict) and str(commit.get("commit_id") or "")
    }


def _build_mapping_lookup(mapping_output: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    return {
        str(mapping.get("commit_id") or ""): mapping
        for mapping in mapping_output.get("mappings") or []
        if isinstance(mapping, dict) and str(mapping.get("commit_id") or "")
    }


def _collect_commit_contexts(
    section: Dict[str, Any],
    commit_lookup: Dict[str, Dict[str, Any]],
    mapping_lookup: Dict[str, Dict[str, Any]],
) -> List[_CommitContext]:
    commit_contexts: List[_CommitContext] = []
    for index, commit_id in enumerate(section.get("commit_ids") or []):
        commit = commit_lookup.get(str(commit_id))
        mapping = mapping_lookup.get(str(commit_id))
        if commit is None or mapping is None:
            continue
        commit_contexts.append(_CommitContext(section_order=index, commit=commit, mapping=mapping))
    return commit_contexts


def _collect_arch_contexts(
    section: Dict[str, Any],
    arch_change_lookup: Dict[str, Stage4ArchChange],
) -> List[Stage4ArchChange]:
    arch_contexts: List[Stage4ArchChange] = []
    for arch_change_id in section.get("arch_change_ids") or []:
        arch_change = arch_change_lookup.get(str(arch_change_id))
        if arch_change is not None:
            arch_contexts.append(arch_change)
    return arch_contexts


def _build_section_summary_text(
    section: Dict[str, Any],
    commit_contexts: List[_CommitContext],
    arch_contexts: List[Stage4ArchChange],
) -> str:
    section_type = str(section.get("section_type") or "")
    title = str(section.get("title") or "")
    module_name = str(section.get("primary_module_name") or section.get("primary_module") or "").strip() or "this area"
    component_name = str(section.get("primary_component") or "").strip() or None
    commit_count = len(commit_contexts)

    lead = _build_lead_sentence(
        title=title,
        section_type=section_type,
        module_name=module_name,
        component_name=component_name,
        commit_count=commit_count,
        secondary_module_names=[str(item) for item in section.get("secondary_module_names") or [] if str(item)],
    )

    arch_themes = _collect_arch_themes(arch_contexts, max_items=2)
    commit_themes = _collect_commit_themes(commit_contexts, max_items=2)
    evidence = _build_evidence_sentence(arch_themes, commit_themes, commit_count)

    return " ".join(part for part in [lead, evidence] if part).strip()


def _build_lead_sentence(
    *,
    title: str,
    section_type: str,
    module_name: str,
    component_name: Optional[str],
    commit_count: int,
    secondary_module_names: List[str],
) -> str:
    component_clause = f" inside {component_name}" if component_name else ""

    if section_type == "module-added":
        return f"{title} records a version-level structural addition around {module_name}{component_clause}."
    if section_type == "module-removed":
        return f"{title} records a version-level structural removal around {module_name}{component_clause}."
    if section_type == "module-evolution":
        return f"{title} captures structural evolution in {module_name}{component_clause} and currently groups {commit_count} mapped commits."
    if section_type == "cross-module":
        modules = _format_list(secondary_module_names[:4])
        if modules:
            return f"{title} groups {commit_count} commits whose effects cross module boundaries, especially {modules}."
        return f"{title} groups {commit_count} commits whose effects cross module boundaries."
    if section_type == "supporting-updates":
        return f"{title} gathers {commit_count} non-module-centric commits across tests, documentation, build, or tooling assets."
    if section_type == "module-updates":
        return f"{title} compresses {commit_count} localized commits within {module_name}{component_clause}."
    return f"{title} groups {commit_count} commits for downstream release-note composition."


def _build_evidence_sentence(
    arch_themes: List[str],
    commit_themes: List[str],
    commit_count: int,
) -> str:
    if arch_themes and commit_themes:
        return (
            f"Architectural evidence highlights {_format_list(arch_themes)}, while representative commit-level themes include "
            f"{_format_list(commit_themes)}."
        )
    if arch_themes:
        suffix = ""
        if commit_count == 0:
            suffix = " No directly mapped commit summaries were available, so the section is retained as architectural context."
        return f"Architectural evidence highlights {_format_list(arch_themes)}.{suffix}"
    if commit_themes:
        return f"Representative commit-level themes include {_format_list(commit_themes)}."
    return "No additional section evidence was available beyond the release-plan structure."


def _collect_arch_themes(arch_contexts: List[Stage4ArchChange], max_items: int) -> List[str]:
    themes: List[str] = []
    seen = set()
    for arch_change in sorted(arch_contexts, key=lambda item: (-item.significance, item.change_id)):
        candidate = _strip_terminal_punctuation(_clean_text(arch_change.summary or ""))
        if not candidate:
            continue
        normalized = _normalize_for_dedup(candidate)
        if normalized in seen:
            continue
        seen.add(normalized)
        themes.append(_truncate_text(candidate, 140))
        if len(themes) >= max_items:
            break
    return themes


def _collect_commit_themes(commit_contexts: List[_CommitContext], max_items: int) -> List[str]:
    themes: List[str] = []
    seen = set()
    for context in _rank_commit_contexts(commit_contexts):
        candidate = _strip_terminal_punctuation(_extract_commit_theme(context.commit))
        if not candidate:
            continue
        normalized = _normalize_for_dedup(candidate)
        if normalized in seen:
            continue
        seen.add(normalized)
        themes.append(_truncate_text(candidate, 120))
        if len(themes) >= max_items:
            break
    return themes


def _rank_commit_contexts(commit_contexts: List[_CommitContext]) -> List[_CommitContext]:
    return [
        item
        for item in sorted(
            commit_contexts,
            key=lambda context: (
                -_arch_priority(context.mapping),
                -_safe_float(context.mapping.get("impact_score")),
                -_safe_int(context.commit.get("file_count")),
                -_safe_int(context.commit.get("method_count")),
                context.section_order,
            ),
        )
    ]


def _build_supporting_details(
    section: Dict[str, Any],
    commit_contexts: List[_CommitContext],
    arch_contexts: List[Stage4ArchChange],
) -> List[str]:
    details: List[str] = []

    if section.get("secondary_module_names"):
        modules = [str(item) for item in section.get("secondary_module_names") or [] if str(item)]
        details.append(f"Modules involved: {_format_list(modules[:6])}")

    for arch_change in sorted(arch_contexts, key=lambda item: (-item.significance, item.change_id))[:2]:
        summary = _truncate_text(_clean_text(arch_change.summary or ""), 180)
        if summary:
            details.append(
                f"Architecture [{arch_change.change_id} | {arch_change.change_type}]: {summary}"
            )
        if arch_change.related_files:
            details.append(
                f"Related files: {', '.join(arch_change.related_files[:5])}"
            )

    for context in _rank_commit_contexts(commit_contexts)[:4]:
        commit_id = str(context.commit.get("commit_id") or "")[:8]
        commit_theme = _truncate_text(_extract_commit_theme(context.commit), 180)
        arch_label = str(context.mapping.get("arch_label") or "")
        scope = str(context.mapping.get("scope") or "")
        counts = (
            f"files={_safe_int(context.commit.get('file_count'))}, "
            f"methods={_safe_int(context.commit.get('method_count'))}"
        )
        if commit_theme:
            details.append(f"Commit {commit_id} [{arch_label}, {scope}, {counts}]: {commit_theme}")

    if not details and section.get("rationale"):
        details.append(_truncate_text(_clean_text(str(section.get("rationale") or "")), 180))

    return details


def _build_stage4_stats(summaries: List[SectionSummaryRecord]) -> Dict[str, Any]:
    return {
        "summary_count": len(summaries),
        "arch_only_section_count": sum(1 for item in summaries if item.arch_change_ids and not item.commit_ids),
        "mixed_evidence_section_count": sum(1 for item in summaries if item.arch_change_ids and item.commit_ids),
        "commit_only_section_count": sum(1 for item in summaries if item.commit_ids and not item.arch_change_ids),
        "sections_with_supporting_details_count": sum(1 for item in summaries if item.supporting_details),
        "total_supporting_detail_count": sum(len(item.supporting_details) for item in summaries),
    }


def _extract_commit_theme(commit: Dict[str, Any]) -> str:
    summary = _clean_text(str(commit.get("commit_summary") or ""))
    if summary:
        return summary

    message = _clean_text(str(commit.get("commit_message") or ""))
    if not message:
        return ""
    return _first_line(message)


def _arch_priority(mapping: Dict[str, Any]) -> int:
    return 1 if str(mapping.get("arch_label") or "") == "A-type" else 0


def _safe_int(value: Any) -> int:
    try:
        return int(value)
    except Exception:
        return 0


def _safe_float(value: Any) -> float:
    try:
        return float(value)
    except Exception:
        return 0.0


def _format_list(items: Sequence[str]) -> str:
    values = [item for item in items if item]
    if not values:
        return ""
    if len(values) == 1:
        return values[0]
    if len(values) == 2:
        return f"{values[0]} and {values[1]}"
    return ", ".join(values[:-1]) + f", and {values[-1]}"


def _clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def _first_line(value: str) -> str:
    return value.splitlines()[0].strip() if value else ""


def _normalize_for_dedup(value: str) -> str:
    return _clean_text(value).lower()


def _truncate_text(value: str, limit: int) -> str:
    text = _clean_text(value)
    if len(text) <= limit:
        return text
    return text[: max(0, limit - 3)].rstrip() + "..."


def _strip_terminal_punctuation(value: str) -> str:
    return value.rstrip(" .,!?:;。！？；：")
