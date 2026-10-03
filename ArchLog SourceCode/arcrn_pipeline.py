from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Tuple

from arcrn_external_analysis import prepare_external_analysis_inputs
from arcrn_metrics import duration_between_iso, elapsed_sec, start_timer, write_experiment_metrics
from arcrn_output_layout import stage_output_dir
from arcrn_stages.models import ArcRNPipelineResult, ArcRNPipelineStageRecord, utc_now_iso
from phase1_change_evidence_builder import run_phase1_change_evidence_builder
from phase2_arch_signal_attributor import run_phase2_arch_signal_attribution
from phase3_llm_aggregation_planner import run_phase3_llm_aggregation_planner
from phase3_release_note_composer import run_phase3_release_note_composer
from phase3_slot_entry_generator import run_phase3_slot_entry_generator
from run_code_changes import run_code_changes_subpipeline


def run_arcrn_pipeline(config, *, include_code_changes: bool = True) -> ArcRNPipelineResult:
    pipeline_started_at, pipeline_started_perf = start_timer()
    output_dir = Path(config.output_dir)
    code_changes_dir = stage_output_dir(output_dir, "code_changes")
    phase1_dir = stage_output_dir(output_dir, "phase1")
    phase2_dir = stage_output_dir(output_dir, "phase2")
    phase3_1_dir = stage_output_dir(output_dir, "phase3_1")
    phase3_2_dir = stage_output_dir(output_dir, "phase3_2")
    phase3_3_dir = stage_output_dir(output_dir, "phase3_3")
    pipeline_dir = stage_output_dir(output_dir, "pipeline")
    repo_name = config.repo_path.name
    stages = []
    if bool(getattr(config, "external_analysis_enabled", False)):
        stage_started_at, stage_started_perf = start_timer()
        external_outputs = prepare_external_analysis_inputs(config)
        stage_finished_at = utc_now_iso()
        stages.append(
            ArcRNPipelineStageRecord(
                stage_name="external_analysis_input_preparation",
                started_at=stage_started_at,
                finished_at=stage_finished_at,
                duration_sec=elapsed_sec(stage_started_perf),
                output_files=external_outputs,
                stats={"generated_or_reused_artifact_count": len(external_outputs)},
            )
        )
    diff_ir_path = _find_latest_diff_ir(config=config, repo_name=repo_name, base_ref=config.base_ref, new_ref=config.new_ref)
    semarc_paths = _build_semarc_paths(config=config, repo_name=repo_name, base_ref=config.base_ref, new_ref=config.new_ref)

    if include_code_changes:
        stage_started_at, stage_started_perf = start_timer()
        code_changes_result = run_code_changes_subpipeline(config)
        stage_finished_at = utc_now_iso()
        stages.append(
            ArcRNPipelineStageRecord(
                stage_name="code_changes",
                started_at=stage_started_at,
                finished_at=stage_finished_at,
                duration_sec=elapsed_sec(stage_started_perf),
                output_files=code_changes_result.output_files,
                stats=code_changes_result.pipeline_result.report.final_stats or {},
            )
        )

    phase1_input_dir = code_changes_dir if include_code_changes else output_dir
    print("\n" + "=" * 100, flush=True)
    print("RUNNING PHASE 1 MULTI-SOURCE CHANGE EVIDENCE CONSTRUCTION", flush=True)
    print("=" * 100, flush=True)
    print(f"Input dir: {phase1_input_dir}", flush=True)
    print(f"Output dir: {phase1_dir}", flush=True)
    phase1_started_at, phase1_started_perf = start_timer()
    phase1_result = run_phase1_change_evidence_builder(input_dir=phase1_input_dir, output_dir=phase1_dir)
    phase1_finished_at = utc_now_iso()
    print(f"FINISHED PHASE 1 MULTI-SOURCE CHANGE EVIDENCE CONSTRUCTION ({elapsed_sec(phase1_started_perf):.1f}s).", flush=True)

    print("\n" + "=" * 100, flush=True)
    print("RUNNING PHASE 2 KEY DESIGN-DECISION COMMIT IDENTIFICATION", flush=True)
    print("=" * 100, flush=True)
    print(f"Change records: {phase1_result.output_files['change_records']}", flush=True)
    print(f"Architecture diff IR: {diff_ir_path}", flush=True)
    print(f"Output dir: {phase2_dir}", flush=True)
    phase2_started_at, phase2_started_perf = start_timer()
    phase2_result = run_phase2_arch_signal_attribution(
        change_records_path=Path(phase1_result.output_files["change_records"]),
        diff_ir_path=diff_ir_path,
        diff_summary_path=diff_ir_path.parent / "diff_summary.md",
        archsem_old_path=semarc_paths["archsem_old"],
        codesem_old_path=semarc_paths["codesem_old"],
        namedclusters_old_path=semarc_paths["namedclusters_old"],
        clustercomponent_old_path=semarc_paths["clustercomponent_old"],
        archsem_new_path=semarc_paths["archsem_new"],
        codesem_new_path=semarc_paths["codesem_new"],
        namedclusters_new_path=semarc_paths["namedclusters_new"],
        clustercomponent_new_path=semarc_paths["clustercomponent_new"],
        output_dir=phase2_dir,
        config=config,
    )
    phase2_finished_at = utc_now_iso()
    print(f"FINISHED PHASE 2 KEY DESIGN-DECISION COMMIT IDENTIFICATION ({elapsed_sec(phase2_started_perf):.1f}s).", flush=True)

    print("\n" + "=" * 100, flush=True)
    print("RUNNING PHASE 3.1 LLM AGGREGATION PLANNING", flush=True)
    print("=" * 100, flush=True)
    print(f"Input records: {phase2_result.output_files['attributed_change_records']}", flush=True)
    print(f"Output dir: {phase3_1_dir}", flush=True)
    phase3_1_started_at, phase3_1_started_perf = start_timer()
    aggregation_plan_result = run_phase3_llm_aggregation_planner(
        attributed_change_records_path=Path(phase2_result.output_files["attributed_change_records"]),
        output_dir=phase3_1_dir,
        config=config,
    )
    phase3_1_finished_at = utc_now_iso()
    print(f"FINISHED PHASE 3.1 LLM AGGREGATION PLANNING ({elapsed_sec(phase3_1_started_perf):.1f}s).", flush=True)

    print("\n" + "=" * 100, flush=True)
    print("RUNNING PHASE 3.2 SLOT ENTRY GENERATION", flush=True)
    print("=" * 100, flush=True)
    print(f"Aggregation plan: {aggregation_plan_result.output_files['aggregation_plan']}", flush=True)
    print(f"Output dir: {phase3_2_dir}", flush=True)
    stage_started_at_phase3_2, stage_started_perf_phase3_2 = start_timer()
    section_entries_result = run_phase3_slot_entry_generator(
        aggregation_plan_path=Path(aggregation_plan_result.output_files["aggregation_plan"]),
        attributed_change_records_path=Path(phase2_result.output_files["attributed_change_records"]),
        output_dir=phase3_2_dir,
        config=config,
    )
    phase3_2_finished_at = utc_now_iso()
    print(f"FINISHED PHASE 3.2 SLOT ENTRY GENERATION ({elapsed_sec(stage_started_perf_phase3_2):.1f}s).", flush=True)

    print("\n" + "=" * 100, flush=True)
    print("RUNNING PHASE 3.3 FINAL RELEASE NOTE COMPOSITION", flush=True)
    print("=" * 100, flush=True)
    print(f"Section entries: {section_entries_result.output_files['section_entries']}", flush=True)
    print(f"Output dir: {phase3_3_dir}", flush=True)
    stage_started_at_phase3_3, stage_started_perf_phase3_3 = start_timer()
    final_note_result = run_phase3_release_note_composer(
        section_entries_path=Path(section_entries_result.output_files["section_entries"]),
        output_dir=phase3_3_dir,
        config=config,
    )
    phase3_3_finished_at = utc_now_iso()
    print(f"FINISHED PHASE 3.3 FINAL RELEASE NOTE COMPOSITION ({elapsed_sec(stage_started_perf_phase3_3):.1f}s).", flush=True)
    pipeline_finished_at = utc_now_iso()
    pipeline_duration_sec = elapsed_sec(pipeline_started_perf) or 0.0
    report_json_path, overview_md_path, output_index_md_path = _pipeline_report_paths(pipeline_dir)

    result = ArcRNPipelineResult(
        generated_at=utc_now_iso(),
        repo_name=repo_name,
        base_ref=config.base_ref,
        new_ref=config.new_ref,
        output_dir=str(output_dir),
        started_at=pipeline_started_at,
        finished_at=pipeline_finished_at,
        duration_sec=pipeline_duration_sec,
        stages=stages
        + [
            ArcRNPipelineStageRecord(
                stage_name="phase1_change_evidence_modeling",
                started_at=phase1_started_at,
                finished_at=phase1_finished_at,
                duration_sec=duration_between_iso(phase1_started_at, phase1_finished_at),
                output_files=phase1_result.output_files,
                stats=phase1_result.stats,
            ),
            ArcRNPipelineStageRecord(
                stage_name="phase2_architecture_signal_attribution",
                started_at=phase2_started_at,
                finished_at=phase2_finished_at,
                duration_sec=duration_between_iso(phase2_started_at, phase2_finished_at),
                output_files=phase2_result.output_files,
                stats=phase2_result.stats,
            ),
            ArcRNPipelineStageRecord(
                stage_name="phase3_1_llm_aggregation_planning",
                started_at=phase3_1_started_at,
                finished_at=phase3_1_finished_at,
                duration_sec=duration_between_iso(phase3_1_started_at, phase3_1_finished_at),
                output_files=aggregation_plan_result.output_files,
                stats=aggregation_plan_result.stats,
            ),
            ArcRNPipelineStageRecord(
                stage_name="phase3_2_slot_level_entry_generation",
                started_at=stage_started_at_phase3_2,
                finished_at=phase3_2_finished_at,
                duration_sec=duration_between_iso(stage_started_at_phase3_2, phase3_2_finished_at),
                output_files=section_entries_result.output_files,
                stats=section_entries_result.stats,
            ),
            ArcRNPipelineStageRecord(
                stage_name="phase3_2_5_architecture_label_decision",
                started_at=section_entries_result.stats.get("phase3_2_5_started_at"),
                finished_at=section_entries_result.stats.get("phase3_2_5_finished_at"),
                duration_sec=section_entries_result.stats.get("phase3_2_5_duration_sec"),
                output_files={
                    key: value
                    for key, value in section_entries_result.output_files.items()
                    if "arch_label" in key
                },
                stats={
                    "arch_label_llm_used_slot_count": section_entries_result.stats.get("arch_label_llm_used_slot_count", 0),
                    "architecture_labeled_entry_count": section_entries_result.stats.get("architecture_labeled_entry_count", 0),
                },
            ),
            ArcRNPipelineStageRecord(
                stage_name="phase3_3_document_level_composition",
                started_at=stage_started_at_phase3_3,
                finished_at=phase3_3_finished_at,
                duration_sec=duration_between_iso(stage_started_at_phase3_3, phase3_3_finished_at),
                output_files=final_note_result.output_files,
                stats=final_note_result.stats,
            ),
        ],
        final_outputs={
            **phase1_result.output_files,
            **phase2_result.output_files,
            **aggregation_plan_result.output_files,
            **section_entries_result.output_files,
            **final_note_result.output_files,
            "archlog_pipeline_report_json": str(report_json_path),
            "archlog_pipeline_overview_markdown": str(overview_md_path),
            "archlog_outputs_index_markdown": str(output_index_md_path),
        },
    )

    metrics_outputs = write_experiment_metrics(
        output_dir=output_dir,
        config=config,
        pipeline_result=result,
        started_at=pipeline_started_at,
        finished_at=pipeline_finished_at,
        duration_sec=pipeline_duration_sec,
    )
    result.final_outputs.update(
        {
            "experiment_metrics_json": metrics_outputs["experiment_metrics"],
            "llm_call_metrics_jsonl": metrics_outputs["llm_call_metrics_jsonl"],
        }
    )
    _save_pipeline_report(result, pipeline_dir)
    return result


def run_archlog_pipeline(config, *, include_code_changes: bool = True) -> ArcRNPipelineResult:
    return run_arcrn_pipeline(config, include_code_changes=include_code_changes)


def _build_semarc_paths(*, config, repo_name: str, base_ref: str, new_ref: str) -> Dict[str, Path]:
    return {
        "archsem_old": _semarc_result_path(config=config, repo_name=repo_name, ref=base_ref, suffix="ArchSem"),
        "codesem_old": _semarc_result_path(config=config, repo_name=repo_name, ref=base_ref, suffix="CodeSem"),
        "namedclusters_old": _semarc_result_path(config=config, repo_name=repo_name, ref=base_ref, suffix="NamedClusters"),
        "clustercomponent_old": _semarc_result_path(config=config, repo_name=repo_name, ref=base_ref, suffix="ClusterComponent"),
        "archsem_new": _semarc_result_path(config=config, repo_name=repo_name, ref=new_ref, suffix="ArchSem"),
        "codesem_new": _semarc_result_path(config=config, repo_name=repo_name, ref=new_ref, suffix="CodeSem"),
        "namedclusters_new": _semarc_result_path(config=config, repo_name=repo_name, ref=new_ref, suffix="NamedClusters"),
        "clustercomponent_new": _semarc_result_path(config=config, repo_name=repo_name, ref=new_ref, suffix="ClusterComponent"),
    }


def _semarc_result_path(*, config, repo_name: str, ref: str, suffix: str) -> Path:
    configured_root = Path(getattr(config, "semarc_output_dir", "") or "outputs/external_artifacts/semarc_results")
    roots = [configured_root, Path("outputs/external_artifacts/semarc_results"), Path("arch_changes-reports/sema_results")]
    seen = set()
    for root in roots:
        directory = root / f"{repo_name}-{ref}"
        for candidate in (
            directory / f"{repo_name}-{ref}_{suffix}.json",
            directory / f"{repo_name}_{ref}_{suffix}.json",
        ):
            key = str(candidate)
            if key in seen:
                continue
            seen.add(key)
            if candidate.exists():
                return candidate
    return roots[0] / f"{repo_name}-{ref}" / f"{repo_name}-{ref}_{suffix}.json"


def _find_latest_diff_ir(*, config, repo_name: str, base_ref: str, new_ref: str) -> Path:
    pattern = f"{repo_name}_{base_ref}-{new_ref}-*"
    out_roots = [
        Path("outputs/external_artifacts/arch_diff"),
        Path("arch_changes-reports/out"),
    ]
    seen = set()
    for out_root in out_roots:
        key = str(out_root)
        if key in seen:
            continue
        seen.add(key)
        candidates = sorted(
            out_root.glob(pattern),
            key=lambda path: path.name,
            reverse=True,
        )

        for directory in candidates:
            candidate_path = directory / "diff_ir-denoised-significance.json"
            if candidate_path.exists():
                return candidate_path

    raise FileNotFoundError(
        f"Could not find diff_ir-denoised-significance.json for {repo_name} {base_ref}->{new_ref} under outputs/external_artifacts/arch_diff or arch_changes-reports/out"
    )

def _save_pipeline_report(result: ArcRNPipelineResult, output_dir: Path) -> Tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    report_json_path, overview_md_path, output_index_md_path = _pipeline_report_paths(output_dir)

    with report_json_path.open("w", encoding="utf-8") as handle:
        json.dump(result.to_dict(), handle, ensure_ascii=False, indent=2)
    overview_md_path.write_text(_render_pipeline_overview(result), encoding="utf-8")
    output_index_md_path.write_text(_render_output_index(result), encoding="utf-8")

    return report_json_path, overview_md_path


def _pipeline_report_paths(output_dir: Path) -> Tuple[Path, Path, Path]:
    return (
        output_dir / "archlog_pipeline_report.json",
        output_dir / "archlog_pipeline_overview.md",
        output_dir / "outputs_index.md",
    )


def _render_pipeline_overview(result: ArcRNPipelineResult) -> str:
    lines = [
        "# ArchLog Pipeline Overview",
        "",
        f"- Repository: `{result.repo_name}`",
        f"- Version range: `{result.base_ref} -> {result.new_ref}`",
        f"- Output dir: `{result.output_dir}`",
        "",
        "## Stages",
        "",
    ]

    for stage in result.stages:
        lines.append(f"### {stage.stage_name}")
        lines.append("")
        if stage.duration_sec is not None:
            lines.append(f"- duration_sec: `{stage.duration_sec}`")
        if stage.stats:
            for key, value in sorted(stage.stats.items()):
                lines.append(f"- {key}: `{value}`")
        else:
            lines.append("- stats: `(none)`")
        if stage.output_files:
            for key, value in sorted(stage.output_files.items()):
                lines.append(f"- {key}: `{value}`")
        else:
            lines.append("- output_files: `(none)`")
        lines.append("")

    lines.append("## Final Outputs")
    lines.append("")
    for key, value in sorted(result.final_outputs.items()):
        lines.append(f"- {key}: `{value}`")
    lines.append("")

    return "\n".join(lines)


def _render_output_index(result: ArcRNPipelineResult) -> str:
    lines = [
        "# ArchLog Outputs Index",
        "",
        f"- Output root: `{result.output_dir}`",
        "",
        "## Folder Map",
        "",
        "- `00_pipeline_summary/`: whole-pipeline reports and this output index.",
        "- `01_code_changes/`: code_changes 10-step subpipeline outputs, including Step 1-10 compatibility JSON files.",
        "- `02_phase1_change_evidence/`: normalized change evidence and legacy `change_ir` files.",
        "- `03_phase2_arch_signal_attribution/`: architecture-event attribution, evidence matrix, posterior matrix, and debug payloads.",
        "- `04_phase3_1_llm_aggregation_planning/`: LLM multi-stage aggregation plan and Phase 3.1 intermediate decisions.",
        "- `05_phase3_2_slot_entry_generation/`: release-note slot entries generated from aggregation groups.",
        "- `06_phase3_3_final_composition/`: final release note markdown/json and composition audit.",
        "",
        "## Stage Files",
        "",
    ]

    for stage in result.stages:
        lines.append(f"### {stage.stage_name}")
        lines.append("")
        if not stage.output_files:
            lines.append("- (no files)")
        else:
            for key, value in sorted(stage.output_files.items()):
                lines.append(f"- `{key}`: `{value}`")
        lines.append("")

    return "\n".join(lines)
