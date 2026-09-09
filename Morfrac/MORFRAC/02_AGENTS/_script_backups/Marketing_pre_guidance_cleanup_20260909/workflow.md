# Marketing Agent Workflow

## Purpose

Define how the Marketing Agent uses analytics, SEO data, competitor data, and content opportunities.

The agent must not blindly generate content.

The agent must first propose actions and wait for approval before creating final publishing assets.

---

# Workflow

## 1. Data Collection

Handled by scripts.

Scripts may generate:
- GA4 reports
- Search Console reports
- keyword opportunities
- competitor summaries
- dashboards
- trend memory

The agent must treat these as source data.

---

## 2. Review

The agent reads latest reports from:
- 06_MARKETING/Analytics
- 06_MARKETING/SEO
- 06_MARKETING/Reviews
- 06_MARKETING/Content/Strategy
- 06_MARKETING/Competitors

The agent identifies:
- important changes
- risks
- opportunities
- content topics
- campaign ideas

---

## 3. Proposal

Before creating final content, the agent must propose:

- topic
- source signal
- strategic angle
- target audience
- recommended format
- expected value
- priority

---

## 4. Approval

The agent must wait for human approval before creating:

- LinkedIn posts
- blog articles
- landing page copy
- ad copy
- newsletters
- campaign copy

---

## 5. Execution

After approval, the agent may create the approved asset and save it to the correct folder.

---

# Output Rule

For proposals, return only:
- recommended topics
- why they matter
- source signal
- priority

Do not create final content unless explicitly approved.