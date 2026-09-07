# MORFRAC Costing Standard

## Purpose

This file defines the technical costing rules used by the Project Costing Analyst.

It covers:

- cost classification;
- estimate maturity;
- calculation rules;
- cost/price/margin definitions;
- uncertainty treatment;
- controlled costing master-data structure.

Workflow, delegation, persistence and approval rules belong in `AGENTS.md`, not here.

---

# 1. Core Costing Principles

Keep these concepts separate.

## Cost

Economic resource consumed by the project under the applicable MORFRAC costing treatment.

## Cash

Timing and amount of actual cash movement, including:

- deposits;
- milestone payments;
- taxes and duties;
- freight;
- timing exposure.

Cash is not the same as cost.

## Price

Amount proposed or charged to the client after commercial policy.

Cost does not itself establish price.

## Revenue and Profit

Commercial/accounting outcomes.

Do not infer revenue or profit from cost alone.

---

# 2. Cost Taxonomy

## 2.1 Labour

Typical labour categories include:

- requirements and intake;
- project management and coordination;
- engineering analysis, design and review;
- CAD, drawings and documentation;
- procurement and supplier coordination;
- assembly;
- inspection;
- testing;
- installation;
- training;
- closeout;
- manuals;
- support.

Where MORFRAC uses fully burdened labour cost:

`Labour Cost = Approved Hours × Approved Cost Rate`

Do not use a customer billing rate as labour cost.

Identify whether the labour rate already includes:

- payroll burden;
- overhead;
- indirect costs.

Do not add the same burden again elsewhere.

---

## 2.2 Purchased and External Costs

Typical categories include:

- materials;
- components;
- external machining;
- fabrication;
- finishing;
- consultants;
- laboratories;
- prototypes;
- tooling;
- jigs;
- fixtures;
- NRE;
- certification;
- inspection;
- testing;
- attributable software/licensing;
- packing;
- freight;
- insurance;
- customs;
- duty;
- travel;
- accommodation;
- site work;
- installation.

Record relevant basis such as:

- supplier;
- quantity;
- MOQ;
- unit;
- currency;
- tax basis;
- freight basis;
- Incoterm where supplied;
- validity;
- lead time;
- exclusions;
- source reference.

---

## 2.3 Indirect, Commercial and Risk Costs

Use only when supported by an applicable MORFRAC policy or explicit project treatment.

Possible categories include:

- overhead/indirect allocation;
- warranty or after-sales allowance;
- commission;
- financing or credit cost;
- escalation;
- exchange-rate exposure;
- contingency for defined uncertainty;
- management reserve under approved policy.

Do not double-count a burden already contained in another rate or line item.

---

# 3. Core Calculations

## Line Cost

`Line Cost = Quantity × Unit Cost Rate`

## Labour Cost

`Labour Cost = Approved Hours × Approved Cost Rate`

## Base Cost

`Base Cost = Sum of Supported Cost Rows Before Separately Applied Contingency`

## Total Estimated Cost

`Total Estimated Cost = Base Cost + Applicable Indirect/Overhead + Contingency + Other Explicitly Included Costs`

Only add components not already embedded in another rate.

## Cost Variance

`Cost Variance = Current Cost View - Comparison Baseline`

## Estimate at Completion

`EAC = Actual + Applicable Committed/Accrued Cost + Forecast Remaining`

The treatment of commitments and accruals must be stated.

---

# 4. Price and Margin Calculations

Price scenarios are commercial analysis, not automatic price approval.

## Price from Markup

`Price = Cost × (1 + Markup Rate)`

## Price from Target Gross Margin

`Price = Cost / (1 - Gross Margin Rate)`

Do not use a margin rate at or above 100%.

## Gross Margin

`Gross Margin = (Price - Cost) / Price`

## Markup

`Markup = (Price - Cost) / Cost`

Gross margin and markup are not interchangeable.

Example:

If:

- Cost = 100
- Price = 125

Then:

- Markup = 25%
- Gross Margin = 20%

Always identify which measure is being used.

---

# 5. Calculation Controls

Every estimate must state:

- currency;
- tax-inclusive or tax-exclusive basis;
- relevant units;
- relevant dates;
- estimate maturity;
- source status;
- principal assumptions;
- exclusions;
- unpriced items.

For currency conversions:

- retain the original currency;
- record the exchange rate used;
- record the exchange-rate date;
- identify the converted value.

Use consistent units and periods.

Reconcile:

- individual rows;
- WBS sections;
- cost categories;
- subtotals;
- total cost.

Do not:

- treat a missing value as zero;
- divide by zero;
- hide unsupported allocations;
- double-count overhead or burdens;
- convert a public benchmark into a supplier quotation;
- convert a price scenario into an approved selling price.

Keep calculation precision internally.

Round presentation values consistently.

For percentage allocations, show:

- percentage;
- calculation base;
- resulting amount.

---

# 6. Evidence and Scenario Labels

Distinguish evidence from scenarios.

## Evidence Inputs

Examples:

- confirmed value;
- current supplier quotation;
- approved company parameter;
- historical actual;
- documented project actual.

## Scenario Inputs

Examples:

- low;
- base;
- high;
- budgetary assumption;
- estimated allowance;
- public benchmark.

Low/base/high scenarios are not statistical confidence intervals unless statistically supported.

A public benchmark is not a quotation.

A scenario selling price is not an approved selling price.

---

# 7. Estimate Maturity

Use these MORFRAC working classes unless replaced by a later approved company standard.

| Class | Purpose | Typical Information | Output Rule |
|---|---|---|---|
| Concept | Feasibility / order-of-magnitude discussion | Early scope, analogous evidence, major assumptions | Wide uncertainty; no false detail |
| Budgetary | Internal budget / client-discussion support | Initial WBS, preliminary hours, budgetary supplier inputs | Show allowances, unpriced items and validity |
| Preliminary | Decision / proposal preparation | Developed scope, specialist inputs, current quotations | Reconcile risks and commercial dependencies |
| Detailed | Baseline / final internal review | Stable scope, detailed WBS, current rates, quotations and schedule | Full QA and change-control basis |
| Change | Incremental decision | Existing baseline plus defined change | Show delta, sunk/committed/rework cost and revised exposure |
| EAC | Execution control | Baseline, actuals, commitments and remaining forecast | Reconcile data and variance causes |

Do not assign numerical accuracy ranges to these classes unless MORFRAC adopts a documented standard defining those ranges and the estimate satisfies its requirements.

---

# 8. Minimum Estimate Structure

A substantive project estimate should normally identify:

## Scope

- objective;
- included work;
- excluded work;
- estimate class;
- estimate date;
- currency and tax basis.

## Cost Breakdown

Use the applicable WBS and cost taxonomy.

For each material line where practical record:

- item/work package;
- quantity;
- unit;
- unit rate;
- source/basis;
- calculated cost;
- status;
- assumptions.

## Reconciliation

Show:

- direct labour;
- purchased/external costs;
- applicable indirects;
- contingency;
- other included costs;
- total estimated cost.

## Unknowns

Clearly identify:

- missing quotations;
- unpriced items;
- missing hours;
- unresolved scope;
- unsupported rates;
- dependencies.

Do not silently convert unknowns to zero.

## Assumptions and Dependencies

Material assumptions should be explicit and traceable to their basis.

## Risk and Contingency

Contingency must correspond to defined uncertainty.

Do not use contingency to conceal missing scope or known omitted cost.

## Commercial View

Where requested, keep clearly separate:

- estimated cost;
- price scenario;
- markup;
- gross margin;
- cash/timing implications.

---

# 9. Change Costing

For a defined project change, compare against a named baseline.

Distinguish:

- original baseline;
- added work;
- removed work;
- sunk cost;
- committed cost;
- rework;
- remaining work;
- schedule/cash consequences where supported.

Report both:

`Change Delta`

and, when relevant:

`Revised Project Estimate`

Do not overwrite or reinterpret the original baseline silently.

---

# 10. Actual Versus Estimate

Where reliable actual data is available, reconcile:

- original estimate;
- current approved baseline where different;
- actual cost;
- committed/accrued cost under the stated treatment;
- remaining forecast;
- EAC;
- variance;
- variance cause.

Do not label an accounting value as actual project cost unless its treatment and project attribution are supported.

---

# 11. Controlled Costing Master Data

Controlled costing master data is distinct from ordinary project estimates.

Typical controlled records include:

- costing parameters;
- labour/resource rates;
- MORFRAC price-list entries;
- discount policies;
- supplier identities/capabilities;
- dated supplier quotations.

Project assumptions must not be silently promoted into master data.

---

# 12. Shared Master-Data Fields

Controlled records should contain, where applicable:

- `record_id`;
- `record_type`;
- `status`;
- `revision`;
- value;
- unit;
- currency;
- tax basis;
- scope;
- geography;
- customer/channel;
- quantity band;
- applicability;
- source classification;
- source reference;
- source owner;
- approval owner;
- source date;
- approved date;
- effective-from date;
- effective-to/expiry date;
- authoritative system;
- authoritative-system record ID;
- last verified/sync timestamp;
- confidentiality;
- assumptions;
- exclusions;
- change reason;
- supersedes reference;
- Paperclip issue/approval reference.

Typical statuses:

- candidate;
- approved;
- future;
- active;
- superseded;
- expired;
- rejected.

---

# 13. Costing Parameter Records

Where applicable record:

- parameter code;
- category;
- role/resource/process;
- value;
- unit;
- rate type;
- calculation base;
- included burdens;
- effective dates;
- review frequency/date.

Rate types may include:

- payroll;
- burdened cost;
- transfer;
- bill;
- allocation;
- policy.

Do not store payroll-person data.

Use role/resource classes and approved aggregate rates.

---

# 14. MORFRAC Price-List Records

Where applicable record:

- product/service code;
- description;
- unit;
- quantity band;
- list/base price;
- currency;
- tax basis;
- geography;
- channel;
- customer class;
- inclusions;
- exclusions;
- validity/effective dates;
- related Odoo product/pricelist ID when supplied.

A price-list record is controlled commercial data and is not inferred from a project estimate.

---

# 15. Discount-Policy Records

Where applicable record:

- rule code;
- eligible product/service;
- eligible customer/channel/quantity;
- discount type;
- discount value;
- stackable yes/no;
- precedence;
- maximum authority;
- required approver;
- minimum-price or margin-guardrail reference;
- exclusions;
- validity.

Never store an unrestricted discount without an approver and applicable guardrail.

---

# 16. Supplier Records

Where applicable record:

- supplier code;
- legal/trading name;
- country;
- necessary business contact channel;
- approved/candidate status;
- capability;
- currency;
- payment basis;
- delivery basis;
- Incoterm where supplied;
- quality/NDA/compliance references;
- quote/price record ID;
- part/service/scope;
- quantity;
- MOQ;
- tooling/NRE;
- lead time;
- validity;
- tax;
- freight/duty basis;
- evidence path;
- exclusions;
- supported performance notes.

Do not record unsupported certifications or capability claims.

Supplier quotations are append-only dated commercial records.

Do not replace the historical quote record with a single overwritten “current price”.

---

# 17. Data Integrity Rules

Always distinguish:

- source fact;
- calculated value;
- estimate;
- assumption;
- scenario;
- candidate master value;
- controlled master value.

Do not:

- fabricate missing values;
- backfill unknown values merely to complete a table;
- promote observed/public/historical values into controlled current rates without the applicable master-data process;
- erase superseded values or historical quotations;
- hide conflicts between sources.

Where sources conflict, expose the conflict and identify the decision or evidence required to resolve it.

---

# 18. Output Quality

A costing result should allow a reviewer to understand:

- what is being costed;
- what is included;
- what is excluded;
- which values are supported;
- which values are assumptions;
- how the arithmetic was performed;
- which uncertainty remains;
- what the estimate maturity is;
- how cost differs from price and cash;
- what decision or additional evidence is required.

Precision in presentation must not imply greater certainty than the evidence supports.