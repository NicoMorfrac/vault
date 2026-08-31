# Revision and Status Control

Use a stable proposal ID such as `PROP-YYYY-NNN` and monotonic versions `v01`, `v02`, and so on.

Never overwrite a prior version. Record:

- baseline version;
- reason/requester;
- changed sources;
- affected sections;
- required re-reviews;
- save approval;
- release approval;
- superseded/current status.

Only these new approved filenames are used in the existing optional proposal area:

- `06_Proposals/Client_Drafts/<Proposal_ID>_<Version>_DRAFT.md`
- `06_Proposals/Internal_Review/<Proposal_ID>_<Version>_INTERNAL.md`

Keep the same proposal ID/version on the client/internal pair. Do not add a client short name or reuse a conflicting prior filename. Any content, metadata, filename, ID, version or path change requires a new exact save plan and approval. A collision never authorises an automatic version bump. Prior files remain immutable; current/superseded/readiness state and the later save/release approval references are recorded in Paperclip, not by rewriting older files.

Only an authorised human process may remove `DRAFT` or transmit the file.
