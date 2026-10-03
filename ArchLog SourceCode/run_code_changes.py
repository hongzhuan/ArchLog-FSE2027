from __future__ import annotations

import json
import time
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any, Dict, List

from arcrn_llm_io_exporter import export_code_change_llm_io
from arcrn_output_layout import llm_io_dir, stage_output_dir
from config import build_config
from code_changes.pipeline import run_code_change_pipeline


@dataclass
class CodeChangesSubpipelineResult:
    pipeline_result: Any
    output_files: Dict[str, str] = field(default_factory=dict)


def main() -> None:
    config = build_config()
    config.validate()

    print("=" * 100)
    print("RUN CODE CHANGES START")
    print("=" * 100)
    print(f"Repository: {config.repo_path}")
    print(f"Version range: {config.base_ref} -> {config.new_ref}")
    print(f"ENRE JSON: {config.enre_json_path}")
    print(f"Output dir: {stage_output_dir(Path(config.output_dir), 'code_changes')}")
    print(f"LLM model: {config.llm_model_name}")
    print(f"Step10 concurrency: {config.step10_concurrency}")
    print(f"Step10 rate limit qps: {config.step10_rate_limit_qps}")
    print(f"Step10 retry attempts: {config.step10_retry_max_attempts}")
    print("=" * 100)

    subpipeline_result = run_code_changes_subpipeline(config)
    result = subpipeline_result.pipeline_result

    print("\n" + "=" * 100)
    print("RUN SUMMARY")
    print("=" * 100)
    _print_run_summary(result)

    print("\nOutputs saved to:")
    print(config.output_dir.resolve())

    print("\n" + "=" * 100)
    print("RUN CODE CHANGES FINISHED")
    print("=" * 100)


def run_code_changes_subpipeline(config) -> CodeChangesSubpipelineResult:
    config.validate()

    output_root = Path(config.output_dir)
    code_changes_dir = stage_output_dir(output_root, "code_changes")
    run_config = replace(config, output_dir=code_changes_dir)
    result = run_code_change_pipeline(run_config)

    print("\n" + "=" * 100)
    print("SAVING COMPATIBILITY OUTPUTS")
    print("=" * 100)
    output_files = _save_compatibility_outputs(result)

    return CodeChangesSubpipelineResult(
        pipeline_result=result,
        output_files=output_files,
    )


def _save_compatibility_outputs(result) -> Dict[str, str]:
    compatibility_started = time.perf_counter()
    output_dir = result.config.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    saved_files: Dict[str, str] = {}
    compatibility_files = [
        ("step1_changed_methods.json", result.artifacts.changed_methods),
        ("step2_methods_with_commits.json", result.artifacts.changed_methods_with_commits),
        ("step3_methods_with_enre.json", result.artifacts.changed_methods_with_enre),
        ("step4_method_context_graphs.json", result.artifacts.method_context_graphs),
        ("step5_diff_hunks.json", result.artifacts.diff_hunks),
        ("step6_method_hunk_pairs.json", result.artifacts.method_hunk_pairs),
        ("step7_change_units.json", result.artifacts.change_units),
        ("step8_prompts.json", result.artifacts.llm_prompts),
        ("step9_selected_exemplars.json", result.artifacts.selected_exemplars),
        ("step10_summaries.json", result.artifacts.code_change_summaries),
    ]
    compatibility_items = [(filename, artifact) for filename, artifact in compatibility_files if artifact is not None]
    print(f"Compatibility JSON outputs: {len(compatibility_items)} files.", flush=True)

    for index, (filename, artifact) in enumerate(compatibility_items, start=1):
        if artifact is None:
            continue
        target_path = output_dir / filename
        item_started = time.perf_counter()
        print(f"[compat {index}/{len(compatibility_items)}] Writing {filename} ...", flush=True)
        serialize_started = time.perf_counter()
        payload = artifact.to_dict()
        serialize_sec = time.perf_counter() - serialize_started
        _save_json(target_path, payload)
        del payload
        saved_files[filename] = str(target_path)
        print(
            f"[compat {index}/{len(compatibility_items)}] Finished {filename} "
            f"({_format_file_size(target_path)}, {time.perf_counter() - item_started:.1f}s, "
            f"to_dict={serialize_sec:.1f}s).",
            flush=True,
        )

    summaries_path = output_dir / "code_change_summaries.md"
    overview_path = output_dir / "run_overview.txt"
    print("[compat text] Writing code_change_summaries.md ...", flush=True)
    text_started = time.perf_counter()
    _save_text(summaries_path, _render_summaries_markdown(result))
    print(
        f"[compat text] Finished code_change_summaries.md "
        f"({_format_file_size(summaries_path)}, {time.perf_counter() - text_started:.1f}s).",
        flush=True,
    )
    print("[compat text] Writing run_overview.txt ...", flush=True)
    text_started = time.perf_counter()
    _save_text(overview_path, _render_run_overview(result))
    print(
        f"[compat text] Finished run_overview.txt "
        f"({_format_file_size(overview_path)}, {time.perf_counter() - text_started:.1f}s).",
        flush=True,
    )
    saved_files["code_change_summaries.md"] = str(summaries_path)
    saved_files["run_overview.txt"] = str(overview_path)
    print("[compat llm_io] Exporting Step10 LLM input/output text ...", flush=True)
    llm_io_started = time.perf_counter()
    llm_io_path = export_code_change_llm_io(result, llm_io_dir(output_dir))
    if llm_io_path:
        saved_files["step10_llm_input_output_txt"] = llm_io_path
        print(
            f"[compat llm_io] Finished Step10 LLM input/output text "
            f"({_format_file_size(Path(llm_io_path))}, {time.perf_counter() - llm_io_started:.1f}s).",
            flush=True,
        )
    else:
        print(f"[compat llm_io] No Step10 LLM input/output text exported ({time.perf_counter() - llm_io_started:.1f}s).", flush=True)

    print(
        f"Compatibility outputs saved: {len(saved_files)} files in {time.perf_counter() - compatibility_started:.1f}s.",
        flush=True,
    )

    return saved_files


def _print_run_summary(result) -> None:
    stats = result.report.final_stats or {}
    summaries = result.final_summaries()

    print(f"Changed methods: {stats.get('changed_methods_count', 0)}")
    print(f"Matched ENRE methods: {stats.get('methods_with_enre_match_count', 0)}")
    print(f"Context graphs: {stats.get('method_context_graphs_count', 0)}")
    print(f"Diff hunks: {stats.get('diff_hunks_count', 0)}")
    print(f"Method-hunk pairs: {stats.get('method_hunk_pairs_count', 0)}")
    print(f"Change units: {stats.get('change_units_count', 0)}")
    print(f"Prompt records: {stats.get('prompts_count', 0)}")
    print(f"Exemplar sets: {stats.get('selected_exemplar_sets_count', 0)}")
    print(f"Summaries: {stats.get('summaries_count', 0)}")

    print("\nExecuted steps:")
    for record in result.report.executed_steps:
        status = "OK" if record.success else "FAILED"
        print(f"- {record.step_name}: {status}")

    print("\nTop summaries:")
    if not summaries:
        print("(none)")
        return

    for idx, item in enumerate(summaries[:10], start=1):
        print(f"{idx:02d}. [{item.predicted_category}] {item.summary}")


def _save_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _save_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _format_file_size(path: Path) -> str:
    try:
        size = path.stat().st_size
    except OSError:
        return "unknown size"
    units = ["B", "KB", "MB", "GB", "TB"]
    value = float(size)
    for unit in units:
        if value < 1024.0 or unit == units[-1]:
            if unit == "B":
                return f"{int(value)} {unit}"
            return f"{value:.1f} {unit}"
        value /= 1024.0


def _render_summaries_markdown(result) -> str:
    lines: List[str] = []
    lines.append("# Code Change Summaries")
    lines.append("")

    summaries = result.final_summaries()
    if not summaries:
        lines.append("(none)")
        return "\n".join(lines)

    for item in summaries:
        lines.append(f"## {item.unit_id}")
        lines.append("")
        lines.append(f"- Commit: `{item.commit_id}`")
        lines.append(f"- Category: `{item.predicted_category}`")
        lines.append(f"- Used Exemplars: {item.used_exemplar_ids if item.used_exemplar_ids else '[]'}")
        lines.append(f"- Summary: {item.summary}")
        lines.append("")

    return "\n".join(lines)


def _render_run_overview(result) -> str:
    config = result.config
    stats = result.report.final_stats or {}
    summaries = result.final_summaries()

    lines: List[str] = []
    lines.append("ArchLog Run Overview")
    lines.append("=" * 80)
    lines.append(f"Repository: {config.repo_path}")
    lines.append(f"Version range: {config.base_ref} -> {config.new_ref}")
    lines.append(f"ENRE JSON: {config.enre_json_path}")
    lines.append(f"Output dir: {config.output_dir}")
    lines.append(f"LLM model: {config.llm_model_name}")
    lines.append("")
    lines.append(f"Changed methods: {stats.get('changed_methods_count', 0)}")
    lines.append(f"Matched ENRE methods: {stats.get('methods_with_enre_match_count', 0)}")
    lines.append(f"Context graphs: {stats.get('method_context_graphs_count', 0)}")
    lines.append(f"Diff hunks: {stats.get('diff_hunks_count', 0)}")
    lines.append(f"Method-hunk pairs: {stats.get('method_hunk_pairs_count', 0)}")
    lines.append(f"Change units: {stats.get('change_units_count', 0)}")
    lines.append(f"Prompt records: {stats.get('prompts_count', 0)}")
    lines.append(f"Exemplar sets: {stats.get('selected_exemplar_sets_count', 0)}")
    lines.append(f"Summaries: {stats.get('summaries_count', 0)}")
    lines.append("")

    lines.append("Executed steps:")
    for record in result.report.executed_steps:
        status = "OK" if record.success else "FAILED"
        output_file = record.output_file or "(not saved)"
        lines.append(f"- {record.step_name}: {status} -> {output_file}")

    lines.append("")
    lines.append("Summary Preview:")
    if not summaries:
        lines.append("(none)")
    else:
        for idx, item in enumerate(summaries[:10], start=1):
            lines.append(f"{idx:02d}. [{item.predicted_category}] {item.summary}")

    return "\n".join(lines)


if __name__ == "__main__":
    main()
