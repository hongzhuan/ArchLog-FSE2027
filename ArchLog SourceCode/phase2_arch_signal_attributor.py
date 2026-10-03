from __future__ import annotations

import json
import math
import os
import re
import threading
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Set, Tuple

from arcrn_models import PhasePipelineResult, utc_now_iso
from arcrn_metrics import mark_llm_metric_attempt, normalize_llm_metrics
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


EPS = 1e-8
SUPPORTED_EVENT_TYPES = {
    "module_added",
    "module_removed",
    "module_changed",
    "component_changed",
}
FEATURE_NAMES = [
    "file_overlap",
    "module_match",
    "component_match",
    "operation_match",
    "semantic_support",
    "negative_evidence",
]
PROTECTED_EVENT_TYPES = {"module_added", "module_removed"}
DEFAULT_EVENT_PROFILE_PROMPT = Path(__file__).resolve().parent / "prompts" / "phase2_arch_event_profile_prompt.txt"
DEFAULT_ARCH_RELEVANCE_PROMPT = (
    Path(__file__).resolve().parent / "prompts" / "phase2_arch_relevance_classification_prompt.txt"
)
DEFAULT_SUMMARY_DIFF_ONLY_PROMPT = (
    Path(__file__).resolve().parent / "prompts" / "phase2_arch_relevance_summary_diff_only_prompt.txt"
)
PHASE2_ABLATION_FULL = "full"
PHASE2_ABLATION_NO_ARCH_RELEVANCE = "no_phase2_arch_relevance"
PHASE2_ABLATION_SUMMARY_DIFF_ONLY = "summary_diff_only"
EVIDENCE_SCORE_NAMES = [
    "contract_surface_score",
    "core_area_score",
    "cross_area_score",
    "event_alignment_score",
    "change_intent_score",
    "negative_evidence_score",
]
POSITIVE_EVIDENCE_WEIGHTS = {
    "contract_surface_score": 0.30,
    "core_area_score": 0.25,
    "cross_area_score": 0.15,
    "event_alignment_score": 0.20,
    "change_intent_score": 0.10,
}
ARCH_RELEVANCE_LEVELS = {"high", "medium", "low", "none"}
STRUCTURE_ROLES = {"structure_guiding", "architecture_related_supporting", "local_supporting"}
_PHASE2_VALIDATION_RETRY_AUDIT_LOCK = threading.Lock()
_PHASE2_LLM_METRICS_LOCK = threading.Lock()


def _phase2_log_start(step_name: str) -> float:
    print(f"[Phase2] Starting {step_name} ...", flush=True)
    return time.perf_counter()


def _phase2_log_done(step_name: str, started_at: float, detail: str = "") -> None:
    suffix = f" ({detail})" if detail else ""
    print(f"[Phase2] Finished {step_name}{suffix} in {time.perf_counter() - started_at:.1f}s.", flush=True)


@dataclass
class ArchitectureEvent:
    event_id: str
    event_type: str
    module: str = ""
    component: str = ""
    related_files: List[str] = field(default_factory=list)
    added_files: List[str] = field(default_factory=list)
    removed_files: List[str] = field(default_factory=list)
    modified_files: List[str] = field(default_factory=list)
    summary: str = ""
    significance: float = 0.5
    source_confidence: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class SemArcMappingIndex:
    file_to_module: Dict[str, str] = field(default_factory=dict)
    file_to_component: Dict[str, str] = field(default_factory=dict)
    module_to_files: Dict[str, Set[str]] = field(default_factory=dict)
    component_to_modules: Dict[str, Set[str]] = field(default_factory=dict)
    _module_exact_lookup: Dict[str, str] = field(init=False, default_factory=dict, repr=False)
    _module_suffix_candidates: List[Tuple[str, str]] = field(init=False, default_factory=list, repr=False)
    _module_lookup_cache: Dict[str, Optional[str]] = field(init=False, default_factory=dict, repr=False)
    _component_exact_lookup: Dict[str, str] = field(init=False, default_factory=dict, repr=False)
    _component_suffix_candidates: List[Tuple[str, str]] = field(init=False, default_factory=list, repr=False)
    _component_lookup_cache: Dict[str, Optional[str]] = field(init=False, default_factory=dict, repr=False)

    def __post_init__(self) -> None:
        self._module_exact_lookup, self._module_suffix_candidates = _build_path_lookup_index(self.file_to_module)
        self._component_exact_lookup, self._component_suffix_candidates = _build_path_lookup_index(self.file_to_component)

    def module_for_file(self, path: str) -> Optional[str]:
        return _lookup_path_index(
            exact_lookup=self._module_exact_lookup,
            suffix_candidates=self._module_suffix_candidates,
            lookup_cache=self._module_lookup_cache,
            path=path,
        )

    def component_for_file(self, path: str) -> Optional[str]:
        return _lookup_path_index(
            exact_lookup=self._component_exact_lookup,
            suffix_candidates=self._component_suffix_candidates,
            lookup_cache=self._component_lookup_cache,
            path=path,
        )


def run_phase2_arch_signal_attribution(
    *,
    change_records_path: Path,
    diff_ir_path: Path,
    namedclusters_new_path: Path,
    clustercomponent_new_path: Path,
    output_dir: Path,
    namedclusters_old_path: Optional[Path] = None,
    clustercomponent_old_path: Optional[Path] = None,
    archsem_old_path: Optional[Path] = None,
    archsem_new_path: Optional[Path] = None,
    codesem_old_path: Optional[Path] = None,
    codesem_new_path: Optional[Path] = None,
    diff_summary_path: Optional[Path] = None,
    config=None,
) -> PhasePipelineResult:
    step_started = _phase2_log_start("loading change records")
    phase1_payload = _load_json(change_records_path)
    records = _normalize_change_records(phase1_payload)
    _phase2_log_done("loading change records", step_started, f"{len(records)} record(s)")

    ablation_mode = _phase2_ablation_mode(config)
    if ablation_mode == PHASE2_ABLATION_NO_ARCH_RELEVANCE:
        return _run_phase2_no_arch_relevance_ablation(
            records=records,
            change_records_path=change_records_path,
            diff_ir_path=diff_ir_path,
            namedclusters_new_path=namedclusters_new_path,
            clustercomponent_new_path=clustercomponent_new_path,
            output_dir=output_dir,
            namedclusters_old_path=namedclusters_old_path,
            clustercomponent_old_path=clustercomponent_old_path,
            archsem_old_path=archsem_old_path,
            archsem_new_path=archsem_new_path,
            codesem_old_path=codesem_old_path,
            codesem_new_path=codesem_new_path,
            diff_summary_path=diff_summary_path,
        )
    if ablation_mode == PHASE2_ABLATION_SUMMARY_DIFF_ONLY:
        return _run_phase2_summary_diff_only_ablation(
            records=records,
            change_records_path=change_records_path,
            diff_ir_path=diff_ir_path,
            namedclusters_new_path=namedclusters_new_path,
            clustercomponent_new_path=clustercomponent_new_path,
            output_dir=output_dir,
            namedclusters_old_path=namedclusters_old_path,
            clustercomponent_old_path=clustercomponent_old_path,
            archsem_old_path=archsem_old_path,
            archsem_new_path=archsem_new_path,
            codesem_old_path=codesem_old_path,
            codesem_new_path=codesem_new_path,
            diff_summary_path=diff_summary_path,
            config=config,
        )

    step_started = _phase2_log_start("building SemArc mapping index")
    mapping_index = build_semarc_mapping_index(
        namedclusters_new_path=namedclusters_new_path,
        clustercomponent_new_path=clustercomponent_new_path,
        namedclusters_old_path=namedclusters_old_path,
        clustercomponent_old_path=clustercomponent_old_path,
    )
    _phase2_log_done(
        "building SemArc mapping index",
        step_started,
        f"{len(mapping_index.file_to_module)} file-to-module mapping(s), "
        f"{len(mapping_index.file_to_component)} file-to-component mapping(s)",
    )

    step_started = _phase2_log_start("loading architecture events")
    events = build_architecture_event_index(diff_ir_path)
    _phase2_log_done("loading architecture events", step_started, f"{len(events)} event(s)")

    step_started = _phase2_log_start("estimating architecture impact priors")
    priors, prior_debug = _estimate_arch_impact_prior_with_features(records, mapping_index)
    _phase2_log_done("estimating architecture impact priors", step_started, f"{len(priors)} prior score(s)")

    step_started = _phase2_log_start("building commit-event evidence matrix")
    evidence_matrix = _build_evidence_matrix(records, events, mapping_index, config=config)
    _phase2_log_done(
        "building commit-event evidence matrix",
        step_started,
        f"{len(events)} event(s) x {len(records)} commit record(s)",
    )

    step_started = _phase2_log_start("computing feature reliabilities")
    reliability_by_event = _compute_feature_reliabilities(events, records, evidence_matrix)
    _phase2_log_done("computing feature reliabilities", step_started, f"{len(reliability_by_event)} event(s)")

    step_started = _phase2_log_start("computing event posterior matrix")
    posterior_matrix = _compute_event_posteriors(records, events, priors, evidence_matrix, reliability_by_event)
    _phase2_log_done("computing event posterior matrix", step_started, f"{len(posterior_matrix)} event(s)")

    step_started = _phase2_log_start("computing event confidences")
    event_confidences = _compute_event_confidences(records, events, posterior_matrix)
    _phase2_log_done("computing event confidences", step_started, f"{len(event_confidences)} confidence score(s)")

    step_started = _phase2_log_start("computing event role sets")
    event_sets = _compute_event_role_sets(records, events, posterior_matrix)
    _phase2_log_done("computing event role sets", step_started, f"{len(event_sets)} event set(s)")

    step_started = _phase2_log_start("assigning deterministic structure roles")
    role_debug = _assign_structure_roles(
        records=records,
        events=events,
        priors=priors,
        prior_debug=prior_debug,
        evidence_matrix=evidence_matrix,
        posterior_matrix=posterior_matrix,
        event_confidences=event_confidences,
        event_sets=event_sets,
        mapping_index=mapping_index,
    )
    _phase2_log_done("assigning deterministic structure roles", step_started, f"{len(role_debug)} commit role record(s)")

    phase2_llm_enabled = _phase2_arch_relevance_enabled(config)
    event_profile_llm_enabled = _phase2_event_profile_enabled(config) and bool(events)
    phase2_validation_retry_audit: List[Dict[str, Any]] = []
    phase2_llm_call_metrics: List[Dict[str, Any]] = []
    llm_client = None
    rate_limiter = None
    if phase2_llm_enabled or event_profile_llm_enabled:
        step_started = _phase2_log_start("building Phase2 LLM client")
        _ensure_phase2_api_key(config)
        llm_client = maybe_build_llm_client(config)
        if llm_client is None:
            raise RuntimeError("Phase 2 LLM is enabled, but no OpenAI-compatible LLM client could be created.")
        rate_limiter = TokenBucketRateLimiter(
            qps=getattr(config, "step10_rate_limit_qps", None),
            burst=int(getattr(config, "step10_rate_limit_burst", 1)),
        )
        _phase2_log_done("building Phase2 LLM client", step_started)

    step_started = _phase2_log_start("building architecture event profiles")
    event_profiles = _build_arch_event_profiles(
        events=events,
        mapping_index=mapping_index,
        config=config,
        llm_client=llm_client,
        rate_limiter=rate_limiter,
        output_dir=output_dir,
        validation_retry_audit=phase2_validation_retry_audit,
        llm_call_metrics=phase2_llm_call_metrics,
    )
    _phase2_log_done("building architecture event profiles", step_started, f"{len(event_profiles)} profile(s)")

    step_started = _phase2_log_start("building architecture evidence cards")
    evidence_cards = _build_architecture_evidence_cards(
        records=records,
        events=events,
        priors=priors,
        prior_debug=prior_debug,
        evidence_matrix=evidence_matrix,
        posterior_matrix=posterior_matrix,
        event_confidences=event_confidences,
        event_sets=event_sets,
        role_debug=role_debug,
        mapping_index=mapping_index,
        event_profiles=event_profiles,
    )
    _phase2_log_done("building architecture evidence cards", step_started, f"{len(evidence_cards)} card(s)")

    step_started = _phase2_log_start("checking evidence score distributions")
    feature_distribution_debug = _feature_distribution_debug(evidence_cards)
    _attach_bayesian_evidence_scores(evidence_cards, feature_distribution_debug)
    _phase2_log_done("checking evidence score distributions", step_started)

    step_started = _phase2_log_start("classifying architecture relevance")
    llm_decisions = _classify_architecture_relevance(
        evidence_cards=evidence_cards,
        enabled=phase2_llm_enabled,
        config=config,
        llm_client=llm_client,
        rate_limiter=rate_limiter,
        output_dir=output_dir,
        validation_retry_audit=phase2_validation_retry_audit,
        llm_call_metrics=phase2_llm_call_metrics,
    )
    _phase2_log_done("classifying architecture relevance", step_started, f"{len(llm_decisions)} decision(s)")
    evidence_card_by_id = {str(card.get("commit_id") or ""): card for card in evidence_cards}
    decision_by_id = {str(decision.get("commit_id") or ""): decision for decision in llm_decisions}

    step_started = _phase2_log_start("assembling attributed change records")
    output_records = [
        _build_output_record(
            record=record,
            events=events,
            priors=priors,
            posterior_matrix=posterior_matrix,
            event_confidences=event_confidences,
            event_sets=event_sets,
            evidence_matrix=evidence_matrix,
            reliability_by_event=reliability_by_event,
            role_debug=role_debug,
            mapping_index=mapping_index,
            evidence_card=evidence_card_by_id.get(str(record.get("commit_id") or ""), {}),
            llm_decision=decision_by_id.get(str(record.get("commit_id") or ""), {}),
        )
        for record in records
    ]
    _phase2_log_done("assembling attributed change records", step_started, f"{len(output_records)} record(s)")

    output = {
        "generated_at": utc_now_iso(),
        "algorithm": "posterior_architecture_signal_attribution",
        "source_change_records_path": str(change_records_path),
        "source_arch_inputs": {
            "diff_ir": str(diff_ir_path),
            "diff_summary": str(diff_summary_path or ""),
            "namedclusters_old": str(namedclusters_old_path or ""),
            "clustercomponent_old": str(clustercomponent_old_path or ""),
            "namedclusters_new": str(namedclusters_new_path),
            "clustercomponent_new": str(clustercomponent_new_path),
            "archsem_old": str(archsem_old_path or ""),
            "archsem_new": str(archsem_new_path or ""),
            "codesem_old": str(codesem_old_path or ""),
            "codesem_new": str(codesem_new_path or ""),
        },
        "attribution_model": {
            "posterior": "P(c|e) proportional to P(e|c) * P(c), normalized per architecture event.",
            "architecture_signal_score": "Backward-compatible posterior/bayesian evidence signal, not the final architecture relevance judgment.",
            "architecture_relevance_score": "Final commit-level architecture relevance score judged by Phase 2 LLM when enabled.",
            "feature_reliability": "IQR-based per-event feature reliability gating.",
            "llm_architecture_relevance_enabled": phase2_llm_enabled,
        },
        "attributed_change_records": output_records,
        "stats": _stats(output_records, events),
    }

    debug_payloads = {
        "architecture_events_index": [event.to_dict() for event in events],
        "commit_event_evidence_matrix": _debug_evidence_matrix(records, events, evidence_matrix),
        "event_posterior_matrix": _debug_posterior_matrix(
            records,
            events,
            posterior_matrix,
            reliability_by_event,
            event_confidences,
        ),
        "phase2_role_assignment_debug": {
            "prior_features": prior_debug,
            "role_assignments": role_debug,
            "event_sets": event_sets,
        },
        "architecture_event_profiles": event_profiles,
        "architecture_evidence_cards": evidence_cards,
        "phase2_llm_arch_relevance_decisions": llm_decisions,
        "phase2_llm_validation_retry_audit": {"attempts": phase2_validation_retry_audit},
        "phase2_llm_call_metrics": phase2_llm_call_metrics,
        "phase2_feature_distribution_debug": feature_distribution_debug,
    }
    step_started = _phase2_log_start("exporting Phase2 outputs")
    output_files = _export(output, debug_payloads, output_dir)
    _phase2_log_done("exporting Phase2 outputs", step_started, f"{len(output_files)} file(s)")
    return PhasePipelineResult(output_files=output_files, stats=output["stats"])


def _run_phase2_no_arch_relevance_ablation(
    *,
    records: Sequence[Dict[str, Any]],
    change_records_path: Path,
    diff_ir_path: Path,
    namedclusters_new_path: Path,
    clustercomponent_new_path: Path,
    output_dir: Path,
    namedclusters_old_path: Optional[Path],
    clustercomponent_old_path: Optional[Path],
    archsem_old_path: Optional[Path],
    archsem_new_path: Optional[Path],
    codesem_old_path: Optional[Path],
    codesem_new_path: Optional[Path],
    diff_summary_path: Optional[Path],
) -> PhasePipelineResult:
    step_started = _phase2_log_start("running no-architecture-relevance ablation")
    empty_events: List[ArchitectureEvent] = []
    empty_mapping = SemArcMappingIndex()
    priors = {str(record.get("commit_id") or ""): 0.0 for record in records}
    evidence_cards = [_neutral_arch_evidence_card(record) for record in records]
    decisions = [_neutral_arch_relevance_decision(card) for card in evidence_cards]
    evidence_card_by_id = {str(card.get("commit_id") or ""): card for card in evidence_cards}
    decision_by_id = {str(decision.get("commit_id") or ""): decision for decision in decisions}
    output_records = [
        _build_output_record(
            record=record,
            events=empty_events,
            priors=priors,
            posterior_matrix={},
            event_confidences={},
            event_sets={},
            evidence_matrix={},
            reliability_by_event={},
            role_debug={},
            mapping_index=empty_mapping,
            evidence_card=evidence_card_by_id.get(str(record.get("commit_id") or ""), {}),
            llm_decision=decision_by_id.get(str(record.get("commit_id") or ""), {}),
        )
        for record in records
    ]
    output = _phase2_output_payload(
        change_records_path=change_records_path,
        diff_ir_path=diff_ir_path,
        diff_summary_path=diff_summary_path,
        namedclusters_old_path=namedclusters_old_path,
        clustercomponent_old_path=clustercomponent_old_path,
        namedclusters_new_path=namedclusters_new_path,
        clustercomponent_new_path=clustercomponent_new_path,
        archsem_old_path=archsem_old_path,
        archsem_new_path=archsem_new_path,
        codesem_old_path=codesem_old_path,
        codesem_new_path=codesem_new_path,
        output_records=output_records,
        events=empty_events,
        llm_enabled=False,
        ablation_mode=PHASE2_ABLATION_NO_ARCH_RELEVANCE,
    )
    debug_payloads = {
        "architecture_events_index": [],
        "commit_event_evidence_matrix": {},
        "event_posterior_matrix": {},
        "phase2_role_assignment_debug": {"prior_features": {}, "role_assignments": {}, "event_sets": {}},
        "architecture_event_profiles": {},
        "architecture_evidence_cards": evidence_cards,
        "phase2_llm_arch_relevance_decisions": decisions,
        "phase2_llm_validation_retry_audit": {"attempts": []},
        "phase2_llm_call_metrics": [],
        "phase2_feature_distribution_debug": {},
        "phase2_ablation_debug": {
            "mode": PHASE2_ABLATION_NO_ARCH_RELEVANCE,
            "description": "Phase 2 architecture relevance judgment is disabled; every commit receives architecture_relevance_level=none.",
        },
    }
    output_files = _export(output, debug_payloads, output_dir)
    _phase2_log_done("running no-architecture-relevance ablation", step_started, f"{len(output_records)} record(s)")
    return PhasePipelineResult(output_files=output_files, stats=output["stats"])


def _run_phase2_summary_diff_only_ablation(
    *,
    records: Sequence[Dict[str, Any]],
    change_records_path: Path,
    diff_ir_path: Path,
    namedclusters_new_path: Path,
    clustercomponent_new_path: Path,
    output_dir: Path,
    namedclusters_old_path: Optional[Path],
    clustercomponent_old_path: Optional[Path],
    archsem_old_path: Optional[Path],
    archsem_new_path: Optional[Path],
    codesem_old_path: Optional[Path],
    codesem_new_path: Optional[Path],
    diff_summary_path: Optional[Path],
    config,
) -> PhasePipelineResult:
    step_started = _phase2_log_start("running summary-and-diff-only ablation")
    _ensure_phase2_api_key(config)
    llm_client = maybe_build_llm_client(config)
    if llm_client is None:
        raise RuntimeError("Phase 2 summary/diff-only ablation requires an OpenAI-compatible LLM client.")
    rate_limiter = TokenBucketRateLimiter(
        qps=getattr(config, "step10_rate_limit_qps", None),
        burst=int(getattr(config, "step10_rate_limit_burst", 1)),
    )
    empty_events: List[ArchitectureEvent] = []
    empty_mapping = SemArcMappingIndex()
    priors = {str(record.get("commit_id") or ""): 0.0 for record in records}
    evidence_cards = [_summary_diff_only_evidence_card(record) for record in records]
    feature_distribution_debug = _feature_distribution_debug(evidence_cards)
    _attach_bayesian_evidence_scores(evidence_cards, feature_distribution_debug)
    validation_retry_audit: List[Dict[str, Any]] = []
    llm_call_metrics: List[Dict[str, Any]] = []
    decisions = _classify_architecture_relevance(
        evidence_cards=evidence_cards,
        enabled=True,
        config=config,
        llm_client=llm_client,
        rate_limiter=rate_limiter,
        output_dir=output_dir,
        validation_retry_audit=validation_retry_audit,
        llm_call_metrics=llm_call_metrics,
    )
    evidence_card_by_id = {str(card.get("commit_id") or ""): card for card in evidence_cards}
    decision_by_id = {str(decision.get("commit_id") or ""): decision for decision in decisions}
    output_records = [
        _build_output_record(
            record=record,
            events=empty_events,
            priors=priors,
            posterior_matrix={},
            event_confidences={},
            event_sets={},
            evidence_matrix={},
            reliability_by_event={},
            role_debug={},
            mapping_index=empty_mapping,
            evidence_card=evidence_card_by_id.get(str(record.get("commit_id") or ""), {}),
            llm_decision=decision_by_id.get(str(record.get("commit_id") or ""), {}),
        )
        for record in records
    ]
    output = _phase2_output_payload(
        change_records_path=change_records_path,
        diff_ir_path=diff_ir_path,
        diff_summary_path=diff_summary_path,
        namedclusters_old_path=namedclusters_old_path,
        clustercomponent_old_path=clustercomponent_old_path,
        namedclusters_new_path=namedclusters_new_path,
        clustercomponent_new_path=clustercomponent_new_path,
        archsem_old_path=archsem_old_path,
        archsem_new_path=archsem_new_path,
        codesem_old_path=codesem_old_path,
        codesem_new_path=codesem_new_path,
        output_records=output_records,
        events=empty_events,
        llm_enabled=True,
        ablation_mode=PHASE2_ABLATION_SUMMARY_DIFF_ONLY,
    )
    debug_payloads = {
        "architecture_events_index": [],
        "commit_event_evidence_matrix": {},
        "event_posterior_matrix": {},
        "phase2_role_assignment_debug": {"prior_features": {}, "role_assignments": {}, "event_sets": {}},
        "architecture_event_profiles": {},
        "architecture_evidence_cards": evidence_cards,
        "phase2_llm_arch_relevance_decisions": decisions,
        "phase2_llm_validation_retry_audit": {"attempts": validation_retry_audit},
        "phase2_llm_call_metrics": llm_call_metrics,
        "phase2_feature_distribution_debug": feature_distribution_debug,
        "phase2_ablation_debug": {
            "mode": PHASE2_ABLATION_SUMMARY_DIFF_ONLY,
            "description": "Phase 2 LLM receives only commit summary, changed files/methods, and diff evidence; SemArc, architecture events, and component evidence are withheld.",
        },
    }
    output_files = _export(output, debug_payloads, output_dir)
    _phase2_log_done("running summary-and-diff-only ablation", step_started, f"{len(output_records)} record(s)")
    return PhasePipelineResult(output_files=output_files, stats=output["stats"])


def _phase2_output_payload(
    *,
    change_records_path: Path,
    diff_ir_path: Path,
    diff_summary_path: Optional[Path],
    namedclusters_old_path: Optional[Path],
    clustercomponent_old_path: Optional[Path],
    namedclusters_new_path: Path,
    clustercomponent_new_path: Path,
    archsem_old_path: Optional[Path],
    archsem_new_path: Optional[Path],
    codesem_old_path: Optional[Path],
    codesem_new_path: Optional[Path],
    output_records: Sequence[Dict[str, Any]],
    events: Sequence[ArchitectureEvent],
    llm_enabled: bool,
    ablation_mode: str,
) -> Dict[str, Any]:
    output = {
        "generated_at": utc_now_iso(),
        "algorithm": "posterior_architecture_signal_attribution",
        "source_change_records_path": str(change_records_path),
        "source_arch_inputs": {
            "diff_ir": str(diff_ir_path),
            "diff_summary": str(diff_summary_path or ""),
            "namedclusters_old": str(namedclusters_old_path or ""),
            "clustercomponent_old": str(clustercomponent_old_path or ""),
            "namedclusters_new": str(namedclusters_new_path),
            "clustercomponent_new": str(clustercomponent_new_path),
            "archsem_old": str(archsem_old_path or ""),
            "archsem_new": str(archsem_new_path or ""),
            "codesem_old": str(codesem_old_path or ""),
            "codesem_new": str(codesem_new_path or ""),
        },
        "attribution_model": {
            "posterior": "P(c|e) proportional to P(e|c) * P(c), normalized per architecture event.",
            "architecture_signal_score": "Backward-compatible posterior/bayesian evidence signal, not the final architecture relevance judgment.",
            "architecture_relevance_score": "Final commit-level architecture relevance score judged by Phase 2 LLM when enabled.",
            "feature_reliability": "IQR-based per-event feature reliability gating.",
            "llm_architecture_relevance_enabled": llm_enabled,
            "ablation_mode": ablation_mode,
        },
        "attributed_change_records": list(output_records),
        "stats": _stats(output_records, events),
    }
    output["stats"]["phase2_ablation_mode"] = ablation_mode
    return output


def build_architecture_event_index(diff_ir_path: Optional[Path]) -> List[ArchitectureEvent]:
    payload = _load_json(_resolve_diff_ir_path(diff_ir_path))
    raw_events = _iter_raw_events(payload)
    events: List[ArchitectureEvent] = []
    for index, raw_event in enumerate(raw_events, start=1):
        if not isinstance(raw_event, dict):
            continue
        detail = raw_event.get("detail") if isinstance(raw_event.get("detail"), dict) else {}
        event_type = _normalize_event_type(
            raw_event.get("type")
            or raw_event.get("event_type")
            or raw_event.get("change_type")
            or detail.get("type")
            or detail.get("event_type")
        )
        module = _first_text(
            detail.get("module_name"),
            raw_event.get("module"),
            raw_event.get("module_name"),
            detail.get("to_name"),
            detail.get("from_name"),
            _strip_module_uid(detail.get("module_uid")),
            _strip_module_uid(detail.get("to_module_uid")),
            _strip_module_uid(detail.get("from_module_uid")),
        )
        component = _extract_component(raw_event, detail)

        added_files = _unique_paths(
            _extract_files(raw_event, ("added_files", "added", "new_files"))
            + _extract_files(detail, ("added_files", "added", "new_files"))
            + _extract_semantic_code_files(detail, ("added_files", "new_files"))
            + _extract_files(detail.get("examples") or {}, ("added_files_top", "added_files"))
        )
        removed_files = _unique_paths(
            _extract_files(raw_event, ("removed_files", "deleted_files", "removed", "deleted", "old_files"))
            + _extract_files(detail, ("removed_files", "deleted_files", "removed", "deleted", "old_files"))
            + _extract_semantic_code_files(detail, ("removed_files", "deleted_files", "old_files"))
            + _extract_files(detail.get("examples") or {}, ("removed_files_top", "deleted_files_top", "removed_files"))
        )
        modified_files = _unique_paths(
            _extract_files(raw_event, ("modified_files", "changed_files", "related_files", "files"))
            + _extract_files(detail, ("modified_files", "changed_files", "related_files", "files"))
            + _extract_semantic_code_files(detail, ("modified_files", "changed_files"))
            + _extract_files(detail.get("examples") or {}, ("modified_files_top", "changed_files_top"))
        )
        related_files = _unique_paths(
            _extract_files(raw_event, ("related_files", "files"))
            + _extract_files(detail, ("related_files", "files"))
            + added_files
            + removed_files
            + modified_files
        )

        significance = _safe_float(
            detail.get("architecture_significance"),
            detail.get("significance"),
            raw_event.get("architecture_significance"),
            raw_event.get("significance"),
            default=0.5,
        )
        source_confidence = _safe_float(raw_event.get("confidence"), detail.get("confidence"), default=0.0)
        summary = str(raw_event.get("summary") or detail.get("summary") or "").strip()
        if not summary:
            subject = module or component or "unknown"
            summary = f"{event_type} {subject}"
        event_id = str(raw_event.get("id") or raw_event.get("event_id") or "").strip()
        if not event_id:
            subject = _slug(module or component or "unknown")
            event_id = f"{event_type}:{subject}:{index}"

        events.append(
            ArchitectureEvent(
                event_id=event_id,
                event_type=event_type,
                module=module,
                component=component,
                related_files=related_files,
                added_files=added_files,
                removed_files=removed_files,
                modified_files=modified_files,
                summary=summary,
                significance=_clip(significance, 0.0, 1.0),
                source_confidence=_clip(source_confidence, 0.0, 1.0),
            )
        )
    return events


def build_semarc_mapping_index(
    *,
    namedclusters_new_path: Optional[Path],
    clustercomponent_new_path: Optional[Path],
    namedclusters_old_path: Optional[Path] = None,
    clustercomponent_old_path: Optional[Path] = None,
) -> SemArcMappingIndex:
    module_to_files: Dict[str, Set[str]] = defaultdict(set)
    for path in (namedclusters_old_path, namedclusters_new_path):
        for module, files in _parse_namedclusters(path).items():
            module_to_files[module].update(files)

    component_to_modules: Dict[str, Set[str]] = defaultdict(set)
    for path in (clustercomponent_old_path, clustercomponent_new_path):
        for component, modules in _parse_clustercomponent(path).items():
            component_to_modules[component].update(modules)

    file_to_module: Dict[str, str] = {}
    for module, files in module_to_files.items():
        for file_path in files:
            file_to_module.setdefault(file_path, module)

    module_to_components: Dict[str, Set[str]] = defaultdict(set)
    for component, modules in component_to_modules.items():
        for module in modules:
            module_to_components[module].add(component)

    file_to_component: Dict[str, str] = {}
    for module, files in module_to_files.items():
        components = sorted(module_to_components.get(module) or [])
        if not components:
            continue
        component = components[0]
        for file_path in files:
            file_to_component.setdefault(file_path, component)

    return SemArcMappingIndex(
        file_to_module=file_to_module,
        file_to_component=file_to_component,
        module_to_files={module: set(files) for module, files in module_to_files.items()},
        component_to_modules={component: set(modules) for component, modules in component_to_modules.items()},
    )


def estimate_arch_impact_prior(records: Sequence[Dict[str, Any]], mapping_index: SemArcMappingIndex) -> Dict[str, float]:
    priors, _ = _estimate_arch_impact_prior_with_features(records, mapping_index)
    return priors


def extract_commit_event_evidence(
    record: Dict[str, Any],
    event: ArchitectureEvent,
    mapping_index: SemArcMappingIndex,
    record_context: Optional[Dict[str, Any]] = None,
    event_context: Optional[Dict[str, Any]] = None,
) -> Dict[str, float]:
    if record_context is None:
        record_context = _record_lookup_context(record, mapping_index)
    if event_context is None:
        event_context = _event_lookup_context(event, mapping_index)

    ops = record_context["ops"]
    changed_files = record_context["changed_files"]
    event_files = event.related_files
    file_overlap = _f1_overlap(changed_files, event_files)

    commit_modules = record_context["modules"]
    event_modules = event_context["modules"]
    module_match = 1.0 if commit_modules and event_modules and _names_intersect(commit_modules, event_modules) else 0.0

    commit_components = record_context["components"]
    event_components = event_context["components"]
    component_match = (
        1.0 if commit_components and event_components and _names_intersect(commit_components, event_components) else 0.0
    )

    operation_match = _operation_match(ops, event, file_overlap, component_match)
    semantic_support = 0.0
    negative_evidence = _negative_evidence(record, changed_files)

    return {
        "file_overlap": _round(file_overlap),
        "module_match": _round(module_match),
        "component_match": _round(component_match),
        "operation_match": _round(operation_match),
        "semantic_support": _round(semantic_support),
        "negative_evidence": _round(negative_evidence),
    }


def _record_lookup_context(record: Dict[str, Any], mapping_index: SemArcMappingIndex) -> Dict[str, Any]:
    ops = _record_file_ops(record)
    changed_files = ops["changed_files"]
    modules = {
        module
        for module in (mapping_index.module_for_file(file_path) for file_path in changed_files)
        if module
    }
    components = {
        component
        for component in (mapping_index.component_for_file(file_path) for file_path in changed_files)
        if component
    }
    return {
        "ops": ops,
        "changed_files": changed_files,
        "modules": modules,
        "components": components,
    }


def _event_lookup_context(event: ArchitectureEvent, mapping_index: SemArcMappingIndex) -> Dict[str, Any]:
    modules = {
        module
        for module in (mapping_index.module_for_file(file_path) for file_path in event.related_files)
        if module
    }
    if event.module:
        modules.add(event.module)
    components = {
        component
        for component in (mapping_index.component_for_file(file_path) for file_path in event.related_files)
        if component
    }
    if event.component:
        components.add(event.component)
    return {
        "modules": modules,
        "components": components,
    }


def _normalize_change_records(payload: Any) -> List[Dict[str, Any]]:
    raw_records = payload.get("change_records") if isinstance(payload, dict) else payload
    if not isinstance(raw_records, list):
        return []
    records: List[Dict[str, Any]] = []
    seen: Counter[str] = Counter()
    for index, raw in enumerate(raw_records, start=1):
        if not isinstance(raw, dict):
            continue
        record = dict(raw)
        commit_id = str(record.get("commit_id") or "").strip() or f"unknown-{index}"
        seen[commit_id] += 1
        if seen[commit_id] > 1:
            commit_id = f"{commit_id}#{seen[commit_id]}"
        record["commit_id"] = commit_id
        record["commit_message"] = str(record.get("commit_message") or "")
        record["commit_summary"] = str(record.get("commit_summary") or "")
        record["functional_category"] = str(record.get("functional_category") or "unknown")
        record["changed_files"] = _unique_paths(_extract_record_files(record))
        record["changed_methods"] = [str(item) for item in record.get("changed_methods") or [] if str(item)]
        record["diff_hunks"] = [str(item) for item in record.get("diff_hunks") or [] if str(item)]
        record["call_context"] = str(record.get("call_context") or "")
        record["evidence_granularity"] = str(record.get("evidence_granularity") or "method_level")
        record["change_detection_status"] = str(record.get("change_detection_status") or "method_level_change")
        record["source_refs"] = record.get("source_refs") if isinstance(record.get("source_refs"), dict) else {}
        records.append(record)
    return records


def _estimate_arch_impact_prior_with_features(
    records: Sequence[Dict[str, Any]],
    mapping_index: SemArcMappingIndex,
) -> Tuple[Dict[str, float], Dict[str, Dict[str, Any]]]:
    feature_rows = [_prior_feature_row(record, mapping_index) for record in records]
    feature_names = [
        "num_changed_methods",
        "num_changed_files",
        "num_added_deleted_files",
        "cross_module_count",
        "change_entropy",
    ]
    z_values: Dict[str, List[float]] = {}
    for feature_name in feature_names:
        values = [math.log1p(max(0.0, float(row.get(feature_name, 0.0)))) for row in feature_rows]
        z_values[feature_name] = _robust_z_scores(values)

    priors: Dict[str, float] = {}
    debug: Dict[str, Dict[str, Any]] = {}
    for index, record in enumerate(records):
        raw = (
            0.30 * z_values["num_changed_methods"][index]
            + 0.25 * z_values["num_changed_files"][index]
            + 0.20 * z_values["num_added_deleted_files"][index]
            + 0.15 * z_values["cross_module_count"][index]
            + 0.10 * z_values["change_entropy"][index]
        )
        prior = _clip(_sigmoid(raw), 0.01, 0.99)
        commit_id = str(record.get("commit_id") or "")
        priors[commit_id] = _round(prior)
        debug[commit_id] = {
            "features": feature_rows[index],
            "z_scores": {feature_name: _round(z_values[feature_name][index]) for feature_name in feature_names},
            "raw_logistic": _round(raw),
            "arch_impact_prior": _round(prior),
        }
    return priors, debug


def _prior_feature_row(record: Dict[str, Any], mapping_index: SemArcMappingIndex) -> Dict[str, Any]:
    ops = _record_file_ops(record)
    changed_files = ops["changed_files"]
    modules = {
        module
        for module in (mapping_index.module_for_file(file_path) for file_path in changed_files)
        if module
    }
    components = {
        component
        for component in (mapping_index.component_for_file(file_path) for file_path in changed_files)
        if component
    }
    directories = [_top_directory(file_path) for file_path in changed_files]
    entropy_buckets = list(modules) if modules else directories
    return {
        "num_changed_files": len(changed_files),
        "num_changed_methods": len(record.get("changed_methods") or []),
        "num_diff_hunks": len(record.get("diff_hunks") or []),
        "num_added_files": len(ops["added_files"]),
        "num_deleted_files": len(ops["deleted_files"]),
        "num_modified_files": len(ops["modified_files"]),
        "num_added_deleted_files": len(ops["added_files"]) + len(ops["deleted_files"]),
        "cross_directory_count": len(set(item for item in directories if item)),
        "cross_module_count": len(modules),
        "cross_component_count": len(components),
        "change_entropy": _entropy(entropy_buckets),
    }


def _build_evidence_matrix(
    records: Sequence[Dict[str, Any]],
    events: Sequence[ArchitectureEvent],
    mapping_index: SemArcMappingIndex,
    *,
    config=None,
) -> Dict[str, Dict[str, Dict[str, float]]]:
    matrix: Dict[str, Dict[str, Dict[str, float]]] = {}
    record_contexts = {
        str(record.get("commit_id") or ""): _record_lookup_context(record, mapping_index)
        for record in records
    }
    progress_bar = progress_bar_for(config, "Phase2 evidence matrix progress") if events else None
    for index, event in enumerate(events, start=1):
        event_context = _event_lookup_context(event, mapping_index)
        matrix[event.event_id] = {}
        for record in records:
            commit_id = str(record.get("commit_id") or "")
            matrix[event.event_id][commit_id] = extract_commit_event_evidence(
                record,
                event,
                mapping_index,
                record_context=record_contexts.get(commit_id),
                event_context=event_context,
            )
        if progress_bar is not None:
            progress_bar.update(completed=index, total=len(events))
    if progress_bar is not None:
        progress_bar.finish()
    return matrix


def _compute_feature_reliabilities(
    events: Sequence[ArchitectureEvent],
    records: Sequence[Dict[str, Any]],
    evidence_matrix: Dict[str, Dict[str, Dict[str, float]]],
) -> Dict[str, Dict[str, float]]:
    reliabilities: Dict[str, Dict[str, float]] = {}
    for event in events:
        event_values = evidence_matrix.get(event.event_id, {})
        reliabilities[event.event_id] = {}
        for feature_name in FEATURE_NAMES:
            values = [
                float(event_values.get(str(record.get("commit_id") or ""), {}).get(feature_name, 0.0))
                for record in records
            ]
            iqr = _percentile(values, 0.75) - _percentile(values, 0.25)
            reliability = 0.0 if iqr <= EPS else iqr / (iqr + EPS)
            reliabilities[event.event_id][feature_name] = _round(_clip(reliability, 0.0, 1.0))
    return reliabilities


def _compute_event_posteriors(
    records: Sequence[Dict[str, Any]],
    events: Sequence[ArchitectureEvent],
    priors: Dict[str, float],
    evidence_matrix: Dict[str, Dict[str, Dict[str, float]]],
    reliability_by_event: Dict[str, Dict[str, float]],
) -> Dict[str, Dict[str, float]]:
    posterior_matrix: Dict[str, Dict[str, float]] = {}
    for event in events:
        scores: List[Tuple[str, float]] = []
        reliabilities = reliability_by_event.get(event.event_id, {})
        for record in records:
            commit_id = str(record.get("commit_id") or "")
            evidence = evidence_matrix.get(event.event_id, {}).get(commit_id, {})
            score = (
                math.log(float(priors.get(commit_id, 0.01)) + EPS)
                + reliabilities.get("file_overlap", 0.0) * 1.20 * evidence.get("file_overlap", 0.0)
                + reliabilities.get("module_match", 0.0) * 1.00 * evidence.get("module_match", 0.0)
                + reliabilities.get("component_match", 0.0) * 0.80 * evidence.get("component_match", 0.0)
                + reliabilities.get("operation_match", 0.0) * 1.20 * evidence.get("operation_match", 0.0)
                + reliabilities.get("semantic_support", 0.0) * 0.50 * evidence.get("semantic_support", 0.0)
                - reliabilities.get("negative_evidence", 0.0) * 1.50 * evidence.get("negative_evidence", 0.0)
            )
            scores.append((commit_id, score))
        posterior_matrix[event.event_id] = _softmax(scores)
    return posterior_matrix


def _compute_event_confidences(
    records: Sequence[Dict[str, Any]],
    events: Sequence[ArchitectureEvent],
    posterior_matrix: Dict[str, Dict[str, float]],
) -> Dict[str, float]:
    confidences: Dict[str, float] = {}
    n = len(records)
    for event in events:
        if n <= 0:
            confidences[event.event_id] = 0.0
            continue
        if n == 1:
            confidences[event.event_id] = 1.0
            continue
        posteriors = list(posterior_matrix.get(event.event_id, {}).values())
        entropy = -sum(posterior * math.log(posterior + EPS) for posterior in posteriors)
        confidence = 1.0 - entropy / max(EPS, math.log(n))
        confidences[event.event_id] = _round(_clip(confidence, 0.0, 1.0))
    return confidences


def _compute_event_role_sets(
    records: Sequence[Dict[str, Any]],
    events: Sequence[ArchitectureEvent],
    posterior_matrix: Dict[str, Dict[str, float]],
) -> Dict[str, Dict[str, Any]]:
    event_sets: Dict[str, Dict[str, Any]] = {}
    for event in events:
        ordered = sorted(
            posterior_matrix.get(event.event_id, {}).items(),
            key=lambda item: (-item[1], item[0]),
        )
        core = _cumulative_set(ordered, 0.80)
        support = _cumulative_set(ordered, 0.95)
        event_sets[event.event_id] = {
            "core_set": core,
            "support_set": support,
            "ordered_commits": [{"commit_id": commit_id, "posterior": _round(value, 8)} for commit_id, value in ordered],
        }
    return event_sets


def _assign_structure_roles(
    *,
    records: Sequence[Dict[str, Any]],
    events: Sequence[ArchitectureEvent],
    priors: Dict[str, float],
    prior_debug: Dict[str, Dict[str, Any]],
    evidence_matrix: Dict[str, Dict[str, Dict[str, float]]],
    posterior_matrix: Dict[str, Dict[str, float]],
    event_confidences: Dict[str, float],
    event_sets: Dict[str, Dict[str, Any]],
    mapping_index: SemArcMappingIndex,
) -> Dict[str, Dict[str, Any]]:
    event_by_id = {event.event_id: event for event in events}
    role_debug: Dict[str, Dict[str, Any]] = {}
    for record in records:
        commit_id = str(record.get("commit_id") or "")
        core_events: List[str] = []
        support_events: List[str] = []
        for event in events:
            sets = event_sets.get(event.event_id, {})
            if commit_id in sets.get("core_set", []):
                core_events.append(event.event_id)
            if commit_id in sets.get("support_set", []):
                support_events.append(event.event_id)

        best_core_event = _best_event(core_events, event_by_id, posterior_matrix, event_confidences, commit_id)
        best_support_event = _best_event(support_events, event_by_id, posterior_matrix, event_confidences, commit_id)
        max_negative = _max_evidence_value(commit_id, events, evidence_matrix, "negative_evidence")
        max_file_overlap = _max_evidence_value(commit_id, events, evidence_matrix, "file_overlap")
        max_operation = _max_evidence_value(commit_id, events, evidence_matrix, "operation_match")
        protected_core = bool(best_core_event and event_by_id[best_core_event].event_type in PROTECTED_EVENT_TYPES)

        role = "local_supporting"
        reason = "No strong architecture event attribution; treated as local supporting change."

        if best_core_event:
            event = event_by_id[best_core_event]
            important = _is_important_event(event, event_confidences.get(best_core_event, 0.0))
            if important:
                if event_confidences.get(best_core_event, 0.0) < 0.05:
                    role = "architecture_related_supporting"
                    reason = f"Included in the 80% posterior CoreSet of {event.event_type}, but event confidence is low."
                else:
                    role = "structure_guiding"
                    reason = f"Included in the 80% posterior CoreSet of a high-significance {event.event_type} event."
            else:
                role = "architecture_related_supporting"
                reason = f"Included in the 80% posterior CoreSet of a lower-significance {event.event_type} event."
        elif best_support_event:
            event = event_by_id[best_support_event]
            role = "architecture_related_supporting"
            reason = f"Included in the 95% SupportSet of a {event.event_type} event."
        else:
            features = prior_debug.get(commit_id, {}).get("features", {})
            if (
                float(priors.get(commit_id, 0.0)) >= 0.65
                and (int(features.get("cross_module_count", 0)) > 1 or int(features.get("cross_component_count", 0)) > 1)
            ):
                role = "global_supporting"
                reason = "High architecture impact prior but no confident event attribution."

        if max_negative >= 0.8:
            strong_hit = max(max_file_overlap, max_operation) >= 0.5
            if protected_core and strong_hit:
                if role == "structure_guiding":
                    role = "architecture_related_supporting"
                reason = "Downgraded due to high negative evidence, but retained as architecture-related support."
            elif not strong_hit:
                role = "local_supporting"
                reason = "Downgraded due to high negative evidence."

        if not events:
            features = prior_debug.get(commit_id, {}).get("features", {})
            if (
                float(priors.get(commit_id, 0.0)) >= 0.65
                and (int(features.get("cross_module_count", 0)) > 1 or int(features.get("cross_component_count", 0)) > 1)
            ):
                role = "global_supporting"
                reason = "High architecture impact prior but no architecture events were available."
            else:
                role = "local_supporting"
                reason = "No architecture events were available; treated as local supporting change."

        role_debug[commit_id] = {
            "structure_role": role,
            "role_reason": reason,
            "core_events": core_events,
            "support_events": support_events,
            "max_negative_evidence": _round(max_negative),
            "max_file_overlap": _round(max_file_overlap),
            "max_operation_match": _round(max_operation),
        }
    return role_debug


def _phase2_arch_relevance_enabled(config) -> bool:
    if config is None:
        return False
    return bool(getattr(config, "phase2_llm_arch_relevance_enabled", True))


def _phase2_ablation_mode(config) -> str:
    mode = str(getattr(config, "phase2_ablation_mode", PHASE2_ABLATION_FULL) or PHASE2_ABLATION_FULL).strip().lower()
    supported = {PHASE2_ABLATION_FULL, PHASE2_ABLATION_NO_ARCH_RELEVANCE, PHASE2_ABLATION_SUMMARY_DIFF_ONLY}
    if mode not in supported:
        raise ValueError(f"Unsupported phase2_ablation_mode: {mode}. Supported modes: {sorted(supported)}")
    return mode


def _phase2_event_profile_enabled(config) -> bool:
    if config is None:
        return False
    return bool(getattr(config, "phase2_llm_event_profile_enabled", True))


def _ensure_phase2_api_key(config) -> None:
    env_var = str(getattr(config, "llm_api_key_env_var", "") or "").strip()
    if not env_var:
        raise RuntimeError("Phase 2 LLM is enabled, but config.llm_api_key_env_var is empty.")
    if not os.getenv(env_var):
        raise RuntimeError(f"Phase 2 LLM is enabled, but environment variable {env_var} is not set.")


def _request_phase2_json_with_validation_retry(
    *,
    stage: str,
    item_id: str,
    config,
    llm_client,
    system_prompt: str,
    user_prompt: str,
    request_name: str,
    rate_limiter: Optional[TokenBucketRateLimiter],
    validation_retry_audit: List[Dict[str, Any]],
    llm_call_metrics: List[Dict[str, Any]],
    normalize_fn: Callable[[Dict[str, Any]], Dict[str, Any]],
) -> Tuple[str, Dict[str, Any], Dict[str, Any], List[Dict[str, Any]]]:
    max_retries = llm_output_validation_max_retries(config)
    attempts: List[Dict[str, Any]] = []
    previous_error: Optional[BaseException] = None
    for retry_index in range(max_retries + 1):
        current_request_name = request_name if retry_index == 0 else f"{request_name}:validation_retry{retry_index}"
        retry_user_prompt = _phase2_validation_retry_prompt(user_prompt, previous_error) if retry_index else user_prompt
        try:
            raw, llm_metrics = generate_chat_completion_with_retry(
                config=config,
                llm_client=llm_client,
                system_prompt=system_prompt,
                user_prompt=retry_user_prompt,
                request_name=current_request_name,
                rate_limiter=rate_limiter,
            )
        except Exception as exc:
            failure_metrics = mark_llm_metric_attempt(
                normalize_llm_metrics(getattr(exc, "llm_metrics", {})),
                validation_attempt_count=retry_index + 1,
                is_validation_retry=retry_index > 0,
                success=False,
                error_type=type(exc).__name__,
                error_message=str(exc),
            )
            _append_phase2_llm_metrics(llm_call_metrics, [failure_metrics])
            raise
        llm_metrics = mark_llm_metric_attempt(
            normalize_llm_metrics(llm_metrics),
            validation_attempt_count=retry_index + 1,
            is_validation_retry=retry_index > 0,
        )
        parsed: Optional[Dict[str, Any]] = None
        try:
            parsed = parse_json_response_strict(raw)
            normalized = normalize_fn(parsed)
        except Exception as exc:
            failed_metrics = mark_llm_metric_attempt(
                dict(llm_metrics),
                success=False,
                error_type=type(exc).__name__,
                error_message=str(exc),
            )
            _append_phase2_llm_metrics(llm_call_metrics, [failed_metrics])
            attempts.append(
                {
                    "stage": stage,
                    "item_id": item_id,
                    "request_name": current_request_name,
                    "attempt": retry_index + 1,
                    "result": "retry_scheduled" if retry_index < max_retries else "failed",
                    "error_type": type(exc).__name__,
                    "error_message": str(exc),
                    "raw_llm_response": raw,
                    "parsed_json_if_any": parsed or {},
                    "llm_metrics": failed_metrics,
                }
            )
            if retry_index < max_retries:
                previous_error = exc
                continue
            _append_phase2_validation_retry_audit(validation_retry_audit, attempts)
            setattr(exc, "phase2_last_raw_response", raw)
            setattr(exc, "phase2_validation_retry_attempts", attempts)
            raise
        if attempts:
            attempts.append(
                {
                    "stage": stage,
                    "item_id": item_id,
                    "request_name": current_request_name,
                    "attempt": retry_index + 1,
                    "result": "succeeded",
                    "error_type": "",
                    "error_message": "",
                    "raw_llm_response": raw,
                    "parsed_json_if_any": parsed,
                    "llm_metrics": llm_metrics,
                }
            )
            _append_phase2_validation_retry_audit(validation_retry_audit, attempts)
        _append_phase2_llm_metrics(llm_call_metrics, [llm_metrics])
        return raw, parsed, normalized, attempts
    raise AssertionError("unreachable")


def _phase2_validation_retry_prompt(user_prompt: str, error: Optional[BaseException]) -> str:
    if error is None:
        return user_prompt
    return (
        user_prompt
        + "\n\nThe previous response failed output validation: "
        + str(error)[:600]
        + "\nGenerate the answer again using the same input. Return only valid JSON that satisfies every required field and value constraint."
    )


def _append_phase2_validation_retry_audit(target: List[Dict[str, Any]], attempts: Sequence[Dict[str, Any]]) -> None:
    with _PHASE2_VALIDATION_RETRY_AUDIT_LOCK:
        target.extend(dict(attempt) for attempt in attempts)


def _append_phase2_llm_metrics(target: List[Dict[str, Any]], metrics: Sequence[Dict[str, Any]]) -> None:
    with _PHASE2_LLM_METRICS_LOCK:
        target.extend(dict(metric) for metric in metrics if isinstance(metric, dict))


def _build_arch_event_profiles(
    *,
    events: Sequence[ArchitectureEvent],
    mapping_index: SemArcMappingIndex,
    config,
    llm_client,
    rate_limiter: Optional[TokenBucketRateLimiter],
    output_dir: Path,
    validation_retry_audit: List[Dict[str, Any]],
    llm_call_metrics: List[Dict[str, Any]],
) -> Dict[str, Dict[str, Any]]:
    if not events:
        return {}
    if not (_phase2_event_profile_enabled(config) and llm_client is not None):
        return {event.event_id: _deterministic_event_profile(event, mapping_index) for event in events}

    prompt_path = resolve_prompt_path(config, "phase2_event_profile_prompt_path", DEFAULT_EVENT_PROFILE_PROMPT)
    template = load_prompt_text(prompt_path)
    system_prompt = "You are a software architecture event explanation assistant. Output only valid JSON."
    max_workers = max(1, int(getattr(config, "phase2_llm_concurrency", getattr(config, "step10_concurrency", 1)) or 1))
    profiles: Dict[str, Dict[str, Any]] = {}
    progress_bar = progress_bar_for(config, "Phase2 event profile progress")

    def profile_one(event: ArchitectureEvent) -> Tuple[str, Dict[str, Any]]:
        event_payload = _event_profile_input(event, mapping_index)
        user_prompt = render_prompt_template(template, {"architecture_event_json": to_compact_json(event_payload)})
        raw = ""
        parsed: Optional[Dict[str, Any]] = None
        validation_retry_attempts: List[Dict[str, Any]] = []
        try:
            raw, parsed, profile, validation_retry_attempts = _request_phase2_json_with_validation_retry(
                stage="phase2.event_profile",
                item_id=event.event_id,
                config=config,
                llm_client=llm_client,
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                request_name=f"phase2:event_profile:{event.event_id}",
                rate_limiter=rate_limiter,
                validation_retry_audit=validation_retry_audit,
                llm_call_metrics=llm_call_metrics,
                normalize_fn=lambda response, expected_event=event: _normalize_event_profile(expected_event, response),
            )
            return event.event_id, profile
        except Exception as exc:
            _raise_phase2_llm_failure(
                output_dir=output_dir,
                stage="phase2.event_profile",
                item_id=event.event_id,
                prompt_path=prompt_path,
                rendered_prompt=user_prompt,
                raw_response=str(getattr(exc, "phase2_last_raw_response", raw) or ""),
                parsed_json=parsed,
                error=exc,
                input_payload=event_payload,
                validation_retry_attempts=getattr(exc, "phase2_validation_retry_attempts", validation_retry_attempts),
            )
        raise AssertionError("unreachable")
    if progress_bar is not None:
        progress_bar.update(completed=0, total=len(events))
    try:
        with suppress_noisy_llm_loggers(enabled=progress_bar is not None):
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = [executor.submit(profile_one, event) for event in events]
                completed = 0
                for future in as_completed(futures):
                    event_id, profile = future.result()
                    profiles[event_id] = profile
                    completed += 1
                    if progress_bar is not None:
                        progress_bar.update(completed=completed, total=len(events))
    finally:
        if progress_bar is not None:
            progress_bar.finish()
    return profiles


def _event_profile_input(event: ArchitectureEvent, mapping_index: SemArcMappingIndex) -> Dict[str, Any]:
    key_files = _unique_paths(event.related_files or event.added_files + event.removed_files + event.modified_files)
    return {
        "event_id": event.event_id,
        "event_type": event.event_type,
        "module": event.module or "",
        "component": event.component or "",
        "summary": event.summary or "",
        "related_files": key_files,
        "added_files": event.added_files,
        "removed_files": event.removed_files,
        "modified_files": event.modified_files,
        "significance": _round(event.significance),
        "source_confidence": _round(event.source_confidence),
        "module_files_sample": sorted(mapping_index.module_to_files.get(event.module, set()))[:20] if event.module else [],
        "component_modules": sorted(mapping_index.component_to_modules.get(event.component, set()))[:20]
        if event.component
        else [],
    }


def _normalize_event_profile(event: ArchitectureEvent, parsed: Dict[str, Any]) -> Dict[str, Any]:
    profile = parsed.get("arch_event_profile") if isinstance(parsed.get("arch_event_profile"), dict) else parsed
    result = _deterministic_event_profile(event, SemArcMappingIndex())
    for key in (
        "what_changed",
        "affected_architecture_area",
        "important_files",
        "why_it_may_matter",
        "not_enough_evidence_cases",
    ):
        value = profile.get(key) if isinstance(profile, dict) else None
        if key == "important_files":
            result[key] = _unique_paths(_coerce_file_values(value)) if value is not None else result[key]
        elif key in {"why_it_may_matter", "not_enough_evidence_cases"}:
            result[key] = _string_list(value) or result[key]
        elif value is not None:
            result[key] = str(value).strip() or result[key]
    return result


def _deterministic_event_profile(event: ArchitectureEvent, mapping_index: SemArcMappingIndex) -> Dict[str, Any]:
    key_files = _unique_paths(event.related_files or event.added_files + event.removed_files + event.modified_files)
    module = event.module or "unknown module"
    component = event.component or "unknown component"
    return {
        "event_id": event.event_id,
        "event_type": event.event_type,
        "module": event.module or "",
        "component": event.component or "",
        "what_changed": event.summary or f"{event.event_type} in {module}",
        "affected_architecture_area": f"Module {module}, component {component}.",
        "important_files": key_files[:12],
        "why_it_may_matter": _unique(
            [
                "This event may indicate a module or component responsibility change.",
                "Files in public headers, core implementation, build, package, or release paths may affect architecture-facing contracts.",
            ]
            + ([f"Module {event.module} has {len(mapping_index.module_to_files.get(event.module, set()))} mapped files."] if event.module else [])
        ),
        "not_enough_evidence_cases": [
            "Formatting, spelling, trivial comments, and metadata-only changes are not strong architecture evidence.",
            "Touching a core module name alone is not enough; the actual change intent still matters.",
        ],
    }


def _build_architecture_evidence_cards(
    *,
    records: Sequence[Dict[str, Any]],
    events: Sequence[ArchitectureEvent],
    priors: Dict[str, float],
    prior_debug: Dict[str, Dict[str, Any]],
    evidence_matrix: Dict[str, Dict[str, Dict[str, float]]],
    posterior_matrix: Dict[str, Dict[str, float]],
    event_confidences: Dict[str, float],
    event_sets: Dict[str, Dict[str, Any]],
    role_debug: Dict[str, Dict[str, Any]],
    mapping_index: SemArcMappingIndex,
    event_profiles: Dict[str, Dict[str, Any]],
) -> List[Dict[str, Any]]:
    cards: List[Dict[str, Any]] = []
    for record in records:
        commit_id = str(record.get("commit_id") or "")
        evidence_scores, evidence_facts = _architecture_evidence_scores_and_facts(
            record=record,
            events=events,
            evidence_matrix=evidence_matrix,
            mapping_index=mapping_index,
        )
        matched_events = _matched_arch_event_cards(
            record=record,
            events=events,
            evidence_matrix=evidence_matrix,
            posterior_matrix=posterior_matrix,
            event_confidences=event_confidences,
            event_sets=event_sets,
            event_profiles=event_profiles,
        )
        cards.append(
            {
                "commit_id": commit_id,
                "commit_summary": str(record.get("commit_summary") or ""),
                "changed_files": list(record.get("changed_files") or []),
                "changed_methods": list(record.get("changed_methods") or []),
                "functional_category": str(record.get("functional_category") or "unknown"),
                "evidence_granularity": str(record.get("evidence_granularity") or "method_level"),
                "change_detection_status": str(record.get("change_detection_status") or "method_level_change"),
                "module_component_context": _module_component_context(record, mapping_index),
                "evidence_scores": evidence_scores,
                "evidence_facts": evidence_facts,
                "matched_arch_events": matched_events,
                "bayesian_evidence": {
                    "arch_impact_prior": _round(priors.get(commit_id, 0.01)),
                    "legacy_structure_role": role_debug.get(commit_id, {}).get("structure_role", "local_supporting"),
                    "legacy_role_reason": role_debug.get(commit_id, {}).get("role_reason", ""),
                    "prior_features": prior_debug.get(commit_id, {}).get("features", {}),
                    "prior_z_scores": prior_debug.get(commit_id, {}).get("z_scores", {}),
                },
            }
        )
    return cards


def _neutral_arch_evidence_card(record: Dict[str, Any]) -> Dict[str, Any]:
    commit_id = str(record.get("commit_id") or "")
    return {
        "commit_id": commit_id,
        "commit_summary": str(record.get("commit_summary") or ""),
        "changed_files": list(record.get("changed_files") or []),
        "changed_methods": list(record.get("changed_methods") or []),
        "functional_category": str(record.get("functional_category") or "unknown"),
        "evidence_granularity": str(record.get("evidence_granularity") or "method_level"),
        "change_detection_status": str(record.get("change_detection_status") or "method_level_change"),
        "module_component_context": {},
        "evidence_scores": {name: 0.0 for name in EVIDENCE_SCORE_NAMES},
        "evidence_facts": {},
        "matched_arch_events": [],
        "bayesian_evidence": {
            "arch_impact_prior": 0.0,
            "legacy_structure_role": "local_supporting",
            "legacy_role_reason": "Ablation disables Phase 2 architecture relevance judgment.",
            "bayesian_evidence_score": 0.0,
            "active_score_features": [],
            "negative_evidence_active": False,
            "ablation_mode": PHASE2_ABLATION_NO_ARCH_RELEVANCE,
        },
    }


def _summary_diff_only_evidence_card(record: Dict[str, Any]) -> Dict[str, Any]:
    changed_files = [str(item) for item in record.get("changed_files") or [] if str(item)]
    contract_score, contract_facts = _contract_surface_signal(record, changed_files)
    intent_score, intent_facts = _change_intent_signal(
        " ".join(
            [
                str(record.get("commit_summary") or ""),
                str(record.get("functional_category") or ""),
                " ".join(changed_files[:20]),
            ]
        )
    )
    negative_score = _negative_evidence(record, changed_files)
    negative_facts = _negative_evidence_facts(record, changed_files)
    return {
        "commit_id": str(record.get("commit_id") or ""),
        "commit_summary": str(record.get("commit_summary") or ""),
        "changed_files": changed_files,
        "changed_methods": list(record.get("changed_methods") or []),
        "functional_category": str(record.get("functional_category") or "unknown"),
        "evidence_granularity": str(record.get("evidence_granularity") or "method_level"),
        "change_detection_status": str(record.get("change_detection_status") or "method_level_change"),
        "diff_evidence": _diff_evidence_snippets(record),
        "evidence_scores": {
            "contract_surface_score": _round(contract_score),
            "core_area_score": 0.0,
            "cross_area_score": 0.0,
            "event_alignment_score": 0.0,
            "change_intent_score": _round(intent_score),
            "negative_evidence_score": _round(negative_score),
        },
        "evidence_facts": {
            "contract_surface_facts": contract_facts,
            "change_intent_facts": intent_facts,
            "negative_evidence_facts": negative_facts,
        },
        "matched_arch_events": [],
        "bayesian_evidence": {
            "arch_impact_prior": 0.0,
            "legacy_structure_role": "local_supporting",
            "legacy_role_reason": "Ablation withholds SemArc, architecture events, and component evidence.",
            "ablation_mode": PHASE2_ABLATION_SUMMARY_DIFF_ONLY,
        },
        "ablation_note": "Only commit summary, changed files/methods, and diff evidence are provided to the LLM.",
    }


def _diff_evidence_snippets(record: Dict[str, Any], *, limit: int = 8, max_chars: int = 600) -> List[str]:
    snippets: List[str] = []
    for raw in record.get("diff_hunks") or []:
        text = ""
        if isinstance(raw, dict):
            text = str(
                raw.get("snippet")
                or raw.get("diff")
                or raw.get("patch")
                or raw.get("content")
                or raw.get("text")
                or ""
            )
            path = str(raw.get("file") or raw.get("path") or raw.get("file_path") or "")
            if path:
                text = f"{path}\n{text}".strip()
        else:
            text = str(raw or "")
        text = text.strip()
        if not text:
            continue
        snippets.append(text[:max_chars])
        if len(snippets) >= limit:
            break
    return snippets


def _architecture_evidence_scores_and_facts(
    *,
    record: Dict[str, Any],
    events: Sequence[ArchitectureEvent],
    evidence_matrix: Dict[str, Dict[str, Dict[str, float]]],
    mapping_index: SemArcMappingIndex,
) -> Tuple[Dict[str, float], Dict[str, List[str]]]:
    changed_files = [str(item) for item in record.get("changed_files") or [] if str(item)]
    text = _record_text(record)
    contract_score, contract_facts = _contract_surface_signal(record, changed_files)
    core_score, core_facts = _core_area_signal(changed_files, mapping_index)
    cross_score, cross_facts = _cross_area_signal(changed_files, mapping_index)
    event_score, event_facts = _event_alignment_signal(record, events, evidence_matrix)
    intent_score, intent_facts = _change_intent_signal(text)
    negative_score = _negative_evidence(record, changed_files)
    negative_facts = _negative_evidence_facts(record, changed_files)
    return (
        {
            "contract_surface_score": _round(contract_score),
            "core_area_score": _round(core_score),
            "cross_area_score": _round(cross_score),
            "event_alignment_score": _round(event_score),
            "change_intent_score": _round(intent_score),
            "negative_evidence_score": _round(negative_score),
        },
        {
            "contract_surface_facts": contract_facts,
            "core_area_facts": core_facts,
            "cross_area_facts": cross_facts,
            "event_alignment_facts": event_facts,
            "change_intent_facts": intent_facts,
            "negative_evidence_facts": negative_facts,
        },
    )


def _contract_surface_signal(record: Dict[str, Any], changed_files: Sequence[str]) -> Tuple[float, List[str]]:
    score = 0.0
    facts: List[str] = []
    methods = [str(item) for item in record.get("changed_methods") or [] if str(item)]
    for file_path in changed_files:
        lower = normalize_path(file_path).lower()
        basename = lower.rsplit("/", 1)[-1]
        if lower.startswith("include/") or basename.endswith((".h", ".hpp", ".hh", ".hxx")):
            score = max(score, 0.75)
            facts.append(f"changed public/header-like file {file_path}")
        if basename in {"version.h", "config.h", "features.h", "json_features.h"}:
            score = max(score, 0.85)
            facts.append(f"changed API/config/version surface file {file_path}")
        if "pkg-config/" in lower or basename.endswith(".pc.in"):
            score = max(score, 0.65)
            facts.append(f"changed package configuration contract {file_path}")
        if _is_build_or_release_path(lower):
            score = max(score, 0.55)
            facts.append(f"changed build/package/release contract file {file_path}")
    if methods and any(_looks_public_method(method) for method in methods):
        score = max(score, 0.80)
        facts.append("changed public-looking method or API entity")
    return _clip(score, 0.0, 1.0), _unique(facts)[:8]


def _core_area_signal(changed_files: Sequence[str], mapping_index: SemArcMappingIndex) -> Tuple[float, List[str]]:
    score = 0.0
    facts: List[str] = []
    for file_path in changed_files:
        module = mapping_index.module_for_file(file_path) or ""
        component = mapping_index.component_for_file(file_path) or ""
        module_key = module.lower()
        component_key = component.lower()
        if module and _is_core_name(module_key):
            score = max(score, 0.70)
            facts.append(f"{file_path} belongs to core-like module {module}")
        if component and _is_core_name(component_key):
            score = max(score, 0.75)
            facts.append(f"{file_path} belongs to architecture-sensitive component {component}")
        if module and _module_has_public_surface(module, mapping_index):
            score = max(score, 0.65)
            facts.append(f"module {module} contains public/header files")
    return _clip(score, 0.0, 1.0), _unique(facts)[:8]


def _cross_area_signal(changed_files: Sequence[str], mapping_index: SemArcMappingIndex) -> Tuple[float, List[str]]:
    modules = _unique([mapping_index.module_for_file(path) or "" for path in changed_files])
    components = _unique([mapping_index.component_for_file(path) or "" for path in changed_files])
    categories = _unique([_file_area_category(path) for path in changed_files])
    facts: List[str] = []
    score = 0.0
    if len(modules) >= 2:
        score = max(score, min(1.0, 0.35 + 0.15 * len(modules)))
        facts.append(f"changed files span modules: {', '.join(modules[:5])}")
    if len(components) >= 2:
        score = max(score, min(1.0, 0.40 + 0.15 * len(components)))
        facts.append(f"changed files span components: {', '.join(components[:5])}")
    if len(categories) >= 2:
        score = max(score, min(1.0, 0.25 + 0.12 * len(categories)))
        facts.append(f"changed files span areas: {', '.join(categories[:6])}")
    return _clip(score, 0.0, 1.0), facts[:8]


def _event_alignment_signal(
    record: Dict[str, Any],
    events: Sequence[ArchitectureEvent],
    evidence_matrix: Dict[str, Dict[str, Dict[str, float]]],
) -> Tuple[float, List[str]]:
    commit_id = str(record.get("commit_id") or "")
    best = 0.0
    facts: List[str] = []
    for event in events:
        evidence = evidence_matrix.get(event.event_id, {}).get(commit_id, {})
        score = (
            0.40 * float(evidence.get("file_overlap", 0.0))
            + 0.25 * float(evidence.get("module_match", 0.0))
            + 0.20 * float(evidence.get("component_match", 0.0))
            + 0.15 * float(evidence.get("operation_match", 0.0))
        )
        if score > best:
            best = score
        if score > 0:
            facts.append(
                f"matches event {event.event_id} by file={_round(evidence.get('file_overlap', 0.0))}, "
                f"module={_round(evidence.get('module_match', 0.0))}, component={_round(evidence.get('component_match', 0.0))}"
            )
    return _clip(best, 0.0, 1.0), facts[:8]


def _change_intent_signal(text: str) -> Tuple[float, List[str]]:
    lower = text.lower()
    strong_keywords = {
        "api": 0.8,
        "public api": 0.9,
        "compatibility": 0.8,
        "compatible": 0.75,
        "breaking": 0.9,
        "deprecate": 0.8,
        "configuration": 0.65,
        "config": 0.55,
        "platform": 0.65,
        "install": 0.55,
        "package": 0.55,
        "pkg-config": 0.7,
        "cmake": 0.55,
        "meson": 0.55,
        "release": 0.55,
        "version": 0.45,
        "parser": 0.45,
        "writer": 0.45,
        "reader": 0.45,
    }
    facts: List[str] = []
    score = 0.0
    for keyword, value in strong_keywords.items():
        if keyword in lower:
            score = max(score, value)
            facts.append(f"summary contains architecture-relevant intent keyword '{keyword}'")
    if _text_is_low_value(lower):
        score = min(score, 0.25)
    return _clip(score, 0.0, 1.0), facts[:8]


def _negative_evidence_facts(record: Dict[str, Any], changed_files: Sequence[str]) -> List[str]:
    facts: List[str] = []
    text = _record_text(record).lower()
    if _text_is_low_value(text):
        facts.append("summary suggests formatting, typo, comment, metadata, or docs-only work")
    low_paths = [path for path in changed_files if _is_low_value_path(path)]
    if low_paths:
        facts.append(f"low-value path types detected: {', '.join(low_paths[:5])}")
    return facts[:8]


def _matched_arch_event_cards(
    *,
    record: Dict[str, Any],
    events: Sequence[ArchitectureEvent],
    evidence_matrix: Dict[str, Dict[str, Dict[str, float]]],
    posterior_matrix: Dict[str, Dict[str, float]],
    event_confidences: Dict[str, float],
    event_sets: Dict[str, Dict[str, Any]],
    event_profiles: Dict[str, Dict[str, Any]],
) -> List[Dict[str, Any]]:
    commit_id = str(record.get("commit_id") or "")
    cards: List[Dict[str, Any]] = []
    for event in events:
        evidence = evidence_matrix.get(event.event_id, {}).get(commit_id, {})
        posterior = float(posterior_matrix.get(event.event_id, {}).get(commit_id, 0.0))
        role = _role_in_event(commit_id, event.event_id, event_sets)
        if role == "weak" and posterior <= 0.0 and max([float(value) for value in evidence.values()] or [0.0]) <= 0.0:
            continue
        cards.append(
            {
                "event_id": event.event_id,
                "event_type": event.event_type,
                "module": event.module or "",
                "component": event.component or "",
                "key_files": _unique_paths(event.related_files)[:12],
                "arch_event_profile": event_profiles.get(event.event_id)
                or _deterministic_event_profile(event, SemArcMappingIndex()),
                "matching_facts": _event_matching_facts(event, evidence, role),
                "posterior_hint": _round(posterior, 8),
                "event_confidence": _round(event_confidences.get(event.event_id, 0.0)),
                "event_significance": _round(event.significance),
                "role_in_event": role,
            }
        )
    cards.sort(key=lambda item: (-float(item.get("posterior_hint") or 0.0), item.get("event_id") or ""))
    return cards[:5]


def _event_matching_facts(event: ArchitectureEvent, evidence: Dict[str, float], role: str) -> List[str]:
    facts = [f"role in event posterior set: {role}"]
    for key in ("file_overlap", "module_match", "component_match", "operation_match", "negative_evidence"):
        value = float(evidence.get(key, 0.0))
        if value > 0:
            facts.append(f"{key}={_round(value)} for event {event.event_id}")
    return facts


def _module_component_context(record: Dict[str, Any], mapping_index: SemArcMappingIndex) -> Dict[str, Any]:
    rows = []
    modules: List[str] = []
    components: List[str] = []
    for file_path in record.get("changed_files") or []:
        module = mapping_index.module_for_file(str(file_path)) or ""
        component = mapping_index.component_for_file(str(file_path)) or ""
        if module:
            modules.append(module)
        if component:
            components.append(component)
        rows.append({"file": str(file_path), "module": module, "component": component})
    return {
        "primary_module": _most_common(modules) or "",
        "primary_component": _most_common(components) or "",
        "touched_modules": _unique(modules),
        "touched_components": _unique(components),
        "file_mappings": rows[:20],
    }


def _feature_distribution_debug(cards: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for name in EVIDENCE_SCORE_NAMES:
        values = [float((card.get("evidence_scores") or {}).get(name, 0.0)) for card in cards]
        if not values:
            result[name] = {"active": False, "reason": "no_values", "min": 0.0, "max": 0.0, "distinct_count": 0}
            continue
        minimum = min(values)
        maximum = max(values)
        distinct = {round(value, 4) for value in values}
        iqr = _percentile(values, 0.75) - _percentile(values, 0.25)
        active = not (
            maximum - minimum <= 0.001
            or len(distinct) <= 1
            or (all(value <= 0.001 for value in values))
            or (all(value >= 0.999 for value in values))
        )
        result[name] = {
            "active_for_bayesian_evidence_score": active,
            "min": _round(minimum),
            "max": _round(maximum),
            "iqr": _round(iqr),
            "distinct_count": len(distinct),
            "reason": "usable" if active else "low_discrimination",
        }
    return result


def _attach_bayesian_evidence_scores(cards: Sequence[Dict[str, Any]], distribution: Dict[str, Any]) -> None:
    active_weights = {
        name: weight
        for name, weight in POSITIVE_EVIDENCE_WEIGHTS.items()
        if distribution.get(name, {}).get("active_for_bayesian_evidence_score")
    }
    active_negative = bool(distribution.get("negative_evidence_score", {}).get("active_for_bayesian_evidence_score"))
    total_weight = sum(active_weights.values())
    for card in cards:
        scores = card.setdefault("evidence_scores", {})
        if total_weight <= EPS:
            positive = 0.0
        else:
            positive = sum(active_weights[name] * float(scores.get(name, 0.0)) for name in active_weights) / total_weight
        if active_negative:
            positive -= 0.30 * float(scores.get("negative_evidence_score", 0.0))
        bayesian_score = _round(_clip(positive, 0.0, 1.0))
        scores["bayesian_evidence_score"] = bayesian_score
        card.setdefault("bayesian_evidence", {})["bayesian_evidence_score"] = bayesian_score
        card["bayesian_evidence"]["active_score_features"] = sorted(active_weights.keys())
        card["bayesian_evidence"]["negative_evidence_active"] = active_negative


def _classify_architecture_relevance(
    *,
    evidence_cards: Sequence[Dict[str, Any]],
    enabled: bool,
    config,
    llm_client,
    rate_limiter: Optional[TokenBucketRateLimiter],
    output_dir: Path,
    validation_retry_audit: List[Dict[str, Any]],
    llm_call_metrics: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    if not enabled:
        return [_fallback_arch_relevance_decision(card) for card in evidence_cards]

    if _phase2_ablation_mode(config) == PHASE2_ABLATION_SUMMARY_DIFF_ONLY:
        prompt_path = resolve_prompt_path(
            config,
            "phase2_summary_diff_only_prompt_path",
            DEFAULT_SUMMARY_DIFF_ONLY_PROMPT,
        )
    else:
        prompt_path = resolve_prompt_path(config, "phase2_llm_prompt_path", DEFAULT_ARCH_RELEVANCE_PROMPT)
    template = load_prompt_text(prompt_path)
    system_prompt = "You are a software architecture relevance classification assistant. Output only valid JSON and do not write Markdown."
    max_workers = max(1, int(getattr(config, "phase2_llm_concurrency", getattr(config, "step10_concurrency", 1)) or 1))
    decisions: List[Optional[Dict[str, Any]]] = [None] * len(evidence_cards)
    progress_bar = progress_bar_for(config, "Phase2 architecture relevance progress") if evidence_cards else None

    def classify_one(index: int, card: Dict[str, Any]) -> Tuple[int, Dict[str, Any]]:
        user_prompt = render_prompt_template(template, {"architecture_evidence_card_json": to_compact_json(card)})
        raw = ""
        parsed: Optional[Dict[str, Any]] = None
        validation_retry_attempts: List[Dict[str, Any]] = []
        try:
            raw, parsed, decision, validation_retry_attempts = _request_phase2_json_with_validation_retry(
                stage="phase2.arch_relevance",
                item_id=str(card.get("commit_id") or ""),
                config=config,
                llm_client=llm_client,
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                request_name=f"phase2:arch_relevance:{card.get('commit_id')}",
                rate_limiter=rate_limiter,
                validation_retry_audit=validation_retry_audit,
                llm_call_metrics=llm_call_metrics,
                normalize_fn=lambda response: _normalize_arch_relevance_decision(card, response),
            )
            return index, decision
        except Exception as exc:
            _raise_phase2_llm_failure(
                output_dir=output_dir,
                stage="phase2.arch_relevance",
                item_id=str(card.get("commit_id") or ""),
                prompt_path=prompt_path,
                rendered_prompt=user_prompt,
                raw_response=str(getattr(exc, "phase2_last_raw_response", raw) or ""),
                parsed_json=parsed,
                error=exc,
                input_payload=card,
                validation_retry_attempts=getattr(exc, "phase2_validation_retry_attempts", validation_retry_attempts),
            )
        raise AssertionError("unreachable")

    if progress_bar is not None:
        progress_bar.update(completed=0, total=len(evidence_cards))
    try:
        with suppress_noisy_llm_loggers(enabled=progress_bar is not None):
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = [executor.submit(classify_one, index, card) for index, card in enumerate(evidence_cards)]
                completed = 0
                for future in as_completed(futures):
                    index, decision = future.result()
                    decisions[index] = decision
                    completed += 1
                    if progress_bar is not None:
                        progress_bar.update(completed=completed, total=len(evidence_cards))
    finally:
        if progress_bar is not None:
            progress_bar.finish()

    return [decision for decision in decisions if decision is not None]


def _fallback_arch_relevance_decision(card: Dict[str, Any]) -> Dict[str, Any]:
    scores = card.get("evidence_scores") or {}
    bayesian_score = float(scores.get("bayesian_evidence_score", 0.0))
    legacy_role = str((card.get("bayesian_evidence") or {}).get("legacy_structure_role") or "local_supporting")
    negative = float(scores.get("negative_evidence_score", 0.0))
    if legacy_role == "structure_guiding" or (bayesian_score >= 0.70 and negative < 0.6):
        level = "high"
        role = "structure_guiding"
    elif legacy_role == "architecture_related_supporting" or bayesian_score >= 0.35:
        level = "medium"
        role = "architecture_related_supporting"
    elif bayesian_score >= 0.12:
        level = "low"
        role = "architecture_related_supporting"
    else:
        level = "none"
        role = "local_supporting"
    return {
        "commit_id": str(card.get("commit_id") or ""),
        "architecture_relevance_level": level,
        "architecture_relevance_score": _round(bayesian_score),
        "structure_role": role,
        "architecture_relevance_labels": _fallback_arch_labels(card),
        "architecture_relevance_reason": str((card.get("bayesian_evidence") or {}).get("legacy_role_reason") or "Fallback from Phase 2 architecture evidence."),
    }


def _neutral_arch_relevance_decision(card: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "commit_id": str(card.get("commit_id") or ""),
        "architecture_relevance_level": "none",
        "architecture_relevance_score": 0.0,
        "structure_role": "local_supporting",
        "architecture_relevance_labels": [],
        "architecture_relevance_reason": "Ablation disables Phase 2 architecture relevance judgment for this commit.",
    }


def _fallback_arch_labels(card: Dict[str, Any]) -> List[str]:
    scores = card.get("evidence_scores") or {}
    labels: List[str] = []
    if float(scores.get("contract_surface_score", 0.0)) >= 0.5:
        labels.append("public_contract")
    if float(scores.get("core_area_score", 0.0)) >= 0.5:
        labels.append("core_area")
    if float(scores.get("cross_area_score", 0.0)) >= 0.5:
        labels.append("cross_area")
    if float(scores.get("event_alignment_score", 0.0)) >= 0.5:
        labels.append("architecture_event")
    return labels


def _normalize_arch_relevance_decision(card: Dict[str, Any], parsed: Dict[str, Any]) -> Dict[str, Any]:
    decision = parsed.get("decision") if isinstance(parsed.get("decision"), dict) else parsed
    commit_id = str(decision.get("commit_id") or "")
    expected = str(card.get("commit_id") or "")
    if commit_id != expected:
        raise ValueError(f"Phase 2 LLM decision commit_id mismatch: expected {expected}, got {commit_id}")
    level = str(decision.get("architecture_relevance_level") or "").strip().lower()
    if level not in ARCH_RELEVANCE_LEVELS:
        raise ValueError(f"Invalid architecture_relevance_level for {commit_id}: {level}")
    score = float(decision.get("architecture_relevance_score"))
    if score < 0.0 or score > 1.0:
        raise ValueError(f"architecture_relevance_score out of range for {commit_id}: {score}")
    role = str(decision.get("structure_role") or "").strip()
    if role not in STRUCTURE_ROLES:
        raise ValueError(f"Invalid structure_role for {commit_id}: {role}")
    reason = " ".join(str(decision.get("architecture_relevance_reason") or "").split()).strip()
    if not reason:
        raise ValueError(f"architecture_relevance_reason is required for {commit_id}")
    labels = _string_list(decision.get("architecture_relevance_labels"))
    return {
        "commit_id": commit_id,
        "architecture_relevance_level": level,
        "architecture_relevance_score": _round(score),
        "structure_role": role,
        "architecture_relevance_labels": labels,
        "architecture_relevance_reason": reason,
    }


def _raise_phase2_llm_failure(
    *,
    output_dir: Path,
    stage: str,
    item_id: str,
    prompt_path: Path,
    rendered_prompt: str,
    raw_response: str,
    parsed_json: Optional[Dict[str, Any]],
    error: BaseException,
    input_payload: Dict[str, Any],
    validation_retry_attempts: Optional[Sequence[Dict[str, Any]]] = None,
) -> None:
    failure_dir = output_dir / "phase2_llm_failures"
    failure_dir.mkdir(parents=True, exist_ok=True)
    safe_stage = re.sub(r"[^A-Za-z0-9_.-]+", "_", stage)
    safe_item = re.sub(r"[^A-Za-z0-9_.-]+", "_", item_id or "unknown")[:80]
    stamp = re.sub(r"[^0-9A-Za-z]+", "", utc_now_iso())[:20]
    path = failure_dir / f"{stamp}_{safe_stage}_{safe_item}_failure.json"
    _write_json(
        path,
        {
            "stage": stage,
            "item_id": item_id,
            "prompt_template_path": str(prompt_path),
            "rendered_prompt": rendered_prompt,
            "raw_llm_response": raw_response,
            "parsed_json_if_any": parsed_json or {},
            "error_type": type(error).__name__,
            "error_message": str(error),
            "input_payload": input_payload,
            "validation_attempts": list(validation_retry_attempts or []),
        },
    )
    raise RuntimeError(f"Phase 2 LLM output validation failed at {stage}; failure file: {path}") from error


def _build_output_record(
    *,
    record: Dict[str, Any],
    events: Sequence[ArchitectureEvent],
    priors: Dict[str, float],
    posterior_matrix: Dict[str, Dict[str, float]],
    event_confidences: Dict[str, float],
    event_sets: Dict[str, Dict[str, Any]],
    evidence_matrix: Dict[str, Dict[str, Dict[str, float]]],
    reliability_by_event: Dict[str, Dict[str, float]],
    role_debug: Dict[str, Dict[str, Any]],
    mapping_index: SemArcMappingIndex,
    evidence_card: Dict[str, Any],
    llm_decision: Dict[str, Any],
) -> Dict[str, Any]:
    commit_id = str(record.get("commit_id") or "")
    attributions = []
    for event in events:
        posterior = float(posterior_matrix.get(event.event_id, {}).get(commit_id, 0.0))
        role_in_event = _role_in_event(commit_id, event.event_id, event_sets)
        attributions.append(
            {
                "event_id": event.event_id,
                "event_type": event.event_type,
                "posterior": _round(posterior, 8),
                "event_confidence": _round(event_confidences.get(event.event_id, 0.0)),
                "event_significance": _round(event.significance),
                "role_in_event": role_in_event,
                "module": event.module or "unknown",
                "component": event.component or "unknown",
                "evidence": {
                    key: _round(value)
                    for key, value in (evidence_matrix.get(event.event_id, {}).get(commit_id, {}) or {}).items()
                },
                "feature_reliability": {
                    key: _round(value)
                    for key, value in (reliability_by_event.get(event.event_id, {}) or {}).items()
                },
            }
        )
    attributions.sort(key=lambda item: (-item["posterior"], item["event_id"]))

    arch_signal = _architecture_signal_score(commit_id, events, posterior_matrix, event_confidences, priors)
    primary_module, primary_component = _primary_module_component(record, attributions, mapping_index)
    matched_attributions = [
        item
        for item in attributions
        if item["role_in_event"] in {"core", "support"} or item["posterior"] > 0.0
    ]
    matched_modules = _unique(
        item["module"] for item in matched_attributions if item.get("module") and item.get("module") != "unknown"
    )
    matched_components = _unique(
        item["component"]
        for item in matched_attributions
        if item.get("component") and item.get("component") != "unknown"
    )
    matched_events = _unique(item["event_id"] for item in matched_attributions if item.get("event_id"))
    top_event_id = attributions[0]["event_id"] if attributions else ""
    confidence = _commit_confidence(commit_id, attributions, priors)

    decision = llm_decision or _fallback_arch_relevance_decision(evidence_card)
    matched_event_cards = list((evidence_card.get("matched_arch_events") if isinstance(evidence_card, dict) else []) or [])
    matched_event_ids = _unique(
        [str(item.get("event_id") or "") for item in matched_event_cards if isinstance(item, dict)]
        + matched_events
    )
    evidence_scores = dict((evidence_card.get("evidence_scores") if isinstance(evidence_card, dict) else {}) or {})
    evidence_facts = dict((evidence_card.get("evidence_facts") if isinstance(evidence_card, dict) else {}) or {})
    bayesian_evidence = dict((evidence_card.get("bayesian_evidence") if isinstance(evidence_card, dict) else {}) or {})

    return {
        "commit_id": commit_id,
        "commit_message": str(record.get("commit_message") or ""),
        "commit_summary": str(record.get("commit_summary") or ""),
        "commit_url": str(record.get("commit_url") or ""),
        "pull_requests": [
            dict(item)
            for item in record.get("pull_requests") or []
            if isinstance(item, dict) and item.get("number") and item.get("url")
        ],
        "changed_files": list(record.get("changed_files") or []),
        "changed_methods": list(record.get("changed_methods") or []),
        "diff_hunks": list(record.get("diff_hunks") or []),
        "call_context": str(record.get("call_context") or ""),
        "functional_category": str(record.get("functional_category") or "unknown"),
        "evidence_granularity": str(record.get("evidence_granularity") or "method_level"),
        "change_detection_status": str(record.get("change_detection_status") or "method_level_change"),
        "arch_impact_prior": _round(priors.get(commit_id, 0.01)),
        "architecture_signal_score": _round(arch_signal),
        "architecture_relevance_score": _round(decision.get("architecture_relevance_score", 0.0)),
        "architecture_relevance_level": str(decision.get("architecture_relevance_level") or "none"),
        "architecture_relevance_labels": list(decision.get("architecture_relevance_labels") or []),
        "architecture_relevance_reason": str(decision.get("architecture_relevance_reason") or ""),
        "structure_role": str(decision.get("structure_role") or role_debug.get(commit_id, {}).get("structure_role", "local_supporting")),
        "primary_module": primary_module,
        "primary_component": primary_component,
        "matched_arch_events": matched_event_ids,
        "event_attributions": attributions,
        "architecture_evidence": {
            "matched_modules": matched_modules,
            "matched_components": matched_components,
            "matched_arch_events": matched_event_cards,
            "matched_arch_event_ids": matched_event_ids,
            "top_event_id": top_event_id,
            "role_reason": str(decision.get("architecture_relevance_reason") or role_debug.get(commit_id, {}).get("role_reason", "")),
            "llm_decision": decision,
            "evidence_scores": evidence_scores,
            "evidence_facts": evidence_facts,
            "bayesian_evidence": bayesian_evidence,
        },
        "confidence": _round(confidence),
        "source_refs": record.get("source_refs") or {},
    }


def _architecture_signal_score(
    commit_id: str,
    events: Sequence[ArchitectureEvent],
    posterior_matrix: Dict[str, Dict[str, float]],
    event_confidences: Dict[str, float],
    priors: Dict[str, float],
) -> float:
    if not events:
        return float(priors.get(commit_id, 0.01)) * 0.2
    values = [
        float(posterior_matrix.get(event.event_id, {}).get(commit_id, 0.0))
        * float(event_confidences.get(event.event_id, 0.0))
        * event.significance
        for event in events
    ]
    return max(values) if values else 0.0


def _primary_module_component(
    record: Dict[str, Any],
    attributions: Sequence[Dict[str, Any]],
    mapping_index: SemArcMappingIndex,
) -> Tuple[str, str]:
    top_event = attributions[0] if attributions else None
    if top_event:
        module = str(top_event.get("module") or "")
        component = str(top_event.get("component") or "")
        if module and module != "unknown":
            return module, component if component else "unknown"

    module_counter: Counter[str] = Counter()
    component_counter: Counter[str] = Counter()
    for file_path in record.get("changed_files") or []:
        module = mapping_index.module_for_file(str(file_path))
        component = mapping_index.component_for_file(str(file_path))
        if module:
            module_counter[module] += 1
        if component:
            component_counter[component] += 1
    module = module_counter.most_common(1)[0][0] if module_counter else "unknown"
    component = component_counter.most_common(1)[0][0] if component_counter else "unknown"
    return module, component


def _commit_confidence(commit_id: str, attributions: Sequence[Dict[str, Any]], priors: Dict[str, float]) -> float:
    if not attributions:
        return float(priors.get(commit_id, 0.01)) * 0.2
    return max(
        float(item.get("posterior", 0.0)) * float(item.get("event_confidence", 0.0))
        for item in attributions
    )


def _record_file_ops(record: Dict[str, Any]) -> Dict[str, Any]:
    changed_files = _unique_paths(_extract_record_files(record))
    explicit_added = _unique_paths(
        _extract_files(record, ("added_files", "new_files"))
        + _extract_file_changes_by_status(record, {"a", "add", "added", "new"})
    )
    explicit_deleted = _unique_paths(
        _extract_files(record, ("deleted_files", "removed_files", "old_files"))
        + _extract_file_changes_by_status(record, {"d", "delete", "deleted", "remove", "removed"})
    )
    explicit_modified = _unique_paths(
        _extract_files(record, ("modified_files",))
        + _extract_file_changes_by_status(record, {"m", "modify", "modified", "change", "changed"})
    )

    has_explicit_ops = bool(explicit_added or explicit_deleted or explicit_modified)
    if not changed_files:
        changed_files = _unique_paths(explicit_added + explicit_deleted + explicit_modified)
    if not explicit_modified and not has_explicit_ops:
        explicit_modified = list(changed_files)

    return {
        "changed_files": changed_files,
        "added_files": explicit_added,
        "deleted_files": explicit_deleted,
        "modified_files": explicit_modified if explicit_modified else ([] if has_explicit_ops else list(changed_files)),
        "has_explicit_ops": has_explicit_ops,
    }


def _operation_match(ops: Dict[str, List[str]], event: ArchitectureEvent, file_overlap: float, component_match: float) -> float:
    if event.event_type == "module_added":
        event_files = event.added_files or event.related_files
        commit_files = ops["added_files"] or ops["changed_files"]
        return _f1_overlap(commit_files, event_files)
    if event.event_type == "module_removed":
        event_files = event.removed_files or event.related_files
        commit_files = ops["deleted_files"] or ops["changed_files"]
        return _f1_overlap(commit_files, event_files)
    if event.event_type == "module_changed":
        event_files = event.related_files
        commit_files = ops["modified_files"] or ops["changed_files"]
        return _f1_overlap(commit_files, event_files)
    if event.event_type == "component_changed":
        return (component_match + file_overlap) / 2.0
    return file_overlap


def _negative_evidence(record: Dict[str, Any], changed_files: Sequence[str]) -> float:
    text = " ".join(
        [
            str(record.get("commit_message") or ""),
            str(record.get("commit_summary") or ""),
            str(record.get("functional_category") or ""),
        ]
    ).lower()
    if not changed_files:
        return 1.0 if _text_is_low_value(text) else 0.0
    low_count = sum(1 for file_path in changed_files if _is_low_value_path(file_path))
    ratio = low_count / max(1, len(changed_files))
    if _text_is_low_value(text):
        ratio = max(ratio, 0.85)
    if low_count == len(changed_files):
        ratio = 1.0
    return _clip(ratio, 0.0, 1.0)


def _text_is_low_value(text: str) -> bool:
    return any(
        marker in text
        for marker in (
            "docs only",
            "documentation only",
            "comments only",
            "comment only",
            "formatting only",
            "formatting-only",
            "format only",
            "whitespace",
            "indentation",
            "prettier",
            "black",
            "clang-format",
            "gofmt",
            "snapshot only",
            "generated files only",
            "version bump only",
            "metadata only",
            "lock file only",
            "typo",
            "spelling",
        )
    ) or text.strip() in {"docs", "documentation", "format", "formatting", "comments", "comment", "metadata"}


def _is_low_value_path(path: str) -> bool:
    lower = normalize_path(path).lower()
    basename = lower.rsplit("/", 1)[-1]
    parts = lower.split("/")
    lockfiles = {
        "package-lock.json",
        "yarn.lock",
        "pnpm-lock.yaml",
        "cargo.lock",
        "go.sum",
        "poetry.lock",
        "pipfile.lock",
    }
    if basename in lockfiles:
        return True
    if basename.endswith((".md", ".rst", ".adoc", ".txt", ".snap", ".snapshot")):
        return True
    if any(part in {"docs", "doc", "documentation", "test", "tests", "__tests__", "spec", "snapshot", "snapshots", ".travis_scripts"} for part in parts):
        return True
    if any(part in {"dist", "build", "generated"} for part in parts):
        return True
    if lower.startswith((".github/", ".gitlab/", ".circleci/", ".azure-pipelines/")):
        return True
    if basename in {"version", "version.txt", "metadata.json", "manifest.json", ".travis.yml", ".gitlab-ci.yml", "appveyor.yml", ".appveyor.yml", "azure-pipelines.yml"}:
        return True
    if basename.endswith((".dict", ".expected", ".golden")):
        return True
    return False


def _f1_overlap(left: Sequence[str], right: Sequence[str]) -> float:
    left_unique = _unique_paths(left)
    right_unique = _unique_paths(right)
    if not left_unique or not right_unique:
        return 0.0
    overlap = _path_intersection_count(left_unique, right_unique)
    precision = overlap / len(left_unique)
    recall = overlap / len(right_unique)
    return 2.0 * precision * recall / (precision + recall + EPS)


def _path_intersection_count(left: Sequence[str], right: Sequence[str]) -> int:
    matched_right: Set[int] = set()
    count = 0
    for left_path in left:
        for index, right_path in enumerate(right):
            if index in matched_right:
                continue
            if _path_matches(left_path, right_path):
                matched_right.add(index)
                count += 1
                break
    return count


def _path_matches(left: str, right: str) -> bool:
    left_key = _path_key(left)
    right_key = _path_key(right)
    if not left_key or not right_key:
        return False
    return left_key == right_key or left_key.endswith(f"/{right_key}") or right_key.endswith(f"/{left_key}")


def _lookup_path_map(mapping: Dict[str, str], path: str) -> Optional[str]:
    exact_lookup, suffix_candidates = _build_path_lookup_index(mapping)
    return _lookup_path_index(
        exact_lookup=exact_lookup,
        suffix_candidates=suffix_candidates,
        lookup_cache={},
        path=path,
    )


def _build_path_lookup_index(mapping: Dict[str, str]) -> Tuple[Dict[str, str], List[Tuple[str, str]]]:
    exact_lookup: Dict[str, str] = {}
    suffix_candidates: List[Tuple[str, str]] = []
    for candidate, value in mapping.items():
        candidate_key = _path_key(candidate)
        if not candidate_key:
            continue
        exact_lookup.setdefault(candidate_key, value)
        suffix_candidates.append((candidate_key, value))
    return exact_lookup, suffix_candidates


def _lookup_path_index(
    *,
    exact_lookup: Dict[str, str],
    suffix_candidates: Sequence[Tuple[str, str]],
    lookup_cache: Dict[str, Optional[str]],
    path: str,
) -> Optional[str]:
    key = _path_key(path)
    if not key:
        return None
    if key in lookup_cache:
        return lookup_cache[key]
    exact_value = exact_lookup.get(key)
    if exact_value is not None:
        lookup_cache[key] = exact_value
        return exact_value
    for candidate_key, value in suffix_candidates:
        if key.endswith(f"/{candidate_key}") or candidate_key.endswith(f"/{key}"):
            lookup_cache[key] = value
            return value
    lookup_cache[key] = None
    return None


def normalize_path(path: Any) -> str:
    if path is None:
        return ""
    text = str(path).replace("\\", "/").strip().strip('"').strip("'")
    text = re.sub(r"^[A-Za-z]:/", "", text)
    text = re.sub(r"/+", "/", text)
    while text.startswith("./"):
        text = text[2:]
    if text.startswith("a/") or text.startswith("b/"):
        text = text[2:]
    return text.strip("/")


def _path_key(path: Any) -> str:
    return normalize_path(path).lower()


def _extract_record_files(record: Dict[str, Any]) -> List[str]:
    files = _extract_files(record, ("changed_files", "all_changed_files", "files"))
    files.extend(_extract_files(record.get("source_refs") or {}, ("changed_files", "files")))
    files.extend(_extract_file_changes_by_status(record, set()))
    return files


def _extract_file_changes_by_status(record: Dict[str, Any], statuses: Set[str]) -> List[str]:
    result: List[str] = []
    for key in ("file_changes", "changed_file_records", "files"):
        value = record.get(key)
        if not isinstance(value, list):
            continue
        for item in value:
            if not isinstance(item, dict):
                continue
            status = str(item.get("status") or item.get("change_type") or item.get("operation") or "").strip().lower()
            if statuses and status not in statuses:
                continue
            file_path = _first_text(item.get("path"), item.get("file"), item.get("filename"), item.get("name"))
            if file_path:
                result.append(file_path)
    return result


def _extract_files(container: Any, keys: Sequence[str]) -> List[str]:
    if not isinstance(container, dict):
        return []
    result: List[str] = []
    for key in keys:
        value = container.get(key)
        if value is None:
            continue
        result.extend(_coerce_file_values(value))
    return result


def _extract_semantic_code_files(detail: Dict[str, Any], keys: Sequence[str]) -> List[str]:
    semantics = detail.get("semantics") if isinstance(detail, dict) else {}
    code = semantics.get("code") if isinstance(semantics, dict) else {}
    return _extract_files(code, keys)


def _coerce_file_values(value: Any) -> List[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        path = _first_text(value.get("path"), value.get("file"), value.get("filename"), value.get("name"))
        return [path] if path else []
    if not isinstance(value, list):
        return []
    result: List[str] = []
    for item in value:
        result.extend(_coerce_file_values(item))
    return result


def _unique_paths(values: Iterable[Any]) -> List[str]:
    result: List[str] = []
    seen: Set[str] = set()
    for value in values:
        normalized = normalize_path(value)
        key = _path_key(normalized)
        if not normalized or key in seen:
            continue
        result.append(normalized)
        seen.add(key)
    return result


def _parse_namedclusters(path: Optional[Path]) -> Dict[str, Set[str]]:
    payload = _load_json(path)
    module_to_files: Dict[str, Set[str]] = defaultdict(set)
    if not payload:
        return {}

    structure = payload.get("structure") if isinstance(payload, dict) else None
    if isinstance(structure, list):
        for node in structure:
            if not isinstance(node, dict) or str(node.get("@type") or "").lower() != "group":
                continue
            module = str(node.get("name") or "").strip()
            if not module:
                continue
            files = []
            for nested in node.get("nested") or []:
                if isinstance(nested, dict) and str(nested.get("@type") or "").lower() == "item":
                    files.append(nested.get("name"))
            module_to_files[module].update(_unique_paths(files))
        return module_to_files

    candidates = payload.get("modules") or payload.get("clusters") or payload.get("named_clusters") if isinstance(payload, dict) else {}
    if isinstance(candidates, dict):
        for module, files in candidates.items():
            module_to_files[str(module)].update(_unique_paths(_coerce_file_values(files)))
    elif isinstance(candidates, list):
        for item in candidates:
            if not isinstance(item, dict):
                continue
            module = _first_text(item.get("name"), item.get("module"), item.get("module_name"))
            files = _extract_files(item, ("files", "items", "nested"))
            if module:
                module_to_files[module].update(_unique_paths(files))
    return module_to_files


def _parse_clustercomponent(path: Optional[Path]) -> Dict[str, Set[str]]:
    payload = _load_json(path)
    component_to_modules: Dict[str, Set[str]] = defaultdict(set)
    if not payload:
        return {}

    structure = payload.get("structure") if isinstance(payload, dict) else None
    if isinstance(structure, list):
        for component_node in structure:
            if not isinstance(component_node, dict) or str(component_node.get("@type") or "").lower() != "component":
                continue
            component = str(component_node.get("name") or "").strip()
            if not component:
                continue
            modules = []
            for nested in component_node.get("nested") or []:
                if isinstance(nested, dict) and str(nested.get("@type") or "").lower() == "cluster":
                    modules.append(str(nested.get("name") or "").strip())
            component_to_modules[component].update(item for item in modules if item)
        return component_to_modules

    candidates = payload.get("components") or payload.get("component_to_modules") if isinstance(payload, dict) else {}
    if isinstance(candidates, dict):
        for component, modules in candidates.items():
            if isinstance(modules, list):
                component_to_modules[str(component)].update(str(item) for item in modules if str(item))
    elif isinstance(candidates, list):
        for item in candidates:
            if not isinstance(item, dict):
                continue
            component = _first_text(item.get("name"), item.get("component"), item.get("component_name"))
            modules = item.get("modules") or item.get("clusters") or []
            if component and isinstance(modules, list):
                component_to_modules[component].update(str(module) for module in modules if str(module))
    return component_to_modules


def _iter_raw_events(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    if not isinstance(payload, dict):
        return []
    for key in ("changes", "architecture_events", "events", "diff_events"):
        value = payload.get(key)
        if isinstance(value, list):
            return [item for item in value if isinstance(item, dict)]
    return []


def _resolve_diff_ir_path(path: Optional[Path]) -> Optional[Path]:
    if path and path.exists():
        return path
    if not path:
        return None
    candidates = [
        path.parent / "diff_ir-denoised-significance.json",
        path.parent / "diff_ir-denoised.json",
        path.parent / "diff_ir-summary.json",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return path


def _extract_component(raw_event: Dict[str, Any], detail: Dict[str, Any]) -> str:
    semantics = detail.get("semantics") if isinstance(detail, dict) else {}
    arch = semantics.get("arch") if isinstance(semantics, dict) else {}
    return _first_text(
        raw_event.get("component"),
        raw_event.get("component_name"),
        detail.get("component"),
        detail.get("component_name"),
        detail.get("to_component"),
        detail.get("from_component"),
        arch.get("to_component") if isinstance(arch, dict) else "",
        arch.get("from_component") if isinstance(arch, dict) else "",
    )


def _normalize_event_type(value: Any) -> str:
    text = str(value or "").strip().lower()
    return text if text in SUPPORTED_EVENT_TYPES else "other"


def _strip_module_uid(value: Any) -> str:
    text = str(value or "").strip()
    if "#" in text:
        return text.split("#", 1)[0]
    return text


def _is_important_event(event: ArchitectureEvent, event_confidence: float) -> bool:
    return (
        event.event_type in PROTECTED_EVENT_TYPES
        or event.significance >= 0.6
        or (event_confidence >= 0.6 and event.significance >= 0.5)
    )


def _role_in_event(commit_id: str, event_id: str, event_sets: Dict[str, Dict[str, Any]]) -> str:
    sets = event_sets.get(event_id, {})
    if commit_id in sets.get("core_set", []):
        return "core"
    if commit_id in sets.get("support_set", []):
        return "support"
    return "weak"


def _best_event(
    event_ids: Sequence[str],
    event_by_id: Dict[str, ArchitectureEvent],
    posterior_matrix: Dict[str, Dict[str, float]],
    event_confidences: Dict[str, float],
    commit_id: str,
) -> str:
    if not event_ids:
        return ""
    return max(
        event_ids,
        key=lambda event_id: (
            posterior_matrix.get(event_id, {}).get(commit_id, 0.0)
            * event_confidences.get(event_id, 0.0)
            * event_by_id.get(event_id, ArchitectureEvent(event_id, "other")).significance,
            event_id,
        ),
    )


def _max_evidence_value(
    commit_id: str,
    events: Sequence[ArchitectureEvent],
    evidence_matrix: Dict[str, Dict[str, Dict[str, float]]],
    feature_name: str,
) -> float:
    if not events:
        return 0.0
    return max(
        float(evidence_matrix.get(event.event_id, {}).get(commit_id, {}).get(feature_name, 0.0))
        for event in events
    )


def _debug_evidence_matrix(
    records: Sequence[Dict[str, Any]],
    events: Sequence[ArchitectureEvent],
    evidence_matrix: Dict[str, Dict[str, Dict[str, float]]],
) -> Dict[str, Any]:
    return {
        event.event_id: {
            str(record.get("commit_id") or ""): evidence_matrix.get(event.event_id, {}).get(
                str(record.get("commit_id") or ""),
                {},
            )
            for record in records
        }
        for event in events
    }


def _debug_posterior_matrix(
    records: Sequence[Dict[str, Any]],
    events: Sequence[ArchitectureEvent],
    posterior_matrix: Dict[str, Dict[str, float]],
    reliability_by_event: Dict[str, Dict[str, float]],
    event_confidences: Dict[str, float],
) -> Dict[str, Any]:
    return {
        event.event_id: {
            "event_type": event.event_type,
            "module": event.module,
            "component": event.component,
            "significance": _round(event.significance),
            "event_confidence": _round(event_confidences.get(event.event_id, 0.0)),
            "feature_reliability": reliability_by_event.get(event.event_id, {}),
            "posteriors": {
                str(record.get("commit_id") or ""): _round(
                    posterior_matrix.get(event.event_id, {}).get(str(record.get("commit_id") or ""), 0.0),
                    8,
                )
                for record in records
            },
        }
        for event in events
    }


def _stats(records: Sequence[Dict[str, Any]], events: Sequence[ArchitectureEvent]) -> Dict[str, Any]:
    role_counts = Counter(str(record.get("structure_role") or "local_supporting") for record in records)
    return {
        "attributed_record_count": len(records),
        "architecture_event_count": len(events),
        "structure_guiding_count": role_counts.get("structure_guiding", 0),
        "architecture_related_supporting_count": role_counts.get("architecture_related_supporting", 0),
        "global_supporting_count": role_counts.get("global_supporting", 0),
        "local_supporting_count": role_counts.get("local_supporting", 0),
    }


def _export(output: Dict[str, Any], debug_payloads: Dict[str, Any], output_dir: Path) -> Dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    attributed_path = output_dir / "attributed_change_records.json"
    debug_md_path = output_dir / "architecture_attribution_debug.md"
    _write_json(attributed_path, output)
    debug_md_path.write_text(_render_debug(output), encoding="utf-8")

    output_files = {
        "attributed_change_records": str(attributed_path),
        "architecture_attribution_debug": str(debug_md_path),
    }
    for name, payload in debug_payloads.items():
        path = output_dir / f"{name}.json"
        _write_json(path, payload)
        output_files[name] = str(path)
    return output_files


def _render_debug(output: Dict[str, Any]) -> str:
    lines = [
        "# Phase 2 Key Design-Decision Commit Identification Debug",
        "",
        "Phase 2 estimates posterior attribution probabilities P(c|e) per architecture event.",
        "The architecture_signal_score is derived from posterior attribution, not the old weighted ARS.",
        "",
        "## Records",
        "",
    ]
    for record in output.get("attributed_change_records") or []:
        evidence = record.get("architecture_evidence") or {}
        lines.append(f"### {str(record.get('commit_id') or '')[:12] or 'unknown'}")
        lines.append(f"- prior: `{record.get('arch_impact_prior')}`")
        lines.append(f"- signal: `{record.get('architecture_signal_score')}`")
        lines.append(f"- role: `{record.get('structure_role')}`")
        lines.append(f"- confidence: `{record.get('confidence')}`")
        lines.append(f"- module/component: `{record.get('primary_module')}` / `{record.get('primary_component')}`")
        lines.append(f"- top_event_id: `{evidence.get('top_event_id') or ''}`")
        lines.append(f"- role_reason: {evidence.get('role_reason') or ''}")
        lines.append("")
    return "\n".join(lines)


def _write_json(path: Path, payload: Any) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)


def _load_json(path: Optional[Path]) -> Dict[str, Any]:
    if not path or not Path(path).exists():
        return {}
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception:
        return {}


def _softmax(scores: Sequence[Tuple[str, float]]) -> Dict[str, float]:
    if not scores:
        return {}
    max_score = max(score for _, score in scores)
    exp_values = [(commit_id, math.exp(score - max_score)) for commit_id, score in scores]
    denominator = sum(value for _, value in exp_values)
    if denominator <= EPS:
        uniform = 1.0 / len(scores)
        return {commit_id: uniform for commit_id, _ in scores}
    return {commit_id: value / denominator for commit_id, value in exp_values}


def _cumulative_set(ordered: Sequence[Tuple[str, float]], threshold: float) -> List[str]:
    result: List[str] = []
    total = 0.0
    for commit_id, posterior in ordered:
        result.append(commit_id)
        total += posterior
        if total + EPS >= threshold:
            break
    return result


def _robust_z_scores(values: Sequence[float]) -> List[float]:
    if not values:
        return []
    median = _median(values)
    deviations = [abs(value - median) for value in values]
    mad = _median(deviations)
    if mad <= EPS:
        return [0.0 for _ in values]
    return [(value - median) / (mad + EPS) for value in values]


def _median(values: Sequence[float]) -> float:
    ordered = sorted(float(value) for value in values)
    if not ordered:
        return 0.0
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2.0


def _percentile(values: Sequence[float], quantile: float) -> float:
    ordered = sorted(float(value) for value in values)
    if not ordered:
        return 0.0
    if len(ordered) == 1:
        return ordered[0]
    index = (len(ordered) - 1) * quantile
    lower = math.floor(index)
    upper = math.ceil(index)
    if lower == upper:
        return ordered[int(index)]
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (index - lower)


def _sigmoid(value: float) -> float:
    if value >= 0:
        z = math.exp(-value)
        return 1.0 / (1.0 + z)
    z = math.exp(value)
    return z / (1.0 + z)


def _entropy(values: Sequence[str]) -> float:
    filtered = [str(value) for value in values if str(value)]
    if not filtered:
        return 0.0
    counts = Counter(filtered)
    total = sum(counts.values())
    return -sum((count / total) * math.log(count / total + EPS) for count in counts.values())


def _top_directory(path: str) -> str:
    normalized = normalize_path(path)
    if "/" not in normalized:
        return normalized
    return normalized.split("/", 1)[0]


def _record_text(record: Dict[str, Any]) -> str:
    return " ".join(
        [
            str(record.get("commit_message") or ""),
            str(record.get("commit_summary") or ""),
            str(record.get("functional_category") or ""),
            " ".join(str(item) for item in record.get("changed_methods") or []),
            " ".join(str(item) for item in record.get("changed_files") or []),
        ]
    )


def _is_build_or_release_path(path: str) -> bool:
    lower = normalize_path(path).lower()
    basename = lower.rsplit("/", 1)[-1]
    if basename in {
        "cmakelists.txt",
        "meson.build",
        "meson_options.txt",
        "makefile",
        "gnumakefile",
        "configure.ac",
        "build",
        "build.bazel",
        "workspace",
        "workspace.bazel",
        "makerelease.py",
        ".travis.yml",
        ".gitlab-ci.yml",
        "appveyor.yml",
        ".appveyor.yml",
        "azure-pipelines.yml",
    }:
        return True
    if basename.endswith((".cmake", ".mk", ".pc.in")):
        return True
    if lower.startswith(("pkg-config/", ".github/", ".gitlab/", ".circleci/", ".azure-pipelines/")):
        return True
    if any(part in {"scripts", "devtools", "release", ".travis_scripts"} for part in lower.split("/")):
        return True
    return False


def _looks_public_method(method: str) -> bool:
    text = str(method or "")
    return "::" in text or text[:1].isupper() or "public" in text.lower()


def _is_core_name(name: str) -> bool:
    lower = str(name or "").lower()
    return any(
        marker in lower
        for marker in (
            "core",
            "api",
            "public",
            "runtime",
            "engine",
            "kernel",
            "model",
            "parser",
            "reader",
            "writer",
            "broker",
            "client proxy",
        )
    )


def _module_has_public_surface(module: str, mapping_index: SemArcMappingIndex) -> bool:
    files = mapping_index.module_to_files.get(module, set())
    return any(normalize_path(file_path).lower().startswith("include/") for file_path in files)


def _file_area_category(path: str) -> str:
    lower = normalize_path(path).lower()
    basename = lower.rsplit("/", 1)[-1]
    if lower.startswith("include/") or basename.endswith((".h", ".hpp", ".hh", ".hxx")):
        return "public_header"
    if lower.startswith(("src/", "source/")) or basename.endswith((".c", ".cc", ".cpp", ".cxx")):
        return "implementation"
    if any(part in {"test", "tests", "testing", "unittest", "fuzz"} for part in lower.split("/")) or basename.endswith((".dict", ".expected", ".golden")):
        return "test_resource"
    if basename.endswith((".md", ".rst", ".adoc", ".txt")) or any(part in {"docs", "doc", "documentation"} for part in lower.split("/")):
        return "documentation"
    if _is_build_or_release_path(lower):
        return "build_ci_release"
    if basename.endswith((".json", ".in", ".out")):
        return "resource_or_metadata"
    return "other"


def _most_common(values: Sequence[str]) -> str:
    filtered = [str(value) for value in values if str(value)]
    if not filtered:
        return ""
    return Counter(filtered).most_common(1)[0][0]


def _string_list(value: Any) -> List[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def _names_intersect(left: Iterable[str], right: Iterable[str]) -> bool:
    left_keys = {_name_key(item) for item in left if str(item)}
    right_keys = {_name_key(item) for item in right if str(item)}
    return bool(left_keys & right_keys)


def _name_key(value: Any) -> str:
    text = str(value or "").strip().lower()
    text = re.sub(r"#\d+$", "", text)
    return text


def _first_text(*values: Any) -> str:
    for value in values:
        text = str(value or "").strip()
        if text:
            return text
    return ""


def _safe_float(*values: Any, default: float = 0.0) -> float:
    for value in values:
        if value is None or value == "":
            continue
        try:
            result = float(value)
        except Exception:
            continue
        if math.isfinite(result):
            return result
    return default


def _clip(value: float, lower: float, upper: float) -> float:
    if not math.isfinite(value):
        return lower
    return min(upper, max(lower, value))


def _round(value: Any, digits: int = 4) -> float:
    try:
        numeric = float(value)
    except Exception:
        return 0.0
    if not math.isfinite(numeric):
        return 0.0
    return round(numeric, digits)


def _unique(values: Iterable[Any]) -> List[str]:
    result: List[str] = []
    seen: Set[str] = set()
    for value in values:
        text = str(value or "").strip()
        if not text or text in seen:
            continue
        result.append(text)
        seen.add(text)
    return result


def _slug(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", value.strip())[:80] or "unknown"
