from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, Mapping, Sequence

from arcrn_output_layout import stage_output_dir
from arcrn_stages.llm_utils import progress_bar_for


PROJECT_ROOT = Path(__file__).resolve().parent
SEMARC_SUFFIXES = ("ArchSem", "CodeSem", "NamedClusters", "ClusterComponent")
SEMARC_CLUSTER_SUFFIXES = ("NamedClusters", "ClusterComponent")
SEMARC_PROGRESS_PREFIX = "@@ARCRN_PROGRESS@@"
SEMARC_SCHEMA_KEYS = (
    "@schemaVersion",
    "@type",
    "Functionality",
    "architecture_pattern",
    "components",
    "content",
    "file",
    "name",
    "nested",
    "structure",
    "summary",
)
SEMARC_SCHEMA_KEY_LOOKUP = {key.lower(): key for key in SEMARC_SCHEMA_KEYS}
KEY_ERROR_PATTERN = re.compile(r"KeyError:\s*['\"]([^'\"]+)['\"]")
MARKDOWN_JSON_BLOCK_PATTERN = re.compile(r"```json\s*(\{.*?\})\s*```", re.IGNORECASE | re.DOTALL)
SEMARC_PHASE_LABELS = {
    "code_files": "file semantics",
    "code_summary": "code summary",
    "arch_semantics": "architecture semantics",
    "embedding": "embedding",
    "clustering": "clustering",
    "module_naming": "module naming",
}


def prepare_external_analysis_inputs(config: Any) -> Dict[str, str]:
    """Generate ENRE and SemArc inputs required by the ArchLog pipeline."""
    repo_path = _resolve_project_path(config.repo_path)
    repo_name = repo_path.name
    base_ref = str(config.base_ref)
    new_ref = str(config.new_ref)

    worktree_root = _resolve_project_path(config.external_worktree_root)
    base_worktree = _ensure_version_worktree(repo_path, base_ref, worktree_root / f"{repo_name}-{base_ref}")
    new_worktree = _ensure_version_worktree(repo_path, new_ref, worktree_root / f"{repo_name}-{new_ref}")

    enre_json_path = _resolve_project_path(config.enre_json_path)
    if not (_reuse_existing(config) and enre_json_path.exists()):
        _run_enre(config, new_worktree, repo_name, new_ref, enre_json_path)

    semarc_root = _resolve_project_path(config.semarc_output_dir)
    generated_base_semarc = _ensure_semarc_result(config, base_worktree, repo_name, base_ref, semarc_root)
    generated_new_semarc = _ensure_semarc_result(config, new_worktree, repo_name, new_ref, semarc_root)

    diff_ir_path = _find_latest_diff_ir(repo_name, base_ref, new_ref)
    if diff_ir_path is None or generated_base_semarc or generated_new_semarc or not _reuse_existing(config):
        diff_progress = progress_bar_for(config, "SemArc architecture diff progress")
        if diff_progress is not None:
            diff_progress.update(completed=0, total=1)
        try:
            diff_ir_path = _run_semarc_diff(config, repo_name, base_ref, new_ref, semarc_root)
            if diff_progress is not None:
                diff_progress.update(completed=1, total=1)
        finally:
            if diff_progress is not None:
                diff_progress.finish()

    outputs = {
        "base_worktree": str(base_worktree),
        "new_worktree": str(new_worktree),
        "enre_json_path": str(enre_json_path),
        "semarc_base_dir": str(_semarc_version_dir(semarc_root, repo_name, base_ref)),
        "semarc_new_dir": str(_semarc_version_dir(semarc_root, repo_name, new_ref)),
        "diff_ir_path": str(diff_ir_path),
    }
    for name, log_path in _external_analysis_log_paths(config, repo_name, base_ref, new_ref).items():
        if log_path.exists():
            outputs[name] = str(log_path)
    return outputs


def check_external_analysis_outputs(config: Any) -> tuple[bool, list[str]]:
    """Check whether all external analysis artifacts exist and are valid.

    Returns ``(complete, missing)`` where *complete* is ``True`` when every
    expected artifact is present and valid, and *missing* lists the names of
    artifacts that need (re-)generation.
    """
    repo_path = _resolve_project_path(config.repo_path)
    repo_name = repo_path.name
    base_ref = str(config.base_ref)
    new_ref = str(config.new_ref)
    missing: list[str] = []

    # --- ENRE ---
    enre_json_path = _resolve_project_path(config.enre_json_path)
    if not enre_json_path.exists():
        missing.append(f"enre:{new_ref}")

    # --- SemArc (base + new) ---
    semarc_root = _resolve_project_path(config.semarc_output_dir)
    for ref in (base_ref, new_ref):
        version_dir = _semarc_version_dir(semarc_root, repo_name, ref)
        project_name = f"{repo_name}-{ref}"
        if not _semarc_core_outputs_are_valid(version_dir, project_name):
            missing.append(f"semarc:{ref}")

    # --- Architecture diff ---
    if _find_latest_diff_ir(repo_name, base_ref, new_ref) is None:
        missing.append("diff_ir")

    return (len(missing) == 0, missing)


def cleanup_external_analysis_outputs(config: Any) -> None:
    """Remove all external analysis artifacts for the given config.

    Removes SemArc results (sema_results), extracted_info, and the
    architecture diff output directory.  ENRE output and git worktrees are
    left intact since they are cheap to reuse.
    """
    repo_path = _resolve_project_path(config.repo_path)
    repo_name = repo_path.name
    base_ref = str(config.base_ref)
    new_ref = str(config.new_ref)
    semarc_root = _resolve_project_path(config.semarc_output_dir)

    # SemArc core outputs for both versions
    for ref in (base_ref, new_ref):
        version_dir = _semarc_version_dir(semarc_root, repo_name, ref)
        project_name = f"{repo_name}-{ref}"
        _remove_semarc_core_outputs(version_dir, project_name)
        # Also remove cluster outputs that may be partial
        _remove_semarc_cluster_outputs(version_dir, project_name)

    # SemArc extracted_info
    tool_dir = _resolve_project_path(config.semarc_executable_path).parent
    extracted = tool_dir / "extracted_info" / f"{repo_name}-{base_ref}"
    if extracted.is_dir():
        import shutil
        shutil.rmtree(extracted)
    extracted = tool_dir / "extracted_info" / f"{repo_name}-{new_ref}"
    if extracted.is_dir():
        import shutil
        shutil.rmtree(extracted)

    # Architecture diff output
    out_root = PROJECT_ROOT / "arch_changes-reports" / "out"
    for directory in out_root.glob(f"{repo_name}_{base_ref}-{new_ref}-*"):
        if directory.is_dir():
            import shutil
            shutil.rmtree(directory)


def _ensure_version_worktree(repo_path: Path, ref: str, target: Path) -> Path:
    repo_path = repo_path.resolve()
    target = target.resolve()
    expected_head = _git_output(repo_path, ["rev-parse", f"{ref}^{{commit}}"])
    if target.exists():
        actual_head = _git_output(target, ["rev-parse", "HEAD"])
        if actual_head != expected_head:
            raise RuntimeError(
                f"Existing analysis worktree is at the wrong revision: {target}. "
                f"Expected {ref} ({expected_head}), found {actual_head}."
            )
        return target

    target.parent.mkdir(parents=True, exist_ok=True)
    _run_command(["git", "-C", str(repo_path), "worktree", "add", "--detach", str(target), ref])
    return target


def _run_enre(config: Any, worktree: Path, repo_name: str, ref: str, expected_output: Path) -> None:
    jar_path = _resolve_project_path(config.enre_jar_path)
    if not jar_path.exists():
        raise FileNotFoundError(f"ENRE JAR not found: {jar_path}")
    output_dir = expected_output.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    project_name = f"{repo_name}-{ref}"
    log_path = _external_analysis_log_paths(config, repo_name, "", ref)["enre_log"]
    source_total = _count_enre_source_files(worktree)
    progress = progress_bar_for(config, f"ENRE-CPP {project_name} progress")
    if progress is not None:
        progress.update(completed=0, total=max(source_total, 1))

    def handle_enre_line(line: str) -> None:
        if progress is None:
            return
        match = re.search(r"\bcount\s*:\s*(\d+)\b", line)
        if match:
            completed = min(int(match.group(1)), max(source_total, 1))
            progress.update(completed=completed, total=max(source_total, 1))

    try:
        _run_command([
            str(getattr(config, "java_executable", "java")),
            "-jar",
            str(jar_path),
            str(worktree),
            project_name,
            f"-o={output_dir}",
        ], log_path=log_path, line_callback=handle_enre_line)
        if progress is not None:
            progress.update(completed=max(source_total, 1), total=max(source_total, 1))
    finally:
        if progress is not None:
            progress.finish()
    if not expected_output.exists():
        raise FileNotFoundError(f"ENRE did not generate expected output: {expected_output}")


def _count_enre_source_files(worktree: Path) -> int:
    suffixes = {".c", ".cc", ".cpp", ".h", ".hpp"}
    ignored_parts = {".git"}
    count = 0
    for path in worktree.rglob("*"):
        if not path.is_file():
            continue
        if any(part in ignored_parts for part in path.parts):
            continue
        if path.suffix.lower() in suffixes:
            count += 1
    return count


def _ensure_semarc_result(config: Any, worktree: Path, repo_name: str, ref: str, semarc_root: Path) -> bool:
    version_dir = _semarc_version_dir(semarc_root, repo_name, ref)
    expected = [version_dir / f"{repo_name}-{ref}_{suffix}.json" for suffix in SEMARC_SUFFIXES]
    project_name = f"{repo_name}-{ref}"
    if _reuse_existing(config) and all(path.exists() for path in expected):
        if _semarc_core_outputs_are_valid(version_dir, project_name):
            return False
        _remove_semarc_core_outputs(version_dir, project_name)

    executable_path = _resolve_project_path(config.semarc_executable_path)
    if not executable_path.exists():
        raise FileNotFoundError(f"Packaged SemArc entrypoint not found: {executable_path}")
    tool_dir = executable_path.parent
    semarc_root.mkdir(parents=True, exist_ok=True)
    log_path = _semarc_log_path(config, repo_name, ref)
    command = [
        str(executable_path),
        str(worktree),
        "--project-name",
        project_name,
        "--output-dir",
        str(semarc_root),
        "--core-outputs-only",
        "--emit-progress",
    ]
    if not _reuse_existing(config):
        command.append("--force")
    progress_display = _SemArcProgressDisplay(config, f"{repo_name}-{ref}")
    run_started_at = time.time()
    try:
        try:
            _run_semarc_command(command, tool_dir, log_path, progress_display)
        except RuntimeError:
            recovered = _recover_semarc_after_failed_run(log_path, version_dir, project_name)
            if not recovered:
                raise
            _remove_semarc_cluster_outputs(version_dir, project_name)
            progress_display.finish()
            retry_command = [part for part in command if part != "--force"]
            _run_semarc_command(retry_command, tool_dir, log_path, progress_display)
    finally:
        progress_display.finish()
    missing = [str(path) for path in expected if not path.exists()]
    if missing:
        raise FileNotFoundError(f"SemArc did not generate expected outputs: {missing}")
    _validate_semarc_core_outputs(version_dir, project_name)
    if not _reuse_existing(config):
        stale = [str(path) for path in expected if path.stat().st_mtime < run_started_at - 1.0]
        if stale:
            raise RuntimeError(f"SemArc left stale outputs after regeneration: {stale}")
    return True


def _run_semarc_command(
    command: Sequence[str],
    tool_dir: Path,
    log_path: Path,
    progress_display: "_SemArcProgressDisplay",
) -> None:
    _run_command(
        command,
        cwd=tool_dir,
        log_path=log_path,
        line_callback=progress_display.consume,
        env=_semarc_subprocess_env(),
    )


def _is_semarc_schema_key_failure(log_path: Path) -> bool:
    if not log_path.exists():
        return False
    log_text = log_path.read_text(encoding="utf-8", errors="replace")
    return any(match.group(1).lower() in SEMARC_SCHEMA_KEY_LOOKUP for match in KEY_ERROR_PATTERN.finditer(log_text))


def _recover_semarc_after_failed_run(log_path: Path, version_dir: Path, project_name: str) -> bool:
    if _is_semarc_schema_key_failure(log_path):
        return _normalize_semarc_json_schema(version_dir, project_name) > 0

    code_sem_path = version_dir / f"{project_name}_CodeSem.json"
    if not _semarc_codesem_needs_recovery(code_sem_path):
        return False
    recovered = _recover_semarc_codesem_from_log(log_path, code_sem_path)
    return recovered > 0


def _semarc_codesem_needs_recovery(code_sem_path: Path) -> bool:
    if not code_sem_path.exists():
        return True
    try:
        data = json.loads(code_sem_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return True
    return len(_semarc_codesem_summary(data)) == 0


def _recover_semarc_codesem_from_log(log_path: Path, code_sem_path: Path) -> int:
    if not log_path.exists():
        return 0
    log_text = log_path.read_text(encoding="utf-8", errors="replace")
    recovered = list(_extract_codesem_summary_items_from_text(log_text))
    if not recovered:
        return 0
    code_sem_path.parent.mkdir(parents=True, exist_ok=True)
    code_sem_path.write_text(
        json.dumps({"summary": recovered}, ensure_ascii=False, indent=4),
        encoding="utf-8",
    )
    return len(recovered)


def _extract_codesem_summary_items_from_text(text: str) -> Iterable[Dict[str, str]]:
    seen_files: set[str] = set()
    for match in MARKDOWN_JSON_BLOCK_PATTERN.finditer(text):
        try:
            payload = json.loads(match.group(1))
        except json.JSONDecodeError:
            continue
        for item in _semarc_codesem_summary(payload):
            file_name = str(item["file"]).strip()
            functionality = str(item["Functionality"]).strip()
            if not file_name or not functionality or file_name in seen_files:
                continue
            seen_files.add(file_name)
            yield {"file": file_name, "Functionality": functionality}


def _normalize_semarc_codesem_functionality_keys(code_sem_path: Path) -> int:
    if not code_sem_path.exists():
        raise FileNotFoundError(f"Cannot normalize missing SemArc CodeSem file: {code_sem_path}")
    data = json.loads(code_sem_path.read_text(encoding="utf-8"))
    changed = _normalize_semarc_schema_keys(data)
    if changed:
        code_sem_path.write_text(json.dumps(data, ensure_ascii=False, indent=4), encoding="utf-8")
    return changed


def _validate_semarc_core_outputs(version_dir: Path, project_name: str) -> None:
    code_sem_path = version_dir / f"{project_name}_CodeSem.json"
    if not code_sem_path.exists():
        raise FileNotFoundError(f"SemArc CodeSem output is missing: {code_sem_path}")
    try:
        code_sem = json.loads(code_sem_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"SemArc CodeSem output is not valid JSON: {code_sem_path}") from exc
    if len(_semarc_codesem_summary(code_sem)) == 0:
        raise ValueError(f"SemArc CodeSem output has empty summary: {code_sem_path}")


def _semarc_core_outputs_are_valid(version_dir: Path, project_name: str) -> bool:
    try:
        _validate_semarc_core_outputs(version_dir, project_name)
    except (FileNotFoundError, ValueError):
        return False
    return True


def _semarc_codesem_summary(data: Any) -> list[Dict[str, Any]]:
    if not isinstance(data, dict):
        return []
    _normalize_semarc_schema_keys(data)
    summary = data.get("summary")
    if not isinstance(summary, list):
        return []
    valid_items = []
    for item in summary:
        if not isinstance(item, dict):
            continue
        file_name = item.get("file")
        functionality = item.get("Functionality")
        if isinstance(file_name, str) and file_name.strip() and isinstance(functionality, str) and functionality.strip():
            valid_items.append(item)
    return valid_items


def _normalize_semarc_json_schema(version_dir: Path, project_name: str) -> int:
    changed = 0
    for suffix in SEMARC_SUFFIXES:
        json_path = version_dir / f"{project_name}_{suffix}.json"
        if not json_path.exists():
            continue
        data = json.loads(json_path.read_text(encoding="utf-8"))
        file_changed = _normalize_semarc_schema_keys(data)
        if file_changed:
            json_path.write_text(json.dumps(data, ensure_ascii=False, indent=4), encoding="utf-8")
            changed += file_changed
    return changed


def _normalize_semarc_schema_keys(value: Any) -> int:
    changed = 0
    if isinstance(value, dict):
        for key in list(value.keys()):
            canonical_key = SEMARC_SCHEMA_KEY_LOOKUP.get(key.lower())
            if canonical_key is not None and key != canonical_key:
                if canonical_key not in value:
                    value[canonical_key] = value[key]
                del value[key]
                changed += 1
        for child in value.values():
            changed += _normalize_semarc_schema_keys(child)
    elif isinstance(value, list):
        for item in value:
            changed += _normalize_semarc_schema_keys(item)
    return changed


def _remove_semarc_cluster_outputs(version_dir: Path, project_name: str) -> None:
    targets = [
        version_dir / f"{project_name}_{suffix}.json"
        for suffix in SEMARC_CLUSTER_SUFFIXES
    ]
    targets.extend([
        version_dir / f"{project_name}_cluster_component_mapping.json",
        version_dir / f"{project_name}_Final.json",
        version_dir / "cluster_result.json",
        version_dir / "cluster_result_named.json",
        version_dir / "cluster_result_pkg.json",
        version_dir / "metrics_our_to_GT.json",
    ])
    _remove_semarc_output_paths(version_dir, targets)


def _remove_semarc_core_outputs(version_dir: Path, project_name: str) -> None:
    targets = [
        version_dir / f"{project_name}_{suffix}.json"
        for suffix in SEMARC_SUFFIXES
    ]
    _remove_semarc_output_paths(version_dir, targets)


def _remove_semarc_output_paths(version_dir: Path, targets: Sequence[Path]) -> None:
    resolved_version_dir = version_dir.resolve()
    for target in targets:
        if not target.exists():
            continue
        resolved_target = target.resolve()
        if resolved_version_dir not in resolved_target.parents:
            raise RuntimeError(f"Refusing to remove SemArc output outside version dir: {resolved_target}")
        resolved_target.unlink()


def _run_semarc_diff(config: Any, repo_name: str, base_ref: str, new_ref: str, semarc_root: Path) -> Path:
    script_path = PROJECT_ROOT / "arch_changes-reports" / "run_diff.py"
    log_path = _external_analysis_log_paths(config, repo_name, base_ref, new_ref)["semarc_diff_log"]
    diff_output_root = PROJECT_ROOT / "outputs" / "external_artifacts" / "arch_diff"
    _run_command([
        str(sys.executable),
        str(script_path),
        "--dir-a",
        str(_semarc_version_dir(semarc_root, repo_name, base_ref)),
        "--dir-b",
        str(_semarc_version_dir(semarc_root, repo_name, new_ref)),
        "--repo-name",
        repo_name,
        "--version-a",
        base_ref,
        "--version-b",
        new_ref,
        "--no-llm",
        "--output-root",
        str(diff_output_root),
    ], cwd=script_path.parent, log_path=log_path)
    generated = _find_latest_diff_ir(repo_name, base_ref, new_ref)
    if generated is None:
        raise FileNotFoundError("SemArc diff did not generate diff_ir-denoised-significance.json")
    return generated


def _find_latest_diff_ir(repo_name: str, base_ref: str, new_ref: str) -> Path | None:
    out_roots = [
        PROJECT_ROOT / "outputs" / "external_artifacts" / "arch_diff",
        PROJECT_ROOT / "arch_changes-reports" / "out",
    ]
    for out_root in out_roots:
        candidates = sorted(out_root.glob(f"{repo_name}_{base_ref}-{new_ref}-*"), reverse=True)
        for directory in candidates:
            path = directory / "diff_ir-denoised-significance.json"
            if path.exists():
                return path
    return None


def _semarc_version_dir(semarc_root: Path, repo_name: str, ref: str) -> Path:
    return semarc_root / f"{repo_name}-{ref}"


def _reuse_existing(config: Any) -> bool:
    return bool(getattr(config, "external_analysis_reuse_existing", True))


def _resolve_project_path(path: Path | str) -> Path:
    resolved = Path(path)
    if not resolved.is_absolute():
        resolved = PROJECT_ROOT / resolved
    return resolved.resolve()


def _external_analysis_log_paths(config: Any, repo_name: str, base_ref: str, new_ref: str) -> Dict[str, Path]:
    output_root = _resolve_project_path(config.output_dir)
    log_dir = stage_output_dir(output_root, "pipeline") / "external_analysis_logs"
    return {
        "enre_log": log_dir / f"enre_{repo_name}-{new_ref}.log",
        "semarc_base_log": log_dir / f"semarc_{repo_name}-{base_ref}.log",
        "semarc_new_log": log_dir / f"semarc_{repo_name}-{new_ref}.log",
        "semarc_diff_log": log_dir / f"semarc_diff_{repo_name}-{base_ref}-{new_ref}.log",
    }


def _semarc_log_path(config: Any, repo_name: str, ref: str) -> Path:
    output_root = _resolve_project_path(config.output_dir)
    log_dir = stage_output_dir(output_root, "pipeline") / "external_analysis_logs"
    return log_dir / f"semarc_{repo_name}-{ref}.log"


def _git_output(repo_path: Path, args: Sequence[str]) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo_path), *args],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return result.stdout.strip()


def _semarc_subprocess_env() -> Dict[str, str]:
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    env["PYTHONIOENCODING"] = "utf-8:replace"
    env["PYTHONLEGACYWINDOWSSTDIO"] = "0"
    env["PYTHONUNBUFFERED"] = "1"
    env["NO_COLOR"] = "1"
    env["TERM"] = "dumb"
    return env


class _SemArcProgressDisplay:
    def __init__(self, config: Any, version_label: str) -> None:
        self._config = config
        self._version_label = version_label
        self._phase: str | None = None
        self._bar = None

    def consume(self, line: str) -> None:
        if not line.startswith(SEMARC_PROGRESS_PREFIX):
            return
        try:
            event = json.loads(line[len(SEMARC_PROGRESS_PREFIX):].strip())
            phase = str(event["phase"])
            completed = int(event["completed"])
            total = int(event["total"])
        except (KeyError, TypeError, ValueError, json.JSONDecodeError):
            return
        if phase != self._phase:
            self.finish()
            stage_label = SEMARC_PHASE_LABELS.get(phase, phase)
            self._bar = progress_bar_for(self._config, f"SemArc {self._version_label} {stage_label} progress")
            self._phase = phase
        if self._bar is not None:
            self._bar.update(completed=completed, total=total)

    def finish(self) -> None:
        if self._bar is not None:
            self._bar.finish()
        self._bar = None
        self._phase = None


def _run_command(
    command: Sequence[str],
    *,
    cwd: Path | None = None,
    log_path: Path | None = None,
    line_callback: Callable[[str], None] | None = None,
    env: Mapping[str, str] | None = None,
) -> None:
    normalized_command = [str(part) for part in command]
    if log_path is None:
        subprocess.run(normalized_command, cwd=str(cwd) if cwd else None, check=True, env=env)
        return

    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("wb") as log_handle:
        process = subprocess.Popen(
            normalized_command,
            cwd=str(cwd) if cwd else None,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            env=env,
        )
        assert process.stdout is not None
        for raw_line in process.stdout:
            log_handle.write(raw_line)
            log_handle.flush()
            line = raw_line.decode("utf-8", errors="replace").rstrip("\r\n") + "\n"
            if line_callback is not None:
                line_callback(line)
        return_code = process.wait()
        if return_code != 0:
            raise RuntimeError(f"External command failed. See log: {log_path}")
