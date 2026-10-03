import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SUMMARIZER_DIR = BASE_DIR / "verlog" / "verlog_summarizer"

def env_value(*names: str) -> str | None:
    for name in names:
        value = os.environ.get(name)
        if value:
            return value
    return None


# Configure provider endpoint, model, and API key source here.
# Keep api_key as an environment lookup by default so secrets are not stored in
# this repository. You may replace api_key with a literal string for local tests.
LLM_PROVIDERS = {
    "ChatGPT": {
        "model_name": "gpt-4o-mini",
        "base_url": None,
        "api_key": env_value("OPENAI_API_KEY"),
        "api_key_env": "OPENAI_API_KEY",
    },
    "DeepSeek": {
        "model_name": "deepseek-v4-flash",
        "base_url": "https://api.deepseek.com",
        "api_key": env_value("DEEPSEEK_API_KEY"),
        "api_key_env": "DEEPSEEK_API_KEY",
    },
    "Qwen": {
        "model_name": "qwen3.5-flash",
        "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "api_key": env_value("DASHSCOPE_API_KEY", "QWEN_API_KEY"),
        "api_key_env": "DASHSCOPE_API_KEY or QWEN_API_KEY",
        "extra_body": {"enable_thinking": False},
    },
    "SiliconFlow": {
        "model_name": "deepseek-ai/DeepSeek-V4-Flash",
        "base_url": "https://api.siliconflow.cn/v1",
        "api_key": env_value("SILICONFLOW_API_KEY"),
        "api_key_env": "SILICONFLOW_API_KEY",
    },
    "OpenAICompatible": {
        "model_name": env_value("VERLOG_LLM_MODEL") or "gpt-4o-mini",
        "base_url": env_value("VERLOG_LLM_BASE_URL"),
        "api_key": env_value("VERLOG_LLM_API_KEY"),
        "api_key_env": "VERLOG_LLM_API_KEY",
    },
}


# Provider names: ChatGPT, DeepSeek, Qwen, SiliconFlow, OpenAICompatible.
LLM_MODEL = "SiliconFlow"

# Kept for command-line defaults and backward readability. Normally this is
# derived from LLM_PROVIDERS[LLM_MODEL]["model_name"].
LLM_EXACT_MODEL_NAME = LLM_PROVIDERS[LLM_MODEL]["model_name"]

# Number of independent prompt summarization requests to run at once.
LLM_CONCURRENCY = 32

# Retry transient LLM API failures such as 429 burst-rate and 5xx errors.
LLM_MAX_RETRIES = 8
LLM_RETRY_BASE_SECONDS = 5.0
LLM_RETRY_MAX_SECONDS = 90.0
LLM_RETRY_JITTER_SECONDS = 3.0

# Retry model responses that are syntactically successful but empty after
# VerLog's summary extraction. This does not retry the valid no-op marker "{}".
LLM_EMPTY_RESPONSE_MAX_RETRIES = int(os.environ.get("VERLOG_LLM_EMPTY_RESPONSE_MAX_RETRIES", "3"))

# Large CMG/function-cluster prompts are summarized in chunks before the
# per-prompt release-note entry is merged. Keep this below provider context and
# TPM limits; 60k characters is roughly 15k English/code tokens.
LLM_PROMPT_CHUNK_MAX_CHARS = int(os.environ.get("VERLOG_LLM_PROMPT_CHUNK_MAX_CHARS", "60000"))
LLM_PROMPT_CHUNK_MIN_CHARS = 1000
LLM_PROMPT_CHUNK_MAX_ROUNDS = int(os.environ.get("VERLOG_LLM_PROMPT_CHUNK_MAX_ROUNDS", "6"))
LLM_NO_RELEASE_NOTE_MARKER = "{}"

# Prompt generation keeps the original VerLog behavior by default. Set this to a
# positive value or pass --max-commit-messages to reduce very large version pairs
# where thousands of commit subjects would otherwise be repeated in every CMG.
PROMPT_MAX_COMMIT_MESSAGES = int(os.environ.get("VERLOG_PROMPT_MAX_COMMIT_MESSAGES", "0"))

# Final synthesis is always generated in English first; this toggles the
# follow-up Chinese translation.
TRANSLATE_ZH = True

SYSTEM_PROMPT_FILE = SUMMARIZER_DIR / "assets" / "system_prompt_cpp.txt"
SYNTHESIS_SYSTEM_PROMPT_FILE = (
    SUMMARIZER_DIR / "assets" / "example_system_prompt_synthesize_cpp.txt"
)
