from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence

from .constants import (
    CATEGORY_BUGFIX,
    CATEGORY_FEATURE,
    CATEGORY_MAINTENANCE,
    CATEGORY_REFACTORING,
    CATEGORY_UNKNOWN,
    COMMIT_KEYWORDS_BUGFIX,
    COMMIT_KEYWORDS_FEATURE,
    COMMIT_KEYWORDS_REFACTORING,
    DEFAULT_EXEMPLARS_DIRNAME,
    DEFAULT_LOGGER_NAME,
    EXEMPLAR_BUGFIX_FILENAME,
    EXEMPLAR_FEATURE_FILENAME,
    EXEMPLAR_REFACTORING_FILENAME,
)
from .models import (
    ChangeUnitsOutput,
    ExemplarRecord,
    PipelineConfig,
    SelectedExemplarSet,
    SelectedExemplarsOutput,
)


LOGGER = logging.getLogger(DEFAULT_LOGGER_NAME)


# ============================================================
# Public entry
# ============================================================

def run_exemplar_selector(
    config: PipelineConfig,
    change_units_output: ChangeUnitsOutput,
) -> SelectedExemplarsOutput:
    """
    Select few-shot exemplars for each change unit.

    Current implementation:
    - heuristic category resolution
    - JSONL-based exemplar loading
    - category-first selection with simple fallback

    Important:
    - If exemplars_dir is None or missing, this step still works.
    - In that case, each unit gets an empty exemplar list.
    """
    exemplar_dir = _resolve_exemplar_dir(config)
    exemplar_pools = _load_exemplar_pools(exemplar_dir)

    selected_sets: List[SelectedExemplarSet] = []
    for unit in change_units_output.change_units:
        predicted_category, selection_evidence = _resolve_target_category(unit)
        exemplars = _select_exemplars_for_unit(
            unit=unit,
            predicted_category=predicted_category,
            exemplar_pools=exemplar_pools,
            top_k=config.prompt.top_k_exemplars,
        )

        selected_sets.append(
            SelectedExemplarSet(
                unit_id=unit.unit_id,
                predicted_change_category=predicted_category,
                selection_evidence=selection_evidence,
                exemplars=exemplars,
            )
        )

    LOGGER.info(
        "Step9 exemplar selection finished: %d exemplar sets built for %d change units.",
        len(selected_sets),
        len(change_units_output.change_units),
    )

    return SelectedExemplarsOutput(selected_exemplar_sets=selected_sets)


# ============================================================
# Category resolution
# ============================================================

def _resolve_target_category(unit) -> tuple[str, Dict[str, Any]]:
    """
    Priority:
    1. unit.inferred_change_category if directly usable
    2. fallback from commit message keywords
    3. default to refactoring
    """
    category = unit.inferred_change_category or CATEGORY_UNKNOWN
    commit_text = (unit.commit.full_message or "").lower()

    evidence: Dict[str, Any] = {
        "unit_inferred_category": unit.inferred_change_category,
        "commit_id": unit.commit.commit_id,
        "commit_subject": unit.commit.subject,
        "keyword_hits": [],
        "resolution_path": [],
    }

    if category in {CATEGORY_FEATURE, CATEGORY_BUGFIX, CATEGORY_REFACTORING}:
        evidence["resolution_path"].append("use_unit_inferred_category_directly")
        return category, evidence

    if _contains_any(commit_text, COMMIT_KEYWORDS_BUGFIX):
        evidence["keyword_hits"].append("bugfix")
        evidence["resolution_path"].append("fallback_from_commit_keywords_bugfix")
        return CATEGORY_BUGFIX, evidence

    if _contains_any(commit_text, COMMIT_KEYWORDS_FEATURE):
        evidence["keyword_hits"].append("feature")
        evidence["resolution_path"].append("fallback_from_commit_keywords_feature")
        return CATEGORY_FEATURE, evidence

    if _contains_any(commit_text, COMMIT_KEYWORDS_REFACTORING):
        evidence["keyword_hits"].append("refactoring")
        evidence["resolution_path"].append("fallback_from_commit_keywords_refactoring")
        return CATEGORY_REFACTORING, evidence

    if category == CATEGORY_MAINTENANCE:
        evidence["resolution_path"].append("maintenance_fallback_to_refactoring")
        return CATEGORY_REFACTORING, evidence

    evidence["resolution_path"].append("unknown_fallback_to_refactoring")
    return CATEGORY_REFACTORING, evidence


# ============================================================
# Exemplar loading
# ============================================================

def _resolve_exemplar_dir(config: PipelineConfig) -> Optional[Path]:
    """
    If config.prompt.exemplars_dir is provided, use it.
    Otherwise return None.

    Rationale:
    - At the current stage, the user may not yet have exemplar files.
    - We should not force a default path and fail unexpectedly.
    """
    if config.prompt.exemplars_dir is not None:
        return config.prompt.exemplars_dir
    return None


def _load_exemplar_pools(exemplar_dir: Optional[Path]) -> Dict[str, List[ExemplarRecord]]:
    pools: Dict[str, List[ExemplarRecord]] = {
        CATEGORY_FEATURE: [],
        CATEGORY_BUGFIX: [],
        CATEGORY_REFACTORING: [],
    }

    if exemplar_dir is None:
        LOGGER.warning(
            "No exemplars_dir configured. Step9 will continue with empty exemplar pools."
        )
        return pools

    file_map = {
        CATEGORY_FEATURE: exemplar_dir / EXEMPLAR_FEATURE_FILENAME,
        CATEGORY_BUGFIX: exemplar_dir / EXEMPLAR_BUGFIX_FILENAME,
        CATEGORY_REFACTORING: exemplar_dir / EXEMPLAR_REFACTORING_FILENAME,
    }

    for category, path in file_map.items():
        pools[category] = _load_jsonl_exemplars(path, fallback_category=category)

    return pools


def _load_jsonl_exemplars(path: Path, fallback_category: str) -> List[ExemplarRecord]:
    if not path.exists():
        LOGGER.warning("Exemplar file does not exist: %s. Using empty pool.", path)
        return []

    exemplars: List[ExemplarRecord] = []
    try:
        with path.open("r", encoding="utf-8") as f:
            for idx, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue

                try:
                    item = json.loads(line)
                except Exception as exc:
                    LOGGER.warning("Failed to parse JSONL line %d in %s: %s", idx, path, exc)
                    continue

                exemplar = ExemplarRecord(
                    exemplar_id=str(
                        item.get("exemplar_id")
                        or item.get("id")
                        or f"{fallback_category}_{idx:04d}"
                    ),
                    category=str(item.get("category") or fallback_category),
                    input_text=str(item.get("input") or item.get("input_text") or "").strip(),
                    output_text=str(item.get("output") or item.get("output_text") or "").strip(),
                    source=str(item.get("source") or path.name),
                    metadata=item if isinstance(item, dict) else {},
                )
                exemplars.append(exemplar)
    except Exception as exc:
        LOGGER.warning("Failed to load exemplar file %s: %s. Using empty pool.", path, exc)
        return []

    return exemplars


# ============================================================
# Exemplar selection
# ============================================================

def _select_exemplars_for_unit(
    unit,
    predicted_category: str,
    exemplar_pools: Dict[str, List[ExemplarRecord]],
    top_k: int,
) -> List[ExemplarRecord]:
    """
    Simple category-first selection:
    1. primary pool
    2. fallback pool(s)
    3. truncate to top_k
    """
    selected: List[ExemplarRecord] = []

    primary = exemplar_pools.get(predicted_category, [])
    selected.extend(_rank_exemplars(unit, primary))

    if len(selected) < top_k:
        for fallback_category in _fallback_categories(predicted_category):
            fallback_pool = exemplar_pools.get(fallback_category, [])
            selected.extend(_rank_exemplars(unit, fallback_pool))
            if len(selected) >= top_k:
                break

    # deduplicate by exemplar_id while preserving order
    deduped: List[ExemplarRecord] = []
    seen_ids = set()
    for exemplar in selected:
        if exemplar.exemplar_id in seen_ids:
            continue
        seen_ids.add(exemplar.exemplar_id)
        deduped.append(exemplar)

    return deduped[:top_k]


def _rank_exemplars(unit, exemplars: Sequence[ExemplarRecord]) -> List[ExemplarRecord]:
    """
    Current lightweight ranking:
    - prioritize exemplars whose input/output is non-empty
    - slight preference if commit subject overlaps exemplar text
    """
    commit_text = (unit.commit.full_message or "").lower()

    scored: List[tuple[float, ExemplarRecord]] = []
    for exemplar in exemplars:
        score = 0.0

        if exemplar.input_text.strip():
            score += 1.0
        if exemplar.output_text.strip():
            score += 1.0

        exemplar_text = f"{exemplar.input_text}\n{exemplar.output_text}".lower()
        if exemplar_text and commit_text:
            overlap = _keyword_overlap_score(commit_text, exemplar_text)
            score += overlap

        scored.append((score, exemplar))

    scored.sort(key=lambda x: (-x[0], x[1].exemplar_id))
    return [item[1] for item in scored]


def _fallback_categories(predicted_category: str) -> List[str]:
    if predicted_category == CATEGORY_FEATURE:
        return [CATEGORY_BUGFIX, CATEGORY_REFACTORING]
    if predicted_category == CATEGORY_BUGFIX:
        return [CATEGORY_REFACTORING, CATEGORY_FEATURE]
    if predicted_category == CATEGORY_REFACTORING:
        return [CATEGORY_BUGFIX, CATEGORY_FEATURE]
    return [CATEGORY_REFACTORING, CATEGORY_BUGFIX, CATEGORY_FEATURE]


# ============================================================
# Utility helpers
# ============================================================

def _contains_any(text: str, keywords: Iterable[str]) -> bool:
    for kw in keywords:
        if kw in text:
            return True
    return False


def _keyword_overlap_score(text_a: str, text_b: str) -> float:
    tokens_a = {tok for tok in _simple_tokenize(text_a) if len(tok) >= 3}
    tokens_b = {tok for tok in _simple_tokenize(text_b) if len(tok) >= 3}

    if not tokens_a or not tokens_b:
        return 0.0

    overlap = tokens_a & tokens_b
    return min(1.0, 0.1 * len(overlap))


def _simple_tokenize(text: str) -> List[str]:
    cleaned = []
    current = []

    for ch in text.lower():
        if ch.isalnum() or ch == "_":
            current.append(ch)
        else:
            if current:
                cleaned.append("".join(current))
                current = []

    if current:
        cleaned.append("".join(current))

    return cleaned