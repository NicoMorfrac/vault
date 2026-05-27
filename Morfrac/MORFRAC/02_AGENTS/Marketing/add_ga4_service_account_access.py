from pathlib import Path

from google.analytics.admin import AnalyticsAdminServiceClient
from google.analytics.admin_v1alpha.types import AccessBinding
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

ACCOUNT_ID = "308773452"
SERVICE_ACCOUNT_EMAIL = "paperclip-ga4@morfrac-paperclip.iam.gserviceaccount.com"

CLIENT_FILE = r"C:\Users\nicol\.credentials\ga4-admin-oauth-client.json"
TOKEN_FILE = r"C:\Users\nicol\.credentials\ga4-admin-oauth-token.json"

SCOPES = ["https://www.googleapis.com/auth/analytics.manage.users"]

creds = None

if Path(TOKEN_FILE).exists():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_FILE, SCOPES)
        creds = flow.run_local_server(port=0)

    Path(TOKEN_FILE).write_text(creds.to_json(), encoding="utf-8")

client = AnalyticsAdminServiceClient(credentials=creds)

parent = f"accounts/{ACCOUNT_ID}"

binding = AccessBinding(
    user=f"serviceAccount:{SERVICE_ACCOUNT_EMAIL}",
    roles=["predefinedRoles/viewer"],
)

response = client.create_access_binding(
    parent=parent,
    access_binding=binding,
)

print("Created access binding:")
print(response)