# Secured Source Data Access

The public datasets in this repository are sufficient to understand the evidence,
priorities, metric definitions, and delivery plan. They are not a substitute for
secured raw customer and product data when implementing analytics or validating a
specific workflow.

## Raw sources intentionally excluded

- 946 Sybill transcript files and the identifying transcript manifest;
- participant names, meeting titles, timestamps, conversation IDs, and recording URLs;
- verbatim customer statements;
- PostHog event-level rows, person properties, organization properties, and session
  recordings;
- authenticated PostHog project URLs;
- CRM, billing, support, and account-value data.

## How an authorized developer should obtain them

1. Request access from the internal Cactus owner for Sybill and both PostHog projects.
2. Confirm the developer's need-to-know scope, data-retention period, and approved
   storage location.
3. Work in an access-controlled repository, data warehouse, or encrypted workspace.
4. Keep raw exports, access tokens, cookies, customer identifiers, and recording URLs
   out of this public repository and its issue tracker.
5. Publish only reviewed aggregates or redacted derivatives back to this project.

## If raw data must be versioned

Create a separate private repository or restricted object store. Add explicit access
controls, a retention policy, an owner, an audit process, and automated secret and PII
scanning before uploading any source files.

## Reproducibility limitation

The PostHog files here are a fixed validated snapshot through 2026-07-27. The original
query definitions were reviewed during analysis, but a complete runnable query package
was not retained. Reproduction should begin by validating the current event taxonomy
in each PostHog project because instrumentation may have changed.
