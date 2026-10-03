from __future__ import annotations

from pathlib import Path

from .models import Stage5PipelineResult
from .stage5_document_composer import build_stage5_final_release_note, render_final_release_note_markdown
from .stage5_exporter import export_stage5_outputs
from .stage5_input_loader import load_stage5_inputs
from .stage5_llm_generator import maybe_generate_stage5_with_llm


def run_stage5_final_release_note(
    *,
    release_plan_path: Path,
    section_summaries_path: Path,
    output_dir: Path,
    config=None,
) -> Stage5PipelineResult:
    loaded_inputs = load_stage5_inputs(
        release_plan_path=release_plan_path,
        section_summaries_path=section_summaries_path,
    )
    fallback_document = build_stage5_final_release_note(loaded_inputs)
    llm_audit_payloads = None
    if config is not None:
        document, llm_audit_payloads = maybe_generate_stage5_with_llm(
            config=config,
            loaded_inputs=loaded_inputs,
            fallback_document=fallback_document,
        )
    else:
        document = fallback_document

    markdown = render_final_release_note_markdown(document)
    output_files = export_stage5_outputs(document, markdown, output_dir, llm_audit_payloads=llm_audit_payloads)

    return Stage5PipelineResult(
        final_release_note=document,
        output_files=output_files,
    )
