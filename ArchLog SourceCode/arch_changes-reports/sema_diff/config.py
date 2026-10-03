"""ArchLog runtime helper."""

from __future__ import annotations

from dataclasses import dataclass, field
from sema_diff.denoise import DenoiseConfig

@dataclass(frozen=True)
class DiffConfig:
    rename_overlap: float = 0.90

    split_merge_overlap: float = 0.30

    coverage_threshold: float = 0.80

    module_count_delta_warn_ratio: float = 0.30

    enable_occurrence_disambiguation: bool = True

    normalize_path_separators: bool = True

    denoise: DenoiseConfig = field(
        default_factory=lambda: DenoiseConfig(
            enabled=True,
            drop_module_renamed=True,
            drop_renamed_if_has_other_events_same_pair=True,
            keep_rename_if_only=False,  #
            drop_rename_if_unknown_name=True,
        )
    )


def default_config() -> DiffConfig:
    return DiffConfig()


def main() -> None:
    cfg = default_config()
    print("Default DiffConfig:")
    print(cfg)


if __name__ == "__main__":
    main()
