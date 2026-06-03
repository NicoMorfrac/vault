import pickle
import pandas as pd
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

REPORT_TYPE = "content_opportunities"
SOURCE_AGENT = "Marketing"


OUTPUT_PATH = BASE_PATH / r"06_MARKETING\SEO\Content_Opportunities"

CLIENT_SECRET_FILE = r"C:\Users\nicol\.credentials\oauth_client.json"

TOKEN_PATH = Path(__file__).parent / "token_search_console.pkl"

SCOPES = [
    "https://www.googleapis.com/auth/webmasters.readonly"
]

SITE_URL = "https://www.morfrac.com/"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

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

def today():

    return datetime.today().strftime("%Y-%m-%d")


def date_days_ago(days):

    return (
        datetime.today() - timedelta(days=days)
    ).strftime("%Y-%m-%d")


def classify_query(query):

    q = query.lower()

    branded_terms = [
        "morfrac",
        "morf",
        "morfblock",
        "morfring",
        "powerfurl",
        "mreel",
        "morfwing",
    ]

    for term in branded_terms:

        if term in q:
            return "Branded"

    return "Non-branded"


def markdown_table(headers, rows):

    if not rows:
        return "No data available.\n"

    table = []

    table.append(
        "| " + " | ".join(headers) + " |"
    )

    table.append(
        "| " + " | ".join(["---"] * len(headers)) + " |"
    )

    for row in rows:

        table.append(
            "| " + " | ".join(str(v) for v in row) + " |"
        )

    return "\n".join(table)

# =========================================
# SEARCH CONSOLE QUERY
# =========================================

def query_search_console(
    service,
    start_date,
    end_date,
    dimensions,
    limit=250
):

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

# =========================================
# MAIN
# =========================================

def main():

    run_date = today()

    start_date = date_days_ago(28)
    end_date = today()

    creds = get_credentials()

    service = build(
        "searchconsole",
        "v1",
        credentials=creds
    )

    query_rows = query_search_console(
        service,
        start_date,
        end_date,
        ["query"],
        limit=500
    )

    opportunities = []

    for row in query_rows:

        query = row.get("query", "")
        clicks = row.get("clicks", 0)
        impressions = row.get("impressions", 0)
        ctr = row.get("ctr", 0)
        position = row.get("position", 0)

        query_type = classify_query(query)

        # Ignore branded
        if query_type == "Branded":
            continue

        # Ignore tiny volume
        if impressions < 30:
            continue

        score = 0

        # =====================================
        # OPPORTUNITY LOGIC
        # =====================================

        if ctr < 0.02:
            score += 3

        if 4 <= position <= 15:
            score += 3

        if impressions > 100:
            score += 2

        if impressions > 500:
            score += 2

        # =====================================
        # PRIORITY
        # =====================================

        priority = "LOW"

        if score >= 7:
            priority = "HIGH"

        elif score >= 4:
            priority = "MEDIUM"

        # =====================================
        # CONTENT RECOMMENDATION
        # =====================================

        recommendation = "Improve SEO landing page"

        if "vs" in query.lower():
            recommendation = "Create comparison article"

        elif "how" in query.lower():
            recommendation = "Create educational article"

        elif "what" in query.lower():
            recommendation = "Create technical explanation page"

        elif "price" in query.lower():
            recommendation = "Create commercial/product page"

        opportunities.append({
            "query": query,
            "clicks": clicks,
            "impressions": impressions,
            "ctr": ctr,
            "position": position,
            "score": score,
            "priority": priority,
            "recommendation": recommendation,
        })

    opportunities = sorted(
        opportunities,
        key=lambda x: (
            x["score"],
            x["impressions"]
        ),
        reverse=True
    )

    # =========================================
    # BUILD TABLE
    # =========================================

    table_rows = []

    for item in opportunities[:50]:

        table_rows.append([
            item["query"],
            round(item["clicks"], 2),
            round(item["impressions"], 2),
            f"{item['ctr']:.2%}",
            round(item["position"], 2),
            item["score"],
            item["priority"],
            item["recommendation"],
        ])

    table = markdown_table(
        [
            "Query",
            "Clicks",
            "Impressions",
            "CTR",
            "Position",
            "Score",
            "Priority",
            "Recommendation"
        ],
        table_rows
    )

    # =========================================
    # OUTPUT
    # =========================================

    output_file = (
        OUTPUT_PATH /
        f"{run_date}_Content_Opportunities.md"
    )

    content = f"""# SEO Content Opportunities

## Date

{run_date}

## Site

{SITE_URL}

## Objective

Identify SEO content and landing page opportunities
from Search Console query data.

## Opportunity Logic

Higher scores are generated by:
- low CTR
- high impressions
- ranking between positions 4 and 15
- non-branded queries

## Opportunities

{table}

## Notes

This report is intended to support:
- SEO strategy
- content generation
- landing page planning
- campaign ideas
- technical article creation
- commercial positioning

Generated from:
- Google Search Console
- Non-branded query analysis

"""

    write_markdown_report(output_file, content, report_type=REPORT_TYPE, source_agent=SOURCE_AGENT)

    print("\nCONTENT OPPORTUNITIES CREATED\n")
    print(output_file)


if __name__ == "__main__":
    main()