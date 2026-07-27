#!/usr/bin/env python3
"""Synchronize the skill's bundled snapshot from the repository data directory."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


SKILL = Path(__file__).resolve().parents[1]
REPO = Path(__file__).resolve().parents[4]
REFERENCES = SKILL / "references"

MAPPING = {
    REPO / "data/catalog.json": REFERENCES / "data-catalog.json",
    REPO / "data/posthog/posthog_metrics_aggregate.csv": REFERENCES / "posthog-metrics.csv",
    REPO / "data/posthog/metric_definitions.csv": REFERENCES / "posthog-metric-definitions.csv",
    REPO / "data/transcripts/transcript_corpus_summary.json": REFERENCES / "transcript-corpus-summary.json",
    REPO / "data/transcripts/opportunity_theme_counts.csv": REFERENCES / "opportunity-theme-counts.csv",
    REPO / "data/prioritization/priority_scorecard.csv": REFERENCES / "priority-scorecard.csv",
    REPO / "data/prioritization/growth_revenue_roadmap.csv": REFERENCES / "growth-revenue-roadmap.csv",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    missing = [str(source) for source in MAPPING if not source.is_file()]
    if missing:
        print("Repository data files are unavailable:\n" + "\n".join(missing), file=sys.stderr)
        return 1

    stale = []
    for source, destination in MAPPING.items():
        if not destination.is_file() or source.read_bytes() != destination.read_bytes():
            stale.append(destination.name)
            if not args.check:
                shutil.copyfile(source, destination)

    if args.check and stale:
        print("Stale bundled references: " + ", ".join(stale), file=sys.stderr)
        return 1

    print("Snapshot is synchronized." if not stale or args.check else "Snapshot updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
