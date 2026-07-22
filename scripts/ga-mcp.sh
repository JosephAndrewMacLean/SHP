#!/usr/bin/env bash
#
# Launcher for the official Google Analytics MCP server (`analytics-mcp` on PyPI).
# Wired up via .mcp.json — Claude Code runs this automatically at session start.
#
# Credential resolution order:
#   1. GOOGLE_APPLICATION_CREDENTIALS already points at a key file → use as-is.
#   2. GA_SERVICE_ACCOUNT_KEY_JSON holds the service-account key (raw JSON or
#      base64) → write it to ~/.config/shp-ga/service-account.json and point
#      Application Default Credentials at it. This is the path used in Claude
#      Code on the web, where the key is injected as an environment variable.
#   3. A local gcloud ADC file exists (laptop use, after
#      `gcloud auth application-default login`) → the Google client libraries
#      find it on their own.
# Anything else → fail fast so the misconfiguration is visible in /mcp logs.
#
# One-time Google Cloud / GA4 setup: docs/google-analytics-mcp-setup.md

set -euo pipefail

err() { printf 'ga-mcp: %s\n' "$*" >&2; }

CRED_DIR="${HOME}/.config/shp-ga"
CRED_FILE="${CRED_DIR}/service-account.json"

if [[ -n "${GOOGLE_APPLICATION_CREDENTIALS:-}" ]]; then
  if [[ ! -f "${GOOGLE_APPLICATION_CREDENTIALS}" ]]; then
    err "GOOGLE_APPLICATION_CREDENTIALS is set but no file exists at: ${GOOGLE_APPLICATION_CREDENTIALS}"
    exit 1
  fi
elif [[ -n "${GA_SERVICE_ACCOUNT_KEY_JSON:-}" ]]; then
  umask 077
  mkdir -p "${CRED_DIR}"
  case "${GA_SERVICE_ACCOUNT_KEY_JSON}" in
    *\{*)
      printf '%s' "${GA_SERVICE_ACCOUNT_KEY_JSON}" > "${CRED_FILE}"
      ;;
    *)
      if ! printf '%s' "${GA_SERVICE_ACCOUNT_KEY_JSON}" | tr -d '[:space:]' | base64 -d > "${CRED_FILE}" 2>/dev/null; then
        err "GA_SERVICE_ACCOUNT_KEY_JSON is neither raw JSON nor valid base64."
        exit 1
      fi
      ;;
  esac
  export GOOGLE_APPLICATION_CREDENTIALS="${CRED_FILE}"
elif [[ -f "${HOME}/.config/gcloud/application_default_credentials.json" ]]; then
  : # gcloud ADC present — nothing to do
else
  err "No Google credentials found."
  err "Set the GA_SERVICE_ACCOUNT_KEY_JSON environment variable in this Claude Code"
  err "environment's settings (service-account key JSON, raw or base64-encoded),"
  err "or run 'gcloud auth application-default login' when working locally."
  err "Setup guide: docs/google-analytics-mcp-setup.md"
  exit 1
fi

# Validate the key file parses, and derive GOOGLE_PROJECT_ID from it if unset.
if [[ -n "${GOOGLE_APPLICATION_CREDENTIALS:-}" ]]; then
  project_id="$(python3 - <<'PY'
import json, os, sys
path = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
try:
    with open(path) as f:
        data = json.load(f)
except Exception as e:
    print(f"credentials file {path} is not valid JSON: {e}", file=sys.stderr)
    sys.exit(1)
print(data.get("project_id") or data.get("quota_project_id") or "")
PY
)" || { err "invalid credentials file"; exit 1; }
  if [[ -z "${GOOGLE_PROJECT_ID:-}" && -n "${project_id}" ]]; then
    export GOOGLE_PROJECT_ID="${project_id}"
  fi
fi

exec uvx analytics-mcp
