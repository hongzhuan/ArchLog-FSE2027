from __future__ import annotations

import json
import os
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict


_PROGRESS_LOCK = threading.Lock()


def write_progress_event(config: Any, event_type: str, **fields: Any) -> None:
    """Append a small progress event without affecting pipeline behavior."""
    output_dir = _resolve_output_dir(config)
    if output_dir is None:
        return
    payload: Dict[str, Any] = {
        "schema_version": 1,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": str(event_type or ""),
        "provider": str(getattr(config, "llm_provider", "") or ""),
        "model": str(getattr(config, "llm_model_name", "") or ""),
        "thinking_enabled": bool(getattr(config, "llm_enable_thinking", False)),
        "pid": os.getpid(),
        "thread": threading.current_thread().name,
    }
    payload.update({key: _jsonable(value) for key, value in fields.items()})
    try:
        progress_dir = output_dir / "00_pipeline_summary"
        progress_dir.mkdir(parents=True, exist_ok=True)
        progress_path = progress_dir / "archlog_progress.jsonl"
        with _PROGRESS_LOCK:
            with progress_path.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
    except Exception:
        return


def _resolve_output_dir(config: Any) -> Path | None:
    configured = getattr(config, "output_dir", None) if config is not None else None
    if not configured:
        return None
    path = Path(configured)
    if path.name in {
        "01_code_changes",
        "02_phase1_change_evidence",
        "03_phase2_arch_signal_attribution",
        "04_phase3_1_llm_aggregation_planning",
        "05_phase3_2_slot_entry_generation",
        "06_phase3_3_final_composition",
        "00_pipeline_summary",
    }:
        return path.parent
    return path


def _jsonable(value: Any) -> Any:
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_jsonable(item) for item in value]
    return str(value)
