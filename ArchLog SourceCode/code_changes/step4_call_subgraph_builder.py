from __future__ import annotations

import logging
from collections import defaultdict, deque
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

from .constants import (
    CALLABLE_ENTITY_CATEGORIES,
    DEFAULT_CONTEXT_RELATION_TYPES,
    DEFAULT_LOGGER_NAME,
)
from .models import (
    EnreEntity,
    EnreMatchedOutput,
    EnreRelation,
    GraphEdge,
    GraphNode,
    MethodContextGraph,
    MethodContextGraphsOutput,
    PipelineConfig,
)


LOGGER = logging.getLogger(DEFAULT_LOGGER_NAME)


# ============================================================
# Public entry
# ============================================================

def run_call_subgraph_builder(
    config: PipelineConfig,
    enre_matched_output: EnreMatchedOutput,
) -> MethodContextGraphsOutput:
    """
    Build local call/context subgraphs for changed methods matched to ENRE entities.

    Design:
    - one changed method -> one local graph
    - graph is centered on method.enre_entity_id
    - currently default to 1-hop caller/callee context
    - only callable entities are kept as nodes
    """
    entities = enre_matched_output.entities
    relations = enre_matched_output.relations
    methods = enre_matched_output.changed_methods

    entity_by_id = {entity.entity_id: entity for entity in entities}
    callable_entity_ids = {
        entity.entity_id for entity in entities
        if entity.category in CALLABLE_ENTITY_CATEGORIES
    }

    relation_filter = _resolve_relation_filter(config)
    outgoing, incoming = _build_relation_adjacency(
        relations=relations,
        callable_entity_ids=callable_entity_ids,
        relation_filter=relation_filter,
    )

    graphs: List[MethodContextGraph] = []
    for method in methods:
        if method.enre_entity_id is None:
            # unmatched method -> no graph
            continue

        if method.enre_entity_id not in entity_by_id:
            continue

        graph = _build_single_method_context_graph(
            method=method,
            entity_by_id=entity_by_id,
            outgoing=outgoing,
            incoming=incoming,
            max_hops=config.graph.max_hops,
            max_nodes=config.graph.max_nodes,
            max_edges=config.graph.max_edges,
        )
        graphs.append(graph)

    LOGGER.info(
        "Step4 call subgraph building finished: %d context graphs built from %d changed methods.",
        len(graphs),
        len(methods),
    )

    return MethodContextGraphsOutput(graphs=graphs)


# ============================================================
# Relation normalization / filtering
# ============================================================

def _resolve_relation_filter(config: PipelineConfig) -> Set[str]:
    configured = {
        _normalize_relation_type(x)
        for x in (config.graph.include_relation_types or [])
        if x
    }
    if configured:
        return configured

    return {
        _normalize_relation_type(x)
        for x in DEFAULT_CONTEXT_RELATION_TYPES
    }


def _normalize_relation_type(name: Optional[str]) -> str:
    if not name:
        return ""
    return str(name).strip().lower()


def _is_call_like_relation(relation_type: str, allowed: Set[str]) -> bool:
    norm = _normalize_relation_type(relation_type)
    if not norm:
        return False

    if norm in allowed:
        return True

    # tolerate ENRE naming variations
    if "call" in norm:
        return True
    if norm in {"invoke", "invokes", "callee", "caller"}:
        return True

    return False


# ============================================================
# Adjacency construction
# ============================================================

def _build_relation_adjacency(
    relations: Sequence[EnreRelation],
    callable_entity_ids: Set[int],
    relation_filter: Set[str],
) -> Tuple[Dict[int, List[EnreRelation]], Dict[int, List[EnreRelation]]]:
    outgoing: Dict[int, List[EnreRelation]] = defaultdict(list)
    incoming: Dict[int, List[EnreRelation]] = defaultdict(list)

    for relation in relations:
        if relation.src_entity_id not in callable_entity_ids:
            continue
        if relation.dst_entity_id not in callable_entity_ids:
            continue
        if not _is_call_like_relation(relation.relation_type, relation_filter):
            continue

        outgoing[relation.src_entity_id].append(relation)
        incoming[relation.dst_entity_id].append(relation)

    return outgoing, incoming


# ============================================================
# Graph building
# ============================================================

def _build_single_method_context_graph(
    method,
    entity_by_id: Dict[int, EnreEntity],
    outgoing: Dict[int, List[EnreRelation]],
    incoming: Dict[int, List[EnreRelation]],
    max_hops: int,
    max_nodes: int,
    max_edges: int,
) -> MethodContextGraph:
    entry_id = method.enre_entity_id
    assert entry_id is not None

    visited_nodes: Set[int] = set()
    kept_edges: List[EnreRelation] = []
    edge_keys: Set[Tuple[int, int, str, Optional[int], Optional[int]]] = set()

    queue = deque([(entry_id, 0)])
    visited_nodes.add(entry_id)

    while queue and len(visited_nodes) < max_nodes and len(kept_edges) < max_edges:
        current_id, depth = queue.popleft()
        if depth >= max_hops:
            continue

        neighbors = []
        neighbors.extend(outgoing.get(current_id, []))
        neighbors.extend(incoming.get(current_id, []))

        for rel in neighbors:
            edge_key = (
                rel.src_entity_id,
                rel.dst_entity_id,
                rel.relation_type,
                rel.start_line,
                rel.end_line,
            )
            if edge_key not in edge_keys:
                edge_keys.add(edge_key)
                kept_edges.append(rel)
                if len(kept_edges) >= max_edges:
                    break

            other_id = rel.dst_entity_id if rel.src_entity_id == current_id else rel.src_entity_id
            if other_id not in visited_nodes:
                visited_nodes.add(other_id)
                if len(visited_nodes) >= max_nodes:
                    break
                queue.append((other_id, depth + 1))

        if len(visited_nodes) >= max_nodes or len(kept_edges) >= max_edges:
            break

    nodes = _build_graph_nodes(
        entry_id=entry_id,
        visited_node_ids=visited_nodes,
        method=method,
        entity_by_id=entity_by_id,
        outgoing=outgoing,
        incoming=incoming,
    )
    edges = _build_graph_edges(kept_edges)

    changed_method_uids = [method.method_uid]

    graph_id = f"cg_{method.method_uid}"

    return MethodContextGraph(
        graph_id=graph_id,
        entry_method_uid=method.method_uid,
        entry_entity_id=entry_id,
        commit_id=method.primary_commit_id,
        nodes=nodes,
        edges=edges,
        changed_method_uids=changed_method_uids,
    )


def _build_graph_nodes(
    entry_id: int,
    visited_node_ids: Set[int],
    method,
    entity_by_id: Dict[int, EnreEntity],
    outgoing: Dict[int, List[EnreRelation]],
    incoming: Dict[int, List[EnreRelation]],
) -> List[GraphNode]:
    nodes: List[GraphNode] = []

    for entity_id in sorted(visited_node_ids):
        entity = entity_by_id.get(entity_id)
        if entity is None:
            continue

        role = _infer_node_role(
            entity_id=entity_id,
            entry_id=entry_id,
            outgoing=outgoing,
            incoming=incoming,
        )

        nodes.append(
            GraphNode(
                entity_id=entity.entity_id,
                qualified_name=entity.qualified_name,
                category=entity.category,
                file_path=entity.file_path,
                start_line=entity.start_line,
                end_line=entity.end_line,
                role=role,
            )
        )

    return nodes


def _infer_node_role(
    entity_id: int,
    entry_id: int,
    outgoing: Dict[int, List[EnreRelation]],
    incoming: Dict[int, List[EnreRelation]],
) -> str:
    if entity_id == entry_id:
        return "changed_method"

    is_callee = any(rel.src_entity_id == entry_id and rel.dst_entity_id == entity_id for rel in outgoing.get(entry_id, []))
    is_caller = any(rel.src_entity_id == entity_id and rel.dst_entity_id == entry_id for rel in incoming.get(entry_id, []))

    if is_caller and is_callee:
        return "caller_callee"
    if is_caller:
        return "caller"
    if is_callee:
        return "callee"
    return "context"


def _build_graph_edges(relations: Sequence[EnreRelation]) -> List[GraphEdge]:
    edges: List[GraphEdge] = []
    for rel in relations:
        edges.append(
            GraphEdge(
                src_entity_id=rel.src_entity_id,
                dst_entity_id=rel.dst_entity_id,
                relation_type=rel.relation_type,
                start_line=rel.start_line,
                end_line=rel.end_line,
            )
        )
    return edges