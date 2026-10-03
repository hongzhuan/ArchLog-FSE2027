from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

from .models import ReleaseNotePlan


def export_stage3_outputs(release_plan: ReleaseNotePlan, output_dir: Path) -> Dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)

    release_plan_path = output_dir / "release_plan.json"
    debug_md_path = output_dir / "release_plan_debug.md"

    _write_json(release_plan_path, release_plan.to_dict())
    debug_md_path.write_text(_render_stage3_debug(release_plan), encoding="utf-8")

    return {
        "release_plan": str(release_plan_path),
        "release_plan_debug": str(debug_md_path),
    }


def _write_json(path: Path, payload: Dict) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def _render_stage3_debug(release_plan: ReleaseNotePlan) -> str:
    lines: List[str] = []
    lines.append("# Release Plan Debug Report")
    lines.append("")
    lines.append("## Overview")
    lines.append("")
    lines.append(f"- Generated at: `{release_plan.generated_at}`")
    lines.append(f"- Source change_ir: `{release_plan.source_change_ir_path}`")
    lines.append(f"- Source mapping: `{release_plan.source_mapping_path}`")
    lines.append(f"- Source arch diff: `{release_plan.source_arch_diff_path}`")
    for key, value in sorted(release_plan.stats.items()):
        lines.append(f"- {key}: `{value}`")
    lines.append("")

    lines.append("## Sections")
    lines.append("")
    for section in release_plan.sections:
        lines.append(f"### {section.title}")
        lines.append("")
        lines.append(f"- section_id: `{section.section_id}`")
        lines.append(f"- section_type: `{section.section_type}`")
        lines.append(f"- primary_module: `{section.primary_module or ''}`")
        lines.append(f"- primary_module_name: `{section.primary_module_name or ''}`")
        lines.append(f"- primary_component: `{section.primary_component or ''}`")
        lines.append(
            f"- secondary_module_names: {', '.join(f'`{item}`' for item in section.secondary_module_names) or '(none)'}"
        )
        lines.append(
            f"- secondary_components: {', '.join(f'`{item}`' for item in section.secondary_components) or '(none)'}"
        )
        lines.append(f"- commit_ids ({len(section.commit_ids)}): {', '.join(f'`{item}`' for item in section.commit_ids) or '(none)'}")
        lines.append(
            f"- arch_change_ids: {', '.join(f'`{item}`' for item in section.arch_change_ids) or '(none)'}"
        )
        lines.append(
            f"- arch_change_types: {', '.join(f'`{item}`' for item in section.arch_change_types) or '(none)'}"
        )
        lines.append("")
        lines.append("Rationale:")
        lines.append("")
        lines.append("```text")
        lines.append(section.rationale or "")
        lines.append("```")
        lines.append("")

    return "\n".join(lines)
