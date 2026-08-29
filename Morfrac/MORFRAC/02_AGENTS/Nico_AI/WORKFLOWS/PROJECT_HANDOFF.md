# Workflow - Project Handoff

## Preconditions

- The project brief revision is approved.
- The receiving owner exists and is active.
- Required input records are accessible.
- Blocking safety, legal, commercial, and schedule questions are resolved or explicitly owned.

## Handoff content

Create the receiving Paperclip issue using `TEMPLATES/HANDOFF_PACKAGE.md` and include:

- originating issue UUID;
- approved brief revision;
- project name;
- objective and decision/deliverable requested;
- supplied inputs and exact source paths/links;
- scope, exclusions, acceptance criteria, and approver;
- assumptions, unknowns, contradictions, risks, and constraints;
- due date and dependencies;
- output location/format where already controlled;
- callback instruction to the originating issue.

## Rules

- Use Paperclip issues and comments; do not rely on unrecorded direct communication.
- Create one accountable handoff per deliverable or tightly coupled work package.
- Do not duplicate a live specialist issue for the same objective and baseline.
- Delegation is not completion. Report `HANDED_OFF` until the result is accepted.
- If assignment fails, report the exact error and stop without automatic retry.
