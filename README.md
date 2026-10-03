# ArchLog Artifact Package

This package contains the anonymized data and source code for the FSE 2027 submission **ArchLog: Architecture-Guided Change Selection and Aggregation for Release Note Generation**. It provides the ground truth, final release notes, experimental results, and implementations used to study release note generation for large and complex C/C++ systems.

ArchLog uses architecture knowledge to guide change selection and entry aggregation. Its three phases are **Multi-Source Change Evidence Construction**, **Key Design-Decision Commit Identification**, and **Architecture-Guided Entry Aggregation**. The resulting release notes organize key changes by architecture module and routine changes by generic category, with commit/PR traceability.

## Directory Layout

```text
Data Availability/
  Results/
    Groound truth/
    Outputs/
      ArchLog/
      SmartNote/
      Verlog/
      Textrank/
      Codex-Base/
      Codex-Arch/
    RQ1/
      OverallEffectiveness/
      ModuleReliability/
    RQ2/
    RQ3/
    RQ4/
  ArchLog SourceCode/
  Baselines SourceCode/
    SmartNote.md
    VerLog/
    TextRank.md
    Codex-Base.md
    Codex-Arch.md
```

## Data

- [Ground truth](Results/Groound%20truth/GT.json) contains 11,475 entries across 25 version pairs. Each entry records its version pair, GT identifier, change description, change category, supporting commits, and associated PRs.
- `Results/Outputs/<method>/<version-pair>/release_note.md` stores the final release-note document for each method and version pair. There are 150 documents: 25 for ArchLog and 25 for each of the five baselines.
- [RQ1: Effectiveness Evaluation](Results/RQ1/) contains one JSON/Markdown pair per method in `OverallEffectiveness/`. The JSON files record entry-level GT matches, and the Markdown files report Precision, Recall, F1, Important Recall, and Routine Recall. `ModuleReliability/Phase2.json` and `Phase2.md` report Key Design-Decision Commit Identification, with **key** as the positive class; `Phase3.json` and `Phase3.md` report Architecture-Guided Entry Aggregation, with **merge** as the positive class.
- [RQ2: Ablation Analyses](Results/RQ2/) contains one JSON/Markdown pair per ablation: `M2` is **w/o Key Identification**, `M3` is **w/o Attribution Evidence**, and `M4` is **w/o Guided Aggregation**. The full-method results are in `Results/RQ1/OverallEffectiveness/ArchLog.json` and `ArchLog.md`.
- [RQ3: User Study](Results/RQ3/) contains `rq3_user_study_scores.csv` for overall ratings and `rq3_user_study_by_repository.csv` for ratings by repository. Both files cover all six methods and the five dimensions: accuracy, coverage, readability, conciseness, and structural organization, using a 5-point Likert scale.
- [RQ4: Efficiency Evaluation](Results/RQ4/) contains `rq4_archlog_by_repository.csv` for runtime, LLM calls, token consumption, and average call time by repository, and `rq4_archlog_phase_cost.csv` for LLM calls, token consumption, average call time, and token share by component.

## Experimental Setup

The study covers five version pairs from each of Ceph, OpenSSL, DPDK, jemalloc, and zstd, totaling 25 version pairs and 21,185 commits. The version-pair identifiers below are used in the data and output directories.

| Project | Version-pair identifiers |
|---|---|
| Ceph | `ceph-v18.2.7-v18.2.8`, `ceph-v19.2.0-v19.2.1`, `ceph-v19.2.2-v19.2.3`, `ceph-v19.2.3-v19.2.4`, `ceph-v20.2.0-v20.2.1` |
| OpenSSL | `openssl-3.1.0-3.2.0`, `openssl-3.2.0-3.3.0`, `openssl-3.3.0-3.4.0`, `openssl-3.4.0-3.5.0`, `openssl-3.5.0-3.6.0` |
| DPDK | `dpdk-v24.07-v24.11`, `dpdk-v24.11-v25.03`, `dpdk-v25.03-v25.07`, `dpdk-v25.07-v25.11`, `dpdk-v25.11-v26.03` |
| jemalloc | `jemalloc-5.0.1-5.1.0`, `jemalloc-5.1.0-5.2.0`, `jemalloc-5.2.0-5.2.1`, `jemalloc-5.2.1-5.3.0`, `jemalloc-5.3.0-5.3.1` |
| zstd | `zstd-v1.5.1-v1.5.2`, `zstd-v1.5.2-v1.5.4`, `zstd-v1.5.4-v1.5.5`, `zstd-v1.5.5-v1.5.6`, `zstd-v1.5.6-v1.5.7` |

ArchLog is compared with SmartNote, VerLog, TextRank, Codex-Base, and Codex-Arch. ArchLog, SmartNote, and VerLog use DeepSeek-v4-Flash with the same model context limit and raw inputs. SmartNote and VerLog follow the prompts in their original papers. VerLog is adapted to C/C++ using ENRE for static parsing to support code-change detection and CMG construction. TextRank is the non-LLM extractive summarization baseline.

Codex-Base is the original general-purpose software engineering agent, which analyzes commits/PRs and source code in the specified version range to generate release notes. Codex-Arch augments it with raw SemArc architecture information for both versions and task prompts for module-related change identification and entry aggregation. Both configurations use the same base model and reasoning effort.

## Source Code

- [ArchLog SourceCode/README.md](ArchLog%20SourceCode/README.md) describes the requirements, LLM configuration, and commands for running ArchLog on a repository/version pair.
- `ArchLog SourceCode/requirements.txt` lists the Python dependencies.
- `ArchLog SourceCode/scripts/` contains the runnable entry point and environment check. `prompts/` contains the method's prompt templates, and `third_party/` contains the ENRE-CPP and SemArc components.
- [SmartNote.md](Baselines%20SourceCode/SmartNote.md) and [TextRank.md](Baselines%20SourceCode/TextRank.md) link to the baseline implementations.
- [VerLog/README.md](Baselines%20SourceCode/VerLog/README.md) describes the included C/C++ adaptation and its execution command.
- [Codex-Base.md](Baselines%20SourceCode/Codex-Base.md) describes the original Codex configuration; [Codex-Arch.md](Baselines%20SourceCode/Codex-Arch.md) describes the added architecture inputs, task prompt, and output template.
