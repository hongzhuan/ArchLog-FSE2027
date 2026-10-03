from __future__ import annotations

from dataclasses import asdict, dataclass, field, is_dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional

from .constants import (
    CATEGORY_UNKNOWN,
    CHANGE_TYPE_MODIFIED,
    DEFAULT_CONTEXT_GRAPH_MAX_EDGES,
    DEFAULT_CONTEXT_GRAPH_MAX_HOPS,
    DEFAULT_CONTEXT_GRAPH_MAX_NODES,
    DEFAULT_ENRE_MATCH_MIN_SCORE,
    DEFAULT_HUNK_METHOD_MIN_COVERAGE,
    DEFAULT_TOP_K_EXEMPLARS,
    PIPELINE_NAME,
    PIPELINE_STEP_SEQUENCE,
)


LLM_CONTEXT_TOKEN_LIMIT = 65_536


def _default_file_level_fallback_patterns() -> List[str]:
    return [
        "*.md",
        "*.rst",
        "*.adoc",
        "*.txt",
        "README*",
        "CHANGELOG*",
        "CONTRIBUTING*",
        "LICENSE*",
        "COPYING*",
        "AUTHORS*",
        "CMakeLists.txt",
        "*.cmake",
        "meson.build",
        "meson_options.txt",
        "Makefile",
        "GNUmakefile",
        "*.mk",
        "configure.ac",
        "BUILD",
        "BUILD.bazel",
        "WORKSPACE",
        "WORKSPACE.bazel",
        "pkg-config/**",
        "*.pc.in",
        ".travis.yml",
        ".gitlab-ci.yml",
        "appveyor.yml",
        ".appveyor.yml",
        ".github/**",
        ".circleci/**",
        ".azure-pipelines/**",
        ".travis_scripts/**",
        "makerelease.py",
        "devtools/**",
        "scripts/**",
        "release/**",
        "*.dict",
        "*.expected",
        "*.golden",
        "*.in",
        "*.out",
        "*.json",
        ".gitignore",
        ".gitattributes",
    ]


# ============================================================
# General helpers
# ============================================================

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class SerializationMixin:
    def to_dict(self) -> Dict[str, Any]:
        return _to_serializable(asdict(self))

    def to_json_ready(self) -> Dict[str, Any]:
        return self.to_dict()


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


# ============================================================
# Pipeline configuration
# ============================================================

@dataclass
class PromptConfig(SerializationMixin):
    system_prompt_path: Optional[Path] = None
    user_prompt_path: Optional[Path] = None
    exemplars_dir: Optional[Path] = None
    top_k_exemplars: int = DEFAULT_TOP_K_EXEMPLARS


@dataclass
class GraphConfig(SerializationMixin):
    max_hops: int = DEFAULT_CONTEXT_GRAPH_MAX_HOPS
    max_nodes: int = DEFAULT_CONTEXT_GRAPH_MAX_NODES
    max_edges: int = DEFAULT_CONTEXT_GRAPH_MAX_EDGES
    include_relation_types: List[str] = field(default_factory=list)


@dataclass
class MatchingConfig(SerializationMixin):
    enre_min_score: float = DEFAULT_ENRE_MATCH_MIN_SCORE
    hunk_method_min_coverage: float = DEFAULT_HUNK_METHOD_MIN_COVERAGE


@dataclass
class PipelineConfig(SerializationMixin):
    repo_path: Path
    base_ref: str
    new_ref: str
    enre_json_path: Path
    output_dir: Path

    language: str = "cpp"
    pipeline_name: str = PIPELINE_NAME

    architecture_changes_path: Optional[Path] = None
    app_description_path: Optional[Path] = None
    external_analysis_enabled: bool = False
    external_analysis_reuse_existing: bool = True
    external_worktree_root: Path = Path("repositories/.archlog_worktrees")
    enre_jar_path: Path = Path("third_party/ENRE-CPP/ENRE-CPP.jar")
    enre_output_dir: Path = Path("repositories/ENRE-C")
    semarc_executable_path: Path = Path("third_party/SemArc/SemArcArcRN.exe")
    semarc_output_dir: Path = Path("arch_changes-reports/sema_results")
    java_executable: str = "java"

    llm_model_name: Optional[str] = None
    llm_provider: str = "qwen"
    llm_temperature: float = 0.0
    llm_max_tokens: Optional[int] = LLM_CONTEXT_TOKEN_LIMIT
    llm_context_token_limit: int = LLM_CONTEXT_TOKEN_LIMIT
    llm_request_timeout_sec: float = 180.0
    llm_base_url: Optional[str] = None
    llm_api_key_env_var: str = ""
    llm_enable_thinking: bool = False
    debug_fail_fast_on_llm_error: bool = True
    phase3_debug_fail_fast: bool = True
    step10_concurrency: int = 1
    step10_rate_limit_qps: Optional[float] = None
    step10_rate_limit_burst: int = 1
    step10_retry_max_attempts: int = 3
    step10_retry_base_delay_sec: float = 1.0
    step10_retry_max_delay_sec: float = 10.0
    step10_retry_jitter_ratio: float = 0.2
    llm_output_validation_max_retries: int = 1
    file_level_fallback_enabled: bool = True
    file_level_fallback_patterns: List[str] = field(default_factory=_default_file_level_fallback_patterns)
    step10_pr_metadata_enabled: bool = True
    step10_pr_metadata_token_env: str = "GITHUB_TOKEN"
    phase3_llm_short_hash_min_length: int = 7
    phase3_value_batch_size: int = 8
    phase3_group_review_batch_size: int = 40
    phase3_final_composition_fallback_on_coverage_failure: bool = True
    phase3_arch_module_assignment_enabled: bool = True
    phase3_arch_module_assignment_batch_size: int = 20
    phase3_arch_module_assignment_concurrency: int = 1
    phase3_arch_module_assignment_prompt_path: Optional[Path] = None
    phase3_final_composition_batch_size: int = 25
    phase3_final_composition_concurrency: int = 1
    phase3_final_overview_prompt_path: Optional[Path] = None
    phase3_low_priority_routing_batch_size: int = 8
    phase3_low_priority_routing_concurrency: int = 8
    phase3_low_priority_routing_candidate_limit: int = 80
    phase3_low_priority_brief_batch_size: int = 20
    phase3_low_priority_brief_concurrency: int = 8
    phase2_llm_arch_relevance_enabled: bool = True
    phase2_llm_event_profile_enabled: bool = True
    phase2_llm_concurrency: int = 1
    phase2_llm_prompt_path: Optional[Path] = None
    phase2_ablation_mode: str = "full"
    phase2_summary_diff_only_prompt_path: Optional[Path] = None
    phase2_event_profile_prompt_path: Optional[Path] = None
    phase3_arch_label_llm_enabled: bool = True
    phase3_arch_label_prompt_path: Optional[Path] = None
    phase3_arch_label_concurrency: int = 1
    phase3_important_grouping_mode: str = "component"

    save_intermediate: bool = True
    fail_fast: bool = True
    verbose: bool = True

    prompt: PromptConfig = field(default_factory=PromptConfig)
    graph: GraphConfig = field(default_factory=GraphConfig)
    matching: MatchingConfig = field(default_factory=MatchingConfig)

    def validate(self) -> None:
        if not self.repo_path:
            raise ValueError("repo_path is required.")
        if not self.base_ref:
            raise ValueError("base_ref is required.")
        if not self.new_ref:
            raise ValueError("new_ref is required.")
        if not self.enre_json_path:
            raise ValueError("enre_json_path is required.")
        if not self.output_dir:
            raise ValueError("output_dir is required.")
        if self.base_ref == self.new_ref:
            raise ValueError("base_ref and new_ref must be different.")

        if not self.repo_path.exists() or not self.repo_path.is_dir():
            raise ValueError(f"repo_path does not exist or is not a directory: {self.repo_path}")

        if not self.enre_json_path.exists() or not self.enre_json_path.is_file():
            raise ValueError(f"enre_json_path does not exist or is not a file: {self.enre_json_path}")

        if self.step10_concurrency < 1:
            raise ValueError("step10_concurrency must be >= 1.")
        if self.llm_request_timeout_sec <= 0:
            raise ValueError("llm_request_timeout_sec must be > 0.")
        if self.step10_rate_limit_qps is not None and self.step10_rate_limit_qps <= 0:
            raise ValueError("step10_rate_limit_qps must be > 0 when provided.")
        if self.step10_rate_limit_burst < 1:
            raise ValueError("step10_rate_limit_burst must be >= 1.")
        if self.step10_retry_max_attempts < 1:
            raise ValueError("step10_retry_max_attempts must be >= 1.")
        if self.step10_retry_base_delay_sec < 0:
            raise ValueError("step10_retry_base_delay_sec must be >= 0.")
        if self.step10_retry_max_delay_sec < self.step10_retry_base_delay_sec:
            raise ValueError("step10_retry_max_delay_sec must be >= step10_retry_base_delay_sec.")
        if not 0 <= self.step10_retry_jitter_ratio <= 1:
            raise ValueError("step10_retry_jitter_ratio must be in [0, 1].")
        if self.llm_output_validation_max_retries < 0:
            raise ValueError("llm_output_validation_max_retries must be >= 0.")

    @property
    def version_range(self) -> str:
        return f"{self.base_ref}..{self.new_ref}"


# ============================================================
# Core domain models
# ============================================================

@dataclass
class MethodIdentity(SerializationMixin):
    method_uid: str
    qualified_name: str
    simple_name: str
    file_path: str
    start_line: int
    end_line: int

    category: str = "Function"
    parent_qualified_name: Optional[str] = None
    return_type: Optional[str] = None
    parameters: List[str] = field(default_factory=list)
    start_offset: Optional[int] = None
    end_offset: Optional[int] = None


@dataclass
class CommitInfo(SerializationMixin):
    commit_id: str
    author_name: Optional[str] = None
    author_email: Optional[str] = None
    authored_date: Optional[str] = None
    committer_name: Optional[str] = None
    committer_email: Optional[str] = None
    committed_date: Optional[str] = None
    subject: str = ""
    body: str = ""
    files_touched: List[str] = field(default_factory=list)

    @property
    def full_message(self) -> str:
        if self.body and self.body.strip():
            return f"{self.subject}\n{self.body}".strip()
        return self.subject.strip()


@dataclass
class ChangedMethod(SerializationMixin):
    method_uid: str
    change_type: str = CHANGE_TYPE_MODIFIED

    old_identity: Optional[MethodIdentity] = None
    new_identity: Optional[MethodIdentity] = None

    locator_confidence: float = 0.0
    evidence: Dict[str, Any] = field(default_factory=dict)

    commits: List[CommitInfo] = field(default_factory=list)
    primary_commit_id: Optional[str] = None

    enre_entity_id: Optional[int] = None
    enre_match_score: Optional[float] = None
    enre_match_strategy: List[str] = field(default_factory=list)

    def active_identity(self) -> MethodIdentity:
        if self.new_identity is not None:
            return self.new_identity
        if self.old_identity is not None:
            return self.old_identity
        raise ValueError(f"ChangedMethod {self.method_uid} has neither old_identity nor new_identity.")

    @property
    def qualified_name(self) -> str:
        return self.active_identity().qualified_name

    @property
    def file_path(self) -> str:
        return self.active_identity().file_path

    @property
    def start_line(self) -> int:
        return self.active_identity().start_line

    @property
    def end_line(self) -> int:
        return self.active_identity().end_line


@dataclass
class EnreEntity(SerializationMixin):
    entity_id: int
    qualified_name: str
    category: str
    file_path: str
    start_line: int
    end_line: int

    parent_id: Optional[int] = None
    entity_file: Optional[int] = None
    start_offset: Optional[int] = None
    end_offset: Optional[int] = None
    return_type: Optional[str] = None

    raw: Dict[str, Any] = field(default_factory=dict)


@dataclass
class EnreRelation(SerializationMixin):
    relation_id: Optional[str]
    src_entity_id: int
    dst_entity_id: int
    relation_type: str

    start_line: Optional[int] = None
    end_line: Optional[int] = None
    raw: Dict[str, Any] = field(default_factory=dict)


@dataclass
class EnreMatch(SerializationMixin):
    matched: bool
    entity_id: Optional[int] = None
    match_score: float = 0.0
    match_strategy: List[str] = field(default_factory=list)
    matched_entity: Optional[EnreEntity] = None


@dataclass
class GraphNode(SerializationMixin):
    entity_id: int
    qualified_name: str
    category: str
    file_path: Optional[str] = None
    start_line: Optional[int] = None
    end_line: Optional[int] = None
    role: str = "context"


@dataclass
class GraphEdge(SerializationMixin):
    src_entity_id: int
    dst_entity_id: int
    relation_type: str
    start_line: Optional[int] = None
    end_line: Optional[int] = None


@dataclass
class MethodContextGraph(SerializationMixin):
    graph_id: str
    entry_method_uid: str
    entry_entity_id: int
    commit_id: Optional[str] = None

    nodes: List[GraphNode] = field(default_factory=list)
    edges: List[GraphEdge] = field(default_factory=list)
    changed_method_uids: List[str] = field(default_factory=list)

    def node_entity_ids(self) -> List[int]:
        return [node.entity_id for node in self.nodes]


@dataclass
class DiffLine(SerializationMixin):
    line_no: Optional[int]
    text: str


@dataclass
class DiffHunk(SerializationMixin):
    hunk_id: str
    commit_id: str
    file_path_old: Optional[str]
    file_path_new: Optional[str]

    source_start: int
    source_length: int
    target_start: int
    target_length: int

    diff_header: str
    diff_text: str

    added_lines: List[DiffLine] = field(default_factory=list)
    deleted_lines: List[DiffLine] = field(default_factory=list)


@dataclass
class MatchedHunk(SerializationMixin):
    hunk_id: str
    commit_id: str
    match_type: str
    coverage_score: float

    matched_old_lines: List[int] = field(default_factory=list)
    matched_new_lines: List[int] = field(default_factory=list)
    matched_diff_text: List[str] = field(default_factory=list)


@dataclass
class MethodHunkPair(SerializationMixin):
    pair_id: str
    method_uid: str
    change_type: str
    matched_hunks: List[MatchedHunk] = field(default_factory=list)
    all_commit_ids: List[str] = field(default_factory=list)
    primary_commit_id: Optional[str] = None


@dataclass
class ArchitectureEvidence(SerializationMixin):
    architecture_change_id: str
    component_name: Optional[str] = None
    change_type: Optional[str] = None
    significance: Optional[float] = None
    summary: Optional[str] = None
    raw: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ChangeUnit(SerializationMixin):
    unit_id: str
    commit: CommitInfo

    changed_method_uids: List[str] = field(default_factory=list)
    changed_methods: List[ChangedMethod] = field(default_factory=list)

    method_context_graphs: List[MethodContextGraph] = field(default_factory=list)
    method_hunk_pairs: List[MethodHunkPair] = field(default_factory=list)

    architecture_evidence: List[ArchitectureEvidence] = field(default_factory=list)

    inferred_change_category: str = CATEGORY_UNKNOWN
    evidence: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ExemplarRecord(SerializationMixin):
    exemplar_id: str
    category: str
    input_text: str
    output_text: str
    source: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SelectedExemplarSet(SerializationMixin):
    unit_id: str
    predicted_change_category: str
    selection_evidence: Dict[str, Any] = field(default_factory=dict)
    exemplars: List[ExemplarRecord] = field(default_factory=list)


@dataclass
class PromptPayload(SerializationMixin):
    unit_id: str
    app_description: Optional[str]
    commit_id: str
    commit_message: str

    changed_methods: List[Dict[str, Any]] = field(default_factory=list)
    changed_statements: List[Dict[str, Any]] = field(default_factory=list)
    graph_texts: List[Dict[str, Any]] = field(default_factory=list)
    architecture_changes: List[Dict[str, Any]] = field(default_factory=list)

    inferred_change_category: str = CATEGORY_UNKNOWN
    evidence_granularity: str = "method_level"
    change_detection_status: str = "method_level_change"
    architecture_changes_text: Optional[str] = None
    pr_title: Optional[str] = None
    pr_body: Optional[str] = None
    pr_number: Optional[int] = None
    pr_url: Optional[str] = None
    commit_url: Optional[str] = None
    pull_requests: List[Dict[str, Any]] = field(default_factory=list)


@dataclass
class PromptRecord(SerializationMixin):
    unit_id: str
    system_prompt: str
    user_prompt: str
    payload: PromptPayload


@dataclass
class CodeChangeSummary(SerializationMixin):
    unit_id: str
    commit_id: str
    predicted_category: str
    summary: str

    raw_response: Optional[str] = None
    llm_failure_reason: Optional[str] = None
    llm_failure_raw_response: Optional[str] = None
    llm_metrics: Dict[str, Any] = field(default_factory=dict)
    used_exemplar_ids: List[str] = field(default_factory=list)
    evidence_links: Dict[str, List[str]] = field(default_factory=dict)
    commit_url: Optional[str] = None
    pull_requests: List[Dict[str, Any]] = field(default_factory=list)


# ============================================================
# Step outputs
# ============================================================

@dataclass
class ChangedMethodsOutput(SerializationMixin):
    repo_path: Path
    base_ref: str
    new_ref: str
    changed_methods: List[ChangedMethod] = field(default_factory=list)


@dataclass
class CommitsMappedOutput(SerializationMixin):
    changed_methods: List[ChangedMethod] = field(default_factory=list)


@dataclass
class EnreMatchedOutput(SerializationMixin):
    changed_methods: List[ChangedMethod] = field(default_factory=list)
    entities: List[EnreEntity] = field(default_factory=list)
    relations: List[EnreRelation] = field(default_factory=list)


@dataclass
class MethodContextGraphsOutput(SerializationMixin):
    graphs: List[MethodContextGraph] = field(default_factory=list)


@dataclass
class DiffHunksOutput(SerializationMixin):
    repo_path: Path
    version_range: str
    hunks: List[DiffHunk] = field(default_factory=list)
    file_level_hunks: List[DiffHunk] = field(default_factory=list)


@dataclass
class MethodHunkPairsOutput(SerializationMixin):
    method_hunk_pairs: List[MethodHunkPair] = field(default_factory=list)


@dataclass
class ChangeUnitsOutput(SerializationMixin):
    change_units: List[ChangeUnit] = field(default_factory=list)


@dataclass
class SelectedExemplarsOutput(SerializationMixin):
    selected_exemplar_sets: List[SelectedExemplarSet] = field(default_factory=list)


@dataclass
class PromptsOutput(SerializationMixin):
    prompts: List[PromptRecord] = field(default_factory=list)


@dataclass
class SummariesOutput(SerializationMixin):
    summaries: List[CodeChangeSummary] = field(default_factory=list)


# ============================================================
# Pipeline execution metadata
# ============================================================

@dataclass
class StepExecutionRecord(SerializationMixin):
    step_name: str
    started_at: str
    finished_at: Optional[str] = None
    duration_sec: Optional[float] = None
    success: bool = False
    output_file: Optional[str] = None
    message: Optional[str] = None
    stats: Dict[str, Any] = field(default_factory=dict)


@dataclass
class PipelineArtifacts(SerializationMixin):
    changed_methods: Optional[ChangedMethodsOutput] = None
    changed_methods_with_commits: Optional[CommitsMappedOutput] = None
    changed_methods_with_enre: Optional[EnreMatchedOutput] = None
    method_context_graphs: Optional[MethodContextGraphsOutput] = None
    diff_hunks: Optional[DiffHunksOutput] = None
    method_hunk_pairs: Optional[MethodHunkPairsOutput] = None
    change_units: Optional[ChangeUnitsOutput] = None
    selected_exemplars: Optional[SelectedExemplarsOutput] = None
    llm_prompts: Optional[PromptsOutput] = None
    code_change_summaries: Optional[SummariesOutput] = None


@dataclass
class PipelineReport(SerializationMixin):
    pipeline_name: str
    started_at: str
    finished_at: Optional[str] = None
    duration_sec: Optional[float] = None
    config: Dict[str, Any] = field(default_factory=dict)
    executed_steps: List[StepExecutionRecord] = field(default_factory=list)
    final_stats: Dict[str, Any] = field(default_factory=dict)


@dataclass
class PipelineResult(SerializationMixin):
    config: PipelineConfig
    report: PipelineReport
    artifacts: PipelineArtifacts

    def final_summaries(self) -> List[CodeChangeSummary]:
        if self.artifacts.code_change_summaries is None:
            return []
        return self.artifacts.code_change_summaries.summaries
