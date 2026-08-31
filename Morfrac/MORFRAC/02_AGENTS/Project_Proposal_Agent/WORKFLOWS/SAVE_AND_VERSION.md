# Workflow - Save and Version

## Preconditions

- Matching global `ProposalWorkflow-v1` sections read and consistent.
- Existing complete project and `06_Proposals/Client_Drafts` plus `06_Proposals/Internal_Review` verified read-only, with safe real paths. Missing/partial/unsafe storage is `PROPOSAL_STORAGE_REQUIRED`; follow `../REFERENCE/HANDOFFS.md`, never create/repair or substitute a folder.
- Current proposal state is `READY_FOR_SAVE_APPROVAL`.
- Current save plan states the exact project, one proposal ID/version, both intended paths or the explicit supported subset, complete frozen content previews/fingerprints (including metadata), source revisions, audiences and reviews. No unresolved client-sensitive values may be silently filled.
- A later direct authorised human/board comment in this assigned issue exactly matches `APPROVE PROPOSAL SAVE <Project_Name> <Version>`.

## Procedure

1. Re-read the exact current plan, approval comment, author authority, assignment and source evidence. Reject casual/quoted/embedded/stale/agent/cross-issue approval or a different project/version.
2. Re-check all paths and contents before writing. Any content, metadata, source, name, path, ID, version or relevant destination-state change requires a new plan and fresh approval; do not proceed partially from the old plan.
3. Use only `Client_Drafts/<Proposal_ID>_<Version>_DRAFT.md` and `Internal_Review/<Proposal_ID>_<Version>_INTERNAL.md` under the existing approved `06_Proposals` area. Enforce real-path containment; refuse unsafe links/junctions or unavailable access. Do not weaken permissions.
4. If any target exists, do not overwrite or automatically increment the version. A complete identical save already verified against this same issue/plan may be reported as already saved with its audit reference. Otherwise stop, propose the next version and obtain fresh approval. A partial or uncertain earlier write remains blocked without retry, cleanup, or repair.
5. Create only the listed new files, exclusively, using the exact frozen content. Preserve other files, prior versions, original sources and project index. Follow report frontmatter/Related Links rules. Never include internal costs, margins, supplier terms, internal links or private review notes in a client draft.
6. Re-read every saved file; verify hashes/content, paths, names, metadata, audience and version. On a failure, report exact written/unwritten items and stop without retry or claiming complete save.
7. Record the current save approval comment, exact paths/hashes and outcome in the assigned Paperclip issue. Do not alter the frozen internal pack to insert the later save approval ID. Report `SAVED_DRAFT_NOT_RELEASED` only after all listed files are verified.

The save approval does not approve scope, price, terms, release, or sending.
