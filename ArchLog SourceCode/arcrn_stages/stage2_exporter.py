from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

from .models import CommitArchMappingOutput


def export_stage2_outputs(output: CommitArchMappingOutput, output_dir: Path) -> Dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)

    mapping_json_path = output_dir / "commit_arch_mapping.json"
    debug_md_path = output_dir / "commit_arch_mapping_debug.md"

    _write_json(mapping_json_path, output.to_dict())
    debug_md_path.write_text(_render_stage2_debug(output), encoding="utf-8")

    return {
        "commit_arch_mapping": str(mapping_json_path),
        "commit_arch_mapping_debug": str(debug_md_path),
    }


def _write_json(path: Path, payload: Dict) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def _render_stage2_debug(output: CommitArchMappingOutput) -> str:
    lines: List[str] = []
    lines.append("# Commit Architecture Mapping Debug Report")
    lines.append("")
    lines.append("## Overview")
    lines.append("")
    lines.append(f"- Generated at: `{output.generated_at}`")
    lines.append(f"- Source change_ir: `{output.source_change_ir_path}`")
    for key, value in sorted(output.source_arch_inputs.items()):
        lines.append(f"- {key}: `{value}`")
    for key, value in sorted(output.stats.items()):
        lines.append(f"- {key}: `{value}`")
    lines.append("")

    lines.append("## Mappings")
    lines.append("")
    for mapping in output.mappings:
        lines.append(f"### {mapping.commit_id[:12]}")
        lines.append("")
        lines.append(f"- arch_label: `{mapping.arch_label}`")
        lines.append(f"- arch_confidence: `{mapping.arch_confidence}`")
        lines.append(f"- impact_score: `{mapping.impact_score}`")
        lines.append(f"- primary_module: `{mapping.primary_module or ''}`")
        lines.append(f"- primary_module_name: `{mapping.primary_module_name or ''}`")
        lines.append(f"- primary_component: `{mapping.primary_component or ''}`")
        lines.append(f"- scope: `{mapping.scope}`")
        lines.append(f"- secondary_modules: {', '.join(f'`{item}`' for item in mapping.secondary_modules) or '(none)'}")
        lines.append(
            f"- secondary_module_names: {', '.join(f'`{item}`' for item in mapping.secondary_module_names) or '(none)'}"
        )
        lines.append(f"- secondary_components: {', '.join(f'`{item}`' for item in mapping.secondary_components) or '(none)'}")
        lines.append(f"- changed_files: {', '.join(f'`{item}`' for item in mapping.changed_files[:12]) or '(none)'}")
        lines.append(f"- matched_arch_change_ids: {', '.join(f'`{item}`' for item in mapping.matched_arch_change_ids) or '(none)'}")
        lines.append(f"- matched_arch_change_types: {', '.join(f'`{item}`' for item in mapping.matched_arch_change_types) or '(none)'}")
        lines.append("")
        lines.append("Reasons:")
        lines.append("")
        for reason in mapping.arch_reasons:
            lines.append(f"- {reason}")
        lines.append("")

    return "\n".join(lines)
