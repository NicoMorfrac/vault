# CAD approval matrix

| Action | Exact gate | Current availability |
| --- | --- | --- |
| First internal reference baseline | Assigned direct task or approved project handoff | Available; no repeated step approval |
| Execute first internal reference build | Same assigned-task authority | Available through controlled bridge |
| Execute 2D build | `APPROVE CAD 2D BUILD <CAD-ID> <Run-Version>` | Blocked until supervised validation |
| Save/export new internal reference files | Same assigned-task authority | Available through controlled bridge; no overwrite |
| Save internal Markdown review | `APPROVE RECORD SAVE <Issue-ID> <Version>` | Available through SpecialistRecords-v1 |
| Prepare external pack | `APPROVE CAD EXTERNAL PACK <CAD-ID> <Version>` | Human handoff only |
| Close task | `APPROVE CAD CLOSE <CAD-ID> <Version>` | Paperclip closeout only |

The first internal reference draft flows under the assigned task. Any geometry decision beyond the supplied baseline, overwrite, production drawing, manufacture, release or external handoff remains separately gated. A task approval never substitutes for manufacturing or release authority.
