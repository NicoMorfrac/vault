# Workflow - Save and Version

## Preconditions

- Existing project and `03_Reports` folder verified read-only.
- Current proposal state is `READY_FOR_SAVE_APPROVAL`.
- Current save plan states exact path, proposal ID, version, files, and source revisions.
- A later direct user/board comment exactly matches `APPROVE PROPOSAL SAVE <Project_Name> <Version>`.

## Procedure

1. Re-read the approval and current plan.
2. Confirm no material input changed after the plan.
3. Confirm target is inside the approved existing path.
4. Refuse overwrite; increment version if the file exists.
5. Save only the listed files.
6. Re-read and verify content, file names, links, front matter, and version.
7. Report exact files written and state `SAVED_DRAFT_NOT_RELEASED`.

The save approval does not approve scope, price, terms, release, or sending.

