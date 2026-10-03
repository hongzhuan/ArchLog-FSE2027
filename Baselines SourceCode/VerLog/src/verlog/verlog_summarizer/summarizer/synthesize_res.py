import os
import argparse
import llm_assistant


def system_message_factory(system_prompt_file):
    with open(system_prompt_file, 'r', encoding='utf-8', errors='replace') as f:
        return f.read()

def should_skip_entry(entry_text):
    stripped = entry_text.strip()
    no_release_note_marker = getattr(llm_assistant.runtime_config, "LLM_NO_RELEASE_NOTE_MARKER", "{}")
    return not stripped or stripped == no_release_note_marker


def split_text_by_lines(text, max_chars):
    chunks = []
    current_lines = []
    current_size = 0

    def flush_current():
        nonlocal current_lines, current_size
        if current_lines:
            chunks.append("".join(current_lines))
            current_lines = []
            current_size = 0

    for line in text.splitlines(keepends=True):
        if len(line) > max_chars:
            flush_current()
            for start in range(0, len(line), max_chars):
                chunks.append(line[start:start + max_chars])
            continue

        if current_lines and current_size + len(line) > max_chars:
            flush_current()

        current_lines.append(line)
        current_size += len(line)

    flush_current()
    return chunks or [text]


def build_synthesis_chunk_prompt(chunk, chunk_index, chunk_count):
    return (
        "The following final VerLog synthesis prompt was too large and has "
        "been split into chunks for engineering reasons.\n"
        f"Chunk: {chunk_index}/{chunk_count}\n\n"
        "Apply the same content-selection and presentation requirements as "
        "the original VerLog synthesis prompt. Keep only end-user-perceivable "
        "changes supported by this chunk. Output a concise bullet list, with "
        "one independent change per bullet. Do not use component/category "
        "headings or component-prefixed buckets. If nothing is "
        "end-user-perceivable, output {}. Only output release notes, no other "
        "explanations.\n\n"
        "Chunk content:\n"
        f"{chunk}"
    )


def build_synthesis_merge_prompt(chunk_summaries):
    numbered_summaries = "\n".join(
        f"{index}. {summary}" for index, summary in enumerate(chunk_summaries, start=1)
    )
    return (
        "The following release-note candidates were generated from chunks of "
        "one large final VerLog synthesis prompt.\n\n"
        "Merge them according to the original VerLog synthesis requirements. "
        "Remove duplicates and entries that are not end-user-perceivable. "
        "Output a concise bullet list, with one independent change per bullet. "
        "Do not use component/category headings or component-prefixed buckets. "
        "Do not pack multiple independent changes into one bullet using "
        "semicolons. If nothing is end-user-perceivable, output {}. Only "
        "output release notes, no other explanations.\n\n"
        "Chunk-level candidates:\n"
        f"{numbered_summaries}\n"
    )


def truncate_prompt_to_limit(prompt, max_chars, context):
    if len(prompt) <= max_chars:
        return prompt
    marker = (
        "\n\n[VerLog omitted the remaining intermediate synthesis content because "
        "the prompt stayed above the configured chunk limit after repeated "
        "compression.]\n"
    )
    keep = max(0, max_chars - len(marker))
    print(
        f"Truncating oversized {context}: {len(prompt)} chars to {max_chars} chars.",
        flush=True,
    )
    return prompt[:keep] + marker


def summarize_large_prompt(prompt, summarizer, prompt_name, depth=0):
    max_chars = int(getattr(llm_assistant.runtime_config, "LLM_PROMPT_CHUNK_MAX_CHARS", 0))
    min_chars = int(getattr(llm_assistant.runtime_config, "LLM_PROMPT_CHUNK_MIN_CHARS", 1000))
    max_rounds = int(getattr(llm_assistant.runtime_config, "LLM_PROMPT_CHUNK_MAX_ROUNDS", 6))
    if max_chars < min_chars or len(prompt) <= max_chars:
        return summarizer.summarize(prompt)
    if depth >= max_rounds:
        return summarizer.summarize(truncate_prompt_to_limit(prompt, max_chars, prompt_name))

    chunk_body_limit = max(min_chars, max_chars - 2500)
    chunks = split_text_by_lines(prompt, chunk_body_limit)
    print(
        f"Splitting large {prompt_name}: {len(prompt)} chars into {len(chunks)} chunk(s).",
        flush=True,
    )

    chunk_summaries = []
    for index, chunk in enumerate(chunks, start=1):
        chunk_prompt = build_synthesis_chunk_prompt(chunk, index, len(chunks))
        summary = summarizer.summarize(chunk_prompt)
        if not should_skip_entry(summary):
            chunk_summaries.append(summary)

    if not chunk_summaries:
        return llm_assistant.runtime_config.LLM_NO_RELEASE_NOTE_MARKER

    merge_prompt = build_synthesis_merge_prompt(chunk_summaries)
    return summarize_large_prompt(merge_prompt, summarizer, f"{prompt_name} merge", depth + 1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir', type=str, required=True)
    parser.add_argument('--model', type=str, required=False, choices=['ChatGPT', 'DeepSeek', 'Qwen', 'SiliconFlow', 'OpenAICompatible'])
    parser.add_argument('--exact-model-name', type=str, default=None)
    parser.add_argument('--commit-messages-file', type=str, required=True)
    parser.add_argument('--system-prompt-file', type=str, required=True)
    parser.add_argument('--output-dir', type=str, required=True)
    parser.add_argument('--translate-zh', action='store_true', default=False)

    args = parser.parse_args()

    input_prompt_dir = args.input_dir
    model_name = args.model
    exact_model_name = args.exact_model_name
    system_prompt_file = args.system_prompt_file
    commit_messages_file = args.commit_messages_file
    output_dir = args.output_dir
    translate_zh = args.translate_zh

    model = llm_assistant.model_factory(model_name)
    system_message = system_message_factory(system_prompt_file)

    synthesize_summarizer = llm_assistant.Summarizer(model, exact_model_name, system_message)

    input_summarization_results = []

    with open(commit_messages_file, 'r', encoding='utf-8', errors='replace') as f:
        commit_messages_list = f.readlines()

    commit_messages = []
    seen_commit_messages = set()
    for line in commit_messages_list:
        message = line.strip().lstrip('\ufeff')
        if not message or message in seen_commit_messages:
            continue
        seen_commit_messages.add(message)
        commit_messages.append(message)

    for i, input_prompt_file in enumerate(sorted(os.listdir(input_prompt_dir)), start=1):
        with open(f'{input_prompt_dir}/{input_prompt_file}', 'r', encoding='utf-8', errors='replace') as f:
            input_summarization_result = f.read().strip()
            if should_skip_entry(input_summarization_result):
                continue
            input_summarization_results.append(f'{i}.\t{input_summarization_result}')

    input_summarization_prompt = "Commit Messages:\n" + '\n'.join(commit_messages) + '\n\n'    
    input_summarization_prompt += "Generated Release Notes Entry:\n" + '\n'.join(input_summarization_results)

    synthesize_result = summarize_large_prompt(
        input_summarization_prompt,
        synthesize_summarizer,
        "final synthesis prompt",
    )

    output_file = f'{output_dir}/release_note.{model_name}.txt'

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(synthesize_result)

    if translate_zh:
        translate_system_message = (
            "You are a professional software release note translator. "
            "Translate English release notes into concise Simplified Chinese. "
            "Preserve bullet structure and technical product names. Output only Chinese release notes."
        )
        translate_prompt = (
            "Translate the following English release notes into Simplified Chinese:\n\n"
            f"{synthesize_result}"
        )
        zh_result = llm_assistant.raw_response_with_empty_retries(
            model,
            translate_prompt,
            translate_system_message,
            exact_model_name,
            "Chinese release-note translation",
        )
        zh_output_file = f'{output_dir}/release_note.{model_name}.zh.txt'
        with open(zh_output_file, 'w', encoding='utf-8') as f:
            f.write(zh_result)

        bilingual_output_file = f'{output_dir}/release_note.{model_name}.bilingual.txt'
        with open(bilingual_output_file, 'w', encoding='utf-8') as f:
            f.write("# English\n")
            f.write(synthesize_result.strip())
            f.write("\n\n# Chinese\n")
            f.write(zh_result.strip())
            f.write("\n")
