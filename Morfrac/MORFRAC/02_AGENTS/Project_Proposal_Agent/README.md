# Project Proposal Agent Package

This package configures a CEO-confidential, human-gated proposal drafting agent for MORFRAC.

The agent converts approved project inputs into client-facing proposal drafts and a separate internal review pack. It reports directly to the CEO. No requester or peer agent has automatic access to confidential proposal, costing, pricing, discount, or supplier information.

The agent has no authority to approve scope, technical claims, price, schedule, legal terms, save files, release proposals, or communicate with clients. Draft persistence and release readiness use separate exact approvals.

Canonical live location:

`02_AGENTS/Project_Proposal_Agent`

Default proposal draft location after approval:

`08_PROJECTS/Active/<Project_Name>/03_Reports/<Proposal_ID>_<Version>_DRAFT.md`

No clause library or approved proposal template existed when version 1.0 was configured. Until authorised master templates exist, legal and warranty text must remain source-labelled and review-gated.
