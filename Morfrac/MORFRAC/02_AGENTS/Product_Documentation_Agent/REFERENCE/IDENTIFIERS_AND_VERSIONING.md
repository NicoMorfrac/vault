# Identifiers and Versioning

## Required identifiers

Each controlled artifact must include:

- unique document ID;
- explicit version/revision;
- product/model/variant and configuration revision;
- serial/lot/date applicability or an explicit “all” approved by the owner;
- language/locale;
- lifecycle status;
- source/review references;
- superseded document/version where relevant.

## Lifecycle labels

- `DRAFT - NOT RELEASED`: working content with no external-use authority.
- `SAVED DRAFT NOT RELEASED`: persisted after the exact save gate but still unreleased.
- `SUPPORT DRAFT - NOT SIGNED/ISSUED`: declaration/compliance support only.
- `HUMAN RELEASE READY`: exact release gate and required reviews complete; still not published/supplied.
- `RELEASED`: only a controlled human/document system may apply this status.
- `OBSOLETE/SUPERSEDED`: retained for traceability and prevented from accidental use.

Never overwrite a released or prior version. Create a new version and link its change basis. Filenames are not sufficient configuration control; use the manifest and hashes.
