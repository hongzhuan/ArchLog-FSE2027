from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional

from .models import FinalReleaseNoteDocument


def export_stage5_outputs(
    document: FinalReleaseNoteDocument,
    markdown: str,
    output_dir: Path,
    llm_audit_payloads: Optional[Dict[str, Any]] = None,
) -> Dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "final_release_note.json"
    markdown_path = output_dir / "final_release_note.md"

    with json_path.open("w", encoding="utf-8") as handle:
        json.dump(document.to_dict(), handle, ensure_ascii=False, indent=2)
    markdown_path.write_text(markdown, encoding="utf-8")

    output_files = {
        "final_release_note_json": str(json_path),
        "final_release_note_markdown": str(markdown_path),
    }

    if llm_audit_payloads:
        prompts_path = output_dir / "stage5_llm_prompts.json"
        responses_path = output_dir / "stage5_llm_responses.json"
        with prompts_path.open("w", encoding="utf-8") as handle:
            json.dump(llm_audit_payloads.get("stage5_llm_prompts") or {}, handle, ensure_ascii=False, indent=2)
        with responses_path.open("w", encoding="utf-8") as handle:
            json.dump(llm_audit_payloads.get("stage5_llm_responses") or {}, handle, ensure_ascii=False, indent=2)
        output_files["stage5_llm_prompts"] = str(prompts_path)
        output_files["stage5_llm_responses"] = str(responses_path)

    return output_files
