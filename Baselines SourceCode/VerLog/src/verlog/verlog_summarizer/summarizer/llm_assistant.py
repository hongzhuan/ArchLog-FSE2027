import random
import sys
import time
from abc import ABC, abstractmethod
from pathlib import Path

from openai import APIConnectionError, APIStatusError, APITimeoutError, OpenAI, RateLimitError


SRC_DIR = Path(__file__).resolve().parents[3]
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import config as runtime_config  # noqa: E402


class LLM(ABC):
    @abstractmethod
    def summarize(self, prompt, system_message, exact_model_name):
        pass


class ChatGPT(LLM):
    def summarize(self, prompt, system_message, exact_model_name):
        return summarize_with_openai_compatible_provider("ChatGPT", prompt, system_message, exact_model_name)

class DeepSeek(LLM):
    def summarize(self, prompt, system_message, exact_model_name='chat'):
        return summarize_with_openai_compatible_provider("DeepSeek", prompt, system_message, exact_model_name)

class Qwen(LLM):
    def summarize(self, prompt, system_message, exact_model_name='qwen-plus'):
        return summarize_with_openai_compatible_provider("Qwen", prompt, system_message, exact_model_name)

class SiliconFlow(LLM):
    def summarize(self, prompt, system_message, exact_model_name='deepseek-ai/DeepSeek-V4-Flash'):
        return summarize_with_openai_compatible_provider("SiliconFlow", prompt, system_message, exact_model_name)

class OpenAICompatible(LLM):
    def summarize(self, prompt, system_message, exact_model_name):
        return summarize_with_openai_compatible_provider("OpenAICompatible", prompt, system_message, exact_model_name)


def get_provider_config(provider_name):
    provider_config = runtime_config.LLM_PROVIDERS.get(provider_name)
    if provider_config is None:
        raise ValueError(f"LLM provider is not configured in src/config.py: {provider_name}")
    return provider_config


def resolve_model_name(provider_name, exact_model_name):
    provider_config = get_provider_config(provider_name)
    if provider_name == "DeepSeek" and exact_model_name in (None, "", "chat"):
        return provider_config.get("model_name")
    return exact_model_name or provider_config.get("model_name")


def summarize_with_openai_compatible_provider(provider_name, prompt, system_message, exact_model_name):
    provider_config = get_provider_config(provider_name)
    api_key = provider_config.get("api_key")
    api_key_env = provider_config.get("api_key_env") or "the configured API key environment variable"
    assert api_key is not None, (
        f"Please set api_key for {provider_name} in src/config.py or set {api_key_env}."
    )

    model_name = resolve_model_name(provider_name, exact_model_name)
    assert model_name is not None, f"Please set model_name for {provider_name} in src/config.py."

    base_url = provider_config.get("base_url")
    if provider_name == "OpenAICompatible":
        assert base_url is not None, "Please set base_url for OpenAICompatible in src/config.py."

    client_kwargs = {"api_key": api_key}
    if base_url:
        client_kwargs["base_url"] = base_url
    client = OpenAI(**client_kwargs)

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]
    request_kwargs = {
        "model": model_name,
        "messages": messages,
        "stream": False,
    }
    extra_body = provider_config.get("extra_body")
    if extra_body is not None:
        request_kwargs["extra_body"] = extra_body

    completion = create_completion_with_retries(client, request_kwargs, provider_config, provider_name)
    return completion.choices[0].message.content


def create_completion_with_retries(client, request_kwargs, provider_config, provider_name):
    max_retries = int(provider_config.get("max_retries", runtime_config.LLM_MAX_RETRIES))
    base_seconds = float(provider_config.get("retry_base_seconds", runtime_config.LLM_RETRY_BASE_SECONDS))
    max_seconds = float(provider_config.get("retry_max_seconds", runtime_config.LLM_RETRY_MAX_SECONDS))
    jitter_seconds = float(provider_config.get("retry_jitter_seconds", runtime_config.LLM_RETRY_JITTER_SECONDS))

    for attempt in range(max_retries + 1):
        try:
            return client.chat.completions.create(**request_kwargs)
        except Exception as exc:
            if attempt >= max_retries or not is_retryable_llm_error(exc):
                raise
            delay = min(max_seconds, base_seconds * (2 ** attempt))
            if jitter_seconds > 0:
                delay += random.uniform(0, jitter_seconds)
            print(
                f"{provider_name} request failed with retryable error; "
                f"retry {attempt + 1}/{max_retries} in {delay:.1f}s: {exc}",
                file=sys.stderr,
                flush=True,
            )
            time.sleep(delay)

    raise RuntimeError("unreachable retry loop exit")


def is_retryable_llm_error(exc):
    if isinstance(exc, (RateLimitError, APIConnectionError, APITimeoutError)):
        return True
    if isinstance(exc, APIStatusError):
        status_code = getattr(exc, "status_code", None)
        return status_code == 429 or (status_code is not None and status_code >= 500)
    status_code = getattr(exc, "status_code", None)
    return status_code == 429 or (status_code is not None and status_code >= 500)


def empty_response_retry_delay(attempt):
    base_seconds = float(getattr(runtime_config, "LLM_RETRY_BASE_SECONDS", 5.0))
    max_seconds = float(getattr(runtime_config, "LLM_RETRY_MAX_SECONDS", 90.0))
    jitter_seconds = float(getattr(runtime_config, "LLM_RETRY_JITTER_SECONDS", 3.0))
    delay = min(max_seconds, base_seconds * (2 ** attempt))
    if jitter_seconds > 0:
        delay += random.uniform(0, jitter_seconds)
    return delay


def is_empty_text(value):
    return value is None or not str(value).strip()


def raw_response_with_empty_retries(model, prompt, system_message, exact_model_name, context):
    max_empty_retries = int(getattr(runtime_config, "LLM_EMPTY_RESPONSE_MAX_RETRIES", 0))

    for attempt in range(max_empty_retries + 1):
        response_message = model.summarize(prompt, system_message, exact_model_name)
        if not is_empty_text(response_message):
            return str(response_message).strip()

        if attempt >= max_empty_retries:
            break

        delay = empty_response_retry_delay(attempt)
        print(
            f"LLM returned an empty response for {context}; "
            f"retry {attempt + 1}/{max_empty_retries} in {delay:.1f}s.",
            file=sys.stderr,
            flush=True,
        )
        time.sleep(delay)

    raise RuntimeError(
        f"LLM returned an empty response for {context} after "
        f"{max_empty_retries + 1} attempt(s)."
    )


def model_factory(model_name):
    # Expand your models here    
    # if model_name == 'LLama3':
    #     return llm_assistant.LLama3()
    # elif model_name == 'Claude':
    #     return llm_assistant.Claude()
    # elif model_name == 'CodeLlama':
    #     return llm_assistant.CodeLlama()
    # elif model_name == 'DeepSeek':
    #     return llm_assistant.DeepSeek()
    # else:
    if model_name == 'DeepSeek':
        return DeepSeek()
    if model_name == 'Qwen':
        return Qwen()
    if model_name == 'SiliconFlow':
        return SiliconFlow()
    if model_name == 'OpenAICompatible':
        return OpenAICompatible()
    return ChatGPT()


class Summarizer:
    def __init__(self, model, exact_model_name, system_message):
        self._model = model
        self._exact_model_name = exact_model_name
        self._system_message = system_message
        self._results = []
        self._synthetic_result = ""

    def set_model(self, model):
        self._model = model

    def __extract_summarization(self, response_message):
        if response_message is None:
            return ""
        # In the response message, the real summarization is within the '{}' brackets
        if '{' not in response_message:
            return response_message
        summarization = response_message.split('{', 1)[1].split('}', 1)[0].strip()
        if not summarization:
            return runtime_config.LLM_NO_RELEASE_NOTE_MARKER
        return summarization

    def summarize(self, prompt):
        max_empty_retries = int(getattr(runtime_config, "LLM_EMPTY_RESPONSE_MAX_RETRIES", 0))

        for attempt in range(max_empty_retries + 1):
            response_message = self._model.summarize(prompt, self._system_message, self._exact_model_name)
            summarization = self.__extract_summarization(response_message)
            if not is_empty_text(summarization):
                summarization = str(summarization).strip()
                self._results.append(summarization)
                return summarization

            if attempt >= max_empty_retries:
                break

            delay = empty_response_retry_delay(attempt)
            print(
                "LLM returned an empty summarization; "
                f"retry {attempt + 1}/{max_empty_retries} in {delay:.1f}s.",
                file=sys.stderr,
                flush=True,
            )
            time.sleep(delay)

        raise RuntimeError(
            "LLM returned an empty summarization after "
            f"{max_empty_retries + 1} attempt(s)."
        )

    def get_summarization_results(self):
        return self._results

    def final_summarization(self, final_prompt):
        self._synthetic_result = raw_response_with_empty_retries(
            self._model,
            final_prompt,
            self._system_message,
            self._exact_model_name,
            "final summarization",
        )
        return self._synthetic_result

    def serialize_results(self, path):
        with open(path, 'w') as f:
            for i, result in enumerate(self._results, start=1):
                f.write(f"Summarization {i}. {result}\n")
        with open(path + ".final", 'w') as f:
            f.write(f"Synthetic Summarization:\n {self._synthetic_result}\n")
