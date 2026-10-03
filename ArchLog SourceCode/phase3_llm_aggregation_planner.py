from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from difflib import SequenceMatcher
from pathlib import Path
import threading
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence

from arcrn_llm_io_exporter import export_phase3_aggregation_llm_io
from arcrn_metrics import mark_llm_metric_attempt, normalize_llm_metrics
from arcrn_models import RELEASE_NOTE_SCHEMA, SCHEMA_SLOTS, PhasePipelineResult, utc_now_iso
from arcrn_output_layout import llm_io_dir
from arcrn_stages.llm_utils import (
    TokenBucketRateLimiter,
    generate_chat_completion_with_retry,
    llm_output_validation_max_retries,
    load_prompt_text,
    maybe_build_llm_client,
    parse_json_response_strict,
    progress_bar_for,
    render_prompt_template,
    resolve_prompt_path,
    suppress_noisy_llm_loggers,
    to_compact_json,
)
from phase3_llm_debug import (
    phase3_debug_fail_fast,
    phase3_failure_output_dir,
    raise_phase3_llm_failure,
)


PROMPT_DIR = Path(__file__).resolve().parent / "prompts"
VALUE_PROMPT = PROMPT_DIR / "phase3_1_value_classification_prompt.txt"
SLOT_PROMPT = PROMPT_DIR / "phase3_1_slot_assignment_prompt.txt"
BUCKET_PROMPT = PROMPT_DIR / "phase3_1_bucket_aggregation_prompt.txt"
REVIEW_PROMPT = PROMPT_DIR / "phase3_1_group_review_prompt.txt"
LOW_PRIORITY_ROUTING_PROMPT = PROMPT_DIR / "phase3_1_low_priority_routing_prompt.txt"
LOW_PRIORITY_BRIEF_GROUPING_PROMPT = PROMPT_DIR / "phase3_1_low_priority_brief_grouping_prompt.txt"
COVERAGE_REPAIR_PROMPT = PROMPT_DIR / "phase3_1_coverage_repair_prompt.txt"

INCLUDE_DECISION = "include"
DEPRIORITIZE_DECISION = "deprioritize"
FILTER_DECISION = "filter"

VALUE_ENUM = {INCLUDE_DECISION, DEPRIORITIZE_DECISION, FILTER_DECISION}
AUDIENCE_VALUE_ENUM = {"high", "medium", "low", "none"}
ASSIGNMENT_CONFIDENCE_ENUM = {"high", "medium", "low"}

INCLUDE_REASON_CODES = {
    "architecture_guiding",
    "architecture_supporting",
    "new_feature",
    "bug_fix",
    "security",
    "performance",
    "breaking_change",
    "api_change",
    "behavior_change",
    "build_or_runtime_impact",
    "compatibility",
}
DEPRIORITIZE_REASON_CODES = {
    "internal_refactoring",
    "tests_only",
    "docs_only",
    "ci_only",
    "dependency_maintenance",
    "chore",
    "minor_maintenance",
    "low_confidence_architecture_support",
}
FILTER_REASON_CODES = {
    "formatting_only",
    "typo_only",
    "comments_only",
    "lockfile_only",
    "generated_only",
    "version_bump_only",
    "metadata_only",
    "duplicate_merge_commit",
    "trivial_docs_only",
}
ALL_REASON_CODES = INCLUDE_REASON_CODES | DEPRIORITIZE_REASON_CODES | FILTER_REASON_CODES
_AUDIT_LOCK = threading.Lock()

PHASE3_LLM_SHORT_HASH_DEFAULT_MIN_LENGTH = 7
PHASE3_LLM_SHORT_HASH_MAX_LENGTH = 10
PHASE3_LLM_SHORT_HASH_UNIQUE_PREFIX_MIN_LENGTH = 6
_PHASE3_COMMIT_SCALAR_KEYS = {"commit_id"}
_PHASE3_COMMIT_LIST_KEYS = {
    "commit_ids",
    "source_commits",
    "problem_commits",
    "included_commit_ids",
    "deprioritized_commit_ids",
    "filtered_commit_ids",
    "unassigned_commits",
    "duplicated_commits",
}


def run_phase3_llm_aggregation_planner(
    *,
    attributed_change_records_path: Path,
    output_dir: Path,
    config=None,
) -> PhasePipelineResult:
    payload = _load_json(attributed_change_records_path)
    records = [record for record in payload.get("attributed_change_records") or [] if isinstance(record, dict)]
    commit_cards = build_commit_cards(records)
    cards_by_id = _cards_by_id(commit_cards)
    records_by_id = _records_by_id(records)
    all_commit_ids = [card["commit_id"] for card in commit_cards]

    audit: Dict[str, Any] = {
        "llm_used": False,
        "generation_mode": "fallback",
        "calls": [],
        "errors": [],
        "output_dir": str(output_dir),
    }
    llm_client = maybe_build_llm_client(config) if config is not None else None
    rate_limiter = TokenBucketRateLimiter(
        qps=getattr(config, "step10_rate_limit_qps", None) if config is not None else None,
        burst=int(getattr(config, "step10_rate_limit_burst", 1)) if config is not None else 1,
    )
    low_priority_stage_artifacts = _empty_low_priority_stage_artifacts()

    if llm_client is None:
        value_decisions = _fallback_value_decisions(commit_cards)
        slot_assignments = _fallback_slot_assignments(commit_cards, value_decisions)
        buckets = build_buckets(commit_cards, value_decisions, slot_assignments)
        partial_plans = [_fallback_bucket_plan(bucket, cards_by_id, value_decisions, slot_assignments) for bucket in buckets]
        group_review_actions = _empty_group_review_actions()
        merged_before_validation = merge_partial_plans(
            partial_plans=partial_plans,
            value_decisions=value_decisions,
            cards_by_id=cards_by_id,
            generation_mode="fallback",
        )
        low_priority_actions = _fallback_low_priority_actions(merged_before_validation, cards_by_id)
        merged_before_validation = apply_low_priority_actions(
            merged_before_validation,
            low_priority_actions,
            cards_by_id=cards_by_id,
        )
        repair_actions = {"repair_actions": []}
    else:
        audit["generation_mode"] = "llm_multi_stage"
        value_decisions = classify_commit_values_with_llm(
            commit_cards=commit_cards,
            llm_client=llm_client,
            rate_limiter=rate_limiter,
            config=config,
            audit=audit,
        )
        slot_assignments = assign_slots_with_llm(
            commit_cards=commit_cards,
            value_decisions=value_decisions,
            llm_client=llm_client,
            rate_limiter=rate_limiter,
            config=config,
            audit=audit,
        )
        buckets = build_buckets(commit_cards, value_decisions, slot_assignments)
        partial_plans = plan_buckets_with_llm(
            buckets=buckets,
            cards_by_id=cards_by_id,
            value_decisions=value_decisions,
            slot_assignments=slot_assignments,
            llm_client=llm_client,
            rate_limiter=rate_limiter,
            config=config,
            audit=audit,
        )
        group_review_actions = review_groups_with_llm(
            partial_plans=partial_plans,
            llm_client=llm_client,
            rate_limiter=rate_limiter,
            config=config,
            audit=audit,
        )
        merged_before_validation = merge_partial_plans(
            partial_plans=partial_plans,
            value_decisions=value_decisions,
            cards_by_id=cards_by_id,
            generation_mode="llm_multi_stage",
        )
        merged_before_validation = apply_group_review_actions(
            merged_before_validation,
            group_review_actions,
            cards_by_id=cards_by_id,
        )
        low_priority_actions = plan_low_priority_commits_with_llm(
            plan=merged_before_validation,
            cards_by_id=cards_by_id,
            value_decisions=value_decisions,
            llm_client=llm_client,
            rate_limiter=rate_limiter,
            config=config,
            audit=audit,
            stage_artifacts=low_priority_stage_artifacts,
        )
        merged_before_validation = apply_low_priority_actions(
            merged_before_validation,
            low_priority_actions,
            cards_by_id=cards_by_id,
        )
        validated_once = validate_aggregation_plan(merged_before_validation, all_commit_ids, records)
        if _coverage_has_fail_fast_errors(validated_once.get("coverage_report", {})):
            if phase3_debug_fail_fast(config):
                _raise_phase3_coverage_failure(
                    config=config,
                    audit=audit,
                    plan=validated_once,
                    all_commit_ids=all_commit_ids,
                    stage="phase3.1.5:validation",
                    context_name="coverage",
                )
            repair_actions = repair_coverage_with_llm(
                plan=validated_once,
                problem_commit_ids=validated_once["coverage_report"]["unassigned_commits"],
                cards_by_id=cards_by_id,
                llm_client=llm_client,
                rate_limiter=rate_limiter,
                config=config,
                audit=audit,
            )
            merged_before_validation = apply_coverage_repair_actions(
                validated_once,
                repair_actions,
                cards_by_id=cards_by_id,
            )
        else:
            repair_actions = {"repair_actions": []}

    final_plan = validate_aggregation_plan(merged_before_validation, all_commit_ids, records)
    coverage_errors = final_plan.get("coverage_report", {})
    unassigned = coverage_errors.get("unassigned_commits") or []
    duplicated = coverage_errors.get("duplicated_commits") or []
    if unassigned or duplicated:
        if phase3_debug_fail_fast(config):
            _raise_phase3_coverage_failure(
                config=config,
                audit=audit,
                plan=final_plan,
                all_commit_ids=all_commit_ids,
                stage="phase3.1.5:validation",
                context_name="final_coverage",
            )
        _fallback_assign_missing_into_plan(final_plan, [cards_by_id[commit_id] for commit_id in unassigned if commit_id in cards_by_id])
        final_plan = validate_aggregation_plan(final_plan, all_commit_ids, records)

    final_plan["generation_mode"] = audit["generation_mode"]
    validation_report = _validation_report(final_plan, all_commit_ids)
    intermediates = {
        "phase3_1_commit_cards": {"commit_cards": commit_cards},
        "phase3_1_value_decisions": {"decisions": value_decisions},
        "phase3_1_slot_assignments": {"slot_assignments": slot_assignments},
        "phase3_1_buckets": {"buckets": buckets},
        "phase3_1_partial_plans": {"partial_plans": partial_plans},
        "phase3_1_group_review_actions": group_review_actions,
        "phase3_1_low_priority_actions": low_priority_actions,
        "phase3_1_low_priority_routing_decisions": low_priority_stage_artifacts["phase3_1_low_priority_routing_decisions"],
        "phase3_1_low_priority_brief_groups": low_priority_stage_artifacts["phase3_1_low_priority_brief_groups"],
        "phase3_1_merged_plan_before_validation": {"aggregation_plan": merged_before_validation},
        "phase3_1_validation_report": validation_report,
        "phase3_1_repair_actions": repair_actions,
    }

    coverage = final_plan.get("coverage_report") or {}
    output = {
        "generated_at": utc_now_iso(),
        "source_attributed_change_records_path": str(attributed_change_records_path),
        "schema": RELEASE_NOTE_SCHEMA,
        "aggregation_plan": final_plan,
        "stats": {
            "group_count": _count_groups(final_plan),
            "llm_used": 1 if audit.get("llm_used") else 0,
            "generation_mode": final_plan.get("generation_mode") or audit["generation_mode"],
            "total_commits": coverage.get("total_commits", len(records)),
            "included_commits": coverage.get("included_commits", 0),
            "deprioritized_commits": coverage.get("deprioritized_commits", 0),
            "filtered_commits": coverage.get("filtered_commits", 0),
            "unassigned_commits": len(coverage.get("unassigned_commits") or []),
            "phase3_1_llm_call_count": len(audit.get("calls") or []),
        },
    }
    output_files = _export(output, audit, intermediates, output_dir)
    return PhasePipelineResult(output_files=output_files, stats=output["stats"])


def build_commit_cards(attributed_records: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    cards: List[Dict[str, Any]] = []
    for record in attributed_records:
        commit_id = str(record.get("commit_id") or "")
        if not commit_id:
            continue
        changed_files = _changed_files(record)
        top_event = _top_event(record)
        cards.append(
            {
                "commit_id": commit_id,
                "commit_message": str(record.get("commit_message") or ""),
                "commit_summary": str(record.get("commit_summary") or ""),
                "functional_category": str(record.get("functional_category") or "unknown"),
                "evidence_granularity": str(record.get("evidence_granularity") or "method_level"),
                "change_detection_status": str(record.get("change_detection_status") or "method_level_change"),
                "structure_role": str(record.get("structure_role") or "local_supporting"),
                "architecture_signal_score": _safe_float(record.get("architecture_signal_score")),
                "architecture_relevance_score": _safe_float(record.get("architecture_relevance_score")),
                "architecture_relevance_level": str(record.get("architecture_relevance_level") or ""),
                "architecture_relevance_labels": [str(item) for item in record.get("architecture_relevance_labels") or [] if str(item)],
                "architecture_relevance_reason": str(record.get("architecture_relevance_reason") or ""),
                "arch_impact_prior": _safe_float(record.get("arch_impact_prior")),
                "confidence": _confidence_float(record.get("confidence")),
                "primary_module": str(record.get("primary_module") or ""),
                "primary_component": str(record.get("primary_component") or ""),
                "top_event": top_event,
                "related_arch_events": _event_ids_for_record(record),
                "changed_files_summary": _changed_files_summary(changed_files),
                "negative_evidence": _negative_evidence(record),
                "source_refs": record.get("source_refs") or {},
            }
        )
    return cards


def classify_commit_values_with_llm(
    *,
    commit_cards: Sequence[Dict[str, Any]],
    llm_client,
    rate_limiter: TokenBucketRateLimiter,
    config,
    audit: Dict[str, Any],
) -> List[Dict[str, Any]]:
    decisions: List[Dict[str, Any]] = []
    batch_size = _phase3_batch_size(config, "phase3_value_batch_size", 8)
    batches = list(enumerate(_chunks(list(commit_cards), batch_size), start=1))
    progress_bar = progress_bar_for(config, "Phase3.1 value classification progress") if batches else None

    def classify_batch(index: int, batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        id_map = _build_phase3_llm_commit_id_map([card["commit_id"] for card in batch], config)
        prompt_batch = _shorten_commit_ids_for_llm(_value_prompt_cards(batch), id_map)
        expected_commit_ids = [card["commit_id"] for card in batch]
        base_debug_context = {
            "input_summary": {"commit_count": len(batch), "batch": f"batch{index}"},
            "input_payload": {"commit_cards": prompt_batch},
            "commit_id_map": _phase3_llm_commit_id_map_debug(id_map),
        }

        def validate_payload(parsed: Dict[str, Any]) -> None:
            restored = _restore_commit_ids_from_llm(parsed, id_map)
            _validate_value_payload(restored, expected_commit_ids)

        def request_payload(request_suffix: str, debug_context: Dict[str, Any], validate_fn) -> Dict[str, Any]:
            return _call_json_stage(
                stage="phase3.1.1:value_classification",
                prompt_path=VALUE_PROMPT,
                target_json_type="value_classification",
                target_schema={
                    "decisions": [
                        {
                            "commit_id": "",
                            "release_note_value": "include",
                            "reason_code": "bug_fix",
                            "target_audience_value": "medium",
                            "reason": "",
                        }
                    ]
                },
                values={"commit_cards_json": to_compact_json(prompt_batch)},
                llm_client=llm_client,
                rate_limiter=rate_limiter,
                config=config,
                audit=audit,
                request_suffix=request_suffix,
                debug_context=debug_context,
                validate_fn=validate_fn,
            )

        payload = request_payload(f"batch{index}", base_debug_context, validate_payload)
        payload = _restore_commit_ids_from_llm(payload, id_map)
        return _normalize_value_decisions(payload, batch)

    concurrency = _phase3_concurrency(config, "phase3_value_concurrency")
    if progress_bar is not None:
        progress_bar.update(completed=0, total=len(batches))
    try:
        with suppress_noisy_llm_loggers(enabled=progress_bar is not None):
            if concurrency <= 1 or len(batches) <= 1:
                for completed, (index, batch) in enumerate(batches, start=1):
                    decisions.extend(classify_batch(index, batch))
                    if progress_bar is not None:
                        progress_bar.update(completed=completed, total=len(batches))
            else:
                results: Dict[int, List[Dict[str, Any]]] = {}
                with ThreadPoolExecutor(max_workers=min(concurrency, len(batches)), thread_name_prefix="phase3-value") as executor:
                    future_to_index = {
                        executor.submit(classify_batch, index, batch): index
                        for index, batch in batches
                    }
                    completed = 0
                    for future in as_completed(future_to_index):
                        index = future_to_index[future]
                        results[index] = future.result()
                        completed += 1
                        if progress_bar is not None:
                            progress_bar.update(completed=completed, total=len(batches))
                for index, _batch in batches:
                    decisions.extend(results.get(index, []))
    finally:
        if progress_bar is not None:
            progress_bar.finish()
    return _normalize_value_decisions({"decisions": decisions}, commit_cards)


def assign_slots_with_llm(
    *,
    commit_cards: Sequence[Dict[str, Any]],
    value_decisions: Sequence[Dict[str, Any]],
    llm_client,
    rate_limiter: TokenBucketRateLimiter,
    config,
    audit: Dict[str, Any],
) -> List[Dict[str, Any]]:
    decision_by_id = _by_id(value_decisions)
    candidates = [
        card
        for card in commit_cards
        if decision_by_id.get(card["commit_id"], {}).get("release_note_value") != FILTER_DECISION
    ]
    assignments: List[Dict[str, Any]] = []
    batch_size = _phase3_batch_size(config, "phase3_slot_batch_size", 15)
    batches = list(enumerate(_chunks(candidates, batch_size), start=1))
    progress_bar = progress_bar_for(config, "Phase3.1 slot assignment progress") if batches else None

    def assign_batch(index: int, batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        batch_cards = [
            _card_with_value_decision(card, decision_by_id.get(card["commit_id"], {}))
            for card in batch
        ]
        id_map = _build_phase3_llm_commit_id_map([card["commit_id"] for card in batch_cards], config)
        prompt_cards = _shorten_commit_ids_for_llm(_slot_prompt_cards(batch_cards), id_map)

        def validate_payload(parsed: Dict[str, Any]) -> None:
            restored = _restore_commit_ids_from_llm(parsed, id_map)
            _validate_slot_assignment_payload(restored, [card["commit_id"] for card in batch_cards])

        payload = _call_json_stage(
            stage="phase3.1.2:slot_assignment",
            prompt_path=SLOT_PROMPT,
            target_json_type="slot_assignment",
            target_schema={"assignments": [{"commit_id": "", "slot": "others", "event_id": "", "reason": ""}]},
            values={
                "commit_cards_json": to_compact_json(prompt_cards),
                "required_assignment_count": str(len(prompt_cards)),
            },
            llm_client=llm_client,
            rate_limiter=rate_limiter,
            config=config,
            audit=audit,
            request_suffix=f"batch{index}",
            debug_context={
                "input_summary": {"commit_count": len(prompt_cards), "batch": f"batch{index}"},
                "input_payload": {"commit_cards": prompt_cards},
                "commit_id_map": _phase3_llm_commit_id_map_debug(id_map),
            },
            validate_fn=validate_payload,
        )
        payload = _restore_commit_ids_from_llm(payload, id_map)
        batch_decisions = [decision_by_id[card["commit_id"]] for card in batch if card["commit_id"] in decision_by_id]
        return _normalize_slot_assignments(payload, batch_cards, batch_decisions)

    concurrency = _phase3_concurrency(config, "phase3_slot_assignment_concurrency")
    if progress_bar is not None:
        progress_bar.update(completed=0, total=len(batches))
    try:
        with suppress_noisy_llm_loggers(enabled=progress_bar is not None):
            if concurrency <= 1 or len(batches) <= 1:
                for completed, (index, batch) in enumerate(batches, start=1):
                    assignments.extend(assign_batch(index, batch))
                    if progress_bar is not None:
                        progress_bar.update(completed=completed, total=len(batches))
            else:
                results: Dict[int, List[Dict[str, Any]]] = {}
                with ThreadPoolExecutor(max_workers=min(concurrency, len(batches)), thread_name_prefix="phase3-slot") as executor:
                    future_to_index = {
                        executor.submit(assign_batch, index, batch): index
                        for index, batch in batches
                    }
                    completed = 0
                    for future in as_completed(future_to_index):
                        index = future_to_index[future]
                        results[index] = future.result()
                        completed += 1
                        if progress_bar is not None:
                            progress_bar.update(completed=completed, total=len(batches))
                for index, _batch in batches:
                    assignments.extend(results.get(index, []))
    finally:
        if progress_bar is not None:
            progress_bar.finish()
    return _normalize_slot_assignments({"slot_assignments": assignments}, candidates, value_decisions)


def _card_with_value_decision(card: Dict[str, Any], decision: Dict[str, Any]) -> Dict[str, Any]:
    merged = dict(card)
    for key in ("release_note_value", "reason_code", "target_audience_value"):
        if decision.get(key):
            merged[key] = decision[key]
    if decision.get("reason"):
        merged["value_reason"] = decision["reason"]
    return merged


def _value_prompt_cards(cards: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [_value_prompt_card(card) for card in cards]


def _value_prompt_card(card: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "commit_id": str(card.get("commit_id") or ""),
        "commit_summary": str(card.get("commit_summary") or ""),
        "functional_category": str(card.get("functional_category") or "unknown"),
        "evidence_granularity": str(card.get("evidence_granularity") or ""),
        "change_detection_status": str(card.get("change_detection_status") or ""),
        "changed_files_summary": card.get("changed_files_summary") or {},
        "negative_evidence": _safe_float(card.get("negative_evidence")),
        "architecture_hint": _architecture_hint_for_prompt(card),
    }


def _slot_prompt_cards(cards: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [_slot_prompt_card(card) for card in cards]


def _slot_prompt_card(card: Dict[str, Any]) -> Dict[str, Any]:
    prompt_card = _value_prompt_card(card)
    prompt_card["release_note_value"] = str(card.get("release_note_value") or "")
    prompt_card["reason_code"] = str(card.get("reason_code") or "")
    prompt_card["target_audience_value"] = str(card.get("target_audience_value") or "")
    return prompt_card


def _bucket_prompt_cards(
    cards: Sequence[Dict[str, Any]],
    decision_by_id: Dict[str, Dict[str, Any]],
    assignment_by_id: Dict[str, Dict[str, Any]],
) -> List[Dict[str, Any]]:
    return [
        _bucket_prompt_card(
            card,
            decision_by_id.get(str(card.get("commit_id") or ""), {}),
            assignment_by_id.get(str(card.get("commit_id") or ""), {}),
        )
        for card in cards
    ]


def _bucket_prompt_card(card: Dict[str, Any], decision: Dict[str, Any], assignment: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "commit_id": str(card.get("commit_id") or ""),
        "commit_summary": str(card.get("commit_summary") or ""),
        "release_note_value": str(decision.get("release_note_value") or ""),
        "reason_code": str(decision.get("reason_code") or ""),
        "assigned_slot": str(assignment.get("primary_slot") or ""),
        "changed_files_summary": card.get("changed_files_summary") or {},
        "evidence_granularity": str(card.get("evidence_granularity") or ""),
        "architecture_hint": _architecture_hint_for_prompt(card),
    }


def _architecture_hint_for_prompt(card: Dict[str, Any]) -> Dict[str, Any]:
    top_event = card.get("top_event") or {}
    hint = {
        "structure_role": str(card.get("structure_role") or "local_supporting"),
        "architecture_relevance_score": _arch_score(card),
        "legacy_architecture_signal_score": _safe_float(card.get("architecture_signal_score")),
        "architecture_relevance_level": str(card.get("architecture_relevance_level") or ""),
        "architecture_relevance_labels": [str(item) for item in card.get("architecture_relevance_labels") or [] if str(item)],
        "architecture_relevance_reason": str(card.get("architecture_relevance_reason") or ""),
        "event_id": str(top_event.get("event_id") or ""),
        "event_type": str(top_event.get("event_type") or ""),
        "module": str(top_event.get("module") or card.get("primary_module") or ""),
    }
    return hint


def build_buckets(
    commit_cards: Sequence[Dict[str, Any]],
    value_decisions: Sequence[Dict[str, Any]],
    slot_assignments: Sequence[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    decision_by_id = _by_id(value_decisions)
    assignment_by_id = _by_id(slot_assignments)
    bucket_map: Dict[str, Dict[str, Any]] = {}
    for card in commit_cards:
        commit_id = card["commit_id"]
        decision = decision_by_id.get(commit_id, {})
        if decision.get("release_note_value") == FILTER_DECISION:
            continue
        assignment = assignment_by_id.get(commit_id)
        if not assignment:
            assignment = _fallback_slot_assignment(card, decision)
        slot = assignment["primary_slot"]
        event_id = card.get("top_event", {}).get("event_id") if slot.startswith("architecture_changes") else ""
        bucket_key = f"{slot}::{event_id}" if event_id else slot
        bucket = bucket_map.setdefault(
            bucket_key,
            {
                "bucket_id": bucket_key,
                "slot": slot,
                "event_id": event_id or "",
                "commit_ids": [],
                "is_architecture_event_bucket": bool(event_id),
            },
        )
        bucket["commit_ids"].append(commit_id)

    max_bucket_size = 20
    buckets: List[Dict[str, Any]] = []
    for bucket in bucket_map.values():
        commit_ids = bucket["commit_ids"]
        if len(commit_ids) <= max_bucket_size:
            buckets.append(bucket)
            continue
        for index, chunk in enumerate(_chunks(commit_ids, max_bucket_size), start=1):
            next_bucket = dict(bucket)
            next_bucket["bucket_id"] = f"{bucket['bucket_id']}::chunk_{index:03d}"
            next_bucket["commit_ids"] = chunk
            buckets.append(next_bucket)
    return buckets


def plan_buckets_with_llm(
    *,
    buckets: Sequence[Dict[str, Any]],
    cards_by_id: Dict[str, Dict[str, Any]],
    value_decisions: Sequence[Dict[str, Any]],
    slot_assignments: Sequence[Dict[str, Any]],
    llm_client,
    rate_limiter: TokenBucketRateLimiter,
    config,
    audit: Dict[str, Any],
) -> List[Dict[str, Any]]:
    decision_by_id = _by_id(value_decisions)
    assignment_by_id = _by_id(slot_assignments)
    bucket_items = list(enumerate(buckets, start=1))
    progress_bar = progress_bar_for(config, "Phase3.1 bucket aggregation progress") if bucket_items else None

    def plan_one_bucket(_index: int, bucket: Dict[str, Any]) -> Dict[str, Any]:
        bucket_cards = [cards_by_id[commit_id] for commit_id in bucket["commit_ids"] if commit_id in cards_by_id]
        id_map = _build_phase3_llm_commit_id_map(bucket.get("commit_ids") or [], config)
        prompt_bucket = _shorten_commit_ids_for_llm(bucket, id_map)
        prompt_bucket_cards = _shorten_commit_ids_for_llm(
            _bucket_prompt_cards(bucket_cards, decision_by_id, assignment_by_id),
            id_map,
        )

        def validate_payload(parsed: Dict[str, Any]) -> None:
            restored = _restore_commit_ids_from_llm(parsed, id_map)
            _validate_bucket_payload(restored, bucket)

        payload = _call_json_stage(
            stage="phase3.1.3:bucket_aggregation",
            prompt_path=BUCKET_PROMPT,
            target_json_type="bucket_aggregation",
            target_schema={"groups": [], "deprioritized": [], "filtered": []},
            values={
                "bucket_json": to_compact_json(prompt_bucket),
                "bucket_commit_cards_json": to_compact_json(prompt_bucket_cards),
            },
            llm_client=llm_client,
            rate_limiter=rate_limiter,
            config=config,
            audit=audit,
            request_suffix=bucket["bucket_id"],
            debug_context={
                "input_summary": {
                    "commit_count": len(bucket_cards),
                    "bucket_id": bucket.get("bucket_id", ""),
                    "slot": bucket.get("slot", ""),
                },
                "input_payload": {
                    "bucket": prompt_bucket,
                    "commit_cards": prompt_bucket_cards,
                },
                "commit_id_map": _phase3_llm_commit_id_map_debug(id_map),
            },
            validate_fn=validate_payload,
        )
        payload = _restore_commit_ids_from_llm(payload, id_map)
        _validate_bucket_payload(payload, bucket)
        return _normalize_bucket_plan(
            payload,
            bucket,
            cards_by_id=cards_by_id,
            value_decisions=decision_by_id,
            slot_assignments=assignment_by_id,
            debug=phase3_debug_fail_fast(config),
        )

    concurrency = _phase3_concurrency(config, "phase3_bucket_concurrency")
    if progress_bar is not None:
        progress_bar.update(completed=0, total=len(bucket_items))
    try:
        with suppress_noisy_llm_loggers(enabled=progress_bar is not None):
            if concurrency <= 1 or len(bucket_items) <= 1:
                plans: List[Dict[str, Any]] = []
                for completed, (index, bucket) in enumerate(bucket_items, start=1):
                    plans.append(plan_one_bucket(index, bucket))
                    if progress_bar is not None:
                        progress_bar.update(completed=completed, total=len(bucket_items))
                return plans

            results: Dict[int, Dict[str, Any]] = {}
            with ThreadPoolExecutor(max_workers=min(concurrency, len(bucket_items)), thread_name_prefix="phase3-bucket") as executor:
                future_to_index = {
                    executor.submit(plan_one_bucket, index, bucket): index
                    for index, bucket in bucket_items
                }
                completed = 0
                for future in as_completed(future_to_index):
                    index = future_to_index[future]
                    results[index] = future.result()
                    completed += 1
                    if progress_bar is not None:
                        progress_bar.update(completed=completed, total=len(bucket_items))
            return [results[index] for index, _bucket in bucket_items if index in results]
    finally:
        if progress_bar is not None:
            progress_bar.finish()


def review_groups_with_llm(
    *,
    partial_plans: Sequence[Dict[str, Any]],
    llm_client,
    rate_limiter: TokenBucketRateLimiter,
    config,
    audit: Dict[str, Any],
) -> Dict[str, Any]:
    summaries = _group_summaries(partial_plans)
    if not summaries:
        return _empty_group_review_actions()
    batch_size = _phase3_batch_size(config, "phase3_group_review_batch_size", 40)
    chunks = list(enumerate(_chunks(summaries, batch_size), start=1))
    combined_actions = _empty_group_review_actions()
    progress_bar = progress_bar_for(config, "Phase3.1 group review progress")
    if progress_bar is not None:
        progress_bar.update(completed=0, total=len(chunks))
    try:
        with suppress_noisy_llm_loggers(enabled=progress_bar is not None):
            for chunk_index, chunk in chunks:
                payload = _call_json_stage(
                    stage="phase3.1.4:group_review",
                    prompt_path=REVIEW_PROMPT,
                    target_json_type="group_review",
                    target_schema={"actions": []},
                    values={
                        "group_summaries_json": to_compact_json(chunk),
                        "slot_enum_json": to_compact_json(SCHEMA_SLOTS),
                    },
                    llm_client=llm_client,
                    rate_limiter=rate_limiter,
                    config=config,
                    audit=audit,
                    request_suffix=f"chunk{chunk_index:03d}",
                    debug_context={
                        "input_summary": {
                            "group_count": len(chunk),
                            "total_group_count": len(summaries),
                            "chunk_index": chunk_index,
                            "chunk_count": len(chunks),
                        },
                        "input_payload": {"groups": chunk},
                    },
                    validate_fn=lambda parsed, s=chunk: _validate_group_review_payload(parsed, s),
                )
                actions = _normalize_group_review_actions(payload, chunk)
                _extend_group_review_actions(combined_actions, actions)
                if progress_bar is not None:
                    progress_bar.update(completed=chunk_index, total=len(chunks))
    finally:
        if progress_bar is not None:
            progress_bar.finish()
    return combined_actions


def plan_low_priority_commits_with_llm(
    *,
    plan: Dict[str, Any],
    cards_by_id: Dict[str, Dict[str, Any]],
    value_decisions: Sequence[Dict[str, Any]],
    llm_client,
    rate_limiter: TokenBucketRateLimiter,
    config,
    audit: Dict[str, Any],
    stage_artifacts: Optional[Dict[str, Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    low_priority_commits = _low_priority_items_for_prompt(plan, cards_by_id, value_decisions)
    artifacts = stage_artifacts if stage_artifacts is not None else _empty_low_priority_stage_artifacts()
    artifacts.update(_empty_low_priority_stage_artifacts())
    if not low_priority_commits:
        return _empty_low_priority_actions()

    deprioritized = [
        item for item in low_priority_commits
        if str(item.get("release_note_value") or "") == DEPRIORITIZE_DECISION
    ]
    filtered = [
        {**item, "suggested_slot": "others"}
        for item in low_priority_commits
        if str(item.get("release_note_value") or "") == FILTER_DECISION
    ]
    routing_decisions = _route_deprioritized_commits_with_llm(
        deprioritized_commits=deprioritized,
        plan=plan,
        llm_client=llm_client,
        rate_limiter=rate_limiter,
        config=config,
        audit=audit,
        artifact=artifacts["phase3_1_low_priority_routing_decisions"],
    )
    decision_by_id = {str(item.get("commit_id") or ""): item for item in routing_decisions}
    merge_actions: List[Dict[str, Any]] = []
    brief_candidates: List[Dict[str, Any]] = []
    for item in low_priority_commits:
        commit_id = str(item.get("commit_id") or "")
        if str(item.get("release_note_value") or "") == FILTER_DECISION:
            brief_candidates.append({**item, "suggested_slot": "others"})
            continue
        decision = decision_by_id.get(commit_id)
        if not decision:
            raise ValueError(f"Missing low-priority routing decision for commit: {commit_id}")
        if decision["action"] == "merge_existing":
            merge_actions.append(
                {
                    "target_group_id": decision["target_group_id"],
                    "source_commits": [commit_id],
                    "merge_note": decision["reason"],
                    "reason": decision["reason"],
                }
            )
            continue
        brief_candidates.append({**item, "suggested_slot": decision["brief_slot"]})

    brief_groups = _group_low_priority_brief_commits_with_llm(
        brief_commits=brief_candidates,
        llm_client=llm_client,
        rate_limiter=rate_limiter,
        config=config,
        audit=audit,
        artifact=artifacts["phase3_1_low_priority_brief_groups"],
    )
    actions = {"brief_groups": brief_groups, "merge_actions": merge_actions}
    _validate_low_priority_payload(actions, low_priority_commits, plan)
    return actions


def _empty_low_priority_stage_artifacts() -> Dict[str, Dict[str, Any]]:
    return {
        "phase3_1_low_priority_routing_decisions": {"routing_batches": [], "decisions": []},
        "phase3_1_low_priority_brief_groups": {"brief_chunks": [], "brief_groups": []},
    }


def _route_deprioritized_commits_with_llm(
    *,
    deprioritized_commits: Sequence[Dict[str, Any]],
    plan: Dict[str, Any],
    llm_client,
    rate_limiter: TokenBucketRateLimiter,
    config,
    audit: Dict[str, Any],
    artifact: Dict[str, Any],
) -> List[Dict[str, Any]]:
    if not deprioritized_commits:
        return []
    candidates, group_ref_to_id = _low_priority_existing_entry_candidates(plan)
    batch_size = _phase3_batch_size(config, "phase3_low_priority_routing_batch_size", 8)
    batches = list(_chunks(list(deprioritized_commits), batch_size))
    decisions: List[Dict[str, Any]] = []
    progress_bar = progress_bar_for(config, "Phase3.1 low priority routing progress")
    if progress_bar is not None:
        progress_bar.update(completed=0, total=len(batches))

    def route_batch(batch_index: int, batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        batch_candidates = _low_priority_candidates_for_batch(
            candidates,
            batch,
            limit=int(getattr(config, "phase3_low_priority_routing_candidate_limit", 80) or 80),
        )
        id_map = _build_phase3_llm_commit_id_map(
            [item["commit_id"] for item in batch if item.get("commit_id")],
            config,
        )
        prompt_commits = _shorten_commit_ids_for_llm(
            [_low_priority_routing_prompt_item(item) for item in batch],
            id_map,
        )

        def validate_payload(parsed: Dict[str, Any], current_batch=batch, current_map=id_map) -> None:
            restored = _restore_commit_ids_from_llm(parsed, current_map)
            _validate_low_priority_routing_payload(restored, current_batch, group_ref_to_id)

        payload = _call_json_stage(
            stage="phase3.1.5a:low_priority_routing",
            prompt_path=LOW_PRIORITY_ROUTING_PROMPT,
            target_json_type="low_priority_routing",
            target_schema={"decisions": []},
            values={
                "slot_enum_json": to_compact_json(SCHEMA_SLOTS),
                "existing_entry_candidates_json": to_compact_json(batch_candidates),
                "deprioritized_commits_json": to_compact_json(prompt_commits),
            },
            llm_client=llm_client,
            rate_limiter=rate_limiter,
            config=config,
            audit=audit,
            request_suffix=f"batch{batch_index:03d}",
            debug_context={
                "input_summary": {
                    "deprioritized_commit_count": len(batch),
                    "existing_entry_candidate_count": len(batch_candidates),
                    "total_existing_entry_candidate_count": len(candidates),
                },
                "input_payload": {
                    "deprioritized_commits": prompt_commits,
                    "existing_entry_candidates": batch_candidates,
                },
                "commit_id_map": _phase3_llm_commit_id_map_debug(id_map),
                "group_ref_to_id": dict(group_ref_to_id),
            },
            validate_fn=validate_payload,
        )
        restored = _restore_commit_ids_from_llm(payload, id_map)
        _validate_low_priority_routing_payload(restored, batch, group_ref_to_id)
        return _normalize_low_priority_routing_decisions(restored, group_ref_to_id)

    concurrency = _phase3_concurrency(config, "phase3_low_priority_routing_concurrency")
    try:
        with suppress_noisy_llm_loggers(enabled=progress_bar is not None):
            batch_pairs = list(enumerate(batches, start=1))
            results: Dict[int, List[Dict[str, Any]]] = {}
            if concurrency <= 1 or len(batch_pairs) <= 1:
                for completed, (batch_index, batch) in enumerate(batch_pairs, start=1):
                    results[batch_index] = route_batch(batch_index, batch)
                    if progress_bar is not None:
                        progress_bar.update(completed=completed, total=len(batches))
            else:
                with ThreadPoolExecutor(
                    max_workers=min(concurrency, len(batch_pairs)),
                    thread_name_prefix="phase3-low-routing",
                ) as executor:
                    future_to_index = {
                        executor.submit(route_batch, batch_index, batch): batch_index
                        for batch_index, batch in batch_pairs
                    }
                    completed = 0
                    for future in as_completed(future_to_index):
                        batch_index = future_to_index[future]
                        results[batch_index] = future.result()
                        completed += 1
                        if progress_bar is not None:
                            progress_bar.update(completed=completed, total=len(batches))
            for batch_index, batch in batch_pairs:
                normalized = results.get(batch_index, [])
                artifact["routing_batches"].append(
                    {
                        "batch_id": f"batch{batch_index:03d}",
                        "commit_ids": [str(item.get("commit_id") or "") for item in batch],
                        "decisions": normalized,
                    }
                )
                decisions.extend(normalized)
    finally:
        if progress_bar is not None:
            progress_bar.finish()
    artifact["decisions"] = list(decisions)
    return decisions


def _group_low_priority_brief_commits_with_llm(
    *,
    brief_commits: Sequence[Dict[str, Any]],
    llm_client,
    rate_limiter: TokenBucketRateLimiter,
    config,
    audit: Dict[str, Any],
    artifact: Dict[str, Any],
) -> List[Dict[str, Any]]:
    by_slot: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for item in brief_commits:
        slot = str(item.get("suggested_slot") or "")
        if slot not in SCHEMA_SLOTS:
            raise ValueError(f"Invalid low-priority brief slot for {item.get('commit_id')}: {slot}")
        by_slot[slot].append(item)
    batch_size = _phase3_batch_size(config, "phase3_low_priority_brief_batch_size", 20)
    chunks: List[tuple[str, int, List[Dict[str, Any]]]] = []
    for slot in SCHEMA_SLOTS:
        for chunk_index, chunk in enumerate(_chunks(by_slot.get(slot, []), batch_size), start=1):
            chunks.append((slot, chunk_index, chunk))
    brief_groups: List[Dict[str, Any]] = []
    progress_bar = progress_bar_for(config, "Phase3.1 low priority brief grouping progress") if chunks else None
    if progress_bar is not None:
        progress_bar.update(completed=0, total=len(chunks))

    def process_chunk(slot: str, chunk_index: int, chunk: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        id_map = _build_phase3_llm_commit_id_map(
            [item["commit_id"] for item in chunk if item.get("commit_id")],
            config,
        )
        prompt_commits = _shorten_commit_ids_for_llm(
            [_low_priority_brief_prompt_item(item) for item in chunk],
            id_map,
        )

        def validate_payload(parsed: Dict[str, Any], current_chunk=chunk, current_map=id_map) -> None:
            restored = _restore_commit_ids_from_llm(parsed, current_map)
            _validate_low_priority_brief_payload(restored, current_chunk)

        suffix = f"{slot}_chunk{chunk_index:03d}"
        payload = _call_json_stage(
            stage="phase3.1.5b:low_priority_brief_grouping",
            prompt_path=LOW_PRIORITY_BRIEF_GROUPING_PROMPT,
            target_json_type="low_priority_brief_grouping",
            target_schema={"brief_groups": []},
            values={
                "target_slot_json": to_compact_json({"slot": slot, "display_name": _slot_display_name(slot)}),
                "brief_commits_json": to_compact_json(prompt_commits),
            },
            llm_client=llm_client,
            rate_limiter=rate_limiter,
            config=config,
            audit=audit,
            request_suffix=suffix,
            debug_context={
                "input_summary": {"slot": slot, "brief_commit_count": len(chunk)},
                "input_payload": {"target_slot": slot, "brief_commits": prompt_commits},
                "commit_id_map": _phase3_llm_commit_id_map_debug(id_map),
            },
            validate_fn=validate_payload,
        )
        restored = _restore_commit_ids_from_llm(payload, id_map)
        _validate_low_priority_brief_payload(restored, chunk)
        return _normalize_low_priority_brief_groups(restored, chunk, slot)

    concurrency = _phase3_concurrency(config, "phase3_low_priority_brief_concurrency")
    try:
        with suppress_noisy_llm_loggers(enabled=progress_bar is not None):
            results: Dict[int, List[Dict[str, Any]]] = {}
            if concurrency <= 1 or len(chunks) <= 1:
                for completed, (slot, chunk_index, chunk) in enumerate(chunks, start=1):
                    results[completed - 1] = process_chunk(slot, chunk_index, chunk)
                    if progress_bar is not None:
                        progress_bar.update(completed=completed, total=len(chunks))
            else:
                with ThreadPoolExecutor(
                    max_workers=min(concurrency, len(chunks)),
                    thread_name_prefix="phase3-low-brief",
                ) as executor:
                    future_to_index = {
                        executor.submit(process_chunk, slot, chunk_index, chunk): index
                        for index, (slot, chunk_index, chunk) in enumerate(chunks)
                    }
                    completed = 0
                    for future in as_completed(future_to_index):
                        index = future_to_index[future]
                        results[index] = future.result()
                        completed += 1
                        if progress_bar is not None:
                            progress_bar.update(completed=completed, total=len(chunks))
            for index, (slot, chunk_index, chunk) in enumerate(chunks):
                normalized = results.get(index, [])
                artifact["brief_chunks"].append(
                    {
                        "slot": slot,
                        "chunk_id": f"chunk{chunk_index:03d}",
                        "commit_ids": [str(item.get("commit_id") or "") for item in chunk],
                        "brief_groups": normalized,
                    }
                )
                brief_groups.extend(normalized)
    finally:
        if progress_bar is not None:
            progress_bar.finish()
    artifact["brief_groups"] = list(brief_groups)
    return brief_groups


def _low_priority_existing_entry_candidates(plan: Dict[str, Any]) -> tuple[List[Dict[str, str]], Dict[str, str]]:
    candidates: List[Dict[str, str]] = []
    group_ref_to_id: Dict[str, str] = {}
    for index, group in enumerate(_flat_groups(plan), start=1):
        group_ref = f"G{index:03d}"
        group_id = str(group.get("group_id") or "")
        if not group_id:
            continue
        candidates.append(
            {
                "group_ref": group_ref,
                "slot": str(group.get("slot") or ""),
                "entry_intent": str(group.get("entry_intent") or ""),
            }
        )
        group_ref_to_id[group_ref] = group_id
    return candidates, group_ref_to_id


def _low_priority_candidates_for_batch(
    candidates: Sequence[Dict[str, str]],
    batch: Sequence[Dict[str, Any]],
    *,
    limit: int,
) -> List[Dict[str, str]]:
    if limit <= 0 or len(candidates) <= limit:
        return list(candidates)
    suggested_slots = {str(item.get("suggested_slot") or "") for item in batch if item.get("suggested_slot")}
    batch_text_parts: List[str] = []
    for item in batch:
        batch_text_parts.extend(
            [
                str(item.get("commit_summary") or ""),
                str(item.get("reason") or ""),
                str(item.get("reason_code") or ""),
                to_compact_json(item.get("changed_files_summary") or {}),
            ]
        )
    batch_tokens = _low_priority_candidate_tokens(" ".join(batch_text_parts))

    scored: List[tuple[int, int, Dict[str, str]]] = []
    for index, candidate in enumerate(candidates):
        slot = str(candidate.get("slot") or "")
        candidate_tokens = _low_priority_candidate_tokens(
            " ".join([slot, str(candidate.get("entry_intent") or "")])
        )
        overlap = len(batch_tokens & candidate_tokens)
        slot_score = 8 if slot in suggested_slots else 0
        score = slot_score + overlap
        if score > 0:
            scored.append((score, -index, candidate))

    scored.sort(reverse=True)
    selected = [candidate for _, _, candidate in scored[:limit]]
    if selected:
        return selected
    return list(candidates[:limit])


def _low_priority_candidate_tokens(text: str) -> set[str]:
    raw_tokens = re.findall(r"[A-Za-z0-9_][A-Za-z0-9_./+-]{1,}", str(text or "").lower())
    stop_words = {
        "and",
        "the",
        "for",
        "with",
        "from",
        "this",
        "that",
        "commit",
        "change",
        "changes",
        "update",
        "updates",
        "file",
        "files",
        "documentation",
        "test",
        "tests",
    }
    return {token for token in raw_tokens if token not in stop_words and len(token) >= 2}


def _low_priority_routing_prompt_item(item: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "commit_id": str(item.get("commit_id") or ""),
        "commit_summary": str(item.get("commit_summary") or ""),
        "reason_code": str(item.get("reason_code") or ""),
        "reason": str(item.get("reason") or ""),
        "suggested_slot": str(item.get("suggested_slot") or ""),
        "changed_files_summary": item.get("changed_files_summary") or {},
    }


def _low_priority_brief_prompt_item(item: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "commit_id": str(item.get("commit_id") or ""),
        "commit_summary": str(item.get("commit_summary") or ""),
        "release_note_value": str(item.get("release_note_value") or ""),
        "reason_code": str(item.get("reason_code") or ""),
        "reason": str(item.get("reason") or ""),
        "changed_files_summary": item.get("changed_files_summary") or {},
    }


def _normalize_low_priority_routing_decisions(payload: Dict[str, Any], group_ref_to_id: Dict[str, str]) -> List[Dict[str, Any]]:
    decisions: List[Dict[str, Any]] = []
    for item in payload.get("decisions") or []:
        action = str(item.get("action") or "")
        target_ref = str(item.get("target_group_ref") or "")
        decisions.append(
            {
                "commit_id": str(item.get("commit_id") or ""),
                "action": action,
                "target_group_ref": target_ref,
                "target_group_id": group_ref_to_id.get(target_ref, "") if action == "merge_existing" else "",
                "brief_slot": str(item.get("brief_slot") or ""),
                "reason": str(item.get("reason") or ""),
            }
        )
    return decisions


def _normalize_low_priority_brief_groups(
    payload: Dict[str, Any],
    brief_commits: Sequence[Dict[str, Any]],
    slot: str,
) -> List[Dict[str, Any]]:
    by_id = {str(item.get("commit_id") or ""): item for item in brief_commits}
    groups: List[Dict[str, Any]] = []
    for item in payload.get("brief_groups") or []:
        source_commits = [str(commit_id) for commit_id in item.get("source_commits") or [] if str(commit_id)]
        groups.append(
            {
                "group_id": _low_priority_group_id(slot, source_commits),
                "slot": slot,
                "entry_style": "brief",
                "release_note_value": _release_note_value_for_group(source_commits, by_id),
                "source_commits": source_commits,
                "entry_intent": str(item.get("entry_intent") or ""),
                "aggregation_reason": str(item.get("aggregation_reason") or ""),
            }
        )
    return groups


def _slot_display_name(slot: str) -> str:
    label = _get_slot(RELEASE_NOTE_SCHEMA.get("sections") or {}, slot)
    return str(label or slot)


def apply_low_priority_actions(
    plan: Dict[str, Any],
    actions: Dict[str, Any],
    *,
    cards_by_id: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    normalized = _coerce_plan(plan)
    low_priority_by_id = _low_priority_entries_by_id(normalized)
    if not low_priority_by_id:
        return normalized

    handled: set[str] = set()
    group_by_id = {str(group.get("group_id") or ""): group for group in _flat_groups(normalized)}

    for action in actions.get("merge_actions") or []:
        if not isinstance(action, dict):
            continue
        target_group_id = str(action.get("target_group_id") or "")
        target = group_by_id.get(target_group_id)
        if not target:
            continue
        source_commits = [
            commit_id
            for commit_id in _split_values(action.get("source_commits") or [])
            if commit_id in low_priority_by_id and commit_id not in handled
        ]
        if not source_commits:
            continue
        existing_commits = [str(item) for item in target.get("source_commits") or [] if str(item)]
        target["source_commits"] = _unique(existing_commits + source_commits)
        target["traceability"] = _traceability_for_commits(target["source_commits"], cards_by_id)
        target["entry_style"] = "mixed"
        target.setdefault("release_note_value", "include")
        target.setdefault("low_priority_handling", [])
        target["low_priority_handling"].append(
            {
                "action": "merge_into_existing_group",
                "source_commits": source_commits,
                "merge_note": str(action.get("merge_note") or ""),
                "reason": str(action.get("reason") or ""),
            }
        )
        target["aggregation_reason"] = (
            f"{target.get('aggregation_reason') or ''} Low-priority addition: {action.get('reason') or action.get('merge_note') or ''}"
        ).strip()
        handled.update(source_commits)

    for raw_group in actions.get("brief_groups") or []:
        if not isinstance(raw_group, dict):
            continue
        source_commits = [
            commit_id
            for commit_id in _split_values(raw_group.get("source_commits") or [])
            if commit_id in low_priority_by_id and commit_id not in handled
        ]
        if not source_commits:
            continue
        slot = str(raw_group.get("slot") or "")
        if slot not in SCHEMA_SLOTS:
            slot = _slot_for_low_priority_entry(low_priority_by_id[source_commits[0]], cards_by_id.get(source_commits[0], {}))
        group_id = _ensure_unique_group_id(
            str(raw_group.get("group_id") or _low_priority_group_id(slot, source_commits)),
            group_by_id,
        )
        group = _build_group_from_commit_ids(
            group_id=group_id,
            slot=slot,
            source_commits=source_commits,
            cards_by_id=cards_by_id,
            entry_intent=str(raw_group.get("entry_intent") or _low_priority_fallback_intent([low_priority_by_id[cid] for cid in source_commits])),
            aggregation_reason=str(raw_group.get("aggregation_reason") or "LLM judged that the low-priority commit should be written as a brief release-note entry."),
            related_arch_events=_unique(event for commit_id in source_commits for event in cards_by_id.get(commit_id, {}).get("related_arch_events", [])),
        )
        group["entry_style"] = "brief"
        group["release_note_value"] = _release_note_value_for_group(source_commits, low_priority_by_id)
        group["priority_origin"] = "low_priority_handling"
        group["low_priority_reason_codes"] = _unique(str(low_priority_by_id[cid].get("reason_code") or "") for cid in source_commits)
        _append_group(normalized, slot, group)
        group_by_id[group_id] = group
        handled.update(source_commits)

    missing = [commit_id for commit_id in low_priority_by_id if commit_id not in handled]
    if missing:
        fallback = _fallback_low_priority_actions_for_entries([low_priority_by_id[commit_id] for commit_id in missing], cards_by_id)
        normalized = apply_low_priority_actions(normalized, fallback, cards_by_id=cards_by_id)
        low_priority_by_id = _low_priority_entries_by_id(normalized)
        handled.update(commit_id for commit_id in missing if commit_id not in low_priority_by_id)

    _remove_handled_low_priority_entries(normalized, handled)
    return normalized


def _empty_low_priority_actions() -> Dict[str, Any]:
    return {"brief_groups": [], "merge_actions": []}


def _fallback_low_priority_actions(plan: Dict[str, Any], cards_by_id: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    return _fallback_low_priority_actions_for_entries(list(_low_priority_entries_by_id(plan).values()), cards_by_id)


def _fallback_low_priority_actions_for_entries(
    entries: Sequence[Dict[str, Any]],
    cards_by_id: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    grouped: Dict[tuple[str, str, str], List[Dict[str, Any]]] = defaultdict(list)
    for entry in entries:
        commit_id = str(entry.get("commit_id") or "")
        if not commit_id:
            continue
        card = cards_by_id.get(commit_id, {})
        slot = _slot_for_low_priority_entry(entry, card)
        release_note_value = str(entry.get("release_note_value") or "deprioritize")
        reason_code = str(entry.get("reason_code") or "minor_maintenance")
        grouped[(slot, release_note_value, reason_code)].append(entry)

    brief_groups: List[Dict[str, Any]] = []
    for (slot, release_note_value, reason_code), items in grouped.items():
        source_commits = [str(item.get("commit_id") or "") for item in items if str(item.get("commit_id") or "")]
        if not source_commits:
            continue
        brief_groups.append(
            {
                "group_id": _low_priority_group_id(slot, source_commits, reason_code=reason_code),
                "slot": slot,
                "entry_style": "brief",
                "release_note_value": release_note_value,
                "source_commits": source_commits,
                "entry_intent": _low_priority_fallback_intent(items),
                "aggregation_reason": f"Aggregated by low-priority reason_code={reason_code}  as a brief entry.",
            }
        )
    return {"brief_groups": brief_groups, "merge_actions": []}


def _low_priority_items_for_prompt(
    plan: Dict[str, Any],
    cards_by_id: Dict[str, Dict[str, Any]],
    value_decisions: Sequence[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    decision_by_id = _by_id(value_decisions)
    result: List[Dict[str, Any]] = []
    for entry in _low_priority_entries_by_id(plan).values():
        commit_id = str(entry.get("commit_id") or "")
        card = cards_by_id.get(commit_id, {})
        decision = decision_by_id.get(commit_id, {})
        result.append(
            {
                "commit_id": commit_id,
                "release_note_value": str(entry.get("release_note_value") or decision.get("release_note_value") or "deprioritize"),
                "reason_code": str(entry.get("reason_code") or decision.get("reason_code") or ""),
                "reason": str(entry.get("reason") or decision.get("reason") or ""),
                "suggested_slot": _slot_for_low_priority_entry(entry, card),
                "commit_summary": str(card.get("commit_summary") or ""),
                "changed_files_summary": card.get("changed_files_summary") or {},
            }
        )
    return result


def _low_priority_entries_by_id(plan: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    entries: Dict[str, Dict[str, Any]] = {}
    for value, key in ((DEPRIORITIZE_DECISION, "deprioritized_commits"), (FILTER_DECISION, "filtered_commits")):
        for raw in plan.get(key) or []:
            if not isinstance(raw, dict):
                continue
            commit_id = str(raw.get("commit_id") or "")
            if not commit_id or commit_id in entries:
                continue
            item = dict(raw)
            item["release_note_value"] = value
            entries[commit_id] = item
    return entries


def _group_summaries_from_plan(plan: Dict[str, Any]) -> List[Dict[str, Any]]:
    return [
        {
            "group_id": group.get("group_id"),
            "slot": group.get("slot"),
            "entry_intent": group.get("entry_intent"),
            "entry_style": group.get("entry_style") or "full",
            "release_note_value": group.get("release_note_value") or "include",
            "source_commit_count": len(group.get("source_commits") or []),
        }
        for group in _flat_groups(plan)
    ]


def _slot_for_low_priority_entry(entry: Dict[str, Any], card: Dict[str, Any]) -> str:
    suggested_slot = str(entry.get("suggested_slot") or "")
    if suggested_slot in SCHEMA_SLOTS:
        return suggested_slot
    reason_code = str(entry.get("reason_code") or "")
    decision = {
        "release_note_value": str(entry.get("release_note_value") or DEPRIORITIZE_DECISION),
        "reason_code": reason_code,
        "reason": str(entry.get("reason") or ""),
    }
    if reason_code in {"trivial_docs_only"}:
        return "non_functional_changes.documentation"
    if reason_code in {"formatting_only", "comments_only", "typo_only", "generated_only", "lockfile_only", "version_bump_only", "metadata_only"}:
        return "non_functional_changes.maintenance"
    if reason_code == "duplicate_merge_commit":
        return "others"
    slot = _slot_for_card(card, decision)
    return slot if slot in SCHEMA_SLOTS else "others"


def _low_priority_fallback_intent(entries: Sequence[Dict[str, Any]]) -> str:
    values = {str(entry.get("release_note_value") or "") for entry in entries}
    reason_codes = _unique(str(entry.get("reason_code") or "") for entry in entries)
    count = len([entry for entry in entries if entry.get("commit_id")])
    label_by_reason = {
        "internal_refactoring": "Briefly describe internal refactoring or cleanup without overstating user-visible behavior.",
        "tests_only": "Briefly describe test coverage or test maintenance.",
        "docs_only": "Briefly describe documentation maintenance.",
        "ci_only": "Briefly describe CI or automation maintenance.",
        "dependency_maintenance": "Briefly describe dependency maintenance.",
        "chore": "Briefly describe miscellaneous maintenance.",
        "minor_maintenance": "Briefly describe minor maintenance.",
        "formatting_only": "Briefly describe formatting or style cleanup.",
        "typo_only": "Briefly describe spelling or wording fixes.",
        "comments_only": "Briefly describe comment maintenance.",
        "lockfile_only": "Briefly describe lockfile or dependency-lock maintenance.",
        "generated_only": "Briefly describe generated-file maintenance.",
        "version_bump_only": "Briefly describe version or metadata maintenance.",
        "metadata_only": "Briefly describe metadata maintenance.",
        "duplicate_merge_commit": "Briefly describe merge or synchronization maintenance.",
        "trivial_docs_only": "Briefly describe minor documentation fixes.",
    }
    if len(reason_codes) == 1:
        prefix = label_by_reason.get(reason_codes[0], "Briefly describe low-priority maintenance changes.")
    elif FILTER_DECISION in values and DEPRIORITIZE_DECISION in values:
        prefix = "Briefly describe low-priority maintenance, documentation, or formatting changes."
    else:
        prefix = "Briefly describe low-priority maintenance changes."
    return f"{prefix}({count} commits)。"


def _low_priority_group_id(slot: str, source_commits: Sequence[str], *, reason_code: str = "") -> str:
    head = _short_commit_prefix(source_commits[0]) if source_commits else "unknown"
    code = re.sub(r"[^a-zA-Z0-9_]+", "_", reason_code or "brief")
    return f"brief_{slot.replace('.', '_')}_{code}_{head}"


def _ensure_unique_group_id(group_id: str, group_by_id: Dict[str, Dict[str, Any]]) -> str:
    base = group_id or "brief_group"
    if base not in group_by_id:
        return base
    index = 2
    while f"{base}_{index}" in group_by_id:
        index += 1
    return f"{base}_{index}"


def _release_note_value_for_group(source_commits: Sequence[str], low_priority_by_id: Dict[str, Dict[str, Any]]) -> str:
    values = _unique(str(low_priority_by_id.get(commit_id, {}).get("release_note_value") or "") for commit_id in source_commits)
    if len(values) == 1:
        return values[0]
    return "mixed_low_priority"


def _remove_handled_low_priority_entries(plan: Dict[str, Any], handled: set[str]) -> None:
    if not handled:
        return
    plan["deprioritized_commits"] = [
        item
        for item in plan.get("deprioritized_commits") or []
        if not (isinstance(item, dict) and str(item.get("commit_id") or "") in handled)
    ]
    plan["filtered_commits"] = [
        item
        for item in plan.get("filtered_commits") or []
        if not (isinstance(item, dict) and str(item.get("commit_id") or "") in handled)
    ]


def merge_partial_plans(
    *,
    partial_plans: Sequence[Dict[str, Any]],
    value_decisions: Sequence[Dict[str, Any]],
    cards_by_id: Dict[str, Dict[str, Any]],
    generation_mode: str,
) -> Dict[str, Any]:
    plan = _empty_plan_root(generation_mode)
    for partial in partial_plans:
        for group in partial.get("groups") or []:
            _append_group(plan, group.get("slot") or "others", group)
        plan["deprioritized_commits"].extend(partial.get("deprioritized_commits") or [])
        plan["filtered_commits"].extend(partial.get("filtered_commits") or [])

    assigned = set(_ids_from_plan(plan))
    for decision in value_decisions:
        commit_id = str(decision.get("commit_id") or "")
        if not commit_id or commit_id in assigned:
            continue
        card = cards_by_id.get(commit_id)
        if not card:
            continue
        if decision.get("release_note_value") == FILTER_DECISION:
            plan["filtered_commits"].append(_filtered_entry(card, decision))
            assigned.add(commit_id)
    return plan


def apply_group_review_actions(
    plan: Dict[str, Any],
    actions: Dict[str, Any],
    *,
    cards_by_id: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    groups = _flat_groups(plan)
    group_by_id = {group["group_id"]: group for group in groups}
    consumed: set[str] = set()
    next_groups: List[Dict[str, Any]] = []

    for action in actions.get("merge_actions") or []:
        source_ids = [gid for gid in action.get("source_group_ids") or [] if gid in group_by_id and gid not in consumed]
        if len(source_ids) < 2:
            continue
        slot = action.get("new_slot") if action.get("new_slot") in SCHEMA_SLOTS else group_by_id[source_ids[0]].get("slot")
        source_groups = [group_by_id[group_id] for group_id in source_ids]
        source_commits = _unique(commit for group in source_groups for commit in group.get("source_commits") or [])
        merged_group = _build_group_from_commit_ids(
            group_id=str(action.get("new_group_id") or f"MERGED-{len(next_groups) + 1:03d}"),
            slot=slot or "others",
            source_commits=source_commits,
            cards_by_id=cards_by_id,
            entry_intent="；".join(str(group.get("entry_intent") or "") for group in source_groups if group.get("entry_intent"))[:500],
            aggregation_reason=str(action.get("reason") or "Global review suggested merging these groups."),
            related_arch_events=_unique(event for group in source_groups for event in group.get("related_arch_events") or []),
        )
        next_groups.append(merged_group)
        consumed.update(source_ids)

    move_by_id = {
        action.get("group_id"): action
        for action in actions.get("move_actions") or []
        if action.get("group_id") in group_by_id and action.get("new_slot") in SCHEMA_SLOTS
    }
    for group in groups:
        group_id = group.get("group_id")
        if group_id in consumed:
            continue
        if group_id in move_by_id:
            moved = dict(group)
            moved["slot"] = move_by_id[group_id]["new_slot"]
            moved["aggregation_reason"] = f"{moved.get('aggregation_reason') or ''} Global review move reason: {move_by_id[group_id].get('reason') or ''}".strip()
            next_groups.append(moved)
        else:
            next_groups.append(group)

    rebuilt = _empty_plan_root(str(plan.get("generation_mode") or "llm_multi_stage"))
    rebuilt["deprioritized_commits"] = list(plan.get("deprioritized_commits") or [])
    rebuilt["filtered_commits"] = list(plan.get("filtered_commits") or [])
    rebuilt["warnings"] = list(plan.get("warnings") or [])
    for group in next_groups:
        _append_group(rebuilt, group.get("slot") or "others", group)
    return rebuilt


def repair_coverage_with_llm(
    *,
    plan: Dict[str, Any],
    problem_commit_ids: Sequence[str],
    cards_by_id: Dict[str, Dict[str, Any]],
    llm_client,
    rate_limiter: TokenBucketRateLimiter,
    config,
    audit: Dict[str, Any],
) -> Dict[str, Any]:
    if not problem_commit_ids:
        return {"repair_actions": []}
    problem_cards = [cards_by_id[commit_id] for commit_id in problem_commit_ids if commit_id in cards_by_id]
    id_map = _build_phase3_llm_commit_id_map(
        _unique(list(problem_commit_ids) + _ids_from_plan(plan)),
        config,
    )
    prompt_plan_summary = _shorten_commit_ids_for_llm(_aggregation_plan_summary(plan), id_map)
    prompt_problem_commit_ids = _map_phase3_commit_ref_list(list(problem_commit_ids), id_map, direction="to_short")
    prompt_problem_cards = _shorten_commit_ids_for_llm(_value_prompt_cards(problem_cards), id_map)

    def validate_payload(parsed: Dict[str, Any]) -> None:
        _restore_commit_ids_from_llm(parsed, id_map)

    progress_bar = progress_bar_for(config, "Phase3.1 coverage repair progress")
    if progress_bar is not None:
        progress_bar.update(completed=0, total=1)
    try:
        with suppress_noisy_llm_loggers(enabled=progress_bar is not None):
            payload = _call_json_stage(
                stage="phase3.1.6:coverage_repair",
                prompt_path=COVERAGE_REPAIR_PROMPT,
                target_json_type="coverage_repair",
                target_schema={"repair_actions": []},
                values={
                    "aggregation_plan_summary_json": to_compact_json(prompt_plan_summary),
                    "problem_commits_json": to_compact_json(prompt_problem_commit_ids),
                    "problem_commit_cards_json": to_compact_json(prompt_problem_cards),
                },
                llm_client=llm_client,
                rate_limiter=rate_limiter,
                config=config,
                audit=audit,
                request_suffix="coverage",
                debug_context={
                    "input_summary": {"problem_commit_count": len(problem_commit_ids)},
                    "input_payload": {
                        "aggregation_plan_summary": prompt_plan_summary,
                        "problem_commits": prompt_problem_commit_ids,
                        "problem_commit_cards": prompt_problem_cards,
                    },
                    "commit_id_map": _phase3_llm_commit_id_map_debug(id_map),
                },
                validate_fn=validate_payload,
            )
            if progress_bar is not None:
                progress_bar.update(completed=1, total=1)
    finally:
        if progress_bar is not None:
            progress_bar.finish()
    payload = _restore_commit_ids_from_llm(payload, id_map)
    return _normalize_coverage_repair_actions(payload, problem_commit_ids, cards_by_id)


def apply_coverage_repair_actions(
    plan: Dict[str, Any],
    repair_actions: Dict[str, Any],
    *,
    cards_by_id: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    repaired = _coerce_plan(plan)
    group_by_id = {group["group_id"]: group for group in _flat_groups(repaired)}
    for action in repair_actions.get("repair_actions") or []:
        commit_id = str(action.get("commit_id") or "")
        if commit_id not in cards_by_id:
            continue
        name = str(action.get("action") or "")
        if name == "add_to_existing_group":
            target = group_by_id.get(str(action.get("target_group_id") or ""))
            if target and commit_id not in target.get("source_commits", []):
                target.setdefault("source_commits", []).append(commit_id)
                target["traceability"] = _traceability_for_commits(target["source_commits"], cards_by_id)
        elif name == "create_new_group":
            raw_group = action.get("new_group") if isinstance(action.get("new_group"), dict) else {}
            slot = raw_group.get("slot") if raw_group.get("slot") in SCHEMA_SLOTS else _slot_for_card(cards_by_id[commit_id])
            group = _build_group_from_commit_ids(
                group_id=str(raw_group.get("group_id") or f"REPAIR-{_short_commit_prefix(commit_id)}"),
                slot=slot,
                source_commits=[commit_id],
                cards_by_id=cards_by_id,
                entry_intent=str(raw_group.get("entry_intent") or cards_by_id[commit_id].get("commit_summary") or ""),
                aggregation_reason=str(raw_group.get("aggregation_reason") or action.get("reason") or "coverage repair"),
                related_arch_events=raw_group.get("related_arch_events") or cards_by_id[commit_id].get("related_arch_events") or [],
            )
            _append_group(repaired, slot, group)
        elif name == "add_to_deprioritized":
            entry = action.get("deprioritized_commit") if isinstance(action.get("deprioritized_commit"), dict) else {}
            entry["commit_id"] = commit_id
            repaired["deprioritized_commits"].append(_deprioritized_entry(cards_by_id[commit_id], entry))
        elif name == "add_to_filtered":
            entry = action.get("filtered_commit") if isinstance(action.get("filtered_commit"), dict) else {}
            entry["commit_id"] = commit_id
            repaired["filtered_commits"].append(_filtered_entry(cards_by_id[commit_id], entry))
    return repaired


def validate_aggregation_plan(
    plan: Dict[str, Any],
    all_commit_ids: Iterable[str],
    records: Optional[Sequence[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    all_ids = _unique([str(commit_id) for commit_id in all_commit_ids if str(commit_id)])
    valid_commits = set(all_ids)
    card_source = build_commit_cards(records or [])
    cards_by_id = _cards_by_id(card_source)
    normalized = _coerce_plan(plan)
    warnings = [str(item) for item in normalized.get("warnings") or [] if str(item)]

    groups = _empty_groups()
    included_ids: List[str] = []
    included_seen: set[str] = set()
    duplicated_ids: List[str] = []
    for slot in SCHEMA_SLOTS:
        next_groups: List[Dict[str, Any]] = []
        for raw_group in _get_slot(normalized.get("groups") or {}, slot) or []:
            if not isinstance(raw_group, dict):
                warnings.append(f"Dropped non-object group in {slot}.")
                continue
            source_commits: List[str] = []
            for raw_commit in _split_values(raw_group.get("source_commits") or []):
                commit_id = _resolve_commit_prefix(raw_commit, valid_commits)
                if not commit_id:
                    warnings.append(f"Dropped unknown source commit `{raw_commit}` from {slot}.")
                    continue
                if commit_id in included_seen:
                    warnings.append(f"Commit `{commit_id}` appeared in multiple included groups; kept first group.")
                    duplicated_ids.append(commit_id)
                    continue
                source_commits.append(commit_id)
                included_seen.add(commit_id)
            source_commits = _unique(source_commits)
            if not source_commits:
                warnings.append(f"Dropped group in {slot} because it has no valid source_commits.")
                continue
            group = dict(raw_group)
            group["slot"] = slot
            group["source_commits"] = source_commits
            group.setdefault("group_id", _make_group_id(slot, source_commits, index=len(next_groups) + 1))
            group.setdefault("entry_intent", _fallback_intent([cards_by_id.get(cid, {"commit_id": cid}) for cid in source_commits], slot))
            group.setdefault("related_arch_events", _unique(event for cid in source_commits for event in cards_by_id.get(cid, {}).get("related_arch_events", [])))
            group.setdefault("primary_module", _first_nonempty(cards_by_id.get(cid, {}).get("primary_module") for cid in source_commits) or "unknown")
            group.setdefault("primary_component", _first_nonempty(cards_by_id.get(cid, {}).get("primary_component") for cid in source_commits) or "unknown")
            group.setdefault("aggregation_reason", "Normalization retained this aggregation group.")
            group.setdefault("entry_style", "full")
            group.setdefault("release_note_value", "include")
            group["traceability"] = _traceability_for_commits(source_commits, cards_by_id)
            next_groups.append(group)
            included_ids.extend(source_commits)
        _set_slot(groups, slot, next_groups)

    deprioritized: List[Dict[str, Any]] = []
    deprioritized_ids: List[str] = []
    for raw_entry in normalized.get("deprioritized_commits") or []:
        commit_id = _resolve_commit_prefix(str(raw_entry.get("commit_id") or ""), valid_commits) if isinstance(raw_entry, dict) else ""
        if not commit_id:
            warnings.append("Dropped invalid deprioritized commit entry.")
            continue
        if commit_id in included_seen:
            warnings.append(f"Commit `{commit_id}` appeared in included and deprioritized; kept included.")
            duplicated_ids.append(commit_id)
            continue
        if commit_id in deprioritized_ids:
            warnings.append(f"Duplicate deprioritized commit `{commit_id}` removed.")
            duplicated_ids.append(commit_id)
            continue
        deprioritized.append(_deprioritized_entry(cards_by_id.get(commit_id, {"commit_id": commit_id}), raw_entry))
        deprioritized_ids.append(commit_id)

    deprioritized_set = set(deprioritized_ids)
    filtered: List[Dict[str, Any]] = []
    filtered_ids: List[str] = []
    for raw_entry in normalized.get("filtered_commits") or []:
        commit_id = _resolve_commit_prefix(str(raw_entry.get("commit_id") or ""), valid_commits) if isinstance(raw_entry, dict) else ""
        if not commit_id:
            warnings.append("Dropped invalid filtered commit entry.")
            continue
        if commit_id in included_seen:
            warnings.append(f"Commit `{commit_id}` appeared in included and filtered; kept included.")
            duplicated_ids.append(commit_id)
            continue
        if commit_id in deprioritized_set:
            warnings.append(f"Commit `{commit_id}` appeared in deprioritized and filtered; kept deprioritized.")
            duplicated_ids.append(commit_id)
            continue
        if commit_id in filtered_ids:
            warnings.append(f"Duplicate filtered commit `{commit_id}` removed.")
            duplicated_ids.append(commit_id)
            continue
        filtered.append(_filtered_entry(cards_by_id.get(commit_id, {"commit_id": commit_id}), raw_entry))
        filtered_ids.append(commit_id)

    assigned = set(included_ids) | set(deprioritized_ids) | set(filtered_ids)
    unassigned = [commit_id for commit_id in all_ids if commit_id not in assigned]
    normalized["groups"] = groups
    normalized["deprioritized_commits"] = deprioritized
    normalized["filtered_commits"] = filtered
    normalized["warnings"] = warnings
    normalized["coverage_report"] = {
        "total_commits": len(all_ids),
        "included_commits": len(set(included_ids)),
        "deprioritized_commits": len(deprioritized_ids),
        "filtered_commits": len(filtered_ids),
        "unassigned_commits": unassigned,
        "duplicated_commits": _ordered_unique(duplicated_ids, all_ids),
        "included_commit_ids": _ordered_unique(included_ids, all_ids),
        "deprioritized_commit_ids": _ordered_unique(deprioritized_ids, all_ids),
        "filtered_commit_ids": _ordered_unique(filtered_ids, all_ids),
    }
    return normalized


def fallback_assign_unassigned_commits(
    unassigned_records: Sequence[Dict[str, Any]],
    plan: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    cards = build_commit_cards(unassigned_records)
    target = _coerce_plan(plan or _empty_plan_root("fallback"))
    _fallback_assign_missing_into_plan(target, cards)
    known_ids = _ids_from_plan(target) + [card["commit_id"] for card in cards]
    return validate_aggregation_plan(target, known_ids, unassigned_records)


def classify_release_note_value(record: Dict[str, Any]) -> Dict[str, Any]:
    card = record if "changed_files_summary" in record else build_commit_cards([record])[0]
    decision = _deterministic_value_decision(card)
    return {
        "decision": decision["release_note_value"],
        "reason_code": decision["reason_code"],
        "reason": decision["reason"],
        "confidence": 0.8,
    }


def _append_audit_call(audit: Dict[str, Any], call_record: Dict[str, Any]) -> None:
    with _AUDIT_LOCK:
        audit.setdefault("calls", []).append(call_record)


def _mark_audit_llm_used(audit: Dict[str, Any]) -> None:
    with _AUDIT_LOCK:
        audit["llm_used"] = True


def _append_audit_error(audit: Dict[str, Any], error_record: Dict[str, Any]) -> None:
    with _AUDIT_LOCK:
        audit.setdefault("errors", []).append(error_record)


def call_llm_json_or_fail(
    stage_name: str,
    prompt: str,
    target_schema_name: str,
    context: Dict[str, Any],
    parse_fn: Callable[[str], Dict[str, Any]],
    validate_fn: Optional[Callable[[Dict[str, Any]], None]] = None,
) -> Dict[str, Any]:
    config = context.get("config")
    audit = context.get("audit") or {}
    call_record = context.get("call_record")
    base_request_name = context.get("request_name") or f"{stage_name}:{context.get('request_suffix', '')}"
    validation_attempts: List[Dict[str, Any]] = []
    llm_call_metrics: List[Dict[str, Any]] = []
    previous_error: Optional[BaseException] = None
    for retry_index in range(llm_output_validation_max_retries(config) + 1):
        raw: Optional[str] = None
        parsed: Optional[Dict[str, Any]] = None
        llm_metrics: Dict[str, Any] = {}
        current_prompt = prompt if retry_index == 0 else _validation_retry_prompt(prompt, previous_error)
        current_request_name = base_request_name if retry_index == 0 else f"{base_request_name}:validation_retry{retry_index}"
        try:
            raw, llm_metrics = generate_chat_completion_with_retry(
                config=config,
                llm_client=context["llm_client"],
                system_prompt=context.get("system_prompt") or "You are a structured JSON output assistant. Return only valid JSON.",
                user_prompt=current_prompt,
                request_name=current_request_name,
                rate_limiter=context.get("rate_limiter"),
                max_tokens=context.get("max_tokens"),
            )
            llm_metrics = mark_llm_metric_attempt(
                normalize_llm_metrics(llm_metrics),
                validation_attempt_count=retry_index + 1,
                is_validation_retry=retry_index > 0,
            )
            _mark_audit_llm_used(audit)
            parsed = parse_fn(raw)
            if validate_fn is not None:
                validate_fn(parsed)
            if validation_attempts:
                validation_attempts.append(
                    {
                        "attempt": retry_index + 1,
                        "request_name": current_request_name,
                        "result": "succeeded",
                        "raw_llm_response": raw,
                        "parsed_json_if_any": parsed,
                        "error_message": "",
                        "llm_metrics": llm_metrics,
                    }
                )
            llm_call_metrics.append(llm_metrics)
            if call_record is not None:
                call_record["raw_response"] = raw
                call_record["ok"] = True
                call_record["validation_attempts"] = validation_attempts
                call_record["llm_metrics"] = llm_metrics
                call_record["llm_call_metrics"] = llm_call_metrics
            return parsed
        except Exception as exc:
            error_type = _phase3_stage_error_type(exc, parsed, raw)
            candidate_metrics = normalize_llm_metrics(llm_metrics or getattr(exc, "llm_metrics", {}))
            failed_metric = {}
            if candidate_metrics:
                failed_metric = mark_llm_metric_attempt(
                    candidate_metrics,
                    validation_attempt_count=retry_index + 1,
                    is_validation_retry=retry_index > 0,
                    success=False,
                    error_type=error_type,
                    error_message=str(exc),
                )
                llm_call_metrics.append(failed_metric)
            previous_error = exc
            should_retry_validation = (
                retry_index < llm_output_validation_max_retries(config)
                and not _phase3_is_llm_request_failure(exc, raw, parsed)
            )
            validation_attempts.append(
                {
                    "attempt": retry_index + 1,
                    "request_name": current_request_name,
                    "result": "retry_scheduled" if should_retry_validation else "failed",
                    "raw_llm_response": raw or "",
                    "parsed_json_if_any": parsed or {},
                    "error_type": error_type,
                    "error_message": str(exc),
                    "llm_metrics": failed_metric,
                }
            )
            if should_retry_validation:
                continue
            if call_record is not None:
                call_record["raw_response"] = raw
                call_record["error_message"] = str(exc)
                call_record["validation_attempts"] = validation_attempts
                call_record["llm_metrics"] = failed_metric
                call_record["llm_call_metrics"] = llm_call_metrics
            _raise_phase3_stage_failure(
                config=config,
                audit=audit,
                stage=stage_name,
                request_suffix=str(context.get("request_suffix") or ""),
                error_type=error_type,
                error_message=str(exc),
                exception=exc,
                prompt_path=Path(context.get("prompt_template_path") or ""),
                user_prompt=current_prompt,
                raw=raw or "",
                parsed=parsed,
                debug_context=context.get("debug_context") or {},
                validation_attempts=validation_attempts,
            )
    raise AssertionError("unreachable")


def _call_json_stage(
    *,
    stage: str,
    prompt_path: Path,
    target_json_type: str,
    target_schema: Dict[str, Any],
    values: Dict[str, str],
    llm_client,
    rate_limiter: TokenBucketRateLimiter,
    config,
    audit: Dict[str, Any],
    request_suffix: str,
    debug_context: Optional[Dict[str, Any]] = None,
    validate_fn=None,
) -> Dict[str, Any]:
    user_prompt = render_prompt_template(load_prompt_text(prompt_path), values)
    system_prompt = "You are a structured release-note planning assistant. Return only valid JSON."
    call_record: Dict[str, Any] = {
        "stage": stage,
        "request_suffix": request_suffix,
        "prompt_path": str(prompt_path),
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
        "raw_response": None,
        "validation_attempts": [],
        "ok": False,
        "error_message": None,
    }
    _append_audit_call(audit, call_record)
    return call_llm_json_or_fail(
        stage_name=stage,
        prompt=user_prompt,
        target_schema_name=target_json_type,
        context={
            "config": config,
            "audit": audit,
            "llm_client": llm_client,
            "rate_limiter": rate_limiter,
            "system_prompt": system_prompt,
            "request_name": f"{stage}:{request_suffix}",
            "request_suffix": request_suffix,
            "prompt_template_path": str(prompt_path),
            "max_tokens": max(2200, int(getattr(config, "llm_max_tokens", 0) or 0)),
            "call_record": call_record,
            "debug_context": debug_context,
        },
        parse_fn=_loads_json_strict,
        validate_fn=validate_fn,
    )


def _loads_json_strict(raw_text: str) -> Dict[str, Any]:
    return parse_json_response_strict(raw_text)


def _validation_retry_prompt(user_prompt: str, error: Optional[BaseException]) -> str:
    error_message = str(error or "output validation failed")
    error_message = re.sub(r"\b[0-9a-fA-F]{40}\b", "<internal_commit_id>", error_message)[:600]
    return (
        user_prompt
        + "\n\nThe previous response failed validation: "
        + error_message
        + "\nGenerate the response again from the same input. Return only valid JSON, copy only the short commit_id values shown in the input, and cover every required item exactly once."
    )


def _phase3_stage_error_type(
    exc: BaseException,
    parsed: Optional[Dict[str, Any]],
    raw: Optional[str] = None,
) -> str:
    if _phase3_is_llm_request_failure(exc, raw, parsed):
        return _phase3_llm_request_error_type(exc)
    if parsed is None:
        return "json_parse_error"
    message = str(exc).lower()
    if any(token in message for token in ("mismatch", "unknown", "missing", "duplicate", "source commit", "group_id")):
        return "source_backed_validation_error"
    if "coverage" in message:
        return "coverage_validation_error"
    return "schema_validation_error"


def _phase3_is_llm_request_failure(
    exc: BaseException,
    raw: Optional[str],
    parsed: Optional[Dict[str, Any]],
) -> bool:
    """Return True when the request itself failed before a model response existed."""
    if parsed is not None:
        return False
    if raw not in (None, ""):
        return False
    if _looks_like_llm_api_exception(exc):
        return True
    return False


def _looks_like_llm_api_exception(exc: BaseException) -> bool:
    exc_type = type(exc)
    module = str(getattr(exc_type, "__module__", "") or "").lower()
    name = str(getattr(exc_type, "__name__", "") or "").lower()
    if module.startswith("openai") or module.startswith("httpx") or module.startswith("httpcore"):
        return True
    if hasattr(exc, "status_code") or hasattr(exc, "response") or hasattr(exc, "request"):
        return True
    api_exception_tokens = (
        "apierror",
        "apistatuserror",
        "apiconnectionerror",
        "apitimeouterror",
        "authenticationerror",
        "permissiondeniederror",
        "ratelimiterror",
        "badrequesterror",
        "internalservererror",
        "timeout",
        "connection",
    )
    return any(token in name for token in api_exception_tokens)


def _phase3_llm_request_error_type(exc: BaseException) -> str:
    name = str(getattr(type(exc), "__name__", "") or "").lower()
    message = str(exc).lower()
    status_code = getattr(exc, "status_code", None)
    if status_code in (401, 403) or any(token in name + " " + message for token in ("permission", "authentication", "unauthorized", "forbidden")):
        return "llm_permission_error"
    if status_code == 429 or "rate limit" in message or "ratelimit" in name:
        return "llm_rate_limit_error"
    if any(token in name + " " + message for token in ("timeout", "connection", "connect", "network")):
        return "llm_transport_error"
    return "llm_api_error"


def _raise_phase3_stage_failure(
    *,
    config,
    audit: Dict[str, Any],
    stage: str,
    request_suffix: str,
    error_type: str,
    error_message: str,
    exception: BaseException,
    prompt_path: Path,
    user_prompt: str,
    raw: str,
    parsed: Optional[Dict[str, Any]],
    debug_context: Optional[Dict[str, Any]],
    validation_attempts: Optional[List[Dict[str, Any]]] = None,
) -> None:
    context = debug_context or {}
    raise_phase3_llm_failure(
        output_dir=phase3_failure_output_dir(config, Path(audit.get("output_dir") or ".")),
        stage=stage,
        batch_or_bucket_or_slot=request_suffix,
        error_type=error_type,
        error_message=error_message,
        exception=exception,
        prompt_template_path=str(prompt_path),
        rendered_prompt=user_prompt,
        raw_llm_response=raw,
        cleaned_response_if_any=(raw or "").strip(),
        parsed_json_if_any=parsed or {},
        input_summary=context.get("input_summary") or {},
        input_payload=context.get("input_payload") or {},
        validation_attempts=validation_attempts or [],
    )


def _raise_phase3_coverage_failure(
    *,
    config,
    audit: Dict[str, Any],
    plan: Dict[str, Any],
    all_commit_ids: Sequence[str],
    stage: str,
    context_name: str,
    ) -> None:
    coverage = plan.get("coverage_report") or {}
    raise_phase3_llm_failure(
        output_dir=phase3_failure_output_dir(config, Path(audit.get("output_dir") or ".")),
        stage=stage,
        batch_or_bucket_or_slot=context_name,
        error_type="coverage_validation_error",
        error_message=(
            "aggregation_plan coverage validation failed: "
            f"unassigned={coverage.get('unassigned_commits') or []}, "
            f"duplicated={coverage.get('duplicated_commits') or []}"
        ),
        prompt_template_path="",
        rendered_prompt="",
        raw_llm_response="",
        cleaned_response_if_any="",
        parsed_json_if_any={"coverage_report": coverage},
        input_summary={
            "commit_count": len(all_commit_ids),
            "unassigned_count": len(coverage.get("unassigned_commits") or []),
            "duplicated_count": len(coverage.get("duplicated_commits") or []),
        },
        input_payload={"all_commit_ids": list(all_commit_ids), "aggregation_plan": plan},
    )


def _coverage_has_fail_fast_errors(coverage: Dict[str, Any]) -> bool:
    return bool((coverage or {}).get("unassigned_commits") or (coverage or {}).get("duplicated_commits"))


def _validate_value_payload(payload: Dict[str, Any], expected_commit_ids: Sequence[str]) -> None:
    _validate_exact_commit_items(payload.get("decisions"), expected_commit_ids, "decisions")
    for item in payload.get("decisions") or []:
        value = str(item.get("release_note_value") or "")
        if value not in VALUE_ENUM:
            raise ValueError(f"Invalid release_note_value for {item.get('commit_id')}: {value}")


def _validate_slot_assignment_payload(payload: Dict[str, Any], expected_commit_ids: Sequence[str]) -> None:
    items = payload.get("assignments")
    if items is None:
        items = payload.get("slot_assignments")
    _validate_exact_commit_items(items, expected_commit_ids, "assignments")
    for item in items or []:
        slot = _normalize_slot_name(str(item.get("slot") or item.get("primary_slot") or ""))
        if slot not in SCHEMA_SLOTS:
            raise ValueError(f"Invalid slot for {item.get('commit_id')}: {slot}")


def _validate_bucket_payload(payload: Dict[str, Any], bucket: Dict[str, Any]) -> None:
    _coerce_bucket_payload_commit_ids(payload, bucket)
    valid_ids = set(str(item) for item in bucket.get("commit_ids") or [])
    assigned: List[str] = []
    for group in payload.get("groups") or []:
        if not isinstance(group, dict):
            raise ValueError("groups must contain JSON objects.")
        source_commits = group.get("source_commits")
        if not isinstance(source_commits, list) or not source_commits:
            raise ValueError("Each bucket group must contain non-empty source_commits.")
        assigned.extend(str(item) for item in source_commits)
    for key in ("deprioritized", "deprioritized_commits", "filtered", "filtered_commits"):
        for item in payload.get(key) or []:
            if not isinstance(item, dict):
                raise ValueError(f"{key} must contain JSON objects.")
            assigned.append(str(item.get("commit_id") or ""))
    _validate_exact_ids(assigned, list(valid_ids), "bucket commit assignment")


def _validate_group_review_payload(payload: Dict[str, Any], group_summaries: Sequence[Dict[str, Any]]) -> None:
    valid_group_ids = {str(summary.get("group_id") or "") for summary in group_summaries}
    group_slot_by_id = _group_slot_by_id(group_summaries)
    if "actions" in payload:
        for item in payload.get("actions") or []:
            if not isinstance(item, dict):
                raise ValueError("actions must contain JSON objects.")
            action = str(item.get("action") or "")
            if action not in {"merge", "move", "keep"}:
                raise ValueError(f"Invalid group review action: {action}")
            group_ids = [str(group_id) for group_id in item.get("group_ids") or []]
            for group_id in group_ids:
                if group_id not in valid_group_ids:
                    raise ValueError(f"Unknown group_id in group review: {group_id}")
            new_slot = _resolve_group_review_new_slot(action, str(item.get("new_slot") or ""), group_ids, group_slot_by_id)
            if action in {"merge", "move"} and new_slot not in SCHEMA_SLOTS:
                raise ValueError(f"Invalid new_slot in group review: {item.get('new_slot')}")
        return
    for key in ("merge_actions", "move_actions", "keep_actions"):
        if key not in payload:
            raise ValueError("Group review payload must contain actions or legacy action arrays.")


def _validate_low_priority_routing_payload(
    payload: Dict[str, Any],
    deprioritized_commits: Sequence[Dict[str, Any]],
    group_ref_to_id: Dict[str, str],
) -> None:
    if not isinstance(payload, dict) or set(payload) != {"decisions"}:
        raise ValueError("Low-priority routing payload must contain only decisions.")
    decisions = payload.get("decisions")
    if not isinstance(decisions, list):
        raise ValueError("Low-priority routing decisions must be a list.")
    expected_ids = [
        str(item.get("commit_id") or "")
        for item in deprioritized_commits
        if str(item.get("commit_id") or "")
    ]
    _validate_exact_commit_items(decisions, expected_ids, "low-priority routing decisions")
    required_fields = {"commit_id", "action", "target_group_ref", "brief_slot", "reason"}
    for decision in decisions:
        if not isinstance(decision, dict) or set(decision) != required_fields:
            raise ValueError("Each low-priority routing decision must contain only commit_id, action, target_group_ref, brief_slot, and reason.")
        commit_id = str(decision.get("commit_id") or "")
        action = str(decision.get("action") or "")
        target_group_ref = str(decision.get("target_group_ref") or "")
        brief_slot = str(decision.get("brief_slot") or "")
        reason = str(decision.get("reason") or "").strip()
        if not reason:
            raise ValueError(f"Low-priority routing reason is empty for commit: {commit_id}")
        if action == "merge_existing":
            if target_group_ref not in group_ref_to_id:
                raise ValueError(f"Unknown target_group_ref in low-priority routing: {target_group_ref}")
            if brief_slot:
                raise ValueError(f"merge_existing cannot provide brief_slot for commit: {commit_id}")
            continue
        if action == "create_brief":
            if target_group_ref:
                raise ValueError(f"create_brief cannot provide target_group_ref for commit: {commit_id}")
            if brief_slot not in SCHEMA_SLOTS:
                raise ValueError(f"Invalid low-priority routing brief_slot for {commit_id}: {brief_slot}")
            continue
        raise ValueError(f"Invalid low-priority routing action for {commit_id}: {action}")


def _validate_low_priority_brief_payload(
    payload: Dict[str, Any],
    brief_commits: Sequence[Dict[str, Any]],
) -> None:
    if not isinstance(payload, dict) or set(payload) != {"brief_groups"}:
        raise ValueError("Low-priority brief grouping payload must contain only brief_groups.")
    brief_groups = payload.get("brief_groups")
    if not isinstance(brief_groups, list) or not brief_groups:
        raise ValueError("Low-priority brief grouping must contain at least one brief_group.")
    expected_ids = [
        str(item.get("commit_id") or "")
        for item in brief_commits
        if str(item.get("commit_id") or "")
    ]
    assigned: List[str] = []
    required_fields = {"source_commits", "entry_intent", "aggregation_reason"}
    for group in brief_groups:
        if not isinstance(group, dict) or set(group) != required_fields:
            raise ValueError("Each brief_group must contain only source_commits, entry_intent, and aggregation_reason.")
        source_commits = group.get("source_commits")
        if not isinstance(source_commits, list) or not source_commits:
            raise ValueError("Each brief_group must contain non-empty source_commits.")
        if not str(group.get("entry_intent") or "").strip():
            raise ValueError("Each brief_group must contain a non-empty entry_intent.")
        if not str(group.get("aggregation_reason") or "").strip():
            raise ValueError("Each brief_group must contain a non-empty aggregation_reason.")
        assigned.extend(str(item) for item in source_commits)
    _validate_exact_ids(assigned, expected_ids, "low-priority brief grouping")


def _validate_low_priority_payload(
    payload: Dict[str, Any],
    low_priority_commits: Sequence[Dict[str, Any]],
    plan: Dict[str, Any],
) -> None:
    if not isinstance(payload, dict):
        raise ValueError("Low-priority handling payload must be a JSON object.")
    valid_ids = [str(item.get("commit_id") or "") for item in low_priority_commits if str(item.get("commit_id") or "")]
    valid_set = set(valid_ids)
    existing_group_ids = {str(group.get("group_id") or "") for group in _flat_groups(plan)}
    assigned: List[str] = []

    brief_groups = payload.get("brief_groups")
    if brief_groups is None:
        brief_groups = []
    if not isinstance(brief_groups, list):
        raise ValueError("brief_groups must be a list.")
    for group in brief_groups:
        if not isinstance(group, dict):
            raise ValueError("brief_groups must contain JSON objects.")
        slot = str(group.get("slot") or "")
        if slot not in SCHEMA_SLOTS:
            raise ValueError(f"Invalid low-priority slot: {slot}")
        source_commits = group.get("source_commits")
        if not isinstance(source_commits, list) or not source_commits:
            raise ValueError("Each brief_group must contain non-empty source_commits.")
        assigned.extend(str(item) for item in source_commits)

    merge_actions = payload.get("merge_actions")
    if merge_actions is None:
        merge_actions = []
    if not isinstance(merge_actions, list):
        raise ValueError("merge_actions must be a list.")
    for action in merge_actions:
        if not isinstance(action, dict):
            raise ValueError("merge_actions must contain JSON objects.")
        target_group_id = str(action.get("target_group_id") or "")
        if target_group_id not in existing_group_ids:
            raise ValueError(f"Unknown target_group_id in low-priority merge action: {target_group_id}")
        source_commits = action.get("source_commits")
        if not isinstance(source_commits, list) or not source_commits:
            raise ValueError("Each merge_action must contain non-empty source_commits.")
        assigned.extend(str(item) for item in source_commits)

    if not brief_groups and not merge_actions and valid_ids:
        raise ValueError("Low-priority handling must assign every low-priority commit.")
    _validate_exact_ids(assigned, list(valid_set), "low-priority commit handling")


def _validate_exact_commit_items(items: Any, expected_commit_ids: Sequence[str], label: str) -> None:
    if not isinstance(items, list):
        raise ValueError(f"{label} must be a list.")
    ids = [str(item.get("commit_id") or "") for item in items if isinstance(item, dict)]
    _validate_exact_ids(ids, expected_commit_ids, label)


def _validate_exact_ids(actual_ids: Sequence[str], expected_ids: Sequence[str], label: str) -> None:
    actual = [item for item in actual_ids if item]
    expected = [str(item) for item in expected_ids if str(item)]
    actual_set = set(actual)
    expected_set = set(expected)
    duplicates = sorted({item for item in actual if actual.count(item) > 1})
    missing = [item for item in expected if item not in actual_set]
    unknown = [item for item in actual if item not in expected_set]
    if duplicates or missing or unknown:
        raise ValueError(
            f"{label} mismatch: duplicates={duplicates}, missing={missing}, unknown={unknown}"
        )


def _coerce_bucket_payload_commit_ids(payload: Dict[str, Any], bucket: Dict[str, Any]) -> None:
    if not isinstance(payload, dict):
        return

    valid_ids = [str(item) for item in bucket.get("commit_ids") or [] if str(item)]
    valid_set = set(valid_ids)
    assigned: set[str] = set()

    def resolve(raw_value: Any) -> str:
        raw = str(raw_value or "").strip()
        if not raw:
            return ""

        resolved = _resolve_commit_prefix(raw, valid_set)
        if resolved:
            return resolved

        if not re.fullmatch(r"[0-9a-fA-F]{12,80}", raw):
            return ""

        raw_lower = raw.lower()
        ranked = sorted(
            (
                (SequenceMatcher(None, raw_lower, commit_id.lower()).ratio(), commit_id)
                for commit_id in valid_ids
            ),
            reverse=True,
        )
        if not ranked:
            return ""

        best_score, best_id = ranked[0]
        second_score = ranked[1][0] if len(ranked) > 1 else 0.0
        if best_score >= 0.90 and best_score - second_score >= 0.02:
            return best_id
        return ""

    def canonicalize_commit_values(raw_values: Any) -> List[str]:
        canonical: List[str] = []
        for raw_commit in _split_values(raw_values):
            commit_id = resolve(raw_commit)
            if not commit_id or commit_id in assigned:
                continue
            assigned.add(commit_id)
            canonical.append(commit_id)
        return canonical

    next_groups: List[Dict[str, Any]] = []
    for raw_group in payload.get("groups") or []:
        if not isinstance(raw_group, dict):
            continue
        source_commits = canonicalize_commit_values(raw_group.get("source_commits") or [])
        if not source_commits:
            continue
        group = dict(raw_group)
        group["source_commits"] = source_commits
        next_groups.append(group)
    payload["groups"] = next_groups

    def canonicalize_commit_entries(*keys: str) -> List[Dict[str, Any]]:
        raw_entries: List[Any] = []
        for key in keys:
            value = payload.get(key)
            if isinstance(value, list):
                raw_entries.extend(value)

        entries: List[Dict[str, Any]] = []
        for raw_entry in raw_entries:
            if not isinstance(raw_entry, dict):
                continue
            commit_id = resolve(raw_entry.get("commit_id"))
            if not commit_id or commit_id in assigned:
                continue
            assigned.add(commit_id)
            entry = dict(raw_entry)
            entry["commit_id"] = commit_id
            entries.append(entry)
        return entries

    deprioritized = canonicalize_commit_entries("deprioritized", "deprioritized_commits")
    payload["deprioritized"] = deprioritized
    payload["deprioritized_commits"] = []

    filtered = canonicalize_commit_entries("filtered", "filtered_commits")
    payload["filtered"] = filtered
    payload["filtered_commits"] = []

    missing = [commit_id for commit_id in valid_ids if commit_id not in assigned]
    for commit_id in missing:
        payload["deprioritized"].append(
            {
                "commit_id": commit_id,
                "reason_code": "low_confidence_architecture_support",
                "reason": "LLM output omitted this input commit; assigned by deterministic coverage repair.",
            }
        )


def _normalize_value_decisions(payload: Dict[str, Any], commit_cards: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    valid_ids = [card["commit_id"] for card in commit_cards]
    raw_items = payload.get("decisions") if isinstance(payload, dict) else []
    by_commit: Dict[str, Dict[str, Any]] = {}
    if isinstance(raw_items, list):
        for item in raw_items:
            if not isinstance(item, dict):
                continue
            commit_id = str(item.get("commit_id") or "")
            if commit_id in valid_ids and commit_id not in by_commit:
                by_commit[commit_id] = item
    decisions: List[Dict[str, Any]] = []
    for card in commit_cards:
        raw = by_commit.get(card["commit_id"])
        if not raw:
            decisions.append(_deterministic_value_decision(card))
            continue
        value = str(raw.get("release_note_value") or "").lower()
        if value not in VALUE_ENUM:
            value = DEPRIORITIZE_DECISION
        reason_code = str(raw.get("reason_code") or "").strip()
        if reason_code not in ALL_REASON_CODES:
            reason_code = _default_reason_code_for_value(value, card)
        target_value = str(raw.get("target_audience_value") or "").lower()
        if target_value not in AUDIENCE_VALUE_ENUM:
            target_value = "low"
        decision = {
            "commit_id": card["commit_id"],
            "release_note_value": value,
            "reason_code": reason_code,
            "target_audience_value": target_value,
            "reason": str(raw.get("reason") or _reason_for_code(reason_code)),
        }
        decision = _protect_decision(card, decision)
        decisions.append(decision)
    return decisions


def _normalize_slot_assignments(
    payload: Dict[str, Any],
    commit_cards: Sequence[Dict[str, Any]],
    value_decisions: Sequence[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    valid_ids = [card["commit_id"] for card in commit_cards]
    decision_by_id = _by_id(value_decisions)
    raw_items = []
    if isinstance(payload, dict):
        raw_items = payload.get("assignments")
        if raw_items is None:
            raw_items = payload.get("slot_assignments")
    by_commit: Dict[str, Dict[str, Any]] = {}
    if isinstance(raw_items, list):
        for item in raw_items:
            if not isinstance(item, dict):
                continue
            commit_id = str(item.get("commit_id") or "")
            if commit_id in valid_ids and commit_id not in by_commit:
                by_commit[commit_id] = item

    assignments: List[Dict[str, Any]] = []
    for card in commit_cards:
        decision = decision_by_id.get(card["commit_id"], {})
        if decision.get("release_note_value") == FILTER_DECISION:
            continue
        raw = by_commit.get(card["commit_id"])
        if not raw:
            assignments.append(_fallback_slot_assignment(card, decision))
            continue
        primary_slot = _normalize_slot_name(str(raw.get("slot") or raw.get("primary_slot") or ""))
        if primary_slot not in SCHEMA_SLOTS:
            primary_slot = _slot_for_card(card, decision)
        secondary_slots = [
            slot
            for slot in (_normalize_slot_name(str(slot)) for slot in raw.get("secondary_slots") or [])
            if slot in SCHEMA_SLOTS
        ]
        confidence = str(raw.get("assignment_confidence") or "medium").lower()
        if confidence not in ASSIGNMENT_CONFIDENCE_ENUM:
            confidence = "medium"
        assignments.append(
            {
                "commit_id": card["commit_id"],
                "primary_slot": primary_slot,
                "secondary_slots": secondary_slots,
                "related_arch_events": _unique(([raw.get("event_id")] if raw.get("event_id") else []) or raw.get("related_arch_events") or card.get("related_arch_events") or []),
                "assignment_confidence": confidence,
                "reason": str(raw.get("reason") or "Normalized slot assignment."),
            }
        )
    return assignments


def _normalize_slot_name(slot: str) -> str:
    value = str(slot or "").strip()
    aliases = {
        "functional_changes.maintenance": "non_functional_changes.maintenance",
        "functional_changes.documentation": "non_functional_changes.documentation",
        "functional_changes.build_ci": "non_functional_changes.build_ci",
        "functional_changes.performance": "non_functional_changes.performance",
        "functional_changes.security": "non_functional_changes.security",
    }
    return aliases.get(value, value)


def _normalize_bucket_plan(
    payload: Dict[str, Any],
    bucket: Dict[str, Any],
    *,
    cards_by_id: Dict[str, Dict[str, Any]],
    value_decisions: Dict[str, Dict[str, Any]],
    slot_assignments: Dict[str, Dict[str, Any]],
    debug: bool = False,
) -> Dict[str, Any]:
    valid_ids = set(bucket.get("commit_ids") or [])
    slot = bucket.get("slot") or "others"
    partial = {
        "bucket_id": bucket.get("bucket_id") or slot,
        "groups": [],
        "deprioritized_commits": [],
        "filtered_commits": [],
        "warnings": [],
    }
    assigned: set[str] = set()

    for raw_group in payload.get("groups") or [] if isinstance(payload, dict) else []:
        if not isinstance(raw_group, dict):
            continue
        commits = [commit_id for commit_id in _split_values(raw_group.get("source_commits") or []) if commit_id in valid_ids and commit_id not in assigned]
        if not commits:
            continue
        assigned.update(commits)
        group = _build_group_from_commit_ids(
            group_id=str(raw_group.get("group_id") or _make_group_id(slot, commits, index=len(partial["groups"]) + 1)),
            slot=slot,
            source_commits=commits,
            cards_by_id=cards_by_id,
            entry_intent=str(raw_group.get("entry_intent") or _fallback_intent([cards_by_id[cid] for cid in commits], slot)),
            aggregation_reason=str(raw_group.get("aggregation_reason") or "Local bucket aggregation."),
            related_arch_events=raw_group.get("related_arch_events") or ([bucket["event_id"]] if bucket.get("event_id") else []),
        )
        partial["groups"].append(group)

    raw_deprioritized = []
    if isinstance(payload, dict):
        raw_deprioritized = payload.get("deprioritized")
        if raw_deprioritized is None:
            raw_deprioritized = payload.get("deprioritized_commits")
    for raw_entry in raw_deprioritized or []:
        if not isinstance(raw_entry, dict):
            continue
        commit_id = str(raw_entry.get("commit_id") or "")
        if commit_id in valid_ids and commit_id not in assigned:
            assigned.add(commit_id)
            partial["deprioritized_commits"].append(_deprioritized_entry(cards_by_id[commit_id], raw_entry))

    raw_filtered = []
    if isinstance(payload, dict):
        raw_filtered = payload.get("filtered")
        if raw_filtered is None:
            raw_filtered = payload.get("filtered_commits")
    for raw_entry in raw_filtered or []:
        if not isinstance(raw_entry, dict):
            continue
        commit_id = str(raw_entry.get("commit_id") or "")
        if commit_id in valid_ids and commit_id not in assigned:
            assigned.add(commit_id)
            partial["filtered_commits"].append(_filtered_entry(cards_by_id[commit_id], raw_entry))

    missing = [commit_id for commit_id in bucket.get("commit_ids") or [] if commit_id not in assigned]
    if missing:
        if debug:
            raise ValueError(f"Bucket normalization left unassigned commits with fail-fast enabled: {missing}")
        fallback = _fallback_bucket_plan(
            {**bucket, "commit_ids": missing},
            cards_by_id,
            list(value_decisions.values()),
            list(slot_assignments.values()),
        )
        partial["groups"].extend(fallback.get("groups") or [])
        partial["deprioritized_commits"].extend(fallback.get("deprioritized_commits") or [])
        partial["filtered_commits"].extend(fallback.get("filtered_commits") or [])
    return partial


def _normalize_group_review_actions(payload: Dict[str, Any], group_summaries: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    valid_group_ids = {summary["group_id"] for summary in group_summaries}
    group_slot_by_id = _group_slot_by_id(group_summaries)
    actions = _empty_group_review_actions()
    if isinstance(payload, dict) and isinstance(payload.get("actions"), list):
        for raw in payload.get("actions") or []:
            if not isinstance(raw, dict):
                continue
            action = str(raw.get("action") or "")
            group_ids = [str(group_id) for group_id in raw.get("group_ids") or [] if str(group_id) in valid_group_ids]
            new_slot = _resolve_group_review_new_slot(action, str(raw.get("new_slot") or ""), group_ids, group_slot_by_id)
            if action == "merge" and len(group_ids) >= 2 and new_slot in SCHEMA_SLOTS:
                actions["merge_actions"].append(
                    {
                        "source_group_ids": group_ids,
                        "new_group_id": f"MERGED-G-{len(actions['merge_actions']) + 1:03d}",
                        "new_slot": new_slot,
                        "reason": str(raw.get("reason") or ""),
                    }
                )
            elif action == "move" and len(group_ids) == 1 and new_slot in SCHEMA_SLOTS:
                actions["move_actions"].append({"group_id": group_ids[0], "new_slot": new_slot, "reason": str(raw.get("reason") or "")})
            elif action == "keep" and len(group_ids) == 1:
                actions["keep_actions"].append({"group_id": group_ids[0], "reason": str(raw.get("reason") or "")})
        return actions
    for raw in payload.get("merge_actions") or [] if isinstance(payload, dict) else []:
        if not isinstance(raw, dict):
            continue
        source_ids = [str(group_id) for group_id in raw.get("source_group_ids") or [] if str(group_id) in valid_group_ids]
        if len(source_ids) < 2:
            continue
        new_slot = _resolve_group_review_new_slot("merge", str(raw.get("new_slot") or ""), source_ids, group_slot_by_id)
        if new_slot not in SCHEMA_SLOTS:
            continue
        actions["merge_actions"].append(
            {
                "source_group_ids": source_ids,
                "new_group_id": str(raw.get("new_group_id") or f"MERGED-G-{len(actions['merge_actions']) + 1:03d}"),
                "new_slot": new_slot,
                "reason": str(raw.get("reason") or ""),
            }
        )
    for raw in payload.get("move_actions") or [] if isinstance(payload, dict) else []:
        if not isinstance(raw, dict):
            continue
        group_id = str(raw.get("group_id") or "")
        new_slot = str(raw.get("new_slot") or "")
        if group_id in valid_group_ids and new_slot in SCHEMA_SLOTS:
            actions["move_actions"].append({"group_id": group_id, "new_slot": new_slot, "reason": str(raw.get("reason") or "")})
    for raw in payload.get("keep_actions") or [] if isinstance(payload, dict) else []:
        if not isinstance(raw, dict):
            continue
        group_id = str(raw.get("group_id") or "")
        if group_id in valid_group_ids:
            actions["keep_actions"].append({"group_id": group_id, "reason": str(raw.get("reason") or "")})
    return actions


def _normalize_low_priority_actions(
    payload: Dict[str, Any],
    low_priority_commits: Sequence[Dict[str, Any]],
    plan: Dict[str, Any],
) -> Dict[str, Any]:
    valid_ids = {str(item.get("commit_id") or "") for item in low_priority_commits if str(item.get("commit_id") or "")}
    existing_group_ids = {str(group.get("group_id") or "") for group in _flat_groups(plan)}
    actions = _empty_low_priority_actions()
    assigned: set[str] = set()

    for raw_action in payload.get("merge_actions") or [] if isinstance(payload, dict) else []:
        if not isinstance(raw_action, dict):
            continue
        target_group_id = str(raw_action.get("target_group_id") or "")
        if target_group_id not in existing_group_ids:
            continue
        source_commits = [
            commit_id
            for commit_id in _split_values(raw_action.get("source_commits") or [])
            if commit_id in valid_ids and commit_id not in assigned
        ]
        if not source_commits:
            continue
        assigned.update(source_commits)
        actions["merge_actions"].append(
            {
                "target_group_id": target_group_id,
                "source_commits": source_commits,
                "merge_note": str(raw_action.get("merge_note") or ""),
                "reason": str(raw_action.get("reason") or ""),
            }
        )

    for raw_group in payload.get("brief_groups") or [] if isinstance(payload, dict) else []:
        if not isinstance(raw_group, dict):
            continue
        source_commits = [
            commit_id
            for commit_id in _split_values(raw_group.get("source_commits") or [])
            if commit_id in valid_ids and commit_id not in assigned
        ]
        if not source_commits:
            continue
        slot = str(raw_group.get("slot") or "")
        if slot not in SCHEMA_SLOTS:
            slot = "others"
        assigned.update(source_commits)
        actions["brief_groups"].append(
            {
                "group_id": str(raw_group.get("group_id") or _low_priority_group_id(slot, source_commits)),
                "slot": slot,
                "entry_style": "brief",
                "release_note_value": str(raw_group.get("release_note_value") or "mixed_low_priority"),
                "source_commits": source_commits,
                "entry_intent": str(raw_group.get("entry_intent") or ""),
                "aggregation_reason": str(raw_group.get("aggregation_reason") or raw_group.get("reason") or ""),
            }
        )

    missing = [item for item in low_priority_commits if str(item.get("commit_id") or "") not in assigned]
    if missing:
        fallback = _fallback_low_priority_actions_for_entries(missing, {})
        actions["brief_groups"].extend(fallback.get("brief_groups") or [])
    return actions


def _group_slot_by_id(group_summaries: Sequence[Dict[str, Any]]) -> Dict[str, str]:
    return {
        str(summary.get("group_id") or ""): str(summary.get("slot") or "")
        for summary in group_summaries
        if str(summary.get("group_id") or "")
    }


def _resolve_group_review_new_slot(
    action: str,
    new_slot: str,
    group_ids: Sequence[str],
    group_slot_by_id: Dict[str, str],
) -> str:
    if new_slot in SCHEMA_SLOTS:
        return new_slot
    if action != "merge":
        return new_slot
    source_slots = {
        group_slot_by_id.get(str(group_id), "")
        for group_id in group_ids
        if group_slot_by_id.get(str(group_id), "") in SCHEMA_SLOTS
    }
    if len(source_slots) == 1:
        return next(iter(source_slots))
    return new_slot


def _normalize_coverage_repair_actions(
    payload: Dict[str, Any],
    problem_commit_ids: Sequence[str],
    cards_by_id: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    valid_ids = set(problem_commit_ids)
    actions = {"repair_actions": []}
    for raw in payload.get("repair_actions") or [] if isinstance(payload, dict) else []:
        if not isinstance(raw, dict):
            continue
        commit_id = str(raw.get("commit_id") or "")
        action = str(raw.get("action") or "")
        if commit_id not in valid_ids or action not in {"add_to_existing_group", "create_new_group", "add_to_deprioritized", "add_to_filtered"}:
            continue
        item = dict(raw)
        item["commit_id"] = commit_id
        actions["repair_actions"].append(item)
    for commit_id in valid_ids - {item["commit_id"] for item in actions["repair_actions"]}:
        card = cards_by_id.get(commit_id)
        if not card:
            continue
        decision = _deterministic_value_decision(card)
        if decision["release_note_value"] == FILTER_DECISION:
            actions["repair_actions"].append(
                {
                    "commit_id": commit_id,
                    "action": "add_to_filtered",
                    "target_group_id": "",
                    "new_group": None,
                    "deprioritized_commit": None,
                    "filtered_commit": _filtered_entry(card, decision),
                    "reason": decision["reason"],
                }
            )
        elif decision["release_note_value"] == DEPRIORITIZE_DECISION:
            actions["repair_actions"].append(
                {
                    "commit_id": commit_id,
                    "action": "add_to_deprioritized",
                    "target_group_id": "",
                    "new_group": None,
                    "deprioritized_commit": _deprioritized_entry(card, decision),
                    "filtered_commit": None,
                    "reason": decision["reason"],
                }
            )
        else:
            slot = _slot_for_card(card, decision)
            actions["repair_actions"].append(
                {
                    "commit_id": commit_id,
                    "action": "create_new_group",
                    "target_group_id": "",
                    "new_group": _build_group_from_commit_ids(
                        group_id=f"REPAIR-G-{_short_commit_prefix(commit_id)}",
                        slot=slot,
                        source_commits=[commit_id],
                        cards_by_id=cards_by_id,
                        entry_intent=card.get("commit_summary") or card.get("commit_message") or "",
                        aggregation_reason="coverage repair deterministic fallback",
                        related_arch_events=card.get("related_arch_events") or [],
                    ),
                    "deprioritized_commit": None,
                    "filtered_commit": None,
                    "reason": decision["reason"],
                }
            )
    return actions


def _fallback_value_decisions(commit_cards: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [_deterministic_value_decision(card) for card in commit_cards]


def _deterministic_value_decision(card: Dict[str, Any]) -> Dict[str, Any]:
    category = _category(card)
    text = _card_text(card)
    role = str(card.get("structure_role") or "local_supporting")
    has_event = bool(card.get("top_event", {}).get("event_id") or card.get("related_arch_events"))
    if role == "structure_guiding":
        return _value_decision(card, INCLUDE_DECISION, "architecture_guiding", "high", "Structure-guiding commit is retained for release-note aggregation.")
    if role == "architecture_related_supporting" and has_event and _arch_score(card) >= 0.25:
        return _value_decision(card, INCLUDE_DECISION, "architecture_supporting", "medium", "Architecture-related supporting commit has event evidence.")
    top_event = card.get("top_event") or {}
    if (
        has_event
        and _safe_float(top_event.get("posterior")) >= 0.35
        and _safe_float(card.get("negative_evidence")) < 0.6
        and not (_is_docs_only(card) or _is_tests_only(card) or _is_ci_only(card))
        and not (_is_formatting_only(card) or _is_typo_only(card) or _is_generated_only(card) or _is_lockfile_only(card))
    ):
        return _value_decision(card, INCLUDE_DECISION, "architecture_supporting", "medium", "Strongly related to a high-confidence architecture event and retained as architecture evidence.")
    if _is_security_related(text):
        return _value_decision(card, INCLUDE_DECISION, "security", "high", "Security-related change.")
    if _is_performance_related(text):
        return _value_decision(card, INCLUDE_DECISION, "performance", "high", "Performance-related change.")
    if _is_breaking_or_api_change(text):
        return _value_decision(card, INCLUDE_DECISION, "api_change", "high", "API, behavior, or compatibility change.")
    if _is_build_install_runtime_change(card):
        return _value_decision(card, INCLUDE_DECISION, "build_or_runtime_impact", "medium", "Affects build, installation, or runtime environment.")
    if _is_feature_category(category, text):
        return _value_decision(card, INCLUDE_DECISION, "new_feature", "high", "New feature or enhancement.")
    if _is_bugfix_category(category, text):
        return _value_decision(card, INCLUDE_DECISION, "bug_fix", "high", "Bug fix or correctness improvement.")
    if _is_formatting_only(card):
        return _value_decision(card, FILTER_DECISION, "formatting_only", "none", "Formatting-only change.")
    if _is_typo_only(card):
        return _value_decision(card, FILTER_DECISION, "typo_only", "none", "Spelling or typo fix.")
    if _is_generated_only(card):
        return _value_decision(card, FILTER_DECISION, "generated_only", "none", "Generated-file-only change.")
    if _is_lockfile_only(card):
        return _value_decision(card, FILTER_DECISION, "lockfile_only", "none", "Lockfile-only change.")
    if _is_version_or_metadata_only(card):
        return _value_decision(card, FILTER_DECISION, "version_bump_only", "none", "Version or metadata only.")
    if _is_tests_only(card):
        return _value_decision(card, DEPRIORITIZE_DECISION, "tests_only", "low", "Test maintenance change.")
    if _is_docs_only(card):
        return _value_decision(card, DEPRIORITIZE_DECISION, "docs_only", "low", "Documentation maintenance change.")
    if _is_ci_only(card):
        return _value_decision(card, DEPRIORITIZE_DECISION, "ci_only", "low", "Internal CI or workflow maintenance.")
    if _is_refactoring_category(category, text):
        return _value_decision(card, DEPRIORITIZE_DECISION, "internal_refactoring", "low", "Internal refactoring without clear user-visible behavior change.")
    return _value_decision(card, DEPRIORITIZE_DECISION, "minor_maintenance", "low", "Low-priority maintenance change.")


def _protect_decision(card: Dict[str, Any], decision: Dict[str, Any]) -> Dict[str, Any]:
    role = str(card.get("structure_role") or "")
    if role == "structure_guiding" and decision.get("release_note_value") == FILTER_DECISION:
        return _deterministic_value_decision(card)
    if _is_feature_category(_category(card), _card_text(card)) and decision.get("release_note_value") == FILTER_DECISION:
        return _deterministic_value_decision(card)
    if _is_bugfix_category(_category(card), _card_text(card)) and decision.get("reason_code") == "formatting_only":
        return _deterministic_value_decision(card)
    return decision


def _value_decision(card: Dict[str, Any], value: str, reason_code: str, audience: str, reason: str) -> Dict[str, Any]:
    return {
        "commit_id": card["commit_id"],
        "release_note_value": value,
        "reason_code": reason_code,
        "target_audience_value": audience,
        "reason": reason,
    }


def _fallback_slot_assignments(
    commit_cards: Sequence[Dict[str, Any]],
    value_decisions: Sequence[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    decision_by_id = _by_id(value_decisions)
    return [
        _fallback_slot_assignment(card, decision_by_id.get(card["commit_id"], {}))
        for card in commit_cards
        if decision_by_id.get(card["commit_id"], {}).get("release_note_value") != FILTER_DECISION
    ]


def _fallback_slot_assignment(card: Dict[str, Any], decision: Dict[str, Any]) -> Dict[str, Any]:
    slot = _slot_for_card(card, decision)
    return {
        "commit_id": card["commit_id"],
        "primary_slot": slot,
        "secondary_slots": [],
        "related_arch_events": card.get("related_arch_events") or [],
        "assignment_confidence": "high" if decision.get("target_audience_value") == "high" else "medium",
        "reason": "No concise reason was returned by the model.",
    }


def _fallback_bucket_plan(
    bucket: Dict[str, Any],
    cards_by_id: Dict[str, Dict[str, Any]],
    value_decisions: Sequence[Dict[str, Any]],
    slot_assignments: Sequence[Dict[str, Any]],
) -> Dict[str, Any]:
    decision_by_id = _by_id(value_decisions)
    slot = bucket.get("slot") or "others"
    include_ids: List[str] = []
    deprioritized: List[Dict[str, Any]] = []
    filtered: List[Dict[str, Any]] = []
    for commit_id in bucket.get("commit_ids") or []:
        card = cards_by_id.get(commit_id)
        if not card:
            continue
        decision = decision_by_id.get(commit_id) or _deterministic_value_decision(card)
        if decision.get("release_note_value") == INCLUDE_DECISION:
            include_ids.append(commit_id)
        elif decision.get("release_note_value") == FILTER_DECISION:
            filtered.append(_filtered_entry(card, decision))
        else:
            deprioritized.append(_deprioritized_entry(card, decision))
    groups = []
    if include_ids:
        groups.append(
            _build_group_from_commit_ids(
                group_id=_make_group_id(slot, include_ids),
                slot=slot,
                source_commits=include_ids,
                cards_by_id=cards_by_id,
                entry_intent=_fallback_intent([cards_by_id[commit_id] for commit_id in include_ids], slot),
                aggregation_reason="Single included commit retained as its own release-note group.",
                related_arch_events=[bucket["event_id"]] if bucket.get("event_id") else _unique(event for commit_id in include_ids for event in cards_by_id[commit_id].get("related_arch_events", [])),
            )
        )
    return {
        "bucket_id": bucket.get("bucket_id") or slot,
        "groups": groups,
        "deprioritized_commits": deprioritized,
        "filtered_commits": filtered,
    }


def _fallback_assign_missing_into_plan(plan: Dict[str, Any], cards: Sequence[Dict[str, Any]]) -> None:
    for card in cards:
        decision = _deterministic_value_decision(card)
        if decision["release_note_value"] == INCLUDE_DECISION:
            slot = _slot_for_card(card, decision)
            _append_group(
                plan,
                slot,
                _build_group_from_commit_ids(
                    group_id=f"FALLBACK-{_short_commit_prefix(card['commit_id'])}",
                    slot=slot,
                    source_commits=[card["commit_id"]],
                    cards_by_id={card["commit_id"]: card},
                    entry_intent=card.get("commit_summary") or card.get("commit_message") or "",
                    aggregation_reason="Related commits share the same slot and module context.",
                    related_arch_events=card.get("related_arch_events") or [],
                ),
            )
        elif decision["release_note_value"] == FILTER_DECISION:
            plan.setdefault("filtered_commits", []).append(_filtered_entry(card, decision))
        else:
            plan.setdefault("deprioritized_commits", []).append(_deprioritized_entry(card, decision))


def _slot_for_card(card: Dict[str, Any], decision: Optional[Dict[str, Any]] = None) -> str:
    event_type = str((card.get("top_event") or {}).get("event_type") or "")
    role = str(card.get("structure_role") or "")
    reason_code = str((decision or {}).get("reason_code") or "")
    category = _category(card)
    text = _card_text(card)
    if role == "structure_guiding" or reason_code in {"architecture_guiding", "architecture_supporting"}:
        if event_type == "module_added":
            return "architecture_changes.added_modules"
        if event_type == "module_removed":
            return "architecture_changes.removed_modules"
        return "architecture_changes.changed_modules"
    if reason_code == "security" or _is_security_related(text):
        return "non_functional_changes.security"
    if reason_code == "performance" or _is_performance_related(text):
        return "non_functional_changes.performance"
    if reason_code in {"build_or_runtime_impact", "compatibility"} or _is_build_install_runtime_change(card):
        return "non_functional_changes.build_ci"
    if reason_code == "new_feature" or _is_feature_category(category, text):
        return "functional_changes.new_features"
    if reason_code == "bug_fix" or _is_bugfix_category(category, text):
        return "functional_changes.bug_fixes"
    if reason_code == "tests_only" or _is_tests_only(card):
        return "functional_changes.tests"
    if reason_code == "docs_only" or _is_docs_only(card):
        return "non_functional_changes.documentation"
    if reason_code == "internal_refactoring" or _is_refactoring_category(category, text):
        return "functional_changes.refactorings"
    if reason_code in {"ci_only", "dependency_maintenance", "chore", "minor_maintenance"}:
        return "non_functional_changes.maintenance"
    return "others"


def _build_group_from_commit_ids(
    *,
    group_id: str,
    slot: str,
    source_commits: Sequence[str],
    cards_by_id: Dict[str, Dict[str, Any]],
    entry_intent: str,
    aggregation_reason: str,
    related_arch_events: Sequence[str],
) -> Dict[str, Any]:
    first_card = next((cards_by_id.get(commit_id) for commit_id in source_commits if commit_id in cards_by_id), {}) or {}
    return {
        "group_id": group_id,
        "slot": slot,
        "entry_intent": entry_intent,
        "source_commits": list(source_commits),
        "related_arch_events": _unique([str(item) for item in related_arch_events if str(item)]),
        "primary_module": str(first_card.get("primary_module") or "unknown"),
        "primary_component": str(first_card.get("primary_component") or "unknown"),
        "aggregation_reason": aggregation_reason,
        "traceability": _traceability_for_commits(source_commits, cards_by_id),
    }


def _deprioritized_entry(card: Dict[str, Any], decision: Dict[str, Any]) -> Dict[str, Any]:
    reason_code = str(decision.get("reason_code") or "minor_maintenance")
    if reason_code not in DEPRIORITIZE_REASON_CODES:
        reason_code = "minor_maintenance"
    return {
        "commit_id": str(card.get("commit_id") or decision.get("commit_id") or ""),
        "functional_category": str(card.get("functional_category") or "unknown"),
        "reason_code": reason_code,
        "reason": str(decision.get("reason") or _reason_for_code(reason_code)),
        "can_be_mentioned_briefly": bool(decision.get("can_be_mentioned_briefly", True)),
        "suggested_slot": str(decision.get("suggested_slot") or _slot_for_card(card, decision)),
    }


def _filtered_entry(card: Dict[str, Any], decision: Dict[str, Any]) -> Dict[str, Any]:
    reason_code = str(decision.get("reason_code") or "metadata_only")
    if reason_code not in FILTER_REASON_CODES:
        reason_code = "metadata_only"
    return {
        "commit_id": str(card.get("commit_id") or decision.get("commit_id") or ""),
        "functional_category": str(card.get("functional_category") or "unknown"),
        "reason_code": reason_code,
        "reason": str(decision.get("reason") or _reason_for_code(reason_code)),
        "can_be_mentioned_briefly": bool(decision.get("can_be_mentioned_briefly", True)),
        "suggested_slot": "others",
    }


def _traceability_for_commits(source_commits: Sequence[str], cards_by_id: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    return {
        "source_commit_count": len(source_commits),
        "source_commits": [
            {
                "commit_id": commit_id,
                "commit_message": str(cards_by_id.get(commit_id, {}).get("commit_message") or ""),
                "commit_summary": str(cards_by_id.get(commit_id, {}).get("commit_summary") or ""),
                "structure_role": str(cards_by_id.get(commit_id, {}).get("structure_role") or ""),
                "architecture_signal_score": _safe_float(cards_by_id.get(commit_id, {}).get("architecture_signal_score")),
                "architecture_relevance_score": _arch_score(cards_by_id.get(commit_id, {})),
                "architecture_relevance_level": str(cards_by_id.get(commit_id, {}).get("architecture_relevance_level") or ""),
                "architecture_relevance_labels": [
                    str(item) for item in cards_by_id.get(commit_id, {}).get("architecture_relevance_labels") or [] if str(item)
                ],
                "functional_category": str(cards_by_id.get(commit_id, {}).get("functional_category") or ""),
                "evidence_granularity": str(cards_by_id.get(commit_id, {}).get("evidence_granularity") or ""),
            }
            for commit_id in source_commits
        ],
    }


def _empty_plan_root(generation_mode: str) -> Dict[str, Any]:
    return {
        "generation_mode": generation_mode,
        "groups": _empty_groups(),
        "deprioritized_commits": [],
        "filtered_commits": [],
        "coverage_report": {
            "total_commits": 0,
            "included_commits": 0,
            "deprioritized_commits": 0,
            "filtered_commits": 0,
            "unassigned_commits": [],
            "duplicated_commits": [],
            "included_commit_ids": [],
            "deprioritized_commit_ids": [],
            "filtered_commit_ids": [],
        },
        "warnings": [],
    }


def _empty_groups() -> Dict[str, Any]:
    return {
        "architecture_changes": {"added_modules": [], "removed_modules": [], "changed_modules": []},
        "functional_changes": {"new_features": [], "bug_fixes": [], "refactorings": [], "tests": []},
        "non_functional_changes": {
            "performance": [],
            "security": [],
            "documentation": [],
            "build_ci": [],
            "maintenance": [],
        },
        "others": [],
    }


def _coerce_plan(plan: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(plan, dict):
        return _empty_plan_root("fallback")
    candidate = plan.get("aggregation_plan") if isinstance(plan.get("aggregation_plan"), dict) else plan
    root = _empty_plan_root(str(candidate.get("generation_mode") or "llm_multi_stage"))
    source_groups = candidate.get("groups") if isinstance(candidate.get("groups"), dict) else candidate
    for slot in SCHEMA_SLOTS:
        raw_groups = _get_slot(source_groups, slot)
        if isinstance(raw_groups, list):
            _set_slot(root["groups"], slot, list(raw_groups))
    root["deprioritized_commits"] = list(candidate.get("deprioritized_commits") or [])
    root["filtered_commits"] = list(candidate.get("filtered_commits") or [])
    root["warnings"] = list(candidate.get("warnings") or [])
    return root


def _append_group(plan: Dict[str, Any], slot: str, group: Dict[str, Any]) -> None:
    target = _get_slot(plan.setdefault("groups", _empty_groups()), slot)
    if isinstance(target, list):
        target.append(group)


def _get_slot(plan: Dict[str, Any], slot: str) -> Any:
    target: Any = plan
    for part in slot.split("."):
        if not isinstance(target, dict):
            return None
        target = target.get(part)
    return target


def _set_slot(plan: Dict[str, Any], slot: str, value: Any) -> None:
    target: Any = plan
    parts = slot.split(".")
    for part in parts[:-1]:
        target = target.setdefault(part, {})
    target[parts[-1]] = value


def _flat_groups(plan: Dict[str, Any]) -> List[Dict[str, Any]]:
    groups_root = plan.get("groups") if isinstance(plan.get("groups"), dict) else plan
    groups: List[Dict[str, Any]] = []
    for slot in SCHEMA_SLOTS:
        groups.extend([group for group in _get_slot(groups_root, slot) or [] if isinstance(group, dict)])
    return groups


def _ids_from_plan(plan: Dict[str, Any]) -> List[str]:
    ids: List[str] = []
    for group in _flat_groups(plan):
        ids.extend([str(item) for item in group.get("source_commits") or [] if str(item)])
    ids.extend([str(item.get("commit_id") or "") for item in plan.get("deprioritized_commits") or [] if isinstance(item, dict)])
    ids.extend([str(item.get("commit_id") or "") for item in plan.get("filtered_commits") or [] if isinstance(item, dict)])
    return [item for item in ids if item]


def _count_groups(plan: Dict[str, Any]) -> int:
    return len(_flat_groups(plan))


def _group_summaries(partial_plans: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    summaries: List[Dict[str, Any]] = []
    for partial in partial_plans:
        for group in partial.get("groups") or []:
            summaries.append(
                {
                    "group_id": group.get("group_id"),
                    "slot": group.get("slot"),
                    "entry_intent": group.get("entry_intent"),
                    "entry_style": group.get("entry_style") or "full",
                    "release_note_value": group.get("release_note_value") or "include",
                    "source_commit_count": len(group.get("source_commits") or []),
                }
            )
    return summaries


def _empty_group_review_actions() -> Dict[str, Any]:
    return {"merge_actions": [], "move_actions": [], "keep_actions": []}


def _extend_group_review_actions(target: Dict[str, Any], source: Dict[str, Any]) -> None:
    for raw in source.get("merge_actions") or []:
        if not isinstance(raw, dict):
            continue
        item = dict(raw)
        item["new_group_id"] = f"MERGED-G-{len(target.get('merge_actions') or []) + 1:03d}"
        target.setdefault("merge_actions", []).append(item)
    for key in ("move_actions", "keep_actions"):
        for raw in source.get(key) or []:
            if isinstance(raw, dict):
                target.setdefault(key, []).append(dict(raw))


def _aggregation_plan_summary(plan: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "groups": [
            {
                "group_id": group.get("group_id"),
                "slot": group.get("slot"),
                "source_commits": group.get("source_commits"),
                "entry_intent": group.get("entry_intent"),
            }
            for group in _flat_groups(plan)
        ],
        "coverage_report": plan.get("coverage_report") or {},
    }


def _validation_report(plan: Dict[str, Any], all_commit_ids: Sequence[str]) -> Dict[str, Any]:
    coverage = plan.get("coverage_report") or {}
    membership = []
    for commit_id in all_commit_ids:
        locations = []
        if commit_id in set(coverage.get("included_commit_ids") or []):
            locations.append("included")
        if commit_id in set(coverage.get("deprioritized_commit_ids") or []):
            locations.append("deprioritized")
        if commit_id in set(coverage.get("filtered_commit_ids") or []):
            locations.append("filtered")
        membership.append({"commit_id": commit_id, "locations": locations})
    return {
        "coverage_report": coverage,
        "warnings": plan.get("warnings") or [],
        "membership": membership,
        "ok": not coverage.get("unassigned_commits"),
    }


def _changed_files_summary(changed_files: Sequence[str]) -> Dict[str, Any]:
    main_dirs = []
    file_types = []
    for path in changed_files:
        normalized = path.replace("\\", "/")
        parts = normalized.split("/")
        main_dirs.append(parts[0] if len(parts) > 1 else ".")
        suffix = Path(normalized).suffix.lower()
        file_types.append(suffix or "<none>")
    return {
        "count": len(changed_files),
        "main_dirs": _unique(main_dirs)[:5],
        "file_types": _unique(file_types)[:5],
        "sample_files": list(changed_files)[:5],
    }


def _top_event(record: Dict[str, Any]) -> Dict[str, Any]:
    best: Dict[str, Any] = {}
    best_posterior = -1.0
    for attribution in record.get("event_attributions") or []:
        if not isinstance(attribution, dict):
            continue
        posterior = _safe_float(attribution.get("posterior"))
        if posterior > best_posterior:
            best = attribution
            best_posterior = posterior
    if best:
        return {
            "event_id": str(best.get("event_id") or best.get("id") or ""),
            "event_type": str(best.get("event_type") or ""),
            "role_in_event": str(best.get("role_in_event") or ""),
            "posterior": best_posterior,
            "event_confidence": _safe_float(best.get("event_confidence")),
            "event_significance": _safe_float(best.get("event_significance")),
            "module": str(best.get("module") or ""),
            "component": str(best.get("component") or ""),
        }
    evidence = record.get("architecture_evidence")
    if isinstance(evidence, dict):
        matched = evidence.get("matched_arch_events") or []
        if isinstance(matched, list):
            item = next((entry for entry in matched if isinstance(entry, dict)), {})
            if item:
                return {
                    "event_id": str(item.get("event_id") or ""),
                    "event_type": str(item.get("event_type") or ""),
                    "role_in_event": str(item.get("role_in_event") or ""),
                    "posterior": _safe_float(item.get("posterior_hint")),
                    "event_confidence": _safe_float(item.get("event_confidence")),
                    "event_significance": _safe_float(item.get("event_significance")),
                    "module": str(item.get("module") or ""),
                    "component": str(item.get("component") or ""),
                }
    if isinstance(evidence, list) and evidence:
        item = next((entry for entry in evidence if isinstance(entry, dict)), {})
        return {
            "event_id": str(item.get("event_id") or ""),
            "event_type": str(item.get("event_type") or ""),
            "role_in_event": str(item.get("role_in_event") or ""),
            "posterior": 0.0,
            "event_confidence": 0.0,
            "event_significance": _safe_float(item.get("significance")),
            "module": str(item.get("module") or ""),
            "component": str(item.get("component") or ""),
        }
    return {
        "event_id": "",
        "event_type": "",
        "role_in_event": "",
        "posterior": 0.0,
        "event_confidence": 0.0,
        "event_significance": 0.0,
        "module": "",
        "component": "",
    }


def _event_ids_for_record(record: Dict[str, Any]) -> List[str]:
    ids: List[str] = []
    for item in record.get("event_attributions") or []:
        if isinstance(item, dict) and (item.get("event_id") or item.get("id")):
            ids.append(str(item.get("event_id") or item.get("id")))
    for item in record.get("architecture_evidence") or []:
        if isinstance(item, dict) and item.get("event_id"):
            ids.append(str(item.get("event_id")))
    evidence = record.get("architecture_evidence")
    if isinstance(evidence, dict):
        ids.extend([str(item) for item in evidence.get("matched_arch_event_ids") or [] if str(item)])
        for item in evidence.get("matched_arch_events") or []:
            if isinstance(item, dict) and item.get("event_id"):
                ids.append(str(item.get("event_id")))
    ids.extend([str(item) for item in record.get("matched_arch_events") or [] if str(item)])
    return _unique(ids)


def _negative_evidence(record: Dict[str, Any]) -> float:
    if _is_formatting_only(record) or _is_typo_only(record) or _is_generated_only(record) or _is_lockfile_only(record):
        return 1.0
    if _is_docs_only(record) or _is_tests_only(record) or _is_ci_only(record):
        return 0.6
    return 0.0


def _cards_by_id(cards: Sequence[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    return {card["commit_id"]: card for card in cards if card.get("commit_id")}


def _records_by_id(records: Sequence[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    return {str(record.get("commit_id") or ""): record for record in records if isinstance(record, dict) and record.get("commit_id")}


def _by_id(items: Sequence[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    return {str(item.get("commit_id") or ""): item for item in items if isinstance(item, dict) and item.get("commit_id")}


def _chunks(items: Sequence[Any], size: int) -> Iterable[List[Any]]:
    for index in range(0, len(items), max(1, size)):
        yield list(items[index : index + max(1, size)])


def _phase3_batch_size(config, attr_name: str, default: int) -> int:
    if config is None:
        return default
    try:
        return max(1, int(getattr(config, attr_name, default)))
    except Exception:
        return default


def _phase3_concurrency(config, attr_name: str) -> int:
    if config is None:
        return 1
    for name in (attr_name, "phase3_1_concurrency", "phase3_slot_concurrency", "step10_concurrency"):
        value = getattr(config, name, None)
        if value is None:
            continue
        try:
            return max(1, int(value))
        except Exception:
            continue
    return 1


def _phase3_short_hash_min_length(config) -> int:
    if config is None:
        return PHASE3_LLM_SHORT_HASH_DEFAULT_MIN_LENGTH
    try:
        value = int(getattr(config, "phase3_llm_short_hash_min_length", PHASE3_LLM_SHORT_HASH_DEFAULT_MIN_LENGTH))
    except Exception:
        return PHASE3_LLM_SHORT_HASH_DEFAULT_MIN_LENGTH
    return max(1, value)


def _build_phase3_llm_commit_id_map(
    commit_ids: Sequence[str],
    config=None,
) -> Dict[str, Any]:
    full_ids = _unique(str(commit_id) for commit_id in commit_ids if str(commit_id))
    min_length = _phase3_short_hash_min_length(config)
    max_length = max(PHASE3_LLM_SHORT_HASH_MAX_LENGTH, min_length)
    if not full_ids:
        return {"short_to_full": {}, "full_to_short": {}, "length": min_length}

    for length in range(min_length, max_length + 1):
        full_to_short = {commit_id: _short_commit_prefix(commit_id, length) for commit_id in full_ids}
        short_values = list(full_to_short.values())
        if len(set(short_values)) == len(short_values):
            return {
                "short_to_full": {short_id: full_id for full_id, short_id in full_to_short.items()},
                "full_to_short": full_to_short,
                "length": length,
            }

    collisions = {
        short_id: [commit_id for commit_id in full_ids if _short_commit_prefix(commit_id, max_length) == short_id]
        for short_id in {_short_commit_prefix(commit_id, max_length) for commit_id in full_ids}
    }
    collisions = {short_id: values for short_id, values in collisions.items() if len(values) > 1}
    raise ValueError(
        "Could not build unique Phase 3 LLM short commit hash map "
        f"between lengths {min_length} and {max_length}: {collisions}"
    )


def _short_commit_prefix(commit_id: str, length: int = PHASE3_LLM_SHORT_HASH_DEFAULT_MIN_LENGTH) -> str:
    text = str(commit_id or "")
    if not text:
        return ""
    return text[: max(1, int(length))]


def _shorten_commit_ids_for_llm(value: Any, id_map: Dict[str, Any]) -> Any:
    return _map_phase3_commit_refs(value, id_map, direction="to_short")


def _restore_commit_ids_from_llm(value: Any, id_map: Dict[str, Any]) -> Any:
    return _map_phase3_commit_refs(value, id_map, direction="to_full")


def _phase3_llm_commit_id_map_debug(id_map: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "short_hash_length": id_map.get("length"),
        "short_to_full": dict(id_map.get("short_to_full") or {}),
    }


def _map_phase3_commit_refs(value: Any, id_map: Dict[str, Any], *, direction: str) -> Any:
    if isinstance(value, dict):
        result: Dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            if key_text in _PHASE3_COMMIT_SCALAR_KEYS:
                result[key] = _map_phase3_commit_ref_value(item, id_map, direction=direction)
            elif key_text in _PHASE3_COMMIT_LIST_KEYS:
                result[key] = _map_phase3_commit_ref_list(item, id_map, direction=direction)
            else:
                result[key] = _map_phase3_commit_refs(item, id_map, direction=direction)
        return result
    if isinstance(value, list):
        return [_map_phase3_commit_refs(item, id_map, direction=direction) for item in value]
    return value


def _map_phase3_commit_ref_list(value: Any, id_map: Dict[str, Any], *, direction: str) -> Any:
    if not isinstance(value, list):
        return value
    result: List[Any] = []
    for item in value:
        if isinstance(item, str):
            result.append(_map_phase3_commit_ref_value(item, id_map, direction=direction))
        else:
            result.append(_map_phase3_commit_refs(item, id_map, direction=direction))
    return result


def _map_phase3_commit_ref_value(value: Any, id_map: Dict[str, Any], *, direction: str) -> Any:
    if not isinstance(value, str):
        return value
    text = value.strip()
    if not text:
        return value

    if direction == "to_short":
        mapped = (id_map.get("full_to_short") or {}).get(text)
        if mapped:
            return mapped
        if text in (id_map.get("short_to_full") or {}):
            return text
        raise ValueError(f"Unknown full commit_id for Phase 3 LLM short-hash mapping: {text}")

    mapped = (id_map.get("short_to_full") or {}).get(text)
    if mapped:
        return mapped
    if text in (id_map.get("full_to_short") or {}):
        return text
    mapped = _resolve_unique_llm_short_commit_prefix(text, id_map)
    if mapped:
        return mapped
    mapped = _resolve_unique_llm_short_commit_substitution(text, id_map)
    if mapped:
        return mapped
    raise ValueError(f"Unknown short commit_id returned by Phase 3 LLM: {text}")


def _resolve_unique_llm_short_commit_prefix(value: str, id_map: Dict[str, Any]) -> str:
    """Accept a slightly malformed LLM short hash only when it is unambiguous."""
    text = str(value or "").strip()
    if len(text) < PHASE3_LLM_SHORT_HASH_UNIQUE_PREFIX_MIN_LENGTH:
        return ""
    if not re.fullmatch(r"[0-9a-fA-F]+", text):
        return ""
    short_to_full = id_map.get("short_to_full") or {}
    for prefix_length in range(len(text), PHASE3_LLM_SHORT_HASH_UNIQUE_PREFIX_MIN_LENGTH - 1, -1):
        prefix = text[:prefix_length].lower()
        matches = [
            full_id
            for short_id, full_id in short_to_full.items()
            if str(short_id).lower().startswith(prefix)
        ]
        if len(matches) == 1:
            return matches[0]
        if len(matches) > 1:
            return ""
    return ""


def _resolve_unique_llm_short_commit_substitution(value: str, id_map: Dict[str, Any]) -> str:
    """Accept one copied hex digit error only when it points to one input commit."""
    text = str(value or "").strip().lower()
    if len(text) < PHASE3_LLM_SHORT_HASH_UNIQUE_PREFIX_MIN_LENGTH:
        return ""
    if not re.fullmatch(r"[0-9a-f]+", text):
        return ""
    matches: List[str] = []
    for short_id, full_id in (id_map.get("short_to_full") or {}).items():
        candidate = str(short_id or "").strip().lower()
        if len(candidate) != len(text):
            continue
        distance = sum(left != right for left, right in zip(candidate, text))
        if distance == 1:
            matches.append(str(full_id))
    unique_matches = sorted(set(matches))
    if len(unique_matches) == 1:
        return unique_matches[0]
    return ""


def _split_values(value: Any) -> List[str]:
    if isinstance(value, list):
        raw_values = value
    else:
        raw_values = re.split(r"[,，\s]+", str(value or ""))
    result: List[str] = []
    for item in raw_values:
        if isinstance(item, dict):
            item = item.get("commit_id") or item.get("id") or ""
        text = str(item).strip()
        if text:
            result.append(text)
    return result


def _resolve_commit_prefix(value: str, valid_commits: set[str]) -> str:
    if not value:
        return ""
    if value in valid_commits:
        return value
    matches = [commit_id for commit_id in valid_commits if commit_id.startswith(value)]
    return matches[0] if len(matches) == 1 else ""


def _unique(values: Iterable[str]) -> List[str]:
    result: List[str] = []
    seen = set()
    for value in values:
        text = str(value)
        if text and text not in seen:
            result.append(text)
            seen.add(text)
    return result


def _ordered_unique(values: Iterable[str], order: Sequence[str]) -> List[str]:
    value_set = set(values)
    ordered = [commit_id for commit_id in order if commit_id in value_set]
    return ordered + [commit_id for commit_id in _unique(values) if commit_id not in ordered]


def _make_group_id(slot: str, source_commits: Sequence[str], *, index: int = 0) -> str:
    head = _short_commit_prefix(source_commits[0]) if source_commits else str(index)
    return f"{slot.replace('.', '_')}_{head}"


def _fallback_intent(cards: Sequence[Dict[str, Any]], slot: str) -> str:
    if len(cards) == 1:
        return str(cards[0].get("commit_summary") or cards[0].get("commit_message") or "Summarize the single source commit.")[:240]
    categories = sorted({_category(card) for card in cards if _category(card)})
    module = _first_nonempty(card.get("primary_module") for card in cards) or ""
    if module:
        category_text = ", ".join(categories) or "related"
        return f"Aggregate {len(cards)} {category_text} changes related to {module}."
    return f"Aggregate {len(cards)} {', '.join(categories) or slot} changes."


def _first_nonempty(values: Iterable[Any]) -> str:
    for value in values:
        text = str(value or "").strip()
        if text:
            return text
    return ""


def _default_reason_code_for_value(value: str, card: Dict[str, Any]) -> str:
    if value == INCLUDE_DECISION:
        return _deterministic_value_decision(card)["reason_code"]
    if value == FILTER_DECISION:
        return "metadata_only"
    return "minor_maintenance"


def _reason_for_code(reason_code: str) -> str:
    return {
        "architecture_guiding": "Architecture-guiding change.",
        "architecture_supporting": "Architecture-supporting change.",
        "new_feature": "New feature or enhancement.",
        "bug_fix": "Bug fix or correctness improvement.",
        "security": "Security-related change.",
        "performance": "Performance-related change.",
        "breaking_change": "Breaking or compatibility-impacting change.",
        "api_change": "API-facing change.",
        "behavior_change": "Behavior change.",
        "build_or_runtime_impact": "Build, installation, or runtime-impacting change.",
        "compatibility": "Compatibility-related change.",
        "internal_refactoring": "Internal refactoring.",
        "tests_only": "Test-only maintenance.",
        "docs_only": "Documentation-only maintenance.",
        "ci_only": "CI-only maintenance.",
        "dependency_maintenance": "Dependency maintenance.",
        "chore": "Routine maintenance.",
        "minor_maintenance": "Minor maintenance.",
        "low_confidence_architecture_support": "Low-confidence architecture support.",
        "formatting_only": "Formatting-only change.",
        "typo_only": "Typo-only fix.",
        "comments_only": "Comment-only maintenance.",
        "lockfile_only": "Lockfile-only change.",
        "generated_only": "Generated-file-only change.",
        "version_bump_only": "Version-only update.",
        "metadata_only": "Metadata-only update.",
        "duplicate_merge_commit": "Duplicate merge or synchronization commit.",
        "trivial_docs_only": "Trivial documentation update.",
    }.get(reason_code, "Low-priority maintenance.")


def _category(record_or_card: Dict[str, Any]) -> str:
    return str(record_or_card.get("functional_category") or "unknown").lower().replace("-", "_")


def _card_text(record_or_card: Dict[str, Any]) -> str:
    return " ".join(
        [
            str(record_or_card.get("commit_message") or ""),
            str(record_or_card.get("commit_summary") or ""),
            _category(record_or_card),
            " ".join(_changed_files(record_or_card)),
        ]
    ).lower()


def _changed_files(record_or_card: Dict[str, Any]) -> List[str]:
    if "changed_files_summary" in record_or_card:
        return [str(item).replace("\\", "/") for item in record_or_card.get("changed_files_summary", {}).get("sample_files") or [] if str(item)]
    return [str(item).replace("\\", "/") for item in record_or_card.get("changed_files") or [] if str(item)]


def _basename(path: str) -> str:
    return path.replace("\\", "/").rstrip("/").split("/")[-1].lower()


def _arch_score(record_or_card: Dict[str, Any]) -> float:
    for key in ("architecture_relevance_score", "architecture_signal_score", "arch_impact_prior"):
        value = record_or_card.get(key)
        if value is None or value == "":
            continue
        try:
            return float(value)
        except Exception:
            continue
    return 0.0


def _confidence_float(value: Any) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    return {"high": 1.0, "medium": 0.6, "low": 0.25}.get(str(value or "").lower(), 0.0)


def _safe_float(value: Any) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _is_feature_category(category: str, text: str) -> bool:
    return category in {"new_feature", "feature", "enhancement"} or any(keyword in text for keyword in ("new feature", "enhance", "add support", "new api"))


def _is_bugfix_category(category: str, text: str) -> bool:
    return category in {"bug_fix", "bugfix", "fix"} or "fix" in category or any(keyword in text for keyword in ("bug", "fixes #", "fix ", "correct", "regression"))


def _is_refactoring_category(category: str, text: str) -> bool:
    return "refactor" in category or any(keyword in text for keyword in ("refactor", "cleanup", "clean up", "reorganize"))


def _is_security_related(text: str) -> bool:
    if re.search(
        r"\b(security|cve|vulnerability|authentication|authorization|auth|permission|encryption|credential|secret)\b",
        text,
    ):
        return True
    return bool(
        re.search(r"\b(access|refresh|api|auth|session|bearer)\s+token\b|\btoken\s+(auth|credential|permission|leak|secret|validation)\b", text)
    )


def _is_performance_related(text: str) -> bool:
    return any(keyword in text for keyword in ("performance", "speed", "latency", "memory", "cache", "optimize", "optimise"))


def _is_breaking_or_api_change(text: str) -> bool:
    return any(keyword in text for keyword in ("breaking", "deprecated", "deprecate", "remove api", "rename api", "api change", "behavior change", "migration", "compatibility"))


def _is_build_install_runtime_change(card: Dict[str, Any]) -> bool:
    text = _card_text(card)
    files = _changed_files(card)
    if any(keyword in text for keyword in ("packaging", "build system", "installation", "install", "runtime dependency", "platform compatibility", "cmake", "meson", "pkg-config", "setup.py", "pyproject", "package.json", "release script")):
        return True
    build_files = {
        "cmakelists.txt",
        "meson.build",
        "meson_options.txt",
        "makefile",
        "gnumakefile",
        "configure.ac",
        "setup.py",
        "pyproject.toml",
        "package.json",
        "requirements.txt",
        "cargo.toml",
        "go.mod",
        "makerelease.py",
        "vcpkg.json",
    }
    return any(
        _basename(path) in build_files
        or _basename(path).endswith((".cmake", ".mk", ".pc.in"))
        or path.lower().startswith(("pkg-config/", "release/", "scripts/", "devtools/"))
        for path in files
    )


def _is_tests_only(card: Dict[str, Any]) -> bool:
    category = _category(card)
    files = _changed_files(card)
    if category in {"test", "tests"}:
        return True
    return bool(files) and all(_is_test_path(path) for path in files)


def _is_test_path(path: str) -> bool:
    lower = path.lower()
    parts = lower.replace("\\", "/").split("/")
    basename = parts[-1]
    return (
        any(part in {"test", "tests", "__tests__", "spec", "snapshots", "snapshot"} for part in parts)
        or basename.startswith("test_")
        or "test" in basename
        or basename.endswith((".dict", ".expected", ".golden"))
    )


def _is_docs_only(card: Dict[str, Any]) -> bool:
    category = _category(card)
    files = _changed_files(card)
    if category in {"doc", "docs", "documentation"}:
        return True
    return bool(files) and all(_is_doc_path(path) for path in files)


def _is_doc_path(path: str) -> bool:
    lower = path.lower()
    basename = _basename(lower)
    doc_names = {
        "readme",
        "readme.md",
        "changelog",
        "changelog.md",
        "contributing",
        "contributing.md",
        "license",
        "license.md",
        "copying",
        "authors",
    }
    return lower.startswith(("docs/", "doc/")) or basename in doc_names or basename.endswith((".md", ".rst", ".txt", ".adoc"))


def _is_ci_only(card: Dict[str, Any]) -> bool:
    category = _category(card)
    files = _changed_files(card)
    if category in {"ci", "workflow", "tooling"}:
        return True
    return bool(files) and all(
        path.lower().startswith((".github/", ".gitlab/", ".circleci/", ".azure-pipelines/", ".travis_scripts/"))
        or _basename(path).lower() in {".travis.yml", ".gitlab-ci.yml", "appveyor.yml", ".appveyor.yml", "azure-pipelines.yml"}
        or "workflow" in path.lower()
        or "ci" in _basename(path)
        for path in files
    )


def _is_formatting_only(card: Dict[str, Any]) -> bool:
    category = _category(card)
    text = _card_text(card)
    strong_value = _is_feature_category(category, text) or _is_bugfix_category(category, text) or _is_breaking_or_api_change(text)
    pure_markers = ("formatting-only", "format only", "whitespace-only", "indentation-only", "run clang-format", "clang-format only", "prettier", "gofmt")
    if category in {"formatting", "format"}:
        return True
    return not strong_value and any(marker in text for marker in pure_markers)


def _is_typo_only(card: Dict[str, Any]) -> bool:
    category = _category(card)
    text = _card_text(card)
    return category in {"typo", "spelling"} or any(keyword in text for keyword in ("typo-only", "spelling-only", "spelling fix"))


def _is_generated_only(card: Dict[str, Any]) -> bool:
    files = _changed_files(card)
    text = _card_text(card)
    if "auto-generated" in text or "generated files only" in text:
        return True
    return bool(files) and all("generated" in path.lower() or path.lower().startswith(("dist/", "build/")) or "snapshot" in path.lower() for path in files)


def _is_lockfile_only(card: Dict[str, Any]) -> bool:
    files = _changed_files(card)
    lockfiles = {"package-lock.json", "yarn.lock", "pnpm-lock.yaml", "cargo.lock", "go.sum", "poetry.lock", "pipfile.lock"}
    return bool(files) and all(_basename(path) in lockfiles for path in files)


def _is_version_or_metadata_only(card: Dict[str, Any]) -> bool:
    text = _card_text(card)
    files = _changed_files(card)
    if any(keyword in text for keyword in ("version bump only", "metadata only", "badge update", "copyright year")):
        return True
    return bool(files) and all(_basename(path) in {"version", "version.txt", "metadata.json", "manifest.json"} for path in files)


def _export(output: Dict[str, Any], audit: Dict[str, Any], intermediates: Dict[str, Any], output_dir: Path) -> Dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_files: Dict[str, str] = {}
    for key, payload in intermediates.items():
        path = output_dir / f"{key}.json"
        _write_json(path, {"generated_at": output["generated_at"], **payload})
        output_files[key] = str(path)

    aggregation_path = output_dir / "aggregation_plan.json"
    debug_path = output_dir / "aggregation_plan_debug.md"
    audit_path = output_dir / "phase3_aggregation_plan_llm_audit.json"
    _write_json(aggregation_path, output)
    _write_json(audit_path, audit)
    debug_path.write_text(_render_debug(output, audit), encoding="utf-8")
    llm_io_path = export_phase3_aggregation_llm_io(audit, llm_io_dir(output_dir))
    output_files.update(
        {
            "aggregation_plan": str(aggregation_path),
            "aggregation_plan_debug": str(debug_path),
            "phase3_aggregation_plan_llm_audit": str(audit_path),
        }
    )
    if llm_io_path:
        output_files["phase3_1_llm_input_output_txt"] = llm_io_path
    return output_files


def _render_debug(output: Dict[str, Any], audit: Dict[str, Any]) -> str:
    coverage = output.get("aggregation_plan", {}).get("coverage_report", {})
    return "\n".join(
        [
            "# Phase 3.1 Multi-stage Aggregation Planning Debug",
            "",
            f"- generation_mode: `{output['stats']['generation_mode']}`",
            f"- llm_call_count: `{len(audit.get('calls') or [])}`",
            f"- group_count: `{output['stats']['group_count']}`",
            f"- total_commits: `{coverage.get('total_commits', 0)}`",
            f"- included_commits: `{coverage.get('included_commits', 0)}`",
            f"- deprioritized_commits: `{coverage.get('deprioritized_commits', 0)}`",
            f"- filtered_commits: `{coverage.get('filtered_commits', 0)}`",
            f"- unassigned_commits: `{len(coverage.get('unassigned_commits') or [])}`",
            f"- warning_count: `{len(output.get('aggregation_plan', {}).get('warnings') or [])}`",
            "",
        ]
    )


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))
