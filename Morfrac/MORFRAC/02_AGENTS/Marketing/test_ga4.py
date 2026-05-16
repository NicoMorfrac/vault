import os
import pickle

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Metric, Dimension

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]

PROPERTY_ID = "435000386"

TOKEN_PATH = "token.pkl"
CLIENT_SECRET_FILE = r"C:\Users\nicol\.credentials\oauth_client.json"

creds = None

if os.path.exists(TOKEN_PATH):
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