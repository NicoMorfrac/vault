# Workflow - QA, Validation, Save and Release

## QA and validation

- Verify document/product/configuration identity, revision, applicability and source set.
- Confirm intended use, users, markets/languages and lifecycle coverage.
- Confirm technical values, procedures, figures, warnings, intervals, parts and claims trace to approved sources.
- Confirm risk-assessment alignment and no warning/control omission.
- Confirm compliance and warranty sections use approved references and contain no unsupported declaration.
- Confirm translation and terminology review.
- Perform task walkthrough/readability review with representative competent users when required.
- Check numbering, tables, links, figures, callouts, units, typography, front matter and related links.
- Confirm draft/internal comments are not in the user-facing output.

## Save

Require the current plan and exact `APPROVE DOCUMENTATION SAVE <Document-ID> <Version>`. Save only listed files, preserve history, verify content/hashes and set `SAVED_DRAFT_NOT_RELEASED`.

## Release

Require all listed technical/safety/compliance/Legal/translation/quality reviews, exact files/hashes and `APPROVE DOCUMENTATION RELEASE <Document-ID> <Version>`. Set `HUMAN_RELEASE_READY` and hand off to the named human. Never publish, supply, upload, email, print for distribution, sign, declare conformity or notify externally.

