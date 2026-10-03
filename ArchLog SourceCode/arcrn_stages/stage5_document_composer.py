from __future__ import annotations

import re
from typing import Any, Dict, List, Sequence

from .models import FinalReleaseNoteDocument, FinalReleaseNoteSection, utc_now_iso
from .stage5_input_loader import Stage5LoadedInputs


MAX_HIGHLIGHTS = 3
MAX_SECTION_KEY_POINTS = 4


def build_stage5_final_release_note(loaded_inputs: Stage5LoadedInputs) -> FinalReleaseNoteDocument:
    section_records = _build_final_sections(loaded_inputs.section_summaries)
    overview = _compose_overview(loaded_inputs.release_plan, loaded_inputs.section_summaries, section_records)
    highlights = _compose_highlights(section_records)

    stats = {
        "section_count": len(section_records),
        "highlight_count": len(highlights),
        "total_key_point_count": sum(len(section.key_points) for section in section_records),
        "architecture_section_count": sum(
            1 for section in section_records if section.section_type in {"module-added", "module-removed", "module-evolution"}
        ),
        "cross_module_section_count": sum(1 for section in section_records if section.section_type == "cross-module"),
        "supporting_section_count": sum(1 for section in section_records if section.section_type == "supporting-updates"),
    }

    return FinalReleaseNoteDocument(
        generated_at=utc_now_iso(),
        source_plan_path=str(loaded_inputs.release_plan_path),
        source_section_summaries_path=str(loaded_inputs.section_summaries_path),
        title="Architecture-Guided Release Note",
        overview=overview,
        highlights=highlights,
        sections=section_records,
        stats=stats,
    )


def render_final_release_note_markdown(document: FinalReleaseNoteDocument) -> str:
    lines: List[str] = []
    lines.append(f"# {document.title}")
    lines.append("")
    lines.append("## Overview")
    lines.append("")
    lines.append(document.overview)
    lines.append("")

    if document.highlights:
        lines.append("## Highlights")
        lines.append("")
        for item in document.highlights:
            lines.append(f"- {item}")
        lines.append("")

    for section in document.sections:
        lines.append(f"## {section.title}")
        lines.append("")
        lines.append(section.summary)
        lines.append("")
        if section.key_points:
            lines.append("Key points:")
            lines.append("")
            for item in section.key_points:
                lines.append(f"- {item}")
            lines.append("")

    return "\n".join(lines)


def _build_final_sections(section_summaries: Dict[str, Any]) -> List[FinalReleaseNoteSection]:
    sections: List[FinalReleaseNoteSection] = []
    for item in section_summaries.get("summaries") or []:
        if not isinstance(item, dict):
            continue
        key_points = _dedupe_preserve_order(
            [
                _truncate_sentence(_clean_text(str(value or "")), 220)
                for value in item.get("supporting_details") or []
                if _clean_text(str(value or ""))
            ]
        )[:MAX_SECTION_KEY_POINTS]

        sections.append(
            FinalReleaseNoteSection(
                section_id=str(item.get("section_id") or "").strip() or None,
                title=str(item.get("title") or ""),
                section_type=str(item.get("section_type") or ""),
                summary=_clean_text(str(item.get("summary") or "")),
                primary_module_name=str(item.get("primary_module_name") or "").strip() or None,
                primary_component=str(item.get("primary_component") or "").strip() or None,
                commit_count=len(item.get("commit_ids") or []),
                arch_change_count=len(item.get("arch_change_ids") or []),
                key_points=key_points,
            )
        )

    return sections


def _compose_overview(
    release_plan: Dict[str, Any],
    section_summaries: Dict[str, Any],
    section_records: List[FinalReleaseNoteSection],
) -> str:
    plan_stats = release_plan.get("stats") or {}
    summary_stats = section_summaries.get("stats") or {}

    assigned_commit_count = _safe_int(plan_stats.get("assigned_commit_count"))
    section_count = len(section_records)
    architecture_sections = sum(
        1 for section in section_records if section.section_type in {"module-added", "module-removed", "module-evolution"}
    )
    cross_module_sections = sum(1 for section in section_records if section.section_type == "cross-module")
    module_sections = sum(1 for section in section_records if section.section_type == "module-updates")
    supporting_sections = sum(1 for section in section_records if section.section_type == "supporting-updates")
    arch_only_sections = _safe_int(summary_stats.get("arch_only_section_count"))

    sentences = [
        f"This release note summarizes {assigned_commit_count} mapped commits across {section_count} structured sections.",
        f"The document is anchored by {architecture_sections} architecture-driven sections, {cross_module_sections} cross-module section{'s' if cross_module_sections != 1 else ''}, and {module_sections} localized module section{'s' if module_sections != 1 else ''}.",
    ]
    if supporting_sections:
        sentences.append(
            f"Supporting changes are consolidated into {supporting_sections} dedicated section{'s' if supporting_sections != 1 else ''}."
        )
    if arch_only_sections:
        sentences.append(
            f"{arch_only_sections} section{'s are' if arch_only_sections != 1 else ' is'} retained as architecture-only context so version-level structural shifts remain visible even without direct commit-level evidence."
        )

    return " ".join(sentences)


def _compose_highlights(section_records: List[FinalReleaseNoteSection]) -> List[str]:
    ranked_sections = sorted(
        section_records,
        key=lambda section: (
            -_highlight_priority(section),
            -section.arch_change_count,
            -section.commit_count,
            section.title.lower(),
        ),
    )

    highlights: List[str] = []
    seen = set()
    for section in ranked_sections:
        highlight = _build_highlight_line(section)
        normalized = _normalize_text(highlight)
        if not highlight or normalized in seen:
            continue
        highlights.append(highlight)
        seen.add(normalized)
        if len(highlights) >= MAX_HIGHLIGHTS:
            break
    return highlights


def _build_highlight_line(section: FinalReleaseNoteSection) -> str:
    if section.section_type == "module-added":
        target = section.primary_module_name or section.title
        return f"{target} is surfaced as a version-level structural addition."
    if section.section_type == "module-removed":
        target = section.primary_module_name or section.title
        return f"{target} is surfaced as a version-level structural removal."
    if section.section_type == "module-evolution":
        target = section.primary_module_name or section.title
        return f"{target} is highlighted as a structural evolution area with {section.commit_count} mapped commits."
    if section.section_type == "cross-module":
        return f"Cross-module impacts connect {section.commit_count} commits that cut across architectural boundaries."
    if section.section_type == "module-updates":
        target = section.primary_module_name or section.title
        return f"{target} concentrates {section.commit_count} localized follow-up commits."
    if section.section_type == "supporting-updates":
        return f"Supporting updates consolidate {section.commit_count} non-module-centric changes."
    return _first_sentence(section.summary)


def _highlight_priority(section: FinalReleaseNoteSection) -> int:
    order = {
        "module-added": 5,
        "module-removed": 5,
        "module-evolution": 4,
        "cross-module": 3,
        "module-updates": 2,
        "supporting-updates": 1,
    }
    return order.get(section.section_type, 0)


def _dedupe_preserve_order(items: Sequence[str]) -> List[str]:
    results: List[str] = []
    seen = set()
    for item in items:
        normalized = _normalize_text(item)
        if not normalized or normalized in seen:
            continue
        results.append(item)
        seen.add(normalized)
    return results


def _truncate_sentence(value: str, limit: int) -> str:
    text = value.strip()
    if len(text) <= limit:
        return text
    return text[: max(0, limit - 3)].rstrip() + "..."


def _first_sentence(value: str) -> str:
    text = _clean_text(value)
    if not text:
        return ""
    match = re.split(r"(?<=[.!?])\s+", text, maxsplit=1)
    return match[0]


def _clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def _normalize_text(value: str) -> str:
    return _clean_text(value).lower()


def _safe_int(value: Any) -> int:
    try:
        return int(value)
    except Exception:
        return 0
