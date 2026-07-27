# Cactus Product Growth Research

This public, redacted research package converts aggregate customer conversations and
Cactus product analytics into an outcome-based product strategy and roadmap.

## Read the complete report

- [Download the combined 38-page PDF](pdf/cactus-product-growth-research-packet-2026-07-27.pdf)

## Individual reports

| Report | Markdown | Readable PDF |
|---|---|---|
| Growth and revenue product plan | [Read](docs/cactus-growth-revenue-product-plan.md) | [Download](pdf/cactus-growth-revenue-product-plan.pdf) |
| PostHog product evidence | [Read](docs/cactus-posthog-product-evidence.md) | [Download](pdf/cactus-posthog-product-evidence.pdf) |
| Product opportunity portfolio | [Read](docs/cactus-product-opportunity-portfolio.md) | [Download](pdf/cactus-product-opportunity-portfolio.pdf) |
| Growth and revenue roadmap | [Read](docs/cactus-growth-revenue-roadmap.md) | [Download](pdf/cactus-growth-revenue-roadmap.pdf) |

## Developer data package

The [`data/`](data/) directory contains the structured, machine-readable evidence
behind the recommendations:

- aggregate Cactus 1.0 and Cactus 2.0 PostHog metrics;
- PostHog metric definitions and known limitations;
- transcript-corpus size and scope;
- transcript opportunity and signal counts;
- the integrated priority scorecard;
- the execution roadmap dataset;
- a data catalog and secure-source access guide.

Start with the [developer data guide](data/README.md). Raw customer transcripts,
participant identities, private recordings, person-level events, and account-level
properties are not stored in this public repository.

## Product-version evidence model

- **Cactus 1.0** is the legacy behavior benchmark: which jobs users repeatedly
  performed and how intensely they used them.
- **Cactus 2.0** is the current-product baseline: activation, discoverability,
  workflow completion, reliability, collaboration, and scalable adoption.
- **Cross-version evidence** tests whether proven Cactus 1.0 jobs were preserved and
  improved in Cactus 2.0. Comparisons are directional unless event definitions,
  populations, routes, and time windows are verified as equivalent.

## Privacy

This is the public redacted edition. Direct customer identities, verbatim quotes,
private Sybill recording links, account-level data, and authenticated PostHog links
are excluded. Aggregate evidence, methodology, caveats, prioritization, and product
recommendations are retained.

## Important caveat

This research supports prioritization and validation planning. It is not a causal
revenue forecast, and the growth scores are not delivery commitments.
