from __future__ import annotations

from pathlib import Path
from typing import Optional

from .models import Stage1PipelineResult
from .stage1_input_loader import load_stage1_inputs
from .stage1_ir_builder import build_stage1_change_ir
from .stage1_ir_exporter import export_stage1_outputs
from .stage1_ir_validator import validate_stage1_change_ir


def run_stage1_change_ir(input_dir: Path, output_dir: Optional[Path] = None) -> Stage1PipelineResult:
    loaded_inputs = load_stage1_inputs(input_dir)
    change_ir = build_stage1_change_ir(loaded_inputs)
    change_ir.validation = validate_stage1_change_ir(change_ir)

    output_root = output_dir or input_dir
    output_files = export_stage1_outputs(change_ir, output_root)

    return Stage1PipelineResult(
        change_ir=change_ir,
        output_files=output_files,
    )
