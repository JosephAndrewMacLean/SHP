# Google Analytics (GA4) MCP — Setup Guide

This workspace is wired to Google's **official Google Analytics MCP server**
([github.com/googleanalytics/google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp)),
so Claude can query real GA4 data — which pages are performing now and how they've
performed historically — instead of guessing.

The server config lives in [`.mcp.json`](../.mcp.json) and starts via
[`scripts/ga-mcp.sh`](../scripts/ga-mcp.sh). **The only missing piece is a
credential**, which requires the one-time setup below (~15 minutes).

## What Claude can do once this is live

Read-only reporting tools (they appear as `mcp__google-analytics__*`):

| Tool | What it answers |
|------|-----------------|
| `get_account_summaries` | Which GA accounts/properties we have (finds our property ID) |
| `get_property_details` | Property settings, time zone, currency |
| `run_report` | The workhorse: sessions, users, conversions by page, channel, source, device, geography — **any date range in the property's history** |
| `run_realtime_report` | What's happening on the site right now |
| `get_custom_dimensions_and_metrics` | Custom definitions available on our property |

Example asks once connected:

- "Top 25 pages by organic sessions, last 90 days vs. the previous 90."
- "How has the spine service-line page performed month-by-month over the past year?"
- "Which blog posts drive the most engaged sessions from mobile?"
- "Which landing pages get traffic but have weak engagement — content refresh candidates?"

> **Historical note:** GA4's Data API can query back to when the GA4 property
> began collecting. If SHP was on Universal Analytics before the GA4 cutover
> (UA stopped processing mid-2023/2024), those older years are not in GA4.

## One-time setup

You'll create a Google Cloud **service account** (a robot identity), give it
**read-only** access to SHP's GA4 property, and paste its key into this Claude
Code environment as an environment variable.

> **Who does what:** Steps 1–4 need a Google account with access to a Google
> Cloud project (any account works — it doesn't need GA access). Step 5 needs
> someone with **Administrator** access to SHP's GA4 property. Per
> `playbooks/spine-patient-acquisition.md`, GA4 ownership may sit with the
> external agency — if so, send them the service-account email and ask for
> Viewer access.

### 1. Create (or pick) a Google Cloud project

1. Go to [console.cloud.google.com](https://console.cloud.google.com) and sign in.
2. Top bar → project picker → **New project** (e.g. `shp-marketing-analytics`), or reuse an existing one.

### 2. Enable the two Analytics APIs

With that project selected, enable both (search **APIs & Services → Library**, or use direct links):

- [Google Analytics Data API](https://console.cloud.google.com/apis/library/analyticsdata.googleapis.com)
- [Google Analytics Admin API](https://console.cloud.google.com/apis/library/analyticsadmin.googleapis.com)

### 3. Create the service account

1. **IAM & Admin → Service Accounts → Create service account**.
2. Name: e.g. `ga4-claude-readonly`. Skip the optional role/user-access steps (no Cloud roles needed).
3. **Copy the service-account email** (looks like `ga4-claude-readonly@shp-marketing-analytics.iam.gserviceaccount.com`).

### 4. Create a JSON key

1. Open the service account → **Keys** tab → **Add key → Create new key → JSON → Create**.
2. A `.json` file downloads. **Treat it like a password** — don't commit it, don't email it around.

### 5. Grant the service account read-only access in GA4

Done by whoever administers SHP's GA4 property:

1. In [analytics.google.com](https://analytics.google.com): **Admin → Property → Property access management**.
2. **+ → Add users** → paste the service-account email from step 3.
3. Role: **Viewer** (read-only). Uncheck "Notify by email". Add.

### 6. Add the key to this Claude Code environment

1. Base64-encode the downloaded key file into a single line:
   - Mac: `base64 -i ~/Downloads/YOUR-KEY-FILE.json | tr -d '\n' | pbcopy` (copies to clipboard)
   - Linux: `base64 -w0 ~/Downloads/YOUR-KEY-FILE.json`
   - (Pasting the raw JSON also works; base64 just avoids multiline/quoting issues.)
2. In Claude Code on the web ([claude.ai/code](https://claude.ai/code)): open this repo's
   **environment settings → Environment variables** and add:
   - **Name:** `GA_SERVICE_ACCOUNT_KEY_JSON`
   - **Value:** the base64 string
3. Delete the downloaded key file from your machine once it's stored in the environment settings.

### 7. Verify

Start a **new session** (existing sessions won't pick up the new variable) and ask:

> "Using the Google Analytics tools, list our GA accounts and properties."

If it returns SHP's property, then ask for a first real report — and **record the
property ID in `CLAUDE.md`** (there's a placeholder for it) so future sessions
don't have to rediscover it.

## Working locally instead (optional)

On a laptop with the [gcloud CLI](https://cloud.google.com/sdk/docs/install), you can skip the
service account entirely:

```bash
gcloud auth application-default login \
  --scopes https://www.googleapis.com/auth/analytics.readonly,https://www.googleapis.com/auth/cloud-platform
```

The launcher script detects gcloud's credentials automatically.

## Security & compliance notes

- **Read-only by design**: the MCP server only exposes reporting tools, and the
  Viewer role can't change GA4 config even if something went wrong.
- The key is stored only in the Claude Code environment settings and written at
  runtime to `~/.config/shp-ga/` (outside the repo, permissions `600`). Never
  commit a key file; `.gitignore` has guardrails, but stay alert.
- **If a key ever leaks**: in the service account's Keys tab, delete the key
  (instantly revokes it) and create a new one.
- **HIPAA reminder** (about GA itself, not this integration): GA4 data is
  aggregate web analytics and must stay that way. Per HHS/OCR guidance on
  tracking technologies, GA4 should not be collecting identifiers or capturing
  URLs/parameters that reveal patient-specific health information (e.g. on
  portal or appointment-booking pages). Reading reports here doesn't change that
  posture — but if analysis surfaces URLs containing personal info, flag it as a
  collection-configuration problem to fix.

## Troubleshooting

| Symptom | Likely cause / fix |
|---------|--------------------|
| GA tools don't appear in the session | Env var not set in environment settings, or session predates it — start a new session; check `/mcp` for the `google-analytics` server status and logs |
| Server fails to start, log says "No Google credentials found" | `GA_SERVICE_ACCOUNT_KEY_JSON` missing in this environment's settings |
| `403 PERMISSION_DENIED` on API calls | Step 5 not done (service account not added to the GA4 property), or the two APIs aren't enabled (step 2) |
| `invalid_grant` / auth errors | Key was deleted/rotated, or the pasted value got truncated — re-encode and re-paste |
| `SERVICE_DISABLED` | Enable the exact API named in the error, in the same project as the service account |
| Network errors reaching `*.googleapis.com` | The environment's network policy must allow `pypi.org` (server install) and `*.googleapis.com` (API calls) — both verified reachable in this environment as of 2026-07-22 |
