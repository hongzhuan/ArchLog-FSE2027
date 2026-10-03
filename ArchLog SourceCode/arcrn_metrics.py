from __future__ import annotations

import json
import time
from dataclasses import asdict, is_dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

from arcrn_output_layout import stage_output_dir


METRICS_SCHEMA_VERSION = 1
LLM_METRIC_TOKEN_FIELDS = ("prompt_tokens", "completion_tokens", "reasoning_tokens", "total_tokens")


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def start_timer() -> Tuple[str, float]:
    return utc_now_iso(), time.perf_counter()


def elapsed_sec(started_perf: Optional[float]) -> Optional[float]:
    if started_perf is None:
        return None
    return round(max(0.0, time.perf_counter() - started_perf), 6)


def duration_between_iso(started_at: Optional[str], finished_at: Optional[str]) -> Optional[float]:
    if not started_at or not finished_at:
        return None
    try:
        started = datetime.fromisoformat(str(started_at).replace("Z", "+00:00"))
        finished = datetime.fromisoformat(str(finished_at).replace("Z", "+00:00"))
    except Exception:
        return None
    return round(max(0.0, (finished - started).total_seconds()), 6)


def normalize_llm_metrics(value: Any) -> Dict[str, Any]:
    return dict(value) if isinstance(value, dict) else {}


def build_llm_call_metrics(
    *,
    stage: str,
    request_name: str,
    config: Any,
    system_prompt: str,
    user_prompt: str,
    raw_response: Optional[str],
    response: Any = None,
    success: bool = True,
    started_at: Optional[str] = None,
    started_perf: Optional[float] = None,
    finished_at: Optional[str] = None,
    duration_sec: Optional[float] = None,
    transport_attempt_count: int = 1,
    validation_attempt_count: int = 1,
    is_validation_retry: bool = False,
    error_type: str = "",
    error_message: str = "",
) -> Dict[str, Any]:
    resolved_finished_at = finished_at or utc_now_iso()
    resolved_duration = duration_sec if duration_sec is not None else elapsed_sec(started_perf)
    raw_usage = extract_raw_usage(response)
    token_fields = extract_common_usage(raw_usage)
    output_text = raw_response or ""
    system_chars = len(system_prompt or "")
    user_chars = len(user_prompt or "")
    metric = {
        "schema_version": METRICS_SCHEMA_VERSION,
        "stage": str(stage or ""),
        "request_name": str(request_name or ""),
        "provider": str(getattr(config, "llm_provider", "") or ""),
        "model": str(getattr(config, "llm_model_name", "") or ""),
        "thinking_enabled": bool(getattr(config, "llm_enable_thinking", False)),
        "success": bool(success),
        "started_at": started_at,
        "finished_at": resolved_finished_at,
        "duration_sec": resolved_duration,
        "system_prompt_chars": system_chars,
        "user_prompt_chars": user_chars,
        "input_chars": system_chars + user_chars,
        "output_chars": len(output_text),
        "transport_attempt_count": max(1, int(transport_attempt_count or 1)),
        "validation_attempt_count": max(1, int(validation_attempt_count or 1)),
        "is_validation_retry": bool(is_validation_retry),
        "error_type": str(error_type or ""),
        "error_message": str(error_message or ""),
        "raw_usage": raw_usage,
    }
    metric.update(token_fields)
    return metric


def mark_llm_metric_attempt(
    metric: Any,
    *,
    transport_attempt_count: Optional[int] = None,
    validation_attempt_count: Optional[int] = None,
    is_validation_retry: Optional[bool] = None,
    success: Optional[bool] = None,
    error_type: Optional[str] = None,
    error_message: Optional[str] = None,
) -> Dict[str, Any]:
    data = normalize_llm_metrics(metric)
    if transport_attempt_count is not None:
        data["transport_attempt_count"] = max(1, int(transport_attempt_count or 1))
    if validation_attempt_count is not None:
        data["validation_attempt_count"] = max(1, int(validation_attempt_count or 1))
    if is_validation_retry is not None:
        data["is_validation_retry"] = bool(is_validation_retry)
    if success is not None:
        data["success"] = bool(success)
    if error_type is not None:
        data["error_type"] = str(error_type or "")
    if error_message is not None:
        data["error_message"] = str(error_message or "")
    return data


def extract_raw_usage(response: Any) -> Optional[Dict[str, Any]]:
    if response is None:
        return None
    usage = None
    if isinstance(response, dict):
        usage = response.get("usage")
    else:
        usage = getattr(response, "usage", None)
    if usage is None:
        return None
    converted = _to_jsonable(usage)
    return converted if isinstance(converted, dict) else None


def extract_common_usage(raw_usage: Optional[Dict[str, Any]]) -> Dict[str, Optional[int]]:
    result: Dict[str, Optional[int]] = {field: None for field in LLM_METRIC_TOKEN_FIELDS}
    if not isinstance(raw_usage, dict):
        return result
    result["prompt_tokens"] = _safe_int(raw_usage.get("prompt_tokens") or raw_usage.get("input_tokens"))
    result["completion_tokens"] = _safe_int(raw_usage.get("completion_tokens") or raw_usage.get("output_tokens"))
    result["total_tokens"] = _safe_int(raw_usage.get("total_tokens"))
    result["reasoning_tokens"] = _find_reasoning_tokens(raw_usage)
    return result


def write_experiment_metrics(
    *,
    output_dir: Path,
    config: Any,
    pipeline_result: Any,
    started_at: str,
    finished_at: str,
    duration_sec: float,
) -> Dict[str, Any]:
    summary_dir = stage_output_dir(Path(output_dir), "pipeline")
    summary_dir.mkdir(parents=True, exist_ok=True)
    llm_metrics = collect_llm_metrics(Path(output_dir))
    llm_jsonl_path = summary_dir / "llm_call_metrics.jsonl"
    with llm_jsonl_path.open("w", encoding="utf-8") as handle:
        for metric in llm_metrics:
            handle.write(json.dumps(metric, ensure_ascii=False) + "\n")

    experiment_metrics = {
        "schema_version": METRICS_SCHEMA_VERSION,
        "generated_at": utc_now_iso(),
        "repo_name": str(getattr(pipeline_result, "repo_name", "") or ""),
        "base_ref": str(getattr(pipeline_result, "base_ref", "") or ""),
        "new_ref": str(getattr(pipeline_result, "new_ref", "") or ""),
        "provider": str(getattr(config, "llm_provider", "") or ""),
        "model": str(getattr(config, "llm_model_name", "") or ""),
        "thinking_enabled": bool(getattr(config, "llm_enable_thinking", False)),
        "runtime": {
            "started_at": started_at,
            "finished_at": finished_at,
            "duration_sec": round(float(duration_sec), 6),
        },
        "stages": _stage_metrics(pipeline_result, Path(output_dir)),
        "llm_totals": aggregate_llm_metrics(llm_metrics),
        "llm_by_stage": aggregate_llm_metrics_by_stage(llm_metrics),
        "quality_and_coverage": build_quality_and_coverage(pipeline_result, llm_metrics),
    }
    metrics_path = summary_dir / "experiment_metrics.json"
    metrics_path.write_text(json.dumps(experiment_metrics, ensure_ascii=False, indent=2), encoding="utf-8")
    return {
        "experiment_metrics": str(metrics_path),
        "llm_call_metrics_jsonl": str(llm_jsonl_path),
        "llm_totals": experiment_metrics["llm_totals"],
        "llm_call_count": experiment_metrics["llm_totals"]["call_count"],
        "total_tokens": experiment_metrics["llm_totals"]["total_tokens"],
    }


def collect_llm_metrics(output_dir: Path) -> List[Dict[str, Any]]:
    metrics: List[Dict[str, Any]] = []
    metrics.extend(_collect_step10_metrics(output_dir))
    metrics.extend(_collect_json_list(output_dir / "03_phase2_arch_signal_attribution" / "phase2_llm_call_metrics.json"))
    metrics.extend(_collect_phase3_1_metrics(output_dir))
    metrics.extend(_collect_audit_record_attempt_metrics(output_dir / "05_phase3_2_slot_entry_generation" / "phase3_slot_entry_llm_audit.json"))
    metrics.extend(_collect_audit_record_attempt_metrics(output_dir / "05_phase3_2_slot_entry_generation" / "phase3_arch_label_llm_audit.json"))
    metrics.extend(_collect_audit_record_attempt_metrics(output_dir / "05_phase3_2_slot_entry_generation" / "phase3_arch_module_assignment_llm_audit.json"))
    metrics.extend(_collect_final_composition_metrics(output_dir / "06_phase3_3_final_composition" / "phase3_final_composition_llm_audit.json"))
    return [_minimal_metric(metric) for metric in metrics if isinstance(metric, dict)]


def aggregate_llm_metrics(metrics: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    total = _empty_llm_aggregate()
    token_sums = {field: 0 for field in LLM_METRIC_TOKEN_FIELDS}
    token_seen = {field: False for field in LLM_METRIC_TOKEN_FIELDS}
    for metric in metrics:
        total["call_count"] += 1
        if bool(metric.get("success", False)):
            total["success_count"] += 1
        else:
            total["failure_count"] += 1
        total["input_chars"] += _safe_int(metric.get("input_chars")) or 0
        total["output_chars"] += _safe_int(metric.get("output_chars")) or 0
        total["llm_duration_sec"] += float(metric.get("duration_sec") or 0.0)
        total["transport_retry_count"] += max(0, (_safe_int(metric.get("transport_attempt_count")) or 1) - 1)
        if bool(metric.get("is_validation_retry", False)):
            total["validation_retry_count"] += 1
        for field in LLM_METRIC_TOKEN_FIELDS:
            value = _safe_int(metric.get(field))
            if value is not None:
                token_sums[field] += value
                token_seen[field] = True
    for field in LLM_METRIC_TOKEN_FIELDS:
        total[field] = token_sums[field] if token_seen[field] else None
    total["llm_duration_sec"] = round(total["llm_duration_sec"], 6)
    return total


def aggregate_llm_metrics_by_stage(metrics: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    by_stage: Dict[str, List[Dict[str, Any]]] = {}
    for metric in metrics:
        by_stage.setdefault(str(metric.get("stage") or "unknown"), []).append(metric)
    return {stage: aggregate_llm_metrics(items) for stage, items in sorted(by_stage.items())}


def build_quality_and_coverage(pipeline_result: Any, llm_metrics: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    stage_stats = _stats_by_stage(pipeline_result)
    code_stats = stage_stats.get("code_changes", {})
    phase1_stats = stage_stats.get("phase1_change_evidence_modeling", {})
    phase3_1_stats = stage_stats.get("phase3_1_llm_aggregation_planning", {})
    phase3_2_stats = stage_stats.get("phase3_2_slot_level_entry_generation", {})
    phase3_3_stats = stage_stats.get("phase3_3_document_level_composition", {})
    phase3_covered = phase3_1_stats.get("covered_commits")
    if phase3_covered is None:
        included = _safe_int(phase3_1_stats.get("included_commits")) or 0
        deprioritized = _safe_int(phase3_1_stats.get("deprioritized_commits")) or 0
        filtered = _safe_int(phase3_1_stats.get("filtered_commits")) or 0
        phase3_covered = included + deprioritized + filtered
    coverage = {
        "commit_count": phase1_stats.get("commit_count"),
        "change_unit_count": code_stats.get("change_units_count"),
        "summary_count": code_stats.get("summaries_count"),
        "phase3_covered_commits": phase3_covered,
        "included_commits": phase3_1_stats.get("included_commits"),
        "deprioritized_commits": phase3_1_stats.get("deprioritized_commits"),
        "filtered_commits": phase3_1_stats.get("filtered_commits"),
        "unassigned_commits": phase3_1_stats.get("unassigned_commits"),
        "release_note_entry_count": phase3_2_stats.get("entry_count") or phase3_3_stats.get("entry_count"),
        "architecture_labeled_entry_count": phase3_2_stats.get("architecture_labeled_entry_count"),
    }
    totals = aggregate_llm_metrics(llm_metrics)
    coverage.update(
        {
            "llm_json_validation_retry_count": totals["validation_retry_count"],
            "llm_failure_count": totals["failure_count"],
        }
    )
    return coverage


def _collect_step10_metrics(output_dir: Path) -> List[Dict[str, Any]]:
    payload = _read_json(output_dir / "01_code_changes" / "step10_code_change_summaries.json")
    summaries = payload.get("summaries") if isinstance(payload, dict) else None
    if summaries is None:
        payload = _read_json(output_dir / "01_code_changes" / "code_change_summaries.json")
        summaries = payload.get("summaries") if isinstance(payload, dict) else None
    result = []
    for summary in summaries or []:
        if isinstance(summary, dict) and isinstance(summary.get("llm_metrics"), dict):
            result.append(summary["llm_metrics"])
    return result


def _collect_phase3_1_metrics(output_dir: Path) -> List[Dict[str, Any]]:
    payload = _read_json(output_dir / "04_phase3_1_llm_aggregation_planning" / "phase3_aggregation_plan_llm_audit.json")
    result = []
    for call in (payload.get("calls") if isinstance(payload, dict) else []) or []:
        if not isinstance(call, dict):
            continue
        for metric in call.get("llm_call_metrics") or []:
            if isinstance(metric, dict):
                result.append(metric)
        if not call.get("llm_call_metrics") and isinstance(call.get("llm_metrics"), dict):
            result.append(call["llm_metrics"])
    return result


def _collect_audit_record_attempt_metrics(path: Path) -> List[Dict[str, Any]]:
    payload = _read_json(path)
    result = []
    for record in (payload.get("records") if isinstance(payload, dict) else []) or []:
        if not isinstance(record, dict):
            continue
        for attempt in record.get("attempts") or []:
            if isinstance(attempt, dict) and isinstance(attempt.get("llm_metrics"), dict):
                result.append(attempt["llm_metrics"])
    return result


def _collect_final_composition_metrics(path: Path) -> List[Dict[str, Any]]:
    payload = _read_json(path)
    result = []
    for call in (payload.get("calls") if isinstance(payload, dict) else []) or []:
        if not isinstance(call, dict):
            continue
        for attempt in call.get("attempts") or []:
            if isinstance(attempt, dict) and isinstance(attempt.get("llm_metrics"), dict):
                result.append(attempt["llm_metrics"])
    for attempt in (payload.get("attempts") if isinstance(payload, dict) else []) or []:
        if isinstance(attempt, dict) and isinstance(attempt.get("llm_metrics"), dict):
            result.append(attempt["llm_metrics"])
    return result


def _collect_json_list(path: Path) -> List[Dict[str, Any]]:
    payload = _read_json(path)
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if isinstance(payload, dict):
        items = payload.get("records") or payload.get("metrics") or payload.get("calls")
        if isinstance(items, list):
            return [item for item in items if isinstance(item, dict)]
    return []


def _stage_metrics(pipeline_result: Any, output_dir: Path) -> List[Dict[str, Any]]:
    result = []
    for stage in getattr(pipeline_result, "stages", []) or []:
        stats = getattr(stage, "stats", {}) or {}
        item = {
            "stage_name": str(getattr(stage, "stage_name", "") or ""),
            "started_at": getattr(stage, "started_at", None),
            "finished_at": getattr(stage, "finished_at", None),
            "duration_sec": getattr(stage, "duration_sec", None),
            "stats": _to_jsonable(stats),
        }
        if item["stage_name"] == "code_changes":
            item["steps"] = _code_change_step_metrics(output_dir)
        result.append(item)
    return result


def _code_change_step_metrics(output_dir: Path) -> List[Dict[str, Any]]:
    payload = _read_json(output_dir / "01_code_changes" / "pipeline_report.json")
    steps = payload.get("executed_steps") if isinstance(payload, dict) else []
    result = []
    for step in steps or []:
        if not isinstance(step, dict):
            continue
        result.append(
            {
                "step_name": step.get("step_name"),
                "started_at": step.get("started_at"),
                "finished_at": step.get("finished_at"),
                "duration_sec": step.get("duration_sec"),
                "success": step.get("success"),
                "stats": step.get("stats") or {},
            }
        )
    return result


def _stats_by_stage(pipeline_result: Any) -> Dict[str, Dict[str, Any]]:
    result: Dict[str, Dict[str, Any]] = {}
    for stage in getattr(pipeline_result, "stages", []) or []:
        result[str(getattr(stage, "stage_name", "") or "")] = dict(getattr(stage, "stats", {}) or {})
    return result


def _minimal_metric(metric: Dict[str, Any]) -> Dict[str, Any]:
    allowed = {
        "schema_version",
        "stage",
        "request_name",
        "provider",
        "model",
        "thinking_enabled",
        "success",
        "started_at",
        "finished_at",
        "duration_sec",
        "system_prompt_chars",
        "user_prompt_chars",
        "input_chars",
        "output_chars",
        "transport_attempt_count",
        "validation_attempt_count",
        "is_validation_retry",
        "error_type",
        "error_message",
        "raw_usage",
        *LLM_METRIC_TOKEN_FIELDS,
    }
    cleaned = {key: _to_jsonable(value) for key, value in metric.items() if key in allowed}
    for key in LLM_METRIC_TOKEN_FIELDS:
        cleaned.setdefault(key, None)
    cleaned.setdefault("schema_version", METRICS_SCHEMA_VERSION)
    cleaned.setdefault("success", True)
    cleaned.setdefault("transport_attempt_count", 1)
    cleaned.setdefault("validation_attempt_count", 1)
    cleaned.setdefault("is_validation_retry", False)
    return cleaned


def _empty_llm_aggregate() -> Dict[str, Any]:
    return {
        "call_count": 0,
        "success_count": 0,
        "failure_count": 0,
        "prompt_tokens": None,
        "completion_tokens": None,
        "reasoning_tokens": None,
        "total_tokens": None,
        "input_chars": 0,
        "output_chars": 0,
        "llm_duration_sec": 0.0,
        "validation_retry_count": 0,
        "transport_retry_count": 0,
    }


def _find_reasoning_tokens(raw_usage: Dict[str, Any]) -> Optional[int]:
    direct = _safe_int(raw_usage.get("reasoning_tokens"))
    if direct is not None:
        return direct
    for key in (
        "completion_tokens_details",
        "output_tokens_details",
        "output_token_details",
        "usage_details",
        "details",
    ):
        nested = raw_usage.get(key)
        if isinstance(nested, dict):
            found = _find_reasoning_tokens(nested)
            if found is not None:
                return found
    return None


def _safe_int(value: Any) -> Optional[int]:
    try:
        if value is None:
            return None
        return int(value)
    except (TypeError, ValueError):
        return None


def _read_json(path: Path) -> Any:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _to_jsonable(value: Any) -> Any:
    if value is None:
        return None
    if is_dataclass(value):
        return _to_jsonable(asdict(value))
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _to_jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_to_jsonable(item) for item in value]
    for method_name in ("model_dump", "dict"):
        method = getattr(value, method_name, None)
        if callable(method):
            try:
                dumped = method()
                if dumped is not value:
                    return _to_jsonable(dumped)
            except Exception:
                pass
    if hasattr(value, "__dict__"):
        try:
            return _to_jsonable(vars(value))
        except Exception:
            pass
    if isinstance(value, (str, int, float, bool)):
        return value
    return str(value)
