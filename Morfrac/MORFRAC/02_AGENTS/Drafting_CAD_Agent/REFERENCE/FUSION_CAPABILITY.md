# Fusion 360 capability and limitations

## Verified locally; capability extension prepared 2026-09-06

- Fusion 2704.1.53 launched from the current user's Autodesk webdeploy production directory.
- MORFRAC Fusion Bridge 0.4.0 is the configured startup add-in. The earlier 0.3.3 path completed supervised, hash-verified F3D/STEP/DXF/preview export with the ORF12 v10 review candidate; 0.4.0 adds schema-tested general reference operations.
- Custom-event main-thread execution, fixed queue, heartbeat, validation, no-overwrite behavior, failure receipts, native F3D/STEP/DXF export and preview capture exercised.
- Paperclip exposes three Drafting tools: status, one-shot internal reference build and verified receipt.

## Supported integration route

The installed add-in watches only the fixed MORFRAC queue. Its worker thread never calls Fusion APIs; it fires a custom event so modelling executes on Fusion's main thread. Jobs cannot provide code or arbitrary paths and are limited to schema-validated declarative operations. Existing outputs are never overwritten. Attachment sources are copied to a controlled folder and SHA-256 checked before import.

Official references:

- https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-9701BBA7-EC0E-4016-A9C8-964AA4838954
- https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/Scripts.htm
- https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/WritingDebugging_UM.htm

## 2D limitation

Autodesk's `DrawingManager.createDrawing` API was introduced in July 2026 as preview functionality. Do not rely on it for released production automation. Use supervised Fusion drawing creation and human verification until the exact API path is released and MORFRAC validates it.

Reference: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/DrawingManager_createDrawing.htm

## Current boundary

Supported operations are instruction-driven cylinder, box and tube; an ordered polygon extrusion with circular holes; hash-bound reference import for DXF, SVG, STEP/STP, IGES/IGS, SAT, SMT, F3D, STL, OBJ and 3MF; and the validated ORF12 bracket family. PDFs/images are read as geometry evidence and translated by the agent into a supported declarative operation. These cover common prismatic reference parts and supplied CAD reuse, but not arbitrary freeform reconstruction. A part beyond this set needs one consolidated clarification or a reviewed new declarative feature family.

Always require a fresh bridge heartbeat and exact output-hash receipt. Automated production drawings, cloud save, master modification, CAM, FEA, manufacturing release and external handoff are unavailable through this connector.
