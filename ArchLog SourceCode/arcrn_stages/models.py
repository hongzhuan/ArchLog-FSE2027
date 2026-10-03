from __future__ import annotations

from dataclasses import asdict, dataclass, field, is_dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


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
        return {str(k): _to_serializable(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_to_serializable(v) for v in value]
    if isinstance(value, tuple):
        return [_to_serializable(v) for v in value]
    return value


@dataclass
class ValidationIssue(SerializationMixin):
    level: str
    message: str
    commit_id: Optional[str] = None
    change_unit_id: Optional[str] = None


@dataclass
class ValidationReport(SerializationMixin):
    issues: List[ValidationIssue] = field(default_factory=list)

    @property
    def warning_count(self) -> int:
        return sum(1 for issue in self.issues if issue.level == "warning")

    @property
    def error_count(self) -> int:
        return sum(1 for issue in self.issues if issue.level == "error")


@dataclass
class ChangeUnitRecord(SerializationMixin):
    change_unit_id: str
    commit_id: str
    summary: Optional[str] = None
    category: Optional[str] = None
    commit_url: Optional[str] = None
    pull_requests: List[Dict[str, Any]] = field(default_factory=list)

    changed_files: List[str] = field(default_factory=list)
    changed_methods: List[str] = field(default_factory=list)
    change_types: List[str] = field(default_factory=list)

    matched_hunk_ids: List[str] = field(default_factory=list)
    diff_snippets: List[str] = field(default_factory=list)

    related_entities: List[str] = field(default_factory=list)
    call_context: Optional[str] = None

    evidence_granularity: str = "method_level"
    change_detection_status: str = "method_level_change"
    source_refs: Dict[str, Any] = field(default_factory=dict)


@dataclass
class CommitChangeRecord(SerializationMixin):
    commit_id: str
    commit_message: str
    author: Optional[str] = None
    date: Optional[str] = None

    change_units: List[ChangeUnitRecord] = field(default_factory=list)

    commit_summary: Optional[str] = None
    category: Optional[str] = None
    commit_url: Optional[str] = None
    pull_requests: List[Dict[str, Any]] = field(default_factory=list)

    all_changed_files: List[str] = field(default_factory=list)
    all_changed_methods: List[str] = field(default_factory=list)

    file_count: int = 0
    method_count: int = 0
    change_unit_count: int = 0

    has_diff: bool = False
    has_call_context: bool = False

    debug_info: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ChangeIR(SerializationMixin):
    generated_at: str
    input_dir: str
    source_files: Dict[str, str] = field(default_factory=dict)
    source_pipeline: Dict[str, Any] = field(default_factory=dict)
    commits: List[CommitChangeRecord] = field(default_factory=list)
    stats: Dict[str, Any] = field(default_factory=dict)
    validation: ValidationReport = field(default_factory=ValidationReport)


@dataclass
class Stage1PipelineResult(SerializationMixin):
    change_ir: ChangeIR
    output_files: Dict[str, str] = field(default_factory=dict)


@dataclass
class CommitArchMapping(SerializationMixin):
    commit_id: str
    arch_label: str
    arch_confidence: str
    arch_reasons: List[str] = field(default_factory=list)
    impact_score: float = 0.0

    primary_module: Optional[str] = None
    primary_module_name: Optional[str] = None
    primary_component: Optional[str] = None
    secondary_modules: List[str] = field(default_factory=list)
    secondary_module_names: List[str] = field(default_factory=list)
    secondary_components: List[str] = field(default_factory=list)

    scope: str = "single-module"

    changed_files: List[str] = field(default_factory=list)
    matched_arch_change_ids: List[str] = field(default_factory=list)
    matched_arch_change_types: List[str] = field(default_factory=list)


@dataclass
class CommitArchMappingOutput(SerializationMixin):
    generated_at: str
    source_change_ir_path: str
    source_arch_inputs: Dict[str, str] = field(default_factory=dict)
    mappings: List[CommitArchMapping] = field(default_factory=list)
    stats: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ReleaseSectionPlan(SerializationMixin):
    section_id: str
    title: str
    section_type: str
    primary_module: Optional[str] = None
    primary_module_name: Optional[str] = None
    primary_component: Optional[str] = None
    secondary_modules: List[str] = field(default_factory=list)
    secondary_module_names: List[str] = field(default_factory=list)
    secondary_components: List[str] = field(default_factory=list)
    commit_ids: List[str] = field(default_factory=list)
    arch_change_ids: List[str] = field(default_factory=list)
    arch_change_types: List[str] = field(default_factory=list)
    rationale: Optional[str] = None


@dataclass
class ReleaseNotePlan(SerializationMixin):
    generated_at: str
    source_change_ir_path: str
    source_mapping_path: str
    source_arch_diff_path: str
    sections: List[ReleaseSectionPlan] = field(default_factory=list)
    stats: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Stage3PipelineResult(SerializationMixin):
    release_plan: ReleaseNotePlan
    output_files: Dict[str, str] = field(default_factory=dict)


@dataclass
class SectionSummaryRecord(SerializationMixin):
    section_id: str
    title: str
    section_type: str
    summary: str
    primary_module_name: Optional[str] = None
    primary_component: Optional[str] = None
    commit_ids: List[str] = field(default_factory=list)
    arch_change_ids: List[str] = field(default_factory=list)
    supporting_details: List[str] = field(default_factory=list)


@dataclass
class SectionSummariesOutput(SerializationMixin):
    generated_at: str
    source_plan_path: str
    source_change_ir_path: str
    source_mapping_path: str
    source_arch_diff_path: str
    summaries: List[SectionSummaryRecord] = field(default_factory=list)
    stats: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Stage4PipelineResult(SerializationMixin):
    section_summaries: SectionSummariesOutput
    output_files: Dict[str, str] = field(default_factory=dict)


@dataclass
class FinalReleaseNoteSection(SerializationMixin):
    title: str
    section_type: str
    summary: str
    section_id: Optional[str] = None
    primary_module_name: Optional[str] = None
    primary_component: Optional[str] = None
    commit_count: int = 0
    arch_change_count: int = 0
    key_points: List[str] = field(default_factory=list)


@dataclass
class FinalReleaseNoteDocument(SerializationMixin):
    generated_at: str
    source_plan_path: str
    source_section_summaries_path: str
    title: str
    overview: str
    highlights: List[str] = field(default_factory=list)
    sections: List[FinalReleaseNoteSection] = field(default_factory=list)
    stats: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Stage5PipelineResult(SerializationMixin):
    final_release_note: FinalReleaseNoteDocument
    output_files: Dict[str, str] = field(default_factory=dict)


@dataclass
class ArcRNPipelineStageRecord(SerializationMixin):
    stage_name: str
    started_at: Optional[str] = None
    finished_at: Optional[str] = None
    duration_sec: Optional[float] = None
    output_files: Dict[str, str] = field(default_factory=dict)
    stats: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ArcRNPipelineResult(SerializationMixin):
    generated_at: str
    repo_name: str
    base_ref: str
    new_ref: str
    output_dir: str
    started_at: Optional[str] = None
    finished_at: Optional[str] = None
    duration_sec: Optional[float] = None
    stages: List[ArcRNPipelineStageRecord] = field(default_factory=list)
    final_outputs: Dict[str, str] = field(default_factory=dict)
