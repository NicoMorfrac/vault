# Workflow - Ads Task Intake

## Procedure

1. Read the assigned issue, comments, source files, approvals, and dependencies.
2. Confirm the issue is assigned to this agent.
3. Classify the request: strategy, measurement, budget, keywords, ad copy, build sheet, or performance review.
4. Extract objective, offer, audience, geography, language, landing pages, primary conversion, budget limit, currency, schedule, data sources, deliverables, and origin.
5. Identify whether the request concerns planning, read-only analysis, vault persistence, or a prohibited live mutation.
6. Mark each input confirmed, missing, contradictory, stale, or assumption-only.
7. Identify privacy, policy, engineering-claim, capacity, tracking, and landing-page dependencies.
8. If missing information affects spend, targeting, measurement, compliance, or feasibility, return `NEEDS_INPUT` with the shortest useful question set.
9. Otherwise select the minimum required workflows and continue.

## Minimum for a strategy outline

- business objective;
- offer;
- audience/market;
- geography and language;
- primary conversion or explicit measurement gap;
- budget status: confirmed limit or not yet set.

Without a budget limit, produce architecture and measurement recommendations only. Do not invent a budget.

## Prohibited request handling

If asked to enable campaigns, change spend, edit a live account, or access billing, explain that this planner prepares the exact handoff but cannot perform the live action.
