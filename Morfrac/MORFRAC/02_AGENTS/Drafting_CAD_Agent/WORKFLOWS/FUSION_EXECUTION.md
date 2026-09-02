# Fusion execution workflow

1. Call `fusion_status`; stop at `FUSION_BRIDGE_NOT_READY` unless the heartbeat is current.
2. Confirm the source is an assigned PDF/image attachment and read it before modelling.
3. Confirm that `create_reference_bracket_v1` matches the geometry family. Do not force unrelated geometry into it.
4. Separate source dimensions from visual assumptions. Use millimetres explicitly and list all assumptions together.
5. Call `plan_fusion_reference` with the source attachment, exact revision, parameters, assumptions and new output basename.
6. Present only the concise plan and `APPROVE CAD REFERENCE BUILD <Issue-ID> <Version>`.
7. After the exact later direct-human approval, call `execute_fusion_reference` once. Never retry an uncertain or failed attempt.
8. Poll with `fusion_receipt`; do not infer success from a queued state.
9. Verify receipt status, source hash, body/feature/parameter counts and every output hash. Review the preview against the source drawing.
10. Report the result as `REFERENCE ONLY / UNVERIFIED / NOT FOR MANUFACTURE`; preserve failure receipts and use a new revision for corrections.

The bridge creates new F3D, STEP and reference DXF/preview files only. It does not modify a project master or create a production drawing.
