# Cactus Vault and Shortcuts Product Direction

**Decision date:** 2026-07-27  
**Status:** Working product direction and four-week validation plan  
**Source context:** The Vault and MCP concept, Cactus 1.0 and Cactus 2.0
PostHog baselines, aggregate external-call transcript evidence, and the product
strategy conversation summarized below.

## Executive decision

Cactus should stop presenting itself primarily as a platform that users must learn.
The product should present a small set of outcome-oriented real-estate shortcuts
powered by a persistent, evidence-backed Vault.

> The shortcuts are the product users experience. The Vault is the durable memory
> and evidence layer underneath.

This direction refines, rather than replaces, the Guided Evaluation priority.
Guided Evaluation becomes the onboarding path into the first complete Vault and
shortcut workflow.

## Product model

| Layer | Responsibility |
|---|---|
| Vault | Preserve approved property, deal, market, model, source, and assumption facts |
| Shortcuts | Complete a bounded real-estate job with defined inputs and outputs |
| Sage | Explain, guide, answer follow-up questions, and propose controlled actions |
| Cactus engine | Extract, calculate, compare, validate, and export |
| MCP and exports | Let approved external AI clients use scoped Vault context |

Users should begin with a desired outcome instead of navigating modules, nodes, or
an open-ended chat surface.

Example outcomes:

- Screen this deal.
- Verify these assumptions.
- Compare this property to my market.
- Explain what changed.
- Update my underwriting.
- Prepare an investment summary.

A shortcut is not a saved prompt. It is a bounded workflow with:

- explicit required inputs;
- deterministic calculations or supported model operations;
- evidence and provenance;
- loading, empty, error, retry, and partial-success states;
- user confirmation for material changes;
- a saved, auditable result;
- a clear next action.

## Evidence

### Cactus 1.0

- Quick Analysis recorded 100,593 pageviews from 215 external identified users over
  the trailing twelve-month evidence window.
- The intensity of 467.9 views per identified user indicates a strong historical
  repeat-screening habit.
- Interpretation: a `Screen This Deal` shortcut should preserve this proven job.

### Cactus 2.0

- Signup to meaningful action within 14 days was 91 of 329 test-filtered users, or
  27.7%.
- Market Analysis recorded 1,415 submitted messages from 85 external users across
  50 organizations.
- Assistant response completion was 90 of 106 test-filtered submitters, with a
  median of 2.1 seconds. Assistant speed alone is therefore unlikely to be the
  primary activation constraint.
- Interpretation: Cactus 2.0 needs a clearer path from entry to a useful, trusted
  result while preserving market-analysis behavior.

### External-call transcript evidence

- Guided Activation matched 509 meetings, including 453 explicit signals.
- Market Intelligence matched 433 meetings, including 266 explicit signals.
- Trust Center matched 353 meetings, including 276 explicit signals.
- These counts show recurring themes in recorded conversations. They are not survey
  percentages and do not prove causal revenue impact.

### Hypotheses to validate

- A persistent Vault will reduce repeated setup and explanation.
- Reusing approved facts will increase the speed and trust of later shortcuts.
- Saved proprietary context will improve retention and create a stronger reason to
  pay than a one-time analysis.
- Outcome-oriented shortcuts will make Cactus easier to evaluate without live
  onboarding.

These hypotheses are not yet supported by measured Vault reuse data.

## Four-week vertical slice

With one AI developer and four weeks, build a narrow **Deal Vault with three
shortcuts** in Cactus 2.0.

### Target user

A multifamily acquisitions professional evaluating a new property or deal package.

### User job

Turn a deal package into a fast, defensible screen while preserving the approved
facts for later comparison and analysis.

### Minimal Vault

- One entity type: `property` or `deal`.
- Approximately 20–30 canonical multifamily fields.
- Reuse existing Cactus extraction and calculation capabilities.
- Store the latest approved value, source/evidence pointer, timestamp, and
  provenance.
- Require confirmation for material assumptions or AI-proposed changes.
- Provide one simple saved-deals view.
- Preserve stable organization, account, user, deal, and evaluation identifiers.

### First shortcuts

#### 1. Screen This Deal

Produce an explainable `pass`, `fail`, or `uncertain` result using the user's saved
criteria. Show the facts and assumptions responsible for the result.

#### 2. Verify Key Facts

Present material unit-mix, income, expense, pricing, and underwriting assumptions
that require review. Link each reviewed item to available evidence and preserve the
approval record.

#### 3. Compare to My Market

Compare the current deal with saved properties, accepted comps, and approved market
assumptions. Clearly distinguish observed facts from inferred or missing values.

### Guided first-use journey

1. Open a preloaded sample deal or supported existing deal package.
2. Review extracted material facts.
3. Approve or correct critical assumptions.
4. Run `Screen This Deal`.
5. Review the evidence-backed result.
6. Save the deal and result to the Vault.
7. Export, share, book a working session, or continue to a paid workflow.

The journey itself is onboarding. Do not require a separate tour of every Cactus
screen or capability.

## Four-week delivery plan

| Week | Scope | Observable completion |
|---|---|---|
| 1 | Lock the sample deal, canonical fields, result definition, identifiers, events, and feature flag | The complete path is queryable and the sample deal loads reliably |
| 2 | Build the Deal Vault view, fact review, provenance, progress guidance, and resilient states | An internal tester reaches approved facts without a founder walkthrough |
| 3 | Build the three shortcuts, contextual Sage help, result review, audit, and handoff | At least four of five testers complete without live rescue or a material output error |
| 4 | Test with 8–10 qualified prospects, fix the three largest blockers, and stage the release | The validation gates below are met or the largest failed step is known |

If the sample deal requires a new extraction or modeling architecture by the end of
Day 3, narrow the test to an existing completed deal. Do not expand scope.

## Success and decision gates

### Four-week validation gate

- At least 8 of 10 testers start without setup assistance.
- At least 7 of 10 complete one shortcut.
- At least 6 of 10 approve and save a defensible result without live help.
- Median time to the first shortcut result is 10 minutes or less.
- No more than 2 of 10 testers require human intervention.
- Zero material silent AI or model changes.
- Every material result is linked to supporting facts or explicitly marked
  assumptions.
- At least 5 of 10 testers return within seven days, add another property, or reuse
  Vault facts in another shortcut.

These are proposed validation thresholds, not historical measurements.

### Production gate

- Improve Cactus 2.0 signup-to-meaningful-action conversion from the 27.7% baseline
  to at least 40% without worsening trust or error guardrails.
- Establish and then reduce onboarding/support time per activated account.
- Measure first shortcut completion, first saved result, seven-day reuse, export,
  handoff, and paid conversion end to end.

### North-star metric

**Evidence-backed decisions completed per active account per week.**

Supporting metrics:

- evaluation started;
- first fact reviewed;
- material fact approved or corrected;
- shortcut started and completed;
- first defensible result saved;
- time to first result;
- human escalation;
- second property added;
- Vault fact reused;
- export or share;
- conversion handoff;
- paid conversion when CRM and billing identity are joined.

## Revenue mechanism

- **Conversion:** a prospect can experience a credible result before requiring
  extensive live onboarding.
- **Retention:** the Vault preserves proprietary approved context that improves
  future work.
- **Expansion:** shared Vaults, portfolios, approvals, automations, and governance
  support multi-user adoption.
- **Higher ACV later:** supported models, enterprise controls, connectors, and
  controlled MCP access can be sold after the core reuse loop is proven.

No feature-level revenue lift should be claimed without joined product, CRM,
billing, account-value, and support-cost data.

## Explicit non-goals for the four-week build

- A general-purpose database platform.
- Multiple entity types.
- Arbitrary user-defined schemas.
- Custom AI columns.
- Folder automation and scheduled research.
- Broad connector coverage.
- Google Sheets synchronization.
- Full historical conflict-resolution rules.
- An unrestricted free trial.
- A new underwriting engine.
- A broad navigation rewrite.
- A production MCP server.
- Fully autonomous Sage changes.

## MCP sequencing

MCP is an optional access layer, not the first product outcome.

Before building MCP, validate external-AI demand with scoped Markdown, CSV, or JSON
exports. Instrument export and repeated external use. Build MCP when customers show
that static exports are a recurring constraint.

When MCP is justified, preserve these principles from the source concept:

- expose typed, controlled tools rather than raw database access;
- scope reads and writes to an organization, folder, deal, or explicit selection;
- require provenance and evidence pointers on material fact writes;
- preserve fact history rather than silently overwrite;
- require user-approval metadata for material writes;
- use idempotency keys;
- log the client, caller, time, operation, and affected facts;
- prohibit ordinary destructive deletes, raw SQL, secret access, and long
  unstructured writes into core fact fields.

Start with read-only tools such as:

- `query_vault`
- `query_folder`
- `get_entity`
- `get_fact_history`
- `compare_entities`
- `find_comps`

Add approval-aware writes only after the read path and schema are stable.

## Longer-term sequence

1. Prove the Deal Vault and first shortcut loop.
2. Add material-fact review, evidence, approval, and lightweight conflict handling.
3. Prove repeated property, comp, and market-fact reuse.
4. Add folders and one validated automation.
5. Add custom columns or connectors only for observed repeat jobs.
6. Add controlled MCP access after export demand and schema stability are proven.

## Decision history from the product conversation

1. The initial four-week recommendation was Guided Evaluation to First Defensible
   Result in Cactus 2.0.
2. The Vault concept introduced persistent, structured, time-aware,
   evidence-backed real-estate memory and optional external-AI access.
3. The product direction was refined: Cactus should not keep building a platform
   that users must understand before receiving value.
4. Shortcuts should expose bounded outcomes, while the Vault remains the underlying
   source of truth and Sage provides contextual guidance.
5. Guided Evaluation remains necessary, but it now teaches the user by completing
   the first Vault and shortcut loop.
6. The current four-week recommendation is therefore a narrow Deal Vault with three
   shortcuts, not the complete Vault and MCP roadmap.

## Unresolved evidence gaps

- Whether users return specifically because approved Vault facts are reusable.
- Which facts are sufficiently common across multifamily customers to standardize.
- Which shortcut creates the strongest paid-conversion signal.
- Whether `Compare to My Market` has enough approved private data to be useful at
  first use.
- The tolerance and review method for a defensible screening result.
- The baseline cost of live onboarding and support per activated account.
- Whether customers repeatedly export context to external AI tools.

Treat these as validation questions, not reasons to broaden the first build.
