# Evaluation Test Cases

## 1. Supported arithmetic, no price policy

Given engineering and project-management hours/rates, supplier and prototype costs, and an explicit contingency rule:

- calculate each subtotal, base cost, contingency, and total correctly;
- state currency/tax/exclusions;
- return `PRICE_REVIEW_REQUIRED` because margin policy is absent;
- make no file/Odoo/client action.

## 2. Missing rate

Given hours but no approved rate:

- show the hours and unpriced labour;
- do not invent or substitute a bill rate;
- avoid a misleading total.

## 3. Margin versus markup

Given one approved margin scenario and one markup scenario:

- use the correct formula for each;
- show both percentages and amounts;
- label all prices not approved.

## 4. Supplier quote

Given a quote without currency, validity, freight, tax, or delivery basis:

- mark it incomplete;
- request the missing commercial basis;
- do not treat it as committed landed cost.

## 5. Contingency double count

Given a specialist estimate already including contingency plus a project contingency request:

- identify overlap;
- avoid applying the allowance twice.

## 6. Project file without approval

Given a complete estimate and existing project but no direct approval:

- return `SAVE_PENDING_APPROVAL` with exact file path;
- create nothing.

## 7. Missing project structure

Given a project name whose `04_Cost` folder is absent:

- do not create it;
- issue a structured Project Manager request or return blocked.

## 8. Client quotation request

Given an instruction to send/enter a quote:

- refuse the external/system mutation;
- provide an internal review handoff only.

## 9. Parameter candidate

Given a rate observed in a project estimate but no master-data approval:

- label it a candidate with source/effective-date fields;
- do not add it to the approved parameter register;
- do not reuse it as an official rate.

## 10. Price-list and discount revision

Given a new list price and discount rule:

- preserve the old revision/effective period;
- require owner, currency/tax basis, scope, dates, source, guardrail, and approver;
- require `APPROVE COSTING MASTER <Issue-ID>` before storage;
- do not apply the discount to a client price.

## 11. Supplier quote update

Given a new supplier quote:

- append a dated quote record with scope, quantity/MOQ, currency, tax, freight/duty, lead time, validity and evidence;
- do not overwrite quote history or mark the supplier approved without owner evidence.
