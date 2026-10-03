"""ArchLog runtime helper."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional, List


REQUIRED_KEYS = ["NamedClusters", "ClusterComponent"]
OPTIONAL_KEYS = ["ArchSem", "CodeSem"]

SUFFIX_MAP = {
    "NamedClusters": "_NamedClusters.json",
    "ClusterComponent": "_ClusterComponent.json",
    "ArchSem": "_ArchSem.json",
    "CodeSem": "_CodeSem.json",
}


@dataclass(frozen=True)
class ResolvedInputs:
    mode: str  # always "dirs" for MVP
    version_a_root: Path
    version_b_root: Path
    version_a_files: Dict[str, Path]  # key -> file path
    version_b_files: Dict[str, Path]


def resolve_inputs_from_dirs(dir_a: Path, dir_b: Path) -> ResolvedInputs:
    if not dir_a or not dir_b:
        raise ValueError("Both dir_a and dir_b must be provided.")

    if not dir_a.exists() or not dir_a.is_dir():
        raise FileNotFoundError(f"Version A directory not found: {dir_a}")
    if not dir_b.exists() or not dir_b.is_dir():
        raise FileNotFoundError(f"Version B directory not found: {dir_b}")

    a_files = _find_semarc_jsons(dir_a)
    b_files = _find_semarc_jsons(dir_b)
    _validate_required(a_files, b_files)

    return ResolvedInputs(
        mode="dirs",
        version_a_root=dir_a,
        version_b_root=dir_b,
        version_a_files=a_files,
        version_b_files=b_files,
    )


def _find_semarc_jsons(root: Path) -> Dict[str, Path]:
    result: Dict[str, Path] = {}
    all_json = list(root.rglob("*.json"))

    for key, suf in SUFFIX_MAP.items():
        matches = [p for p in all_json if p.name.endswith(suf)]
        if not matches:
            continue
        matches.sort(key=lambda p: (len(str(p)), str(p)))
        result[key] = matches[0]

    return result


def _validate_required(a_files: Dict[str, Path], b_files: Dict[str, Path]) -> None:
    missing_a = [k for k in REQUIRED_KEYS if k not in a_files]
    missing_b = [k for k in REQUIRED_KEYS if k not in b_files]
    if missing_a or missing_b:
        raise RuntimeError(
            "Missing required SemArc json files:\n"
            f"  A missing: {missing_a}\n"
            f"  B missing: {missing_b}\n"
            f"Found A keys: {sorted(a_files.keys())}\n"
            f"Found B keys: {sorted(b_files.keys())}\n"
        )


def main() -> None:
    dir_a = Path(r"..\sema_results\libuv-1.49.0")
    dir_b = Path(r"..\sema_results\libuv-1.49.1")

    resolved = resolve_inputs_from_dirs(dir_a=dir_a, dir_b=dir_b)

    print("=== loader.main() test (dirs mode) ===")
    print(f"A root: {resolved.version_a_root}")
    print(f"B root: {resolved.version_b_root}")
    print("--- A files ---")
    for k, v in resolved.version_a_files.items():
        print(f"  {k}: {v}")
    print("--- B files ---")
    for k, v in resolved.version_b_files.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
