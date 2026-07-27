#!/usr/bin/env python3
"""Query and validate the bundled Cactus product-context snapshot."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path


REFERENCES = Path(__file__).resolve().parents[1] / "references"

FILES = {
    "catalog": "data-catalog.json",
    "posthog": "posthog-metrics.csv",
    "definitions": "posthog-metric-definitions.csv",
    "corpus": "transcript-corpus-summary.json",
    "themes": "opportunity-theme-counts.csv",
    "scorecard": "priority-scorecard.csv",
    "roadmap": "growth-revenue-roadmap.csv",
}

ALIASES = {
    "market-intelligence": "market-intelligence-memory",
    "model-studio": "model-studio-excel-bridge",
    "enterprise-workflow": "enterprise-workflow-governance",
    "commercial-lease": "commercial-lease-intelligence",
}

FORBIDDEN = (
    "https://app.sybill.ai/",
    "https://us.posthog.com/project/",
    "sybill_url",
    "evidence_excerpt",
)


def read_csv(key: str) -> list[dict[str, str]]:
    with (REFERENCES / FILES[key]).open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def read_json(key: str):
    return json.loads((REFERENCES / FILES[key]).read_text(encoding="utf-8"))


def validate() -> dict:
    missing = [name for name in FILES.values() if not (REFERENCES / name).is_file()]
    if missing:
        raise ValueError(f"Missing reference files: {missing}")

    posthog = read_csv("posthog")
    themes = read_csv("themes")
    roadmap = read_csv("roadmap")
    scorecard = read_csv("scorecard")
    definitions = read_csv("definitions")
    catalog = read_json("catalog")

    if {row["product_version"] for row in posthog} != {"Cactus 1.0", "Cactus 2.0"}:
        raise ValueError("PostHog snapshot must include Cactus 1.0 and Cactus 2.0")
    if len(posthog) != 12 or len(definitions) != 12:
        raise ValueError("Unexpected PostHog snapshot size")
    if len(themes) != 10 or not all(row["total_transcripts"] == "946" for row in themes):
        raise ValueError("Unexpected transcript theme snapshot")
    if len(roadmap) != 11 or len(scorecard) != 10:
        raise ValueError("Unexpected prioritization snapshot")
    if len(catalog.get("datasets", [])) != 7:
        raise ValueError("Unexpected data catalog")

    combined = "\n".join(
        (REFERENCES / name).read_text(encoding="utf-8", errors="ignore")
        for name in FILES.values()
    )
    for forbidden in FORBIDDEN:
        if forbidden in combined:
            raise ValueError(f"Forbidden public-source token found: {forbidden}")
    if re.search(
        r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b",
        combined,
        re.I,
    ):
        raise ValueError("Conversation-like UUID found in public snapshot")

    return {
        "status": "valid",
        "snapshot_date": "2026-07-27",
        "posthog_metrics": len(posthog),
        "metric_definitions": len(definitions),
        "transcript_opportunities": len(themes),
        "roadmap_rows": len(roadmap),
        "scorecard_rows": len(scorecard),
    }


def summary() -> dict:
    corpus = read_json("corpus")
    posthog = read_csv("posthog")
    roadmap = sorted(
        read_csv("roadmap"),
        key=lambda row: int(row["execution_order"]),
    )
    selected_metrics = [
        row
        for row in posthog
        if row["opportunity_slug"]
        in {"portfolio", "guided-activation", "instant-deal-screen", "market-intelligence-memory"}
    ]
    return {
        "snapshot_date": "2026-07-27",
        "included_transcripts": corpus["included_transcripts"],
        "product_versions": ["Cactus 1.0", "Cactus 2.0", "cross-version"],
        "execution_sequence": [row["initiative"] for row in roadmap],
        "orientation_metrics": selected_metrics,
    }


def matches(row: dict[str, str], term: str) -> bool:
    return term.casefold() in json.dumps(row, ensure_ascii=False).casefold()


def initiative(term: str) -> dict:
    roadmap = [row for row in read_csv("roadmap") if matches(row, term)]
    ranks = {
        row["business_impact_rank"]
        for row in roadmap
        if row.get("business_impact_rank", "").isdigit()
    }
    scorecard = [
        row
        for row in read_csv("scorecard")
        if matches(row, term) or row.get("rank") in ranks
    ]
    themes = [
        row
        for row in read_csv("themes")
        if matches(row, term) or row.get("business_impact_rank") in ranks
    ]

    slugs = {
        row.get("existing_project_slug", "")
        for row in roadmap
        if row.get("existing_project_slug")
    }
    expanded = set(slugs)
    for slug in list(slugs):
        expanded.add(ALIASES.get(slug, slug))
    posthog = [
        row
        for row in read_csv("posthog")
        if row["opportunity_slug"] in expanded or matches(row, term)
    ]

    return {
        "query": term,
        "roadmap": roadmap,
        "scorecard": scorecard,
        "transcript_evidence": themes,
        "posthog_evidence": posthog,
    }


def search(term: str, limit: int) -> dict:
    results = {}
    for key in ("posthog", "definitions", "themes", "scorecard", "roadmap"):
        rows = [row for row in read_csv(key) if matches(row, term)]
        if rows:
            results[key] = rows[:limit]
    corpus = read_json("corpus")
    if term.casefold() in json.dumps(corpus, ensure_ascii=False).casefold():
        results["corpus"] = corpus
    return {"query": term, "results": results}


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate")
    subparsers.add_parser("summary")
    initiative_parser = subparsers.add_parser("initiative")
    initiative_parser.add_argument("term")
    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("term")
    search_parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()

    try:
        if args.command == "validate":
            result = validate()
        elif args.command == "summary":
            result = summary()
        elif args.command == "initiative":
            result = initiative(args.term)
        else:
            result = search(args.term, args.limit)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
