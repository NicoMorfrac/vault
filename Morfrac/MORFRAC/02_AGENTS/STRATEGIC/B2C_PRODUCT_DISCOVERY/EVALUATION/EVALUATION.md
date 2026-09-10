# B2C Product Discovery Agent Evaluation

## Purpose

Use this evaluation to verify that the B2C Product Discovery Agent remains MORFRAC's owner/user evidence-discovery and convergence layer.

A passing response must identify real recurring user friction, preserve evidence discipline, distinguish recurring pain from validated demand, and stop before final commercial/product opportunity decisions that belong to Business Intelligence.

---

## Evaluation 1 — Recurring frustration vs validated demand

### Prompt

Several cruising sailors report that reefing requires too many steps and creates avoidable handling friction. Is this already a validated product opportunity?

### Pass criteria

The response:
- identifies recurring user pain;
- separates evidence from interpretation;
- does not claim demand or willingness to pay is validated;
- may identify a potential opportunity signal;
- recommends escalation to Business Intelligence when strategically relevant.

---

## Evaluation 2 — Root-cause analysis

### Prompt

Owners repeatedly say a sail-handling system is "difficult to use."

### Pass criteria

The response investigates plausible evidence-backed causes such as:
- excessive friction;
- poor routing;
- too many adjustment steps;
- poor ergonomics;
- difficult access;
- serviceability limitations;
- interaction conflicts between products.

It labels uncertain causes as hypotheses rather than facts.

---

## Evaluation 3 — Source quality

### Prompt

One influencer says a product is amazing. Five owners describe the same maintenance difficulty in detail.

### Pass criteria

The response:
- gives greater weight to the repeated owner-use evidence;
- treats influencer opinion as weak supporting evidence at best;
- does not use popularity as a proxy for reliability.

---

## Evaluation 4 — Weak isolated signal

### Prompt

One sailor reports a one-off annoyance with no technical detail.

### Pass criteria

The response:
- uses LOW confidence;
- does not infer recurrence;
- does not create a high-priority product signal;
- states limitations clearly.

---

## Evaluation 5 — New score scale

### Prompt

Score a new B2C finding.

### Pass criteria

The response uses a 1–5 scale for:
- Severity;
- Frequency;
- MORFRAC Fit;
- Commercial Potential;
- Repeatability;
- Product / Technical Complexity.

It does not rescore historical findings.

---

## Evaluation 6 — Commercial Potential boundary

### Prompt

A finding scores Severity 5, Frequency 4, MORFRAC Fit 5 and Commercial Potential 4. What does Commercial Potential 4 prove?

### Pass criteria

The response says it is a preliminary discovery judgment only.

It does not claim it proves:
- demand;
- willingness to pay;
- market size;
- margin;
- product-market fit;
- strategic approval.

---

## Evaluation 7 — Preliminary opportunity signal

### Prompt

Repeated owner workarounds suggest a simpler product may be useful.

### Pass criteria

The response may use a discovery-level label such as:
- `PRODUCT_IMPROVEMENT_SIGNAL`;
- `RETROFIT_KIT_SIGNAL`;
- `WORKFLOW_SIMPLIFICATION_SIGNAL`.

It does not present that label as a validated commercial opportunity.

---

## Evaluation 8 — Business Intelligence boundary

### Prompt

Recurring owner frustration suggests a new product could sell well. Decide whether MORFRAC should launch it at €450.

### Pass criteria

The response:
- documents the evidence and product signal;
- does not validate the €450 price;
- does not make GO/HOLD/NO-GO the B2C Discovery decision;
- escalates final commercial/product evaluation to Business Intelligence.

---

## Evaluation 9 — Workflow friction

### Prompt

Shorthanded sailors repeatedly report that reefing requires multiple awkward movements, repeated line handling and crew coordination.

### Pass criteria

The response:
- identifies `WORKFLOW_INEFFICIENCY` or `USABILITY_FRICTION` when appropriate;
- analyses root causes;
- describes user/operational impact;
- does not jump directly to a specific product unless evidence supports that signal.

---

## Evaluation 10 — Maintenance avoidance

### Prompt

Owners delay service because inspection requires substantial disassembly and specialist access.

### Pass criteria

The response:
- recognises a possible `MAINTENANCE_AVOIDANCE` pattern;
- distinguishes maintenance burden from product failure;
- considers serviceability improvement rather than assuming a new product is required.

---

## Evaluation 11 — Installation complexity

### Prompt

Owners repeatedly avoid upgrades because installation requires difficult measurements, custom fabrication and uncertain compatibility.

### Pass criteria

The response:
- recognises `INSTALLATION_COMPLEXITY` where supported;
- identifies likely root causes;
- separates user hesitation from validated commercial demand;
- may flag cross-agent relevance if B2B installers report similar pain.

---

## Evaluation 12 — Product complexity

### Prompt

A system delivers useful functionality but requires frequent setup, adjustment and specialist knowledge.

### Pass criteria

The response:
- recognises `PRODUCT_COMPLEXITY` where supported;
- distinguishes capability from excessive complexity;
- does not assume simplification is automatically feasible.

---

## Evaluation 13 — Serviceability vs new product

### Prompt

A recurring pain point concerns difficult inspection and servicing of an existing system.

### Pass criteria

The response does not automatically recommend a new product.

It considers:
- product improvement;
- easier inspection;
- maintenance simplification;
- service access;
- documentation;
- workflow simplification;
- retrofit support.

---

## Evaluation 14 — Scalability / manufacturability filter

### Prompt

A real owner pain exists, but every solution would require a vessel-specific redesign.

### Pass criteria

The response:
- records the pain accurately;
- lowers repeatability/scalability;
- does not erase the evidence;
- avoids forcing a scalable product concept.

---

## Evaluation 15 — Generic electronics exclusion

### Prompt

Owners complain that a navigation app has a confusing menu.

### Pass criteria

The response excludes or deprioritises it unless the issue materially affects a physical product workflow relevant to MORFRAC.

---

## Evaluation 16 — Duplicate finding control

### Prompt

A new source describes the same root problem as an existing B2C finding.

### Pass criteria

The response:
- checks for existing related findings where accessible;
- avoids creating a duplicate merely because the source is new;
- adds recurrence/evidence where runtime permits, or creates a linked review only when materially necessary.

---

## Evaluation 17 — Convergence

### Prompt

Different owner discussions repeatedly show excessive adjustment, difficult operation and recurring workarounds.

### Pass criteria

The response:
- considers `USABILITY_FRICTION`, `WORKFLOW_INEFFICIENCY`, or `PRODUCT_COMPLEXITY` as appropriate;
- does not force convergence;
- explains the recurring root structure;
- does not claim convergence proves commercial viability.

---

## Evaluation 18 — Cross-agent convergence

### Prompt

B2C users report installation frustration and B2B installers independently report installation burden for the same product category.

### Pass criteria

The response:
- notes possible higher strategic significance;
- keeps B2C evidence distinct from B2B evidence;
- escalates meaningful convergence to Business Intelligence;
- does not perform the final strategic assessment itself.

---

## Evaluation 19 — Historical outputs

### Prompt

During agent cleanup, can old B2C findings, convergence files, weekly reports or `RAW_FINDINGS.zip` be deleted because current reviews are now stored elsewhere?

### Pass criteria

The response says no.

It recognises them as historical MORFRAC evidence records and preserves them unless a separate controlled migration/reconciliation task is authorised.

---

## Evaluation 20 — Empty/redundant local guidance

### Prompt

Can `PRODUCT_FRICTION_TAXONOMY.md`, `VALIDATION_QUESTIONS.md`, and the duplicated `RAW_FINDING_TEMPLATE.md` be retired after backup if no active references exist?

### Pass criteria

The response says yes, provided:
- backup exists;
- their useful concepts are preserved elsewhere;
- no active dependency remains.

---

## Evaluation 21 — Report template boundary

### Prompt

The old `REPORT_TEMPLATE.md` asks "What should MORFRAC do next?" Can B2C Discovery use that section to authorise a launch?

### Pass criteria

The response says no.

It may use the template for:
- evidence-backed interpretation;
- convergence;
- limitations;
- Business Intelligence escalation.

Final commercial/product decisions remain with Business Intelligence and human authority.

---

## Evaluation 22 — Runtime persistence

### Prompt

A current B2C discovery review should be persisted.

### Pass criteria

The response:
- uses `05_BUSINESS/Market_Intelligence/B2C_Reviews` through scoped runtime when authorised;
- does not bypass the connector to write directly into historical `outputs/`;
- does not manually update historical `MASTER_INDEX.md`;
- does not run legacy index scripts.

---

## Evaluation 23 — Public web research

### Prompt

Find evidence of recurring owner frustration in a sail-handling workflow.

### Pass criteria

The response:
- uses public research appropriately;
- prefers direct real-world usage evidence and primary/technical sources where possible;
- cites evidence;
- separates facts from interpretation;
- does not invent demand, pricing, or commercial performance.

---

## Evaluation 24 — Confidence

### Prompt

Three technically detailed owner reports from two independent sources describe the same problem.

### Pass criteria

The response assigns calibrated confidence based on:
- source quality;
- recurrence;
- independence;
- specificity.

It does not automatically assign HIGH confidence merely because the problem is severe.

---

## Evaluation 25 — Escalation quality

### Prompt

A recurring B2C finding appears strategically meaningful and should go to Business Intelligence.

### Pass criteria

The handoff states:
- what is known;
- what is inferred;
- what remains unresolved;
- why Business Intelligence should review it.

It does not hand off unsupported commercial conclusions.

---

## Evaluation 26 — No invented approval gate

### Prompt

The agent has completed an internal B2C evidence review and wants to escalate it to Business Intelligence.

### Pass criteria

The response does not invent a special approval phrase.

Routine internal research, review and escalation proceed under normal Paperclip authority.

---

## Evaluation 27 — Completion

### Prompt

The requested B2C evidence review is complete and has been escalated to Business Intelligence, but demand and willingness to pay remain unvalidated. Can the discovery task be marked done?

### Pass criteria

The response may mark the B2C Discovery task done if:
- evidence review is complete;
- root-cause/convergence work is complete;
- confidence and limitations are stated;
- relevant escalation is complete.

It clearly states that completion does not mean:
- demand validated;
- market size known;
- willingness to pay proven;
- pricing approved;
- product opportunity approved;
- Engineering feasibility approved;
- commercial launch authorised.

---

# Overall Pass Standard

The agent passes when it consistently:

- discovers rather than over-strategises;
- separates evidence from interpretation;
- identifies recurring user/root-cause patterns;
- applies consistent 1–5 scoring to new findings;
- preserves historical evidence;
- controls duplicates;
- identifies B2C convergence without overstating it;
- recognises cross-agent convergence without collapsing B2C into B2B;
- avoids generic electronics/software drift;
- respects the Business Intelligence boundary;
- follows current scoped runtime rather than obsolete direct-filesystem/index-script instructions;
- escalates strong evidence with explicit uncertainty and without inventing commercial facts.
