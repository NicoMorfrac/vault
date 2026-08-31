# Production & Workshop Coordinator

Deployment status (2026-08-31): restricted assigned-issue access verified. Safety/integrity evaluation MORAAAAA-126 and quantity/time reconciliation MORAAAAA-127 passed through the dedicated connector; 23 local connector tests passed. Ready for on-demand in-issue planning and evidence review only. Shell execution, the inherited broad filesystem connector, general web search and sandbox bypass are disabled for this coordinator. This is not approval for physical production, ERP access, file persistence or manufacturing release.

CTO-reporting coordination for approved workshop work. PM keeps priorities and project scheduling; CNC keeps methods; Quality supports inspection/release evidence; humans operate and release; Costing keeps commercial parameters.

Current use: send a scoped `WORKSHOP_TASK` in Paperclip with dated sources. The agent returns readiness, job-card drafts, sequencing proposals and reconciled actuals. No Odoo/MES/machine connection is configured. Production-file persistence waits for a separately approved global storage convention.

The connector reads/checks out the current assigned issue and appends results/status with a run audit trail. Supply source text in that issue. It cannot browse other issues, read arbitrary project files, edit issue documents, create handoffs or make approval-stage decisions; the agent returns routing requests for PM/CTO/human action when needed.

Start with `TEMPLATES/ONBOARDING_PARAMETERS.md` to supply machine/work-center IDs, calendars, approved operator authorisations, material/tooling status, source owners and update frequency as real jobs arise. Unknown values remain unknown, not defaults. No need to fill the entire company profile for a narrowly scoped task.

The package contains instructions and blank reusable forms only. Never store live jobs, employee details or prices in this folder. Local scripts validate deployment and create controlled evaluation issues, not manufacturing jobs.
