from __future__ import annotations

import copy
import json
import logging
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from .constants import (
    CALLABLE_ENTITY_CATEGORIES,
    DEFAULT_LOGGER_NAME,
)
from .models import (
    ChangedMethod,
    CommitsMappedOutput,
    EnreEntity,
    EnreMatchedOutput,
    EnreRelation,
    PipelineConfig,
)


LOGGER = logging.getLogger(DEFAULT_LOGGER_NAME)


# ============================================================
# Public entry
# ============================================================

def run_enre_entity_matcher(
    config: PipelineConfig,
    commits_mapped_output: CommitsMappedOutput,
) -> EnreMatchedOutput:
    """
    Match changed methods to ENRE entities from the NEW version.

    Matching policy:
    - Prefer new_identity for added / modified methods
    - Deleted methods usually remain unmatched because ENRE is new-version only
    - Matching is occurrence-level, not only qualified-name-level
    - Allow low-confidence nearest-line fallback when ENRE preserves fewer
      occurrences than Step1 (e.g. preprocessor branches)
    """
    raw_data = _load_json(config.enre_json_path)

    entities = _load_enre_entities(raw_data)
    relations = _load_enre_relations(raw_data)

    callable_entities = [e for e in entities if e.category in CALLABLE_ENTITY_CATEGORIES]
    entity_index = _build_entity_index(callable_entities)

    matched_methods: List[ChangedMethod] = []
    matched_count = 0

    for method in commits_mapped_output.changed_methods:
        method_copy = copy.deepcopy(method)

        match_result = _match_single_method_to_enre_entity(
            method=method_copy,
            entities=callable_entities,
            entity_index=entity_index,
            min_score=config.matching.enre_min_score,
        )

        evidence = method_copy.evidence.setdefault("enre_match", {})

        if match_result is not None:
            entity, score, strategy, debug_info = match_result
            method_copy.enre_entity_id = entity.entity_id
            method_copy.enre_match_score = round(score, 6)
            method_copy.enre_match_strategy = list(strategy)
            matched_count += 1

            evidence["matched"] = True
            evidence["entity_id"] = entity.entity_id
            evidence["qualified_name"] = entity.qualified_name
            evidence["file_path"] = entity.file_path
            evidence["start_line"] = entity.start_line
            evidence["end_line"] = entity.end_line
            evidence["score"] = round(score, 6)
            evidence["strategy"] = list(strategy)
            evidence["candidate_count"] = debug_info["candidate_count"]
            evidence["line_overlap_ratio"] = round(debug_info["line_overlap_ratio"], 6)
            evidence["line_distance"] = debug_info["line_distance"]
        else:
            method_copy.enre_entity_id = None
            method_copy.enre_match_score = None
            method_copy.enre_match_strategy = []
            evidence["matched"] = False

        matched_methods.append(method_copy)

    LOGGER.info(
        "Step3 ENRE entity matching finished: %d/%d changed methods matched to ENRE callable entities.",
        matched_count,
        len(matched_methods),
    )

    return EnreMatchedOutput(
        changed_methods=matched_methods,
        entities=entities,
        relations=relations,
    )


# ============================================================
# JSON loading
# ============================================================

def _load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _load_enre_entities(raw_data: Dict[str, Any]) -> List[EnreEntity]:
    raw_entities = _extract_raw_entity_list(raw_data)
    file_lookup = _build_file_lookup_from_raw_entities(raw_entities)

    entities: List[EnreEntity] = []
    for raw in raw_entities:
        entity_id = _safe_int(raw.get("id"))
        if entity_id is None:
            continue

        category = str(raw.get("category", "")).strip()
        qualified_name = str(raw.get("qualifiedName", "")).strip()

        file_path = _resolve_entity_file_path(raw, file_lookup)
        if category == "File" and qualified_name:
            file_path = qualified_name

        start_line = _safe_int(raw.get("startLine")) or 0
        end_line = _safe_int(raw.get("endLine")) or start_line

        entity = EnreEntity(
            entity_id=entity_id,
            qualified_name=qualified_name,
            category=category,
            file_path=_normalize_path(file_path) if file_path else "",
            start_line=start_line,
            end_line=end_line,
            parent_id=_safe_int(raw.get("parentID")),
            entity_file=_safe_int(raw.get("entityFile")),
            start_offset=_safe_int(raw.get("startOffset")),
            end_offset=_safe_int(raw.get("endOffset")),
            return_type=_safe_str(raw.get("returnType")),
            raw=raw,
        )
        entities.append(entity)

    return entities


def _extract_raw_entity_list(raw_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    raw_entities = (
        raw_data.get("entities")
        or raw_data.get("entity")
        or raw_data.get("variables")
        or []
    )
    if isinstance(raw_entities, list):
        return [item for item in raw_entities if isinstance(item, dict)]
    return []


def _load_enre_relations(raw_data: Dict[str, Any]) -> List[EnreRelation]:
    raw_relations = (
        raw_data.get("relations")
        or raw_data.get("relation")
        or []
    )

    relations: List[EnreRelation] = []
    for idx, raw in enumerate(raw_relations, start=1):
        src_id = _safe_int(
            raw.get("src")
            or raw.get("from")
            or raw.get("source")
            or raw.get("srcID")
            or raw.get("fromID")
        )
        dst_id = _safe_int(
            raw.get("dst")
            or raw.get("to")
            or raw.get("target")
            or raw.get("dest")
            or raw.get("dstID")
            or raw.get("toID")
        )

        if src_id is None or dst_id is None:
            continue

        relation_type = _safe_str(
            raw.get("category")
            or raw.get("type")
            or raw.get("relation")
            or raw.get("kind")
        ) or ""

        relation = EnreRelation(
            relation_id=str(raw.get("id", idx)),
            src_entity_id=src_id,
            dst_entity_id=dst_id,
            relation_type=relation_type,
            start_line=_safe_int(raw.get("startLine")),
            end_line=_safe_int(raw.get("endLine")),
            raw=raw,
        )
        relations.append(relation)

    return relations


def _build_file_lookup_from_raw_entities(raw_entities: Sequence[Dict[str, Any]]) -> Dict[int, str]:
    """
    ENRE outputs vary a lot across versions.

    For the jsoncpp sample, the top-level `variables` array contains File entities,
    and regular entities reference them via `entityFile`.
    """
    lookup: Dict[int, str] = {}

    for raw in raw_entities:
        category = str(raw.get("category", "")).strip()
        if category != "File":
            continue

        entity_id = _safe_int(raw.get("id"))
        qualified_name = _safe_str(raw.get("qualifiedName"))
        if entity_id is None or not qualified_name:
            continue

        lookup[entity_id] = _normalize_path(qualified_name)

    return lookup


def _resolve_entity_file_path(raw_entity: Dict[str, Any], file_lookup: Dict[int, str]) -> Optional[str]:
    direct = _safe_str(
        raw_entity.get("filePath")
        or raw_entity.get("path")
        or raw_entity.get("fullPath")
        or raw_entity.get("file")
    )
    if direct:
        return direct

    entity_file_id = _safe_int(raw_entity.get("entityFile"))
    if entity_file_id is not None and entity_file_id in file_lookup:
        return file_lookup[entity_file_id]

    return None


# ============================================================
# Index building
# ============================================================

def _build_entity_index(entities: Sequence[EnreEntity]) -> Dict[str, Any]:
    by_file: Dict[str, List[EnreEntity]] = {}
    by_name: Dict[str, List[EnreEntity]] = {}
    by_qualified_name: Dict[str, List[EnreEntity]] = {}
    by_file_and_name: Dict[Tuple[str, str], List[EnreEntity]] = {}
    by_file_and_qname: Dict[Tuple[str, str], List[EnreEntity]] = {}

    for entity in entities:
        norm_path = _normalize_path(entity.file_path) if entity.file_path else ""
        simple_name = _simple_name_from_qualified_name(entity.qualified_name)
        suffix_name = _scope_suffix_name(entity.qualified_name)

        if norm_path:
            by_file.setdefault(norm_path, []).append(entity)

        if simple_name:
            by_name.setdefault(simple_name, []).append(entity)
            if norm_path:
                by_file_and_name.setdefault((norm_path, simple_name), []).append(entity)

        if suffix_name:
            by_qualified_name.setdefault(suffix_name, []).append(entity)
            if norm_path:
                by_file_and_qname.setdefault((norm_path, suffix_name), []).append(entity)

        if entity.qualified_name:
            by_qualified_name.setdefault(entity.qualified_name, []).append(entity)
            if norm_path:
                by_file_and_qname.setdefault((norm_path, entity.qualified_name), []).append(entity)

    return {
        "by_file": by_file,
        "by_name": by_name,
        "by_qualified_name": by_qualified_name,
        "by_file_and_name": by_file_and_name,
        "by_file_and_qname": by_file_and_qname,
    }


# ============================================================
# Matching core
# ============================================================

def _match_single_method_to_enre_entity(
    method: ChangedMethod,
    entities: Sequence[EnreEntity],
    entity_index: Dict[str, Any],
    min_score: float,
) -> Optional[Tuple[EnreEntity, float, List[str], Dict[str, Any]]]:
    """
    Return:
      (best_entity, score, strategy, debug_info)
    or None
    """
    identity = _select_matching_identity(method)
    if identity is None:
        return None

    # Deleted methods typically do not exist in new-version ENRE.
    if method.change_type == "deleted":
        return None

    method_path = _normalize_path(identity.file_path)
    method_qname = identity.qualified_name or ""
    method_qname_suffix = _scope_suffix_name(method_qname)
    method_simple_name = identity.simple_name or _simple_name_from_qualified_name(method_qname)
    method_start = identity.start_line
    method_end = identity.end_line

    candidates = _collect_candidates(
        method_path=method_path,
        method_qname=method_qname,
        method_qname_suffix=method_qname_suffix,
        method_simple_name=method_simple_name,
        entity_index=entity_index,
        all_entities=entities,
    )

    if not candidates:
        return None

    scored: List[Tuple[EnreEntity, float, List[str], Dict[str, Any]]] = []
    for entity in candidates:
        score, strategy, debug_info = _score_method_entity_match(
            method_path=method_path,
            method_qname=method_qname,
            method_qname_suffix=method_qname_suffix,
            method_simple_name=method_simple_name,
            method_start=method_start,
            method_end=method_end,
            entity=entity,
        )
        if score > 0:
            debug_info["candidate_count"] = len(candidates)
            scored.append((entity, score, strategy, debug_info))

    if not scored:
        return None

    scored.sort(
        key=lambda x: (
            -x[1],
            x[3]["line_distance"],
            x[0].entity_id,
        )
    )

    best_entity, best_score, best_strategy, best_debug = scored[0]
    if best_score < min_score:
        return None

    return best_entity, best_score, best_strategy, best_debug


def _select_matching_identity(method: ChangedMethod):
    if method.new_identity is not None:
        return method.new_identity
    return method.old_identity


def _collect_candidates(
    method_path: str,
    method_qname: str,
    method_qname_suffix: str,
    method_simple_name: str,
    entity_index: Dict[str, Any],
    all_entities: Sequence[EnreEntity],
) -> List[EnreEntity]:
    """
    Candidate strategy:
    1. same file + same qname / qname suffix
    2. same file + same simple name
    3. same file
    4. global qname / suffix name
    5. global simple name
    6. fallback all callable entities
    """
    candidates: List[EnreEntity] = []
    seen_ids = set()

    def add_many(items: Iterable[EnreEntity]) -> None:
        for item in items:
            if item.entity_id in seen_ids:
                continue
            seen_ids.add(item.entity_id)
            candidates.append(item)

    by_file = entity_index["by_file"]
    by_name = entity_index["by_name"]
    by_qualified_name = entity_index["by_qualified_name"]
    by_file_and_name = entity_index["by_file_and_name"]
    by_file_and_qname = entity_index["by_file_and_qname"]

    if method_path and method_qname:
        add_many(by_file_and_qname.get((method_path, method_qname), []))
    if method_path and method_qname_suffix:
        add_many(by_file_and_qname.get((method_path, method_qname_suffix), []))
    if method_path and method_simple_name:
        add_many(by_file_and_name.get((method_path, method_simple_name), []))
    if method_path:
        add_many(by_file.get(method_path, []))
    if method_qname:
        add_many(by_qualified_name.get(method_qname, []))
    if method_qname_suffix:
        add_many(by_qualified_name.get(method_qname_suffix, []))
    if method_simple_name:
        add_many(by_name.get(method_simple_name, []))

    # conservative fallback
    if not candidates:
        add_many(all_entities)

    return candidates


def _score_method_entity_match(
    method_path: str,
    method_qname: str,
    method_qname_suffix: str,
    method_simple_name: str,
    method_start: int,
    method_end: int,
    entity: EnreEntity,
) -> Tuple[float, List[str], Dict[str, Any]]:
    score = 0.0
    strategy: List[str] = []

    entity_path = _normalize_path(entity.file_path) if entity.file_path else ""
    entity_qname = entity.qualified_name or ""
    entity_qname_suffix = _scope_suffix_name(entity_qname)
    entity_simple_name = _simple_name_from_qualified_name(entity_qname)

    # 1. file path match
    if method_path and entity_path:
        if method_path == entity_path:
            score += 0.38
            strategy.append("normalized_file_path_exact")
        elif method_path.endswith(entity_path) or entity_path.endswith(method_path):
            score += 0.22
            strategy.append("normalized_file_path_suffix")

    # 2. qualified name / suffix match
    if method_qname and entity_qname:
        if method_qname == entity_qname:
            score += 0.30
            strategy.append("qualified_name_exact")
        elif _qualified_name_suffix_match(method_qname, entity_qname):
            score += 0.24
            strategy.append("qualified_name_suffix")

    if method_qname_suffix and entity_qname_suffix and method_qname_suffix == entity_qname_suffix:
        if "qualified_name_exact" not in strategy and "qualified_name_suffix" not in strategy:
            score += 0.18
            strategy.append("scope_suffix_exact")

    # 3. simple name match
    if method_simple_name and entity_simple_name and method_simple_name == entity_simple_name:
        score += 0.12
        strategy.append("simple_name_exact")

    # 4. line overlap / distance
    overlap_ratio = _line_overlap_ratio(
        method_start,
        method_end,
        entity.start_line,
        entity.end_line,
    )
    line_distance = _range_distance(method_start, method_end, entity.start_line, entity.end_line)
    if overlap_ratio > 0:
        score += min(0.30, 0.30 * overlap_ratio)
        strategy.append("line_range_overlap")
    else:
        if line_distance == 0:
            score += 0.18
            strategy.append("line_range_touching")
        elif line_distance <= 2:
            score += 0.10
            strategy.append("line_range_near_2")
        elif line_distance <= 5:
            score += 0.05
            strategy.append("line_range_near_5")
        elif (
            entity_path
            and method_path
            and entity_path == method_path
            and _qualified_name_suffix_match(method_qname or method_qname_suffix, entity_qname)
        ):
            # Allow low-confidence fallback when ENRE preserves fewer occurrences than Step1.
            score += 0.03
            strategy.append("nearest_line_fallback")

    # 5. tiny category bonus for direct callable types
    if entity.category in CALLABLE_ENTITY_CATEGORIES:
        score += 0.02

    debug_info = {
        "line_overlap_ratio": overlap_ratio,
        "line_distance": line_distance,
    }
    return min(1.0, score), strategy, debug_info


# ============================================================
# Utility helpers
# ============================================================

def _line_overlap_ratio(a_start: int, a_end: int, b_start: int, b_end: int) -> float:
    if a_end < a_start or b_end < b_start:
        return 0.0

    overlap_start = max(a_start, b_start)
    overlap_end = min(a_end, b_end)
    if overlap_end < overlap_start:
        return 0.0

    overlap = overlap_end - overlap_start + 1
    a_span = max(1, a_end - a_start + 1)
    b_span = max(1, b_end - b_start + 1)
    return overlap / max(a_span, b_span)


def _range_distance(a_start: int, a_end: int, b_start: int, b_end: int) -> int:
    if a_end < b_start:
        return b_start - a_end
    if b_end < a_start:
        return a_start - b_end
    return 0


def _simple_name_from_qualified_name(name: str) -> str:
    if not name:
        return ""
    return name.split("::")[-1].strip()


def _scope_suffix_name(name: str) -> str:
    if not name:
        return ""
    parts = [part.strip() for part in name.split("::") if part.strip()]
    if len(parts) >= 2:
        return "::".join(parts[-2:])
    return parts[-1] if parts else ""


def _qualified_name_suffix_match(lhs: str, rhs: str) -> bool:
    if not lhs or not rhs:
        return False
    if lhs == rhs:
        return True
    return lhs.endswith(f"::{rhs}") or rhs.endswith(f"::{lhs}") or lhs.endswith(rhs) or rhs.endswith(lhs)


def _normalize_path(path: Optional[str]) -> str:
    if not path:
        return ""
    return path.replace("\\", "/").strip()


def _safe_int(value: Any) -> Optional[int]:
    try:
        if value is None:
            return None
        return int(value)
    except Exception:
        return None


def _safe_str(value: Any) -> Optional[str]:
    if value is None:
        return None
    text = str(value).strip()
    return text if text else None