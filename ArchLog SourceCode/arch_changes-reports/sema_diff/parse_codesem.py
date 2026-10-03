"""ArchLog runtime helper."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


def normalize_path(p: str) -> str:
    p = p.replace("\\", "/")
    if p.startswith("./"):
        p = p[2:]
    return p


def _looks_like_file_path(s: str) -> bool:
    if not isinstance(s, str):
        return False
    s = s.strip()
    if len(s) < 3 or len(s) > 300:
        return False

    lower = s.lower()
    if lower.startswith(("http://", "https://")):
        return False

    exts = (
        ".c", ".cc", ".cpp", ".cxx", ".h", ".hpp", ".hh", ".hxx", ".m", ".mm",
        ".py", ".js", ".ts", ".java", ".kt", ".go", ".rs", ".cs", ".swift",
        ".md", ".txt", ".json", ".yml", ".yaml"
    )
    return any(lower.endswith(e) for e in exts)


def _choose_desc_from_dict(d: Dict[str, Any]) -> Optional[str]:
    for k in ("Functionality", "functionality"):
        v = d.get(k)
        if isinstance(v, str):
            t = v.strip()
            if len(t) >= 5:
                return t

    candidates = [
        "description", "desc", "summary", "semantics", "semantic", "meaning",
        "function", "purpose", "responsibility", "comment", "explain", "explanation",
        "content"
    ]
    for k in candidates:
        v = d.get(k)
        if isinstance(v, str):
            t = v.strip()
            if len(t) >= 5:
                return t

    for k, v in d.items():
        if not isinstance(v, str):
            continue
        if k.lower() in ("path", "file", "name", "filename", "fullpath", "relative_path"):
            continue
        t = v.strip()
        if len(t) >= 10:
            return t

    return None


def _extract_file_desc_pairs(obj: Any) -> List[Tuple[str, str]]:
    pairs: List[Tuple[str, str]] = []

    if isinstance(obj, dict):
        file_keys = ["file", "path", "filepath", "file_path", "filename", "name", "fullpath", "relative_path"]
        path_val: Optional[str] = None
        for fk in file_keys:
            v = obj.get(fk)
            if isinstance(v, str) and _looks_like_file_path(v):
                path_val = v
                break

        if path_val is not None:
            desc = _choose_desc_from_dict(obj)
            if desc:
                pairs.append((normalize_path(path_val), desc))

        for v in obj.values():
            pairs.extend(_extract_file_desc_pairs(v))

    elif isinstance(obj, list):
        for item in obj:
            pairs.extend(_extract_file_desc_pairs(item))

    return pairs


@dataclass(frozen=True)
class CodeSemIndex:
    file_to_desc: Dict[str, str]
    total_pairs_found: int
    source_path: str


def parse_codesem(json_path: Path) -> CodeSemIndex:
    data = json.loads(json_path.read_text(encoding="utf-8"))

    pairs: List[Tuple[str, str]] = []

    # NEW: fast path for {"summary": [ {file, Functionality}, ... ]}
    if isinstance(data, dict) and isinstance(data.get("summary"), list):
        for it in data["summary"]:
            if not isinstance(it, dict):
                continue
            fp = it.get("file")
            if isinstance(fp, str) and _looks_like_file_path(fp):
                desc = _choose_desc_from_dict(it)
                if desc:
                    pairs.append((normalize_path(fp), desc))
    else:
        # fallback: recursive extraction for other schemas
        pairs = _extract_file_desc_pairs(data)

    file_to_desc: Dict[str, str] = {}
    for fp, desc in pairs:
        if fp not in file_to_desc or len(desc) > len(file_to_desc[fp]):
            file_to_desc[fp] = desc

    return CodeSemIndex(
        file_to_desc=file_to_desc,
        total_pairs_found=len(pairs),
        source_path=str(json_path),
    )


def main() -> None:
    p = Path(r"C:\path\to\libuv-v1.49.1_CodeSem.json")
    if not p.exists():
        print(f"Not found: {p}")
        return

    idx = parse_codesem(p)
    print("CodeSem parsed.")
    print("source:", idx.source_path)
    print("pairs found:", idx.total_pairs_found)
    print("unique files:", len(idx.file_to_desc))

    for i, (k, v) in enumerate(list(idx.file_to_desc.items())[:5]):
        print(f"\n[{i}] {k}\n{v[:200]}{'...' if len(v) > 200 else ''}")


if __name__ == "__main__":
    main()
