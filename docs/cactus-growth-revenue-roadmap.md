# Cactus Growth and Revenue Roadmap

**Planning date:** 2026-07-27 
**Evidence:** Cactus 1.0 legacy behavior, Cactus 2.0 current-product behavior, aggregate Sybill research, and business-growth prioritization.

This is an outcome-based roadmap. Scores and horizons are decision inputs, not delivery promises or financial forecasts.

## Execution sequence

### 0. Growth and Revenue Telemetry

- **Business-impact rank:** Enabler
- **Program:** Shared platform
- **Growth score:** Enabler
- **Estimated effort:** M
- **Investment posture:** Build immediately
- **Horizon:** Horizon 0
- **Revenue mechanism:** Revenue attribution; lower decision risk
- **Primary metric:** Evaluation-to-paid funnel coverage
- **PostHog evidence scope:** Cross-version: create a stable bridge from Cactus 1.0 legacy behavior through Cactus 2.0 usage to CRM and billing outcomes
- **Decision gate:** Stable account, organization, deal, approval, export, paid-conversion, CRM, billing, and environment fields are queryable end to end
- **Dependencies:** Identity; CRM and billing joins; PostHog taxonomy; data ownership

### 1. Guided Evaluation and Sage Activation

- **Business-impact rank:** 5
- **Program:** Self-serve growth engine
- **Growth score:** 85
- **Estimated effort:** M
- **Investment posture:** Build now
- **Horizon:** Horizons 0-1
- **Revenue mechanism:** Evaluation-to-paid conversion; lower onboarding cost
- **Primary metric:** Percentage of evaluations reaching an approved or exported first result
- **PostHog evidence scope:** Cactus 2.0 current-product baseline: 91 of 329 test-filtered signups reached a meaningful action within 14 days (27.7%)
- **Decision gate:** Cactus 2.0 meaningful-action conversion improves from 27.7% to at least 40%; support hours decline; quality guardrails do not worsen
- **Dependencies:** Growth telemetry; sample data; Sage context and action contract; job status; payment handoff

### 2. Trust Center 2.0 - Exception-First Document Review

- **Business-impact rank:** 1
- **Program:** Defensible underwriting core
- **Growth score:** 95
- **Estimated effort:** L
- **Investment posture:** Build now
- **Horizon:** Horizons 0-1
- **Revenue mechanism:** Conversion; retention; enterprise win rate
- **Primary metric:** Median minutes from extraction complete to approved model inputs
- **PostHog evidence scope:** Cactus 2.0 current-product extraction and confidence-verification evidence
- **Decision gate:** Material review time declines at least 30%; escaped material errors do not increase; 10 beta accounts complete review to approved inputs
- **Dependencies:** Source metadata; confidence; model impact graph; reviewer state; audit

### 3. Instant Deal Screen - Intake-to-Go/No-Go

- **Business-impact rank:** 3
- **Program:** Self-serve growth engine
- **Growth score:** 88
- **Estimated effort:** M
- **Investment posture:** Build now
- **Horizon:** Horizons 0-1
- **Revenue mechanism:** New-logo conversion; repeat usage; deal throughput
- **Primary metric:** Median time from package receipt to recorded go or no-go decision
- **PostHog evidence scope:** Cross-version: strong Cactus 1.0 Quick Analysis habit with a directional Cactus 2.0 migration gap
- **Decision gate:** Package-to-decision time improves against concierge baseline; multiple screens per active account; false-negative review is operational
- **Dependencies:** Document intake; buy-box criteria; deduplication; job state; promotion to underwriting

### 4. Market Intelligence - Evidence-Backed Comps and Memory

- **Business-impact rank:** 4
- **Program:** Compounding data and habit
- **Growth score:** 87
- **Estimated effort:** XL
- **Investment posture:** Validate now; build next
- **Horizon:** Horizons 0 and 2
- **Revenue mechanism:** Retention; expansion; differentiated paid value
- **Primary metric:** Percentage of material market assumptions with approved supporting evidence
- **PostHog evidence scope:** Cactus 2.0 current-product Market Analysis adoption
- **Decision gate:** Design partners select approved comps faster and reuse private comps before source or asset-class expansion
- **Dependencies:** Data licenses; entity resolution; freshness; source metadata; firm-memory schema

### 5. Model Studio - Formula-Aware Excel Roundtrip

- **Business-impact rank:** 2
- **Program:** Defensible underwriting core
- **Growth score:** 89
- **Estimated effort:** XL
- **Investment posture:** Technical spike now; supported subset next
- **Horizon:** Horizons 0 and 2
- **Revenue mechanism:** Enterprise ACV; pilot conversion; expansion
- **Primary metric:** Percentage of pilot models tying out within agreed tolerance
- **PostHog evidence scope:** Cactus 2.0 current-product Excel extraction usage and reliability
- **Decision gate:** At least 80% of selected pilot workbooks tie out; zero silent unsupported failures
- **Dependencies:** Workbook parser; model schema; formula boundaries; template registry; security

### 6. Enterprise Workflow - Integrations Roles and Governance

- **Business-impact rank:** 6
- **Program:** Enterprise and segment expansion
- **Growth score:** 83
- **Estimated effort:** L
- **Investment posture:** Design council now; build next
- **Horizon:** Horizon 2
- **Revenue mechanism:** Higher ACV; multi-user deployment; expansion
- **Primary metric:** Enterprise pilots reaching multi-user production deployment
- **PostHog evidence scope:** Cactus 2.0 current-product invitation and collaboration evidence
- **Decision gate:** Qualified enterprise design partners progress from champion-only use to measurable multi-user production
- **Dependencies:** Tenant identity; roles; audit; SSO; connector framework; API jobs

### 7. Scenario Lab - Conversational Sensitivity With Controls

- **Business-impact rank:** 7
- **Program:** Defensible underwriting core
- **Growth score:** 80
- **Estimated effort:** L
- **Investment posture:** Instrument now; build next
- **Horizon:** Horizon 2
- **Revenue mechanism:** Engagement; retention; seat expansion
- **Primary metric:** Scenario completion without analyst support
- **PostHog evidence scope:** Cactus 2.0 current-product chat behavior; dedicated scenario events are missing
- **Decision gate:** At least 70% of validated common scenario requests complete without analyst help and within agreed quality limits
- **Dependencies:** Model parameter schema; calculation engine; validation; versioning; Sage action contract

### 8. Decision Packages - Source-Linked IC Lender and Client Outputs

- **Business-impact rank:** 10
- **Program:** Defensible underwriting core
- **Growth score:** 71
- **Estimated effort:** M
- **Investment posture:** Concierge validation; productize later
- **Horizon:** Horizon 3
- **Revenue mechanism:** Workflow completion; collaboration; expansion
- **Primary metric:** Median time from approved underwriting to shared decision package
- **PostHog evidence scope:** Cactus 2.0 current-product share evidence; package workflow is under-instrumented
- **Decision gate:** Twenty concierge packages establish the common 80%; product slice cuts creation time at least 50% with zero unsupported claims
- **Dependencies:** Approved deal state; risk flags; scenario data; source links; permissions; document generation

### 9. Development Underwriter - Cost Draw and Stabilization

- **Business-impact rank:** 8
- **Program:** Enterprise and segment expansion
- **Growth score:** 77
- **Estimated effort:** XL
- **Investment posture:** Paid beta later
- **Horizon:** Horizon 3
- **Revenue mechanism:** New segment ARR
- **Primary metric:** Development models completed and approved without offline rebuild
- **PostHog evidence scope:** Cactus 2.0 current-product technical-failure evidence; active cohort remains unproven
- **Decision gate:** Five to eight paid or committed design partners complete and approve the narrow archetype without offline rebuild
- **Dependencies:** Schedule engine; model relationships; permissions; debt model; Excel export

### 10. Commercial Lease Intelligence - Multi-Tenant Underwriting

- **Business-impact rank:** 9
- **Program:** Enterprise and segment expansion
- **Growth score:** 72
- **Estimated effort:** XL
- **Investment posture:** Narrow paid beta after validation
- **Horizon:** Horizon 4
- **Revenue mechanism:** New asset-class ARR
- **Primary metric:** Analyst hours to produce an approved tenant rollover schedule
- **PostHog evidence scope:** Cactus 2.0 current-product rent-roll evidence; sample is very small
- **Decision gate:** Segment selected from qualified pipeline; at least 500 leases benchmarked; accuracy threshold and paid commitments established before build
- **Dependencies:** Document hierarchy; tenant resolution; recovery rules; schedule engine; export integration

---

**Public redacted edition.** This roadmap contains aggregate product evidence and excludes direct customer identities, private recordings, account-level data, and authenticated analytics links.
