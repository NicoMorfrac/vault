# Workflow - QA, Save and Release

## QA

- Verify parties, capacity, document/version, authoritative language, law/forum candidates and transaction facts.
- Confirm official sources and access dates; distinguish applicability from existence.
- Check definitions, clause numbering, cross-references, exhibits, precedence and signature blocks.
- Ensure every new clause is visibly unapproved and every material deviation has an owner.
- Confirm high-risk/urgent matters have required counsel escalation.
- Separate clean counterparty draft from internal advice/issues.
- Remove unnecessary personal data, signatures, credentials and unrelated confidential data.
- Confirm no previous/executed version will be overwritten.

## Save

Require the current plan and exact `APPROVE LEGAL SAVE <Matter-ID> <Version>`. Save only listed files, verify hashes/content, and set `SAVED_DRAFT_NOT_APPROVED`.

## Release

Require resolved reviews, verified final files, signature-authority status, named human sender/channel, current plan, and exact `APPROVE LEGAL RELEASE <Matter-ID> <Version>`. Set `HUMAN_RELEASE_READY` and hand off. Do not sign, send, file, upload, submit, negotiate, accept, terminate, renew, or vary.

