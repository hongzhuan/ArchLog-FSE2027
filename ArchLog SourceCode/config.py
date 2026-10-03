from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from code_changes.models import (
    GraphConfig,
    LLM_CONTEXT_TOKEN_LIMIT,
    MatchingConfig,
    PipelineConfig,
    PromptConfig,
)
from llm_provider_adapters import build_llm_provider_extra_body, resolve_llm_enable_thinking as resolve_provider_thinking

# Select one provider before an experiment. Provider-specific request syntax is
# handled in llm_provider_adapters.py; only these config values need changing.
# concurrency controls the maximum number of in-flight LLM requests.
# qps controls the average request launch rate.
# burst controls short request bursts after idle periods.
# Tune these values together to avoid provider-side rate limits.
LLM_PROVIDER = "siliconflow"  # "qwen" | "mimo" | "deepseek" | "siliconflow"
LLM_PROVIDER_CONFIGS: Dict[str, Dict[str, Any]] = {
    "qwen": {
        "model_name": "qwen3.5-plus",
        "api_key_env_var": "DASHSCOPE_API_KEY",
        "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "temperature": 0.3,
        "max_tokens": LLM_CONTEXT_TOKEN_LIMIT,
        "request_timeout_sec": 360,
        "enable_thinking": False,
        "concurrency": 96,
        "rate_limit_qps": 50,
        "rate_limit_burst": 50,
    },
    "mimo": {
        "model_name": "mimo-v2.5",
        "api_key_env_var": "MIMO_API_KEY",
        "base_url": "https://token-plan-cn.xiaomimimo.com/v1",
        "temperature": 0.3,
        "max_tokens": LLM_CONTEXT_TOKEN_LIMIT,
        "request_timeout_sec": 360.0,
        "enable_thinking": False,
        "concurrency": 1,
        "rate_limit_qps": 0.1,
        "rate_limit_burst": 1,
    },
    "deepseek": {
        "model_name": "deepseek-v4-pro",
        "api_key_env_var": "DEEPSEEK_API_KEY",
        "base_url": "https://api.deepseek.com",
        "temperature": 0.3,
        "max_tokens": LLM_CONTEXT_TOKEN_LIMIT,
        "request_timeout_sec": 600.0,
        "enable_thinking": True,
        "concurrency": 128,
        "rate_limit_qps": 80,
        "rate_limit_burst": 160,
        "reasoning_effort": "high",
    },
    "siliconflow": {
        "model_name": "deepseek-ai/DeepSeek-V4-Flash",
        "api_key_env_var": "SILICONFLOW_API_KEY",
        "base_url": "https://api.siliconflow.cn/v1",
        "temperature": 0.3,
        "max_tokens": LLM_CONTEXT_TOKEN_LIMIT,
        "request_timeout_sec": 600.0,
        "enable_thinking": False,
        "concurrency": 64,
        "rate_limit_qps": 8,
        "rate_limit_burst": 8,
    },
}

def get_llm_provider_config(provider: str | None = None) -> Dict[str, Any]:
    selected_provider = str(provider or LLM_PROVIDER).strip().lower()
    selected = LLM_PROVIDER_CONFIGS.get(selected_provider)
    if selected is None:
        raise ValueError(f"Unsupported LLM_PROVIDER: {selected_provider}. Supported providers: {sorted(LLM_PROVIDER_CONFIGS)}")
    return dict(selected)


_SELECTED_LLM_CONFIG = get_llm_provider_config(LLM_PROVIDER)

LLM_MODEL_NAME = _SELECTED_LLM_CONFIG["model_name"]
LLM_API_KEY_ENV_VAR = _SELECTED_LLM_CONFIG["api_key_env_var"]
LLM_BASE_URL = _SELECTED_LLM_CONFIG["base_url"]
LLM_TEMPERATURE = _SELECTED_LLM_CONFIG["temperature"]
LLM_MAX_TOKENS = _SELECTED_LLM_CONFIG["max_tokens"]
LLM_REQUEST_TIMEOUT_SEC = _SELECTED_LLM_CONFIG["request_timeout_sec"]
LLM_ENABLE_THINKING = _SELECTED_LLM_CONFIG["enable_thinking"]
LLM_PROVIDER_CONCURRENCY = _SELECTED_LLM_CONFIG.get("concurrency", 8)
LLM_PROVIDER_RATE_LIMIT_QPS = _SELECTED_LLM_CONFIG.get("rate_limit_qps", 4)
LLM_PROVIDER_RATE_LIMIT_BURST = _SELECTED_LLM_CONFIG.get("rate_limit_burst", 4)
LLM_REASONING_EFFORT = _SELECTED_LLM_CONFIG.get("reasoning_effort", "high")

FILE_LEVEL_FALLBACK_ENABLED = True
FILE_LEVEL_FALLBACK_PATTERNS = [
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
STEP10_PR_METADATA_ENABLED = True
STEP10_PR_METADATA_TOKEN_ENV = "GITHUB_TOKEN"
PHASE3_LLM_SHORT_HASH_MIN_LENGTH = 7
PHASE3_VALUE_BATCH_SIZE = 8
PHASE3_SLOT_ENTRY_GROUP_BATCH_SIZE = 40
PHASE3_ARCH_LABEL_ENTRY_BATCH_SIZE = 8
PHASE3_GROUP_REVIEW_BATCH_SIZE = 10
PHASE3_FINAL_COMPOSITION_FALLBACK_ON_COVERAGE_FAILURE = True
PHASE3_ARCH_MODULE_ASSIGNMENT_ENABLED = True
PHASE3_ARCH_MODULE_ASSIGNMENT_BATCH_SIZE = 20
PHASE3_ARCH_MODULE_ASSIGNMENT_CONCURRENCY = LLM_PROVIDER_CONCURRENCY
PHASE3_ARCH_MODULE_ASSIGNMENT_PROMPT_PATH = Path("prompts/phase3_2_arch_module_assignment_prompt.txt")
PHASE3_FINAL_COMPOSITION_BATCH_SIZE = 25
PHASE3_FINAL_COMPOSITION_CONCURRENCY = LLM_PROVIDER_CONCURRENCY
PHASE3_FINAL_OVERVIEW_PROMPT_PATH = Path("prompts/phase3_final_overview_prompt.txt")
PHASE3_LOW_PRIORITY_ROUTING_BATCH_SIZE = 20
PHASE3_LOW_PRIORITY_ROUTING_CONCURRENCY = min(int(LLM_PROVIDER_CONCURRENCY), 8)
PHASE3_LOW_PRIORITY_ROUTING_CANDIDATE_LIMIT = 80
PHASE3_LOW_PRIORITY_BRIEF_BATCH_SIZE = 20
PHASE3_LOW_PRIORITY_BRIEF_CONCURRENCY = min(int(LLM_PROVIDER_CONCURRENCY), 8)
PHASE2_LLM_ARCH_RELEVANCE_ENABLED = True
PHASE2_LLM_EVENT_PROFILE_ENABLED = True
LLM_OUTPUT_VALIDATION_MAX_RETRIES = 2
PHASE2_ABLATION_MODE = "full"  # "full" | "no_phase2_arch_relevance" | "summary_diff_only"
PHASE2_LLM_PROMPT_PATH = Path("prompts/phase2_arch_relevance_classification_prompt.txt")
PHASE2_SUMMARY_DIFF_ONLY_PROMPT_PATH = Path("prompts/phase2_arch_relevance_summary_diff_only_prompt.txt")
PHASE2_EVENT_PROFILE_PROMPT_PATH = Path("prompts/phase2_arch_event_profile_prompt.txt")
PHASE3_ARCH_LABEL_LLM_ENABLED = True
PHASE3_ARCH_LABEL_PROMPT_PATH = Path("prompts/phase3_2_arch_label_decision_prompt.txt")
PHASE3_IMPORTANT_GROUPING_MODE = "component"  # "component" | "slot" | "flat"

def apply_llm_config(config: PipelineConfig) -> PipelineConfig:
    config.llm_provider = LLM_PROVIDER
    config.llm_model_name = LLM_MODEL_NAME
    config.llm_api_key_env_var = LLM_API_KEY_ENV_VAR
    config.llm_base_url = LLM_BASE_URL
    config.llm_temperature = LLM_TEMPERATURE
    config.llm_max_tokens = LLM_MAX_TOKENS
    config.llm_context_token_limit = LLM_CONTEXT_TOKEN_LIMIT
    config.llm_request_timeout_sec = LLM_REQUEST_TIMEOUT_SEC
    config.llm_enable_thinking = LLM_ENABLE_THINKING
    config.llm_reasoning_effort = LLM_REASONING_EFFORT
    config.step10_concurrency = int(LLM_PROVIDER_CONCURRENCY)
    config.step10_rate_limit_qps = LLM_PROVIDER_RATE_LIMIT_QPS
    config.step10_rate_limit_burst = int(LLM_PROVIDER_RATE_LIMIT_BURST)
    config.phase2_llm_concurrency = int(LLM_PROVIDER_CONCURRENCY)
    config.phase3_arch_label_concurrency = int(LLM_PROVIDER_CONCURRENCY)
    config.phase3_slot_concurrency = int(LLM_PROVIDER_CONCURRENCY)
    config.llm_output_validation_max_retries = LLM_OUTPUT_VALIDATION_MAX_RETRIES
    config.file_level_fallback_enabled = FILE_LEVEL_FALLBACK_ENABLED
    config.file_level_fallback_patterns = list(FILE_LEVEL_FALLBACK_PATTERNS)
    config.step10_pr_metadata_enabled = STEP10_PR_METADATA_ENABLED
    config.step10_pr_metadata_token_env = STEP10_PR_METADATA_TOKEN_ENV
    config.phase3_llm_short_hash_min_length = PHASE3_LLM_SHORT_HASH_MIN_LENGTH
    config.phase3_value_batch_size = PHASE3_VALUE_BATCH_SIZE
    config.phase3_slot_entry_group_batch_size = PHASE3_SLOT_ENTRY_GROUP_BATCH_SIZE
    config.phase3_arch_label_entry_batch_size = PHASE3_ARCH_LABEL_ENTRY_BATCH_SIZE
    config.phase3_group_review_batch_size = PHASE3_GROUP_REVIEW_BATCH_SIZE
    config.phase3_final_composition_fallback_on_coverage_failure = PHASE3_FINAL_COMPOSITION_FALLBACK_ON_COVERAGE_FAILURE
    config.phase3_arch_module_assignment_enabled = PHASE3_ARCH_MODULE_ASSIGNMENT_ENABLED
    config.phase3_arch_module_assignment_batch_size = PHASE3_ARCH_MODULE_ASSIGNMENT_BATCH_SIZE
    config.phase3_arch_module_assignment_concurrency = int(PHASE3_ARCH_MODULE_ASSIGNMENT_CONCURRENCY)
    config.phase3_arch_module_assignment_prompt_path = PHASE3_ARCH_MODULE_ASSIGNMENT_PROMPT_PATH
    config.phase3_final_composition_batch_size = PHASE3_FINAL_COMPOSITION_BATCH_SIZE
    config.phase3_final_composition_concurrency = int(PHASE3_FINAL_COMPOSITION_CONCURRENCY)
    config.phase3_final_overview_prompt_path = PHASE3_FINAL_OVERVIEW_PROMPT_PATH
    config.phase3_low_priority_routing_batch_size = PHASE3_LOW_PRIORITY_ROUTING_BATCH_SIZE
    config.phase3_low_priority_routing_concurrency = int(PHASE3_LOW_PRIORITY_ROUTING_CONCURRENCY)
    config.phase3_low_priority_routing_candidate_limit = int(PHASE3_LOW_PRIORITY_ROUTING_CANDIDATE_LIMIT)
    config.phase3_low_priority_brief_batch_size = PHASE3_LOW_PRIORITY_BRIEF_BATCH_SIZE
    config.phase3_low_priority_brief_concurrency = int(PHASE3_LOW_PRIORITY_BRIEF_CONCURRENCY)
    config.phase2_llm_arch_relevance_enabled = PHASE2_LLM_ARCH_RELEVANCE_ENABLED
    config.phase2_llm_event_profile_enabled = PHASE2_LLM_EVENT_PROFILE_ENABLED
    config.phase2_ablation_mode = PHASE2_ABLATION_MODE
    config.phase2_llm_prompt_path = PHASE2_LLM_PROMPT_PATH
    config.phase2_summary_diff_only_prompt_path = PHASE2_SUMMARY_DIFF_ONLY_PROMPT_PATH
    config.phase2_event_profile_prompt_path = PHASE2_EVENT_PROFILE_PROMPT_PATH
    config.phase3_arch_label_llm_enabled = PHASE3_ARCH_LABEL_LLM_ENABLED
    config.phase3_arch_label_prompt_path = PHASE3_ARCH_LABEL_PROMPT_PATH
    config.phase3_important_grouping_mode = PHASE3_IMPORTANT_GROUPING_MODE
    return config


def build_llm_thinking_extra_body(config: Any | None = None) -> Dict[str, Any]:
    return build_llm_provider_extra_body(_config_with_default_provider(config))


def resolve_llm_enable_thinking(config: Any | None = None) -> bool:
    return resolve_provider_thinking(config, default=LLM_ENABLE_THINKING)


def _config_with_default_provider(config: Any | None = None) -> Any:
    if config is None:
        from types import SimpleNamespace

        return SimpleNamespace(llm_provider=LLM_PROVIDER, llm_enable_thinking=LLM_ENABLE_THINKING)
    if isinstance(config, bool):
        from types import SimpleNamespace

        return SimpleNamespace(llm_provider=LLM_PROVIDER, llm_enable_thinking=config)
    if not getattr(config, "llm_provider", None):
        try:
            setattr(config, "llm_provider", LLM_PROVIDER)
        except Exception:
            pass
    return config


def _coerce_bool(value: Any) -> bool:
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"1", "true", "yes", "y", "on", "enable", "enabled"}:
            return True
        if normalized in {"0", "false", "no", "n", "off", "disable", "disabled"}:
            return False
    return bool(value)


def build_config() -> PipelineConfig:
    """
    Build the default ArchLog runtime configuration.

    The CLI wrapper in `scripts/run_archlog.py` overrides the repository, version
    pair, output directory, and selected external-tool paths. Edit this function
    only when running the pipeline directly from Python.
    """

    # Basic input and output paths.
    repo_path = Path("repositories/example-project")
    output_dir = Path("outputs/example")

    # Version range.
    base_ref = "v1.0.0"
    new_ref = "v1.1.0"

    # External analysis artifacts.
    external_analysis_enabled = True
    external_analysis_reuse_existing = True
    repo_name = repo_path.name
    enre_output_dir = Path("outputs") / "external_artifacts" / repo_name / "ENRE"
    enre_json_path = enre_output_dir / f"{repo_name}-{new_ref}_out.json"
    semarc_output_dir = Path("outputs") / "external_artifacts" / "semarc_results"
    external_worktree_root = Path("repositories") / ".archlog_worktrees"
    enre_jar_path = Path("third_party") / "ENRE-CPP" / "ENRE-CPP.jar"
    semarc_executable_path = Path("third_party") / "SemArc" / "SemArcArcRN.exe"
    semarc_source_dir = Path("third_party") / "SemArc"

    # Current implementation targets C/C++ repositories.
    language = "cpp"

    # Prompt files.
    system_prompt_path = Path(r"code_changes\prompts\code_change_system.txt")
    user_prompt_path = Path(r"code_changes\prompts\code_change_user.txt")

    # LLM provider configuration.
    llm_provider = LLM_PROVIDER
    llm_model_name = LLM_MODEL_NAME

    llm_api_key_env_var = LLM_API_KEY_ENV_VAR
    llm_base_url = LLM_BASE_URL
    llm_temperature = LLM_TEMPERATURE
    llm_max_tokens = LLM_MAX_TOKENS
    llm_enable_thinking = LLM_ENABLE_THINKING

    # Step 10 request concurrency and retry policy.
    step10_concurrency = 8
    step10_rate_limit_qps = 4
    step10_rate_limit_burst = 4
    step10_retry_max_attempts = 4
    step10_retry_base_delay_sec = 1.0
    step10_retry_max_delay_sec = 12.0
    step10_retry_jitter_ratio = 0.25

    # Pipeline controls.
    save_intermediate = True
    fail_fast = True
    verbose = True

    # Graph context configuration.
    graph_max_hops = 1
    graph_max_nodes = 50
    graph_max_edges = 100
    include_relation_types = ["Call"]

    # Matching thresholds.
    enre_min_score = 0.60
    hunk_method_min_coverage = 0.10

    # Assemble the final PipelineConfig.
    config = PipelineConfig(
        repo_path=repo_path,
        base_ref=base_ref,
        new_ref=new_ref,
        enre_json_path=enre_json_path,
        output_dir=output_dir,
        language=language,
        external_analysis_enabled=external_analysis_enabled,
        external_analysis_reuse_existing=external_analysis_reuse_existing,
        external_worktree_root=external_worktree_root,
        enre_jar_path=enre_jar_path,
        enre_output_dir=enre_output_dir,
        semarc_executable_path=semarc_executable_path,
        semarc_output_dir=semarc_output_dir,
        llm_provider=llm_provider,
        llm_model_name=llm_model_name,
        llm_temperature=llm_temperature,
        llm_max_tokens=llm_max_tokens,
        llm_context_token_limit=LLM_CONTEXT_TOKEN_LIMIT,
        llm_request_timeout_sec=LLM_REQUEST_TIMEOUT_SEC,
        llm_base_url=llm_base_url,
        llm_api_key_env_var=llm_api_key_env_var,
        llm_enable_thinking=llm_enable_thinking,
        debug_fail_fast_on_llm_error=True,
        phase3_debug_fail_fast=True,
        step10_concurrency=step10_concurrency,
        step10_rate_limit_qps=step10_rate_limit_qps,
        step10_rate_limit_burst=step10_rate_limit_burst,
        step10_retry_max_attempts=step10_retry_max_attempts,
        step10_retry_base_delay_sec=step10_retry_base_delay_sec,
        step10_retry_max_delay_sec=step10_retry_max_delay_sec,
        step10_retry_jitter_ratio=step10_retry_jitter_ratio,
        llm_output_validation_max_retries=LLM_OUTPUT_VALIDATION_MAX_RETRIES,
        file_level_fallback_enabled=FILE_LEVEL_FALLBACK_ENABLED,
        file_level_fallback_patterns=list(FILE_LEVEL_FALLBACK_PATTERNS),
        step10_pr_metadata_enabled=STEP10_PR_METADATA_ENABLED,
        step10_pr_metadata_token_env=STEP10_PR_METADATA_TOKEN_ENV,
        phase3_llm_short_hash_min_length=PHASE3_LLM_SHORT_HASH_MIN_LENGTH,
        phase3_value_batch_size=PHASE3_VALUE_BATCH_SIZE,
        phase3_low_priority_routing_batch_size=PHASE3_LOW_PRIORITY_ROUTING_BATCH_SIZE,
        phase3_low_priority_routing_concurrency=PHASE3_LOW_PRIORITY_ROUTING_CONCURRENCY,
        phase3_low_priority_routing_candidate_limit=PHASE3_LOW_PRIORITY_ROUTING_CANDIDATE_LIMIT,
        phase3_low_priority_brief_batch_size=PHASE3_LOW_PRIORITY_BRIEF_BATCH_SIZE,
        phase3_low_priority_brief_concurrency=PHASE3_LOW_PRIORITY_BRIEF_CONCURRENCY,
        phase2_llm_arch_relevance_enabled=PHASE2_LLM_ARCH_RELEVANCE_ENABLED,
        phase2_llm_event_profile_enabled=PHASE2_LLM_EVENT_PROFILE_ENABLED,
        phase2_llm_concurrency=step10_concurrency,
        phase2_ablation_mode=PHASE2_ABLATION_MODE,
        phase2_llm_prompt_path=PHASE2_LLM_PROMPT_PATH,
        phase2_summary_diff_only_prompt_path=PHASE2_SUMMARY_DIFF_ONLY_PROMPT_PATH,
        phase2_event_profile_prompt_path=PHASE2_EVENT_PROFILE_PROMPT_PATH,
        phase3_arch_label_llm_enabled=PHASE3_ARCH_LABEL_LLM_ENABLED,
        phase3_arch_label_prompt_path=PHASE3_ARCH_LABEL_PROMPT_PATH,
        phase3_arch_label_concurrency=step10_concurrency,
        phase3_important_grouping_mode=PHASE3_IMPORTANT_GROUPING_MODE,
        save_intermediate=save_intermediate,
        fail_fast=fail_fast,
        verbose=verbose,
        prompt=PromptConfig(
            system_prompt_path=system_prompt_path,
            user_prompt_path=user_prompt_path,
        ),
        graph=GraphConfig(
            max_hops=graph_max_hops,
            max_nodes=graph_max_nodes,
            max_edges=graph_max_edges,
            include_relation_types=include_relation_types,
        ),
        matching=MatchingConfig(
            enre_min_score=enre_min_score,
            hunk_method_min_coverage=hunk_method_min_coverage,
        ),
    )

    # Phase 3 uses this optional control for independent slot generation work.
    config.phase3_slot_concurrency = step10_concurrency

    return apply_llm_config(config)
