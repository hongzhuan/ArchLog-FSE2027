from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from arcrn_models import ChangeRecord, Phase1ChangeRecordsOutput, PhasePipelineResult, utc_now_iso
from arcrn_stages.stage1_input_loader import load_stage1_inputs
from arcrn_stages.stage1_ir_builder import build_stage1_change_ir
from arcrn_stages.stage1_ir_exporter import export_stage1_outputs
from arcrn_stages.stage1_ir_validator import validate_stage1_change_ir


def run_phase1_change_evidence_builder(input_dir: Path, output_dir: Optional[Path] = None) -> PhasePipelineResult:
    loaded_inputs = load_stage1_inputs(input_dir)
    change_ir = build_stage1_change_ir(loaded_inputs)
    change_ir.validation = validate_stage1_change_ir(change_ir)

    output_root = output_dir or input_dir
    legacy_outputs = export_stage1_outputs(change_ir, output_root)
    change_records = [_to_change_record(commit.to_dict()) for commit in change_ir.commits]

    output = Phase1ChangeRecordsOutput(
        generated_at=utc_now_iso(),
        source_change_ir_path=legacy_outputs["change_ir"],
        source_files=change_ir.source_files,
        change_records=change_records,
        stats={
            "change_record_count": len(change_records),
            "commit_count": len(change_records),
            "records_with_diff": sum(1 for item in change_records if item.diff_hunks),
            "records_with_call_context": sum(1 for item in change_records if item.call_context),
            "method_level_records": sum(1 for item in change_records if item.evidence_granularity == "method_level"),
            "hunk_level_fallback_records": sum(1 for item in change_records if item.evidence_granularity != "method_level"),
            "legacy_change_ir_written": 1,
        },
    )

    output_files = _export_phase1_outputs(output, output_root)
    output_files.update(legacy_outputs)
    return PhasePipelineResult(output_files=output_files, stats=output.stats)


def _to_change_record(commit: Dict[str, Any]) -> ChangeRecord:
    units = [unit for unit in commit.get("change_units") or [] if isinstance(unit, dict)]
    diff_hunks = _dedupe(
        snippet
        for unit in units
        for snippet in unit.get("diff_snippets") or []
        if str(snippet or "").strip()
    )
    call_context = "\n\n".join(
        str(unit.get("call_context") or "").strip()
        for unit in units
        if str(unit.get("call_context") or "").strip()
    )

    return ChangeRecord(
        commit_id=str(commit.get("commit_id") or ""),
        commit_message=str(commit.get("commit_message") or ""),
        commit_summary=str(commit.get("commit_summary") or commit.get("commit_message") or ""),
        commit_url=str(commit.get("commit_url") or "").strip() or None,
        pull_requests=[
            dict(item)
            for item in commit.get("pull_requests") or []
            if isinstance(item, dict) and item.get("number") and item.get("url")
        ],
        changed_files=[str(item) for item in commit.get("all_changed_files") or [] if str(item)],
        changed_methods=[str(item) for item in commit.get("all_changed_methods") or [] if str(item)],
        diff_hunks=diff_hunks,
        call_context=call_context,
        functional_category=str(commit.get("category") or "unknown"),
        evidence_granularity=_aggregate_evidence_granularity(units),
        change_detection_status=_aggregate_change_detection_status(units),
        source_refs={
            "legacy_change_ir": True,
            "change_unit_ids": [str(unit.get("change_unit_id")) for unit in units if unit.get("change_unit_id")],
            "evidence_granularity_by_unit": {
                str(unit.get("change_unit_id")): unit.get("evidence_granularity") or "method_level"
                for unit in units
                if unit.get("change_unit_id")
            },
            "change_detection_status_by_unit": {
                str(unit.get("change_unit_id")): unit.get("change_detection_status") or "method_level_change"
                for unit in units
                if unit.get("change_unit_id")
            },
            "source_refs_by_unit": {
                str(unit.get("change_unit_id")): unit.get("source_refs") or {}
                for unit in units
                if unit.get("change_unit_id")
            },
            "debug_info": commit.get("debug_info") or {},
        },
    )


def _export_phase1_outputs(output: Phase1ChangeRecordsOutput, output_dir: Path) -> Dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "change_records.json"
    debug_path = output_dir / "change_records_debug.md"

    _write_json(json_path, output.to_dict())
    debug_path.write_text(_render_debug(output), encoding="utf-8")
    return {
        "change_records": str(json_path),
        "change_records_debug": str(debug_path),
    }


def _render_debug(output: Phase1ChangeRecordsOutput) -> str:
    lines: List[str] = [
        "# Phase 1 Change Records Debug",
        "",
        "Phase 1 only normalizes multi-granularity code-change evidence. It does not judge architecture relevance.",
        "",
        "## Overview",
        "",
    ]
    for key, value in sorted(output.stats.items()):
        lines.append(f"- {key}: `{value}`")
    lines.append("")

    for record in output.change_records:
        lines.extend(
            [
                f"## {record.commit_id[:12] or 'unknown'}",
                "",
                f"- functional_category: `{record.functional_category}`",
                f"- changed_files: `{len(record.changed_files)}`",
                f"- changed_methods: `{len(record.changed_methods)}`",
                f"- diff_hunks: `{len(record.diff_hunks)}`",
                f"- evidence_granularity: `{record.evidence_granularity}`",
                f"- change_detection_status: `{record.change_detection_status}`",
                "",
                "Summary:",
                "",
                "```text",
                record.commit_summary,
                "```",
                "",
            ]
        )
    return "\n".join(lines)


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def _dedupe(values) -> List[str]:
    results: List[str] = []
    seen = set()
    for value in values:
        text = str(value or "").strip()
        if not text or text in seen:
            continue
        results.append(text)
        seen.add(text)
    return results


def _aggregate_evidence_granularity(units: List[Dict[str, Any]]) -> str:
    values = {
        str(unit.get("evidence_granularity") or "method_level")
        for unit in units
        if isinstance(unit, dict)
    }
    if not values:
        return "method_level"
    if values == {"method_level"}:
        return "method_level"
    if "method_level" in values:
        return "mixed"
    if len(values) == 1:
        return next(iter(values))
    return "mixed"


def _aggregate_change_detection_status(units: List[Dict[str, Any]]) -> str:
    values = {
        str(unit.get("change_detection_status") or "method_level_change")
        for unit in units
        if isinstance(unit, dict)
    }
    if not values:
        return "method_level_change"
    if len(values) == 1:
        return next(iter(values))
    if "method_level_change" in values:
        return "mixed"
    return sorted(values)[0]
