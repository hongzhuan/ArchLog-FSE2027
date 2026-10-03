from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

from .models import ChangeIR


def export_stage1_outputs(change_ir: ChangeIR, output_dir: Path) -> Dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)

    change_ir_path = output_dir / "change_ir.json"
    debug_md_path = output_dir / "change_ir_debug.md"

    _write_json(change_ir_path, change_ir.to_dict())
    debug_md_path.write_text(_render_change_ir_debug(change_ir), encoding="utf-8")

    return {
        "change_ir": str(change_ir_path),
        "change_ir_debug": str(debug_md_path),
    }


def _write_json(path: Path, payload: Dict) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def _render_change_ir_debug(change_ir: ChangeIR) -> str:
    lines: List[str] = []
    lines.append("# Change IR Debug Report")
    lines.append("")
    lines.append("## Overview")
    lines.append("")
    lines.append(f"- Generated at: `{change_ir.generated_at}`")
    lines.append(f"- Input dir: `{change_ir.input_dir}`")
    lines.append(f"- Commit count: `{change_ir.stats.get('commit_count', 0)}`")
    lines.append(f"- Change unit count: `{change_ir.stats.get('change_unit_count', 0)}`")
    lines.append(f"- Commits with diff: `{change_ir.stats.get('commits_with_diff', 0)}`")
    lines.append(f"- Commits with call context: `{change_ir.stats.get('commits_with_call_context', 0)}`")
    lines.append(f"- Validation warnings: `{change_ir.validation.warning_count}`")
    lines.append("")

    if change_ir.source_files:
        lines.append("## Source Files")
        lines.append("")
        for key, path in sorted(change_ir.source_files.items()):
            lines.append(f"- `{key}`: `{path}`")
        lines.append("")

    lines.append("## Commits")
    lines.append("")

    for commit in change_ir.commits:
        lines.append(f"### {commit.commit_id[:12] if commit.commit_id else 'unknown'}")
        lines.append("")
        lines.append(f"- Date: `{commit.date or ''}`")
        lines.append(f"- Author: `{commit.author or ''}`")
        lines.append(f"- Category: `{commit.category or ''}`")
        lines.append(f"- Change units: `{commit.change_unit_count}`")
        lines.append(f"- Files ({commit.file_count}): {', '.join(f'`{item}`' for item in commit.all_changed_files[:12])}")
        lines.append(f"- Methods ({commit.method_count}): {', '.join(f'`{item}`' for item in commit.all_changed_methods[:12])}")
        lines.append("")
        lines.append("Commit message:")
        lines.append("")
        lines.append("```text")
        lines.append(commit.commit_message or "")
        lines.append("```")
        lines.append("")
        lines.append("Commit summary:")
        lines.append("")
        lines.append("```text")
        lines.append(commit.commit_summary or "")
        lines.append("```")
        lines.append("")
        lines.append("Change units:")
        lines.append("")

        for unit in commit.change_units:
            lines.append(f"- `{unit.change_unit_id}` | category=`{unit.category or ''}`")
            lines.append(f"  - evidence_granularity: `{unit.evidence_granularity}`")
            lines.append(f"  - change_detection_status: `{unit.change_detection_status}`")
            lines.append(f"  - summary: {unit.summary or ''}")
            lines.append(f"  - files: {', '.join(unit.changed_files[:10])}")
            lines.append(f"  - methods: {', '.join(unit.changed_methods[:10])}")
            lines.append(f"  - matched_hunks: {', '.join(unit.matched_hunk_ids[:10])}")

        lines.append("")

    if change_ir.validation.issues:
        lines.append("## Validation Issues")
        lines.append("")
        for issue in change_ir.validation.issues:
            location = []
            if issue.commit_id:
                location.append(f"commit={issue.commit_id[:12]}")
            if issue.change_unit_id:
                location.append(f"unit={issue.change_unit_id}")
            suffix = f" ({', '.join(location)})" if location else ""
            lines.append(f"- [{issue.level}] {issue.message}{suffix}")
        lines.append("")

    return "\n".join(lines)
