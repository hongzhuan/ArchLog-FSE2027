"""ArchLog runtime helper."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


def _as_text(v: Any) -> Optional[str]:
    if isinstance(v, str):
        t = v.strip()
        return t if t else None
    return None


def _extract_patterns(obj: Any) -> List[str]:
    patterns: List[str] = []

    if isinstance(obj, dict):
        # NEW: single pattern field
        ap = obj.get("architecture_pattern")
        if isinstance(ap, str) and ap.strip():
            patterns.append(ap.strip())

        for key in ["patterns", "pattern", "arch_patterns", "architecture_patterns"]:
            v = obj.get(key)
            if isinstance(v, list):
                for it in v:
                    if isinstance(it, str) and it.strip():
                        patterns.append(it.strip())
                    elif isinstance(it, dict):
                        name = _as_text(it.get("name")) or _as_text(it.get("pattern")) or _as_text(it.get("type"))
                        if name:
                            patterns.append(name)

        for v in obj.values():
            patterns.extend(_extract_patterns(v))

    elif isinstance(obj, list):
        for it in obj:
            patterns.extend(_extract_patterns(it))

    seen = set()
    out = []
    for p in patterns:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def _build_component_summary(d: Dict[str, Any]) -> Optional[str]:
    name = _as_text(d.get("name")) or _as_text(d.get("component")) or _as_text(d.get("id"))
    if not name:
        return None

    parts: List[str] = []

    # NEW: nested[*].content
    nested = d.get("nested")
    if isinstance(nested, list):
        for it in nested:
            if not isinstance(it, dict):
                continue
            c = _as_text(it.get("content"))
            if c:
                parts.append(c)

    desc_fields = ["description", "desc", "summary", "semantics", "responsibility", "role", "intent"]
    for f in desc_fields:
        t = _as_text(d.get(f))
        if t:
            parts.append(t)

    seen = set()
    uniq_parts = []
    for p in parts:
        if p not in seen:
            seen.add(p)
            uniq_parts.append(p)

    if not uniq_parts:
        return None

    summary = "\n".join(uniq_parts).strip()
    return summary if summary else None


def _extract_component_summaries(obj: Any) -> Dict[str, str]:
    comp_to_sum: Dict[str, str] = {}

    if isinstance(obj, dict):
        for key in ["components", "component", "subsystems", "modules", "architecture", "arch"]:
            v = obj.get(key)
            if isinstance(v, list):
                for it in v:
                    if isinstance(it, dict):
                        name = _as_text(it.get("name")) or _as_text(it.get("component")) or _as_text(it.get("id"))
                        if not name:
                            continue
                        s = _build_component_summary(it)
                        if s:
                            if name not in comp_to_sum or len(s) > len(comp_to_sum[name]):
                                comp_to_sum[name] = s

        name = _as_text(obj.get("name")) or _as_text(obj.get("component"))
        if name:
            s = _build_component_summary(obj)
            if s:
                if name not in comp_to_sum or len(s) > len(comp_to_sum[name]):
                    comp_to_sum[name] = s

        for v in obj.values():
            sub = _extract_component_summaries(v)
            for k, s in sub.items():
                if k not in comp_to_sum or len(s) > len(comp_to_sum[k]):
                    comp_to_sum[k] = s

    elif isinstance(obj, list):
        for it in obj:
            sub = _extract_component_summaries(it)
            for k, s in sub.items():
                if k not in comp_to_sum or len(s) > len(comp_to_sum[k]):
                    comp_to_sum[k] = s

    return comp_to_sum


@dataclass(frozen=True)
class ArchSemIndex:
    patterns: List[str]
    component_to_summary: Dict[str, str]
    source_path: str


def parse_archsem(json_path: Path) -> ArchSemIndex:
    data = json.loads(json_path.read_text(encoding="utf-8"))
    patterns = _extract_patterns(data)
    comp_to_sum = _extract_component_summaries(data)

    return ArchSemIndex(
        patterns=patterns,
        component_to_summary=comp_to_sum,
        source_path=str(json_path),
    )


def main() -> None:
    p = Path(r"C:\path\to\libuv-v1.49.1_ArchSem.json")
    if not p.exists():
        print(f"Not found: {p}")
        return

    idx = parse_archsem(p)
    print("ArchSem parsed.")
    print("source:", idx.source_path)
    print("patterns:", idx.patterns[:10])
    print("components:", len(idx.component_to_summary))

    for i, (k, v) in enumerate(list(idx.component_to_summary.items())[:5]):
        print(f"\n[{i}] {k}\n{v[:200]}{'...' if len(v) > 200 else ''}")


if __name__ == "__main__":
    main()
