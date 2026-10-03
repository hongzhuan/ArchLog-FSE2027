from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional, Sequence

import config as runtime_config


SRC_DIR = Path(__file__).resolve().parent
SUMMARIZER_DIR = SRC_DIR / "verlog" / "verlog_summarizer"
DEFAULT_ARCRN_ENRE_JAR = SRC_DIR / "third_party_tools" / "ENRE-CPP.jar"
SUPPORTED_MODELS = ["ChatGPT", "DeepSeek", "Qwen", "SiliconFlow", "OpenAICompatible"]
SUPPORTED_CONTEXT_MODES = ["callee", "callers-callees", "full"]

sys.path.insert(0, str(SUMMARIZER_DIR))

from prompt_generator.cpp_diff_generator import generate_cpp_diff  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run VerLog for C/C++ projects with ENRE-CPP and VerLog-style CMG prompts."
    )
    parser.add_argument("--git-repo", required=True, type=Path, help="Path to the Git repository.")
    parser.add_argument("--ref-version", required=True, help="Base release tag/ref.")
    parser.add_argument("--tgt-version", required=True, help="Target release tag/ref.")
    parser.add_argument("--project-name", default=None, help="Short project name. Defaults to repo folder name.")
    parser.add_argument("--app-description", default="", help="Project description used in prompts.")
    parser.add_argument("--output-dir", required=True, type=Path, help="Output directory.")
    parser.add_argument("--java", default="java", help="Java executable.")
    parser.add_argument("--enre-jar-source", type=Path, default=DEFAULT_ARCRN_ENRE_JAR)
    parser.add_argument("--enre-jar", type=Path, default=SRC_DIR / "third_party_tools" / "ENRE-CPP.jar")
    parser.add_argument("--ref-enre-json", type=Path, default=None, help="Existing ENRE-CPP JSON for the base version.")
    parser.add_argument("--tgt-enre-json", type=Path, default=None, help="Existing ENRE-CPP JSON for the target version.")
    parser.add_argument("--worktree-dir", type=Path, default=None)
    parser.add_argument("--force-enre", action="store_true", default=False, help="Rerun ENRE even if JSON exists.")
    parser.add_argument(
        "--context-mode",
        default="full",
        choices=SUPPORTED_CONTEXT_MODES,
        help="C/C++ dependency context used in CMG prompts.",
    )
    parser.add_argument("--model", default=runtime_config.LLM_MODEL, choices=SUPPORTED_MODELS)
    parser.add_argument(
        "--exact-model-name",
        default=None,
        help="Concrete provider model name. Defaults to the selected provider's model_name in src/config.py.",
    )
    parser.add_argument(
        "--llm-concurrency",
        type=int,
        default=runtime_config.LLM_CONCURRENCY,
        help="Number of independent prompt summarization requests to run concurrently.",
    )
    parser.add_argument(
        "--max-commit-messages",
        type=int,
        default=runtime_config.PROMPT_MAX_COMMIT_MESSAGES,
        help="Maximum number of commit messages injected into each generated prompt. 0 keeps all messages.",
    )
    parser.add_argument(
        "--system-prompt-file",
        type=Path,
        default=Path(runtime_config.SYSTEM_PROMPT_FILE),
    )
    parser.add_argument(
        "--synthesis-system-prompt-file",
        type=Path,
        default=Path(runtime_config.SYNTHESIS_SYSTEM_PROMPT_FILE),
    )
    parser.add_argument("--skip-llm", action="store_true", default=False, help="Stop after generating prompts.")
    parser.add_argument(
        "--llm-only",
        action="store_true",
        default=False,
        help="Reuse existing prompts and commit messages in output-dir; skip ENRE, diff, and prompt generation.",
    )
    parser.add_argument(
        "--translate-zh",
        dest="translate_zh",
        action="store_true",
        default=runtime_config.TRANSLATE_ZH,
        help="Generate a Simplified Chinese translation after the English release note.",
    )
    parser.add_argument(
        "--no-translate-zh",
        dest="translate_zh",
        action="store_false",
        help="Disable Simplified Chinese translation.",
    )
    args = parser.parse_args()

    if args.llm_concurrency < 1:
        raise SystemExit("--llm-concurrency must be at least 1.")
    if args.max_commit_messages < 0:
        raise SystemExit("--max-commit-messages must be 0 or a positive integer.")
    args.exact_model_name = resolve_configured_model_name(args.model, args.exact_model_name)

    repo_path = args.git_repo.resolve()
    if not repo_path.exists():
        raise SystemExit(f"Repository does not exist: {repo_path}")

    project_name = args.project_name or repo_path.name
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.skip_llm and args.llm_only:
        raise SystemExit("--skip-llm and --llm-only cannot be used together.")

    if args.llm_only:
        run_llm_only(output_dir, project_name, args)
        return

    enre_output_dir = output_dir / "enre"
    enre_output_dir.mkdir(parents=True, exist_ok=True)

    ref_enre_json = (
        resolve_existing_file(args.ref_enre_json, "base ENRE-CPP JSON")
        if args.ref_enre_json is not None
        else None
    )
    tgt_enre_json = (
        resolve_existing_file(args.tgt_enre_json, "target ENRE-CPP JSON")
        if args.tgt_enre_json is not None
        else None
    )
    if ref_enre_json is not None:
        print(f"Using existing base ENRE output: {ref_enre_json}")
    if tgt_enre_json is not None:
        print(f"Using existing target ENRE output: {tgt_enre_json}")

    if ref_enre_json is None or tgt_enre_json is None:
        enre_jar = ensure_enre_jar(args.enre_jar.resolve(), args.enre_jar_source.resolve())
        worktree_root = (
            args.worktree_dir.resolve()
            if args.worktree_dir is not None
            else output_dir / "worktrees"
        )
        if ref_enre_json is None:
            ref_worktree = ensure_worktree(
                repo_path,
                args.ref_version,
                worktree_root,
                f"{project_name}-{args.ref_version}",
            )
            ref_enre_json = run_enre_cpp(
                java_executable=args.java,
                enre_jar=enre_jar,
                source_dir=ref_worktree,
                project_version_name=f"{project_name}-{args.ref_version}",
                output_dir=enre_output_dir,
                force=args.force_enre,
            )
        if tgt_enre_json is None:
            tgt_worktree = ensure_worktree(
                repo_path,
                args.tgt_version,
                worktree_root,
                f"{project_name}-{args.tgt_version}",
            )
            tgt_enre_json = run_enre_cpp(
                java_executable=args.java,
                enre_jar=enre_jar,
                source_dir=tgt_worktree,
                project_version_name=f"{project_name}-{args.tgt_version}",
                output_dir=enre_output_dir,
                force=args.force_enre,
            )

    diff_output_dir = output_dir / "diff_results"
    diff_file = diff_output_dir / f"{project_name}-{args.ref_version}-{args.tgt_version}-diff.json"
    print(f"Generating C/C++ VerLog diff: {diff_file}")
    generate_cpp_diff(
        repo_path=repo_path,
        ref_version=args.ref_version,
        tgt_version=args.tgt_version,
        ref_enre_json=ref_enre_json,
        tgt_enre_json=tgt_enre_json,
        output_path=diff_file,
        context_mode=args.context_mode,
    )

    commit_messages_dir = output_dir / "commit_messages"
    commit_messages_dir.mkdir(parents=True, exist_ok=True)
    commit_messages_file = commit_messages_dir / f"{project_name}-{args.ref_version}-{args.tgt_version}.txt"
    commit_messages_file.write_text(
        run_git(repo_path, ["log", "--pretty=format:%s", f"{args.ref_version}..{args.tgt_version}"]),
        encoding="utf-8",
    )

    prompt_output_dir = output_dir / "prompts"
    prompt_output_dir.mkdir(parents=True, exist_ok=True)
    run_command(
        [
            sys.executable,
            "verlog/verlog_summarizer/verlog.py",
            "parse",
            "--input",
            str(diff_file),
            "--ref-release-tag",
            args.ref_version,
            "--tgt-release-tag",
            args.tgt_version,
            "--repo-path",
            str(repo_path),
            "--app-description",
            args.app_description,
            "--commit-messages-file",
            str(commit_messages_file),
            "--reduce_prompts",
            "--max-commit-messages",
            str(args.max_commit_messages),
            "--output-dir",
            str(prompt_output_dir),
        ],
        cwd=SRC_DIR,
    )

    if args.skip_llm:
        print("LLM steps skipped.")
        print(f"Diff JSON: {diff_file}")
        print(f"Prompts: {prompt_output_dir}")
        return

    rn_entries_dir = output_dir / "rn_entries"
    rn_entries_dir.mkdir(parents=True, exist_ok=True)
    run_prompt_summarizations(sorted(prompt_output_dir.glob("*.prompt")), args, rn_entries_dir)

    synthesize_cmd = [
        sys.executable,
        "verlog/verlog_summarizer/summarizer/synthesize_res.py",
        "--input-dir",
        str(rn_entries_dir),
        "--model",
        args.model,
        "--exact-model-name",
        args.exact_model_name,
        "--commit-messages-file",
        str(commit_messages_file),
        "--system-prompt-file",
        str(args.synthesis_system_prompt_file),
        "--output-dir",
        str(output_dir),
    ]
    if args.translate_zh:
        synthesize_cmd.append("--translate-zh")
    run_command(synthesize_cmd, cwd=SRC_DIR)

    print(f"English release note: {output_dir / ('release_note.' + args.model + '.txt')}")
    if args.translate_zh:
        print(f"Chinese release note: {output_dir / ('release_note.' + args.model + '.zh.txt')}")
        print(f"Bilingual release note: {output_dir / ('release_note.' + args.model + '.bilingual.txt')}")


def build_summarize_command(prompt_file: Path, args: argparse.Namespace, rn_entries_dir: Path) -> list[str]:
    return [
        sys.executable,
        "verlog/verlog_summarizer/verlog.py",
        "summarize",
        "--input-prompt-file",
        str(prompt_file),
        "--model",
        args.model,
        "--exact-model-name",
        args.exact_model_name,
        "--system-prompt-file",
        str(args.system_prompt_file),
        "--output-dir",
        str(rn_entries_dir),
    ]


def run_llm_only(output_dir: Path, project_name: str, args: argparse.Namespace) -> None:
    prompt_output_dir = output_dir / "prompts"
    if not prompt_output_dir.is_dir():
        raise SystemExit(f"--llm-only requires an existing prompts directory: {prompt_output_dir}")
    prompt_files = sorted(prompt_output_dir.glob("*.prompt"))
    if not prompt_files:
        raise SystemExit(f"--llm-only found no prompt files in: {prompt_output_dir}")

    commit_messages_file = find_commit_messages_file(
        output_dir,
        project_name,
        args.ref_version,
        args.tgt_version,
    )

    rn_entries_dir = output_dir / "rn_entries"
    rn_entries_dir.mkdir(parents=True, exist_ok=True)
    run_prompt_summarizations(prompt_files, args, rn_entries_dir)

    synthesize_cmd = [
        sys.executable,
        "verlog/verlog_summarizer/summarizer/synthesize_res.py",
        "--input-dir",
        str(rn_entries_dir),
        "--model",
        args.model,
        "--exact-model-name",
        args.exact_model_name,
        "--commit-messages-file",
        str(commit_messages_file),
        "--system-prompt-file",
        str(args.synthesis_system_prompt_file),
        "--output-dir",
        str(output_dir),
    ]
    if args.translate_zh:
        synthesize_cmd.append("--translate-zh")
    run_command(synthesize_cmd, cwd=SRC_DIR)

    print(f"English release note: {output_dir / ('release_note.' + args.model + '.txt')}")
    if args.translate_zh:
        print(f"Chinese release note: {output_dir / ('release_note.' + args.model + '.zh.txt')}")
        print(f"Bilingual release note: {output_dir / ('release_note.' + args.model + '.bilingual.txt')}")


def find_commit_messages_file(output_dir: Path, project_name: str, ref_version: str, tgt_version: str) -> Path:
    commit_messages_dir = output_dir / "commit_messages"
    expected = commit_messages_dir / f"{project_name}-{ref_version}-{tgt_version}.txt"
    if expected.is_file():
        return expected

    candidates = sorted(commit_messages_dir.glob("*.txt")) if commit_messages_dir.is_dir() else []
    if len(candidates) == 1:
        return candidates[0]
    if not candidates:
        raise SystemExit(f"--llm-only requires an existing commit messages file under: {commit_messages_dir}")
    raise SystemExit(
        "--llm-only found multiple commit messages files; expected "
        f"{expected}, candidates: {', '.join(str(path) for path in candidates)}"
    )


def resolve_configured_model_name(provider_name: str, exact_model_name: Optional[str]) -> str:
    provider_config = runtime_config.LLM_PROVIDERS.get(provider_name)
    if provider_config is None:
        raise SystemExit(f"LLM provider is not configured in src/config.py: {provider_name}")
    if provider_name == "DeepSeek" and exact_model_name in (None, "", "chat"):
        return str(provider_config["model_name"])
    if exact_model_name:
        return exact_model_name
    model_name = provider_config.get("model_name")
    if not model_name:
        raise SystemExit(f"model_name is missing for {provider_name} in src/config.py.")
    return str(model_name)


def run_prompt_summarizations(
    prompt_files: Sequence[Path],
    args: argparse.Namespace,
    rn_entries_dir: Path,
) -> None:
    jobs = []
    for prompt_file in prompt_files:
        output_file = rn_entries_dir / f"{prompt_file.name}.{args.model}"
        if is_non_empty_file(output_file):
            print(f"Skipping existing release-note entry: {output_file}")
            continue
        if output_file.exists():
            print(f"Removing empty or incomplete release-note entry: {output_file}")
            output_file.unlink()
        jobs.append(prompt_file)

    if not jobs:
        print("All prompt-level release-note entries already exist.")
        return

    concurrency = min(args.llm_concurrency, len(jobs))
    print(f"Running {len(jobs)} prompt-level LLM job(s) with concurrency={concurrency}.")

    if concurrency == 1:
        for index, prompt_file in enumerate(jobs, start=1):
            print(f"LLM prompt progress {index}/{len(jobs)}: {prompt_file.name}")
            run_command(build_summarize_command(prompt_file, args, rn_entries_dir), cwd=SRC_DIR)
        return

    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        future_to_prompt = {
            executor.submit(
                run_command,
                build_summarize_command(prompt_file, args, rn_entries_dir),
                SRC_DIR,
                True,
            ): prompt_file
            for prompt_file in jobs
        }
        for index, future in enumerate(as_completed(future_to_prompt), start=1):
            prompt_file = future_to_prompt[future]
            try:
                future.result()
            except Exception as exc:
                raise RuntimeError(f"LLM summarization failed for prompt: {prompt_file}") from exc
            print(f"LLM prompt progress {index}/{len(jobs)}: {prompt_file.name}")


def is_non_empty_file(path: Path) -> bool:
    return path.is_file() and path.stat().st_size > 0


def resolve_existing_file(path: Path, description: str) -> Path:
    resolved = path.resolve()
    if not resolved.exists():
        raise SystemExit(f"{description} does not exist: {resolved}")
    if not resolved.is_file():
        raise SystemExit(f"{description} is not a file: {resolved}")
    return resolved


def ensure_enre_jar(target: Path, source: Path) -> Path:
    if target.exists():
        return target
    if not source.exists():
        raise SystemExit(f"ENRE-CPP.jar not found at target or source: {target}, {source}")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    print(f"Copied ENRE-CPP.jar to {target}")
    return target


def ensure_worktree(repo_path: Path, ref: str, root: Path, label: str) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    expected_head = run_git(repo_path, ["rev-parse", f"{ref}^{{commit}}"]).strip()
    base = root / sanitize_path_name(label)

    candidate = base
    index = 1
    while candidate.exists():
        if is_git_worktree_at_ref(candidate, expected_head):
            return candidate
        candidate = root / f"{sanitize_path_name(label)}-{index}"
        index += 1

    run_command(["git", "worktree", "add", "--detach", str(candidate), ref], cwd=repo_path)
    return candidate


def is_git_worktree_at_ref(path: Path, expected_head: str) -> bool:
    try:
        actual_head = run_git(path, ["rev-parse", "HEAD"]).strip()
        return actual_head == expected_head
    except Exception:
        return False


def run_enre_cpp(
    *,
    java_executable: str,
    enre_jar: Path,
    source_dir: Path,
    project_version_name: str,
    output_dir: Path,
    force: bool,
) -> Path:
    output_name = sanitize_path_name(project_version_name)
    output_path = output_dir / f"{output_name}_out.json"
    if output_path.exists() and not force:
        print(f"Reusing ENRE output: {output_path}")
        return output_path

    print(f"Running ENRE-CPP for {project_version_name}")
    run_command(
        [
            java_executable,
            "-jar",
            str(enre_jar),
            str(source_dir),
            output_name,
            f"-o={output_dir}",
        ],
        cwd=SRC_DIR,
    )
    if not output_path.exists():
        raise RuntimeError(f"ENRE-CPP did not produce expected output: {output_path}")
    return output_path


def run_git(repo_path: Path, args: Sequence[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=str(repo_path),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Git command failed: git {' '.join(args)}\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    return result.stdout


def run_command(args: Sequence[str], cwd: Path, capture_output: bool = False) -> None:
    print("+ " + " ".join(str(arg) for arg in args))
    output_kwargs = {}
    if capture_output:
        output_kwargs = {
            "stdout": subprocess.PIPE,
            "stderr": subprocess.PIPE,
        }
    result = subprocess.run(
        list(args),
        cwd=str(cwd),
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
        **output_kwargs,
    )
    if result.returncode != 0:
        details = ""
        if capture_output:
            details = f"\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        raise RuntimeError(
            f"Command failed with exit code {result.returncode}: {' '.join(str(arg) for arg in args)}{details}"
        )


def sanitize_path_name(value: str) -> str:
    safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in str(value))
    return safe.strip("._-") or "verlog"


if __name__ == "__main__":
    main()
