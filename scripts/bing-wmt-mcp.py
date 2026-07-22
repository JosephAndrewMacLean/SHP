# /// script
# requires-python = ">=3.10"
# dependencies = ["mcp>=1.2", "requests"]
# ///
"""Bing Webmaster Tools MCP server (custom — no official/community server exists).

Auth: BING_WEBMASTER_API_KEY env var (generate: bing.com/webmasters -> Settings
-> API access -> API key; requires the site verified in that Bing account —
one-click import from Google Search Console is easiest).

Wired via .mcp.json -> `uv run scripts/bing-wmt-mcp.py`.
Self-test (no MCP client needed): `uv run scripts/bing-wmt-mcp.py --selftest`

Why Bing matters despite small direct traffic: Bing's index feeds Microsoft
Copilot and ChatGPT search — part of the AEO/GEO workstream
(docs/data-sources-roadmap.md §7).
"""
import json
import os
import sys

import requests

# Trust the environment's TLS-intercepting proxy if its bundle exists.
_CA = "/root/.ccr/ca-bundle.crt"
if os.path.exists(_CA):
    os.environ.setdefault("REQUESTS_CA_BUNDLE", _CA)

API_KEY = os.environ.get("BING_WEBMASTER_API_KEY", "")
BASE = "https://ssl.bing.com/webmaster/api.svc/json"
DEFAULT_SITE = "https://synergyhealth.org/"


def bing_get(method: str, **params) -> object:
    if not API_KEY:
        return {"error": "BING_WEBMASTER_API_KEY is not set in this environment. "
                         "Add it in the Claude Code environment settings "
                         "(sessions started afterwards will have it)."}
    params["apikey"] = API_KEY
    r = requests.get(f"{BASE}/{method}", params=params, timeout=60)
    try:
        body = r.json()
    except Exception:
        return {"error": f"HTTP {r.status_code}", "body": r.text[:500]}
    if r.status_code != 200:
        return {"error": f"HTTP {r.status_code}", "body": body}
    return body.get("d", body)


def _cap(data: object, limit: int) -> str:
    if isinstance(data, list) and limit:
        data = data[:limit]
    return json.dumps(data, indent=1, default=str)


from mcp.server.fastmcp import FastMCP

mcp = FastMCP("bing-webmaster")


@mcp.tool()
def query_stats(site_url: str = DEFAULT_SITE, limit: int = 25) -> str:
    """Top search queries for the site on Bing: impressions, clicks, position."""
    return _cap(bing_get("GetQueryStats", siteUrl=site_url), limit)


@mcp.tool()
def page_stats(site_url: str = DEFAULT_SITE, limit: int = 25) -> str:
    """Top pages for the site in Bing search: impressions, clicks, position."""
    return _cap(bing_get("GetPageStats", siteUrl=site_url), limit)


@mcp.tool()
def rank_and_traffic_stats(site_url: str = DEFAULT_SITE) -> str:
    """Daily impressions and clicks time series for the site on Bing."""
    return _cap(bing_get("GetRankAndTrafficStats", siteUrl=site_url), 0)


@mcp.tool()
def crawl_stats(site_url: str = DEFAULT_SITE) -> str:
    """Bingbot crawl activity and crawl-error counts over time."""
    return _cap(bing_get("GetCrawlStats", siteUrl=site_url), 0)


@mcp.tool()
def url_submission_quota(site_url: str = DEFAULT_SITE) -> str:
    """Remaining daily/monthly IndexNow-style URL submission quota."""
    return _cap(bing_get("GetUrlSubmissionQuota", siteUrl=site_url), 0)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        if not API_KEY:
            print("SELFTEST: server code OK; BING_WEBMASTER_API_KEY not set — "
                  "tools will return a clear error until the key is added.")
            sys.exit(0)
        print("SELFTEST: key present; GetUrlSubmissionQuota ->")
        print(_cap(bing_get("GetUrlSubmissionQuota", siteUrl=DEFAULT_SITE), 0)[:500])
        sys.exit(0)
    mcp.run()
