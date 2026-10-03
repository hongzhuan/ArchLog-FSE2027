from __future__ import annotations

from pathlib import Path


STAGE_OUTPUT_DIRS = {
    "pipeline": "00_pipeline_summary",
    "code_changes": "01_code_changes",
    "phase1": "02_phase1_change_evidence",
    "phase2": "03_phase2_arch_signal_attribution",
    "phase3_1": "04_phase3_1_llm_aggregation_planning",
    "phase3_2": "05_phase3_2_slot_entry_generation",
    "phase3_3": "06_phase3_3_final_composition",
}


def stage_output_dir(output_root: Path, stage_key: str) -> Path:
    dirname = STAGE_OUTPUT_DIRS.get(stage_key)
    if dirname is None:
        raise KeyError(f"Unknown ArchLog output stage: {stage_key}")
    return Path(output_root) / dirname


def llm_io_dir(stage_dir: Path) -> Path:
    return Path(stage_dir) / "llm_io"
