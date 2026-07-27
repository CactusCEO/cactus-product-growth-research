# Data Map

## Bundled skill snapshot

The skill is self-contained. Use these files without needing the rest of the
repository:

| Reference | Grain |
|---|---|
| `posthog-metrics.csv` | One validated aggregate metric |
| `posthog-metric-definitions.csv` | One metric definition |
| `transcript-corpus-summary.json` | One redacted corpus summary |
| `opportunity-theme-counts.csv` | One prioritized opportunity |
| `priority-scorecard.csv` | One integrated opportunity score |
| `growth-revenue-roadmap.csv` | One initiative or shared enabler |
| `data-catalog.json` | One entry per public dataset |

## Full repository sources

When operating inside the cloned repository, prefer:

- `docs/` for narrative product context.
- `data/posthog/` for product-behavior metrics and definitions.
- `data/transcripts/` for corpus and theme aggregates.
- `data/prioritization/` for scores, sequencing, gates, and dependencies.
- `pdf/` only for human distribution.

## Join guidance

- `opportunity_slug` connects PostHog rows to opportunity-oriented work.
- `initiative`, `project`, and `existing_project_slug` connect transcript,
  scorecard, and roadmap rows.
- Names can change. Introduce stable project IDs before treating this snapshot as a
  production semantic layer.
- Preserve metric population and date range with every number.

## Source access

The public skill excludes raw transcripts, names, meeting metadata, recording URLs,
person-level PostHog events, account properties, CRM, and billing.

Authorized developers should request access to Sybill and both PostHog projects from
the internal Cactus owner and work in an access-controlled environment. Do not copy
secured source data into this public repository or its issue tracker.

## Refresh procedure

1. Re-run reviewed analysis against both PostHog projects and the secured transcript
   corpus.
2. Update the root `data/` snapshot.
3. Run `python scripts/sync_snapshot.py` from the skill directory.
4. Run `python scripts/context_query.py validate`.
5. Re-run the skill validator.
