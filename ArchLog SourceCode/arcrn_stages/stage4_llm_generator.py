from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from .llm_utils import (
    TokenBucketRateLimiter,
    generate_chat_completion_with_retry,
    load_prompt_text,
    maybe_build_llm_client,
    parse_json_response,
    render_prompt_template,
    resolve_prompt_path,
    to_pretty_json,
)
from .models import SectionSummariesOutput, SectionSummaryRecord, utc_now_iso
from .stage4_input_loader import Stage4ArchChange, Stage4LoadedInputs


DEFAULT_STAGE4_SYSTEM_PROMPT_PATH = Path(__file__).resolve().parent / "prompts" / "stage4_section_system.txt"
DEFAULT_STAGE4_USER_PROMPT_PATH = Path(__file__).resolve().parent / "prompts" / "stage4_section_user.txt"
MIN_STAGE4_LLM_MAX_TOKENS = 1200


def maybe_generate_stage4_with_llm(
    *,
    config,
    loaded_inputs: Stage4LoadedInputs,
    fallback_output: SectionSummariesOutput,
) -> tuple[SectionSummariesOutput, Dict[str, Any]]:
    llm_client = maybe_build_llm_client(config)
    if llm_client is None:
        return _mark_stage4_fallback_stats(fallback_output), {}

    system_prompt_path = resolve_prompt_path(config, "stage4_system_prompt_path", DEFAULT_STAGE4_SYSTEM_PROMPT_PATH)
    user_prompt_path = resolve_prompt_path(config, "stage4_user_prompt_path", DEFAULT_STAGE4_USER_PROMPT_PATH)
    system_prompt = load_prompt_text(system_prompt_path)
    user_template = load_prompt_text(user_prompt_path)

    rate_limiter = TokenBucketRateLimiter(
        qps=getattr(config, "step10_rate_limit_qps", None),
        burst=int(getattr(config, "step10_rate_limit_burst", 1)),
    )

    commit_lookup = _build_commit_lookup(loaded_inputs.change_ir)
    mapping_lookup = _build_mapping_lookup(loaded_inputs.mapping_output)
    arch_lookup = {item.change_id: item for item in loaded_inputs.arch_changes}
    fallback_lookup = {item.section_id: item for item in fallback_output.summaries}

    generated_summaries: List[SectionSummaryRecord] = []
    prompt_records: List[Dict[str, Any]] = []
    response_records: List[Dict[str, Any]] = []
    llm_generated_count = 0
    fallback_count = 0

    for section in loaded_inputs.release_plan.get("sections") or []:
        section_id = str(section.get("section_id") or "")
        fallback_record = fallback_lookup.get(section_id)
        if fallback_record is None:
            continue

        prompt_payload = _build_section_prompt_payload(
            config=config,
            section=section,
            commit_lookup=commit_lookup,
            mapping_lookup=mapping_lookup,
            arch_lookup=arch_lookup,
        )
        user_prompt = render_prompt_template(user_template, prompt_payload)

        raw_response: Optional[str] = None
        parsed_response: Dict[str, Any] = {}
        error_message: Optional[str] = None
        used_fallback = False

        try:
            raw_response, _ = generate_chat_completion_with_retry(
                config=config,
                llm_client=llm_client,
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                request_name=f"stage4:{section_id}",
                rate_limiter=rate_limiter,
                max_tokens=max(MIN_STAGE4_LLM_MAX_TOKENS, int(getattr(config, "llm_max_tokens", 0) or 0)),
            )
            parsed_response = parse_json_response(raw_response)
            generated_summaries.append(_merge_llm_section_record(fallback_record, parsed_response))
            llm_generated_count += 1
        except Exception as exc:
            generated_summaries.append(fallback_record)
            used_fallback = True
            fallback_count += 1
            error_message = str(exc)

        prompt_records.append(
            {
                "section_id": section_id,
                "system_prompt_path": str(system_prompt_path),
                "user_prompt_path": str(user_prompt_path),
                "system_prompt": system_prompt,
                "user_prompt": user_prompt,
                "prompt_payload": _materialize_prompt_payload(prompt_payload),
            }
        )
        response_records.append(
            {
                "section_id": section_id,
                "used_fallback": used_fallback,
                "error_message": error_message,
                "raw_response": raw_response,
                "parsed_response": parsed_response,
            }
        )

    stats = _build_stage4_stats(generated_summaries)
    stats.update(
        {
            "generation_mode": "llm" if llm_generated_count > 0 else "fallback",
            "llm_attempted_section_count": len(generated_summaries),
            "llm_generated_section_count": llm_generated_count,
            "llm_fallback_section_count": fallback_count,
        }
    )

    output = SectionSummariesOutput(
        generated_at=utc_now_iso(),
        source_plan_path=str(loaded_inputs.release_plan_path),
        source_change_ir_path=str(loaded_inputs.change_ir_path),
        source_mapping_path=str(loaded_inputs.mapping_path),
        source_arch_diff_path=str(loaded_inputs.diff_ir_path),
        summaries=generated_summaries,
        stats=stats,
    )

    return output, {
        "stage4_llm_prompts": {
            "generated_at": output.generated_at,
            "record_count": len(prompt_records),
            "records": prompt_records,
        },
        "stage4_llm_responses": {
            "generated_at": output.generated_at,
            "record_count": len(response_records),
            "records": response_records,
        },
    }


def _build_section_prompt_payload(
    *,
    config,
    section: Dict[str, Any],
    commit_lookup: Dict[str, Dict[str, Any]],
    mapping_lookup: Dict[str, Dict[str, Any]],
    arch_lookup: Dict[str, Stage4ArchChange],
) -> Dict[str, str]:
    arch_evidence = [
        _to_arch_payload(arch_lookup[change_id])
        for change_id in [str(item) for item in section.get("arch_change_ids") or [] if str(item)]
        if change_id in arch_lookup
    ]

    a_type_commits, l_type_commits = _collect_ranked_commit_payloads(
        section=section,
        commit_lookup=commit_lookup,
        mapping_lookup=mapping_lookup,
    )

    return {
        "repo_name": str(getattr(getattr(config, "repo_path", None), "name", "") or ""),
        "base_ref": str(getattr(config, "base_ref", "") or ""),
        "new_ref": str(getattr(config, "new_ref", "") or ""),
        "section_plan_json": to_pretty_json(section),
        "arch_evidence_json": to_pretty_json(arch_evidence),
        "a_type_commits_json": to_pretty_json(a_type_commits),
        "l_type_commits_json": to_pretty_json(l_type_commits),
    }


def _collect_ranked_commit_payloads(
    *,
    section: Dict[str, Any],
    commit_lookup: Dict[str, Dict[str, Any]],
    mapping_lookup: Dict[str, Dict[str, Any]],
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    ranked_entries: List[Dict[str, Any]] = []
    for order, commit_id in enumerate(section.get("commit_ids") or []):
        commit = commit_lookup.get(str(commit_id))
        mapping = mapping_lookup.get(str(commit_id))
        if commit is None or mapping is None:
            continue
        ranked_entries.append(
            {
                "order": order,
                "commit_id": str(commit_id),
                "arch_label": str(mapping.get("arch_label") or ""),
                "scope": str(mapping.get("scope") or ""),
                "impact_score": _safe_float(mapping.get("impact_score")),
                "file_count": _safe_int(commit.get("file_count")),
                "method_count": _safe_int(commit.get("method_count")),
                "commit_message": str(commit.get("commit_message") or "").strip(),
                "commit_summary": str(commit.get("commit_summary") or "").strip(),
                "primary_module_name": str(mapping.get("primary_module_name") or "").strip() or None,
                "primary_component": str(mapping.get("primary_component") or "").strip() or None,
                "secondary_module_names": [str(item) for item in mapping.get("secondary_module_names") or [] if str(item)],
                "matched_arch_change_ids": [str(item) for item in mapping.get("matched_arch_change_ids") or [] if str(item)],
                "changed_files": [str(item) for item in mapping.get("changed_files") or [] if str(item)][:5],
            }
        )

    ranked_entries.sort(
        key=lambda item: (
            -_arch_priority(item["arch_label"]),
            -item["impact_score"],
            -item["file_count"],
            -item["method_count"],
            item["order"],
        )
    )

    a_type_commits = [_strip_commit_order(item) for item in ranked_entries if item["arch_label"] == "A-type"][:3]
    l_type_commits = [_strip_commit_order(item) for item in ranked_entries if item["arch_label"] != "A-type"][:3]
    return a_type_commits, l_type_commits


def _strip_commit_order(payload: Dict[str, Any]) -> Dict[str, Any]:
    result = dict(payload)
    result.pop("order", None)
    return result


def _merge_llm_section_record(
    fallback_record: SectionSummaryRecord,
    parsed_response: Dict[str, Any],
) -> SectionSummaryRecord:
    title = _clean_text(str(parsed_response.get("title") or "")) or fallback_record.title
    summary = _clean_text(str(parsed_response.get("summary") or ""))
    if not summary:
        raise ValueError("Stage 4 LLM response does not contain a non-empty summary.")

    key_points = _coerce_text_list(parsed_response.get("key_points"), limit=5)
    if not key_points:
        key_points = fallback_record.supporting_details

    return replace(
        fallback_record,
        title=title,
        summary=summary,
        supporting_details=key_points,
    )


def _mark_stage4_fallback_stats(output: SectionSummariesOutput) -> SectionSummariesOutput:
    stats = dict(output.stats)
    stats.update(
        {
            "generation_mode": "fallback",
            "llm_attempted_section_count": 0,
            "llm_generated_section_count": 0,
            "llm_fallback_section_count": len(output.summaries),
        }
    )
    return replace(output, stats=stats)


def _build_stage4_stats(summaries: List[SectionSummaryRecord]) -> Dict[str, Any]:
    return {
        "summary_count": len(summaries),
        "arch_only_section_count": sum(1 for item in summaries if item.arch_change_ids and not item.commit_ids),
        "mixed_evidence_section_count": sum(1 for item in summaries if item.arch_change_ids and item.commit_ids),
        "commit_only_section_count": sum(1 for item in summaries if item.commit_ids and not item.arch_change_ids),
        "sections_with_supporting_details_count": sum(1 for item in summaries if item.supporting_details),
        "total_supporting_detail_count": sum(len(item.supporting_details) for item in summaries),
    }


def _build_commit_lookup(change_ir: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    return {
        str(commit.get("commit_id") or ""): commit
        for commit in change_ir.get("commits") or []
        if isinstance(commit, dict) and str(commit.get("commit_id") or "")
    }


def _build_mapping_lookup(mapping_output: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    return {
        str(mapping.get("commit_id") or ""): mapping
        for mapping in mapping_output.get("mappings") or []
        if isinstance(mapping, dict) and str(mapping.get("commit_id") or "")
    }


def _to_arch_payload(item: Stage4ArchChange) -> Dict[str, Any]:
    return {
        "change_id": item.change_id,
        "change_type": item.change_type,
        "module_uid": item.module_uid,
        "module_name": item.module_name,
        "component_name": item.component_name,
        "significance": item.significance,
        "summary": item.summary,
        "related_files": item.related_files[:5],
    }


def _materialize_prompt_payload(payload: Dict[str, str]) -> Dict[str, Any]:
    materialized = dict(payload)
    for key in ("section_plan_json", "arch_evidence_json", "a_type_commits_json", "l_type_commits_json"):
        try:
            materialized[key] = _maybe_parse_json(materialized[key])
        except Exception:
            pass
    return materialized


def _maybe_parse_json(text: str) -> Any:
    return json.loads(text)


def _coerce_text_list(value: Any, *, limit: int) -> List[str]:
    if not isinstance(value, list):
        return []

    results: List[str] = []
    seen = set()
    for item in value:
        text = _clean_text(str(item or ""))
        if not text or text in seen:
            continue
        results.append(text)
        seen.add(text)
        if len(results) >= limit:
            break
    return results


def _arch_priority(label: str) -> int:
    return 1 if label == "A-type" else 0


def _safe_float(value: Any) -> float:
    try:
        return float(value)
    except Exception:
        return 0.0


def _safe_int(value: Any) -> int:
    try:
        return int(value)
    except Exception:
        return 0


def _clean_text(value: str) -> str:
    return " ".join(value.split()).strip()
