from __future__ import annotations

import json
import logging
import os
import random
import sys
import threading
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Dict, Optional

from config import LLM_API_KEY_ENV_VAR, LLM_BASE_URL
from arcrn_metrics import build_llm_call_metrics, mark_llm_metric_attempt, start_timer
from arcrn_progress_logger import write_progress_event
from llm_provider_adapters import build_chat_completion_request_kwargs


LOGGER = logging.getLogger(__name__)
_PROGRESS_LOGGER_NAMES = (
    "httpx",
    "httpcore",
    "openai",
)


class TokenBucketRateLimiter:
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


class SingleLineProgressBar:
    """Render a named progress counter in place while an LLM stage is running."""

    def __init__(self, *, label: str, stream=None) -> None:
        self._label = label
        self._stream = stream if stream is not None else sys.stdout
        self._last_text_length = 0
        self._active = False

    def update(self, *, completed: int, total: int, label: str | None = None) -> None:
        if label is not None:
            self._label = label
        text = format_llm_progress(label=self._label, completed=completed, total=total)
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
        self._last_text_length = 0
        self._active = False


def progress_bar_for(config, label: str) -> Optional[SingleLineProgressBar]:
    if not bool(getattr(config, "verbose", False)):
        return None
    return SingleLineProgressBar(label=label)


def format_llm_progress(*, label: str, completed: int, total: int) -> str:
    if total <= 0:
        return f"{label}: 0/0 [--------------------] 100.0%"
    ratio = min(1.0, max(0.0, completed / total))
    width = 20
    filled = int(width * ratio)
    bar = "#" * filled + "-" * (width - filled)
    return f"{label}: {completed}/{total} [{bar}] {ratio * 100:5.1f}%"


@contextmanager
def suppress_noisy_llm_loggers(*, enabled: bool):
    if not enabled:
        yield
        return

    previous_levels = []
    for logger_name in _PROGRESS_LOGGER_NAMES:
        logger = logging.getLogger(logger_name)
        previous_levels.append((logger, logger.level))
        logger.setLevel(logging.WARNING)
    try:
        yield
    finally:
        for logger, previous_level in previous_levels:
            logger.setLevel(previous_level)


def maybe_build_llm_client(config) -> Any:
    if not getattr(config, "llm_model_name", None):
        LOGGER.info("No llm_model_name configured. ArchLog stages will use fallback generation.")
        return None

    api_key_env_var = str(getattr(config, "llm_api_key_env_var", LLM_API_KEY_ENV_VAR) or LLM_API_KEY_ENV_VAR).strip()
    api_key = os.getenv(api_key_env_var)
    if not api_key:
        LOGGER.info("Environment variable %s is not set. ArchLog stages will use fallback generation.", api_key_env_var)
        return None

    try:
        from openai import OpenAI
    except Exception:
        LOGGER.info("openai package is not available. ArchLog stages will use fallback generation.")
        return None

    timeout = float(getattr(config, "llm_request_timeout_sec", 180.0) or 180.0)
    base_url = getattr(config, "llm_base_url", None) or LLM_BASE_URL
    if base_url:
        LOGGER.info("Building OpenAI-compatible client for ArchLog stages with base_url from config.")
        return OpenAI(api_key=api_key, base_url=base_url, timeout=timeout)

    LOGGER.info("Building default OpenAI client for ArchLog stages.")
    return OpenAI(api_key=api_key, timeout=timeout)


def generate_chat_completion_with_retry(
    *,
    config,
    llm_client,
    system_prompt: str,
    user_prompt: str,
    request_name: str,
    rate_limiter: Optional[TokenBucketRateLimiter] = None,
    max_tokens: Optional[int] = None,
) -> tuple[str, Dict[str, Any]]:
    max_attempts = max(1, int(getattr(config, "step10_retry_max_attempts", 1)))
    base_delay = max(0.0, float(getattr(config, "step10_retry_base_delay_sec", 0.0)))
    max_delay = max(base_delay, float(getattr(config, "step10_retry_max_delay_sec", base_delay)))
    jitter_ratio = min(1.0, max(0.0, float(getattr(config, "step10_retry_jitter_ratio", 0.0))))

    last_error: Optional[Exception] = None
    last_attempt_count = 0

    for attempt in range(1, max_attempts + 1):
        last_attempt_count = attempt
        stage_name = _stage_from_request_name(request_name)
        write_progress_event(
            config,
            "llm_request_attempt_start",
            stage=stage_name,
            request_name=request_name,
            attempt=attempt,
            max_attempts=max_attempts,
            system_prompt_chars=len(system_prompt or ""),
            user_prompt_chars=len(user_prompt or ""),
            input_chars=len(system_prompt or "") + len(user_prompt or ""),
        )
        try:
            raw_text, metrics = _generate_chat_completion(
                config=config,
                llm_client=llm_client,
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                rate_limiter=rate_limiter,
                max_tokens=max_tokens,
                request_name=request_name,
            )
            metrics = mark_llm_metric_attempt(metrics, transport_attempt_count=attempt)
            write_progress_event(
                config,
                "llm_request_attempt_success",
                stage=stage_name,
                request_name=request_name,
                attempt=attempt,
                max_attempts=max_attempts,
                duration_sec=metrics.get("duration_sec"),
                output_chars=metrics.get("output_chars"),
                prompt_tokens=metrics.get("prompt_tokens"),
                completion_tokens=metrics.get("completion_tokens"),
                total_tokens=metrics.get("total_tokens"),
            )
            return raw_text, metrics
        except Exception as exc:
            last_error = exc
            failure_metrics = getattr(exc, "llm_metrics", None)
            write_progress_event(
                config,
                "llm_request_attempt_failure",
                stage=stage_name,
                request_name=request_name,
                attempt=attempt,
                max_attempts=max_attempts,
                duration_sec=(failure_metrics or {}).get("duration_sec") if isinstance(failure_metrics, dict) else None,
                error_type=type(exc).__name__,
                error_message=str(exc),
            )
            if attempt >= max_attempts or not _is_retryable_llm_error(exc):
                break

            retry_after_sec = _extract_retry_after_seconds(exc)
            if retry_after_sec is not None and retry_after_sec > 0:
                sleep_sec = min(max_delay, retry_after_sec)
            else:
                sleep_sec = min(max_delay, base_delay * (2 ** (attempt - 1)))

            if sleep_sec > 0 and jitter_ratio > 0:
                sleep_sec = min(max_delay, sleep_sec + sleep_sec * jitter_ratio * random.random())

            LOGGER.warning(
                "ArchLog LLM retry for %s after error (attempt %d/%d): %s; sleep %.2fs",
                request_name,
                attempt,
                max_attempts,
                exc,
                sleep_sec,
            )
            write_progress_event(
                config,
                "llm_request_retry_sleep",
                stage=stage_name,
                request_name=request_name,
                attempt=attempt,
                max_attempts=max_attempts,
                sleep_sec=round(float(sleep_sec), 6),
                error_type=type(exc).__name__,
                error_message=str(exc),
            )
            if sleep_sec > 0:
                time.sleep(sleep_sec)

    if last_error is None:
        raise RuntimeError(f"LLM generation failed for {request_name} without explicit exception.")
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


def llm_output_validation_max_retries(config) -> int:
    """Return retries for completed LLM responses that fail content validation."""
    if config is None:
        return 0
    try:
        return max(0, int(getattr(config, "llm_output_validation_max_retries", 1) or 0))
    except Exception:
        return 1


def load_prompt_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def resolve_prompt_path(config, attr_name: str, default_path: Path) -> Path:
    configured = getattr(config, attr_name, None)
    if not configured:
        return default_path
    return Path(configured)


def render_prompt_template(template_text: str, values: Dict[str, str]) -> str:
    rendered = template_text
    for key, value in values.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)
    return rendered


def parse_json_response(raw_text: str) -> Dict[str, Any]:
    candidate = _strip_markdown_fences(raw_text).strip()
    if not candidate:
        raise ValueError("LLM returned empty response text.")

    try:
        parsed = json.loads(candidate)
    except Exception:
        start = candidate.find("{")
        end = candidate.rfind("}")
        if start < 0 or end <= start:
            raise
        parsed = json.loads(candidate[start : end + 1])

    if not isinstance(parsed, dict):
        raise ValueError("LLM response must be a JSON object.")
    return parsed


def parse_json_response_strict(raw_text: str) -> Dict[str, Any]:
    """Parse a JSON object after removing only a complete standard JSON fence."""
    candidate = _normalize_json_response_envelope_strict(raw_text)
    if not candidate:
        raise ValueError("LLM returned empty response text.")

    parsed = json.loads(candidate)
    if not isinstance(parsed, dict):
        raise ValueError("LLM response must be a JSON object.")
    return parsed


def to_pretty_json(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2)


def to_compact_json(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))


def _generate_chat_completion(
    *,
    config,
    llm_client,
    system_prompt: str,
    user_prompt: str,
    rate_limiter: Optional[TokenBucketRateLimiter],
    max_tokens: Optional[int],
    request_name: str,
) -> tuple[str, Dict[str, Any]]:
    if rate_limiter is not None:
        rate_limiter.acquire()

    started_at, started_perf = start_timer()
    request_kwargs = build_chat_completion_request_kwargs(
        config=config,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        max_tokens=max_tokens,
    )
    response = None
    try:
        response = llm_client.chat.completions.create(**request_kwargs)
        raw_text = _extract_response_text(response)
        if not raw_text:
            raise RuntimeError("LLM returned empty response.")
        metrics = build_llm_call_metrics(
            stage=_stage_from_request_name(request_name),
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
        return raw_text, metrics
    except Exception as exc:
        metrics = build_llm_call_metrics(
            stage=_stage_from_request_name(request_name),
            request_name=request_name,
            config=config,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            raw_response="",
            response=response,
            success=False,
            started_at=started_at,
            started_perf=started_perf,
            error_type=type(exc).__name__,
            error_message=str(exc),
        )
        setattr(exc, "llm_metrics", metrics)
        raise


def _stage_from_request_name(request_name: str) -> str:
    text = str(request_name or "")
    if not text:
        return "unknown"
    if ":validation_retry" in text:
        text = text.split(":validation_retry", 1)[0]
    if ":attempt" in text:
        text = text.split(":attempt", 1)[0]
    parts = text.split(":")
    if len(parts) >= 2 and parts[0] == "phase2":
        return f"phase2.{parts[1]}" if parts[1] else "phase2"
    if parts[0].startswith("phase"):
        return parts[0]
    return parts[0]


def _extract_response_text(response: Any) -> str:
    try:
        return response.choices[0].message.content.strip()
    except Exception as exc:
        raise RuntimeError(f"Failed to extract text from LLM response: {exc}") from exc


def _is_retryable_llm_error(exc: Exception) -> bool:
    text = str(exc).lower()
    if any(keyword in text for keyword in ("429", "rate limit", "too many requests", "timeout", "timed out")):
        return True
    if any(keyword in text for keyword in (" 500", " 502", " 503", " 504", "server error", "service unavailable")):
        return True

    status_code = getattr(exc, "status_code", None)
    if isinstance(status_code, int) and (status_code == 429 or 500 <= status_code <= 599):
        return True

    response = getattr(exc, "response", None)
    if response is not None:
        response_status = getattr(response, "status_code", None)
        if isinstance(response_status, int) and (response_status == 429 or 500 <= response_status <= 599):
            return True

    return False


def _extract_retry_after_seconds(exc: Exception) -> Optional[float]:
    response = getattr(exc, "response", None)
    if response is None:
        return None

    headers = getattr(response, "headers", None)
    if headers is None:
        return None

    try:
        retry_after_value = headers.get("retry-after") or headers.get("Retry-After")
    except Exception:
        return None

    if retry_after_value is None:
        return None

    try:
        retry_after = float(str(retry_after_value).strip())
    except Exception:
        return None
    return retry_after if retry_after > 0 else None


def _strip_markdown_fences(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("```"):
        lines = stripped.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        return "\n".join(lines).strip()
    return stripped


def _normalize_json_response_envelope_strict(raw_text: str) -> str:
    text = (raw_text or "").strip()
    if text.startswith("\ufeff"):
        text = text[1:].strip()
    if not text.startswith("```"):
        return text

    lines = text.splitlines()
    opening_fence = lines[0].strip().lower() if lines else ""
    if opening_fence not in {"```", "```json"}:
        return text
    if len(lines) < 3 or lines[-1].strip() != "```":
        return text

    content = "\n".join(lines[1:-1]).strip()
    if content.startswith("\ufeff"):
        content = content[1:].strip()
    return content
