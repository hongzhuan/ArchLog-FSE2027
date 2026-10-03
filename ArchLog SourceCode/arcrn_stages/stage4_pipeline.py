from __future__ import annotations

from pathlib import Path

from .models import Stage4PipelineResult
from .stage4_exporter import export_stage4_outputs
from .stage4_input_loader import load_stage4_inputs
from .stage4_llm_generator import maybe_generate_stage4_with_llm
from .stage4_section_fuser import build_stage4_section_summaries


def run_stage4_section_summaries(
    *,
    release_plan_path: Path,
    change_ir_path: Path,
    mapping_path: Path,
    diff_ir_path: Path,
    output_dir: Path,
    config=None,
) -> Stage4PipelineResult:
    loaded_inputs = load_stage4_inputs(
        release_plan_path=release_plan_path,
        change_ir_path=change_ir_path,
        mapping_path=mapping_path,
        diff_ir_path=diff_ir_path,
    )
    fallback_output = build_stage4_section_summaries(loaded_inputs)

    llm_audit_payloads = None
    if config is not None:
        section_summaries, llm_audit_payloads = maybe_generate_stage4_with_llm(
            config=config,
            loaded_inputs=loaded_inputs,
            fallback_output=fallback_output,
        )
    else:
        section_summaries = fallback_output

    output_files = export_stage4_outputs(section_summaries, output_dir, llm_audit_payloads=llm_audit_payloads)

    return Stage4PipelineResult(
        section_summaries=section_summaries,
        output_files=output_files,
    )
