# Developer Data Guide

This directory contains the public, reproducible evidence snapshot used to construct
the Cactus product strategy. The snapshot date is 2026-07-27.

## Recommended reading order

1. Read the [growth and revenue plan](../docs/cactus-growth-revenue-product-plan.md).
2. Review [`catalog.json`](catalog.json) to understand the available datasets.
3. Load the PostHog aggregate snapshot and metric definitions.
4. Join transcript opportunity counts to the priority scorecard by initiative.
5. Use the roadmap dataset for sequencing, dependencies, metrics, and decision gates.
6. Read [`DATA_ACCESS.md`](DATA_ACCESS.md) before requesting secured raw sources.

## Directory map

| Path | Grain | Purpose |
|---|---|---|
| `posthog/posthog_metrics_aggregate.csv` | One row per validated metric | Fixed aggregate snapshot across Cactus 1.0 and 2.0 |
| `posthog/metric_definitions.csv` | One row per metric | Definitions, windows, and limitations |
| `transcripts/transcript_corpus_summary.json` | One corpus | Corpus scope and processing statistics |
| `transcripts/opportunity_theme_counts.csv` | One row per opportunity | Meeting-level prevalence and explicit-signal counts |
| `transcripts/curated_signal_summary.csv` | Opportunity and signal | Aggregate distribution in the 30-item traceability sample |
| `prioritization/priority_scorecard.csv` | One row per opportunity | Integrated transcript and product-behavior scoring |
| `prioritization/growth_revenue_roadmap.csv` | One row per initiative or enabler | Execution order, revenue mechanism, evidence scope, gates, and dependencies |

## Product-version rules

- **Cactus 1.0** metrics are legacy behavior benchmarks. They show established jobs
  and historical usage intensity.
- **Cactus 2.0** metrics describe the refactored product's current activation,
  adoption, reliability, and collaboration.
- **Cross-version** evidence identifies migration gaps. Do not assume event, route,
  population, or time-window equivalence unless it has been verified.
- Do not add Cactus 1.0 and Cactus 2.0 user counts without cross-project identity
  resolution.
- Declining Cactus 1.0 activity during migration is not, by itself, evidence of churn
  or declining demand.

## Transcript-count rules

- Counts are computed at meeting level so a long conversation does not become dozens
  of independent votes.
- One meeting can support multiple opportunities; rows are not additive.
- `matching_meetings` indicates a rule-based theme match.
- `explicit_signal_meetings` also contains pain, request, adoption, revenue, or trust
  language.
- Theme prevalence is directional qualitative evidence, not survey incidence.
- The curated 30-item signal sample was built for traceability, not statistical
  representation.

## PostHog-count rules

- Each metric carries its own population and date range; the rows are not one funnel.
- Test-account and internal-user filtering varies by metric and is documented in the
  population and limitation fields.
- Person properties in these projects reflect event-time values.
- Some Cactus 2.0 server events have inconsistent environment labels.
- July 2026 monthly values are partial through July 27.
- Product usage is not joined to billing or CRM in this snapshot, so revenue effects
  remain hypotheses rather than causal forecasts.

## Join keys

- `opportunity_slug` connects PostHog metrics to opportunity-oriented work.
- `initiative` or `project` connects transcript and prioritization datasets.
- Project names are human-readable and may change; introduce stable project IDs
  before using these files as a production semantic layer.

## First implementation priorities

1. Establish stable account, organization, user, and deal identity across Cactus 2.0.
2. Instrument evaluation start, meaningful action, approved/exported first result,
   human escalation, and paid conversion.
3. Instrument Cactus 1.0-to-2.0 migration for proven jobs, beginning with Quick
   Analysis.
4. Add the decision-gate metrics from the roadmap before activating full builds.
5. Join product usage to CRM, billing, onboarding labor, and support cost in a secure
   analytics environment.
