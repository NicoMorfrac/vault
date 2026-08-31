# Workflow - Release Handoff

## Preconditions

- Saved proposal version is immutable and verified.
- Technical, schedule, commercial, price, and legal review requirements are satisfied.
- No unresolved client-visible placeholder remains.
- Current release plan identifies proposal/version, outputs, approved references, human sender and channel.
- Matching global `ProposalWorkflow-v1` rules permit the issue-only human handoff.
- A later direct authorised human/board comment in the assigned issue exactly matches `APPROVE PROPOSAL RELEASE <Proposal_ID> <Version>` after the unchanged release plan.

## Procedure

1. Revalidate every approval, source revision, saved file hash, audience, intended sender and plan. Reject ambiguous/embedded/stale/agent-authored/cross-issue approvals.
2. Complete `../TEMPLATES/RELEASE_MANIFEST.md` and the final human checklist in the assigned Paperclip issue only. Include source/review/save/release approval references, verified hashes, and the exact client-safe file versus internal-only material.
3. Mark the issue-based package `HUMAN_RELEASE_READY`; do not change saved file contents, frontmatter, names, DRAFT markings or project index.
4. Hand off only to the named authorised human sender, clearly separating client-safe documents and internal-only evidence. No automatic external transmission.

Do not email, upload, submit, sign, publish, negotiate, or accept. If any source changes after release approval, invalidate the approval and return to review.

This approval creates no additional vault file, release copy, PDF/Word export or metadata sidecar. Any newly requested artifact needs its own separately authorised workflow; a release approval does not substitute for save approval.
