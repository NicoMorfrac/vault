Every generated report must contain:

type
source_agent
created
related_findings
related_concepts
related_projects
related_reports

and

## Related Links

## KnowledgeRetention-v1 — fields for future analysis

Keep the required fields above and exactly one `## Related Links` section. Normal role saves still use the exact source_agent value and path/version prescribed by their connector. Never add fabricated metadata just to satisfy a template.

For substantive operational reports, also record where available:

- audience: internal or client, with confidential evidence kept out of client documents;
- status: draft, pending_review, approved_for_a_named_purpose, validated_for_a_stated_scope, historical or superseded;
- as_of / source dates and revision; do not confuse archival date with evidence freshness;
- actual Paperclip issue identifier/UUID, report revision, source filenames/pages or exact reviewed comment references;
- approval scope and actual approval references, clearly separating storage approval from business/domain approval;
- related prior reports, supersedes/decision links and applicable project references.

Approval IDs generated after a frozen file plan must be retained in the verified Paperclip save receipt or an independently approved later note, not inserted by silently rewriting the approved file. Never include secret credentials or private execution tokens.

A reusable report body should cover:

1. Objective and scope.
2. Facts and source evidence, with dates/versions and units/currency/tax basis where relevant.
3. Human decisions already made, their precise scope, and decisions still required.
4. Assumptions/unknowns and the effect on confidence.
5. Analysis, method and conclusions; explicitly label estimates, proposals and hypotheses.
6. Limitations, counter-evidence, unresolved risks and what would change the conclusion.
7. Next actions, accountable owners and dependencies; no invented commitments.
8. Related Links to authorised canonical evidence, prior reports and the relevant project/department context.

For a status/review report, use only applicable sections rather than inventing technical or financial detail. Significant failure/blocked findings are useful knowledge when labelled honestly. Avoid copying duplicate discussion or sensitive information unnecessarily.

Setup/validation archives are internal evidence, not operational instructions or production certification. Historical files must visibly link to the current baseline/readiness record. The company knowledge index is [[05_BUSINESS/Management/Knowledge_Base/README]].


