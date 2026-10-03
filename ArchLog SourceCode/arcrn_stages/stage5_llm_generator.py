from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path
from typing import Any, Dict, List, Optional

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
from .models import FinalReleaseNoteDocument, FinalReleaseNoteSection, utc_now_iso
from .stage5_input_loader import Stage5LoadedInputs


DEFAULT_STAGE5_SYSTEM_PROMPT_PATH = Path(__file__).resolve().parent / "prompts" / "stage5_release_system.txt"
DEFAULT_STAGE5_USER_PROMPT_PATH = Path(__file__).resolve().parent / "prompts" / "stage5_release_user.txt"
MIN_STAGE5_LLM_MAX_TOKENS = 1800


def maybe_generate_stage5_with_llm(
    *,
    config,
    loaded_inputs: Stage5LoadedInputs,
    fallback_document: FinalReleaseNoteDocument,
) -> tuple[FinalReleaseNoteDocument, Dict[str, Any]]:
    llm_client = maybe_build_llm_client(config)
    if llm_client is None:
        return _mark_stage5_fallback_stats(fallback_document), {}

    system_prompt_path = resolve_prompt_path(config, "stage5_system_prompt_path", DEFAULT_STAGE5_SYSTEM_PROMPT_PATH)
    user_prompt_path = resolve_prompt_path(config, "stage5_user_prompt_path", DEFAULT_STAGE5_USER_PROMPT_PATH)
    system_prompt = load_prompt_text(system_prompt_path)
    user_template = load_prompt_text(user_prompt_path)

    prompt_payload = {
        "repo_name": str(getattr(getattr(config, "repo_path", None), "name", "") or ""),
        "base_ref": str(getattr(config, "base_ref", "") or ""),
        "new_ref": str(getattr(config, "new_ref", "") or ""),
        "release_plan_stats_json": to_pretty_json(loaded_inputs.release_plan.get("stats") or {}),
        "section_summaries_json": to_pretty_json(loaded_inputs.section_summaries.get("summaries") or []),
    }
    user_prompt = render_prompt_template(user_template, prompt_payload)

    rate_limiter = TokenBucketRateLimiter(
        qps=getattr(config, "step10_rate_limit_qps", None),
        burst=int(getattr(config, "step10_rate_limit_burst", 1)),
    )

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
            request_name="stage5:final_release_note",
            rate_limiter=rate_limiter,
            max_tokens=max(MIN_STAGE5_LLM_MAX_TOKENS, int(getattr(config, "llm_max_tokens", 0) or 0)),
        )
        parsed_response = parse_json_response(raw_response)
        document = _merge_stage5_document(fallback_document, parsed_response)
        document = _mark_stage5_llm_stats(document)
    except Exception as exc:
        document = _mark_stage5_fallback_stats(fallback_document)
        used_fallback = True
        error_message = str(exc)

    audit_payload = {
        "stage5_llm_prompts": {
            "generated_at": document.generated_at,
            "record_count": 1,
            "records": [
                {
                    "request_name": "stage5:final_release_note",
                    "system_prompt_path": str(system_prompt_path),
                    "user_prompt_path": str(user_prompt_path),
                    "system_prompt": system_prompt,
                    "user_prompt": user_prompt,
                    "prompt_payload": _materialize_prompt_payload(prompt_payload),
                }
            ],
        },
        "stage5_llm_responses": {
            "generated_at": document.generated_at,
            "record_count": 1,
            "records": [
                {
                    "request_name": "stage5:final_release_note",
                    "used_fallback": used_fallback,
                    "error_message": error_message,
                    "raw_response": raw_response,
                    "parsed_response": parsed_response,
                }
            ],
        },
    }
    return document, audit_payload


def _merge_stage5_document(
    fallback_document: FinalReleaseNoteDocument,
    parsed_response: Dict[str, Any],
) -> FinalReleaseNoteDocument:
    overview = _clean_text(str(parsed_response.get("overview") or ""))
    if not overview:
        raise ValueError("Stage 5 LLM response does not contain a non-empty overview.")

    title = _clean_text(str(parsed_response.get("title") or "")) or fallback_document.title
    highlights = _coerce_text_list(parsed_response.get("highlights"), limit=3)
    if not highlights:
        highlights = list(fallback_document.highlights)

    parsed_sections = parsed_response.get("sections")
    if not isinstance(parsed_sections, list):
        raise ValueError("Stage 5 LLM response must contain a sections list.")

    section_by_id = {
        str(item.get("section_id") or ""): item
        for item in parsed_sections
        if isinstance(item, dict) and str(item.get("section_id") or "")
    }

    merged_sections: List[FinalReleaseNoteSection] = []
    for index, fallback_section in enumerate(fallback_document.sections):
        parsed_section = section_by_id.get(fallback_section.section_id or "")
        if parsed_section is None and index < len(parsed_sections) and isinstance(parsed_sections[index], dict):
            parsed_section = parsed_sections[index]

        if parsed_section is None:
            merged_sections.append(fallback_section)
            continue

        merged_sections.append(
            replace(
                fallback_section,
                title=_clean_text(str(parsed_section.get("title") or "")) or fallback_section.title,
                summary=_clean_text(str(parsed_section.get("summary") or "")) or fallback_section.summary,
                key_points=_coerce_text_list(parsed_section.get("key_points"), limit=4) or fallback_section.key_points,
            )
        )

    document = FinalReleaseNoteDocument(
        generated_at=utc_now_iso(),
        source_plan_path=fallback_document.source_plan_path,
        source_section_summaries_path=fallback_document.source_section_summaries_path,
        title=title,
        overview=overview,
        highlights=highlights,
        sections=merged_sections,
        stats=_build_stage5_stats(merged_sections, len(highlights)),
    )
    return document


def _build_stage5_stats(sections: List[FinalReleaseNoteSection], highlight_count: int) -> Dict[str, Any]:
    return {
        "section_count": len(sections),
        "highlight_count": highlight_count,
        "total_key_point_count": sum(len(section.key_points) for section in sections),
        "architecture_section_count": sum(
            1 for section in sections if section.section_type in {"module-added", "module-removed", "module-evolution"}
        ),
        "cross_module_section_count": sum(1 for section in sections if section.section_type == "cross-module"),
        "supporting_section_count": sum(1 for section in sections if section.section_type == "supporting-updates"),
    }


def _mark_stage5_fallback_stats(document: FinalReleaseNoteDocument) -> FinalReleaseNoteDocument:
    stats = dict(document.stats)
    stats.update({"generation_mode": "fallback", "llm_used": 0})
    return replace(document, stats=stats)


def _mark_stage5_llm_stats(document: FinalReleaseNoteDocument) -> FinalReleaseNoteDocument:
    stats = dict(document.stats)
    stats.update({"generation_mode": "llm", "llm_used": 1})
    return replace(document, stats=stats)


def _materialize_prompt_payload(payload: Dict[str, str]) -> Dict[str, Any]:
    materialized = dict(payload)
    for key in ("release_plan_stats_json", "section_summaries_json"):
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


def _clean_text(value: str) -> str:
    return " ".join(value.split()).strip()
