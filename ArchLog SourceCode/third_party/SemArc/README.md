# SemArc Runtime

This directory contains the packaged SemArc runtime used by ArchLog to generate
architecture-level module artifacts. Runtime caches, extracted results, LLM logs,
and previous outputs are intentionally excluded.

The ArchLog pipeline calls `SemArcArcRN.exe` with `--core-outputs-only` and
`--emit-progress`.
