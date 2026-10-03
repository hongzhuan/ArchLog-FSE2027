# Code Change Pipeline

`code_changes/` implements ArchLog's commit-level change summary pipeline.

Responsibilities:
- locate changed methods from version differences;
- align methods with commits, ENRE entities, call graph context, and diff hunks;
- build commit-level `ChangeUnit` records;
- generate one evidence-grounded summary for each `ChangeUnit`.

This subpipeline feeds later ArchLog stages. It is not the final release-note composer.
Use `code_changes.pipeline.run_code_change_pipeline()` as the public entry point.

The returned `result.artifacts` contains structured step outputs, and `result.report`
contains execution records and statistics.
