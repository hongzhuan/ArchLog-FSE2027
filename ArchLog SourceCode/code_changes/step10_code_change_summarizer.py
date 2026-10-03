from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import contextmanager
import json
import logging
import os
from pathlib import Path
import random
import sys
import threading
import time
from typing import Any, Dict, List, Optional

from .constants import DEFAULT_LOGGER_NAME
from .models import (
    CodeChangeSummary,
    PipelineConfig,
    PromptsOutput,
    SelectedExemplarsOutput,
    SummariesOutput,
)

from config import LLM_API_KEY_ENV_VAR, LLM_BASE_URL
from arcrn_metrics import build_llm_call_metrics, mark_llm_metric_attempt, start_timer
from llm_provider_adapters import build_chat_completion_request_kwargs


LOGGER = logging.getLogger(DEFAULT_LOGGER_NAME)
_STEP10_PROGRESS_LOGGER_NAMES = (
    "httpx",
    "httpcore",
    "openai",
)


class _EmptyLLMResponseError(RuntimeError):
    def __init__(self, message: str, *, raw_text: Optional[str], response_debug: Optional[str]) -> None:
        super().__init__(message)
        self.raw_text = raw_text
        self.response_debug = response_debug


class _TokenBucketRateLimiter:
    """
    Simple thread-safe token bucket limiter used by Step10.
    - qps=None or qps<=0 means disabled.
    - burst controls maximum accumulated tokens.
    """

    def __init__(self, qps: Optional[float], burst: int) -> None:
        self._qps = qps if qps is not None and qps > 0 else None
        self._capacity = max(1, int(burst))
        self._tokens = float(self._capacity)
        self._last_refill = time.monotonic()
        self._lock = threading.Lock()

    def acquire(self) -> None:
        if self._qps is None:
            return

        while True:
            wait_sec = 0.0
            with self._lock:
                now = time.monotonic()
                elapsed = max(0.0, now - self._last_refill)
                self._last_refill = now
                self._tokens = min(self._capacity, self._tokens + elapsed * self._qps)

                if self._tokens >= 1.0:
                    self._tokens -= 1.0
                    return

                deficit = 1.0 - self._tokens
                wait_sec = deficit / self._qps

            if wait_sec > 0:
                time.sleep(wait_sec)


class _SingleLineProgressBar:
    """
    Render a single in-place progress line.

    The renderer pads the current line with spaces so shorter updates
    overwrite longer previous content instead of leaving artifacts behind.
    """

    def __init__(self, stream=None) -> None:
        self._stream = stream if stream is not None else sys.stdout
        self._last_text_length = 0
        self._active = False

    def update(self, *, completed: int, total: int) -> None:
        text = _format_step10_progress(completed=completed, total=total)
        padding = max(0, self._last_text_length - len(text))
        self._stream.write("\r" + text + (" " * padding))
        self._stream.flush()
        self._last_text_length = len(text)
        self._active = True

    def finish(self) -> None:
        if not self._active:
            return
        self._stream.write("\n")
        self._stream.flush()
        self._active = False
        self._last_text_length = 0


# ============================================================
# Public entry
# ============================================================

def run_code_change_summarizer(
    config: PipelineConfig,
    change_units_output,
    prompts_output: PromptsOutput,
    selected_exemplars_output: SelectedExemplarsOutput,
) -> SummariesOutput:
    """
    Generate one code change summary per change unit.

    Preferred path:
    - Use an OpenAI-compatible chat model if configured and available

    Fallback path:
    - Use a deterministic heuristic summarizer so the pipeline can still run end-to-end
    """
    prompt_by_unit_id = {p.unit_id: p for p in prompts_output.prompts}
    units = list(change_units_output.change_units)

    llm_client = _maybe_build_llm_client(config)
    max_workers = max(1, int(config.step10_concurrency))
    rate_limiter = _TokenBucketRateLimiter(
        qps=config.step10_rate_limit_qps,
        burst=config.step10_rate_limit_burst,
    )
    summaries: List[CodeChangeSummary] = []
    total_units = len(units)
    progress_enabled = bool(config.verbose)
    progress_bar = _SingleLineProgressBar() if progress_enabled else None
    checkpoint_path = _step10_checkpoint_path(config)
    cached_summaries = _load_step10_checkpoint(checkpoint_path)
    checkpoint_lock = threading.Lock()

    with _suppress_noisy_progress_loggers(enabled=progress_enabled):
        summaries_by_index: List[Optional[CodeChangeSummary]] = [
            _cached_summary_for_unit(cached_summaries, unit)
            for unit in units
        ]
        completed = sum(1 for summary in summaries_by_index if summary is not None)
        if max_workers == 1 or len(units) <= 1:
            if progress_bar is not None:
                progress_bar.update(completed=completed, total=total_units)
            for idx, unit in enumerate(units):
                if summaries_by_index[idx] is not None:
                    continue
                summary = _summarize_one_unit(
                    unit=unit,
                    config=config,
                    llm_client=llm_client,
                    rate_limiter=rate_limiter,
                    prompt_by_unit_id=prompt_by_unit_id,
                )
                summaries_by_index[idx] = summary
                _append_step10_checkpoint(checkpoint_path, summary, checkpoint_lock)
                completed += 1
                if progress_bar is not None:
                    progress_bar.update(completed=completed, total=total_units)
        else:
            LOGGER.info("Step10 running with concurrency=%d for %d change units.", max_workers, len(units))
            if progress_bar is not None:
                progress_bar.update(completed=completed, total=total_units)
            with ThreadPoolExecutor(max_workers=max_workers, thread_name_prefix="step10") as executor:
                future_to_index = {
                    executor.submit(
                        _summarize_one_unit,
                        unit=unit,
                        config=config,
                        llm_client=llm_client,
                        rate_limiter=rate_limiter,
                        prompt_by_unit_id=prompt_by_unit_id,
                    ): idx
                    for idx, unit in enumerate(units)
                    if summaries_by_index[idx] is None
                }

                for future in as_completed(future_to_index):
                    idx = future_to_index[future]
                    summary = future.result()
                    summaries_by_index[idx] = summary
                    _append_step10_checkpoint(checkpoint_path, summary, checkpoint_lock)
                    completed += 1
                    if progress_bar is not None:
                        progress_bar.update(completed=completed, total=total_units)

        summaries = [
            x for x in summaries_by_index
            if x is not None
        ]

    if progress_bar is not None:
        progress_bar.finish()

    LOGGER.info(
        "Step10 code change summarization finished: %d summaries generated.",
        len(summaries),
    )

    return SummariesOutput(summaries=summaries)


def _format_step10_progress(*, completed: int, total: int) -> str:
    if total <= 0:
        return "Step10 summarize progress: 0/0 [--------------------] 100.0%"

    ratio = min(1.0, max(0.0, completed / total))
    width = 20
    filled = int(width * ratio)
    bar = "#" * filled + "-" * (width - filled)
    return f"Step10 summarize progress: {completed}/{total} [{bar}] {ratio * 100:5.1f}%"


def _step10_checkpoint_path(config: PipelineConfig) -> Path:
    return Path(config.output_dir) / "step10_summary_checkpoint.jsonl"


def _load_step10_checkpoint(path: Path) -> Dict[str, CodeChangeSummary]:
    summaries: Dict[str, CodeChangeSummary] = {}
    if not path.exists():
        return summaries
    try:
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                text = line.strip()
                if not text:
                    continue
                try:
                    data = json.loads(text)
                    summary = CodeChangeSummary(**data)
                except Exception:
                    continue
                summaries[summary.unit_id] = summary
    except OSError:
        return {}
    if summaries:
        LOGGER.info("Step10 loaded %d cached summaries from %s.", len(summaries), path)
    return summaries


def _cached_summary_for_unit(cached_summaries: Dict[str, CodeChangeSummary], unit: Any) -> Optional[CodeChangeSummary]:
    summary = cached_summaries.get(str(getattr(unit, "unit_id", "")))
    if summary is None:
        return None
    unit_commit_id = _unit_commit_id(unit)
    if str(summary.commit_id) != str(unit_commit_id):
        return None
    return summary


def _unit_commit_id(unit: Any) -> str:
    commit = getattr(unit, "commit", None)
    if commit is not None and getattr(commit, "commit_id", None):
        return str(getattr(commit, "commit_id"))
    return str(getattr(unit, "commit_id", ""))


def _append_step10_checkpoint(path: Path, summary: CodeChangeSummary, lock: threading.Lock) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(summary.to_dict(), ensure_ascii=False)
    with lock:
        with path.open("a", encoding="utf-8") as handle:
            handle.write(line + "\n")


@contextmanager
def _suppress_noisy_progress_loggers(*, enabled: bool):
    if not enabled:
        yield
        return

    previous_levels = []
    for logger_name in _STEP10_PROGRESS_LOGGER_NAMES:
        logger = logging.getLogger(logger_name)
        previous_levels.append((logger, logger.level))
        logger.setLevel(logging.WARNING)

    try:
        yield
    finally:
        for logger, previous_level in previous_levels:
            logger.setLevel(previous_level)


def _summarize_one_unit(
    *,
    unit,
    config: PipelineConfig,
    llm_client,
    rate_limiter: _TokenBucketRateLimiter,
    prompt_by_unit_id,
    exemplar_by_unit_id=None,
) -> CodeChangeSummary:
    prompt_record = prompt_by_unit_id.get(unit.unit_id)

    if prompt_record is None:
        return _build_summary_record(
            unit=unit,
            predicted_category=unit.inferred_change_category,
            summary_text=_fallback_summary_without_prompt(unit),
            raw_response=None,
            llm_failure_reason="prompt_record_missing",
            llm_failure_raw_response=None,
            used_exemplar_ids=[],
            prompt_record=None,
        )

    llm_failure_reason = None
    llm_failure_raw_response = None

    if llm_client is not None:
        try:
            summary_text, raw_response, llm_metrics = _generate_summary_with_llm_with_retry(
                config=config,
                llm_client=llm_client,
                prompt_record=prompt_record,
                rate_limiter=rate_limiter,
                unit_id=unit.unit_id,
            )
        except Exception as exc:
            if getattr(config, "debug_fail_fast_on_llm_error", False) or getattr(config, "fail_fast", False):
                raise
            LOGGER.warning(
                "LLM generation failed for unit %s, fallback will be used. Error: %s",
                unit.unit_id,
                exc,
            )
            summary_text = _fallback_summary(unit, prompt_record)
            raw_response = None
            llm_metrics = {}
            llm_failure_reason = str(exc)
            llm_failure_raw_response = _extract_failure_raw_response(exc)
    else:
        summary_text = _fallback_summary(unit, prompt_record)
        raw_response = None
        llm_metrics = {}

    predicted_category = unit.inferred_change_category
    return _build_summary_record(
        unit=unit,
        predicted_category=predicted_category,
        summary_text=summary_text,
        raw_response=raw_response,
        llm_failure_reason=llm_failure_reason,
        llm_failure_raw_response=llm_failure_raw_response,
        llm_metrics=llm_metrics,
        used_exemplar_ids=[],
        prompt_record=prompt_record,
    )


def _build_summary_record(
    *,
    unit,
    predicted_category: str,
    summary_text: str,
    raw_response: Optional[str],
    llm_failure_reason: Optional[str],
    llm_failure_raw_response: Optional[str],
    used_exemplar_ids: List[str],
    llm_metrics: Optional[Dict[str, Any]] = None,
    prompt_record=None,
) -> CodeChangeSummary:
    evidence = getattr(unit, "evidence", {}) or {}
    commit_url, pull_requests = _traceability_from_prompt_record(prompt_record)
    return CodeChangeSummary(
        unit_id=unit.unit_id,
        commit_id=unit.commit.commit_id,
        predicted_category=predicted_category,
        summary=summary_text,
        raw_response=raw_response,
        llm_failure_reason=llm_failure_reason,
        llm_failure_raw_response=llm_failure_raw_response,
        llm_metrics=dict(llm_metrics or {}),
        used_exemplar_ids=used_exemplar_ids,
        evidence_links={
            "method_uids": [m.method_uid for m in unit.changed_methods],
            "commit_ids": [unit.commit.commit_id],
            "hunk_ids": [str(item) for item in evidence.get("hunk_ids", [])],
            "changed_files": [str(item) for item in evidence.get("files", [])],
        },
        commit_url=commit_url,
        pull_requests=pull_requests,
    )


def _traceability_from_prompt_record(prompt_record) -> tuple[Optional[str], List[Dict[str, object]]]:
    payload = getattr(prompt_record, "payload", None)
    if payload is None:
        return None, []
    commit_url = str(getattr(payload, "commit_url", "") or "").strip() or None
    raw_pull_requests = getattr(payload, "pull_requests", [])
    pull_requests: List[Dict[str, object]] = []
    seen = set()
    if isinstance(raw_pull_requests, list):
        for raw in raw_pull_requests:
            if not isinstance(raw, dict):
                continue
            pr_url = str(raw.get("url") or "").strip()
            try:
                pr_number = int(raw.get("number"))
            except (TypeError, ValueError):
                continue
            key = (pr_number, pr_url)
            if pr_number > 0 and pr_url and key not in seen:
                pull_requests.append({"number": pr_number, "url": pr_url})
                seen.add(key)
    if pull_requests:
        return commit_url, pull_requests
    pr_url = str(getattr(payload, "pr_url", "") or "").strip()
    pr_number = getattr(payload, "pr_number", None)
    if not pr_url or not pr_number:
        return commit_url, []
    return commit_url, [{"number": int(pr_number), "url": pr_url}]


# ============================================================
# LLM client setup
# ============================================================

def _maybe_build_llm_client(config: PipelineConfig):
    """
    Build an OpenAI-compatible client if possible.

    Requirements:
    - config.llm_model_name is set
    - config.llm_api_key_env_var is set and its env value exists
    - openai package is installed

    Optional:
    - config.llm_base_url for OpenAI-compatible providers
    """
    if not config.llm_model_name:
        LOGGER.info("No llm_model_name configured. Step10 will use fallback summarization.")
        return None

    api_key_env_var = (config.llm_api_key_env_var or LLM_API_KEY_ENV_VAR).strip()
    if not api_key_env_var:
        api_key_env_var = LLM_API_KEY_ENV_VAR

    api_key = os.getenv(api_key_env_var)
    if not api_key:
        LOGGER.info(
            "Environment variable %s is not set. Step10 will use fallback summarization.",
            api_key_env_var,
        )
        return None

    try:
        from openai import OpenAI
    except Exception:
        LOGGER.info("openai package is not available. Step10 will use fallback summarization.")
        return None

    timeout = float(getattr(config, "llm_request_timeout_sec", 180.0) or 180.0)
    base_url = config.llm_base_url or LLM_BASE_URL
    if base_url:
        LOGGER.info("Building OpenAI-compatible client with base_url from config.")
        return OpenAI(api_key=api_key, base_url=base_url, timeout=timeout)

    LOGGER.info("Building default OpenAI client.")
    return OpenAI(api_key=api_key, timeout=timeout)


# ============================================================
# LLM path
# ============================================================

def _generate_summary_with_llm(
    config: PipelineConfig,
    llm_client,
    prompt_record,
    rate_limiter: Optional[_TokenBucketRateLimiter] = None,
    request_name: str = "step10:unknown",
) -> tuple[str, str, Dict[str, Any]]:
    system_prompt = prompt_record.system_prompt
    user_prompt = prompt_record.user_prompt

    if rate_limiter is not None:
        rate_limiter.acquire()

    started_at, started_perf = start_timer()
    request_kwargs = build_chat_completion_request_kwargs(
        config=config,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
    )
    response = None
    try:
        response = llm_client.chat.completions.create(**request_kwargs)
        response_debug = _serialize_llm_response_debug(response)
        raw_text = _extract_response_text(response)
        summary_text = _postprocess_summary_text(raw_text)

        if not summary_text:
            raise _EmptyLLMResponseError(
                "LLM returned empty summary.",
                raw_text=raw_text,
                response_debug=response_debug,
            )

        llm_metrics = build_llm_call_metrics(
            stage="step10.code_change_summary",
            request_name=request_name,
            config=config,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            raw_response=raw_text,
            response=response,
            success=True,
            started_at=started_at,
            started_perf=started_perf,
        )
        return summary_text, raw_text, llm_metrics
    except Exception as exc:
        raw_text = getattr(exc, "raw_text", "") if isinstance(exc, _EmptyLLMResponseError) else ""
        llm_metrics = build_llm_call_metrics(
            stage="step10.code_change_summary",
            request_name=request_name,
            config=config,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            raw_response=raw_text,
            response=response,
            success=False,
            started_at=started_at,
            started_perf=started_perf,
            error_type=type(exc).__name__,
            error_message=str(exc),
        )
        setattr(exc, "llm_metrics", llm_metrics)
        raise


def _generate_summary_with_llm_with_retry(
    *,
    config: PipelineConfig,
    llm_client,
    prompt_record,
    rate_limiter: Optional[_TokenBucketRateLimiter],
    unit_id: str,
) -> tuple[str, str, Dict[str, Any]]:
    max_attempts = max(1, int(config.step10_retry_max_attempts))
    base_delay = max(0.0, float(config.step10_retry_base_delay_sec))
    max_delay = max(base_delay, float(config.step10_retry_max_delay_sec))
    jitter_ratio = min(1.0, max(0.0, float(config.step10_retry_jitter_ratio)))

    last_error: Optional[Exception] = None
    last_attempt_count = 0

    for attempt in range(1, max_attempts + 1):
        last_attempt_count = attempt
        try:
            summary_text, raw_text, llm_metrics = _generate_summary_with_llm(
                config=config,
                llm_client=llm_client,
                prompt_record=prompt_record,
                rate_limiter=rate_limiter,
                request_name=f"step10:{unit_id}",
            )
            return summary_text, raw_text, mark_llm_metric_attempt(llm_metrics, transport_attempt_count=attempt)
        except Exception as exc:
            last_error = exc
            if attempt >= max_attempts or not _is_retryable_llm_error(exc):
                break

            retry_after_sec = _extract_retry_after_seconds(exc)
            if retry_after_sec is not None and retry_after_sec > 0:
                sleep_sec = min(max_delay, retry_after_sec)
            else:
                sleep_sec = min(max_delay, base_delay * (2 ** (attempt - 1)))

            if sleep_sec > 0 and jitter_ratio > 0:
                jitter = sleep_sec * jitter_ratio * random.random()
                sleep_sec = min(max_delay, sleep_sec + jitter)

            LOGGER.warning(
                "Step10 retrying unit %s after LLM error (attempt %d/%d): %s; sleep %.2fs",
                unit_id,
                attempt,
                max_attempts,
                exc,
                sleep_sec,
            )
            if sleep_sec > 0:
                time.sleep(sleep_sec)

    if last_error is None:
        raise RuntimeError("LLM summary generation failed without explicit exception.")
    failure_metrics = getattr(last_error, "llm_metrics", None)
    if isinstance(failure_metrics, dict):
        setattr(
            last_error,
            "llm_metrics",
            mark_llm_metric_attempt(
                failure_metrics,
                transport_attempt_count=last_attempt_count,
                success=False,
                error_type=type(last_error).__name__,
                error_message=str(last_error),
            ),
        )
    raise last_error


def _is_retryable_llm_error(exc: Exception) -> bool:
    if isinstance(exc, _EmptyLLMResponseError):
        return True

    text = str(exc).lower()
    if any(k in text for k in ("429", "rate limit", "too many requests", "timeout", "timed out")):
        return True
    if any(k in text for k in (" 500", " 502", " 503", " 504", "server error", "service unavailable")):
        return True
    if any(k in text for k in ("empty summary", "empty response")):
        return True

    status_code = getattr(exc, "status_code", None)
    if isinstance(status_code, int):
        if status_code == 429 or 500 <= status_code <= 599:
            return True

    response = getattr(exc, "response", None)
    if response is not None:
        resp_status = getattr(response, "status_code", None)
        if isinstance(resp_status, int) and (resp_status == 429 or 500 <= resp_status <= 599):
            return True

    return False


def _extract_retry_after_seconds(exc: Exception) -> Optional[float]:
    response = getattr(exc, "response", None)
    if response is None:
        return None

    headers = getattr(response, "headers", None)
    if headers is None:
        return None

    retry_after_value = None
    try:
        retry_after_value = headers.get("retry-after") or headers.get("Retry-After")
    except Exception:
        return None

    if retry_after_value is None:
        return None

    try:
        parsed = float(str(retry_after_value).strip())
    except Exception:
        return None

    if parsed <= 0:
        return None
    return parsed


def _extract_failure_raw_response(exc: Exception) -> Optional[str]:
    response_debug = getattr(exc, "response_debug", None)
    raw_text = getattr(exc, "raw_text", None)

    if response_debug:
        return response_debug
    if raw_text is not None:
        return raw_text
    return None


def _extract_response_text(response) -> str:
    try:
        content = response.choices[0].message.content
        if content is None:
            return ""
        if isinstance(content, list):
            parts = []
            for item in content:
                if isinstance(item, dict):
                    text_value = item.get("text")
                    if text_value:
                        parts.append(str(text_value))
                    continue
                text_value = getattr(item, "text", None)
                if text_value:
                    parts.append(str(text_value))
            return "\n".join(parts).strip()
        return str(content).strip()
    except Exception as exc:
        raise RuntimeError(f"Failed to extract text from LLM response: {exc}") from exc


def _serialize_llm_response_debug(response) -> Optional[str]:
    try:
        model_dump_json = getattr(response, "model_dump_json", None)
        if callable(model_dump_json):
            return model_dump_json(indent=2)
    except Exception:
        pass

    try:
        model_dump = getattr(response, "model_dump", None)
        if callable(model_dump):
            return json.dumps(model_dump(), ensure_ascii=False, indent=2)
    except Exception:
        pass

    try:
        return repr(response)
    except Exception:
        return None


def _postprocess_summary_text(text: str) -> str:
    return text


# ============================================================
# Fallback path
# ============================================================

def _fallback_summary(unit, prompt_record) -> str:
    """
    Deterministic fallback summary that uses:
    - commit subject
    - inferred category
    - changed methods
    - diff evidence
    """
    subject = (unit.commit.subject or "").strip()
    category = unit.inferred_change_category

    method_names = _collect_method_names(unit)
    diff_hints = _collect_diff_hints_from_prompt(prompt_record)

    base = []

    if subject:
        base.append(subject.rstrip("."))

    if not base:
        base.append(_fallback_category_phrase(category))

    if method_names:
        if len(method_names) == 1:
            base.append(f"It primarily affects `{method_names[0]}`.")
        elif len(method_names) <= 3:
            joined = ", ".join(f"`{x}`" for x in method_names)
            base.append(f"It touches {joined}.")
        else:
            joined = ", ".join(f"`{x}`" for x in method_names[:3])
            base.append(f"It touches {joined}, and other related methods.")

    if diff_hints:
        base.append(diff_hints)

    return " ".join(base).strip()


def _fallback_summary_without_prompt(unit) -> str:
    subject = (unit.commit.subject or "").strip()
    if subject:
        return subject
    return _fallback_category_phrase(unit.inferred_change_category)


def _fallback_category_phrase(category: str) -> str:
    mapping = {
        "feature": "This change introduces a new capability or expands existing functionality.",
        "bugfix": "This change fixes a defect in the current implementation.",
        "refactoring": "This change refactors existing code without necessarily changing user-visible behavior.",
        "performance": "This change improves performance-related behavior.",
        "security": "This change improves security-related handling.",
        "maintenance": "This change performs maintenance-oriented updates to the codebase.",
        "unknown": "This change updates the codebase.",
    }
    return mapping.get(category, "This change updates the codebase.")


def _collect_method_names(unit) -> List[str]:
    names: List[str] = []
    seen = set()

    for method in unit.changed_methods:
        identity = method.new_identity or method.old_identity
        if identity is None:
            continue
        qname = identity.qualified_name
        if not qname or qname in seen:
            continue
        seen.add(qname)
        names.append(qname)

    return names


def _collect_diff_hints_from_prompt(prompt_record) -> str:
    payload = prompt_record.payload
    change_type_counter: Dict[str, int] = {}
    diff_line_count = 0

    for pair in payload.changed_statements:
        change_type = pair.get("change_type") or "unknown"
        change_type_counter[change_type] = change_type_counter.get(change_type, 0) + 1

        for matched_hunk in pair.get("matched_hunks", []):
            diff_line_count += len(matched_hunk.get("matched_diff_text", []))

    hints = []

    if change_type_counter:
        ordered = sorted(change_type_counter.items(), key=lambda x: x[0])
        type_text = ", ".join(f"{k}={v}" for k, v in ordered)
        if payload.evidence_granularity != "method_level":
            hints.append(f"This summary is based on file/hunk-level diff evidence ({type_text}).")
        else:
            hints.append(f"Change composition: {type_text}.")

    if diff_line_count > 0:
        if payload.evidence_granularity != "method_level":
            hints.append(f"The summary is supported by {diff_line_count} lines of diff evidence.")
        else:
            hints.append(f"The summary is supported by {diff_line_count} lines of aligned diff evidence.")

    return " ".join(hints).strip()
