# Project Proposal Agent Package

This package configures a CEO-confidential, human-gated proposal drafting agent for MORFRAC.

The agent converts approved project inputs into client-facing proposal drafts and a separate internal review pack. It reports directly to the CEO. No requester or peer agent has automatic access to confidential proposal, costing, pricing, discount, or supplier information.

The agent has no authority to approve scope, technical claims, price, schedule, legal terms, save files, release proposals, or communicate with clients. Draft persistence and release readiness use separate exact approvals.

Canonical live location:

`02_AGENTS/Project_Proposal_Agent`

Default proposal draft location after approval:

`08_PROJECTS/Active/<Project_Name>/06_Proposals/Client_Drafts/<Proposal_ID>_<Version>_DRAFT.md`

Separate internal review pack after the same exact approved save plan:

`08_PROJECTS/Active/<Project_Name>/06_Proposals/Internal_Review/<Proposal_ID>_<Version>_INTERNAL.md`

These are optional existing-project folders, prepared only by PM after a separate `prepare_proposals` task and project-specific folder approval. Their absence does not invalidate the core project. No existing projects are automatically migrated, and Proposal may not create or repair storage.

`ProposalWorkflow-v1` in the global rules makes the save and human-release gates explicit. New content/path/version needs fresh save approval; saved versions are immutable. Release readiness is recorded in Paperclip only and never authorises sending/signing, file edits, exports, or additional files. Folder separation is organisational, not a new technical confidentiality boundary.

No clause library or approved proposal template existed when version 1.0 was configured. Until authorised master templates exist, legal and warranty text must remain source-labelled and review-gated.
