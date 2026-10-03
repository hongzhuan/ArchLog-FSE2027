from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from .models import SectionSummariesOutput


def export_stage4_outputs(
    output: SectionSummariesOutput,
    output_dir: Path,
    llm_audit_payloads: Optional[Dict[str, Any]] = None,
) -> Dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)

    summaries_path = output_dir / "section_summaries.json"
    debug_md_path = output_dir / "section_summaries_debug.md"

    _write_json(summaries_path, output.to_dict())
    debug_md_path.write_text(_render_stage4_debug(output), encoding="utf-8")

    output_files = {
        "section_summaries": str(summaries_path),
        "section_summaries_debug": str(debug_md_path),
    }

    if llm_audit_payloads:
        prompts_path = output_dir / "stage4_llm_prompts.json"
        responses_path = output_dir / "stage4_llm_responses.json"
        _write_json(prompts_path, llm_audit_payloads.get("stage4_llm_prompts") or {})
        _write_json(responses_path, llm_audit_payloads.get("stage4_llm_responses") or {})
        output_files["stage4_llm_prompts"] = str(prompts_path)
        output_files["stage4_llm_responses"] = str(responses_path)

    return output_files


def _write_json(path: Path, payload: Dict) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def _render_stage4_debug(output: SectionSummariesOutput) -> str:
    lines: List[str] = []
    lines.append("# Section Summaries Debug Report")
    lines.append("")
    lines.append("## Overview")
    lines.append("")
    lines.append(f"- Generated at: `{output.generated_at}`")
    lines.append(f"- Source plan: `{output.source_plan_path}`")
    lines.append(f"- Source change_ir: `{output.source_change_ir_path}`")
    lines.append(f"- Source mapping: `{output.source_mapping_path}`")
    lines.append(f"- Source arch diff: `{output.source_arch_diff_path}`")
    for key, value in sorted(output.stats.items()):
        lines.append(f"- {key}: `{value}`")
    lines.append("")

    lines.append("## Section Summaries")
    lines.append("")
    for item in output.summaries:
        lines.append(f"### {item.title}")
        lines.append("")
        lines.append(f"- section_id: `{item.section_id}`")
        lines.append(f"- section_type: `{item.section_type}`")
        lines.append(f"- primary_module_name: `{item.primary_module_name or ''}`")
        lines.append(f"- primary_component: `{item.primary_component or ''}`")
        lines.append(f"- commit_ids ({len(item.commit_ids)}): {', '.join(f'`{value}`' for value in item.commit_ids) or '(none)'}")
        lines.append(f"- arch_change_ids: {', '.join(f'`{value}`' for value in item.arch_change_ids) or '(none)'}")
        lines.append("")
        lines.append("Summary:")
        lines.append("")
        lines.append("```text")
        lines.append(item.summary or "")
        lines.append("```")
        lines.append("")
        lines.append("Supporting details:")
        lines.append("")
        if item.supporting_details:
            for detail in item.supporting_details:
                lines.append(f"- {detail}")
        else:
            lines.append("- (none)")
        lines.append("")

    return "\n".join(lines)
