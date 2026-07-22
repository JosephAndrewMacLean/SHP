# /// script
# requires-python = ">=3.10"
# dependencies = ["mcp>=1.2", "requests", "google-auth"]
# ///
"""Google Business Profile MCP server (custom).

Auth: the shared read-only service account (same as GA4/GSC) via
GA_SERVICE_ACCOUNT_KEY_JSON or GOOGLE_APPLICATION_CREDENTIALS, with the
business.manage scope.

Access pipeline (status as of 2026-07-22 — run the `gbp_diagnose` tool any time
to see the live state):
  1. Enable THREE APIs in the GCP project: Business Profile Performance,
     My Business Account Management, My Business Business Information.
  2. Submit the GBP API access request form (quota stays 0 until approved):
     https://developers.google.com/my-business/content/prereqs#request-access
  3. A Business Profile owner adds the service account as a **Manager**
     (business.google.com -> Users).

Wired via .mcp.json -> `uv run scripts/gbp-mcp.py`.
Self-test: `uv run scripts/gbp-mcp.py --selftest`  (runs gbp_diagnose)
"""
import json
import os
import subprocess
import sys

import requests

_CA = "/root/.ccr/ca-bundle.crt"
if os.path.exists(_CA):
    os.environ.setdefault("REQUESTS_CA_BUNDLE", _CA)

CRED_DIR = os.path.expanduser("~/.config/shp-ga")
CRED_FILE = os.path.join(CRED_DIR, "service-account.json")
SCOPE = ["https://www.googleapis.com/auth/business.manage"]

ACCT_API = "https://mybusinessaccountmanagement.googleapis.com/v1"
INFO_API = "https://mybusinessbusinessinformation.googleapis.com/v1"
PERF_API = "https://businessprofileperformance.googleapis.com/v1"
REVIEWS_API = "https://mybusiness.googleapis.com/v4"


def _ensure_cred_file() -> str:
    """Mirror scripts/ga-mcp.sh credential resolution."""
    gac = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if gac and os.path.isfile(gac):
        return gac
    key = os.environ.get("GA_SERVICE_ACCOUNT_KEY_JSON", "")
    if key:
        os.makedirs(CRED_DIR, mode=0o700, exist_ok=True)
        if not os.path.isfile(CRED_FILE):
            raw = key if key.lstrip().startswith("{") else None
            if raw is None:
                import base64
                raw = base64.b64decode("".join(key.split())).decode()
            fd = os.open(CRED_FILE, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
            with os.fdopen(fd, "w") as f:
                f.write(raw)
        return CRED_FILE
    adc = os.path.expanduser("~/.config/gcloud/application_default_credentials.json")
    if os.path.isfile(adc):
        return adc
    raise RuntimeError("No Google credentials found — see docs/google-analytics-mcp-setup.md")


def _token() -> str:
    import google.auth.transport.requests
    from google.oauth2 import service_account
    creds = service_account.Credentials.from_service_account_file(
        _ensure_cred_file(), scopes=SCOPE)
    creds.refresh(google.auth.transport.requests.Request())
    return creds.token


def api_get(url: str, **params) -> dict:
    r = requests.get(url, params=params,
                     headers={"Authorization": f"Bearer {_token()}"}, timeout=60)
    try:
        body = r.json()
    except Exception:
        body = {"raw": r.text[:400]}
    if r.status_code != 200:
        return {"http": r.status_code, "error": body.get("error", body)}
    return body


def _j(x: object) -> str:
    return json.dumps(x, indent=1, default=str)


from mcp.server.fastmcp import FastMCP

mcp = FastMCP("google-business-profile")


@mcp.tool()
def gbp_diagnose() -> str:
    """Report the live state of the GBP API access pipeline: which APIs respond,
    whether quota is granted, and whether the service account can see any
    Business Profile accounts. Run this first if anything errors."""
    out = {}
    acct = api_get(f"{ACCT_API}/accounts")
    out["account_management_api"] = acct
    info = api_get(f"{INFO_API}/attributes", regionCode="US", languageCode="en",
                   categoryName="categories/gcid:orthopedic_surgeon", pageSize=1)
    out["business_information_api"] = (
        "OK" if "attributeMetadata" in info or "attributes" in info else info)
    verdict = []
    err = json.dumps(acct)
    if "SERVICE_DISABLED" in err or "has not been used" in err:
        verdict.append("Step 1 pending: enable My Business Account Management API "
                       "(and Business Information + Business Profile Performance) "
                       "in the GCP project.")
    elif "RESOURCE_EXHAUSTED" in err or '"http": 429' in err:
        verdict.append("APIs enabled but quota is 0 — Step 2 pending: submit the "
                       "GBP access request form and wait for approval.")
    elif acct.get("accounts"):
        verdict.append("Access WORKS: accounts visible. If locations are missing, "
                       "confirm the service account is a Manager on the right "
                       "Business Profile account (Step 3).")
    elif "http" not in acct:
        verdict.append("APIs respond but no accounts visible — Step 3 pending: add "
                       "the service account as a Manager at business.google.com -> "
                       "Users.")
    else:
        verdict.append("See raw responses above; likely permission/scope issue.")
    out["verdict"] = " ".join(verdict)
    return _j(out)


@mcp.tool()
def list_accounts() -> str:
    """List Business Profile accounts visible to the service account."""
    return _j(api_get(f"{ACCT_API}/accounts"))


@mcp.tool()
def list_locations(account: str, page_size: int = 100) -> str:
    """List locations under an account (pass e.g. 'accounts/123456789')."""
    return _j(api_get(
        f"{INFO_API}/{account}/locations", pageSize=page_size,
        readMask="name,title,storefrontAddress,phoneNumbers,websiteUri,metadata"))


@mcp.tool()
def performance_daily(location: str, metric: str, start_date: str,
                      end_date: str) -> str:
    """Daily time series for one location and metric.
    location: 'locations/123...'. metric: one of WEBSITE_CLICKS, CALL_CLICKS,
    BUSINESS_DIRECTION_REQUESTS, BUSINESS_IMPRESSIONS_DESKTOP_SEARCH,
    BUSINESS_IMPRESSIONS_MOBILE_SEARCH, BUSINESS_IMPRESSIONS_DESKTOP_MAPS,
    BUSINESS_IMPRESSIONS_MOBILE_MAPS, BUSINESS_CONVERSATIONS, BUSINESS_BOOKINGS.
    Dates: YYYY-MM-DD."""
    sy, sm, sd = start_date.split("-")
    ey, em, ed = end_date.split("-")
    return _j(api_get(
        f"{PERF_API}/{location}:getDailyMetricsTimeSeries",
        dailyMetric=metric,
        **{"dailyRange.start_date.year": sy, "dailyRange.start_date.month": sm,
           "dailyRange.start_date.day": sd, "dailyRange.end_date.year": ey,
           "dailyRange.end_date.month": em, "dailyRange.end_date.day": ed}))


@mcp.tool()
def search_keywords(location: str, from_month: str, to_month: str) -> str:
    """Monthly search keywords that surfaced a location (impressions).
    location: 'locations/123...'; months: YYYY-MM."""
    fy, fm = from_month.split("-")
    ty, tm = to_month.split("-")
    return _j(api_get(
        f"{PERF_API}/{location}/searchkeywords/impressions/monthly",
        **{"monthlyRange.start_month.year": fy, "monthlyRange.start_month.month": fm,
           "monthlyRange.end_month.year": ty, "monthlyRange.end_month.month": tm}))


@mcp.tool()
def list_reviews(account: str, location: str, page_size: int = 20) -> str:
    """Recent reviews for a location (legacy v4 API — the reviews endpoint).
    account: 'accounts/123...'; location: 'locations/123...'.
    HIPAA note: treat review text as potentially sensitive — aggregate counts and
    ratings go in reports; raw text stays out of the repo."""
    return _j(api_get(f"{REVIEWS_API}/{account}/{location}/reviews",
                      pageSize=page_size))


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        try:
            print("SELFTEST gbp_diagnose ->")
            print(gbp_diagnose()[:1200])
        except Exception as e:
            print(f"SELFTEST error: {e}")
        sys.exit(0)
    mcp.run()
