from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict


@dataclass
class Stage5LoadedInputs:
    release_plan: Dict[str, Any]
    section_summaries: Dict[str, Any]
    release_plan_path: Path
    section_summaries_path: Path


def load_stage5_inputs(
    *,
    release_plan_path: Path,
    section_summaries_path: Path,
) -> Stage5LoadedInputs:
    return Stage5LoadedInputs(
        release_plan=_load_json(release_plan_path),
        section_summaries=_load_json(section_summaries_path),
        release_plan_path=release_plan_path,
        section_summaries_path=section_summaries_path,
    )


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))
