# Workflow - Save and Handoff

## Save plan

Before any vault write, post:

- state: `SAVE_PENDING_APPROVAL`;
- Paperclip issue identifier;
- exact target directory;
- every filename;
- whether each item is new or an update;
- asset type and language;
- action not authorised: publication/live deployment;
- approval required: `APPROVE CONTENT <Issue-ID>`.

## Approval validation

The approval must be a direct human/board comment after the current plan and match the issue identifier exactly. Reject quoted, embedded, stale, altered, agent-authored, or evaluation approval strings.

## Save procedure

1. Re-read the issue and approval comment.
2. Revalidate the target is inside the MORFRAC vault and the intended marketing area.
3. Read `FILE_RULES.md`; for an internal report also read `OBSIDIAN_REPORT_STANDARD.md`.
4. Check every target for conflicts.
5. If a different-issue file exists, stop; do not overwrite.
6. Create only the listed Markdown content.
7. Verify every file exists and record its exact path.
8. Post `SAVED_FOR_REVIEW` with evidence status and review owners.
9. Notify the originating issue when valid.

## Content-asset frontmatter

```yaml
---
type: content_asset
source_agent: Blog_Website_Content_Creator
created: YYYY-MM-DD
paperclip_issue: MORAAAAA-000
asset_status: draft_for_human_review
language: en
related_projects: []
related_topics: []
---
```

## Publication boundary

Saving a review draft is not publication approval. Never report the asset as live, uploaded, scheduled, indexed, or published.
