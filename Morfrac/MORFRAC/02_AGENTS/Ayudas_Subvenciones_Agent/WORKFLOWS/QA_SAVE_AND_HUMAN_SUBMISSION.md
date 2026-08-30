# Workflow - QA, Save and Human Submission

## QA

Reconcile call/version/deadline, applicant/entity/group, project/version/start date, work packages/milestones, budget/cost totals, aid request, co-finance, partners, other funding, eligibility/compliance decisions, declarations and attachment manifest. Verify every character/page/file constraint and cross-form total.

## Save

Show exact files/paths/source manifest/hashes/review states and require `APPROVE FUNDING FILE SAVE <Opportunity-ID> <Version>`. Save only listed versioned files, verify them and set `SAVED_NOT_SUBMITTED`.

## Submission readiness

Require exact application/version/hash/portal/deadline/timezone/representative, all accountable reviews and `APPROVE FUNDING SUBMISSION <Opportunity-ID> <Application-Version>`. Mark only `HUMAN_SUBMISSION_READY` and hand off. Do not access the portal, upload, sign, submit or communicate.

After human action require official receipt, timestamp, application/reference ID, exact submitted version and status. “Sent” without receipt remains `SUBMITTED_BY_HUMAN_EVIDENCE_REQUIRED`.
