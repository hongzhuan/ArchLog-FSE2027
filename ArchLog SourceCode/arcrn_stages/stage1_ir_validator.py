from __future__ import annotations

from typing import Set

from .models import ChangeIR, ValidationIssue, ValidationReport


def validate_stage1_change_ir(change_ir: ChangeIR) -> ValidationReport:
    report = ValidationReport()
    seen_unit_ids: Set[str] = set()

    for commit in change_ir.commits:
        if not commit.commit_id:
            report.issues.append(
                ValidationIssue(
                    level="warning",
                    message="Commit record missing commit_id.",
                )
            )

        if not commit.commit_message and not commit.commit_summary:
            report.issues.append(
                ValidationIssue(
                    level="warning",
                    message="Commit record has neither commit_message nor commit_summary.",
                    commit_id=commit.commit_id,
                )
            )

        if commit.file_count == 0:
            report.issues.append(
                ValidationIssue(
                    level="warning",
                    message="Commit record has no changed files.",
                    commit_id=commit.commit_id,
                )
            )

        has_hunk_level_fallback = any(
            unit.evidence_granularity != "method_level"
            for unit in commit.change_units
        )

        if commit.method_count == 0 and not has_hunk_level_fallback:
            report.issues.append(
                ValidationIssue(
                    level="warning",
                    message="Commit record has no changed methods.",
                    commit_id=commit.commit_id,
                )
            )

        if commit.change_unit_count != len(commit.change_units):
            report.issues.append(
                ValidationIssue(
                    level="warning",
                    message="change_unit_count does not match actual change_units length.",
                    commit_id=commit.commit_id,
                )
            )

        for unit in commit.change_units:
            if not unit.change_unit_id:
                report.issues.append(
                    ValidationIssue(
                        level="warning",
                        message="Change unit missing change_unit_id.",
                        commit_id=commit.commit_id,
                    )
                )
                continue

            if unit.change_unit_id in seen_unit_ids:
                report.issues.append(
                    ValidationIssue(
                        level="warning",
                        message="Duplicate change_unit_id detected.",
                        commit_id=commit.commit_id,
                        change_unit_id=unit.change_unit_id,
                    )
                )
            else:
                seen_unit_ids.add(unit.change_unit_id)

            if not unit.summary:
                report.issues.append(
                    ValidationIssue(
                        level="warning",
                        message="Change unit has no summary.",
                        commit_id=commit.commit_id,
                        change_unit_id=unit.change_unit_id,
                    )
                )

            if not unit.changed_files:
                report.issues.append(
                    ValidationIssue(
                        level="warning",
                        message="Change unit has no changed_files.",
                        commit_id=commit.commit_id,
                        change_unit_id=unit.change_unit_id,
                    )
                )

            if not unit.changed_methods and unit.evidence_granularity == "method_level":
                report.issues.append(
                    ValidationIssue(
                        level="warning",
                        message="Change unit has no changed_methods.",
                        commit_id=commit.commit_id,
                        change_unit_id=unit.change_unit_id,
                    )
                )

    return report
