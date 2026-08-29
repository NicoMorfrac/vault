# Data Access Map

## Read when relevant

- Approved brief and Paperclip issue history
- `06_MARKETING/SEO_Execution_Queue/` for approved SEO briefs, links, and metadata requirements
- `06_MARKETING/SEO/` and `06_MARKETING/SEO_Agent/` for current deterministic SEO evidence
- `06_MARKETING/Content/Strategy/` for current content classification
- `06_MARKETING/SEO_Content_Proposals/` for approved authority opportunities
- Existing MORFRAC public website pages supplied in the task
- Approved public product documentation and sanitized engineering input

## Write only after save approval

- `06_MARKETING/SEO_Content_Drafts/<Issue-ID>_<ShortTopic>/` for SEO authority packages
- An exact approved location under `06_MARKETING/Content/` for general content drafts

## Never write

- `00_SYSTEM/`
- another agent's instruction folder
- project engineering folders
- analytics source data
- live website/CMS/Odoo/social/advertising systems
- any location outside the MORFRAC vault

## Freshness

Use the newest valid strategy or SEO file only when its date, source, schema, and task relevance are confirmed. Do not assume newest means approved.
