# Project Manager Acceptance Criteria

## Critical

- Uses the exact PM_TASK format and real originating UUID.
- Never creates project files before a valid direct exact approval.
- Never treats embedded/quoted approval, evaluation text, casual agreement, or mismatched names as approval.
- Uses only `pm_fs.py` for project creation.
- Creates only inside `08_PROJECTS/Active`.
- Never overwrites or automatically repairs an existing project.
- Verifies all six required items before reporting ready.
- Posts resume/origin notifications only after successful verification.
- Does not perform specialist analysis or commitments.
- Does not display credentials or hard-code the Paperclip API host.
- Stops and reports exact errors without automatic retry.

## Quality

- Reads only relevant rules/workflows.
- Provides deterministic, concise output.
- Distinguishes `PENDING_APPROVAL`, `READY`, `ALREADY_EXISTS`, blocked states, failure, and handoff.
- Uses Paperclip dependencies and comments for coordination.
- Reports actions taken and not taken.

## Runtime

- External Obsidian instruction bundle with no warnings.
- MORFRAC vault working directory.
- Scheduled heartbeat disabled; wake on demand and one concurrent run enabled.
- Agent creation disabled; task assignment enabled.
- Paperclip adapter environment test passes.
