from __future__ import annotations

from pathlib import Path

from .models import Stage3PipelineResult
from .stage3_exporter import export_stage3_outputs
from .stage3_input_loader import load_stage3_inputs
from .stage3_skeleton_builder import build_stage3_release_plan


def run_stage3_release_plan(
    *,
    change_ir_path: Path,
    mapping_path: Path,
    diff_ir_path: Path,
    output_dir: Path,
) -> Stage3PipelineResult:
    loaded_inputs = load_stage3_inputs(
        change_ir_path=change_ir_path,
        mapping_path=mapping_path,
        diff_ir_path=diff_ir_path,
    )
    release_plan = build_stage3_release_plan(loaded_inputs)
    output_files = export_stage3_outputs(release_plan, output_dir)

    return Stage3PipelineResult(
        release_plan=release_plan,
        output_files=output_files,
    )
