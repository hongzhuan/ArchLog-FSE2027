# ArchLog Source Code

This directory contains the anonymized, runnable source package for ArchLog.
ArchLog generates traceable release notes from a target repository and a pair of
versions by combining code-change evidence, architecture recovery, and
LLM-based aggregation.

## Package Layout

- `scripts/run_archlog.py` is the main command-line entry point.
- `scripts/check_environment.py` checks the bundled external tools and prompt
  files.
- `config.py` stores the default runtime configuration and LLM provider
  settings.
- `configs/archlog.example.yaml` gives a compact example configuration.
- `code_changes/` builds code-level change evidence from commits and diffs.
- `arch_changes-reports/` contains the SemArc output differ used by Phase 1.
- `prompts/` contains the prompt templates used by Phase 2 and Phase 3.
- `arcrn_stages/` contains shared stage helpers used by the pipeline.
- `third_party/ENRE-CPP/` contains the packaged ENRE-CPP runtime and source.
- `third_party/SemArc/` contains the packaged SemArc runtime.

## Method Phases

ArchLog follows the three phases described in the paper.

### Phase 1: Multi-Source Change Evidence Construction

Phase 1 takes a target repository plus a base and target version. It constructs
code-change evidence and architecture evidence.

- `code_changes/`, `run_code_changes.py`, and
  `phase1_change_evidence_builder.py` extract method-, hunk-, file-, commit-,
  and pull-request-level evidence.
- `third_party/ENRE-CPP/` is used to extract C/C++ entities and relations.
- `third_party/SemArc/` is used to recover architecture-level modules.
- `arcrn_external_analysis.py` prepares and reuses ENRE/SemArc outputs.
- `arch_changes-reports/` compares SemArc outputs across the two versions.

### Phase 2: Key Design-Decision Commit Identification

Phase 2 identifies commits that carry key design decisions and distinguishes
them from routine changes.

- `phase2_arch_signal_attributor.py` performs Module-Change Attribution and
  applies constrained LLM judgment to determine commit importance.
- `prompts/phase2_*.txt` stores the prompt templates for architecture event
  profiling, relevance classification, and relevance summaries.

### Phase 3: Architecture-Guided Entry Aggregation

Phase 3 turns the Phase 1 and Phase 2 evidence into the final release note.

- `phase3_llm_aggregation_planner.py` plans commit handling and grouping.
- `phase3_slot_entry_generator.py` generates release-note entries.
- `phase3_arch_component_assignment.py` assigns important entries to recovered
  architecture modules.
- `phase3_release_note_composer.py` writes the final Markdown and JSON outputs.
- `prompts/phase3_*.txt` stores the prompt templates for planning, aggregation,
  assignment, and final composition.

The final traceable Markdown uses two top-level sections: `Important Changes`
and `Routine Changes`.

## Requirements

- Python 3.10 or newer.
- Java on `PATH`, required by ENRE-CPP.
- Git on `PATH`, required to inspect the target repository and version range.
- A target repository with both requested versions available as tags or commits.
- An API key for one supported LLM provider.

Install Python dependencies from this directory:

```bash
pip install -r requirements.txt
```

Check the local runtime:

```bash
python scripts/check_environment.py
```

The check should report `OK` for Java, ENRE-CPP, SemArc, and the main prompt
files.

## LLM Configuration

The default provider is selected in `config.py`. The bundled configuration
supports `qwen`, `mimo`, `deepseek`, and `siliconflow`; the default provider is
`siliconflow`.

Set the API key environment variable required by the selected provider. For the
default configuration:

```powershell
$env:SILICONFLOW_API_KEY = "your_api_key"
```

To use a different provider at run time, pass `--provider` with one of the
supported provider names.

## Running ArchLog

Run ArchLog on a repository/version pair:

```bash
python scripts/run_archlog.py --repo /path/to/repo --base-ref v1.0.0 --new-ref v1.1.0 --output-dir outputs/example
```

Use an existing ENRE/SemArc cache when present:

```bash
python scripts/run_archlog.py --repo /path/to/repo --base-ref v1.0.0 --new-ref v1.1.0 --output-dir outputs/example --reuse-external
```

If external analysis has already been prepared and paths are configured, skip
ENRE/SemArc preparation:

```bash
python scripts/run_archlog.py --repo /path/to/repo --base-ref v1.0.0 --new-ref v1.1.0 --output-dir outputs/example --skip-external
```

Use the built-in help to inspect all options:

```bash
python scripts/run_archlog.py --help
```

## Main Outputs

The output directory contains intermediate stage artifacts and the final release
note files. The main final outputs are:

- `final_release_note.md`: the final Markdown release note.
- `final_release_note_traceable.md`: the final Markdown release note with
  commit and pull-request trace links.
- `final_release_note.json`: structured final release-note data.
- `final_release_note_debug.md`: debug information emitted by the final
  composition stage.

## Packaging Policy

This source package intentionally excludes local git repositories, previous
experiment outputs, private workbooks, bulk experiment scripts, and manuscript
files. It keeps only the code, prompts, configuration, and third-party runtime
components needed to run ArchLog.
