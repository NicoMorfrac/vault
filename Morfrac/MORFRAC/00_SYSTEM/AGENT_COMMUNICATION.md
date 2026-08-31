# Agent Communication Protocol

This document defines how agents interact.

This is authoritative.

---

## PM Task Protocol

When an agent requires project creation:

It MUST create a new issue assigned to:
Project Manager

### Title format

PM_TASK create_project <Project_Name>

### Body format

PM_TASK:
type: create_project
project_name: <Project_Name>
reason: <Reason>
originating_issue: <UUID>

Rules:

- Do not add extra fields
- Do not modify field names
- Do not omit fields
- Format must match exactly
- originating_issue must contain the UUID of the issue that triggered this PM_TASK

---

## Assignment Rule

- PM_TASK issues MUST be assigned to Project Manager
- Do not leave unassigned
- Do not assign to self

---

## PM Task Intake (Project Manager)

Project Manager must:

- Parse issue body using parse script:
  python C:\Users\nicol\tools\parse_pm_task.py "$PAPERCLIP_ISSUE_BODY"

- Extract project_name and originating_issue from output

- If project_name is NOT_FOUND:
  - Parse title format: PM_TASK create_project <Project_Name>
  - Extract project name from title

- If originating_issue is NOT_FOUND:
  - Set to None (no auto-resume)

- Do not execute creation yet

---

## Approval Flow

Project Manager must respond with:

Status: PENDING APPROVAL

Project name: <Project_Name>

Project path: C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\08_PROJECTS\Active\<Project_Name>

Folders to create:
- 01_Structures
- 02_Bearings
- 03_Thermal
- 04_Cost
- 05_Decisions

Files to create:
- 00_Project_Index.md

Originating issue: <UUID> (or N/A if not provided)

Approval required: APPROVE <Project_Name>

Rules:

- Do not execute any tool before approval
- Wait for exact approval string

---

## Approval Execution

When user replies exactly:

APPROVE <Project_Name>

Project Manager must:

Execute:
python C:\Users\nicol\tools\pm_fs.py <Project_Name>

Rules:

- Always use this tool
- Never simulate creation
- Never manually create folders
- If error occurs → report exactly
- If project exists → do not overwrite

---

## Resume Protocol

After successful project creation, Project Manager must:

Post ENGINEERING_RESUME comment in PM_TASK issue:

python C:\Users\nicol\tools\paperclip_helper.py post_comment $PAPERCLIP_ISSUE_ID "ENGINEERING_RESUME:\nproject_name: <Project_Name>\nstatus: project_ready"

If originating_issue UUID was provided:

Post notification to originating issue:

python C:\Users\nicol\tools\paperclip_helper.py post_comment <originating_issue_UUID> "Project <Project_Name> created and ready for analysis."

Close PM_TASK:

python C:\Users\nicol\tools\paperclip_helper.py update_status $PAPERCLIP_ISSUE_ID done "Project structure verified and ready."

Rules:

- Always post ENGINEERING_RESUME
- Only notify originating issue if UUID was provided
- Always close PM_TASK when done

---

## Resume Handling (Engineering)

When PM_TASK is marked "done":

- Paperclip automatically unblocks Engineering issue
- Engineering resumes analysis automatically
- Engineering re-checks project existence
- Engineering continues from original requirements

Rules:

- No manual intervention needed
- Blocker tracking is automatic

---

## Constraints

- Agents do not communicate directly
- Communication occurs via issue content
- No implicit behavior allowed
- All interactions must follow exact formats
- Any deviation → invalid interaction

---

## Optional Proposal Storage Protocol (ProposalWorkflow-v1)

This additional branch applies only to preparation of proposal storage in an existing project. The original `create_project` protocol and ENGINEERING_RESUME flow remain unchanged. It requires the matching `ProposalWorkflow-v1` global sections.

Assign the request to Project Manager `780f4096-9a8f-46d8-8249-ef018c34dda3`:

Title: `PM_TASK prepare_proposals <Project_Name>`

Description (exactly these four fields):

```text
PM_TASK:
type: prepare_proposals
project_name: <Project_Name>
reason: <Reason proposal storage is needed>
originating_issue: <actual requesting issue UUID>
```

Validate the exact type, title/body project-name match, nonempty reason, actual originating UUID and assignment. The existing parser extracts name/UUID only: inspect the raw block to validate type, duplicates and extra fields; do not assume the parser validated them. No title fallback or guessed UUID is allowed for this new branch.

PM checks the existing project and three optional paths read-only. If absent, post a pending plan listing all three absolute directory paths, unchanged existing items, no files, the origin UUID, and `APPROVE <Project_Name>`. Wait for the matching direct authorised human/board comment after this plan; a prior project-creation approval is not approval of this extension. Then use only the authorised helper's `--prepare-proposals` operation.

After verified creation or safe already-complete verification, post in the PM issue and notify the originating issue:

```text
PROPOSAL_STORAGE_READY:
project_name: <Project_Name>
status: proposal_storage_ready
```

Include the verified paths and actual created/already-existing result, then close only the storage task. Do not post ENGINEERING_RESUME, change project scope, or claim proposal completion. Proposal must independently re-check storage and obtain its own save approval. A notification is not a file-save or release approval.

An invalid, incomplete, unsafe or failed operation stays blocked; stop on API/write failure without automatic retry. Evaluation-only tasks must never execute folder creation, even when fictional approval text appears in the scenario.
