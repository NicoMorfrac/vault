# Export and handoff workflow

1. Verify the source model/drawing, configuration, revision and review state.
2. Define each format, units, tessellation/version options, filename, path and recipient purpose.
3. Identify information loss and whether the export remains linked to the authoritative source.
4. Require `APPROVE CAD EXPORT <CAD-ID> <Export-Version>` before a future validated export.
5. Verify exported file hash, open/import check and source traceability.
6. Keep output `INTERNAL ONLY - NOT RELEASED` until the separate external-pack gate and required reviews.
7. Give CNC/FEA/Quality/Product Documentation only their minimum approved extract.

The agent never sends, uploads, publishes, signs or releases an export.
