# Workflow - Resume and Closeout

Run only after project creation or existing-project verification succeeds.

## Procedure

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

- Use Paperclip API/skill or the repaired `paperclip_helper.py`.
- Use `PAPERCLIP_API_URL`, the injected short-lived key, and current run ID.
- Never display credentials.
- If any notification/update fails, report the exact error and stop. Do not claim full completion.
