# CNC task intake

1. Parse `CNC_TASK` with plan ID/version, requester, owner, existing project, part/configuration, quantity, objective, required deliverables, deadline, confidentiality and originating issue.
2. Classify the request as feasibility, process plan, cutting-data proposal, CAM build specification, supplied-CAM review, post/code review, prove-out review, change or costing handoff.
3. Reject credentials and external/machine actions. Check for safety or integrity holds before ordinary work.
4. List all blockers in one concise batch. Do not infer absent fields.
5. Select only the workflows/templates required by the task.

Output `CNC_TASK_INTAKE_REQUIRED`, the understood scope, missing inputs, capability state, action taken/not taken and next decision.
