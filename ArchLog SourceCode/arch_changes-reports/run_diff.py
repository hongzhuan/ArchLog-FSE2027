"""ArchLog runtime helper."""

from __future__ import annotations

import os
import json
import copy
import sys
import argparse
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config import LLM_API_KEY_ENV_VAR, LLM_MODEL_NAME  # noqa: E402
from llm.summarize_changes import summarize_ir_changes
from llm.render_md import render_markdown_template, render_markdown_llm

from sema_diff.config import DiffConfig, default_config
from sema_diff.loader import resolve_inputs_from_dirs, ResolvedInputs

from sema_diff.parse_namedclusters import parse_namedclusters, NamedClustersIndex
from sema_diff.parse_clustercomponent import parse_clustercomponent, ComponentMapping

from sema_diff.a2a_jaccard import build_module_files, align_modules_by_jaccard
from sema_diff.module_diff_core import build_module_level_events

from sema_diff.quality import build_quality_report
from sema_diff.diff_core import build_snapshot, diff_file_universe  #
from sema_diff.ir import DiffIR, now_iso_local, dump_ir

from sema_diff.parse_codesem import parse_codesem, CodeSemIndex
from sema_diff.parse_archsem import parse_archsem, ArchSemIndex

from sema_diff.denoise import denoise_changes
from sema_diff.significance import compute_architecture_significance

def _ensure_out_dir(out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)


def run_diff(
    *,
    dir_a: Path,
    dir_b: Path,
    version_a_label: str,
    version_b_label: str,
    repo_name: str,
    use_llm: bool = True,
    output_root: Path | None = None,
) -> Path:
    timestamp = datetime.now().astimezone().strftime("%Y%m%dT%H%M%S")

    min_edge_weight = 0.0          #
    min_file_delta = 2             #
    top_k_files = 8                #
    min_jaccard_to_accept = 0.0    #

    generate_md = True
    md_mode = "llm" if use_llm else "template"
    llm_model = LLM_MODEL_NAME

    resolved_output_root = Path(output_root) if output_root is not None else Path(os.getcwd()) / "out"
    out_dir = resolved_output_root / f"{repo_name}_{version_a_label}-{version_b_label}-{timestamp}"
    _ensure_out_dir(out_dir)

    cfg: DiffConfig = default_config()

    resolved: ResolvedInputs = resolve_inputs_from_dirs(dir_a=dir_a, dir_b=dir_b)

    a_named_path = resolved.version_a_files["NamedClusters"]
    a_comp_path = resolved.version_a_files["ClusterComponent"]
    b_named_path = resolved.version_b_files["NamedClusters"]
    b_comp_path = resolved.version_b_files["ClusterComponent"]

    a_arch_path = resolved.version_a_files.get("ArchSem")
    a_code_path = resolved.version_a_files.get("CodeSem")
    b_arch_path = resolved.version_b_files.get("ArchSem")
    b_code_path = resolved.version_b_files.get("CodeSem")

    print("=== Inputs ===")
    print("A NamedClusters:", a_named_path)
    print("A ClusterComponent:", a_comp_path)
    print("B NamedClusters:", b_named_path)
    print("B ClusterComponent:", b_comp_path)

    # 2) parse
    idx_a: NamedClustersIndex = parse_namedclusters(a_named_path, cfg)
    idx_b: NamedClustersIndex = parse_namedclusters(b_named_path, cfg)

    comp_a: ComponentMapping = parse_clustercomponent(a_comp_path, idx_a.name_to_uids_queue, cfg)
    comp_b: ComponentMapping = parse_clustercomponent(b_comp_path, idx_b.name_to_uids_queue, cfg)

    codesem_a = parse_codesem(a_code_path) if a_code_path and a_code_path.exists() else None
    codesem_b = parse_codesem(b_code_path) if b_code_path and b_code_path.exists() else None

    archsem_a = parse_archsem(a_arch_path) if a_arch_path and a_arch_path.exists() else None
    archsem_b = parse_archsem(b_arch_path) if b_arch_path and b_arch_path.exists() else None

    # 3) a2a_jaccard alignment (module mapping)
    modules_a = build_module_files(idx_a)
    modules_b = build_module_files(idx_b)

    alignment = align_modules_by_jaccard(
        modules_a,
        modules_b,
        min_edge_weight=min_edge_weight,
        engine="auto",
    )

    print("\n=== A2A Mapping Summary ===")
    print("engine:", alignment.meta.get("engine"))
    print("global_similarity:", alignment.global_similarity)
    print("mapped:", len(alignment.mapping), "removed(A-only):", len(alignment.removed), "added(B-only):", len(alignment.added))

    # 4) module-level events
    events = []
    next_id = 1

    mod_events, next_id = build_module_level_events(
        idx_a=idx_a,
        idx_b=idx_b,
        comp_a=comp_a,
        comp_b=comp_b,
        alignment=alignment,
        next_id_start=next_id,
        top_k_files=top_k_files,
        min_file_delta=min_file_delta,
        min_jaccard_to_accept=min_jaccard_to_accept,
        codesem_a=codesem_a,
        codesem_b=codesem_b,
        archsem_a=archsem_a,
        archsem_b=archsem_b,
    )

    events.extend(mod_events)

    snap_a = build_snapshot(version_a_label, idx_a, comp_a)
    snap_b = build_snapshot(version_b_label, idx_b, comp_b)
    files_added, files_removed, reassigned = diff_file_universe(snap_a, snap_b)

    quality_report, next_id = build_quality_report(
        snap_a,
        snap_b,
        files_added_count=len(files_added),
        files_removed_count=len(files_removed),
        cfg=cfg,
        next_id_start=next_id,
    )
    events.extend(quality_report.warning_events)

    meta = {
        "repo": repo_name,
        "version_a": version_a_label,
        "version_b": version_b_label,
        "generated_at": now_iso_local(),
        "inputs": {
            "named_clusters_a": str(a_named_path),
            "named_clusters_b": str(b_named_path),
            "cluster_component_a": str(a_comp_path),
            "cluster_component_b": str(b_comp_path),
        },
        "a2a": {
            "engine": alignment.meta.get("engine"),
            "global_similarity": alignment.global_similarity,
            "min_edge_weight": min_edge_weight,
        },
        "module_diff": {
            "min_file_delta": min_file_delta,
            "top_k_files": top_k_files,
            "min_jaccard_to_accept": min_jaccard_to_accept,
        },
        "semantics": {
            "codesem_a_loaded": bool(codesem_a),
            "codesem_b_loaded": bool(codesem_b),
            "archsem_a_loaded": bool(archsem_a),
            "archsem_b_loaded": bool(archsem_b),
            "codesem_a_size": (len(codesem_a.file_to_desc) if codesem_a else 0),
            "codesem_b_size": (len(codesem_b.file_to_desc) if codesem_b else 0),
            "archsem_a_components": (len(archsem_a.component_to_summary) if archsem_a else 0),
            "archsem_b_components": (len(archsem_b.component_to_summary) if archsem_b else 0),
        },
    }

    quality = {**quality_report.flags, "notes": quality_report.notes}

    entities = {
        "files": {
            "count_a": len(snap_a.files),
            "count_b": len(snap_b.files),
            "added": sorted(files_added),
            "removed": sorted(files_removed),
            "reassigned_count": len(reassigned),
        },
        "modules": {
            "count_a": len(idx_a.modules),
            "count_b": len(idx_b.modules),
            "mapped": len(alignment.mapping),
            "removed": len(alignment.removed),
            "added": len(alignment.added),
        },
        "components": {
            "count_a": len(comp_a.component_to_module_uids),
            "count_b": len(comp_b.component_to_module_uids),
            "unresolved_a": len(comp_a.unresolved),
            "unresolved_b": len(comp_b.unresolved),
        },
    }

    ir = DiffIR(meta=meta, quality=quality, entities=entities, changes=events)

    raw_path = out_dir / "diff_ir-raw.json"
    dump_ir(ir, str(raw_path), pretty=True)
    print(f"\nWrote RAW IR: {raw_path}")
    print(f"RAW total changes: {len(events)}")

    ir_denoised = copy.deepcopy(ir)
    filtered_changes, denoise_stats = denoise_changes(
        changes=ir_denoised.changes,
        named_a=idx_a,
        named_b=idx_b,
        cfg=cfg.denoise,
    )
    ir_denoised.changes = filtered_changes
    ir_denoised.meta["denoise"] = denoise_stats

    denoised_path = out_dir / "diff_ir-denoised.json"
    dump_ir(ir_denoised, str(denoised_path), pretty=True)
    print(f"Wrote DENOISED (no significance) IR: {denoised_path}")
    print(f"DENOISED (no significance) total changes: {len(filtered_changes)} (dropped={denoise_stats.get('dropped')})")

    summary_ir_path = out_dir / "diff_ir-summary.json"
    if use_llm:
        try:
            ir_for_stage1 = json.loads(denoised_path.read_text(encoding="utf-8"))
            summarize_ir_changes(
                ir=ir_for_stage1,
                out_path=summary_ir_path,
                model=llm_model,
                api_key_env=LLM_API_KEY_ENV_VAR,
            )
            print(f"Wrote IR with per-change LLM summaries: {summary_ir_path}")
        except Exception as e:
            print(f"[WARN] Stage-1 summarize failed: {e}")
            summary_ir_path = denoised_path
    else:
        summary_ir_path = denoised_path

    max_files = max(
        entities["files"]["count_a"],
        entities["files"]["count_b"],
    )

    scored = 0
    for ev in ir_denoised.changes:
        ev_type = ev["type"] if isinstance(ev, dict) else getattr(ev, "type", None)
        if ev_type == "quality_warning":
            continue

        if isinstance(ev, dict):
            ev.setdefault("detail", {})
            detail = ev["detail"]
        else:
            if getattr(ev, "detail", None) is None:
                ev.detail = {}
            detail = ev.detail

        ev_for_score = ev if isinstance(ev, dict) else {
            "type": ev_type,
            "detail": detail,
            "confidence": getattr(ev, "confidence", None),
            "id": getattr(ev, "id", None),
            "summary": getattr(ev, "summary", None),
        }

        sig = compute_architecture_significance(
            ev_for_score,
            max_files_in_project=max_files,
        )

        detail["architecture_significance"] = sig
        scored += 1

    ir_denoised.meta.setdefault("significance", {})
    ir_denoised.meta["significance"].update({
        "enabled": True,
        "scored_events": scored,
        "max_files_in_project": max_files,
    })

    denoised_significance_path = out_dir / "diff_ir-denoised-significance.json"
    dump_ir(ir_denoised, str(denoised_significance_path), pretty=True)
    print(f"Wrote DENOISED IR: {denoised_significance_path}")
    print(f"DENOISED total changes: {len(filtered_changes)} (dropped={denoise_stats.get('dropped')})")

    if generate_md:
        ir_dict = json.loads(summary_ir_path.read_text(encoding="utf-8"))

        if md_mode == "template":
            md = render_markdown_template(ir_dict)
        elif md_mode == "llm":
            md = render_markdown_llm(ir_dict, model=llm_model)
        else:
            raise ValueError(f"Unknown md_mode: {md_mode}")

        md_path = out_dir / "diff_summary.md"
        md_path.write_text(md, encoding="utf-8")
        print(f"Wrote Markdown summary: {md_path} (mode={md_mode})")

    print("Done.")
    return denoised_significance_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate ArchLog architecture-diff input from two SemArc result directories.")
    parser.add_argument("--dir-a", type=Path, default=Path(r"sema_results/jsoncpp-1.9.4"))
    parser.add_argument("--dir-b", type=Path, default=Path(r"sema_results/jsoncpp-1.9.5"))
    parser.add_argument("--version-a", default="1.9.4")
    parser.add_argument("--version-b", default="1.9.5")
    parser.add_argument("--repo-name", default="jsoncpp")
    parser.add_argument("--no-llm", action="store_true", help="Generate IR and a template markdown summary without LLM calls.")
    parser.add_argument("--output-root", type=Path, default=None, help="Directory where timestamped architecture diff outputs are written.")
    args = parser.parse_args()
    run_diff(
        dir_a=args.dir_a,
        dir_b=args.dir_b,
        version_a_label=args.version_a,
        version_b_label=args.version_b,
        repo_name=args.repo_name,
        use_llm=not args.no_llm,
        output_root=args.output_root,
    )


if __name__ == "__main__":
    main()
