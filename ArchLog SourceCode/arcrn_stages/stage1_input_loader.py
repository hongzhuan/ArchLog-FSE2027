from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional


REQUIRED_INPUT_CANDIDATES = {
    "change_units": ("step7_change_units.json", "change_units.json"),
    "summaries": ("step10_summaries.json", "code_change_summaries.json"),
}

OPTIONAL_INPUT_CANDIDATES = {
    "pipeline_report": ("pipeline_report.json",),
}


@dataclass
class Stage1LoadedInputs:
    input_dir: Path
    resolved_files: Dict[str, Path] = field(default_factory=dict)
    change_units: List[Dict[str, Any]] = field(default_factory=list)
    summaries: List[Dict[str, Any]] = field(default_factory=list)
    pipeline_report: Dict[str, Any] = field(default_factory=dict)


def load_stage1_inputs(input_dir: Path) -> Stage1LoadedInputs:
    if not input_dir.exists() or not input_dir.is_dir():
        raise FileNotFoundError(f"Stage 1 input directory not found: {input_dir}")

    resolved_files: Dict[str, Path] = {}

    for logical_name, candidates in REQUIRED_INPUT_CANDIDATES.items():
        resolved_files[logical_name] = _resolve_first_existing(input_dir, candidates, required=True)

    for logical_name, candidates in OPTIONAL_INPUT_CANDIDATES.items():
        resolved = _resolve_first_existing(input_dir, candidates, required=False)
        if resolved is not None:
            resolved_files[logical_name] = resolved

    change_units_payload = _load_json(resolved_files["change_units"])
    summaries_payload = _load_json(resolved_files["summaries"])
    pipeline_report_payload = {}

    if "pipeline_report" in resolved_files:
        pipeline_report_payload = _load_json(resolved_files["pipeline_report"])

    change_units = _ensure_list_payload(change_units_payload, "change_units")
    summaries = _ensure_list_payload(summaries_payload, "summaries")

    return Stage1LoadedInputs(
        input_dir=input_dir,
        resolved_files=resolved_files,
        change_units=change_units,
        summaries=summaries,
        pipeline_report=pipeline_report_payload,
    )


def _resolve_first_existing(input_dir: Path, candidates: tuple[str, ...], required: bool) -> Optional[Path]:
    for name in candidates:
        candidate_path = input_dir / name
        if candidate_path.exists() and candidate_path.is_file():
            return candidate_path

    if required:
        raise FileNotFoundError(
            f"Missing required Stage 1 input in {input_dir}. Tried: {', '.join(candidates)}"
        )
    return None


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _ensure_list_payload(payload: Dict[str, Any], key: str) -> List[Dict[str, Any]]:
    value = payload.get(key)
    if not isinstance(value, list):
        raise ValueError(f"Invalid Stage 1 input: expected list field '{key}'.")
    return [item for item in value if isinstance(item, dict)]
