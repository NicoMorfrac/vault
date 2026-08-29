# Data Access Map

## Read when relevant and authorised

- Paperclip issue, comments, dependencies, and attached/exported data
- `06_MARKETING/Analytics/` for dated GA4 and campaign context
- `06_MARKETING/SEO/` and `06_MARKETING/SEO_Agent/` for organic/search-intent context only
- `06_MARKETING/Content/` and `06_MARKETING/SEO_Content_Drafts/` for approved message and landing-page assets
- `06_MARKETING/Playbooks/` for MORFRAC marketing process
- approved public MORFRAC pages and product documentation
- authorised CRM/Odoo/sales exports containing only necessary fields
- official current Google Ads/Analytics/Tag Manager documentation

## Write only after save approval

- `06_MARKETING/Campaigns/Google_Ads/<Issue-ID>_<ShortCampaign>/`

All outputs are Markdown planning files. CSV exports remain source inputs and are not modified.

## Never write/access

- live Google Ads, GA4, Tag Manager, Merchant Center, CMS, Odoo, CRM, billing, social, or email systems;
- `00_SYSTEM/` or another agent's instructions;
- project engineering folders;
- any path outside the MORFRAC vault;
- personal/customer data not required for the task.

## Data-quality rule

Record source, account/property, date range, timezone, currency, filters, attribution setting, export date, and missing fields before drawing conclusions.
