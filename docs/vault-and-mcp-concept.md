# Vault and MCP Concept

## Builder Prompt

Design a market-agnostic proprietary real estate intelligence system called the Vault. The Vault lets real estate professionals quickly build their own structured database of property, building, street, micro-market, and market facts, then use AI systems like ChatGPT, Claude, Codex, Perplexity, or local open-source models to analyze that data without training a custom model.

The Vault is not a CRM, not a notes app, and not a long-text document store. It is a structured, time-aware, evidence-backed fact database with a spreadsheet-like interface, AI-assisted enrichment, conflict resolution, folders, automations, and optional MCP access for external AI tools.

## Core Idea

Most real estate professionals have fragmented knowledge:

- Broker emails.
- Listing portals.
- PDFs.
- Spreadsheets.
- Market reports.
- Appraisals.
- Auction files.
- Lease files.
- Internal deal notes.
- Local market intuition.

The Vault turns that fragmented information into a proprietary structured fact layer.

The user should be able to:

- Add data manually.
- Upload CSVs/documents.
- Scrape or connect to market data providers.
- Ask AI to enrich missing facts.
- Create custom AI-generated columns.
- Build folders for markets, portfolios, searches, or deal sets.
- Query the Vault through an analyst interface.
- Use external AI tools against the Vault through MCP or similar controlled interfaces.

## Product Principle

The Vault should make it extremely easy for a real estate professional in any market in the world to build a proprietary knowledge base as fast as possible.

The system should not require model fine-tuning. Instead, it should expose clean structured facts and scoped context to AI tools.

Long-term model options:

- Hosted LLMs such as ChatGPT, Claude, Codex, Perplexity.
- Local/open-source models connected to the Vault.
- Future internal analyst agents.

## What The Vault Is

The Vault is the source-of-truth factual database.

It stores:

- Property facts.
- Building facts.
- Street facts.
- Micro-market facts.
- Municipality/market facts.
- Portfolio or owned-asset facts if needed later.
- Historical fact values over time.
- Source/provenance metadata.
- Evidence behind facts.
- Conflict records.
- Folder membership.
- Automation settings.

It does not store long prose in the main grid.

Main Vault grid values should be short, structured, and filterable.

## What The Vault Is Not

The Vault is not:

- A CRM.
- A notes diary.
- A long-form document repository.
- A chat transcript store.
- A generic file drive.
- A single Google Sheet as the backend.
- A black-box AI memory.

Chat history, long documents, screenshots, and raw source payloads can exist in supporting storage, but the visible Vault remains a clean factual grid.

## Source Of Truth

Use the app database as the true Vault source of truth.

Google Sheets/CSV should be:

- Import surfaces.
- Export surfaces.
- Sync surfaces if useful.
- UI inspiration for the spreadsheet-like grid.

Do not make Google Sheets the canonical backend. Fact history, evidence, conflicts, folders, retention rules, and automations will become brittle if forced into a flat sheet.

## Entity Model

The Vault should support multiple row/entity types.

Recommended entity types:

- `property`: unit, house, listing, comp, auction asset, owned asset.
- `building`: elevator, year built, facade, known works, community facts.
- `street`: pricing trend, perception, access, liquidity, footfall, demand.
- `micro_market`: neighborhood/submarket facts for comps and market selection.
- `municipality`: broader market facts.
- `market`: city/region/national-level facts.
- `portfolio_asset`: optional later lifecycle entity for owned assets.
- `source_record`: optional internal entity for raw/sampled source data.

Every row should have an explicit `entity_type`, even if the UI makes the distinction feel natural.

This allows one Master Vault to support:

- Deal underwriting.
- Acquisitions.
- Development analysis.
- Portfolio analysis.
- Market research.
- Comp selection.
- Custom AI analysis.

## Fact Model

Facts should be singular structured values.

Examples:

- `asking_price`
- `final_sale_price`
- `constructed_m2`
- `usable_m2`
- `price_per_m2`
- `date_first_seen`
- `date_last_seen`
- `time_on_market_days`
- `building_year`
- `elevator`
- `floor`
- `exterior_windows`
- `terrace_m2`
- `condition`
- `renovation_level`
- `auction_deposit`
- `current_bid`
- `population_growth_rate`
- `median_income`
- `transaction_volume`
- `market_price_per_m2`
- `permit_approval_days`

Avoid long text fields. If text is needed, use short structured outputs or categories.

## Time-Series Facts

Do not overwrite prior facts.

The visible grid should show the latest valid value by default, but the underlying system should preserve historical fact records.

Each fact record should support:

- Entity id.
- Field name.
- Value.
- Value type.
- Timestamp.
- Created by/source.
- Provenance category.
- Evidence pointer.
- Status: valid, invalid, outdated, superseded.

When a value changes:

- Add a new fact record.
- Mark old facts invalid/outdated only when appropriate.
- Preserve history.

## Provenance

Track provenance internally using these categories:

- `user`: manually entered or user-approved.
- `document`: extracted from uploaded files such as CSV, PDF, appraisal, lease, auction file, mortgage quote.
- `AI`: inferred or generated by analyst/custom column.
- `market_data_provider`: pulled from listing portals, public datasets, APIs, broker sites, auction portals, Catastro-like sources, etc.

The main Vault grid should not show provenance by default.

Provenance should appear when the user clicks a cell or opens fact history.

## Evidence

Every extracted fact should retain evidence where feasible.

Evidence examples:

- Website screenshot/crop showing the scraped value.
- Document crop/page image showing extracted value.
- Provider response snippet.
- CSV upload row reference.
- User entry metadata.

Evidence is not displayed in the main Vault grid.

Evidence is used for:

- Conflict resolution.
- Auditing.
- Explaining where facts came from.
- Debugging extraction.
- Supporting assumptions or analysis.

## Conflict Resolution

Conflicts occur when two facts disagree materially.

Examples:

- Listing says 96 m2, document says 74 usable m2.
- AI inferred a market category but user entered a different category.
- Provider A says no elevator, Provider B says elevator.

UI behavior:

- Show a small conflict/error icon inside the affected cell.
- Clicking opens a conflict-resolution popup.
- Popup shows conflicts one by one, e.g. `1/51`.
- Show values, timestamps, provenance, source/evidence, and recommended resolution.
- Allow field-specific resolution rules.

Example rules:

- For `usable_m2`, prefer user-confirmed or document-extracted value over listing portal.
- For `asking_price`, prefer latest market-provider scrape.
- For tax/permit facts, prefer official/public source.

User-approved/manual facts generally override AI/provider facts.

## Folders

Folders are persistent scoped views/groups over the Master Vault.

They do not duplicate data.

A row/entity can belong to multiple folders.

Folders can be:

- Manually created.
- AI-created from natural-language tasks.
- Saved filters.
- Living research scopes.
- Automation scopes.

Examples:

- `Mestalla Opportunities`
- `High Upside Valterna`
- `Owned Portfolio`
- `Subastas Watch`
- `Screened Out / Comps`
- `Market Intelligence`
- `Assumption Support`

Folder creation can trigger fresh research:

- Search externally.
- Add new entities/facts to Master Vault.
- Attach those entities to the folder.
- Keep the folder updated over time if automation is enabled.

## Folder Automation

Folders should support their own automation settings:

- Refresh cadence.
- Allowed connectors.
- AI enrichment prompts.
- Custom columns.
- Alert rules.
- Evidence retention.
- Cost/time budget.
- Export/share settings.

Folders reduce cost because AI/research can run against a focused subset instead of the whole Master Vault.

If a folder automation exceeds budget or expected cost/time, pause and ask for approval.

## Retention

Structured facts should generally be retained indefinitely unless deliberately deleted/export-archived.

Evidence retention can be tiered:

- Active opportunities: keep all evidence.
- Owned portfolio: keep indefinitely.
- Assumption support: keep indefinitely.
- Market intelligence: configurable long-term retention.
- Screened-out/comps: facts forever, evidence 6-12 months by default.
- Archive: low-cost retention.

Storage management should be automated through settings, not manual cleanup.

## Custom AI Columns

The Vault should support user-created AI columns.

UI pattern:

- Spreadsheet-like grid.
- `+` in the column/header area.
- Column creator popover with:
  - Label.
  - Format.
  - Prompt.
  - `@` references to other columns.
  - AI Generate button.

Output format options:

- Number.
- Currency.
- Percentage.
- Date.
- Yes/no.
- Short text.
- Dropdown/category.
- URL.
- Formula/computed field.

Outputs should be short and validated:

- Short text limited around 120 characters by default.
- Number must parse.
- Currency defaults to relevant local currency where configured.
- Date must parse.
- Category must match allowed values.

Custom AI columns can use:

- Vault/document extraction by default.
- Optional web search toggle.
- Optional market data connector toggle.
- Advanced connector selection.

Generation scope:

- All Vault rows.
- Visible/filtered rows.
- Selected rows.
- Folder only.

Before expensive runs, show estimated cost/time.

## Analyst Interface

The app should include an analyst assistant, ideally as a right-side panel available across pages.

The analyst should have contextual access depending on page:

- Vault page: selected rows, filters, folders, conflicts.
- Deal/property page: current entity, facts, history, evidence.
- Folder page: folder scope and automation settings.
- Dashboard: high-level market and data updates.
- Settings: assumptions, automations, connectors, approvals.

The analyst can:

- Query Vault data.
- Analyze selected rows/folders.
- Search externally if enabled.
- Create folders.
- Fill custom AI columns.
- Propose new facts.
- Propose conflict resolutions.
- Propose marking facts invalid/outdated.
- Explain analysis using facts and evidence.

Chat history is stored separately from the Vault. Only approved structured facts are written to the Vault.

## MCP Concept

MCP should be treated as an optional interface layer that lets external AI tools safely interact with the Vault.

Purpose:

- Allow Claude, ChatGPT, Codex, Perplexity, or local models to query Vault/folders.
- Let external agents run analysis on selected Vault scopes.
- Let external agents write structured facts back when approved by the user in the external AI interface.

Do not expose raw database access.

Expose controlled tools/actions.

## MCP Design Principles

MCP should:

- Be controlled and typed.
- Respect Vault schema.
- Avoid long-text writes into factual fields.
- Require source/provenance metadata on writes.
- Support scoped access to folders to control cost/context.
- Preserve fact history rather than overwrite.
- Never delete facts directly; mark invalid/outdated where appropriate.
- Log all write operations.
- Support idempotency keys for writes.
- Allow the connected LLM/client to handle user approval before write calls.

## MCP Approval Model

The user’s preference:

- MCP can support read/write technically.
- Before an external LLM writes into the Vault, the LLM using the MCP should ask the user for approval in that LLM’s own interface.
- The Vault app does not need to own every external approval flow.

Recommended implementation:

- MCP write tools require an `approved_by_user` or equivalent confirmation field.
- External LLM is responsible for obtaining approval before invoking commit/write.
- MCP logs caller/client, timestamp, operation, affected facts, and confirmation metadata.
- For higher-risk operations, MCP may reject writes unless approval metadata is present.

This keeps governance with the active AI user experience while still protecting the Vault.

## MCP Tool Categories

Recommended controlled tools:

### Query Tools

- `query_vault`
- `query_folder`
- `get_entity`
- `get_fact_history`
- `search_entities`
- `get_conflicts`
- `get_folder_summary`

### Analysis Tools

- `analyze_folder`
- `analyze_market`
- `compare_entities`
- `find_comps`
- `summarize_market_facts`
- `rank_opportunities`
- `run_financial_analysis`

These can return structured analysis without changing Vault data.

### Write Tools

- `propose_facts`
- `commit_facts`
- `mark_fact_invalid`
- `resolve_conflict`
- `create_folder`
- `update_folder_rules`
- `create_custom_column`
- `run_folder_research`

Writes should be structured and approval-aware.

## MCP Query Examples

Examples external agents should be able to ask:

- “Show all properties in this folder with usable_m2 over 70 and price_per_m2 below market average.”
- “Summarize the last 12 months of price_per_m2 changes for this micro-market.”
- “Find comparable properties within 500 meters of this subject property.”
- “Which facts conflict for this asset?”
- “Analyze this folder and tell me which rows need fresh research.”

## MCP Write Examples

Examples:

- External Claude session finds new market facts and asks user approval.
- User approves in Claude.
- Claude calls MCP `commit_facts` with structured facts and approval metadata.
- Vault stores new timestamped facts with provenance `AI` or `market_data_provider`.

Another example:

- ChatGPT analyzes a folder and finds a fact conflict.
- It asks user: “Do you want to mark the old 96 m2 value as invalid and keep 74 usable_m2 as current?”
- User approves.
- ChatGPT calls `mark_fact_invalid`.
- Vault preserves both records and shows latest valid value.

## MCP Safety Rules

MCP should not allow:

- Raw SQL/database access.
- Destructive deletes as a normal operation.
- Long unstructured text writes into core Vault fields.
- Silent overwrites.
- Schema mutation without explicit tool support.
- Unapproved high-impact writes.
- Secret or credential exposure.

MCP should allow:

- Structured reads.
- Scoped folder reads.
- Structured writes with approval metadata.
- Fact history preservation.
- Conflict-aware updates.
- Export to AI-readable formats.

## Export Without MCP

Even without MCP, folders should support export/share:

- CSV.
- JSON.
- Markdown brief.
- Spreadsheet export.
- Possibly API export later.

MCP is useful, but exports are still valuable for tools that do not support MCP.

## UI Design Direction

Vault UI should feel like a polished spreadsheet/database product:

- Clean white/off-white background.
- Charcoal text.
- Soft gray surfaces.
- Purple used sparingly for primary/AI actions.
- Minimal gridlines.
- High whitespace.
- Apple-level polish.
- Functional animation only.

Custom column design should follow the provided screenshot pattern:

- Add-column `+` near header.
- Floating popover.
- Label field.
- Format dropdown.
- Prompt box.
- `@` column references.
- AI Generate action.

Vault update animation:

- Compact floating pill when properties/facts are added or updated.
- Example: `12 properties updated... +214 -0`.
- Green for added/updated facts.
- Red for removed/invalidated facts.
- Calm number tick animation.
- Informational, not celebratory.

## Implementation Roadmap

### Phase 1: Vault Core

- Internal database as source of truth.
- Entity model.
- Fact model.
- Time-series facts.
- Latest valid value grid.
- CSV import/export.
- Basic folders.

### Phase 2: Provenance and Evidence

- Provenance categories.
- Evidence capture.
- Cell fact history.
- Conflict detection.
- Conflict resolution popup.

### Phase 3: AI Layer

- Analyst panel.
- Custom AI columns.
- Folder analysis.
- Web/market connector toggles.
- Cost/time estimates.

### Phase 4: Automation

- Folder refresh schedules.
- Retention rules.
- Budget controls.
- Automated fact enrichment.
- Conflict detection jobs.

### Phase 5: MCP/API Layer

- Controlled read tools.
- Controlled analysis tools.
- Controlled write tools.
- Approval metadata.
- Logging/audit.
- Scoped folder access.

## Open Product Questions

Questions for the product team:

- Which entity types should ship in MVP: property, building, street, micro-market, municipality?
- Should market-level rows appear in the same grid as property rows, or use grouped views/templates?
- What is the minimum viable evidence system for launch?
- Which write operations should MCP support first?
- Should MCP be built before or after internal analyst workflows?
- What storage limits and retention defaults should be tied to pricing?
- How much Google Sheets sync is needed versus CSV import/export?
- Should custom AI columns run synchronously or as background jobs?
- What approval metadata should MCP require for write calls?

## Out Of Scope For Initial Vault Build

- Full CRM pipeline.
- Full document management system.
- Model fine-tuning.
- Raw database access through MCP.
- Destructive deletion workflows.
- Full mobile app.
- Highly custom per-client schemas before core fact model is stable.
