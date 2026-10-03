from __future__ import annotations

from typing import Any, Dict, Optional


LLM_CONTEXT_TOKEN_LIMIT = 65_536
SUPPORTED_LLM_PROVIDERS = {"qwen", "mimo", "deepseek", "siliconflow"}


def build_chat_completion_request_kwargs(
    *,
    config: Any,
    system_prompt: str,
    user_prompt: str,
    max_tokens: Optional[int] = None,
) -> Dict[str, Any]:
    provider = resolve_llm_provider(config)
    token_budget = resolve_llm_token_budget(config, max_tokens)
    request_kwargs: Dict[str, Any] = {
        "model": getattr(config, "llm_model_name", None),
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }

    if provider == "mimo":
        request_kwargs["max_completion_tokens"] = token_budget
    else:
        request_kwargs["max_tokens"] = token_budget

    temperature = _safe_float(getattr(config, "llm_temperature", None), 0.0)
    if not (provider in {"mimo", "deepseek"} and resolve_llm_enable_thinking(config)):
        request_kwargs["temperature"] = temperature
    if provider == "deepseek" and resolve_llm_enable_thinking(config):
        request_kwargs["reasoning_effort"] = str(getattr(config, "llm_reasoning_effort", "high") or "high")

    if bool(getattr(config, "llm_response_format_json", False)):
        request_kwargs["response_format"] = {"type": "json_object"}

    request_kwargs.update(build_llm_provider_extra_body(config))
    return request_kwargs


def build_llm_provider_extra_body(config: Any | None = None) -> Dict[str, Any]:
    provider = resolve_llm_provider(config)
    thinking_enabled = resolve_llm_enable_thinking(config)
    if provider == "qwen":
        return {"extra_body": {"enable_thinking": thinking_enabled}}
    if provider == "mimo":
        return {"extra_body": {"thinking": {"type": "enabled" if thinking_enabled else "disabled"}}}
    if provider == "deepseek":
        return {"extra_body": {"thinking": {"type": "enabled" if thinking_enabled else "disabled"}}}
    if provider == "siliconflow":
        return {}
    raise ValueError(f"Unsupported LLM provider: {provider}")


def resolve_llm_provider(config: Any | None = None) -> str:
    provider = str(getattr(config, "llm_provider", "qwen") if config is not None else "qwen").strip().lower()
    if not provider:
        provider = "qwen"
    if provider not in SUPPORTED_LLM_PROVIDERS:
        raise ValueError(f"Unsupported LLM provider: {provider}. Supported providers: {sorted(SUPPORTED_LLM_PROVIDERS)}")
    return provider


def resolve_llm_enable_thinking(config: Any | None = None, default: bool = False) -> bool:
    if isinstance(config, bool):
        return config
    configured = getattr(config, "llm_enable_thinking", default) if config is not None else default
    return _coerce_bool(configured)


def resolve_llm_token_budget(config: Any, max_tokens: Optional[int] = None) -> int:
    candidates = [LLM_CONTEXT_TOKEN_LIMIT]
    if max_tokens is not None:
        candidates.append(_safe_positive_int(max_tokens))
    candidates.append(_safe_positive_int(getattr(config, "llm_max_tokens", None)))
    candidates.append(_safe_positive_int(getattr(config, "llm_context_token_limit", None)))
    return max(candidates)


def _coerce_bool(value: Any) -> bool:
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"1", "true", "yes", "y", "on", "enable", "enabled"}:
            return True
        if normalized in {"0", "false", "no", "n", "off", "disable", "disabled"}:
            return False
    return bool(value)


def _safe_positive_int(value: Any) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        return 0
    return parsed if parsed > 0 else 0


def _safe_float(value: Any, default: float) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default
