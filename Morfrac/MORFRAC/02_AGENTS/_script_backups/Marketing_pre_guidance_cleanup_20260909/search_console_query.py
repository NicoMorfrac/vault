import argparse
from pathlib import Path
import sys
from datetime import datetime, timedelta

from google.oauth2 import service_account
from googleapiclient.discovery import build

# =========================================
# CONFIG
# =========================================

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

if str(BASE_PATH) not in sys.path:
    sys.path.insert(0, str(BASE_PATH))

from obsidian_report_links import write_markdown_report

REPORT_TYPE = "raw_data_report"
SOURCE_AGENT = "Marketing"


RAW_OUTPUT_PATH = BASE_PATH / r"06_MARKETING\Analytics\Raw_Data\SearchConsole"

SERVICE_ACCOUNT_FILE = r"C:\Users\nicol\.credentials\paperclip-ga4.json"

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]

SITE_URL = "https://www.morfrac.com/"


# =========================================
# AUTH
# =========================================

def get_credentials():
    return service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES,
    )


# =========================================
# DATE PARSER
# =========================================

def parse_date(value):

    value = value.strip()

    if value == "today":
        return datetime.today().strftime("%Y-%m-%d")

    if value.endswith("daysAgo"):
        days = int(value.replace("daysAgo", ""))
        target = datetime.today() - timedelta(days=days)
        return target.strftime("%Y-%m-%d")

    return value


# =========================================
# MARKDOWN TABLE
# =========================================

def markdown_table(headers, rows):

    table = []

    table.append("| " + " | ".join(headers) + " |")
    table.append("| " + " | ".join(["---"] * len(headers)) + " |")

    for row in rows:
        table.append("| " + " | ".join(row) + " |")

    return "\n".join(table)


# =========================================
# MAIN
# =========================================

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)

    parser.add_argument(
        "--dimensions",
        nargs="+",
        default=["query"]
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=50
    )

    parser.add_argument(
        "--save",
        action="store_true"
    )

    args = parser.parse_args()

    start_date = parse_date(args.start)
    end_date = parse_date(args.end)

    creds = get_credentials()

    service = build("searchconsole", "v1", credentials=creds)

    request = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": args.dimensions,
        "rowLimit": args.limit
    }

    response = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body=request
    ).execute()

    print("\nSEARCH CONSOLE QUERY RESULTS\n")

    headers = args.dimensions + [
        "clicks",
        "impressions",
        "ctr",
        "position"
    ]

    print(" | ".join(headers))
    print("-" * 120)

    output_rows = []

    for row in response.get("rows", []):

        values = []

        for key in row["keys"]:
            values.append(str(key))

        clicks = str(round(row.get("clicks", 0), 2))
        impressions = str(round(row.get("impressions", 0), 2))
        ctr = f"{row.get('ctr', 0):.2%}"
        position = str(round(row.get("position", 0), 2))

        values.extend([
            clicks,
            impressions,
            ctr,
            position
        ])

        output_rows.append(values)

        print(" | ".join(values))

    if args.save:

        RAW_OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        filename = f"{timestamp}_SearchConsole_Query.md"

        filepath = RAW_OUTPUT_PATH / filename

        md_content = f"""# Search Console Query Export

## Date

{timestamp}

## Site

{SITE_URL}

## Start Date

{start_date}

## End Date

{end_date}

## Dimensions

{", ".join(args.dimensions)}

## Results

{markdown_table(headers, output_rows)}
"""

        write_markdown_report(filepath, md_content, report_type=REPORT_TYPE, source_agent=SOURCE_AGENT)

        print("\nMARKDOWN FILE CREATED\n")
        print(filepath)


if __name__ == "__main__":
    main()
