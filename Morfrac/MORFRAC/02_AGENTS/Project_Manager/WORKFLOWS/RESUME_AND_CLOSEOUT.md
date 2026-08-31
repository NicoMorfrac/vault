# Workflow - Resume and Closeout

Run only after project creation or existing-project verification succeeds.

This is the `create_project` closeout only. For `prepare_proposals`, use the `PROPOSAL_STORAGE_READY` notification in `PREPARE_PROPOSALS.md`; never emit ENGINEERING_RESUME or claim a proposal is complete from a storage task.

## Procedure

Runtime mapping: use `notify_origin` for the deterministic current-task and originating-issue receipt, then `post_update` for a substantive verified closeout. No shell/helper API invocation is permitted. The connector blocks operational `done` until structure readiness and originating notification evidence are present. If the origin is closed/unavailable, report blocked for human review; do not change it or claim successful notification.

1. Post this exact status record in the PM_TASK issue:

```text
ENGINEERING_RESUME:
project_name: <Project_Name>
status: project_ready
```

2. If the originating issue UUID is valid, post:

`Project <Project_Name> created and ready for analysis.`

3. Close the PM_TASK issue as done with:

`Project structure verified and ready.`

4. Report:
   - project name and path;
   - `READY` or `ALREADY_EXISTS`;
   - verified folders/files;
   - originating issue notification status;
   - PM_TASK closeout status.

## Rules

- Use only the scoped connector; legacy `paperclip_helper.py` is not available in this runtime.
- Use `PAPERCLIP_API_URL`, the injected short-lived key, and current run ID.
- Never display credentials.
- If any notification/update fails, report the exact error and stop. Do not claim full completion.
