# Cactus Product & Design Opportunity Portfolio

**Research date:** 2026-07-27

## Executive recommendation

Cactus should concentrate the product strategy on one promise: **turn a messy deal package into a defensible decision while preserving the customer's model, evidence, and judgment.** The transcript corpus does not support a generic "more AI" roadmap. It supports a connected workflow with four layers:

1. **Trust the inputs:** prioritize and resolve material exceptions.
2. **Reach a decision faster:** screen, model, and test scenarios without re-entry.
3. **Fit the firm:** preserve Excel, templates, roles, and integrations.
4. **Compound the work:** reuse approved evidence, assumptions, and outputs on the next deal.

The integrated ranking places Trust Center 2.0 first, elevates Market Intelligence from seventh to second because it is already the broadest verified Cactus 2.0 workflow, and keeps Instant Deal Screen third because Quick Analysis was the strongest legacy usage habit. For delivery, start Trust Center, Instant Deal Screen, and Guided Activation now; begin Market Intelligence evidence-card validation and the Model Studio technical spike in parallel.

## Research basis

- 946 unique Sybill transcripts from externally labeled meetings.
- 113,688 normalized speaker turns and 5.72 million total words.
- 56,829 non-Cactus speaker turns and 2.21 million external-speaker words after excluding known Cactus team names.
- 25 meetings classified as likely internal/advisor conversations were excluded from weighted recommendation evidence.
- Evidence was mined at meeting level so a talkative call did not count as dozens of independent votes.
- Thematic counts are directional qualitative evidence, not survey percentages; one meeting can support several opportunities.
- PostHog Cactus 1.0 and Cactus 2.0 projects were analyzed for verified events, external identified usage, activation, workflow adoption, funnels, retention, reliability, and instrumentation gaps.
- Cactus 1.0 external identified monthly activity declined from 118 users in July 2025 to 24 in partial July 2026; Cactus 2.0 grew from 33 in December 2025 to 64 in June 2026, with 52 in partial July.

The analysis followed the linked Product Manager Skills methods: voice-of-customer themes were framed as needs rather than feature requests; an opportunity-solution structure was used before selecting solutions; a weighted scoring model combined customer voice with verified behavior; delivery was split into vertical, testable slices.

## Important temporal limitation

The manifest does not contain meeting dates. Some calls clearly describe earlier product states, while Cactus's current public pages already describe source trails, document reconciliation, custom templates, screening, scenario analysis, Market Intelligence, Proprietary Memory, Excel export, API access, SSO/SAML, and new-development support. PostHog reduces this uncertainty by showing which workflows are currently used, but incomplete or inconsistent instrumentation still prevents precise revenue attribution and end-to-end deal completion measurement.

## Prioritization method

Integrated impact score uses 20% user experience + 20% adoption + 20% revenue + 10% strategic leverage + 15% transcript evidence + 15% PostHog behavioral evidence. Each dimension is scored 1-5, with small or missing cohorts explicitly penalized. Effort remains separate because the purpose is to identify impact before engineering sizing.

| Rank | Project | Impact | Effort | Roadmap | Explicit-signal meetings | PostHog evidence |
|---:|---|---:|:---:|:---:|---:|---|
| 1 | Trust Center 2.0 - Exception-First Document Review | 97 | L | Now | 276 | Strong, narrow cohort |
| 2 | Market Intelligence - Evidence-Backed Comps and Memory | 96 | XL | Next | 266 | Strong and broad |
| 3 | Instant Deal Screen - Intake-to-Go/No-Go | 94 | M | Now | 99 | Strong legacy habit; migration gap |
| 4 | Model Studio - Formula-Aware Excel Roundtrip | 93 | XL | Next | 184 | Strong technical signal; moderate reach |
| 5 | Guided Activation - First Defensible Deal | 92 | M | Now | 453 | Strong growth constraint |
| 6 | Scenario Lab - Conversational Sensitivity With Controls | 84 | L | Next | 216 | Strong adjacent behavior; missing scenario event |
| 7 | Enterprise Workflow - Integrations, Roles, and Governance | 79 | L | Next | 213 | Early but measurable |
| 8 | Development Underwriter - Cost, Draw, and Stabilization | 74 | XL | Later | 149 | Technical pain; limited adoption evidence |
| 9 | Decision Packages - Source-Linked IC, Lender, and Client Outputs | 68 | M | Later | 79 | Weak or under-instrumented |
| 10 | Commercial Lease Intelligence - Multi-Tenant Underwriting | 67 | XL | Later | 31 | Very early sample |

**Reading the evidence:** "Explicit-signal meetings" contain a rule-based opportunity match plus request, pain, adoption, revenue, or trust language. Counts are not additive. PostHog strength reflects current behavioral breadth, funnel quality, and instrumentation confidence - not just raw event volume.

## What PostHog changed

- **Market Intelligence moved from #7 to #2:** **Cactus 2.0** market-analysis chat recorded 1,415 messages from 85 external users across 50 organizations.
- **Instant Deal Screen stayed in the top three:** Cactus 1.0 Quick Analysis logged 100,593 pageviews from 215 external identified users, but the named Cactus 2.0 route reached only 3 users - an urgent migration gap.
- **Guided Activation remains Now:** only 91 of 329 test-filtered **Cactus 2.0** signups reached a meaningful underwriting action within 14 days (27.7%).
- **Model Studio remains a major bet but requires a reliability gate:** 327 of 342 Excel extraction completion events succeeded, with 147.6-second average latency and concentrated workbook-step failures.
- **Commercial Lease Intelligence moved to #10:** the test-filtered rent-roll funnel contained only 4 triggering users and 2 completions.

Full behavioral evidence and caveats: `cactus_posthog_product_evidence_2026-07-27.md` and `cactus_posthog_metrics_2026-07-27.csv`.

## Strategic problem framing

**Look inward:** Cactus's risk is defining success as feature coverage - more asset classes, models, data, and AI behaviors - while users evaluate whether they can reach and defend a decision in their own workflow.

**Look outward:** The problem is most acute for small teams processing high deal volume, analysts inheriting complex models, principals who need quick what-if answers, and enterprise teams that cannot move data outside controlled systems. The status quo benefits manual services and spreadsheet expertise, but it limits product adoption and organizational scale.

**Reframed problem:** CRE teams struggle to delegate underwriting because messy inputs, model variation, evidence review, and stakeholder handoff remain disconnected. Even a fast AI result creates rework when the team cannot verify it, fit it into its model, or reuse the approved decision.

**How might we** help a CRE team move from package receipt to a defensible, reusable decision with minimal re-entry while keeping professionals in control?

## Opportunity-solution tree

```text
Outcome A: Reduce package-to-defensible-decision time
├─ Trust material inputs
│ └─ Trust Center 2.0
├─ Reject low-fit deals earlier
│ └─ Instant Deal Screen
└─ Answer what-if questions safely
 └─ Scenario Lab

Outcome B: Increase activation and repeat usage
├─ Reach first value without a live call
│ └─ Guided Activation
├─ Preserve the firm's model
│ └─ Model Studio
└─ Complete the decision workflow
 └─ Decision Packages

Outcome C: Win larger accounts and expand ARPA
├─ Fit enterprise systems and controls
│ └─ Enterprise Workflow
└─ Compound proprietary market knowledge
 └─ Market Intelligence & Memory

Outcome D: Expand the addressable workflow
├─ Ground-up development
│ └─ Development Underwriter
└─ Multi-tenant office/retail/industrial
 └─ Commercial Lease Intelligence
```

## Project briefs

### 1. Trust Center 2.0 - Exception-First Document Review

**Posture:** Deepen an existing core capability 
**Target user:** Acquisitions analyst, principal reviewer, lender/credit reviewer 
**Impact / effort / roadmap:** 97/100 · L · Now 
**Directional evidence:** 353 matching meetings; 276 with explicit signals; 59 post-sale or working-session meetings.

**PostHog baseline (Strong, narrow cohort):** Cactus 2.0: 29 of 34 test-filtered users completed extraction within one day (85.3%); median conversion was 40.8 seconds and average was 105.5 seconds. Across raw pipeline events, 514 extraction completions covered 41 users. Confidence verification averaged 0.766 confidence and 948.8 source matches across 1,362.1 verified facts per run. Workflow routes logged 1,422 exceptions affecting 35 external users, although a benign ResizeObserver issue dominates the grouped error list.

**Problem:** Analysts will not delegate consequential underwriting work to AI when the remaining errors are difficult to find, conflicts are not prioritized, or review decisions disappear after export.

**How might we:** How might we surface and resolve the few facts that can materially change the deal before those facts flow into the model?

**Proposed experience:** Add an exception-first Review Queue to the existing source-linked extraction flow. Rank facts by financial materiality and confidence; show the source snippet, competing values, model impact, and reviewer state in one fact card. Let analysts approve, replace, defer, or escalate a fact, then preserve that decision in an audit log and tie-out report.

**Design direction:** Primary flow: deal intake summary -> material exceptions -> fact drawer -> resolve -> publish approved inputs. Design for calm review: risk hierarchy, side-by-side sources, keyboard navigation, persistent filters, empty/loading/failed states, and a visible distinction between extracted facts, assumptions, and human approvals.

**MVP slice:** T-12 + rent-roll conflicts for multifamily; materiality rules; source drawer; approve/replace action; reviewer audit trail; tie-out summary.

**Out of scope:** Autonomous approval, a universal diligence checklist, and every document type in the first release.

**Primary metric:** Median minutes from extraction complete to approved model inputs.

**Secondary and guardrail metrics:** High-risk exceptions resolved; correction rate; reviewer agreement; support tickets about wrong values; percentage of deals exported without rework.

**Validation:** Prototype with 8-10 analysts using real conflicted packages; beta with 10 accounts and compare review time/error escape rate with the current workflow.

**Dependencies:** Extraction confidence metadata, source storage, model impact graph, reviewer identity, event analytics.

**Key risk:** A noisy queue will reduce trust. Start with a narrow, calibrated definition of material exceptions and expose why each item was prioritized.

**Public-edition evidence basis:** Aggregate transcript counts are reported above. Direct customer quotes, participant names, timestamps, and private Sybill recording links are omitted.


### 2. Market Intelligence - Evidence-Backed Comps and Memory

**Posture:** Deepen current Market Intelligence and Proprietary Memory 
**Target user:** Market analyst, acquisitions professional, principal 
**Impact / effort / roadmap:** 96/100 · XL · Next 
**Directional evidence:** 433 matching meetings; 266 with explicit signals; 69 post-sale or working-session meetings.

**PostHog baseline (Strong and broad):** Cactus 2.0 external usage: market-analysis generated 1,415 submitted messages from 85 users across 50 organizations (16.6 messages per user), making it the broadest verified custom workflow in the current product.

**Problem:** Finding comps is time-consuming, but unverified or stale comps are worse. Teams need to understand why a comp supports an assumption and preserve trusted private knowledge for the next deal.

**How might we:** How might we turn market data into reviewable evidence that improves every future underwriting rather than another data feed?

**Proposed experience:** Create comp evidence cards with source, freshness, relevance, and confidence. Let users accept/reject a comp, attach it to an assumption, add a private comp, and save the decision into firm memory. Generate a short source-backed market memo.

**Design direction:** Primary flow: suggested comps/map -> inspect evidence -> accept/reject -> attach to assumption -> save to memory. Separate vendor data, public records, customer-owned data, and inference visually. Support map and table workflows equally.

**MVP slice:** Rent-comp evidence cards for one asset class; freshness/relevance indicators; accept/reject; attach to market rent; save customer-owned comps.

**Out of scope:** Owning every market-data source or replacing specialist GIS/data products.

**Primary metric:** Percentage of material market assumptions with approved supporting evidence.

**Secondary and guardrail metrics:** Time to comp set; comp acceptance rate; private comps saved/reused; repeat-deal time savings; Market Intelligence weekly actives.

**Validation:** Compare current comp selection with evidence cards on 30 deals; measure agreement, time, and the reasons users reject recommendations.

**Dependencies:** Data licenses, entity resolution, freshness metadata, map performance, firm memory schema.

**Key risk:** More data can create false confidence. Make source limitations explicit and optimize for defensibility, not volume of data points.

**Public-edition evidence basis:** Aggregate transcript counts are reported above. Direct customer quotes, participant names, timestamps, and private Sybill recording links are omitted.


### 3. Instant Deal Screen - Intake-to-Go/No-Go

**Posture:** Complete and simplify an existing screening capability 
**Target user:** Acquisitions lead, solo sponsor, broker, mortgage originator 
**Impact / effort / roadmap:** 94/100 · M · Now 
**Directional evidence:** 182 matching meetings; 99 with explicit signals; 44 post-sale or working-session meetings.

**PostHog baseline (Strong legacy habit; migration gap):** Cactus 1.0 external identified usage: Quick Analysis generated 100,593 pageviews from 215 users over the last twelve months (467.9 views per user). The comparable Cactus 2.0 quick-analysis route recorded only 18 pageviews from 3 users, indicating a valuable legacy job that has not visibly migrated.

**Problem:** Teams spend too long deciding whether a deal deserves full underwriting and cannot process the volume required to find the few opportunities worth pursuing.

**How might we:** How might we turn an incoming package into an explainable go/no-go decision with almost no setup?

**Proposed experience:** Create a zero-touch intake queue fed by upload, forwarded email, and API. Apply saved buy-box criteria, show pass/fail reasons with source evidence, and let the user promote a promising screen into a full underwriting without re-entry.

**Design direction:** Primary flow: receive deal -> processing queue -> screen card -> inspect reasons -> reject/archive or promote. Optimize for scanning many deals: table/card density, batch actions, processing status, explicit missing-data states, and saved filters.

**MVP slice:** Forwarded email or upload intake; saved criteria; one multifamily screening template; explainable pass/fail; promote to full underwriting.

**Out of scope:** A full CRM, broker relationship management, and transaction execution.

**Primary metric:** Median time from package receipt to recorded go/no-go decision.

**Secondary and guardrail metrics:** Deals screened per active account; screens promoted; offers submitted; return frequency; processing completion rate.

**Validation:** Concierge-screen 100 real packages for 8-12 design partners, compare decision time and agreement with their current process, then release a narrow queue MVP.

**Dependencies:** Document intake, criteria schema, Quick Analysis, job status, deduplication, email security.

**Key risk:** A false negative can hide a good deal. Show uncertainty and missing data; avoid binary automation when the evidence is incomplete.

**Public-edition evidence basis:** Aggregate transcript counts are reported above. Direct customer quotes, participant names, timestamps, and private Sybill recording links are omitted.


### 4. Model Studio - Formula-Aware Excel Roundtrip

**Posture:** Turn current custom-model support into a productized moat 
**Target user:** Senior underwriter, acquisitions team lead, enterprise model owner 
**Impact / effort / roadmap:** 93/100 · XL · Next 
**Directional evidence:** 289 matching meetings; 184 with explicit signals; 40 post-sale or working-session meetings.

**PostHog baseline (Strong technical signal; moderate reach):** Cactus 2.0 recorded 342 Excel extraction completions across 31 users: 327 successes and 15 failures (95.6% event-level success), with successful runs averaging 147.6 seconds. Several workbook-related LLM steps show 18-40% failure rates, and active error tracking includes worksheet-name collisions.

**Problem:** Firms have proprietary Excel models, formulas, and review conventions. A static export or one-off services mapping creates adoption friction and makes teams re-enter or re-check work.

**How might we:** How might we let a firm keep its trusted model while Cactus supplies mapped, source-backed inputs and a reliable roundtrip?

**Proposed experience:** Productize model onboarding with a mapping wizard, supported-formula report, template registry, version history, and formula-aware Excel export. Generate a tie-out report showing what mapped, what did not, and which values changed.

**Design direction:** Primary flow: upload model -> inspect workbook -> map input/output cells -> test with one deal -> resolve unmapped items -> publish template. Use a two-pane mapping interface, confidence/status chips, preview values, and reversible mapping edits. Make unsupported formulas/macros explicit before launch.

**MVP slice:** One workbook, one asset-class template, named-range/cell mapping, supported formula preservation, formula-aware export, and tie-out report.

**Out of scope:** Arbitrary VBA/macro execution, every Excel feature, and replacing Excel as a general-purpose modeling environment.

**Primary metric:** Percentage of pilot models that tie out within agreed tolerance.

**Secondary and guardrail metrics:** Time to onboard a model; repeat use of mapped templates; export rework rate; enterprise pilot-to-paid conversion.

**Validation:** Run a technical spike on 20 anonymized customer workbooks, then a concierge pilot with five firms before committing to self-serve mapping.

**Dependencies:** Workbook parser, calculation engine boundaries, template schema, versioning, security review.

**Key risk:** The long tail of Excel behavior can consume the roadmap. Publish a supported subset, detect unsupported constructs early, and preserve a service-assisted path.

**Public-edition evidence basis:** Aggregate transcript counts are reported above. Direct customer quotes, participant names, timestamps, and private Sybill recording links are omitted.


### 5. Guided Activation - First Defensible Deal

**Posture:** Redesign the first-run experience around time-to-value 
**Target user:** Trial user, new analyst, account champion onboarding teammates 
**Impact / effort / roadmap:** 92/100 · M · Now 
**Directional evidence:** 509 matching meetings; 453 with explicit signals; 115 post-sale or working-session meetings.

**PostHog baseline (Strong growth constraint):** Only 91 of 329 test-filtered Cactus 2.0 signups reached a meaningful action (chat submission, extraction start, or template creation) within 14 days: 27.7% conversion. Converters reached value quickly (median 8.0 minutes), so the primary problem is getting more new users onto the successful path. Mature identified-user cohorts retained at 43.3% in week 1 and 18.6% in week 4, with small denominators.

**Problem:** New users encounter unfamiliar underwriting concepts, required inputs, and processing states before they experience a trustworthy result. Dedicated training helps, but it does not scale or rescue self-serve trial drop-off.

**How might we:** How might we help a new user complete one defensible deal without needing a live walkthrough?

**Proposed experience:** Ask for role and goal, then offer a guided sample deal or a real-deal path. Use a short contextual checklist, progressive disclosure, clear processing status, recoverable errors, and a first-value summary that explains what Cactus did.

**Design direction:** Primary flow: choose goal -> sample or real package -> guided review -> adjust one assumption -> export/share. Avoid tours detached from work. Guidance should be dismissible, resume across sessions, and adapt to analyst versus principal roles.

**MVP slice:** Role/goal selection; one guided multifamily sample; four-step checklist; upload progress and recovery; first-deal completion event.

**Out of scope:** Gamification, a large academy rebuild, and deep persona personalization.

**Primary metric:** Percentage of trials reaching an approved/exported first deal.

**Secondary and guardrail metrics:** Time to first value; checklist completion; trial-to-paid conversion; onboarding support hours; day-7 return rate.

**Validation:** Instrument the current funnel, usability-test two first-run prototypes, then A/B test guided sample versus the current start state.

**Dependencies:** Identity/role model, sample data, job status, event analytics, help content.

**Key risk:** Guidance can feel like extra work to experts. Provide a direct expert path and let users switch paths without losing progress.

**Public-edition evidence basis:** Aggregate transcript counts are reported above. Direct customer quotes, participant names, timestamps, and private Sybill recording links are omitted.


### 6. Scenario Lab - Conversational Sensitivity With Controls

**Posture:** Unify current sensitivity and AI capabilities 
**Target user:** Principal, analyst, broker, lender reviewing an underwriting 
**Impact / effort / roadmap:** 84/100 · L · Next 
**Directional evidence:** 344 matching meetings; 216 with explicit signals; 72 post-sale or working-session meetings.

**PostHog baseline (Strong adjacent behavior; missing scenario event):** Cactus 2.0 chat is established: 90 of 106 test-filtered submitters received an assistant completion within ten minutes (84.9%), with a 2.1-second median and 16.2-second average. No dedicated scenario-created, confirmed-change, or scenario-compared event exists, so scenario demand is inferred from chat and transcripts rather than directly measured.

**Problem:** Decision-makers want to ask natural what-if questions, but unconstrained chat can silently change the wrong input, violate model rules, or lose the path back to the approved base case.

**How might we:** How might we make scenario creation as easy as asking a question while keeping every change explicit, reversible, and model-valid?

**Proposed experience:** Combine structured sensitivity controls with a conversational command bar. Parse the requested change, preview affected assumptions and outputs, require confirmation for material changes, and save a versioned scenario with a side-by-side diff.

**Design direction:** Primary flow: ask/change -> preview diff -> confirm -> compare -> save/share. Pair chat with visible controls and constraint feedback. The base case is immutable; scenario lineage and changed inputs remain visible throughout review.

**MVP slice:** Natural-language changes for five common assumptions; validation preview; two-scenario comparison; save/restore; audit entry.

**Out of scope:** A general-purpose chatbot and autonomous investment recommendations.

**Primary metric:** Scenario creation completion rate without analyst support.

**Secondary and guardrail metrics:** Scenarios per active deal; invalid-change rate; time to answer what-if questions; shared scenario views; weekly active principals.

**Validation:** Wizard-of-Oz 30 common what-if requests, establish a safe command grammar, then prototype with principals before enabling free-form commands.

**Dependencies:** Model parameter schema, calculation engine, validation rules, scenario versioning.

**Key risk:** Chat implies more freedom than the model safely supports. Preview every change and prefer bounded commands until accuracy is demonstrated.

**Public-edition evidence basis:** Aggregate transcript counts are reported above. Direct customer quotes, participant names, timestamps, and private Sybill recording links are omitted.


### 7. Enterprise Workflow - Integrations, Roles, and Governance

**Posture:** Productize the Max-plan platform layer 
**Target user:** Enterprise admin, underwriting manager, IT/security buyer, external reviewer 
**Impact / effort / roadmap:** 79/100 · L · Next 
**Directional evidence:** 329 matching meetings; 213 with explicit signals; 53 post-sale or working-session meetings.

**PostHog baseline (Early but measurable):** Cactus 2.0 logged 36 organization invitations from 18 organizations and 23 acceptances across 15 organizations. The roughly 64% event-level acceptance ratio is directional because sent and accepted events are not joined by invite.

**Problem:** Larger teams need Cactus inside their existing data and approval environment. One-off integrations, coarse permissions, or unclear audit/security controls slow procurement and limit deployment beyond a champion.

**How might we:** How might we let enterprise teams connect, govern, and observe Cactus without turning Cactus into another system of record?

**Proposed experience:** Deliver project-level RBAC, admin-visible audit logs, self-service SSO configuration, API jobs/webhooks, and prioritized external storage connectors beginning with SharePoint or Google Drive. Keep external systems authoritative.

**Design direction:** Primary surfaces: admin security center, role matrix, integration setup, sync/job monitor, audit explorer. Use explicit permission previews, least-privilege defaults, test connection states, and actionable failure messages.

**MVP slice:** Project roles; audit log; one external storage connector; asynchronous API job status and webhook; SSO configuration diagnostics.

**Out of scope:** Rebuilding CRM, document management, or full transaction management.

**Primary metric:** Enterprise pilots reaching multi-user production deployment.

**Secondary and guardrail metrics:** Time through security/onboarding; connected workspaces; API jobs; active users per account; enterprise win rate and expansion.

**Validation:** Run a design council with five enterprise prospects/customers; identify the connector and permission set that blocks the largest qualified pipeline.

**Dependencies:** Identity/tenant model, audit events, API platform, connector framework, security review.

**Key risk:** Integrations can become bespoke services. Select connectors by pipeline and reusable architecture; publish support levels and ownership boundaries.

**Public-edition evidence basis:** Aggregate transcript counts are reported above. Direct customer quotes, participant names, timestamps, and private Sybill recording links are omitted.


### 8. Development Underwriter - Cost, Draw, and Stabilization

**Posture:** Deepen a current launch workflow without becoming project management 
**Target user:** Developer, development analyst, construction lead, capital partner 
**Impact / effort / roadmap:** 74/100 · XL · Later 
**Directional evidence:** 242 matching meetings; 149 with explicit signals; 55 post-sale or working-session meetings.

**PostHog baseline (Technical pain; limited adoption evidence):** Cactus 2.0 LLM steps tied to development-style tables show elevated failure: Unit Mix Table 40.9%, Project Stages Table 26.3%, and several cost-table steps 22-26%. Samples are small and do not establish a large active development cohort.

**Problem:** Ground-up underwriting requires percentage-based fees, cost timing, draw schedules, lease-up/stabilization, and role-specific inputs that acquisition models do not handle.

**How might we:** How might we let a mixed finance/construction team build and defend a development underwriting without exposing every input or recreating execution software?

**Proposed experience:** Create configurable development archetypes with a cost stack, percentage formulas, schedule/curve builder, debt draw logic, and role-scoped input views. Export a source-backed model and variance/tie-out report.

**Design direction:** Primary flow: choose archetype -> build cost stack -> set schedule -> define financing -> model lease-up -> review returns. Use linked visual timelines, formula chips, dependency warnings, and separate construction-input from returns-review views.

**MVP slice:** One multifamily ground-up archetype; hard/soft cost stack; percentage fees; straight-line draw; simple lease-up curve; role-scoped cost entry.

**Out of scope:** Invoice approvals, vendor management, change orders, and full construction execution.

**Primary metric:** Development models completed and approved without offline rebuild.

**Secondary and guardrail metrics:** Time to model; template reuse; cost-entry participation; export tie-out; development pilot conversion and expansion ARR.

**Validation:** Run a paid/design-partner beta with 5-8 developers and validate one archetype before adding curves, debt structures, and asset classes.

**Dependencies:** Schedule engine, formula relationships, permissions, debt model, Excel export.

**Key risk:** Scope can drift into Northspyre-style development management. Keep the boundary at underwriting, decision, and handoff.

**Public-edition evidence basis:** Aggregate transcript counts are reported above. Direct customer quotes, participant names, timestamps, and private Sybill recording links are omitted.


### 9. Decision Packages - Source-Linked IC, Lender, and Client Outputs

**Posture:** A fast-follow workflow-completion win 
**Target user:** Analyst preparing a decision, principal, broker, lender, client 
**Impact / effort / roadmap:** 68/100 · M · Later 
**Directional evidence:** 136 matching meetings; 79 with explicit signals; 28 post-sale or working-session meetings.

**PostHog baseline (Weak or under-instrumented):** Cactus 2.0 recorded 39 chat-share events across 13 users, while external report routes reached only 2 users. Package generation, approval, live views, export, and downstream decision events are not instrumented.

**Problem:** After underwriting, teams still re-read the model, identify red flags, and manually reformat the conclusion for investment committee, lenders, or multiple clients.

**How might we:** How might we turn approved underwriting into a concise, source-backed decision package without creating another static artifact that immediately goes stale?

**Proposed experience:** Generate a configurable executive summary, key assumptions, red flags, scenario table, and source links from approved deal state. Support firm/client templates, a live review link, and export bundles.

**Design direction:** Primary flow: choose audience/template -> preview generated sections -> edit/approve -> share live or export. Preserve the link from every conclusion to its model input/source and display when the package is stale relative to the deal.

**MVP slice:** One IC template; executive summary; five red-flag types; source links; editable preview; PDF export and live read-only link.

**Out of scope:** A general presentation editor and every client format in the first release.

**Primary metric:** Median time from approved underwriting to shared decision package.

**Secondary and guardrail metrics:** Packages generated; sections edited; live views; stale-package warnings; repeated use; support for custom formats.

**Validation:** Generate concierge packages for 20 completed deals, observe edits and audience needs, then productize the common 80%.

**Dependencies:** Approved deal state, risk flags, scenario data, document generation, permissions.

**Key risk:** Generated narrative can overstate certainty. Limit claims to approved inputs and label inference, assumptions, and missing evidence.

**Public-edition evidence basis:** Aggregate transcript counts are reported above. Direct customer quotes, participant names, timestamps, and private Sybill recording links are omitted.


### 10. Commercial Lease Intelligence - Multi-Tenant Underwriting

**Posture:** Advance from lease due diligence to a narrow commercial underwriting beta 
**Target user:** Office/retail/industrial acquisitions analyst and broker 
**Impact / effort / roadmap:** 67/100 · XL · Later 
**Directional evidence:** 56 matching meetings; 31 with explicit signals; 7 post-sale or working-session meetings.

**PostHog baseline (Very early sample):** The test-filtered Cactus 2.0 rent-roll funnel included 4 triggering users and 2 completions within 30 minutes (50%; 74.9-second median among converters). Raw completion events covered only 6 users, too small for a broad build decision.

**Problem:** Multi-tenant commercial deals require lease/amendment abstraction, recovery structures, rollover assumptions, and portfolio-scale review. This is a painful segment, but depth expectations are set by ARGUS.

**How might we:** How might we turn many leases and amendments into a reviewable rollover model without asking the analyst to start from scratch?

**Proposed experience:** Batch-ingest leases, build an amendment-aware abstraction, reconcile it with the rent roll, and generate a tenant rollover/recovery schedule. Export the approved schedule into supported Excel/ARGUS handoffs.

**Design direction:** Primary flow: upload lease set -> processing monitor -> tenant abstraction queue -> rent-roll comparison -> rollover schedule -> export. The UI must handle partial success, duplicate/amended documents, tenant identity, and hundreds of exceptions.

**MVP slice:** One asset class and lease type; batch upload; base lease + amendment chain; critical term abstraction; rent-roll discrepancy report; basic rollover schedule.

**Out of scope:** All commercial asset classes, full ARGUS parity, and lease administration.

**Primary metric:** Analyst hours to produce an approved tenant rollover schedule.

**Secondary and guardrail metrics:** Critical-term accuracy; exception rate; leases per completed job; export rework; paid beta conversion.

**Validation:** Choose office or industrial based on qualified pipeline; benchmark 500 leases against human abstractions before promising full underwriting.

**Dependencies:** Document hierarchy, tenant/entity resolution, recovery rules, schedule engine, export integration.

**Key risk:** Commercial lease variability can overwhelm the team. Enter through a narrow segment with measurable accuracy and a human-review workflow.

**Public-edition evidence basis:** Aggregate transcript counts are reported above. Direct customer quotes, participant names, timestamps, and private Sybill recording links are omitted.


## Now / Next / Later plan

### Now - prove the core promise

- Trust Center 2.0: narrow MVP for material T-12/rent-roll exceptions.
- Instant Deal Screen: explainable package-to-go/no-go workflow.
- Guided Activation: first-defensible-deal path and funnel instrumentation.
- Model Studio: technical spike only; do not promise arbitrary workbook support yet.
- Shared analytics foundation: deal identity, organization identity, activation, approval/export, scenario, and reliability events.

### Next - deepen workflow fit

- Market Intelligence evidence cards and private-memory validation, using the existing 50-organization behavior as the design-partner pool.
- Model Studio MVP for one asset class and supported Excel subset.
- Scenario Lab with bounded natural-language changes and versioning.
- Enterprise Workflow foundation: project roles, audit log, one connector, API job status.

### Later - make explicit segment bets

- Development Underwriter beta for one archetype.
- Decision Packages only after generation, edit, share, export, and view instrumentation establishes demand.
- Commercial Lease Intelligence beta for one asset/lease slice.

This sequence is intentionally Now/Next/Later, not a delivery commitment. Engineering must size the enabling architecture and current production gaps before dates are assigned.

## Portfolio dependencies

```text
Source metadata + reviewer state
├─ Trust Center
├─ Decision Packages
└─ Market Intelligence evidence

Model parameter schema + versioning
├─ Model Studio
├─ Scenario Lab
├─ Development Underwriter
└─ Commercial Lease Intelligence

Identity + audit events + async jobs
├─ Guided Activation analytics
├─ Enterprise Workflow
└─ External sharing
```

## Competitive implications

- Cactus's current public positioning already emphasizes source-backed facts, reviewer control, Excel-ready output, Market Intelligence, and Proprietary Memory. The highest-impact roadmap should make those claims visibly true in end-to-end workflows, not add disconnected feature labels.
- redIQ publicly offers a proprietary valuation model and QuickSync to place standardized data into customer Excel templates. Formula-aware, lower-friction model interoperability is therefore a competitive requirement, not an edge case.
- ARGUS Enterprise remains the depth benchmark for lease-by-lease modeling, market-leasing assumptions, scenario analysis, configurable reports, and Excel connectivity. Cactus should enter commercial through a narrow automation/review wedge rather than promise immediate parity.
- Dealpath owns pipeline, CRM, integrations, reporting, and adjacent AI. Cactus should integrate with systems of record rather than spend core capacity rebuilding a CRM.
- Northspyre spans development acquisition through construction, draw management, and stabilization. Cactus's development boundary should remain underwriting, decision support, and handoff.

## What not to build now

- A generic chat assistant without model controls, lineage, and confirmation.
- A full CRM or transaction-management replacement.
- Full construction project management, invoice approval, or vendor workflows.
- Simultaneous deep support for every commercial asset class.
- A hard break from Excel; customer evidence and competitors both argue for interoperability.

## Measurement plan

Create a shared product scorecard before development begins:

- **North star:** median time from package receipt to approved/shareable decision.
- **Activation:** percentage of new accounts completing one approved or exported real/sample deal.
- **Trust:** material corrections after approval and percentage of key inputs with reviewed evidence.
- **Habit:** deals screened/underwritten per active account and weekly returning underwriting teams.
- **Revenue:** pilot-to-paid conversion, enterprise win rate, expansion ARR, and loss reasons tied to missing workflow capabilities.
- **Efficiency guardrail:** onboarding/support hours per activated account.
- **Quality guardrail:** false-negative screening rate and escaped material extraction/model errors.

## Decision gates before committing engineering capacity

1. Confirm current production gaps for each project; several capabilities already exist publicly.
2. Join transcript evidence to CRM stage, account value, closed/lost reason, and current customer status.
3. Repair the analytics gaps: consistent environment labels, stable deal/account identity, scenario events, approval/export/share outcomes, dead-click coverage, and revenue joins.
4. Size each project with Engineering and identify shared platform work.
5. Select 5-10 design partners across prospect, new customer, active customer, and enterprise segments.
6. Re-score the portfolio collaboratively; scores are decision inputs, not automatic commitments.

## Artifacts

Machine-readable evidence indexes, account-level research, and Linear import files remain internal and are not included in this public edition.


## Sources and framework references

- [Product Manager Skills](https://github.com/deanpeters/Product-Manager-Skills)
- [Cactus CRE underwriting product](https://www.trycactus.com/cre-underwriting-software)
- [Cactus pricing and current plan capabilities](https://www.trycactus.com/pricing)
- [Cactus AI-powered due diligence](https://www.trycactus.com/ai-powered-due-diligence)
- [redIQ product and QuickSync positioning](https://www.rediq.com/)
- [ARGUS Enterprise](https://www.altusgroup.com/solutions/argus-enterprise/)
- [Dealpath CRM and platform positioning](https://www.dealpath.com/crm/)
- [Northspyre commercial development platform](https://www.northspyre.com/all-asset-classes/commercial)
- [Linear importer field documentation](https://linear.app/docs/import-issues)
- Cactus 1.0: internal PostHog project; aggregate results are reported above.
- Cactus 2.0: internal PostHog project; aggregate results are reported above.

## Research caveats

- Meeting date, account status, company, ARR, opportunity stage, closed/lost outcome, and asset class were not consistently present in the manifest.
- External labeling includes some product partners, vendors, advisors, and working sessions; title-based classification reduced but cannot eliminate this noise.
- Transcript language reflects both independent customer voice and reactions to a demo. Seller narration was excluded by known speaker name, but leading-question effects remain.
- Evidence counts are theme-detection outputs and should not be presented as statistically representative market incidence.
- PostHog cohorts are small, partially migrated, and unevenly instrumented. Known internal users were excluded when event-time email was available; typed funnels used the configured test-account filter.
- Several server events label environment as `dev`, taxonomy discovery omitted older dynamic events, and the data-warehouse schema endpoint failed. Behavioral findings therefore distinguish strong direct signals from weak or missing instrumentation.
- Effort estimates are preliminary t-shirt sizes inferred from scope, not engineering commitments.

---

**Public redacted edition.** This document contains aggregate product research. Direct customer identities, verbatim quotes, private recordings, account-level data, and authenticated analytics links are intentionally excluded.
