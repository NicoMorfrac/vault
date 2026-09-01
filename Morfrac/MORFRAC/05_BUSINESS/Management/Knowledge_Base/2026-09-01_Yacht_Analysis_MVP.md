---
type: capability_baseline
source_agent: Codex_Assisted_Setup
created: 2026-09-01
as_of: 2026-09-01
audience: internal
record_class: engineering_workflow_setup
status: implemented_mvp
approval_status: owner_requested_implementation
related_findings: []
related_concepts:
  - yacht_upgrade_analysis
  - engineering_provenance
  - human_design_authority
related_projects: []
related_reports:
  - "[[05_BUSINESS/Management/Knowledge_Base/README]]"
---

# Yacht Sail Plan & Deck Plan Upgrade Analysis MVP

## Purpose

MORFRAC now has an on-demand Paperclip specialist group for analysing an existing yacht from authorised project evidence and proposing mission-specific sail-plan, deck-system and retrofit packages. This is engineering decision support, not autonomous yacht design or professional sign-off.

## Team and authority

The Lead Naval Architecture Reviewer reports to CTO. Boat Intake, Geometry & Sail, Deck Systems, Mission Profile, Rating & Performance, Engineering Loads, Upgrade & Retrofit, and Yacht Cost/Benefit report to the yacht lead.

- The yacht lead coordinates evidence and challenges the package; it is not design authority.
- Existing Engineering/FEA retain professional engineering and solver responsibility.
- Existing Project Costing owns MORFRAC prices, discounts, suppliers and precise estimates. The yacht Cost/Benefit role uses broad bands only.
- ORC/IRC rating effects remain qualitative until an authoritative rating-office/tool trial is supplied.
- Raffa is excluded. Odoo, schedules/heartbeats, external rating/VPP, CAD, FEA, purchasing, manufacture and external release are not connected by this rollout.

## Data and workflow

Every engineering property uses value, unit, source, source document, page, confidence, provenance and notes. Provenance is CERTIFIED, DRAWING_MEASURED, USER_SUPPLIED, CALCULATED, ESTIMATED, ASSUMED or UNKNOWN. Conflicts become UNKNOWN until a human resolves them. If no Boat Model exists, the intake role can now build a read-only canonical model preview directly from declared project documents and exact human-supplied measurements. Missing fields are not invented. A validated inline model and human-approved Mission Profile can then enter the final preview without creating an uncontrolled intermediate file.

The lead prepares a frozen work plan for specialist issues. Only an exact later human approval dispatches it. Deterministic Python modules perform unit conversion, sail reference areas, geometry/ratio screening, static block resultants, preliminary sheet-load checks and transparent recommendation scoring. These calculations expose inputs, assumptions, equations, results, factors of safety and limitations.

After specialist reconciliation and lead review, a deterministic preview freezes seven output files, their exact destination paths and all source hashes. Only a later exact human approval may create a new version under the named project's existing `01_Structures/Yacht_Analysis/Analyses` branch. Existing revisions cannot be overwritten. Saving is not recommendation, engineering, rating, cost, purchase, manufacture or release approval.

## Implemented outputs

- internal Markdown analysis report;
- canonical Boat Model;
- immutable source manifest;
- derived metric records;
- ranked recommendations with visible scoring;
- minimal/recommended/maximum-practical packages;
- run receipt.

## Current limitations

PDF intake is text-only. Scanned/raster drawing interpretation, calibrated geometry and full DXF parsing are not automated. No VPP, rating engine, polar/routing, rig model, CFD, structural solver or hardware/product database is connected. Candidate cost classes are management bands rather than MORFRAC prices. Conclusions narrow when required evidence is unknown.

## Phase 2 direction

Add calibrated vector/DXF extraction, authorised ORC/IRC trials, polar/routing comparison, reviewed engineering solver adapters, WLL/BL-based hardware matching, and a controlled Costing handoff. Do not connect supplier/product/pricing data until the existing Costing authority and human approval model are preserved.

## Related Links

- [[00_SYSTEM/ORGANISATION|Current organisation and authority]]
- [[00_SYSTEM/SCOPED_RUNTIME|Scoped runtime rules]]
- [[05_BUSINESS/Management/Knowledge_Base/README|Company knowledge index]]
