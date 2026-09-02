# Fusion 360 capability and limitations

## Verified locally on 2026-09-02

- Fusion 2704.1.53 launched from the current user's Autodesk webdeploy production directory.
- MORFRAC Fusion Bridge 0.2.4 installed as a startup add-in.
- Custom-event main-thread execution, fixed queue, heartbeat, validation, no-overwrite behavior, failure receipts, native F3D/STEP/DXF export and preview capture exercised.
- Paperclip exposes only four Drafting tools: status, frozen reference plan, approval-bound one-shot queue and verified receipt.

## Supported integration route

The installed add-in watches only the fixed MORFRAC queue. Its worker thread never calls Fusion APIs; it fires a custom event so modelling executes on Fusion's main thread. Jobs cannot provide code or paths and are limited to the allowlisted operation. Existing outputs are never overwritten.

Official references:

- https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-9701BBA7-EC0E-4016-A9C8-964AA4838954
- https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/Scripts.htm
- https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/WritingDebugging_UM.htm

## 2D limitation

Autodesk's `DrawingManager.createDrawing` API was introduced in July 2026 as preview functionality. Do not rely on it for released production automation. Use supervised Fusion drawing creation and human verification until the exact API path is released and MORFRAC validates it.

Reference: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/DrawingManager_createDrawing.htm

## Current boundary

`create_reference_bracket_v1` is the only operational geometry schema. It produces an internal reference F3D, STEP, top/front DXF profiles and preview. It is not a generic drawing-to-3D engine. Any different part family requires a new narrowly defined operation, validation tests and smoke-test evidence before it can be queued.

Always require a fresh bridge heartbeat and exact output-hash receipt. Automated production drawings, cloud save, master modification, CAM, FEA, manufacturing release and external handoff are unavailable through this connector.
