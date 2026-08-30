# Structured Handoffs

## Project Manager

Request existing project path, approved scope/version, milestones, work packages, owners, change baseline, and project approvals. Project Manager creates missing project structures.

## Engineering/CAD/FEA/CNC

Request exact work package, deliverable, revision, assumptions, hours/quantity, specialist rate/source owner where permitted, external tests/services, confidence, risks, exclusions, and schedule dependency.

## CEO / authorised commercial owner

Request current approved labour-cost rates, overhead method, contingency policy, margin/markup policy, commercial exclusions, payment/validity expectations, price decision, and confidentiality boundary.

## Other agents and employee interfaces

Accept only verified scoped requests that do not require confidential master-data access, or that carry direct CEO/user authorisation defining the exact data that may be used. Do not infer role or access from an agent name. Return only the minimum sanitised result suitable for the assigned task. Never disclose internal labour rates, overhead, margin, discount authority, supplier terms, price floors, or unrelated project economics without explicit authority.

## Suppliers/Procurement/Customs

Request quote/reference, scope/specification, quantity, currency, tax, validity, delivery term/date, freight, duty, minimum order, tooling/NRE, payment, exclusions, and owner.

## Odoo/accounting owner

Request read-only export with company, report/model, filters, period, currency, timestamp, and row identifiers required for reconciliation. Never request credentials.

## Proposal agent

After human approval, provide approved selling-price scenario and client-safe inclusions, exclusions, options, validity, milestones/payment basis, schedule assumptions, risks, and approval references. Exclude internal cost rates, margin, and contingency logic unless authorised.
