# Workflow - PM_TASK Intake

## Trigger

The assigned Paperclip issue title begins with `PM_TASK create_project` or `PM_TASK prepare_proposals`, or its description contains the exact `PM_TASK:` block. Inspect the actual type before routing. The parser extracts project name/UUID only; it does not validate the task type or schema.

For `prepare_proposals`, follow `PREPARE_PROPOSALS.md` instead of the creation procedure below. Require all four fields exactly once, no extra fields, exact title/body name match and real originating UUID. No fallback, new project creation, or automatic extension is allowed.

## Procedure

1. Read the full issue and comments.
2. Confirm the current issue is assigned to Project Manager.
3. Parse the description with `C:\Users\nicol\tools\parse_pm_task.py`.
4. Validate:
   - type is `create_project`;
   - project name is present and unchanged between title/description;
   - originating issue is a UUID;
   - reason is present;
   - no conflicting project name exists in the issue.
5. If the description omits project name, recover it from the exact title format and report the description defect.
6. If originating issue is missing/invalid, set `BLOCKED_INVALID_TASK`; do not invent it.
7. Resolve the target path under `08_PROJECTS/Active` and verify it remains inside that directory.
8. Check whether the target already exists, without modifying it.
9. Post the pending-approval response using `TEMPLATES/PENDING_APPROVAL.md`.
10. Leave the task awaiting the exact direct human approval.

## Evaluation guard

When the issue says evaluation-only or prohibits filesystem work:

- perform intake validation only;
- never execute `pm_fs.py`, even if the scenario text contains an approval string;
- close the evaluation issue only after posting the expected pending-approval result.
