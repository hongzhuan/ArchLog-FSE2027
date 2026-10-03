from __future__ import annotations

from dataclasses import asdict, dataclass, field, is_dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


RELEASE_NOTE_SCHEMA: Dict[str, Any] = {
    "title": "Release Note",
    "sections": {
        "overview": "Release overview",
        "architecture_changes": {
            "added_modules": "Added modules",
            "removed_modules": "Removed modules",
            "changed_modules": "Changed modules",
        },
        "functional_changes": {
            "new_features": "New features",
            "bug_fixes": "Bug fixes",
            "refactorings": "Refactoring and optimization",
            "tests": "Tests",
        },
        "non_functional_changes": {
            "performance": "Performance optimization",
            "security": "Security",
            "documentation": "Documentation",
            "build_ci": "Build / CI",
            "maintenance": "Maintenance",
        },
        "others": "Other changes",
    },
}


SCHEMA_SLOTS = [
    "architecture_changes.added_modules",
    "architecture_changes.removed_modules",
    "architecture_changes.changed_modules",
    "functional_changes.new_features",
    "functional_changes.bug_fixes",
    "functional_changes.refactorings",
    "functional_changes.tests",
    "non_functional_changes.performance",
    "non_functional_changes.security",
    "non_functional_changes.documentation",
    "non_functional_changes.build_ci",
    "non_functional_changes.maintenance",
    "others",
]


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class SerializationMixin:
    def to_dict(self) -> Dict[str, Any]:
        return _to_serializable(asdict(self))


def _to_serializable(value: Any) -> Any:
    if is_dataclass(value):
        return _to_serializable(asdict(value))
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _to_serializable(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_to_serializable(item) for item in value]
    if isinstance(value, tuple):
        return [_to_serializable(item) for item in value]
    return value


@dataclass
class ChangeRecord(SerializationMixin):
    commit_id: str
    commit_message: str
    commit_summary: str
    commit_url: Optional[str] = None
    pull_requests: List[Dict[str, Any]] = field(default_factory=list)
    changed_files: List[str] = field(default_factory=list)
    changed_methods: List[str] = field(default_factory=list)
    diff_hunks: List[str] = field(default_factory=list)
    call_context: str = ""
    functional_category: str = "unknown"
    evidence_granularity: str = "method_level"
    change_detection_status: str = "method_level_change"
    source_refs: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Phase1ChangeRecordsOutput(SerializationMixin):
    generated_at: str
    source_change_ir_path: str
    source_files: Dict[str, str] = field(default_factory=dict)
    change_records: List[ChangeRecord] = field(default_factory=list)
    stats: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AttributedChangeRecord(ChangeRecord):
    architecture_relevance_score: float = 0.0
    structure_role: str = "local_supporting"
    confidence: str = "low"
    primary_module: str = ""
    primary_component: str = ""
    secondary_modules: List[str] = field(default_factory=list)
    scope: str = "single_module"
    matched_arch_events: List[str] = field(default_factory=list)
    arch_event_types: List[str] = field(default_factory=list)
    architecture_evidence: List[Dict[str, Any]] = field(default_factory=list)
    score_breakdown: Dict[str, float] = field(default_factory=dict)


@dataclass
class Phase2AttributedChangeRecordsOutput(SerializationMixin):
    generated_at: str
    source_change_records_path: str
    source_arch_inputs: Dict[str, str] = field(default_factory=dict)
    thresholds: Dict[str, float] = field(default_factory=dict)
    attributed_change_records: List[AttributedChangeRecord] = field(default_factory=list)
    stats: Dict[str, Any] = field(default_factory=dict)


@dataclass
class PhasePipelineResult(SerializationMixin):
    output_files: Dict[str, str] = field(default_factory=dict)
    stats: Dict[str, Any] = field(default_factory=dict)
