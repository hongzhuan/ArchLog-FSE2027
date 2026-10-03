from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


def export_code_change_llm_io(result: Any, output_dir: Path) -> Optional[str]:
    prompts_output = getattr(result.artifacts, "llm_prompts", None)
    summaries_output = getattr(result.artifacts, "code_change_summaries", None)
    if prompts_output is None or summaries_output is None:
        return None

    prompt_by_unit = {item.unit_id: item for item in prompts_output.prompts}
    lines: List[str] = ["# Code Changes Step 10 LLM Input/Output", ""]
    for summary in summaries_output.summaries:
        prompt = prompt_by_unit.get(summary.unit_id)
        lines.extend(
            [
                _record_title(summary.unit_id),
                f"commit_id: {summary.commit_id}",
                f"predicted_category: {summary.predicted_category}",
                f"used_fallback: {summary.raw_response is None}",
                f"llm_failure_reason: {summary.llm_failure_reason or ''}",
                "",
                "SYSTEM PROMPT:",
                _text_or_empty(getattr(prompt, "system_prompt", "")),
                "",
                "USER PROMPT:",
                _text_or_empty(getattr(prompt, "user_prompt", "")),
                "",
                "LLM RAW OUTPUT:",
                _text_or_empty(summary.raw_response or summary.llm_failure_raw_response or ""),
                "",
                "FINAL OUTPUT:",
                _text_or_empty(summary.summary),
                "",
            ]
        )

    return _write_text(output_dir / "step10_llm_input_output.txt", "\n".join(lines))


def export_phase3_aggregation_llm_io(audit: Dict[str, Any], output_dir: Path) -> Optional[str]:
    calls = [item for item in audit.get("calls") or [] if isinstance(item, dict)]
    if not calls:
        return None

    lines: List[str] = ["# Phase 3.1 LLM Aggregation Input/Output", ""]
    for index, call in enumerate(calls, start=1):
        lines.extend(
            [
                _record_title(f"{index:03d}_{call.get('stage') or 'llm_call'}"),
                f"request_suffix: {call.get('request_suffix') or ''}",
                f"prompt_path: {call.get('prompt_path') or ''}",
                f"ok: {call.get('ok')}",
                f"validation_attempt_count: {len(call.get('validation_attempts') or [])}",
                f"error_message: {call.get('error_message') or ''}",
                "",
                "SYSTEM PROMPT:",
                _text_or_empty(call.get("system_prompt") or ""),
                "",
                "USER PROMPT:",
                _text_or_empty(call.get("user_prompt") or ""),
                "",
                "LLM RAW OUTPUT:",
                _text_or_empty(call.get("raw_response") or ""),
                "",
                "VALIDATION ATTEMPTS:",
                _text_or_empty(call.get("validation_attempts") or ""),
                "",
            ]
        )

    return _write_text(output_dir / "phase3_1_llm_input_output.txt", "\n".join(lines))


def export_slot_entry_llm_io(audits: Iterable[Dict[str, Any]], output_dir: Path) -> Optional[str]:
    records = [item for item in audits if isinstance(item, dict) and (item.get("system_prompt") or item.get("user_prompt"))]
    if not records:
        return None

    lines: List[str] = ["# Phase 3.2 Slot Entry LLM Input/Output", ""]
    for record in records:
        name = f"{record.get('slot') or 'slot'}_{record.get('group_id') or record.get('section_id') or 'record'}"
        lines.extend(_audit_record_lines(name, record))
    return _write_text(output_dir / "phase3_2_llm_input_output.txt", "\n".join(lines))


def export_arch_label_llm_io(audits: Iterable[Dict[str, Any]], output_dir: Path) -> Optional[str]:
    records = [item for item in audits if isinstance(item, dict) and (item.get("system_prompt") or item.get("user_prompt"))]
    if not records:
        return None

    lines: List[str] = ["# Phase 3.2.5 Architecture Label LLM Input/Output", ""]
    for record in records:
        name = f"{record.get('slot') or 'slot'}_architecture_label"
        lines.extend(_audit_record_lines(name, record))
    return _write_text(output_dir / "phase3_2_arch_label_llm_input_output.txt", "\n".join(lines))


def export_arch_module_assignment_llm_io(audits: Iterable[Dict[str, Any]], output_dir: Path) -> Optional[str]:
    records = [item for item in audits if isinstance(item, dict) and (item.get("system_prompt") or item.get("user_prompt"))]
    if not records:
        return None

    lines: List[str] = ["# Phase 3.2.6 Architecture Component Assignment LLM Input/Output", ""]
    for record in records:
        name = f"{record.get('batch_key') or 'batch'}_architecture_component_assignment"
        lines.extend(_audit_record_lines(name, record))
    return _write_text(output_dir / "phase3_2_arch_module_assignment_llm_input_output.txt", "\n".join(lines))


def export_final_composition_llm_io(audit: Dict[str, Any], output_dir: Path) -> Optional[str]:
    records = [item for item in audit.get("calls") or [] if isinstance(item, dict)]
    if records:
        lines: List[str] = ["# Phase 3.3 Final Composition LLM Input/Output", ""]
        for record in records:
            name = record.get("request_name") or record.get("batch_key") or "final_composition"
            lines.extend(_audit_record_lines(str(name), record))
        return _write_text(output_dir / "phase3_3_llm_input_output.txt", "\n".join(lines))

    if not audit.get("system_prompt") and not audit.get("user_prompt"):
        return None
    text = "\n".join(["# Phase 3.3 Final Composition LLM Input/Output", ""] + _audit_record_lines("final_composition", audit))
    return _write_text(output_dir / "phase3_3_llm_input_output.txt", text)


def _audit_record_lines(name: str, record: Dict[str, Any]) -> List[str]:
    return [
        _record_title(name),
        f"llm_used: {record.get('llm_used')}",
        f"error_message: {record.get('error_message') or ''}",
        "",
        "SYSTEM PROMPT:",
        _text_or_empty(record.get("system_prompt") or ""),
        "",
        "USER PROMPT:",
        _text_or_empty(record.get("user_prompt") or ""),
        "",
        "LLM RAW OUTPUT:",
        _text_or_empty(record.get("raw_response") or ""),
        "",
        "VALIDATION ATTEMPTS:",
        _text_or_empty(record.get("attempts") or ""),
        "",
    ]


def _record_title(name: str) -> str:
    return f"===== {name} ====="


def _text_or_empty(value: Any) -> str:
    text = str(value or "")
    return text if text.strip() else "(empty)"


def _write_text(path: Path, text: str) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return str(path)
