from __future__ import annotations

import sys
from pathlib import Path

from google.analytics.admin import AnalyticsAdminServiceClient
from google.analytics.admin_v1alpha.types import AccessBinding
from google.api_core.exceptions import GoogleAPICallError
from google.auth.exceptions import GoogleAuthError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


ACCOUNT_NAME = "accounts/308773452"
SERVICE_ACCOUNT_EMAIL = "paperclip-ga4@morfrac-paperclip.iam.gserviceaccount.com"
VIEWER_ROLE = "predefinedRoles/viewer"

SCOPES = ["https://www.googleapis.com/auth/analytics.manage.users"]

CLIENT_SECRET_FILE = Path(
    r"C:\Users\nicol\.credentials\ga4-admin-oauth-client.json"
)
TOKEN_FILE = Path(
    r"C:\Users\nicol\.credentials\ga4-admin-oauth-token.json"
)


def load_user_credentials() -> Credentials:
    credentials = None

    if TOKEN_FILE.exists():
        credentials = Credentials.from_authorized_user_file(
            str(TOKEN_FILE),
            SCOPES,
        )

    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())

    if not credentials or not credentials.valid:
        if not CLIENT_SECRET_FILE.exists():
            raise FileNotFoundError(
                f"OAuth client secrets file not found: {CLIENT_SECRET_FILE}"
            )

        flow = InstalledAppFlow.from_client_secrets_file(
            str(CLIENT_SECRET_FILE),
            SCOPES,
        )
        credentials = flow.run_local_server(port=0)

        TOKEN_FILE.parent.mkdir(parents=True, exist_ok=True)
        TOKEN_FILE.write_text(credentials.to_json(), encoding="utf-8")

    return credentials


def create_service_account_viewer_binding() -> AccessBinding:
    credentials = load_user_credentials()
    client = AnalyticsAdminServiceClient(credentials=credentials)

    binding = AccessBinding(
        user=SERVICE_ACCOUNT_EMAIL,
        roles=[VIEWER_ROLE],
    )

    return client.create_access_binding(
        parent=ACCOUNT_NAME,
        access_binding=binding,
    )


def main() -> int:
    try:
        created_binding = create_service_account_viewer_binding()

    except GoogleAPICallError as exc:
        print("Google Analytics Admin API request failed.", file=sys.stderr)
        print(f"{type(exc).__name__}: {exc}", file=sys.stderr)
        return 1

    except GoogleAuthError as exc:
        print("Google OAuth authentication failed.", file=sys.stderr)
        print(f"{type(exc).__name__}: {exc}", file=sys.stderr)
        return 1

    except Exception as exc:
        print("Failed to create GA4 account access binding.", file=sys.stderr)
        print(f"{type(exc).__name__}: {exc}", file=sys.stderr)
        return 1

    print("Created GA4 account access binding:")
    print(f"  Name: {created_binding.name}")
    print(f"  User: {created_binding.user}")
    print(f"  Roles: {', '.join(created_binding.roles)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())