from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    checks = {
        "java_on_path": shutil.which("java") is not None,
        "enre_jar_present": (ROOT / "third_party" / "ENRE-CPP" / "ENRE-CPP.jar").exists(),
        "semarc_entrypoint_present": (ROOT / "third_party" / "SemArc" / "SemArcArcRN.exe").exists(),
        "main_prompts_present": (ROOT / "prompts" / "phase3_final_composition_prompt.txt").exists(),
    }
    for name, ok in checks.items():
        print(f"{name}: {'OK' if ok else 'MISSING'}")
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
