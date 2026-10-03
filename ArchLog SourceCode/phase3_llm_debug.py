from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional


def phase3_debug_fail_fast(config) -> bool:
    if config is None:
        return False
    return bool(
        getattr(
            config,
            "debug_fail_fast_on_llm_error",
            getattr(config, "phase3_debug_fail_fast", True),
        )
    )


def save_phase3_llm_failure(
    *,
    output_dir: Path,
    stage: str,
    batch_or_bucket_or_slot: str,
    error_type: str,
    error_message: str,
    exception: Optional[BaseException] = None,
    prompt_template_path: str = "",
    rendered_prompt: str = "",
    raw_llm_response: str = "",
    cleaned_response_if_any: str = "",
    parsed_json_if_any: Any = None,
    input_summary: Optional[Dict[str, Any]] = None,
    input_payload: Optional[Dict[str, Any]] = None,
    validation_attempts: Optional[list[Dict[str, Any]]] = None,
) -> Path:
    failure_dir = output_dir / "phase3_llm_failures"
    failure_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    safe_stage = _safe_name(stage)
    safe_context = _safe_name(batch_or_bucket_or_slot or "unknown")
    path = failure_dir / f"{timestamp}_{safe_stage}_{safe_context}_failure.json"
    payload = {
        "stage": stage,
        "batch_or_bucket_or_slot": batch_or_bucket_or_slot,
        "error_type": error_type,
        "error_message": error_message,
        "exception_repr": repr(exception) if exception is not None else "",
        "prompt_template_path": prompt_template_path,
        "rendered_prompt": rendered_prompt,
        "raw_llm_response": raw_llm_response,
        "cleaned_response_if_any": cleaned_response_if_any,
        "parsed_json_if_any": parsed_json_if_any if parsed_json_if_any is not None else {},
        "input_summary": input_summary or {},
        "input_payload": input_payload or {},
        "validation_attempts": validation_attempts or [],
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def raise_phase3_llm_failure(
    *,
    output_dir: Path,
    stage: str,
    batch_or_bucket_or_slot: str,
    error_type: str,
    error_message: str,
    exception: Optional[BaseException] = None,
    prompt_template_path: str = "",
    rendered_prompt: str = "",
    raw_llm_response: str = "",
    cleaned_response_if_any: str = "",
    parsed_json_if_any: Any = None,
    input_summary: Optional[Dict[str, Any]] = None,
    input_payload: Optional[Dict[str, Any]] = None,
    validation_attempts: Optional[list[Dict[str, Any]]] = None,
) -> None:
    path = save_phase3_llm_failure(
        output_dir=output_dir,
        stage=stage,
        batch_or_bucket_or_slot=batch_or_bucket_or_slot,
        error_type=error_type,
        error_message=error_message,
        exception=exception,
        prompt_template_path=prompt_template_path,
        rendered_prompt=rendered_prompt,
        raw_llm_response=raw_llm_response,
        cleaned_response_if_any=cleaned_response_if_any,
        parsed_json_if_any=parsed_json_if_any,
        input_summary=input_summary,
        input_payload=input_payload,
        validation_attempts=validation_attempts,
    )
    request_failed = str(error_type or "").startswith("llm_")
    if request_failed:
        heading = "Phase 3 LLM request failed."
        message = f"Phase 3 LLM request failed at {stage}; failure file: {path}"
    else:
        heading = "Phase 3 LLM output validation failed."
        message = f"Phase 3 LLM output validation failed at {stage}; failure file: {path}"
    print(
        f"{heading}\n"
        f"Stage: {stage}\n"
        f"Batch: {batch_or_bucket_or_slot}\n"
        f"Failure file: {path}"
    )
    raise RuntimeError(message)


def phase3_failure_output_dir(config, fallback: Optional[Path] = None) -> Path:
    configured = getattr(config, "output_dir", None) if config is not None else None
    if configured:
        return Path(configured)
    if fallback is not None:
        return Path(fallback)
    return Path.cwd()


def _safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", str(value or "unknown")).strip("_") or "unknown"
