from __future__ import annotations

from pathlib import Path

# ============================================================
# Basic names
# ============================================================

MODULE_NAME = "code_changes"
PIPELINE_NAME = "ArchLogCodeChangesPipeline"

# ============================================================
# Change types
# ============================================================

CHANGE_TYPE_ADDED = "added"
CHANGE_TYPE_MODIFIED = "modified"
CHANGE_TYPE_DELETED = "deleted"

CHANGE_TYPES = {
    CHANGE_TYPE_ADDED,
    CHANGE_TYPE_MODIFIED,
    CHANGE_TYPE_DELETED,
}

# ============================================================
# C/C++ entity categories (ENRE / internal normalized labels)
# ============================================================

ENTITY_CATEGORY_FILE = "File"
ENTITY_CATEGORY_NAMESPACE = "Namespace"
ENTITY_CATEGORY_CLASS = "Class"
ENTITY_CATEGORY_STRUCT = "Struct"
ENTITY_CATEGORY_UNION = "Union"
ENTITY_CATEGORY_FUNCTION = "Function"
ENTITY_CATEGORY_METHOD = "Method"
ENTITY_CATEGORY_CONSTRUCTOR = "Constructor"
ENTITY_CATEGORY_DESTRUCTOR = "Destructor"
ENTITY_CATEGORY_VARIABLE = "Variable"
ENTITY_CATEGORY_FIELD = "Field"
ENTITY_CATEGORY_ENUM = "Enum"
ENTITY_CATEGORY_ENUM_MEMBER = "EnumMember"
ENTITY_CATEGORY_MACRO = "Macro"

CALLABLE_ENTITY_CATEGORIES = {
    ENTITY_CATEGORY_FUNCTION,
    ENTITY_CATEGORY_METHOD,
    ENTITY_CATEGORY_CONSTRUCTOR,
    ENTITY_CATEGORY_DESTRUCTOR,
}

TYPE_LIKE_ENTITY_CATEGORIES = {
    ENTITY_CATEGORY_CLASS,
    ENTITY_CATEGORY_STRUCT,
    ENTITY_CATEGORY_UNION,
    ENTITY_CATEGORY_ENUM,
}

# ============================================================
# ENRE relation types
# ============================================================

RELATION_CALL = "Call"
RELATION_USE = "Use"
RELATION_DEFINE = "Define"
RELATION_CONTAIN = "Contain"
RELATION_INHERIT = "Inherit"
RELATION_IMPLEMENT = "Implement"
RELATION_OVERRIDE = "Override"
RELATION_IMPORT = "Import"
RELATION_INCLUDE = "Include"

CALL_GRAPH_RELATION_TYPES = {
    RELATION_CALL,
}

DEFAULT_CONTEXT_RELATION_TYPES = {
    RELATION_CALL,
}

# ============================================================
# Change categories for release-note oriented summarization
# ============================================================

CATEGORY_FEATURE = "feature"
CATEGORY_BUGFIX = "bugfix"
CATEGORY_REFACTORING = "refactoring"
CATEGORY_PERFORMANCE = "performance"
CATEGORY_SECURITY = "security"
CATEGORY_COMPATIBILITY = "compatibility"
CATEGORY_MAINTENANCE = "maintenance"
CATEGORY_UNKNOWN = "unknown"

CHANGE_CATEGORIES = {
    CATEGORY_FEATURE,
    CATEGORY_BUGFIX,
    CATEGORY_REFACTORING,
    CATEGORY_PERFORMANCE,
    CATEGORY_SECURITY,
    CATEGORY_COMPATIBILITY,
    CATEGORY_MAINTENANCE,
    CATEGORY_UNKNOWN,
}

COMMIT_KEYWORDS_BUGFIX = {
    "fix",
    "bug",
    "crash",
    "fault",
    "issue",
    "error",
    "correct",
    "repair",
    "resolve",
    "hotfix",
}

COMMIT_KEYWORDS_FEATURE = {
    "add",
    "support",
    "enable",
    "introduce",
    "implement",
    "create",
    "new",
    "feature",
}

COMMIT_KEYWORDS_REFACTORING = {
    "refactor",
    "cleanup",
    "rename",
    "reorganize",
    "restructure",
    "tidy",
    "simplify",
}

COMMIT_KEYWORDS_PERFORMANCE = {
    "optimize",
    "performance",
    "speed",
    "faster",
    "latency",
    "throughput",
    "efficient",
}

COMMIT_KEYWORDS_SECURITY = {
    "security",
    "vulnerability",
    "cve",
    "sanitize",
    "validate",
    "overflow",
    "oob",
    "bounds",
}

# ============================================================
# Matching / scoring defaults
# ============================================================

DEFAULT_PATH_MATCH_WEIGHT = 0.45
DEFAULT_LINE_MATCH_WEIGHT = 0.35
DEFAULT_NAME_MATCH_WEIGHT = 0.20

DEFAULT_ENRE_MATCH_MIN_SCORE = 0.60
DEFAULT_HUNK_METHOD_MIN_COVERAGE = 0.10

DEFAULT_CONTEXT_GRAPH_MAX_HOPS = 1
DEFAULT_CONTEXT_GRAPH_MAX_NODES = 50
DEFAULT_CONTEXT_GRAPH_MAX_EDGES = 100

DEFAULT_TOP_K_EXEMPLARS = 3

# ============================================================
# File names for persisted intermediate artifacts
# ============================================================

FILE_CHANGED_METHODS = "changed_methods.json"
FILE_CHANGED_METHODS_WITH_COMMITS = "changed_methods_with_commits.json"
FILE_CHANGED_METHODS_WITH_ENRE = "changed_methods_with_enre.json"
FILE_METHOD_CONTEXT_GRAPHS = "method_context_graphs.json"
FILE_DIFF_HUNKS = "diff_hunks.json"
FILE_METHOD_HUNK_PAIRS = "method_hunk_pairs.json"
FILE_CHANGE_UNITS = "change_units.json"
FILE_SELECTED_EXEMPLARS = "selected_exemplars.json"
FILE_LLM_PROMPTS = "llm_prompts.json"
FILE_CODE_CHANGE_SUMMARIES = "code_change_summaries.json"
FILE_PIPELINE_REPORT = "pipeline_report.json"

INTERMEDIATE_OUTPUT_FILES = {
    "changed_methods": FILE_CHANGED_METHODS,
    "changed_methods_with_commits": FILE_CHANGED_METHODS_WITH_COMMITS,
    "changed_methods_with_enre": FILE_CHANGED_METHODS_WITH_ENRE,
    "method_context_graphs": FILE_METHOD_CONTEXT_GRAPHS,
    "diff_hunks": FILE_DIFF_HUNKS,
    "method_hunk_pairs": FILE_METHOD_HUNK_PAIRS,
    "change_units": FILE_CHANGE_UNITS,
    "selected_exemplars": FILE_SELECTED_EXEMPLARS,
    "llm_prompts": FILE_LLM_PROMPTS,
    "code_change_summaries": FILE_CODE_CHANGE_SUMMARIES,
    "pipeline_report": FILE_PIPELINE_REPORT,
}

# ============================================================
# Prompt / exemplar defaults
# ============================================================

DEFAULT_PROMPTS_DIRNAME = "prompts"
DEFAULT_EXEMPLARS_DIRNAME = "exemplars"

PROMPT_SYSTEM_FILENAME = "code_change_system.txt"
PROMPT_USER_FILENAME = "code_change_user.txt"

EXEMPLAR_FEATURE_FILENAME = "feature.jsonl"
EXEMPLAR_BUGFIX_FILENAME = "bugfix.jsonl"
EXEMPLAR_REFACTORING_FILENAME = "refactoring.jsonl"

# ============================================================
# Step names
# ============================================================

STEP1_METHOD_CHANGE_LOCALIZER = "step1_method_change_localizer"
STEP2_COMMIT_MAPPER = "step2_commit_mapper"
STEP3_ENRE_ENTITY_MATCHER = "step3_enre_entity_matcher"
STEP4_CALL_SUBGRAPH_BUILDER = "step4_call_subgraph_builder"
STEP5_DIFF_HUNK_EXTRACTOR = "step5_diff_hunk_extractor"
STEP6_HUNK_METHOD_ALIGNER = "step6_hunk_method_aligner"
STEP7_CHANGE_UNIT_BUILDER = "step7_change_unit_builder"
STEP8_PROMPT_BUILDER = "step8_prompt_builder"
STEP9_EXEMPLAR_SELECTOR = "step9_exemplar_selector"
STEP10_CODE_CHANGE_SUMMARIZER = "step10_code_change_summarizer"

PIPELINE_STEP_SEQUENCE = [
    STEP1_METHOD_CHANGE_LOCALIZER,
    STEP2_COMMIT_MAPPER,
    STEP3_ENRE_ENTITY_MATCHER,
    STEP4_CALL_SUBGRAPH_BUILDER,
    STEP5_DIFF_HUNK_EXTRACTOR,
    STEP6_HUNK_METHOD_ALIGNER,
    STEP7_CHANGE_UNIT_BUILDER,
    STEP8_PROMPT_BUILDER,
    STEP9_EXEMPLAR_SELECTOR,
    STEP10_CODE_CHANGE_SUMMARIZER,
]

# ============================================================
# Misc
# ============================================================

UTF8 = "utf-8"
JSON_INDENT = 2

PATCH_HEADER_PREFIX = "@@"
GIT_NULL_TREE_HASH = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"

DEFAULT_LOGGER_NAME = "archlog.code_changes"

# ============================================================
# Utility helpers
# ============================================================

def default_prompts_dir(project_root: Path) -> Path:
    return project_root / DEFAULT_PROMPTS_DIRNAME


def default_exemplars_dir(project_root: Path) -> Path:
    return default_prompts_dir(project_root) / DEFAULT_EXEMPLARS_DIRNAME