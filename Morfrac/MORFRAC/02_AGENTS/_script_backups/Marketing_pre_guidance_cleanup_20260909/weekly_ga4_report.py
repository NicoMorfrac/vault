from datetime import datetime
from pathlib import Path
import sys

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Metric, Dimension
from google.oauth2 import service_account

# =========================
# CONFIG
# =========================

PROPERTY_ID = "435000386"

BASE_PATH = Path(r"C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC")

if str(BASE_PATH) not in sys.path:
    sys.path.insert(0, str(BASE_PATH))

from obsidian_report_links import write_markdown_report

REPORT_TYPE = "weekly_report"
SOURCE_AGENT = "Marketing"


SERVICE_ACCOUNT_FILE = Path(r"C:\Users\nicol\.credentials\paperclip-ga4.json")

REPORTS_PATH = BASE_PATH / r"06_MARKETING\Analytics\Weekly_Reports"
RAW_GA4_PATH = BASE_PATH / r"06_MARKETING\Analytics\Raw_Data\GA4"

SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]


# =========================
# AUTH
# =========================

def get_credentials():
    if not SERVICE_ACCOUNT_FILE.exists():
        raise FileNotFoundError(
            f"GA4 service-account credentials file not found: {SERVICE_ACCOUNT_FILE}"
        )

    return service_account.Credentials.from_service_account_file(
        str(SERVICE_ACCOUNT_FILE),
        scopes=SCOPES,
    )

# =========================
# GA4 QUERY
# =========================

def run_ga4_report(client, start_date, end_date, dimensions, metrics):
    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        dimensions=[Dimension(name=d) for d in dimensions],
        metrics=[Metric(name=m) for m in metrics],
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
    )

    response = client.run_report(request)

    rows = []
    for row in response.rows:
        item = {}

        for i, dimension in enumerate(dimensions):
            item[dimension] = row.dimension_values[i].value

        for i, metric in enumerate(metrics):
            item[metric] = row.metric_values[i].value

        rows.append(item)

    return rows


def sum_metric(rows, metric):
    total = 0
    for row in rows:
        try:
            total += float(row.get(metric, 0))
        except ValueError:
            pass
    return total


def percentage_change(current, previous):
    if previous == 0:
        return None
    return ((current - previous) / previous) * 100


# =========================
# FORMAT HELPERS
# =========================

def format_change(value):
    if value is None:
        return "N/A"
    return f"{value:.1f}%"


def markdown_table(rows, columns):
    if not rows:
        return "No data available.\n"

    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join(["---"] * len(columns)) + " |"

    body = []
    for row in rows:
        body.append("| " + " | ".join(str(row.get(col, "")) for col in columns) + " |")

    return "\n".join([header, separator] + body)


# =========================
# MAIN
# =========================

def main():
    today = datetime.now().strftime("%Y-%m-%d")

    REPORTS_PATH.mkdir(parents=True, exist_ok=True)
    RAW_GA4_PATH.mkdir(parents=True, exist_ok=True)

    creds = get_credentials()
    client = BetaAnalyticsDataClient(credentials=creds)

    # Date ranges
    current_7d = ("7daysAgo", "today")
    previous_7d = ("14daysAgo", "8daysAgo")
    current_28d = ("28daysAgo", "today")
    previous_28d = ("56daysAgo", "29daysAgo")

    metrics = ["sessions", "totalUsers", "engagedSessions", "engagementRate"]
    dimensions_date = ["date"]

    current_7_rows = run_ga4_report(client, *current_7d, dimensions_date, metrics)
    previous_7_rows = run_ga4_report(client, *previous_7d, dimensions_date, metrics)
    current_28_rows = run_ga4_report(client, *current_28d, dimensions_date, metrics)
    previous_28_rows = run_ga4_report(client, *previous_28d, dimensions_date, metrics)

    # Additional breakdowns
    source_rows = run_ga4_report(
        client,
        "7daysAgo",
        "today",
        ["sessionSourceMedium"],
        ["sessions", "totalUsers", "engagedSessions"]
    )

    landing_rows = run_ga4_report(
        client,
        "7daysAgo",
        "today",
        ["landingPage"],
        ["sessions", "totalUsers", "engagedSessions"]
    )

    device_rows = run_ga4_report(
        client,
        "7daysAgo",
        "today",
        ["deviceCategory"],
        ["sessions", "totalUsers"]
    )

    country_rows = run_ga4_report(
        client,
        "7daysAgo",
        "today",
        ["country"],
        ["sessions", "totalUsers"]
    )

    # Totals
    current_7_sessions = sum_metric(current_7_rows, "sessions")
    previous_7_sessions = sum_metric(previous_7_rows, "sessions")
    current_28_sessions = sum_metric(current_28_rows, "sessions")
    previous_28_sessions = sum_metric(previous_28_rows, "sessions")

    current_7_users = sum_metric(current_7_rows, "totalUsers")
    previous_7_users = sum_metric(previous_7_rows, "totalUsers")
    current_28_users = sum_metric(current_28_rows, "totalUsers")
    previous_28_users = sum_metric(previous_28_rows, "totalUsers")

    sessions_7_change = percentage_change(current_7_sessions, previous_7_sessions)
    sessions_28_change = percentage_change(current_28_sessions, previous_28_sessions)

    users_7_change = percentage_change(current_7_users, previous_7_users)
    users_28_change = percentage_change(current_28_users, previous_28_users)

    # Sort tables
    source_rows = sorted(source_rows, key=lambda x: float(x.get("sessions", 0)), reverse=True)
    landing_rows = sorted(landing_rows, key=lambda x: float(x.get("sessions", 0)), reverse=True)
    device_rows = sorted(device_rows, key=lambda x: float(x.get("sessions", 0)), reverse=True)
    country_rows = sorted(country_rows, key=lambda x: float(x.get("sessions", 0)), reverse=True)

    # Raw data file
    raw_file = RAW_GA4_PATH / f"{today}_GA4_Raw_Data.md"

    raw_content = f"""# GA4 Raw Data

## Date Pulled

{today}

## Property ID

{PROPERTY_ID}

## Current 7 Days

{markdown_table(current_7_rows, ["date", "sessions", "totalUsers", "engagedSessions", "engagementRate"])}

## Previous 7 Days

{markdown_table(previous_7_rows, ["date", "sessions", "totalUsers", "engagedSessions", "engagementRate"])}

## Current 28 Days

{markdown_table(current_28_rows, ["date", "sessions", "totalUsers", "engagedSessions", "engagementRate"])}

## Previous 28 Days

{markdown_table(previous_28_rows, ["date", "sessions", "totalUsers", "engagedSessions", "engagementRate"])}

## Source / Medium

{markdown_table(source_rows, ["sessionSourceMedium", "sessions", "totalUsers", "engagedSessions"])}

## Landing Pages

{markdown_table(landing_rows[:20], ["landingPage", "sessions", "totalUsers", "engagedSessions"])}

## Devices

{markdown_table(device_rows, ["deviceCategory", "sessions", "totalUsers"])}

## Countries

{markdown_table(country_rows[:20], ["country", "sessions", "totalUsers"])}
"""

    write_markdown_report(raw_file, raw_content, report_type="raw_data_report", source_agent=SOURCE_AGENT)

    # Report file
    report_file = REPORTS_PATH / f"{today}_Weekly_Marketing_Report.md"

    alert_lines = []

    if sessions_7_change is not None and sessions_7_change < -20:
        alert_lines.append(f"- CRITICAL: Sessions dropped {sessions_7_change:.1f}% over 7 days.")

    if sessions_28_change is not None and sessions_28_change < -20:
        alert_lines.append(f"- CRITICAL: Sessions dropped {sessions_28_change:.1f}% over 28 days.")

    if not alert_lines:
        alert_lines.append("- No critical GA4 traffic alerts detected.")

    report_content = f"""# Weekly Marketing Report

## Objective

Review MORFRAC website traffic performance using GA4 data and identify actionable changes.

## Executive Summary

- Current 7-day sessions: {int(current_7_sessions)}
- Previous 7-day sessions: {int(previous_7_sessions)}
- 7-day sessions change: {format_change(sessions_7_change)}
- Current 28-day sessions: {int(current_28_sessions)}
- Previous 28-day sessions: {int(previous_28_sessions)}
- 28-day sessions change: {format_change(sessions_28_change)}

## Key Metrics

| Metric | Current 7d | Previous 7d | Change | Current 28d | Previous 28d | Change |
|---|---:|---:|---:|---:|---:|---:|
| Sessions | {int(current_7_sessions)} | {int(previous_7_sessions)} | {format_change(sessions_7_change)} | {int(current_28_sessions)} | {int(previous_28_sessions)} | {format_change(sessions_28_change)} |
| Users | {int(current_7_users)} | {int(previous_7_users)} | {format_change(users_7_change)} | {int(current_28_users)} | {int(previous_28_users)} | {format_change(users_28_change)} |

## Critical Issues

{chr(10).join(alert_lines)}

## Traffic Analysis

### Source / Medium

{markdown_table(source_rows[:10], ["sessionSourceMedium", "sessions", "totalUsers", "engagedSessions"])}

### Top Landing Pages

{markdown_table(landing_rows[:10], ["landingPage", "sessions", "totalUsers", "engagedSessions"])}

### Device Analysis

{markdown_table(device_rows, ["deviceCategory", "sessions", "totalUsers"])}

### Geography

{markdown_table(country_rows[:10], ["country", "sessions", "totalUsers"])}

## Opportunities

Review manually:

- Pages with good sessions but low engaged sessions
- Sources bringing traffic with weak engagement
- Countries that may not match MORFRAC commercial targets
- Mobile vs desktop performance

## Recommendations

### Recommendation 1

- Action: Review top landing pages with low engagement.
- Reason: High traffic without engagement usually indicates weak intent match, weak CTA, or poor page structure.
- Expected impact: Better lead quality and improved conversion.
- Priority: Medium
- Data source: GA4

### Recommendation 2

- Action: Compare traffic sources by engagement before increasing effort in any channel.
- Reason: Session volume alone does not prove quality.
- Expected impact: Avoid wasting time on low-quality traffic.
- Priority: Medium
- Data source: GA4

## Sources

- Google Analytics 4
- Property ID: {PROPERTY_ID}

## Traceability

- Date data pulled: {today}
- Raw GA4 file written: {raw_file}
- Weekly report written: {report_file}
- Script used: weekly_ga4_report.py
"""

    write_markdown_report(report_file, report_content, report_type=REPORT_TYPE, source_agent=SOURCE_AGENT)

    print("\nWEEKLY GA4 REPORT CREATED\n")
    print(f"Raw data: {raw_file}")
    print(f"Report: {report_file}")


if __name__ == "__main__":
    main()

