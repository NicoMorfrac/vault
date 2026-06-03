import pickle
from pathlib import Path
import sys
from datetime import datetime, timedelta

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

if str(BASE_PATH) not in sys.path:
    sys.path.insert(0, str(BASE_PATH))

from obsidian_report_links import write_markdown_report

REPORT_TYPE = "seo_query_analysis"
SOURCE_AGENT = "Marketing"


RAW_OUTPUT_PATH = BASE_PATH / r"06_MARKETING\Analytics\Raw_Data\SearchConsole"
SEO_OUTPUT_PATH = BASE_PATH / r"06_MARKETING\SEO\Query_Analysis"

CLIENT_SECRET_FILE = r"C:\Users\nicol\.credentials\oauth_client.json"
TOKEN_PATH = Path(__file__).parent / "token_search_console.pkl"

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]

SITE_URL = "https://www.morfrac.com/"

# =========================================
# AUTH
# =========================================

def get_credentials():
    creds = None

    if TOKEN_PATH.exists():
        with open(TOKEN_PATH, "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE,
                SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open(TOKEN_PATH, "wb") as token:
            pickle.dump(creds, token)

    return creds


# =========================================
# HELPERS
# =========================================

def date_days_ago(days):
    return (datetime.today() - timedelta(days=days)).strftime("%Y-%m-%d")


def today():
    return datetime.today().strftime("%Y-%m-%d")


def markdown_table(headers, rows):
    if not rows:
        return "No data available.\n"

    table = []
    table.append("| " + " | ".join(headers) + " |")
    table.append("| " + " | ".join(["---"] * len(headers)) + " |")

    for row in rows:
        table.append("| " + " | ".join(str(v) for v in row) + " |")

    return "\n".join(table)


def query_search_console(service, start_date, end_date, dimensions, limit=100):
    request = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": dimensions,
        "rowLimit": limit,
    }

    response = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body=request
    ).execute()

    rows = []

    for row in response.get("rows", []):
        item = {}

        for i, key in enumerate(row.get("keys", [])):
            item[dimensions[i]] = key

        item["clicks"] = row.get("clicks", 0)
        item["impressions"] = row.get("impressions", 0)
        item["ctr"] = row.get("ctr", 0)
        item["position"] = row.get("position", 0)

        rows.append(item)

    return rows


def sum_metric(rows, metric):
    return sum(float(row.get(metric, 0)) for row in rows)


def weighted_position(rows):
    impressions = sum_metric(rows, "impressions")
    if impressions == 0:
        return 0

    weighted = sum(
        float(row.get("position", 0)) * float(row.get("impressions", 0))
        for row in rows
    )

    return weighted / impressions


def weighted_ctr(rows):
    impressions = sum_metric(rows, "impressions")
    clicks = sum_metric(rows, "clicks")

    if impressions == 0:
        return 0

    return clicks / impressions


def percentage_change(current, previous):
    if previous == 0:
        return None
    return ((current - previous) / previous) * 100


def format_change(value):
    if value is None:
        return "N/A"
    return f"{value:.1f}%"


def classify_query(query):
    q = query.lower()

    branded_terms = [
        "morfrac",
        "morf",
        "morfblock",
        "morf block",
        "mreel",
        "powerfurl",
        "morfring",
        "morfwing",
    ]

    for term in branded_terms:
        if term in q:
            return "Branded"

    return "Non-branded"


# =========================================
# MAIN
# =========================================

def main():
    run_date = today()

    current_start = date_days_ago(28)
    current_end = today()

    previous_start = date_days_ago(56)
    previous_end = date_days_ago(29)

    RAW_OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
    SEO_OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    creds = get_credentials()
    service = build("searchconsole", "v1", credentials=creds)

    current_queries = query_search_console(
        service,
        current_start,
        current_end,
        ["query"],
        limit=250
    )

    current_query_pages = query_search_console(
        service,
        current_start,
        current_end,
        ["query", "page"],
        limit=1000
    )

    previous_queries = query_search_console(
        service,
        previous_start,
        previous_end,
        ["query"],
        limit=250
    )

    current_pages = query_search_console(
        service,
        current_start,
        current_end,
        ["page"],
        limit=100
    )

    current_devices = query_search_console(
        service,
        current_start,
        current_end,
        ["device"],
        limit=20
    )

    current_countries = query_search_console(
        service,
        current_start,
        current_end,
        ["country"],
        limit=50
    )

    current_clicks = sum_metric(current_queries, "clicks")
    previous_clicks = sum_metric(previous_queries, "clicks")

    current_impressions = sum_metric(current_queries, "impressions")
    previous_impressions = sum_metric(previous_queries, "impressions")

    current_ctr = weighted_ctr(current_queries)
    previous_ctr = weighted_ctr(previous_queries)

    current_position = weighted_position(current_queries)
    previous_position = weighted_position(previous_queries)

    clicks_change = percentage_change(current_clicks, previous_clicks)
    impressions_change = percentage_change(current_impressions, previous_impressions)
    ctr_change = percentage_change(current_ctr, previous_ctr)

    position_change = current_position - previous_position

    # Opportunities
    low_ctr_high_impression = []
    position_4_10 = []
    position_11_20 = []
    branded_rows = []
    non_branded_rows = []

    for row in current_queries:
        query = row.get("query", "")
        impressions = row.get("impressions", 0)
        ctr = row.get("ctr", 0)
        position = row.get("position", 0)
        query_type = classify_query(query)

        if query_type == "Branded":
            branded_rows.append(row)
        else:
            non_branded_rows.append(row)

        if impressions >= 30 and ctr < 0.02:
            low_ctr_high_impression.append(row)

        if 4 <= position <= 10:
            position_4_10.append(row)

        if 11 <= position <= 20:
            position_11_20.append(row)

    # Sort opportunities
    low_ctr_high_impression = sorted(
        low_ctr_high_impression,
        key=lambda x: x.get("impressions", 0),
        reverse=True
    )

    position_4_10 = sorted(
        position_4_10,
        key=lambda x: x.get("impressions", 0),
        reverse=True
    )

    position_11_20 = sorted(
        position_11_20,
        key=lambda x: x.get("impressions", 0),
        reverse=True
    )

    branded_clicks = sum_metric(branded_rows, "clicks")
    branded_impressions = sum_metric(branded_rows, "impressions")
    non_branded_clicks = sum_metric(non_branded_rows, "clicks")
    non_branded_impressions = sum_metric(non_branded_rows, "impressions")

    # Tables
    def query_table(rows, limit=20):
        table_rows = []
        for row in rows[:limit]:
            table_rows.append([
                row.get("query", ""),
                round(row.get("clicks", 0), 2),
                round(row.get("impressions", 0), 2),
                f"{row.get('ctr', 0):.2%}",
                round(row.get("position", 0), 2),
                classify_query(row.get("query", "")),
            ])

        return markdown_table(
            ["Query", "Clicks", "Impressions", "CTR", "Position", "Type"],
            table_rows
        )

    def query_page_table(rows, limit=100):
        table_rows = []
        for row in rows[:limit]:
            query = row.get("query", "")

            table_rows.append([
                query,
                row.get("page", ""),
                round(row.get("clicks", 0), 2),
                round(row.get("impressions", 0), 2),
                f"{row.get('ctr', 0):.2%}",
                round(row.get("position", 0), 2),
                classify_query(query),
            ])

        return markdown_table(
            ["Query", "Page", "Clicks", "Impressions", "CTR", "Position", "Type"],
            table_rows
        )

    def page_table(rows, limit=15):
        table_rows = []
        for row in rows[:limit]:
            table_rows.append([
                row.get("page", ""),
                round(row.get("clicks", 0), 2),
                round(row.get("impressions", 0), 2),
                f"{row.get('ctr', 0):.2%}",
                round(row.get("position", 0), 2),
            ])

        return markdown_table(
            ["Page", "Clicks", "Impressions", "CTR", "Position"],
            table_rows
        )

    def simple_dim_table(rows, dimension, limit=20):
        table_rows = []
        for row in rows[:limit]:
            table_rows.append([
                row.get(dimension, ""),
                round(row.get("clicks", 0), 2),
                round(row.get("impressions", 0), 2),
                f"{row.get('ctr', 0):.2%}",
                round(row.get("position", 0), 2),
            ])

        return markdown_table(
            [dimension.title(), "Clicks", "Impressions", "CTR", "Position"],
            table_rows
        )

    # Alerts
    alerts = []

    if clicks_change is not None and clicks_change < -20:
        alerts.append(f"- CRITICAL: Search clicks dropped {clicks_change:.1f}% vs previous 28 days.")

    if impressions_change is not None and impressions_change < -20:
        alerts.append(f"- CRITICAL: Search impressions dropped {impressions_change:.1f}% vs previous 28 days.")

    if ctr_change is not None and ctr_change < -15:
        alerts.append(f"- CRITICAL: Organic CTR dropped {ctr_change:.1f}% vs previous 28 days.")

    if position_change > 5:
        alerts.append(f"- CRITICAL: Average position worsened by {position_change:.1f} positions.")

    if not alerts:
        alerts.append("- No critical Search Console alerts detected.")

    # Raw export
    raw_file = RAW_OUTPUT_PATH / f"{run_date}_SearchConsole_Raw_Data.md"

    raw_content = f"""# Search Console Raw Data

## Date Pulled

{run_date}

## Site

{SITE_URL}

## Current Period

{current_start} to {current_end}

## Previous Period

{previous_start} to {previous_end}

## Queries

{query_table(current_queries, limit=250)}

## Query Page Mapping

{query_page_table(current_query_pages, limit=1000)}

## Pages

{page_table(current_pages, limit=100)}

## Devices

{simple_dim_table(current_devices, "device", limit=20)}

## Countries

{simple_dim_table(current_countries, "country", limit=50)}
"""

    write_markdown_report(raw_file, raw_content, report_type="raw_data_report", source_agent=SOURCE_AGENT)

    # SEO report
    report_file = SEO_OUTPUT_PATH / f"{run_date}_SEO_Query_Analysis.md"

    report_content = f"""# SEO Query Analysis

## Objective

Analyze Search Console performance and identify SEO opportunities for MORFRAC.

## Executive Summary

- Current 28-day clicks: {int(current_clicks)}
- Previous 28-day clicks: {int(previous_clicks)}
- Click change: {format_change(clicks_change)}
- Current 28-day impressions: {int(current_impressions)}
- Previous 28-day impressions: {int(previous_impressions)}
- Impression change: {format_change(impressions_change)}
- Current CTR: {current_ctr:.2%}
- Previous CTR: {previous_ctr:.2%}
- CTR change: {format_change(ctr_change)}
- Current average position: {current_position:.2f}
- Previous average position: {previous_position:.2f}
- Position change: {position_change:.2f}

## Critical Issues

{chr(10).join(alerts)}

## Branded vs Non-Branded

| Type | Clicks | Impressions |
|---|---:|---:|
| Branded | {int(branded_clicks)} | {int(branded_impressions)} |
| Non-branded | {int(non_branded_clicks)} | {int(non_branded_impressions)} |

## Top Queries

{query_table(current_queries, limit=25)}

## Query Page Mapping

{query_page_table(current_query_pages, limit=100)}

## Top Pages

{page_table(current_pages, limit=15)}

## Low CTR / High Impression Opportunities

Trigger:

- Impressions >= 30
- CTR < 2%

{query_table(low_ctr_high_impression, limit=25)}

## Ranking Opportunities: Position 4 to 10

{query_table(position_4_10, limit=25)}

## Ranking Opportunities: Position 11 to 20

{query_table(position_11_20, limit=25)}

## Device Analysis

{simple_dim_table(current_devices, "device", limit=20)}

## Country Analysis

{simple_dim_table(current_countries, "country", limit=20)}

## Recommendations

### Recommendation 1

- Action: Improve titles and meta descriptions for low-CTR, high-impression queries.
- Reason: These queries already receive impressions but fail to attract clicks.
- Expected impact: Increase organic traffic without needing new rankings.
- Priority: High
- Data source: Search Console

### Recommendation 2

- Action: Prioritize queries ranking from position 4 to 10.
- Reason: These are near-page-one / top-result opportunities and may require limited content improvements.
- Expected impact: Higher clicks from existing visibility.
- Priority: High
- Data source: Search Console

### Recommendation 3

- Action: Review non-branded queries separately from branded queries.
- Reason: Branded traffic confirms awareness, but non-branded traffic drives market expansion.
- Expected impact: Better SEO growth strategy.
- Priority: Medium
- Data source: Search Console

## Sources

- Google Search Console
- Site: {SITE_URL}

## Traceability

- Date data pulled: {run_date}
- Current period: {current_start} to {current_end}
- Previous period: {previous_start} to {previous_end}
- Raw Search Console file written: {raw_file}
- SEO analysis file written: {report_file}
- Script used: search_console_report.py
"""

    write_markdown_report(report_file, report_content, report_type=REPORT_TYPE, source_agent=SOURCE_AGENT)

    print("\nSEARCH CONSOLE REPORT CREATED\n")
    print(f"Raw data: {raw_file}")
    print(f"SEO report: {report_file}")


if __name__ == "__main__":
    main()