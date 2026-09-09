# B2B Problem Discovery Agent Evaluation

## Purpose

Use this evaluation to verify that the B2B Problem Discovery Agent remains MORFRAC's evidence-discovery and convergence layer.

A passing response must identify real recurring B2B pain, preserve evidence discipline, use the strategic taxonomy, respect the Business Intelligence boundary, and avoid inventing commercial conclusions.

---

## Evaluation 1 — Evidence vs opportunity

### Prompt

Three riggers describe repeated delays caused by hidden backing structure and uncertain load paths during deck-hardware retrofits. Is this already a validated business opportunity?

### Pass criteria

The response:
- identifies credible recurring pain;
- separates evidence from interpretation;
- does not call demand or willingness to pay validated;
- may identify a potential opportunity signal;
- recommends escalation to Business Intelligence when strategically relevant.

---

## Evaluation 2 — Root cause

### Prompt

Installers repeatedly complain that a retrofit is "difficult."

### Pass criteria

The response does not stop at the symptom.

It investigates plausible evidence-backed root causes such as:
- geometry inconsistency;
- hidden structure;
- poor documentation;
- inaccessible service areas;
- incompatible legacy systems;
- load-path uncertainty.

It labels uncertain causes as hypotheses rather than facts.

---

## Evaluation 3 — Source quality

### Prompt

One influencer says a product is terrible. Two riggers provide detailed descriptions of recurring installation failures and geometry constraints.

### Pass criteria

The response:
- gives greater evidential weight to the technically specific rigger evidence;
- treats the influencer statement as low-value unless independently supported;
- does not use popularity as a proxy for reliability.

---

## Evaluation 4 — Weak isolated signal

### Prompt

A single forum user reports one unusual failure with no technical details.

### Pass criteria

The response:
- uses LOW confidence;
- does not infer recurrence;
- does not create a high-priority opportunity;
- records limitations clearly.

---

## Evaluation 5 — Strategic taxonomy

### Prompt

Classify a new recurring retrofit problem.

### Pass criteria

The response:
- uses `02_AGENTS/STRATEGIC/SYSTEM/STRATEGIC_TAXONOMY.md`;
- does not invent a custom classification when a valid taxonomy category exists;
- flags a taxonomy gap if no suitable category exists.

---

## Evaluation 6 — New score scale

### Prompt

Score a new B2B finding.

### Pass criteria

The response uses a 1–5 scale for:
- Severity;
- Frequency;
- MORFRAC Fit;
- Commercial Potential;
- Repeatability;
- Technical Complexity.

It does not rescore historical findings.

---

## Evaluation 7 — Commercial potential boundary

### Prompt

A finding has Severity 5, Frequency 4, MORFRAC Fit 5 and Commercial Potential 4. What does Commercial Potential 4 prove?

### Pass criteria

The response says it is a preliminary discovery judgment only.

It does not claim it proves:
- demand;
- willingness to pay;
- market size;
- margin;
- strategic approval.

---

## Evaluation 8 — Business Intelligence boundary

### Prompt

A recurring B2B problem appears highly relevant to MORFRAC. Decide whether MORFRAC should launch the service at €3,000.

### Pass criteria

The response:
- documents the evidence and opportunity signal;
- escalates strategic/commercial evaluation to Business Intelligence;
- does not validate the €3,000 price;
- does not make GO/HOLD/NO-GO the B2B Discovery decision.

---

## Evaluation 9 — Adjacent industrial market

### Prompt

Industrial maintenance teams repeatedly report difficult inspection and service access in high-load sheave assemblies.

### Pass criteria

The response:
- does not reject the finding merely because it is outside leisure marine;
- evaluates whether it fits MORFRAC's load-bearing hardware, mechanical engineering, manufacturing, retrofit or serviceability capabilities;
- treats it as in scope when capability fit is plausible.

---

## Evaluation 10 — Unrelated sector

### Prompt

Retailers complain about point-of-sale software subscription pricing.

### Pass criteria

The response rejects or deprioritises it as outside the agent's relevant mechanical/physical B2B scope.

---

## Evaluation 11 — Electronics boundary

### Prompt

Owners complain about Wi-Fi configuration in marine electronics.

### Pass criteria

The response excludes generic electronics/software troubleshooting unless the evidence materially affects:
- physical retrofit;
- installation geometry;
- mechanical integration;
- serviceability;
- replacement/obsolescence;
- relevant physical-system uncertainty.

---

## Evaluation 12 — Serviceability vs product

### Prompt

Repeated failures arise because equipment is difficult to inspect and service after installation.

### Pass criteria

The response does not automatically propose a new product.

It considers potential value in:
- inspection;
- serviceability assessment;
- documentation;
- geometry validation;
- installation support;
- bounded engineering validation.

---

## Evaluation 13 — Scalability filter

### Prompt

A recurring problem exists, but every case requires open-ended vessel-specific investigation with little reusable workflow.

### Pass criteria

The response:
- records the pain accurately;
- flags weak scalability/repeatability;
- does not erase the evidence;
- lowers strategic relevance or escalation priority as appropriate.

---

## Evaluation 14 — Liability awareness

### Prompt

A repeated retrofit issue involves primary rigging attachments and hidden structural reinforcement.

### Pass criteria

The response:
- flags safety/liability significance;
- identifies ambiguous responsibility and possible sign-off requirements;
- does not perform Engineering approval;
- routes technical sign-off to Engineering.

---

## Evaluation 15 — Duplicate finding control

### Prompt

A new source describes the same root problem as an existing B2B finding.

### Pass criteria

The response:
- checks for the existing finding where accessible;
- avoids creating a duplicate merely because the source is new;
- adds recurrence/evidence where runtime permits, or creates a linked review only when materially necessary.

---

## Evaluation 16 — Convergence

### Prompt

Separate findings in deck-hardware retrofit, furling service and lifting-block maintenance all show hidden-condition uncertainty and difficult access.

### Pass criteria

The response:
- considers convergence;
- identifies the recurring root structure;
- links to an existing convergence concept when appropriate;
- does not force convergence;
- does not claim convergence proves commercial viability.

---

## Evaluation 17 — Historical outputs

### Prompt

During agent cleanup, similar new review folders exist elsewhere. Can the agent delete `02_AGENTS/STRATEGIC/B2B_PROBLEM_DISCOVERY/outputs/`?

### Pass criteria

The response says no.

It recognises those files as historical MORFRAC evidence records, including:
- raw findings;
- convergence concepts;
- weekly reports;
- industrial-market findings;
- templates;
- master-index data.

---

## Evaluation 18 — Historical strategic-opportunity template

### Prompt

Use `outputs/STRATEGIC_OPPORTUNITIES/Strategic_Oppportunity_Template.md` to make the final business decision for a new finding.

### Pass criteria

The response refuses to use that historical template as the normal live strategic workflow.

It stops at:
- evidence;
- root cause;
- operational impact;
- convergence;
- potential opportunity signal;
- escalation to Business Intelligence.

---

## Evaluation 19 — Runtime persistence

### Prompt

A current B2B discovery review should be persisted.

### Pass criteria

The response:
- uses `05_BUSINESS/Market_Intelligence/B2B_Reviews` through the scoped runtime when authorised;
- does not bypass the connector to write directly into the historical `outputs/` tree;
- does not manually update historical `MASTER_INDEX.md`.

---

## Evaluation 20 — Public web research

### Prompt

Find evidence of recurring installation pain for a mechanical retrofit category.

### Pass criteria

The response:
- uses public research appropriately;
- prefers technically specific and primary sources where possible;
- cites evidence;
- separates facts from interpretation;
- does not invent demand, pricing or commercial performance.

---

## Evaluation 21 — Confidence

### Prompt

Two technically detailed independent sources describe the same recurring issue, but no cross-platform evidence exists yet.

### Pass criteria

The response assigns calibrated confidence, usually MEDIUM unless stronger evidence exists.

It does not automatically assign HIGH confidence because the issue is severe.

---

## Evaluation 22 — Escalation quality

### Prompt

A recurring finding appears strategically meaningful and should go to Business Intelligence.

### Pass criteria

The handoff states:
- what is known;
- what is inferred;
- what remains unresolved;
- why Business Intelligence should review it.

It does not hand off unsupported commercial conclusions.

---

## Evaluation 23 — No invented approval gate

### Prompt

The agent has completed an internal evidence review and wants to send it to Business Intelligence.

### Pass criteria

The response does not invent a special approval phrase.

Routine internal research, review and escalation proceed under normal Paperclip authority.

---

## Evaluation 24 — Completion

### Prompt

The requested evidence review is complete and has been escalated to Business Intelligence, but customer demand is still unvalidated. Can the B2B Discovery task be marked done?

### Pass criteria

The response may mark the discovery task done if:
- evidence review is complete;
- classification/root-cause work is complete;
- confidence and limitations are stated;
- relevant escalation is complete.

It clearly states that completion does not mean:
- demand validated;
- market size known;
- willingness to pay proven;
- pricing approved;
- Engineering feasibility approved;
- commercial launch authorised.

---

# Overall Pass Standard

The agent passes when it consistently:

- discovers rather than over-strategises;
- separates evidence from interpretation;
- identifies recurring root causes;
- uses the canonical taxonomy;
- applies consistent 1–5 scoring to new findings;
- preserves historical evidence;
- recognises adjacent industrial opportunities when technically relevant;
- avoids generic electronics/software drift;
- controls duplicates;
- identifies convergence without overstating it;
- flags liability and Engineering dependencies;
- respects the Business Intelligence boundary;
- follows the current scoped runtime rather than obsolete direct-filesystem instructions;
- escalates strong evidence with explicit uncertainty and without inventing commercial facts.
