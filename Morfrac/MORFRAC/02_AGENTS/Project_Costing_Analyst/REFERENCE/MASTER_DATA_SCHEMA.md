# Costing Master Data Schema

## Shared fields

- record_id: stable human-readable code;
- record_type;
- status: candidate / approved / future / active / superseded / expired / rejected;
- revision;
- value and unit;
- currency and tax basis where applicable;
- scope, geography, customer/channel, quantity band, and applicability;
- source classification and source reference;
- source owner and approval owner;
- source date, approved date, effective from, effective to/expiry;
- authoritative system and system record ID;
- last verified/sync timestamp;
- confidentiality;
- assumptions/exclusions;
- change reason and supersedes reference;
- Paperclip issue/comment approval reference.

## Costing parameter fields

- parameter code/category;
- role/resource/process;
- rate type: payroll, burdened cost, transfer, bill, allocation, policy;
- calculation base and included burdens;
- frequency/review date.

Do not store payroll-person data. Use role/resource class and approved aggregate rates.

## MORFRAC price-list fields

- product/service code and description;
- unit and quantity band;
- list/base price;
- currency, tax basis, geography/channel/customer class;
- inclusions/exclusions;
- validity/effective dates;
- related Odoo product/pricelist ID when supplied.

## Discount-policy fields

- rule code;
- eligible product/service/customer/channel/quantity;
- discount type and value;
- stackable yes/no and precedence;
- maximum authority/required approver;
- minimum price or margin guardrail reference;
- exclusions and validity.

Never store an unrestricted discount without an approver and guardrail.

## Supplier fields

- supplier code and legal/trading name;
- country and business contact channel only when necessary;
- approved/candidate status and capability;
- currency/payment/delivery/incoterm basis when supplied;
- quality/NDA/compliance references, not unsupported certifications;
- quote/price record ID, part/service/scope, quantity/MOQ, tooling/NRE, lead time, validity, tax, freight/duty, evidence path, and exclusions;
- performance notes supported by approved records.

Supplier quotes are append-only dated commercial records, not a single overwritten current price.
