from __future__ import annotations

import importlib
import json
import logging
from dataclasses import asdict
from pathlib import Path
from typing import Any, Callable, Dict, Optional, Tuple

from .constants import (
    DEFAULT_LOGGER_NAME,
    FILE_PIPELINE_REPORT,
    INTERMEDIATE_OUTPUT_FILES,
    JSON_INDENT,
    PIPELINE_STEP_SEQUENCE,
    STEP10_CODE_CHANGE_SUMMARIZER,
    STEP1_METHOD_CHANGE_LOCALIZER,
    STEP2_COMMIT_MAPPER,
    STEP3_ENRE_ENTITY_MATCHER,
    STEP4_CALL_SUBGRAPH_BUILDER,
    STEP5_DIFF_HUNK_EXTRACTOR,
    STEP6_HUNK_METHOD_ALIGNER,
    STEP7_CHANGE_UNIT_BUILDER,
    STEP8_PROMPT_BUILDER,
    STEP9_EXEMPLAR_SELECTOR,
    UTF8,
)
from .models import (
    ChangeUnitsOutput,
    ChangedMethodsOutput,
    CommitsMappedOutput,
    DiffHunksOutput,
    EnreMatchedOutput,
    MethodContextGraphsOutput,
    MethodHunkPairsOutput,
    PipelineArtifacts,
    PipelineConfig,
    PipelineReport,
    PipelineResult,
    PromptsOutput,
    SelectedExemplarsOutput,
    StepExecutionRecord,
    SummariesOutput,
    utc_now_iso,
)
from arcrn_metrics import duration_between_iso


LOGGER = logging.getLogger(DEFAULT_LOGGER_NAME)


# ============================================================
# Public API
# ============================================================

def run_code_change_pipeline(config: PipelineConfig) -> PipelineResult:
    """
    Orchestrate the complete ArchLog code-changes pipeline.

    Pipeline order:
      1. locate changed methods with tree-sitter / AST
      2. map changed methods to commits
      3. match changed methods to ENRE entities (new version)
      4. build method context graphs from ENRE relations
      5. extract diff hunks from `git log -p base..new`
      6. align hunks to changed methods
      7. build change units (commit = unit)
      8. build LLM prompts
      9. select exemplars
      10. call LLM and generate code-change summaries
    """
    config.validate()
    _prepare_output_dir(config.output_dir)

    if config.verbose:
        _configure_default_logging()

    report = PipelineReport(
        pipeline_name=config.pipeline_name,
        started_at=utc_now_iso(),
        config=config.to_dict(),
    )
    artifacts = PipelineArtifacts()

    try:
        # ----------------------------------------------------
        # Step 1
        # ----------------------------------------------------
        step_record = _start_step(STEP1_METHOD_CHANGE_LOCALIZER, report)
        changed_methods_output = _run_step(
            module_name=".step1_method_change_localizer",
            function_name="run_method_change_localizer",
            kwargs={"config": config},
        )
        _ensure_type(changed_methods_output, ChangedMethodsOutput, STEP1_METHOD_CHANGE_LOCALIZER)
        artifacts.changed_methods = changed_methods_output
        _persist_step_output(
            config=config,
            logical_name="changed_methods",
            data=changed_methods_output.to_dict(),
            step_record=step_record,
            stats={"changed_methods_count": len(changed_methods_output.changed_methods)},
        )

        # ----------------------------------------------------
        # Step 2
        # ----------------------------------------------------
        step_record = _start_step(STEP2_COMMIT_MAPPER, report)
        commits_mapped_output = _run_step(
            module_name=".step2_commit_mapper",
            function_name="run_commit_mapper",
            kwargs={
                "config": config,
                "changed_methods_output": artifacts.changed_methods,
            },
        )
        _ensure_type(commits_mapped_output, CommitsMappedOutput, STEP2_COMMIT_MAPPER)
        artifacts.changed_methods_with_commits = commits_mapped_output
        _persist_step_output(
            config=config,
            logical_name="changed_methods_with_commits",
            data=commits_mapped_output.to_dict(),
            step_record=step_record,
            stats={
                "changed_methods_count": len(commits_mapped_output.changed_methods),
                "methods_with_commits_count": sum(1 for m in commits_mapped_output.changed_methods if m.commits),
            },
        )

        # ----------------------------------------------------
        # Step 3
        # ----------------------------------------------------
        step_record = _start_step(STEP3_ENRE_ENTITY_MATCHER, report)
        enre_matched_output = _run_step(
            module_name=".step3_enre_entity_matcher",
            function_name="run_enre_entity_matcher",
            kwargs={
                "config": config,
                "commits_mapped_output": artifacts.changed_methods_with_commits,
            },
        )
        _ensure_type(enre_matched_output, EnreMatchedOutput, STEP3_ENRE_ENTITY_MATCHER)
        artifacts.changed_methods_with_enre = enre_matched_output
        _persist_step_output(
            config=config,
            logical_name="changed_methods_with_enre",
            data=enre_matched_output.to_dict(),
            step_record=step_record,
            stats={
                "changed_methods_count": len(enre_matched_output.changed_methods),
                "matched_enre_count": sum(
                    1 for m in enre_matched_output.changed_methods if m.enre_entity_id is not None
                ),
                "enre_entities_count": len(enre_matched_output.entities),
                "enre_relations_count": len(enre_matched_output.relations),
            },
        )

        # ----------------------------------------------------
        # Step 4
        # ----------------------------------------------------
        step_record = _start_step(STEP4_CALL_SUBGRAPH_BUILDER, report)
        method_context_graphs_output = _run_step(
            module_name=".step4_call_subgraph_builder",
            function_name="run_call_subgraph_builder",
            kwargs={
                "config": config,
                "enre_matched_output": artifacts.changed_methods_with_enre,
            },
        )
        _ensure_type(method_context_graphs_output, MethodContextGraphsOutput, STEP4_CALL_SUBGRAPH_BUILDER)
        artifacts.method_context_graphs = method_context_graphs_output
        _persist_step_output(
            config=config,
            logical_name="method_context_graphs",
            data=method_context_graphs_output.to_dict(),
            step_record=step_record,
            stats={"graphs_count": len(method_context_graphs_output.graphs)},
        )

        # ----------------------------------------------------
        # Step 5
        # ----------------------------------------------------
        step_record = _start_step(STEP5_DIFF_HUNK_EXTRACTOR, report)
        diff_hunks_output = _run_step(
            module_name=".step5_diff_hunk_extractor",
            function_name="run_diff_hunk_extractor",
            kwargs={"config": config},
        )
        _ensure_type(diff_hunks_output, DiffHunksOutput, STEP5_DIFF_HUNK_EXTRACTOR)
        artifacts.diff_hunks = diff_hunks_output
        _persist_step_output(
            config=config,
            logical_name="diff_hunks",
            data=diff_hunks_output.to_dict(),
            step_record=step_record,
            stats={
                "diff_hunks_count": len(diff_hunks_output.hunks),
                "file_level_hunks_count": len(diff_hunks_output.file_level_hunks),
            },
        )

        # ----------------------------------------------------
        # Step 6
        # ----------------------------------------------------
        step_record = _start_step(STEP6_HUNK_METHOD_ALIGNER, report)
        method_hunk_pairs_output = _run_step(
            module_name=".step6_hunk_method_aligner",
            function_name="run_hunk_method_aligner",
            kwargs={
                "config": config,
                "commits_mapped_output": artifacts.changed_methods_with_commits,
                "diff_hunks_output": artifacts.diff_hunks,
            },
        )
        _ensure_type(method_hunk_pairs_output, MethodHunkPairsOutput, STEP6_HUNK_METHOD_ALIGNER)
        artifacts.method_hunk_pairs = method_hunk_pairs_output
        _persist_step_output(
            config=config,
            logical_name="method_hunk_pairs",
            data=method_hunk_pairs_output.to_dict(),
            step_record=step_record,
            stats={"method_hunk_pairs_count": len(method_hunk_pairs_output.method_hunk_pairs)},
        )

        # ----------------------------------------------------
        # Step 7
        # ----------------------------------------------------
        step_record = _start_step(STEP7_CHANGE_UNIT_BUILDER, report)
        change_units_output = _run_step(
            module_name=".step7_change_unit_builder",
            function_name="run_change_unit_builder",
            kwargs={
                "config": config,
                "commits_mapped_output": artifacts.changed_methods_with_commits,
                "method_context_graphs_output": artifacts.method_context_graphs,
                "method_hunk_pairs_output": artifacts.method_hunk_pairs,
                "diff_hunks_output": artifacts.diff_hunks,
            },
        )
        _ensure_type(change_units_output, ChangeUnitsOutput, STEP7_CHANGE_UNIT_BUILDER)
        artifacts.change_units = change_units_output
        _persist_step_output(
            config=config,
            logical_name="change_units",
            data=change_units_output.to_dict(),
            step_record=step_record,
            stats={"change_units_count": len(change_units_output.change_units)},
        )

        # ----------------------------------------------------
        # Step 8
        # ----------------------------------------------------
        step_record = _start_step(STEP8_PROMPT_BUILDER, report)
        prompts_output = _run_step(
            module_name=".step8_prompt_builder",
            function_name="run_prompt_builder",
            kwargs={
                "config": config,
                "change_units_output": artifacts.change_units,
            },
        )
        _ensure_type(prompts_output, PromptsOutput, STEP8_PROMPT_BUILDER)
        artifacts.llm_prompts = prompts_output
        _persist_step_output(
            config=config,
            logical_name="llm_prompts",
            data=prompts_output.to_dict(),
            step_record=step_record,
            stats={"prompts_count": len(prompts_output.prompts)},
        )

        # ----------------------------------------------------
        # Step 9
        # ----------------------------------------------------
        step_record = _start_step(STEP9_EXEMPLAR_SELECTOR, report)
        selected_exemplars_output = _run_step(
            module_name=".step9_exemplar_selector",
            function_name="run_exemplar_selector",
            kwargs={
                "config": config,
                "change_units_output": artifacts.change_units,
            },
        )
        _ensure_type(selected_exemplars_output, SelectedExemplarsOutput, STEP9_EXEMPLAR_SELECTOR)
        artifacts.selected_exemplars = selected_exemplars_output
        _persist_step_output(
            config=config,
            logical_name="selected_exemplars",
            data=selected_exemplars_output.to_dict(),
            step_record=step_record,
            stats={"selected_exemplar_sets_count": len(selected_exemplars_output.selected_exemplar_sets)},
        )

        # ----------------------------------------------------
        # Step 10
        # ----------------------------------------------------
        step_record = _start_step(STEP10_CODE_CHANGE_SUMMARIZER, report)
        summaries_output = _run_step(
            module_name=".step10_code_change_summarizer",
            function_name="run_code_change_summarizer",
            kwargs={
                "config": config,
                "change_units_output": artifacts.change_units,
                "prompts_output": artifacts.llm_prompts,
                "selected_exemplars_output": artifacts.selected_exemplars,
            },
        )
        _ensure_type(summaries_output, SummariesOutput, STEP10_CODE_CHANGE_SUMMARIZER)
        artifacts.code_change_summaries = summaries_output
        _persist_step_output(
            config=config,
            logical_name="code_change_summaries",
            data=summaries_output.to_dict(),
            step_record=step_record,
            stats={"summaries_count": len(summaries_output.summaries)},
        )

        report.final_stats = _build_final_stats(artifacts)
        report.finished_at = utc_now_iso()
        report.duration_sec = duration_between_iso(report.started_at, report.finished_at)
        _write_json(config.output_dir / FILE_PIPELINE_REPORT, report.to_dict())

        return PipelineResult(
            config=config,
            report=report,
            artifacts=artifacts,
        )

    except Exception as exc:
        report.finished_at = utc_now_iso()
        report.duration_sec = duration_between_iso(report.started_at, report.finished_at)
        report.final_stats = _build_final_stats(artifacts)
        _write_json(config.output_dir / FILE_PIPELINE_REPORT, report.to_dict())

        if config.fail_fast:
            raise

        LOGGER.exception("Pipeline failed but fail_fast=False. Returning partial result. Error: %s", exc)
        return PipelineResult(
            config=config,
            report=report,
            artifacts=artifacts,
        )


# ============================================================
# Internal step helpers
# ============================================================

def _run_step(module_name: str, function_name: str, kwargs: Dict[str, Any]) -> Any:
    module = importlib.import_module(module_name, package=__package__)
    func = getattr(module, function_name, None)
    if func is None or not callable(func):
        raise AttributeError(
            f"Expected callable '{function_name}' in module '{module_name}', but it was not found."
        )
    return func(**kwargs)


def _ensure_type(value: Any, expected_type: type, step_name: str) -> None:
    if not isinstance(value, expected_type):
        raise TypeError(
            f"{step_name} returned invalid type: expected {expected_type.__name__}, "
            f"got {type(value).__name__}."
        )


def _start_step(step_name: str, report: PipelineReport) -> StepExecutionRecord:
    record = StepExecutionRecord(
        step_name=step_name,
        started_at=utc_now_iso(),
        success=False,
    )
    report.executed_steps.append(record)
    LOGGER.info("Starting %s", step_name)
    return record


def _persist_step_output(
    config: PipelineConfig,
    logical_name: str,
    data: Dict[str, Any],
    step_record: StepExecutionRecord,
    stats: Optional[Dict[str, Any]] = None,
) -> None:
    output_file = None
    if config.save_intermediate:
        filename = INTERMEDIATE_OUTPUT_FILES[logical_name]
        output_path = config.output_dir / filename
        _write_json(output_path, data)
        output_file = str(output_path)

    step_record.finished_at = utc_now_iso()
    step_record.duration_sec = duration_between_iso(step_record.started_at, step_record.finished_at)
    step_record.success = True
    step_record.output_file = output_file
    step_record.stats = stats or {}
    LOGGER.info("Finished %s", step_record.step_name)


# ============================================================
# Reporting
# ============================================================

def _build_final_stats(artifacts: PipelineArtifacts) -> Dict[str, Any]:
    stats: Dict[str, Any] = {}

    if artifacts.changed_methods is not None:
        stats["changed_methods_count"] = len(artifacts.changed_methods.changed_methods)

    if artifacts.changed_methods_with_commits is not None:
        methods = artifacts.changed_methods_with_commits.changed_methods
        stats["methods_with_commits_count"] = sum(1 for m in methods if m.commits)

    if artifacts.changed_methods_with_enre is not None:
        methods = artifacts.changed_methods_with_enre.changed_methods
        stats["methods_with_enre_match_count"] = sum(1 for m in methods if m.enre_entity_id is not None)
        stats["enre_entities_count"] = len(artifacts.changed_methods_with_enre.entities)
        stats["enre_relations_count"] = len(artifacts.changed_methods_with_enre.relations)

    if artifacts.method_context_graphs is not None:
        stats["method_context_graphs_count"] = len(artifacts.method_context_graphs.graphs)

    if artifacts.diff_hunks is not None:
        stats["diff_hunks_count"] = len(artifacts.diff_hunks.hunks)
        stats["file_level_hunks_count"] = len(artifacts.diff_hunks.file_level_hunks)

    if artifacts.method_hunk_pairs is not None:
        stats["method_hunk_pairs_count"] = len(artifacts.method_hunk_pairs.method_hunk_pairs)

    if artifacts.change_units is not None:
        stats["change_units_count"] = len(artifacts.change_units.change_units)

    if artifacts.selected_exemplars is not None:
        stats["selected_exemplar_sets_count"] = len(artifacts.selected_exemplars.selected_exemplar_sets)

    if artifacts.llm_prompts is not None:
        stats["prompts_count"] = len(artifacts.llm_prompts.prompts)

    if artifacts.code_change_summaries is not None:
        stats["summaries_count"] = len(artifacts.code_change_summaries.summaries)

    return stats


# ============================================================
# IO / logging
# ============================================================

def _prepare_output_dir(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)


def _write_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding=UTF8) as f:
        json.dump(data, f, ensure_ascii=False, indent=JSON_INDENT)


def _configure_default_logging() -> None:
    if LOGGER.handlers:
        return
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)s] %(name)s - %(message)s",
    )
