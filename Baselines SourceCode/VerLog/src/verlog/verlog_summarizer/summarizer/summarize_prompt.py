import os
from summarizer import llm_assistant
import sys
from pathlib import Path


SRC_DIR = Path(__file__).resolve().parents[3]
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import config as runtime_config  # noqa: E402

def system_message_factory(system_prompt_file):
    # Add your exemplars here
    with open(system_prompt_file, 'r', encoding='utf-8', errors='replace') as f:
        return f.read()


def is_completed_output(output_file):
    return output_file.is_file() and output_file.stat().st_size > 0


def split_prompt_by_lines(prompt, max_chars):
    chunks = []
    current_lines = []
    current_size = 0

    def flush_current():
        nonlocal current_lines, current_size
        if current_lines:
            chunks.append("".join(current_lines))
            current_lines = []
            current_size = 0

    for line in prompt.splitlines(keepends=True):
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
    return chunks or [prompt]


def build_chunk_prompt(input_prompt_name, chunk, chunk_index, chunk_count):
    return (
        "The following VerLog prompt was too large and has been split into "
        "chunks for engineering reasons.\n"
        f"Prompt file: {input_prompt_name}\n"
        f"Chunk: {chunk_index}/{chunk_count}\n\n"
        "Apply the same task, guidelines, and output requirements as the "
        "original VerLog prompt. Summarize only end-user-perceivable "
        "functionality changes supported by this chunk. If the chunk contains "
        "only refactoring or non-end-user-perceivable changes, output {}. "
        "Output only braces, for example {Fixed ...} or {}.\n\n"
        "Chunk content:\n"
        f"{chunk}"
    )


def build_merge_prompt(input_prompt_name, chunk_summaries):
    numbered_summaries = "\n".join(
        f"{index}. {summary}" for index, summary in enumerate(chunk_summaries, start=1)
    )
    return (
        "The following release-note candidates were generated from chunks of one "
        "large VerLog prompt.\n"
        f"Prompt file: {input_prompt_name}\n\n"
        "Merge them according to the same VerLog output requirement: one or "
        "more single-sentence end-user-perceivable release-note entries inside "
        "braces, or {} if nothing is end-user-perceivable. Remove duplicates "
        "and do not add new information. Output only braces.\n\n"
        "Chunk-level candidates:\n"
        f"{numbered_summaries}\n"
    )


def truncate_prompt_to_limit(prompt, max_chars, context):
    if len(prompt) <= max_chars:
        return prompt
    marker = (
        "\n\n[VerLog omitted the remaining intermediate merge content because "
        "the prompt stayed above the configured chunk limit after repeated "
        "compression.]\n"
    )
    keep = max(0, max_chars - len(marker))
    print(
        f"Truncating oversized {context}: {len(prompt)} chars to {max_chars} chars.",
        flush=True,
    )
    return prompt[:keep] + marker


def is_no_release_note(summary):
    return summary.strip() == runtime_config.LLM_NO_RELEASE_NOTE_MARKER


def require_non_empty_summary(summary, context):
    if summary is None or not str(summary).strip():
        raise RuntimeError(f"LLM returned an empty summarization for {context}.")
    return str(summary).strip()


def summarize_prompt(input_prompt, input_prompt_name, summarizer, depth=0):
    max_chars = int(getattr(runtime_config, "LLM_PROMPT_CHUNK_MAX_CHARS", 0))
    min_chars = int(getattr(runtime_config, "LLM_PROMPT_CHUNK_MIN_CHARS", 1000))
    max_rounds = int(getattr(runtime_config, "LLM_PROMPT_CHUNK_MAX_ROUNDS", 6))
    if max_chars < min_chars or len(input_prompt) <= max_chars:
        return require_non_empty_summary(
            summarizer.summarize(input_prompt),
            input_prompt_name,
        )
    if depth >= max_rounds:
        limited_prompt = truncate_prompt_to_limit(input_prompt, max_chars, input_prompt_name)
        return require_non_empty_summary(
            summarizer.summarize(limited_prompt),
            input_prompt_name,
        )

    chunk_body_limit = max(min_chars, max_chars - 2500)
    chunks = split_prompt_by_lines(input_prompt, chunk_body_limit)
    print(
        f"Splitting large prompt {input_prompt_name}: "
        f"{len(input_prompt)} chars into {len(chunks)} chunk(s).",
        flush=True,
    )

    chunk_summaries = []
    for index, chunk in enumerate(chunks, start=1):
        chunk_prompt = build_chunk_prompt(input_prompt_name, chunk, index, len(chunks))
        summary = require_non_empty_summary(
            summarizer.summarize(chunk_prompt),
            f"{input_prompt_name} chunk {index}/{len(chunks)}",
        )
        if not is_no_release_note(summary):
            chunk_summaries.append(summary)

    if not chunk_summaries:
        return runtime_config.LLM_NO_RELEASE_NOTE_MARKER

    merge_prompt = build_merge_prompt(input_prompt_name, chunk_summaries)
    if len(merge_prompt) > max_chars:
        return summarize_prompt(
            merge_prompt,
            f"{input_prompt_name} chunk merge",
            summarizer,
            depth + 1,
        )

    return require_non_empty_summary(
        summarizer.summarize(merge_prompt),
        f"{input_prompt_name} chunk merge",
    )


def write_non_empty_output(output_file, content):
    content = require_non_empty_summary(content, str(output_file))
    output_file.parent.mkdir(parents=True, exist_ok=True)
    tmp_file = output_file.with_name(f"{output_file.name}.{os.getpid()}.tmp")
    tmp_file.write_text(content, encoding='utf-8')
    os.replace(tmp_file, output_file)


def run(args):
    input_prompt_file = args.input_prompt_file
    model_name = args.model
    exact_model_name = args.exact_model_name
    output_dir = args.output_dir
    system_prompt_file = args.system_prompt_file

    model = llm_assistant.model_factory(model_name)
    system_message = system_message_factory(system_prompt_file)

    input_prompt_name = os.path.basename(input_prompt_file)
    output_file = Path(output_dir) / f'{input_prompt_name}.{model_name}'
    if is_completed_output(output_file):
        print(f'File {output_file} already exists and is non-empty. Skipping.')
        return
    if output_file.exists():
        print(f'Removing empty or incomplete output file: {output_file}')
        output_file.unlink()

    summarizer = llm_assistant.Summarizer(model, exact_model_name, system_message)

    with open(input_prompt_file, 'r', encoding='utf-8', errors='replace') as f:
        input_prompt = f.read()

    summarization_result = summarize_prompt(input_prompt, input_prompt_name, summarizer)
    write_non_empty_output(output_file, summarization_result)
