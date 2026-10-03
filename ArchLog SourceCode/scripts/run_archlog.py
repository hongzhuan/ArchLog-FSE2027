from __future__ import annotations

import argparse
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config import build_config  # noqa: E402
from arcrn_pipeline import run_archlog_pipeline  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the ArchLog release-note generation pipeline.")
    parser.add_argument("--repo", required=True, type=Path, help="Path to the target git repository.")
    parser.add_argument("--base-ref", required=True, help="Base version tag or commit.")
    parser.add_argument("--new-ref", required=True, help="Target version tag or commit.")
    parser.add_argument("--output-dir", required=True, type=Path, help="Directory for ArchLog outputs.")
    parser.add_argument("--provider", default=None, help="Optional LLM provider override from config.py.")
    parser.add_argument("--reuse-external", action="store_true", help="Reuse existing ENRE/SemArc outputs when present.")
    parser.add_argument("--skip-external", action="store_true", help="Skip ENRE/SemArc preparation and use configured paths.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = build_config()
    config.repo_path = args.repo
    config.base_ref = args.base_ref
    config.new_ref = args.new_ref
    config.output_dir = args.output_dir
    config.external_analysis_enabled = not args.skip_external
    config.external_analysis_reuse_existing = bool(args.reuse_external)
    if args.provider:
        config.llm_provider = args.provider

    repo_name = config.repo_path.name
    config.enre_json_path = Path("outputs") / "external_artifacts" / repo_name / "ENRE" / f"{repo_name}-{config.new_ref}_out.json"
    config.semarc_output_dir = Path("outputs") / "external_artifacts" / "semarc_results"
    config.external_worktree_root = Path("repositories") / ".archlog_worktrees"
    config.enre_jar_path = Path("third_party") / "ENRE-CPP" / "ENRE-CPP.jar"
    config.semarc_executable_path = Path("third_party") / "SemArc" / "SemArcArcRN.exe"

    result = run_archlog_pipeline(config)
    print("ArchLog finished.")
    print(f"Output directory: {result.output_dir}")
    for key, value in sorted(result.final_outputs.items()):
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
