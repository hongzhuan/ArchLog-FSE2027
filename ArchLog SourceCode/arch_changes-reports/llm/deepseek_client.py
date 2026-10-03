"""LLM helpers for architecture-diff summaries."""

from __future__ import annotations

import os
import json
import sys
from pathlib import Path
from typing import Any, Dict, Optional

from openai import OpenAI

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config import (  # noqa: E402
    LLM_API_KEY_ENV_VAR,
    LLM_BASE_URL,
    LLM_MAX_TOKENS,
    LLM_MODEL_NAME,
    LLM_TEMPERATURE,
    build_llm_thinking_extra_body,
)

DEFAULT_MODEL = LLM_MODEL_NAME
LLM_CONTEXT_TOKEN_LIMIT = 65_536

SYSTEM_PROMPT_STRICT = """You are an architecture-change summarization assistant.
Return concise English Markdown grounded only in the provided architecture-diff IR.
Do not invent modules, files, or behavioral impact beyond the input evidence."""


def _get_client(api_key_env: str = LLM_API_KEY_ENV_VAR) -> OpenAI:
    api_key = os.environ.get(api_key_env)
    if not api_key:
        raise RuntimeError(
            f"Missing environment variable {api_key_env}. "
            f"Please set it before running LLM summary."
        )
    return OpenAI(api_key=api_key, base_url=LLM_BASE_URL)


def generate_markdown_from_ir(
        ir_payload: Dict[str, Any],
        model: str = DEFAULT_MODEL,
        system_prompt: str = SYSTEM_PROMPT_STRICT,
        api_key_env: str = LLM_API_KEY_ENV_VAR,
        temperature: float = LLM_TEMPERATURE,
        max_tokens: int = LLM_MAX_TOKENS,
) -> str:
    """Generate a Markdown summary from an architecture-diff IR payload."""
    client = _get_client(api_key_env=api_key_env)

    user_prompt = (
        "Summarize the following architecture-diff IR in concise English Markdown. "
        "Highlight module/component changes, quality warnings, and concrete evidence. "
        "Use only the JSON payload below:\n"
        f"{json.dumps(ir_payload, ensure_ascii=False, indent=2)}"
    )

    request_kwargs = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "stream": False,
        "temperature": temperature,
        "max_tokens": max(LLM_CONTEXT_TOKEN_LIMIT, int(max_tokens or 0)),
    }
    request_kwargs.update(build_llm_thinking_extra_body())
    resp = client.chat.completions.create(**request_kwargs)
    return resp.choices[0].message.content or ""


CHANGE_SUMMARY_SYSTEM_PROMPT_EN = """You summarize one architecture change event.
Return one concise English sentence grounded only in the provided JSON."""

def generate_change_summary_structured(
    repo: str,
    version_a: str,
    version_b: str,
    change_type: str,
    module_name: str,
    file_count: int,
    semantics_code: Dict[str, Any],
    model: str = DEFAULT_MODEL,
    api_key_env: str = LLM_API_KEY_ENV_VAR,
    temperature: float = LLM_TEMPERATURE,
    max_tokens: int = LLM_MAX_TOKENS,
) -> str:
    """Generate a concise English summary for one structured architecture change."""
    client = _get_client(api_key_env=api_key_env)

    payload = {
        "repo": repo,
        "version_a": version_a,
        "version_b": version_b,
        "change": {
            "type": change_type,
            "module_name": module_name,
            "file_count": file_count,
            "semantics_code": semantics_code or {"added_files": [], "removed_files": []},
        },
    }

    user_prompt = (
        "Summarize this architecture change event in one concise English sentence. "
        "Do not invent impact beyond the JSON evidence:\n"
        f"{json.dumps(payload, ensure_ascii=False, indent=2)}"
    )

    request_kwargs = {
        "model": model,
        "messages": [
            {"role": "system", "content": CHANGE_SUMMARY_SYSTEM_PROMPT_EN},
            {"role": "user", "content": user_prompt},
        ],
        "stream": False,
        "temperature": temperature,
        "max_tokens": max(LLM_CONTEXT_TOKEN_LIMIT, int(max_tokens or 0)),
    }
    request_kwargs.update(build_llm_thinking_extra_body())
    resp = client.chat.completions.create(**request_kwargs)

    text = resp.choices[0].message.content or ""
    return text



def main() -> None:
    """Run a small local demo for the LLM architecture-diff summarizer."""
    demo_ir = {
        "meta": {"version_a": "vA", "version_b": "vB"},
        "quality": {
            "stable_file_universe": True,
            "module_count_delta_large": True,
            "notes": ["Module count changes significantly; interpret with caution."],
        },
        "entities": {"files": {"count_a": 10, "count_b": 10, "added": [], "removed": []}},
        "changes": [
            {
                "id": "CHG-0001",
                "type": "file_reassigned",
                "confidence": 0.9,
                "summary": "File src/a.c reassigned from module X#1 to Y#1.",
                "detail": {"file": "src/a.c", "from_module_uid": "X#1", "to_module_uid": "Y#1"},
                "evidence": [{"kind": "NamedClusters", "ref": "file:src/a.c", "note": "ownership differs"}],
            },
            {
                "id": "CHG-0002",
                "type": "quality_warning",
                "confidence": 1.0,
                "summary": "Module count changes significantly between versions; interpret with caution.",
                "detail": {"flag": "module_count_delta_large"},
                "evidence": [{"kind": "Derived", "ref": "quality:module_count_delta_large", "note": ""}],
            },
        ],
    }

    md = generate_markdown_from_ir(demo_ir)
    print(md)


if __name__ == "__main__":
    main()
