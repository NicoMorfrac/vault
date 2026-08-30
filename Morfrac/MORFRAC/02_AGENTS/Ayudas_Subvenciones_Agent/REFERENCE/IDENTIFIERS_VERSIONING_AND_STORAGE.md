# Identifiers, Versioning and Storage

## Identifiers

Use an approved unique `Opportunity-ID` and `Application-Version`. Link but do not substitute:

- official call/BDNS/topic/programme IDs;
- Paperclip issue/project IDs;
- company/project baseline versions;
- portal draft/application/receipt/award/claim/audit IDs;
- cost/aid/partner/declaration records.

## Lifecycle labels

- `OPPORTUNITY_IDENTIFIED_UNVERIFIED`: discovery only.
- `DRAFT - NOT SUBMITTED` and `ELIGIBILITY NOT CONFIRMED`: working application.
- `SAVED_NOT_SUBMITTED`: approved persistence only.
- `HUMAN_SUBMISSION_READY`: reviewed pack awaiting human portal action.
- `SUBMITTED_BY_HUMAN - RECEIPT REQUIRED`: action reported without authoritative receipt.
- `AWARD NOT ACCEPTED`: award/conditions under human review.
- `AWARD_OBLIGATIONS_OPEN`: accepted/active only after human evidence.
- `CLOSED_RECONCILED`: final evidence and exact close gate; retention continues.

## Proposed repository

After `APPROVE FUNDING MASTER <Issue-ID>`:

```text
05_BUSINESS/Public_Funding/
  00_Company_Funding_Master/
  01_Opportunity_Register/
  02_Applications_Open/
  03_Awards_Active/
  04_Justification_Audits_and_Claims/
  05_Closed/
```

Do not create this structure because it appears here. Preserve official source/application versions and hashes; corrections create a new linked version and never rewrite submitted history.
