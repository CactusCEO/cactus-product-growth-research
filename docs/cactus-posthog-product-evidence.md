# Cactus PostHog behavioral evidence

**Analysis date:** 2026-07-27

## Executive readout

- Cactus 1.0 external identified monthly activity declined from 118 users in July 2025 to 24 in partial July 2026.
- Cactus 2.0 external identified monthly activity grew from 33 users in December 2025 to 64 in June 2026; partial July recorded 52.
- **Cactus 2.0:** activation is the largest measured current-product growth constraint: 91 of 329 test-filtered signups reached chat, extraction, or template creation within 14 days (27.7%).
- **Cactus 2.0:** mature identified-user cohorts retained at 43.3% in week 1 and 18.6% in week 4; cohort sizes are small.
- **Cactus 2.0:** Market Analysis is the broadest verified current custom workflow: 1,415 messages from 85 external users across 50 organizations.
- **Cross-version:** Quick Analysis was the strongest measured **Cactus 1.0** habit, with 100,593 pageviews from 215 external identified users, while only 3 users reached the named **Cactus 2.0** quick-analysis route.
- **Cactus 2.0:** Trust and Excel pipelines show meaningful use plus reliability work: extraction converted 85.3% of test-filtered users within one day; Excel extraction recorded 327 successes and 15 failures.

## How product versions are used

- **Cactus 1.0** is the legacy behavior benchmark: it identifies proven user jobs and historical usage intensity.
- **Cactus 2.0** is the current-product baseline: it measures whether the refactor improves discoverability, completion, trust, repeat use, and scalability.
- **Cross-version comparisons** identify migration gaps. They are directional unless the underlying events, routes, populations, and time windows have been verified as equivalent.
- A strong Cactus 1.0 signal can justify preserving a job, but it cannot establish that the Cactus 2.0 implementation is successful.
- A weak Cactus 2.0 signal does not automatically invalidate the job when Cactus 1.0 demand was strong; it can instead indicate missing parity, discoverability, or instrumentation.
- Declining Cactus 1.0 activity during migration is not, by itself, evidence of declining demand or churn.
- Active-user counts across Cactus 1.0 and 2.0 must not be added until cross-project identity resolution prevents double counting.

## Opportunity evidence

| Rank | Opportunity | Behavioral evidence | Strength |
|---:|---|---|---|
| 1 | Trust Center 2.0 - Exception-First Document Review | Cactus 2.0: 29 of 34 test-filtered users completed extraction within one day (85.3%); median conversion was 40.8 seconds and average was 105.5 seconds. Across raw pipeline events, 514 extraction completions covered 41 users. Confidence verification averaged 0.766 confidence and 948.8 source matches across 1,362.1 verified facts per run. Workflow routes logged 1,422 exceptions affecting 35 external users, although a benign ResizeObserver issue dominates the grouped error list. | Strong, narrow cohort |
| 2 | Market Intelligence - Evidence-Backed Comps and Memory | Cactus 2.0 external usage: market-analysis generated 1,415 submitted messages from 85 users across 50 organizations (16.6 messages per user), making it the broadest verified custom workflow in the current product. | Strong and broad |
| 3 | Instant Deal Screen - Intake-to-Go/No-Go | Cactus 1.0 external identified usage: Quick Analysis generated 100,593 pageviews from 215 users over the last twelve months (467.9 views per user). The comparable Cactus 2.0 quick-analysis route recorded only 18 pageviews from 3 users, indicating a valuable legacy job that has not visibly migrated. | Strong legacy habit; migration gap |
| 4 | Model Studio - Formula-Aware Excel Roundtrip | Cactus 2.0 recorded 342 Excel extraction completions across 31 users: 327 successes and 15 failures (95.6% event-level success), with successful runs averaging 147.6 seconds. Several workbook-related LLM steps show 18-40% failure rates, and active error tracking includes worksheet-name collisions. | Strong technical signal; moderate reach |
| 5 | Guided Activation - First Defensible Deal | Only 91 of 329 test-filtered Cactus 2.0 signups reached a meaningful action (chat submission, extraction start, or template creation) within 14 days: 27.7% conversion. Converters reached value quickly (median 8.0 minutes), so the primary problem is getting more new users onto the successful path. Mature identified-user cohorts retained at 43.3% in week 1 and 18.6% in week 4, with small denominators. | Strong growth constraint |
| 6 | Scenario Lab - Conversational Sensitivity With Controls | Cactus 2.0 chat is established: 90 of 106 test-filtered submitters received an assistant completion within ten minutes (84.9%), with a 2.1-second median and 16.2-second average. No dedicated scenario-created, confirmed-change, or scenario-compared event exists, so scenario demand is inferred from chat and transcripts rather than directly measured. | Strong adjacent behavior; missing scenario event |
| 7 | Enterprise Workflow - Integrations, Roles, and Governance | Cactus 2.0 logged 36 organization invitations from 18 organizations and 23 acceptances across 15 organizations. The roughly 64% event-level acceptance ratio is directional because sent and accepted events are not joined by invite. | Early but measurable |
| 8 | Development Underwriter - Cost, Draw, and Stabilization | Cactus 2.0 LLM steps tied to development-style tables show elevated failure: Unit Mix Table 40.9%, Project Stages Table 26.3%, and several cost-table steps 22-26%. Samples are small and do not establish a large active development cohort. | Technical pain; limited adoption evidence |
| 9 | Decision Packages - Source-Linked IC, Lender, and Client Outputs | Cactus 2.0 recorded 39 chat-share events across 13 users, while external report routes reached only 2 users. Package generation, approval, live views, export, and downstream decision events are not instrumented. | Weak or under-instrumented |
| 10 | Commercial Lease Intelligence - Multi-Tenant Underwriting | The test-filtered Cactus 2.0 rent-roll funnel included 4 triggering users and 2 completions within 30 minutes (50%; 74.9-second median among converters). Raw completion events covered only 6 users, too small for a broad build decision. | Very early sample |

## Measurement caveats

- The PostHog projects use UTC and person-on-events mode; person properties reflect event-time values.
- Known internal users were excluded from SQL aggregates using the company email domain when available. PostHog's configured test-account filter was used for funnel and retention queries.
- Cactus 1.0 pageviews contain substantial anonymous and automated traffic. Legacy adoption statements therefore use identified users and exclude known internal users.
- Several Cactus 2.0 server-side events label `environment` as `dev` even when paired with production-facing activity. Environment is not used as a production filter until instrumentation is corrected.
- Event taxonomy discovery omitted some older or dynamic events/properties that bounded SQL queries found. Every metric names its actual event population.
- The data-warehouse schema endpoint returned `INVALID_ARGUMENT` in both projects. Analyses used verified event/property schemas plus bounded HogQL and typed funnel/retention queries.
- `semantic_matching_prompt_too_long` has no discoverable properties, so its 790 occurrences across 22 raw users cannot be reliably attributed to a workflow.
- Scenario creation, deal approval/export, decision-package generation, dead clicks, and several revenue outcomes are not consistently instrumented. Absence of evidence is not evidence of low demand.
- July 2026 is partial through July 27. Small cohorts, especially rent-roll and development workflows, should not drive broad investment without a design-partner gate.

## PostHog projects

- Cactus 1.0: internal PostHog project; aggregate results are reported above.
- Cactus 2.0: internal PostHog project; aggregate results are reported above.

Machine-readable metrics are in `cactus_posthog_metrics_2026-07-27.csv`.

---

**Public redacted edition.** This document contains aggregate product research. Direct customer identities, verbatim quotes, private recordings, account-level data, and authenticated analytics links are intentionally excluded.
