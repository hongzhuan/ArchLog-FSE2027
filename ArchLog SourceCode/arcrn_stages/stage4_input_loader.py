from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class Stage4ArchChange:
    change_id: str
    change_type: str
    module_uid: Optional[str] = None
    module_name: Optional[str] = None
    component_name: Optional[str] = None
    significance: float = 0.0
    summary: Optional[str] = None
    related_files: List[str] = field(default_factory=list)


@dataclass
class Stage4LoadedInputs:
    release_plan: Dict[str, Any]
    change_ir: Dict[str, Any]
    mapping_output: Dict[str, Any]
    diff_ir: Dict[str, Any]
    release_plan_path: Path
    change_ir_path: Path
    mapping_path: Path
    diff_ir_path: Path
    arch_changes: List[Stage4ArchChange] = field(default_factory=list)


def load_stage4_inputs(
    *,
    release_plan_path: Path,
    change_ir_path: Path,
    mapping_path: Path,
    diff_ir_path: Path,
) -> Stage4LoadedInputs:
    release_plan = _load_json(release_plan_path)
    change_ir = _load_json(change_ir_path)
    mapping_output = _load_json(mapping_path)
    diff_ir = _load_json(diff_ir_path)

    return Stage4LoadedInputs(
        release_plan=release_plan,
        change_ir=change_ir,
        mapping_output=mapping_output,
        diff_ir=diff_ir,
        release_plan_path=release_plan_path,
        change_ir_path=change_ir_path,
        mapping_path=mapping_path,
        diff_ir_path=diff_ir_path,
        arch_changes=_extract_arch_changes(diff_ir),
    )


def _extract_arch_changes(diff_ir_payload: Dict[str, Any]) -> List[Stage4ArchChange]:
    arch_changes: List[Stage4ArchChange] = []
    for raw_change in diff_ir_payload.get("changes") or []:
        if not isinstance(raw_change, dict):
            continue

        detail = raw_change.get("detail") or {}
        semantics = detail.get("semantics") or {}
        arch_semantics = semantics.get("arch") if isinstance(semantics, dict) else {}

        arch_changes.append(
            Stage4ArchChange(
                change_id=str(raw_change.get("id") or "").strip(),
                change_type=str(raw_change.get("type") or "").strip(),
                module_uid=_first_non_empty(detail, "module_uid", "to_module_uid", "from_module_uid"),
                module_name=_first_non_empty(detail, "module_name", "to_name", "from_name"),
                component_name=_first_non_empty(
                    arch_semantics if isinstance(arch_semantics, dict) else {},
                    "to_component",
                    "from_component",
                ),
                significance=_extract_significance(detail),
                summary=str(raw_change.get("summary") or "").strip() or None,
                related_files=_extract_related_files(detail),
            )
        )
    return arch_changes


def _extract_related_files(detail: Dict[str, Any]) -> List[str]:
    related_files: List[str] = []

    semantics = detail.get("semantics") or {}
    code = semantics.get("code") if isinstance(semantics, dict) else {}
    if isinstance(code, dict):
        for key in ("added_files", "removed_files"):
            for item in code.get(key) or []:
                if not isinstance(item, dict):
                    continue
                file_path = _normalize_path(item.get("path"))
                if file_path:
                    related_files.append(file_path)

    examples = detail.get("examples") or {}
    if isinstance(examples, dict):
        for key in ("added_files_top", "removed_files_top"):
            for file_path in examples.get(key) or []:
                normalized = _normalize_path(file_path)
                if normalized:
                    related_files.append(normalized)

    return sorted(set(related_files))


def _extract_significance(detail: Dict[str, Any]) -> float:
    value = detail.get("architecture_significance")
    if value is None:
        value = detail.get("significance")
    try:
        return float(value)
    except Exception:
        return 0.0


def _first_non_empty(container: Dict[str, Any], *keys: str) -> Optional[str]:
    for key in keys:
        value = str(container.get(key) or "").strip()
        if value:
            return value
    return None


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _normalize_path(path: Any) -> str:
    if path is None:
        return ""
    text = str(path).replace("\\", "/").strip()
    while text.startswith("./"):
        text = text[2:]
    return text
