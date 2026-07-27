# Vault, Shortcuts, Sage, and MCP Direction

## Decision

Present Cactus as a small set of outcome-oriented real-estate shortcuts powered by
a persistent, evidence-backed Vault.

- Shortcuts are the product surface users experience.
- The Vault is the approved fact, evidence, and memory layer.
- Sage guides, explains, and proposes controlled actions.
- The Cactus engine extracts, calculates, compares, validates, and exports.
- MCP and exports provide scoped access for external AI clients.

This refines Guided Evaluation rather than replacing it. The guided journey should
teach Cactus by completing the first Vault and shortcut loop.

## Evidence

### Cactus 1.0

- Quick Analysis recorded 100,593 pageviews from 215 external identified users over
  the trailing twelve-month evidence window, or 467.9 views per user.
- Use this as evidence for a proven repeat-screening job, not as a current Cactus
  2.0 activation baseline.

### Cactus 2.0

- Signup to meaningful action within 14 days was 91 of 329 test-filtered users, or
  27.7%.
- Market Analysis recorded 1,415 submitted messages from 85 external users across
  50 organizations.
- Assistant completion was 90 of 106 test-filtered submitters with a 2.1-second
  median. Speed alone is unlikely to explain the activation constraint.

### Transcript evidence

- Guided Activation: 509 matching meetings and 453 explicit signals.
- Market Intelligence: 433 matching meetings and 266 explicit signals.
- Trust Center: 353 matching meetings and 276 explicit signals.
- Treat these as recurring recorded-conversation themes, not survey percentages.

### Unmeasured hypotheses

- Persistent approved facts reduce repeated setup.
- Fact reuse improves the speed and trust of later shortcuts.
- Proprietary saved context improves retention and willingness to pay.
- Shortcuts reduce the need for live onboarding.

Do not present these hypotheses as measured outcomes until Vault reuse is
instrumented.

## Four-week vertical slice

With one AI developer and four weeks, build a narrow Cactus 2.0 Deal Vault:

- one `property` or `deal` entity;
- approximately 20–30 canonical multifamily fields;
- existing extraction and calculations where supported;
- latest approved value, provenance, timestamp, and evidence pointer;
- stable organization, account, user, deal, and evaluation identifiers;
- one simple saved-deals view;
- user confirmation for material facts and AI/model changes.

Build three shortcuts:

1. `Screen This Deal`: explainable pass, fail, or uncertain result.
2. `Verify Key Facts`: review material unit-mix, income, expense, pricing, and
   underwriting assumptions.
3. `Compare to My Market`: compare the deal with saved properties, accepted comps,
   and approved market assumptions.

A shortcut must have explicit inputs, bounded operations, resilient UI states,
evidence, confirmation, an auditable saved result, and a clear next action. It is
not merely a saved chat prompt.

## First-use loop

1. Open a preloaded sample or supported existing deal.
2. Review extracted material facts.
3. Approve or correct critical assumptions.
4. Run `Screen This Deal`.
5. Review the evidence-backed result.
6. Save the deal and result.
7. Export, share, continue to a paid workflow, or request human help.

## Decision gates

Treat these as proposed thresholds:

- 8 of 10 testers start without setup help.
- 7 of 10 complete one shortcut.
- 6 of 10 approve and save a defensible result without live help.
- Median time to the first shortcut result is no more than 10 minutes.
- No more than 2 of 10 require human intervention.
- Zero material silent AI/model changes.
- Every material result is linked to supporting facts or marked assumptions.
- 5 of 10 return within seven days, add a second property, or reuse a Vault fact.
- Cactus 2.0 production signup-to-meaningful-action improves from 27.7% to at least
  40% without worsening trust or error guardrails.

Use **evidence-backed decisions completed per active account per week** as the
longer-term north-star metric.

## Four-week non-goals

- A general database platform.
- Multiple entity types or arbitrary schemas.
- Custom AI columns.
- Folder automations.
- Broad connectors or Google Sheets sync.
- A new underwriting engine.
- An unrestricted free trial.
- A broad navigation rewrite.
- A production MCP server.
- Fully autonomous Sage changes.

## MCP sequencing and guardrails

Validate external-AI demand first with scoped Markdown, CSV, or JSON exports.
Instrument export and repeated use. Build MCP when static exports become a measured
recurring constraint and the Vault schema is stable.

For MCP:

- expose typed tools, never raw SQL;
- scope access by organization, folder, deal, or explicit selection;
- require provenance and evidence pointers on material writes;
- preserve fact history instead of silently overwriting;
- require approval metadata for material writes;
- require idempotency keys;
- log client, caller, timestamp, operation, and affected facts;
- prohibit normal destructive deletes, secret access, and long unstructured writes
  into core fact fields.

Start read-only with `query_vault`, `query_folder`, `get_entity`,
`get_fact_history`, `compare_entities`, and `find_comps`. Add approval-aware writes
only after the read path and schema are stable.

## Revenue mechanism

- Conversion through credible value before extensive live onboarding.
- Retention through reusable proprietary approved context.
- Expansion through shared Vaults, portfolios, approvals, and automations.
- Higher ACV later through supported models, governance, connectors, and controlled
  MCP access.

Do not claim feature ROI without joined product, CRM, billing, account-value, and
support-cost data.

## Evidence gaps

- Measured seven-day and thirty-day Vault reuse.
- The canonical fields common across target multifamily customers.
- The shortcut most associated with paid conversion.
- Minimum private-data density needed for useful market comparisons.
- Screening-result accuracy tolerance and review procedure.
- Live onboarding/support cost per activated account.
- Repeated external-AI export behavior.
