from pathlib import Path

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Metric, Dimension
from google.oauth2 import service_account

SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]

PROPERTY_ID = "435000386"
SERVICE_ACCOUNT_FILE = Path(r"C:\Users\nicol\.credentials\paperclip-ga4.json")

if not SERVICE_ACCOUNT_FILE.exists():
    raise FileNotFoundError(
        f"GA4 service-account credentials file not found: {SERVICE_ACCOUNT_FILE}"
    )

creds = service_account.Credentials.from_service_account_file(
    str(SERVICE_ACCOUNT_FILE),
    scopes=SCOPES,
)

client = BetaAnalyticsDataClient(credentials=creds)

request = RunReportRequest(
    property=f"properties/{PROPERTY_ID}",
    dimensions=[Dimension(name="date")],
    metrics=[
        Metric(name="sessions"),
        Metric(name="totalUsers"),
    ],
    date_ranges=[DateRange(start_date="7daysAgo", end_date="today")],
)

response = client.run_report(request)

print("\nGA4 CONNECTION SUCCESS\n")

for row in response.rows:
    print(
        f"Date: {row.dimension_values[0].value} | "
        f"Sessions: {row.metric_values[0].value} | "
        f"Users: {row.metric_values[1].value}"
    )
