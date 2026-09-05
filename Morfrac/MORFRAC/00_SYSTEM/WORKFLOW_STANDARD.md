# WorkflowStandard-v1

This is the authoritative operational standard for Paperclip task flow. It preserves the existing approval, confidentiality, file, release and role-authority rules; where a local guide conflicts with this standard, this standard governs workflow mechanics.

## State and wake discipline

- A task progresses through `todo` / `in_progress` / `in_review` / `done`, or becomes `blocked` only for a concrete dependency, missing material input, failed verified mutation, or required human decision.
- A blocked update names the blocker, accountable owner and one unambiguous next action. Post it once for that state change. Do not poll, repost `no actionable change`, create repeated recovery tasks, or self-wake solely because a task is blocked.
- On a human approval/input blocker, record the approval phrase or requested input, then sleep until a human comment, dependency transition, explicit requeue/manual wake, or a real recovery signal. Completion after an approval requires a fresh run/read-back.
- A productivity or management review is diagnostic and non-blocking by default. It may be an explicit dependency only when a human or the review record names a concrete safety, legal, financial, or delivery gate. Reviews never trigger reviews and do not block their source merely by being open.

## Transaction and recovery discipline

- Every scoped mutation begins with `read_task`. The connector obtains and verifies the same-run checkout as part of the mutation transaction; an explicit `checkout_task` remains permitted to make lock acquisition visible, but is not a fragile prerequisite.
- A mutation must read back its durable result before any later status change. On an uncertain result, stop once, preserve evidence, and create at most one recovery path. A recovery item is an owner-facing diagnostic, not a dependency unless explicitly declared.
- Repeating a run after a verified blocked update is not progress. Requeue only after its named wake condition changes.

## Origin, handoff and project-name semantics

- Server-owned structured origin metadata (`originId`, with matching `parentId` when present) is canonical. A server-created productivity review may use its structured review origin. Normal generated handoffs retain their exact `originating_issue: <UUID>` text contract.
- An ordinary child that lacks both valid structured origin and valid generated text is a system metadata defect. Route it to trusted system repair; do not ask a human to edit hidden IDs or recreate the task solely for metadata.
- Preserve the project name supplied by the user in task payloads and filesystem operations. Canonicalisation is comparison-only: unescape Markdown separators and compare whitespace, underscore and hyphen forms as one normalized slug. Never silently rename a project or ask the user to re-enter an equivalent spelling.

## Intake and approval

- A normal user request authorises reasonable internal read-only discovery and routine internal delegation inside the assigned role policy. Ask only for a materially outcome-changing choice or a separately governed action.
- New projects and multi-package changes require a frozen brief and explicit approval before dispatch. A plan or review is not approval. Do not start Phase 1 from a review/brief without its exact approval gate.
- Issue creation, origin relation and audit record must be treated as one idempotent operation. Use the platform's structured origin fields rather than duplicate free-text metadata when they are present.

## Diagnostics

- Report structured reasons for waits, denials and retries: `reasonCode`, task/issue identifier, triggering event, owner and next action. Never expose raw guard payloads or internal encoded records in user-facing comments.
