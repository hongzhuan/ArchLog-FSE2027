from __future__ import annotations

import logging
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

from .constants import DEFAULT_LOGGER_NAME
from .models import (
    ChangeUnit,
    PromptPayload,
    PromptRecord,
    PromptsOutput,
    PipelineConfig,
)


LOGGER = logging.getLogger(DEFAULT_LOGGER_NAME)

MAX_DIFF_LINE_CHARS_FOR_PROMPT = 500
MAX_CHANGED_STATEMENTS_TEXT_CHARS = 120_000


# ============================================================
# Public entry
# ============================================================

def run_prompt_builder(
    config: PipelineConfig,
    change_units_output,
) -> PromptsOutput:
    """
    Build LLM prompt records from commit-based ChangeUnit objects.

    Output:
    - one PromptRecord per ChangeUnit
    """
    app_description = None
    architecture_changes_text = None
    system_prompt = _load_system_prompt(config) or _default_system_prompt()
    user_prompt_template = _load_user_prompt_template(config) or _default_user_prompt_template()
    pr_lookup = _GitHubPrLookup.from_config(config)
    pr_metadata_by_commit = _collect_pr_metadata_for_units(config, pr_lookup, change_units_output.change_units)

    prompt_records: List[PromptRecord] = []

    for unit in change_units_output.change_units:
        pr_metadata = pr_metadata_by_commit.get(str(unit.commit.commit_id or "").strip(), {})
        payload = _build_prompt_payload(
            unit=unit,
            app_description=app_description,
            architecture_changes_text=architecture_changes_text,
            pr_metadata=pr_metadata,
        )
        user_prompt = _render_user_prompt_from_template(user_prompt_template, payload)

        prompt_records.append(
            PromptRecord(
                unit_id=unit.unit_id,
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                payload=payload,
            )
        )

    LOGGER.info(
        "Step8 prompt building finished: %d prompt records built from %d change units.",
        len(prompt_records),
        len(change_units_output.change_units),
    )

    return PromptsOutput(prompts=prompt_records)


def _collect_pr_metadata_for_units(
    config: PipelineConfig,
    pr_lookup: Optional["_GitHubPrLookup"],
    change_units: Sequence[ChangeUnit],
) -> Dict[str, Dict[str, Any]]:
    if pr_lookup is None:
        return {}

    commit_ids = _unique_commit_ids(change_units)
    progress_enabled = bool(getattr(config, "verbose", False))
    progress_bar = _SingleLineProgressBar() if progress_enabled else None
    metadata_by_commit: Dict[str, Dict[str, Any]] = {}

    if progress_bar is not None:
        progress_bar.update(completed=0, total=len(commit_ids))

    for index, commit_id in enumerate(commit_ids, start=1):
        metadata_by_commit[commit_id] = pr_lookup.lookup(commit_id)
        if progress_bar is not None:
            progress_bar.update(completed=index, total=len(commit_ids))

    if progress_bar is not None:
        progress_bar.finish()

    return metadata_by_commit


def _unique_commit_ids(change_units: Sequence[ChangeUnit]) -> List[str]:
    seen = set()
    commit_ids: List[str] = []
    for unit in change_units:
        commit_id = str(unit.commit.commit_id or "").strip()
        if not commit_id or commit_id in seen:
            continue
        seen.add(commit_id)
        commit_ids.append(commit_id)
    return commit_ids


class _SingleLineProgressBar:
    """
    Render a single in-place progress line for GitHub PR metadata lookup.
    """

    def __init__(self, stream=None) -> None:
        self._stream = stream if stream is not None else sys.stdout
        self._last_text_length = 0
        self._active = False

    def update(self, *, completed: int, total: int) -> None:
        text = _format_step8_pr_progress(completed=completed, total=total)
        padding = max(0, self._last_text_length - len(text))
        self._stream.write("\r" + text + (" " * padding))
        self._stream.flush()
        self._last_text_length = len(text)
        self._active = True

    def finish(self) -> None:
        if not self._active:
            return
        self._stream.write("\n")
        self._stream.flush()
        self._active = False
        self._last_text_length = 0


def _format_step8_pr_progress(*, completed: int, total: int) -> str:
    if total <= 0:
        return "Step8 PR lookup progress: 0/0 [--------------------] 100.0%"

    ratio = min(1.0, max(0.0, completed / total))
    width = 20
    filled = int(width * ratio)
    bar = "#" * filled + "-" * (width - filled)
    return f"Step8 PR lookup progress: {completed}/{total} [{bar}] {ratio * 100:5.1f}%"


# ============================================================
# Payload construction
# ============================================================

def _build_prompt_payload(
    unit: ChangeUnit,
    app_description: Optional[str],
    architecture_changes_text: Optional[str],
    pr_metadata: Optional[Dict[str, Any]] = None,
) -> PromptPayload:
    changed_methods = [_serialize_method_for_prompt(method) for method in unit.changed_methods]
    changed_statements = _serialize_hunk_pairs_for_prompt(unit.method_hunk_pairs)
    changed_statements.extend(
        _serialize_fallback_hunks_for_prompt(
            unit.evidence.get("fallback_diff_hunks") or [],
            evidence_granularity="hunk_level",
            change_type="hunk_only",
            match_type="hunk_level_fallback",
        )
    )
    changed_statements.extend(
        _serialize_fallback_hunks_for_prompt(
            unit.evidence.get("fallback_file_hunks") or [],
            evidence_granularity="file_level",
            change_type="file_only",
            match_type="file_level_fallback",
        )
    )
    graph_texts = _serialize_graphs_for_prompt(unit.method_context_graphs)
    evidence_granularity = str(unit.evidence.get("evidence_granularity") or "method_level")
    change_detection_status = str(unit.evidence.get("change_detection_status") or "method_level_change")
    pr_metadata = pr_metadata or {}
    return PromptPayload(
        unit_id=unit.unit_id,
        app_description=app_description,
        commit_id=unit.commit.commit_id,
        commit_message=unit.commit.full_message,
        changed_methods=changed_methods,
        changed_statements=changed_statements,
        graph_texts=graph_texts,
        inferred_change_category=unit.inferred_change_category,
        evidence_granularity=evidence_granularity,
        change_detection_status=change_detection_status,
        architecture_changes_text=architecture_changes_text,
        pr_title=_clean_optional_text(pr_metadata.get("title")),
        pr_body=_clean_optional_text(pr_metadata.get("body")),
        pr_number=_clean_optional_int(pr_metadata.get("number")),
        pr_url=_clean_optional_text(pr_metadata.get("url")),
        commit_url=_clean_optional_text(pr_metadata.get("commit_url")),
        pull_requests=_normalize_pull_request_links(pr_metadata.get("pull_requests")),
    )


def _serialize_method_for_prompt(method) -> Dict[str, Any]:
    identity = method.new_identity or method.old_identity

    if identity is None:
        return {
            "method_uid": method.method_uid,
            "change_type": method.change_type,
            "qualified_name": None,
            "file_path": None,
            "start_line": None,
            "end_line": None,
            "enre_entity_id": method.enre_entity_id,
        }

    return {
        "method_uid": method.method_uid,
        "change_type": method.change_type,
        "qualified_name": identity.qualified_name,
        "simple_name": identity.simple_name,
        "file_path": identity.file_path,
        "start_line": identity.start_line,
        "end_line": identity.end_line,
        "category": identity.category,
        "parent_qualified_name": identity.parent_qualified_name,
        "return_type": identity.return_type,
        "parameters": identity.parameters,
        "enre_entity_id": method.enre_entity_id,
        "enre_match_score": method.enre_match_score,
    }


def _serialize_hunk_pairs_for_prompt(method_hunk_pairs: Sequence) -> List[Dict[str, Any]]:
    results: List[Dict[str, Any]] = []

    for pair in method_hunk_pairs:
        pair_item: Dict[str, Any] = {
            "method_uid": pair.method_uid,
            "change_type": pair.change_type,
            "primary_commit_id": pair.primary_commit_id,
            "matched_hunks": [],
        }

        for matched_hunk in pair.matched_hunks:
            pair_item["matched_hunks"].append(
                {
                    "hunk_id": matched_hunk.hunk_id,
                    "commit_id": matched_hunk.commit_id,
                    "match_type": matched_hunk.match_type,
                    "coverage_score": matched_hunk.coverage_score,
                    "matched_old_lines": matched_hunk.matched_old_lines,
                    "matched_new_lines": matched_hunk.matched_new_lines,
                    "matched_diff_text": _truncate_diff_lines(matched_hunk.matched_diff_text, max_lines=20),
                }
            )

        results.append(pair_item)

    return results


def _serialize_fallback_hunks_for_prompt(
    fallback_hunks: Sequence[Dict[str, Any]],
    *,
    evidence_granularity: str,
    change_type: str,
    match_type: str,
) -> List[Dict[str, Any]]:
    results: List[Dict[str, Any]] = []
    for hunk in fallback_hunks:
        if not isinstance(hunk, dict):
            continue
        hunk_id = str(hunk.get("hunk_id") or "").strip()
        if not hunk_id:
            continue
        results.append(
            {
                "method_uid": None,
                "change_type": change_type,
                "primary_commit_id": hunk.get("commit_id"),
                "evidence_granularity": evidence_granularity,
                "matched_hunks": [
                    {
                        "hunk_id": hunk_id,
                        "commit_id": hunk.get("commit_id"),
                        "match_type": match_type,
                        "coverage_score": 1.0,
                        "file_path": hunk.get("file_path_new") or hunk.get("file_path_old"),
                        "matched_old_lines": _line_numbers(hunk.get("deleted_lines") or []),
                        "matched_new_lines": _line_numbers(hunk.get("added_lines") or []),
                        "matched_diff_text": _truncate_diff_lines(
                            str(hunk.get("diff_text") or "").splitlines(),
                            max_lines=24,
                        ),
                    }
                ],
            }
        )
    return results


def _line_numbers(lines: Sequence[Dict[str, Any]]) -> List[int]:
    result: List[int] = []
    for line in lines:
        if not isinstance(line, dict):
            continue
        value = line.get("line_no")
        if isinstance(value, int):
            result.append(value)
    return result


def _serialize_graphs_for_prompt(method_context_graphs: Sequence) -> List[Dict[str, Any]]:
    results: List[Dict[str, Any]] = []

    for graph in method_context_graphs:
        nodes = []
        for node in graph.nodes[:30]:
            nodes.append(
                {
                    "entity_id": node.entity_id,
                    "qualified_name": node.qualified_name,
                    "category": node.category,
                    "role": node.role,
                    "file_path": node.file_path,
                    "start_line": node.start_line,
                    "end_line": node.end_line,
                }
            )

        edges = []
        for edge in graph.edges[:50]:
            edges.append(
                {
                    "src_entity_id": edge.src_entity_id,
                    "dst_entity_id": edge.dst_entity_id,
                    "relation_type": edge.relation_type,
                    "start_line": edge.start_line,
                    "end_line": edge.end_line,
                }
            )

        results.append(
            {
                "graph_id": graph.graph_id,
                "entry_method_uid": graph.entry_method_uid,
                "entry_entity_id": graph.entry_entity_id,
                "commit_id": graph.commit_id,
                "changed_method_uids": graph.changed_method_uids,
                "nodes": nodes,
                "edges": edges,
                "graph_text": _render_graph_text(nodes, edges, graph.entry_entity_id),
            }
        )

    return results


# ============================================================
# Template-driven user prompt rendering
# ============================================================

def _render_user_prompt_from_template(template: str, payload: PromptPayload) -> str:
    """Render the commit-summary user prompt from a template and payload."""
    app_description_text = payload.app_description.strip() if payload.app_description else "(none)"
    architecture_changes_path_text = (
        payload.architecture_changes_text.strip()
        if payload.architecture_changes_text
        else "(none)"
    )
    changed_methods_text = _render_changed_methods_text(
        payload.changed_methods,
        payload.evidence_granularity,
        payload.change_detection_status,
    )
    changed_statements_text = _render_changed_statements_text(payload.changed_statements)
    graph_text = _render_graph_text_block(payload.graph_texts)
    pr_context_text = _render_pr_context_text(payload)
    rendered = template

    rendered = rendered.replace("{commit_id}", payload.commit_id or "")
    rendered = rendered.replace("{commit_message}", payload.commit_message.strip() if payload.commit_message else "(empty)")
    rendered = rendered.replace("{pr_context_text}", pr_context_text)
    rendered = rendered.replace("{pr_title}", payload.pr_title or "(none)")
    rendered = rendered.replace("{pr_body}", payload.pr_body or "(none)")
    rendered = rendered.replace("{inferred_change_category}", payload.inferred_change_category or "unknown")
    rendered = rendered.replace("{evidence_granularity}", payload.evidence_granularity or "method_level")
    rendered = rendered.replace("{change_detection_status}", payload.change_detection_status or "method_level_change")
    rendered = rendered.replace("{app_description}", app_description_text)
    rendered = rendered.replace("{architecture_changes_path}", architecture_changes_path_text)
    rendered = rendered.replace("{architecture_changes_text}", architecture_changes_path_text)
    rendered = rendered.replace("{changed_methods_text}", changed_methods_text)
    rendered = rendered.replace("{changed_statements_text}", changed_statements_text)
    rendered = rendered.replace("{graph_text}", graph_text)
    rendered = rendered.replace("{pr_context_text}", pr_context_text)
    rendered = rendered.replace("{pr_title}", payload.pr_title or "(none)")
    rendered = rendered.replace("{pr_body}", payload.pr_body or "(none)")

    return rendered.strip()


def _render_changed_methods_text(
    changed_methods: Sequence[Dict[str, Any]],
    evidence_granularity: str = "method_level",
    change_detection_status: str = "method_level_change",
) -> str:
    if not changed_methods:
        if evidence_granularity == "file_level":
            return (
                "(none; this change unit is based on file-level diff evidence "
                f"because {change_detection_status})"
            )
        if evidence_granularity != "method_level":
            return (
                "(none; this change unit is based on file/hunk-level diff evidence "
                f"because {change_detection_status})"
            )
        return "(none)"

    lines: List[str] = []
    for item in changed_methods:
        lines.append(
            "- "
            f"method_uid={item.get('method_uid')} | "
            f"type={item.get('change_type')} | "
            f"qualified_name={item.get('qualified_name')} | "
            f"file={item.get('file_path')} | "
            f"lines={item.get('start_line')}-{item.get('end_line')} | "
            f"entity_id={item.get('enre_entity_id')}"
        )
    return "\n".join(lines)


def _render_changed_statements_text(changed_statements: Sequence[Dict[str, Any]]) -> str:
    if not changed_statements:
        return "(none)"

    lines: List[str] = []
    truncated = False

    def append_line(line: str) -> bool:
        nonlocal truncated
        if truncated:
            return False
        projected_size = sum(len(existing) + 1 for existing in lines) + len(line) + 1
        if projected_size > MAX_CHANGED_STATEMENTS_TEXT_CHARS:
            truncated = True
            return False
        lines.append(line)
        return True

    for pair_index, pair in enumerate(changed_statements):
        if not append_line(
            f"- method_uid={pair.get('method_uid')} | "
            f"type={pair.get('change_type')} | "
            f"primary_commit_id={pair.get('primary_commit_id')} | "
            f"evidence_granularity={pair.get('evidence_granularity') or 'method_level'}"
        ):
            break

        matched_hunks = pair.get("matched_hunks", [])
        if not matched_hunks:
            if not append_line("  - (no matched hunks)"):
                break
            continue

        for hunk in matched_hunks:
            if not append_line(
                "  - "
                f"hunk_id={hunk.get('hunk_id')} | "
                f"match_type={hunk.get('match_type')} | "
                f"coverage={hunk.get('coverage_score')} | "
                f"file={hunk.get('file_path') or ''}"
            ):
                break
            diff_lines = hunk.get("matched_diff_text", [])
            if diff_lines:
                if not append_line("    diff:"):
                    break
                for line in diff_lines:
                    if not append_line(f"      {line}"):
                        break
            if truncated:
                break
        if truncated:
            omitted = max(0, len(changed_statements) - pair_index)
            lines.append(
                f"... [truncated: omitted {omitted} diff evidence item(s) "
                "because this commit has too many hunks for one LLM request]"
            )
            break

    return "\n".join(lines)


def _render_pr_context_text(payload: PromptPayload) -> str:
    title = _clean_optional_text(payload.pr_title)
    body = _clean_optional_text(payload.pr_body)
    if not title and not body:
        return "(none)"

    lines = []
    if title:
        lines.append("PR Title:")
        lines.append(title)
    if body:
        if lines:
            lines.append("")
        lines.append("PR Body:")
        lines.append(_truncate_text(body, max_chars=4000))
    return "\n".join(lines).strip()


def _render_graph_text_block(graph_texts: Sequence[Dict[str, Any]]) -> str:
    if not graph_texts:
        return "(none)"

    lines: List[str] = []
    for graph in graph_texts:
        lines.append(
            f"- graph_id={graph.get('graph_id')} | "
            f"entry_method_uid={graph.get('entry_method_uid')} | "
            f"entry_entity_id={graph.get('entry_entity_id')}"
        )
        lines.append(graph.get("graph_text", "").strip() or "  (empty graph)")
    return "\n".join(lines)


def _render_graph_text(nodes: Sequence[Dict[str, Any]], edges: Sequence[Dict[str, Any]], entry_entity_id: int) -> str:
    lines: List[str] = []
    lines.append("  nodes:")
    if nodes:
        for node in nodes:
            marker = "*" if node.get("entity_id") == entry_entity_id else "-"
            lines.append(
                f"    {marker} "
                f"id={node.get('entity_id')} | "
                f"name={node.get('qualified_name')} | "
                f"role={node.get('role')} | "
                f"category={node.get('category')}"
            )
    else:
        lines.append("    (none)")

    lines.append("  edges:")
    if edges:
        for edge in edges:
            lines.append(
                f"    - "
                f"{edge.get('src_entity_id')} -> {edge.get('dst_entity_id')} | "
                f"type={edge.get('relation_type')}"
            )
    else:
        lines.append("    (none)")

    return "\n".join(lines)


def _truncate_diff_lines(lines: Sequence[str], max_lines: int = 20) -> List[str]:
    if len(lines) <= max_lines:
        return [_truncate_diff_line(line) for line in lines]
    kept = [_truncate_diff_line(line) for line in lines[:max_lines]]
    kept.append("... [truncated]")
    return kept


def _truncate_diff_line(line: str) -> str:
    text = str(line)
    if len(text) <= MAX_DIFF_LINE_CHARS_FOR_PROMPT:
        return text
    return text[: MAX_DIFF_LINE_CHARS_FOR_PROMPT - 16].rstrip() + " ... [truncated]"


def _clean_optional_text(value: Any) -> Optional[str]:
    text = str(value or "").strip()
    return text or None


def _clean_optional_int(value: Any) -> Optional[int]:
    try:
        number = int(value)
    except (TypeError, ValueError):
        return None
    return number if number > 0 else None


def _normalize_pull_request_links(value: Any) -> List[Dict[str, Any]]:
    if not isinstance(value, list):
        return []
    links: List[Dict[str, Any]] = []
    seen = set()
    for raw in value:
        if not isinstance(raw, dict):
            continue
        number = _clean_optional_int(raw.get("number"))
        url = _clean_optional_text(raw.get("url") or raw.get("html_url"))
        key = (number, url)
        if number is None or not url or key in seen:
            continue
        links.append({"number": number, "url": url})
        seen.add(key)
    return links


def _truncate_text(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 16].rstrip() + "\n... [truncated]"


class _GitHubPrLookup:
    def __init__(self, *, owner: str, repo: str, token: Optional[str]) -> None:
        self.owner = owner
        self.repo = repo
        self.token = token
        self._cache: Dict[str, Dict[str, Any]] = {}

    @classmethod
    def from_config(cls, config: PipelineConfig) -> Optional["_GitHubPrLookup"]:
        if not bool(getattr(config, "step10_pr_metadata_enabled", True)):
            return None

        owner_repo = _resolve_github_owner_repo(config.repo_path)
        if owner_repo is None:
            LOGGER.info("GitHub PR metadata is enabled, but repo origin is not a GitHub URL. PR context will be skipped.")
            return None

        token_env = str(getattr(config, "step10_pr_metadata_token_env", "GITHUB_TOKEN") or "GITHUB_TOKEN").strip()
        token = os.getenv(token_env)
        if not token:
            raise RuntimeError(
                "GitHub PR metadata is enabled, but the required environment "
                f"variable {token_env} is not set. Set {token_env} or disable "
                "STEP10_PR_METADATA_ENABLED before running Step8/Step10."
            )

        owner, repo = owner_repo
        return cls(owner=owner, repo=repo, token=token)

    def lookup(self, commit_id: str) -> Dict[str, Any]:
        commit_id = str(commit_id or "").strip()
        if not commit_id:
            return {}
        if commit_id not in self._cache:
            self._cache[commit_id] = self._fetch(commit_id)
        return dict(self._cache[commit_id])

    def _fetch(self, commit_id: str) -> Dict[str, Any]:
        result: Dict[str, Any] = {
            "commit_url": f"https://github.com/{self.owner}/{self.repo}/commit/{commit_id}"
        }
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/commits/{commit_id}/pulls"
        request = urllib.request.Request(
            url,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {self.token}",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "ArchLog-Step10-PR-Metadata",
            },
        )

        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = json.loads(response.read().decode("utf-8", errors="replace"))
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return result
            LOGGER.warning("GitHub PR lookup failed for commit %s with HTTP %s.", commit_id, exc.code)
            return result
        except Exception as exc:
            LOGGER.warning("GitHub PR lookup failed for commit %s: %s", commit_id, exc)
            return result

        if not isinstance(payload, list) or not payload:
            return result

        pull_requests = _normalize_pull_request_links(payload)
        if pull_requests:
            result["pull_requests"] = pull_requests
        pr = _choose_pr_for_commit(payload)
        title = _clean_optional_text(pr.get("title"))
        body = _clean_optional_text(pr.get("body"))
        if title:
            result["title"] = title
        if body:
            result["body"] = body
        number = _clean_optional_int(pr.get("number"))
        pr_url = _clean_optional_text(pr.get("html_url"))
        if number is not None:
            result["number"] = number
        if pr_url:
            result["url"] = pr_url
        return result


def _choose_pr_for_commit(prs: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    for pr in prs:
        if isinstance(pr, dict) and _clean_optional_text(pr.get("merged_at")):
            return pr
    for pr in prs:
        if isinstance(pr, dict):
            return pr
    return {}


def _resolve_github_owner_repo(repo_path: Path) -> Optional[tuple[str, str]]:
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=str(repo_path),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
    except Exception:
        return None

    if result.returncode != 0:
        return None
    return _parse_github_owner_repo(result.stdout.strip())


def _parse_github_owner_repo(remote_url: str) -> Optional[tuple[str, str]]:
    text = str(remote_url or "").strip()
    if not text:
        return None

    patterns = [
        r"github\.com[:/](?P<owner>[^/\s:]+)/(?P<repo>[^/\s]+?)(?:\.git)?/?$",
        r"^git@github\.com:(?P<owner>[^/\s:]+)/(?P<repo>[^/\s]+?)(?:\.git)?$",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if not match:
            continue
        owner = match.group("owner").strip()
        repo = match.group("repo").strip()
        if repo.endswith(".git"):
            repo = repo[:-4]
        if owner and repo:
            return owner, repo
    return None


# ============================================================
# Prompt loading
# ============================================================

def _load_system_prompt(config: PipelineConfig) -> Optional[str]:
    prompt_path = config.prompt.system_prompt_path
    if prompt_path is None:
        LOGGER.info("No system_prompt_path configured. Using default system prompt.")
        return None

    if not prompt_path.exists():
        LOGGER.warning("System prompt file does not exist: %s. Using default system prompt.", prompt_path)
        return None

    try:
        text = prompt_path.read_text(encoding="utf-8").strip()
        if not text:
            LOGGER.warning("System prompt file is empty: %s. Using default system prompt.", prompt_path)
            return None

        LOGGER.info("Loaded system prompt from file: %s", prompt_path)
        return text
    except Exception as exc:
        LOGGER.warning("Failed to read system prompt file %s: %s. Using default prompt.", prompt_path, exc)
        return None


def _load_user_prompt_template(config: PipelineConfig) -> Optional[str]:
    prompt_path = config.prompt.user_prompt_path
    if prompt_path is None:
        LOGGER.info("No user_prompt_path configured. Using default user prompt template.")
        return None

    if not prompt_path.exists():
        LOGGER.warning("User prompt template file does not exist: %s. Using default template.", prompt_path)
        return None

    try:
        text = prompt_path.read_text(encoding="utf-8").strip()
        if not text:
            LOGGER.warning("User prompt template file is empty: %s. Using default template.", prompt_path)
            return None

        LOGGER.info("Loaded user prompt template from file: %s", prompt_path)
        return text
    except Exception as exc:
        LOGGER.warning("Failed to read user prompt template file %s: %s. Using default template.", prompt_path, exc)
        return None


def _load_optional_text(path: Optional[Path]) -> Optional[str]:
    if path is None:
        return None
    if not path.exists():
        LOGGER.warning("Optional text file does not exist: %s. Skip loading.", path)
        return None
    try:
        text = path.read_text(encoding="utf-8").strip()
        return text if text else None
    except Exception as exc:
        LOGGER.warning("Failed to read optional text file %s: %s. Skip loading.", path, exc)
        return None


def _default_system_prompt() -> str:
    return (
        "You are a single-commit release-note summary assistant. "
        "Generate one concise English summary from commit messages, diff evidence, "
        "optional changed methods, and optional PR context. Use only provided evidence. "
        "Do not list hunks, machine fields, or long method lists. If no changed methods "
        "are available, summarize file-level API, build, configuration, documentation, CI, "
        "release-script, packaging, or test-resource changes without inventing function-level behavior. "
        "Output only the final summary text."
    )

def _default_user_prompt_template() -> str:
    return (
        "Generate one release-note-style English change summary from the evidence below.\n"
        "Use only the provided evidence and do not guess.\n\n"
        "==============================\n"
        "Commit Information\n\n"
        "Commit ID: {commit_id}\n\n"
        "Commit Message:\n"
        "{commit_message}\n\n"
        "Inferred change type (reference only):\n"
        "{inferred_change_category}\n\n"
        "==============================\n"
        "Changed Methods\n\n"
        "If this section is none, summarize using commit message and file-level diff evidence.\n\n"
        "{changed_methods_text}\n\n"
        "==============================\n"
        "Diff Evidence\n\n"
        "Key diff evidence follows. file_level diffs are real change evidence.\n\n"
        "{changed_statements_text}\n\n"
        "==============================\n"
        "Call Context\n\n"
        "{graph_text}\n\n"
        "==============================\n"
        "Related PR Information (optional)\n\n"
        "{pr_context_text}\n\n"
        "Task: write one concise English change summary. Prefer user- or developer-understandable "
        "behavior, API, fix, feature, build, configuration, documentation, CI, or maintenance changes. "
        "If evidence_granularity is file_level, do not describe it as a function implementation change. "
        "Output only the final summary text."
    )
