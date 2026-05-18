# SEO Content Production Agent Heartbeat

## Purpose

The SEO Content Production Agent heartbeat converts approved SEO briefs into first-draft markdown content.

This heartbeat is drafting-focused, not strategic.

SEO strategy belongs to:

- SEO Intelligence Agent
- SEO Execution Agent

---

## Schedule

Manual initially.

Do NOT automate publishing.

---

## Responsibilities

The heartbeat should:

- read approved content briefs
- generate first-draft markdown content
- integrate approved internal links
- preserve commercial routing
- preserve technical tone

The heartbeat should NOT:

- publish content
- modify live pages
- generate SEO strategy
- override approved briefs

---

## Required Output

Save drafts under:

06_MARKETING/SEO_Content_Drafts/

---

## Reporting Rule

Every heartbeat execution must generate a saved markdown draft or a failed report.

If generation fails, save:

06_MARKETING/SEO_Content_Drafts/CONTENT_DRAFT_FAILED.md

The agent must never complete silently.
