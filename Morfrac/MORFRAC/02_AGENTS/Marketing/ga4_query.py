import os
import pickle
import argparse
from pathlib import Path
from datetime import datetime

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest,
    DateRange,
    Metric,
    Dimension,
)

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# =========================================
# CONFIG
# =========================================

PROPERTY_ID = "435000386"

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

RAW_OUTPUT_PATH = BASE_PATH / r"06_MARKETING\Analytics\Raw_Data\GA4"

CLIENT_SECRET_FILE = r"C:\Users\nicol\.credentials\oauth_client.json"

TOKEN_PATH = Path(__file__).parent / "token.pkl"

SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]


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
        default=["date"]
    )

    parser.add_argument(
        "--metrics",
        nargs="+",
        default=["sessions", "totalUsers"]
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

    creds = get_credentials()

    client = BetaAnalyticsDataClient(credentials=creds)

    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        dimensions=[Dimension(name=d) for d in args.dimensions],
        metrics=[Metric(name=m) for m in args.metrics],
        date_ranges=[
            DateRange(
                start_date=args.start,
                end_date=args.end
            )
        ],
        limit=args.limit,
    )

    response = client.run_report(request)

    print("\nGA4 QUERY RESULTS\n")

    headers = args.dimensions + args.metrics

    print(" | ".join(headers))
    print("-" * 100)

    output_rows = []

    for row in response.rows:

        values = []

        for v in row.dimension_values:
            values.append(v.value)

        for v in row.metric_values:
            values.append(v.value)

        output_rows.append(values)

        print(" | ".join(values))

    # =====================================
    # SAVE TO MARKDOWN
    # =====================================

    if args.save:

        RAW_OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        filename = f"{timestamp}_GA4_Query.md"

        filepath = RAW_OUTPUT_PATH / filename

        md_content = f"""# GA4 Query Export

## Date

{timestamp}

## Property ID

{PROPERTY_ID}

## Start Date

{args.start}

## End Date

{args.end}

## Dimensions

{", ".join(args.dimensions)}

## Metrics

{", ".join(args.metrics)}

## Results

{markdown_table(headers, output_rows)}
"""

        filepath.write_text(md_content, encoding="utf-8")

        print("\nMARKDOWN FILE CREATED\n")
        print(filepath)


if __name__ == "__main__":
    main()