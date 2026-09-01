# Fusion 360 capability and limitations

## Verified locally on 2026-09-01

- `Fusion360.exe` detected under the current user's Autodesk webdeploy production directory.
- Fusion 360 process observed running.
- No MORFRAC Paperclip-to-Fusion execution connector was detected or validated.

## Supported integration route

Autodesk supports Python add-ins/scripts through Fusion's API. On Windows, Fusion automatically searches `%APPDATA%\Autodesk\Autodesk Fusion\API\AddIns` and `...\Scripts`. A MORFRAC read-only probe can confirm the in-process API and active context without editing a design.

Official references:

- https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-9701BBA7-EC0E-4016-A9C8-964AA4838954
- https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/Scripts.htm
- https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/WritingDebugging_UM.htm

## 2D limitation

Autodesk's `DrawingManager.createDrawing` API was introduced in July 2026 as preview functionality. Do not rely on it for released production automation. Use supervised Fusion drawing creation and human verification until the exact API path is released and MORFRAC validates it.

Reference: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/DrawingManager_createDrawing.htm

## Readiness sequence

1. Install and manually run the read-only API probe.
2. Record Fusion/application/API/document context receipt.
3. Run a disposable 3D smoke test in a non-project document after exact approval.
4. Verify parameter units, feature health, save isolation and rollback.
5. Run a disposable supervised 2D drawing test after exact approval.
6. Verify model reference, views, units, dimensions, template and export.
7. Review the allowlisted job schema and connector security before any operational use.

Until all applicable steps pass, report planning capability only and never claim Fusion execution.
