from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from .models import CommitArchMapping, CommitArchMappingOutput, utc_now_iso
from .stage2_arch_classifier import classify_commit_arch
from .stage2_exporter import export_stage2_outputs
from .stage2_input_loader import load_stage2_inputs
from .stage2_module_mapper import map_commit_to_modules


def run_stage2_arch_mapping(
    *,
    change_ir_path: Path,
    diff_ir_path: Path,
    namedclusters_new_path: Path,
    clustercomponent_new_path: Path,
    output_dir: Path,
    namedclusters_old_path: Optional[Path] = None,
    clustercomponent_old_path: Optional[Path] = None,
) -> CommitArchMappingOutput:
    loaded_inputs = load_stage2_inputs(
        change_ir_path=change_ir_path,
        diff_ir_path=diff_ir_path,
        namedclusters_new_path=namedclusters_new_path,
        clustercomponent_new_path=clustercomponent_new_path,
        namedclusters_old_path=namedclusters_old_path,
        clustercomponent_old_path=clustercomponent_old_path,
    )

    mappings: List[CommitArchMapping] = []
    for commit_record in loaded_inputs.change_ir.get("commits") or []:
        mapping_result = map_commit_to_modules(
            commit_record,
            named_new=loaded_inputs.named_new,
            named_old=loaded_inputs.named_old,
            comp_new=loaded_inputs.comp_new,
            comp_old=loaded_inputs.comp_old,
        )
        classification_result = classify_commit_arch(
            commit_record,
            mapping_result,
            arch_index=loaded_inputs.arch_index,
        )

        mappings.append(
            CommitArchMapping(
                commit_id=str(commit_record.get("commit_id") or ""),
                arch_label=classification_result.arch_label,
                arch_confidence=classification_result.arch_confidence,
                arch_reasons=classification_result.arch_reasons,
                impact_score=classification_result.impact_score,
                primary_module=mapping_result.primary_module,
                primary_module_name=mapping_result.primary_module_name,
                primary_component=mapping_result.primary_component,
                secondary_modules=mapping_result.secondary_modules,
                secondary_module_names=mapping_result.secondary_module_names,
                secondary_components=mapping_result.secondary_components,
                scope=mapping_result.scope,
                changed_files=mapping_result.changed_files,
                matched_arch_change_ids=classification_result.matched_arch_change_ids,
                matched_arch_change_types=classification_result.matched_arch_change_types,
            )
        )

    output = CommitArchMappingOutput(
        generated_at=utc_now_iso(),
        source_change_ir_path=str(change_ir_path),
        source_arch_inputs={
            "diff_ir": str(diff_ir_path),
            "namedclusters_new": str(namedclusters_new_path),
            "clustercomponent_new": str(clustercomponent_new_path),
            "namedclusters_old": str(namedclusters_old_path) if namedclusters_old_path else "",
            "clustercomponent_old": str(clustercomponent_old_path) if clustercomponent_old_path else "",
        },
        mappings=mappings,
        stats=_build_stage2_stats(mappings),
    )

    export_stage2_outputs(output, output_dir)
    return output


def _build_stage2_stats(mappings: List[CommitArchMapping]) -> Dict[str, Any]:
    stats = {
        "mapping_count": len(mappings),
        "a_type_count": sum(1 for item in mappings if item.arch_label == "A-type"),
        "l_type_count": sum(1 for item in mappings if item.arch_label == "L-type"),
        "single_module_count": sum(1 for item in mappings if item.scope == "single-module"),
        "cross_module_count": sum(1 for item in mappings if item.scope == "cross-module"),
        "global_count": sum(1 for item in mappings if item.scope == "global"),
        "supporting_count": sum(1 for item in mappings if item.scope == "supporting"),
        "matched_arch_change_count": sum(1 for item in mappings if item.matched_arch_change_ids),
    }
    return stats
