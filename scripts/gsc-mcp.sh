#!/usr/bin/env bash
#
# Launcher for the Google Search Console MCP server (`mcp-server-gsc` on npm,
# version-pinned) — wired up via .mcp.json alongside the GA4 server.
#
# Reuses the SAME Google service account as GA4 (see scripts/ga-mcp.sh). The
# credential block is duplicated rather than shared because each MCP server
# starts in its own process and whichever launches first must be able to set
# up the credential file on its own.
#
# GSC-side requirement (one-time, ~2 minutes, done by a Search Console owner):
# add the service-account email as a user under
#   search.google.com/search-console -> Settings -> Users and permissions
# with "Restricted" (read) permission for the synergyhealth.org property.
# Details: docs/data-sources-roadmap.md

set -euo pipefail

err() { printf 'gsc-mcp: %s\n' "$*" >&2; }

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
  : # gcloud ADC present (laptop use) — nothing to do
else
  err "No Google credentials found — see docs/google-analytics-mcp-setup.md"
  exit 1
fi

exec npx -y mcp-server-gsc@0.3.0
