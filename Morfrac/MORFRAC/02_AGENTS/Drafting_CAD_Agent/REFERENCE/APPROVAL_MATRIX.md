# CAD approval matrix

| Action | Exact gate | Current availability |
| --- | --- | --- |
| Freeze requirements/parameters | `APPROVE CAD BASELINE <CAD-ID> <Version>` | Paperclip decision record |
| Execute 3D build | `APPROVE CAD 3D BUILD <CAD-ID> <Run-Version>` | Blocked until connector validation |
| Execute 2D build | `APPROVE CAD 2D BUILD <CAD-ID> <Run-Version>` | Blocked until supervised validation |
| Save CAD binary | `APPROVE CAD SAVE <CAD-ID> <Version>` | Blocked until binary-save connector |
| Export CAD/drawing | `APPROVE CAD EXPORT <CAD-ID> <Export-Version>` | Blocked until export connector validation |
| Save internal Markdown review | `APPROVE RECORD SAVE <Issue-ID> <Version>` | Available through SpecialistRecords-v1 |
| Prepare external pack | `APPROVE CAD EXTERNAL PACK <CAD-ID> <Version>` | Human handoff only |
| Close task | `APPROVE CAD CLOSE <CAD-ID> <Version>` | Paperclip closeout only |

Every approval is limited to the exact frozen source hashes, script/manifest, destination and version presented before the approval. A baseline approval never substitutes for build, save, export, external handoff or release approval.
