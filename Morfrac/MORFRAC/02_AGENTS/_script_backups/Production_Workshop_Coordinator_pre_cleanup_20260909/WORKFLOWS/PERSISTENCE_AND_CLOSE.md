# Persistence and close

Draft in Paperclip. Before any future file write, resolve the permitted naming/destination policy and exact existing project path. Use an action-specific Workshop save approval only where the current connector technically requires it. If no permitted destination exists, set `STORAGE_POLICY_REQUIRED`; do not make directories or modify other rules.

Never edit ERP/MES/stock/timesheet/maintenance/quality records or close their orders. Keep original evidence and superseded versions under the approved retention policy; do not delete or overwrite adverse records.

Close a coordination record only when its stated deliverable, dependencies, unresolved risks and human approval are documented. If workshop work is incomplete, say so even when the assigned status-review issue is done. Use `TEMPLATES/STATUS_AND_CLOSEOUT.md`.
