# Production & Workshop Coordinator

CTO-reporting coordination for approved workshop work. PM keeps priorities and project scheduling; CNC keeps methods; Quality supports inspection/release evidence; humans operate and release; Costing keeps commercial parameters.

Current use: send a scoped `WORKSHOP_TASK` in Paperclip with dated sources. The agent returns readiness, job-card drafts, sequencing proposals and reconciled actuals. No Odoo/MES/machine connection is configured. Production-file persistence waits for a separately approved global storage convention.

Start with `TEMPLATES/ONBOARDING_PARAMETERS.md` to supply machine/work-center IDs, calendars, approved operator authorisations, material/tooling status, source owners and update frequency as real jobs arise. Unknown values remain unknown, not defaults. No need to fill the entire company profile for a narrowly scoped task.

The package contains instructions and blank reusable forms only. Never store live jobs, employee details or prices in this folder. Local scripts validate deployment and create controlled evaluation issues, not manufacturing jobs.
