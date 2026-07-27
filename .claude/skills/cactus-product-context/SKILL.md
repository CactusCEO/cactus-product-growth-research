---
name: cactus-product-context
description: Ground Cactus product, design, engineering, go-to-market, onboarding, analytics, roadmap, PRD, prioritization, and ticket decisions in the validated customer-transcript evidence and Cactus 1.0/2.0 PostHog snapshot. Use for any Cactus feature proposal, UX flow, implementation plan, instrumentation spec, architecture tradeoff, revenue-impact assessment, migration question, or request to explain what customers need and what the team should build next.
---

# Cactus Product Context

Use this skill as the evidence layer for Cactus product work. Treat the bundled
2026-07-27 snapshot as a baseline, not as timeless truth.

Resolve every relative resource path below against the directory containing this
`SKILL.md`, even when the current working directory is another repository.

## Core workflow

1. Define the decision, target user, workflow, and intended business outcome.
2. Load `references/executive-context.md`.
3. Load only the additional references needed:
   - Quantitative or customer-evidence claims: `references/evidence-baselines.md`.
   - Priority, scope, dependency, or sequencing questions:
     `references/roadmap-and-gates.md`.
   - Analytics implementation, schemas, or source access:
     `references/data-map.md`.
4. For initiative-specific work, run:

   ```bash
   python "<skill-directory>/scripts/context_query.py" initiative "<initiative or keyword>"
   ```

5. Classify every behavioral claim as **Cactus 1.0**, **Cactus 2.0**, or
   **cross-version**.
6. Separate evidence from inference. Label unmeasured claims as hypotheses.
7. Tie the recommendation to a primary metric, revenue mechanism, decision gate,
   dependencies, and quality guardrails.
8. Prefer the smallest end-to-end vertical slice that can test the hypothesis.

## Evidence rules

- Use **Cactus 1.0** as the legacy behavior benchmark: proven jobs and historical
  usage intensity.
- Use **Cactus 2.0** as the current-product baseline: activation, discoverability,
  completion, reliability, collaboration, and scalable adoption.
- Use **cross-version** only for migration questions. Treat comparisons as
  directional unless event, route, population, identity, and date-window parity is
  verified.
- Never add Cactus 1.0 and Cactus 2.0 user counts without cross-project identity
  resolution.
- Never interpret declining Cactus 1.0 activity during migration, by itself, as
  churn or declining demand.
- Prefer current live data when the user provides it. State the date and explain
  any conflict with the bundled snapshot.
- Do not turn transcript theme counts into survey percentages. Meetings can support
  several themes and are not independent market samples.
- Do not claim feature ROI without joined product, CRM, billing, support-cost, and
  account-value data.

## Decision framing

Distinguish two rankings:

- **Unconstrained business impact:** Trust Center, Model Studio, Instant Deal Screen,
  Market Intelligence, Guided Evaluation, Enterprise Workflow, Scenario Lab,
  Development Underwriter, Commercial Lease Intelligence, Decision Packages.
- **Execution order:** telemetry, Guided Evaluation, Trust Center, Instant Deal
  Screen, Market Intelligence, Model Studio, Enterprise Workflow, Scenario Lab,
  Decision Packages, Development Underwriter, Commercial Lease Intelligence.

The lists differ because measurement, activation, trust, and shared platform
dependencies must unlock the higher-ACV bets.

## Output contract

For product recommendations, include:

1. Decision and target outcome.
2. User problem or job.
3. Evidence grouped by Cactus 1.0, Cactus 2.0, transcript evidence, and inference.
4. Revenue mechanism.
5. Proposed first vertical slice and explicit non-goals.
6. Primary metric, decision gate, and guardrails.
7. Dependencies, instrumentation, and unresolved evidence gaps.

For engineering plans or tickets, also include:

- stable account, organization, user, and deal identity needs;
- required events and properties;
- loading, empty, error, retry, partial-success, and permission states;
- auditability and human confirmation for material AI/model changes;
- rollout, migration, and compatibility constraints;
- acceptance criteria that are observable rather than subjective.

## Context efficiency

- Do not load the PDFs by default; use Markdown and CSV/JSON sources.
- Do not load every dataset for a narrow question.
- Run `python "<skill-directory>/scripts/context_query.py" summary` for a compact
  orientation.
- Run `python "<skill-directory>/scripts/context_query.py" search "<term>"` when the
  initiative name is unclear.
- Read the detailed public reports only when a claim needs more narrative context.

## Privacy and safety

- This skill contains only aggregate, public-redacted evidence.
- Do not invent customer identities or reconstruct removed quotations.
- Do not put raw transcripts, meeting metadata, private Sybill links, person-level
  PostHog events, account properties, credentials, CRM data, or billing data in a
  public artifact.
- Use an access-controlled system for secured sources. See
  `references/data-map.md`.

## Maintenance

Run these checks after changing the source datasets:

```bash
python "<skill-directory>/scripts/sync_snapshot.py"
python "<skill-directory>/scripts/context_query.py" validate
```

Then run the platform-neutral skill validator described in the repository README.
