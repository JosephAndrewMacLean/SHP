# Data Sources Roadmap — measuring the site against Cardinal's recommendations

**Anchor:** every data source here exists to measure the **Cardinal (June 2026) audit
recommendations** — the status ledger lives in `audits/cardinal-recommendation-tracker.md`.
Cardinal's own measurement framework (Organic audit, Section 7) calls for: GSC + GA4 as
core, rank/backlink tracking (Semrush/Ahrefs), call attribution (CallRail "or similar" —
ours is **Liine**), review velocity (BirdEye "or similar" — ours is **Rater8**), local
grid tracking, and AIO citation tracking. This doc maps that stack onto what we actually
have and what it takes to connect the rest.

Status as verified **2026-07-22**. The GA4 pattern (read-only service account → env var →
MCP in `.mcp.json`) is the template.

**The shared Google credential:**
`ga4-claude-readonly@synergy-health-partners.iam.gserviceaccount.com`
(GCP project `synergy-health-partners`), stored in the Claude Code environment settings.
Google sources reuse it; each just needs the account granted access on that product.

## At a glance

| Source | Cardinal KPI(s) it measures | Status | Effort |
|---|---|---|---|
| GA4 | Organic consultation requests, conversion events, channel mix, engagement | ✅ **Live** | done |
| Semrush MCP | Site health, schema errors, rich-result/AIO exposure, backlinks, rankings | ✅ **Live** (project "SHP Spine 2026", ID 30453033) | done |
| Google Ads (via GA4 link) | Campaign spend/clicks vs sessions (paid roadmap context) | ✅ **Live** campaign-level | done |
| Search Console | Organic CTR (1.15%→1.8–2.2%), branded share (80%→65–70%), rich results, non-branded growth | ✅ **Live** (granted 2026-07-22) | done |
| PageSpeed API | CWV field data — the **May 1 regression tripwire** | 🟡 key added 2026-07-22 — available to sessions started after that | verify next session |
| Liine | Cardinal's "largest unlock": qualified new-patient calls/bookings by channel | 🟡 **official Liine MCP exists** — allowlist + credentials pending | small |
| Rater8 | Review velocity program (Phase 3), per-physician/location ratings | ⬜ | vendor ask |
| Google Business Profile | Local pack visibility (target 45–50%), listing calls/directions | 🟡 **MCP wired** (`scripts/gbp-mcp.py` + `gbp_diagnose`) — API approval pipeline pending | approval wait |
| Bing Webmaster Tools | Bing/Copilot visibility (feeds AEO/GEO) | 🟡 **MCP wired + key stored 2026-07-22** — verify in a new session (`query_stats`), then mark ✅ | verify next session |
| Bing Places | listing presence only | ⬜ no API | manual |
| ZocDoc | booking-channel cost/capture (already analyzed in `brand/current-state.md`) | ⬜ no reporting API | manual export |
| Local grid (Local Falcon/BrightLocal) | local pack visibility % by geo | ❌ gap | tool decision |
| AIO citations (Profound) | AIO citation rate (target 10–15% of 75 queries) | ❌ gap — interim: Semrush AIO report + manual prompts | tool decision |

## 0. Environment unlocks — ✅ both done 2026-07-22

1. ✅ **Network allowlist** — `synergyhealth.org` added; direct fetches work (caveat:
   Cloudflare bot-challenges non-browser requests for HTML pages, so page-level
   title/schema checks still need a browser pass or a Cloudflare WAF exception).
2. ✅ **PageSpeed Insights API key** — stored as `PAGESPEED_API_KEY`. Environment
   variables load at session start, so use it from any session started after
   2026-07-22: it unlocks scripted CWV field-data checks (the regression tripwire).

## 1. Google Search Console — ✅ LIVE (granted 2026-07-22)

- The service account was granted Restricted access on 2026-07-22; tools appear as
  `mcp__google-search-console__*` (`search_analytics`, `list_sitemaps`,
  `index_inspect`, `detect_quick_wins`, …) via `.mcp.json` → `scripts/gsc-mcp.sh`
  (pinned community `mcp-server-gsc@0.3.0`).
- **Instrument validated:** pulling Cardinal's exact audit window (2026-03-16→06-13)
  returns 13,506 clicks / 1,167,350 impressions / 1.16% CTR vs. their reported
  13,668 / 1,186,066 / 1.15% — same data, so tracker statuses are like-for-like.
- This is the system of record for Cardinal's CTR, branded-share, rich-results, and
  striking-distance KPIs. GSC keeps ~16 months of history and replaces the manual CSV
  exports in `seo/` (open PR #3 branch).

## 2. Semrush — already connected, use it every check-in

- **Covers Cardinal's "Semrush or Ahrefs" slot** (rank tracking, topical authority
  trend, backlink monitoring) **plus** their "Screaming Frog monthly re-crawl" slot via
  Site Audit (weekly snapshots already running: health 75/100 on Jul 21).
- Project: **"SHP Spine 2026"** (ID 30453033), tools: siteaudit, backlinkAudit, gat.
- Highest-value reports for the tracker: `snapshot` (site health + issue counts —
  issue 45 = structured-data errors, the schema-fix tripwire), `domain_rank` with SERP
  feature columns (`serp_faq_keywords` = rich-results tripwire, currently 0;
  `serp_ai_overview_keywords` = AIO exposure, currently 2,276), `backlinks_overview`
  (AS 29, 408 ref domains), `backlinks_refdomains` (watch for first hospital-system /
  association links — currently zero).

## 3. Google Ads — campaign-level is live; settings-level needs access

- **Verified today:** Ads is linked to GA4 — campaign cost/clicks/sessions queryable
  (e.g. last 30d: Ortho Livonia ~$73.9k, Spine Livonia+SH ~$82.9k). Good enough to
  track the paid roadmap's *structure* (GEO consolidation, Troy coverage, PMax launch —
  all visible as campaign names/spend).
- **Not visible via GA4:** conversion-action values (the $125→$5 "New Patient Intent"
  fix), quality scores, ad strength, search terms. For those: Google now ships an
  [official read-only Google Ads MCP](https://ads-developers.googleblog.com/2025/10/open-source-google-ads-api-mcp-server.html)
  — needs a developer token (MCC) + read access to the account (run by **Blue Ox
  Digital** — Shaun Elley / Jake; corrected 2026-07-22) — or ask Blue Ox to confirm
  settings changes in their reporting.

## 4. Liine — Cardinal's "largest unlock," and it ships an OFFICIAL MCP

- Cardinal's conversion strategy runs entirely through Liine (lead calls, booked calls,
  online-scheduling actions with assigned values). GA4 shows the intent-level events
  (`new_patient_intent` 3,981/30d, `click_to_call` 1,328) but **booked-patient truth
  lives in Liine**.
- **Liine publishes an official MCP** — user guide:
  [help.liine.com/en/articles/15627134-liine-mcp-user-guide](https://help.liine.com/en/articles/15627134-liine-mcp-user-guide)
  (surfaced 2026-07-22; the guide isn't fetchable from this environment yet — the
  domain is outside the network allowlist).
- **To connect:** (1) ✅ `liine.com` domains allowlisted 2026-07-22; (2) ⚠️ the guide
  article turned out to be **behind Liine's customer login** (help center returns 401
  anonymously) — someone with a Liine login must open it and copy the setup section
  (MCP endpoint/command + credential instructions) into the workspace; (3) then wire
  per the guide (remote MCP or `.mcp.json` entry). Their
  [API docs](https://api-docs.liine.com/) remain the fallback.
- ⚠️ **PHI:** Liine records patient calls. Only de-identified aggregates enter this
  repo (counts, rates, channels) — same standard as `pm/spine-imaging-pain-call-review-pack.md`.
  No transcripts, names, numbers.

## 5. Rater8 — fills Cardinal's "review velocity" slot

- Cardinal Phase 3 calls for a review-velocity program tracked in "BirdEye, Podium, or
  ReviewTrackers" — our stack already has **Rater8** (named data feed D8 in the routing
  process on the open PR #2 branch).
- rater8 has a client-facing API (per their [terms](https://rater8.com/terms-and-conditions/))
  and exportable reports, but no self-serve developer portal → **ask our rater8 rep**
  for API access or a scheduled weekly CSV (reviews by physician/location) into the
  drop folder (§9).
- ⚠️ Raw review text can contain patient-written health details — aggregates only.

## 6. Google Business Profile — MCP wired, approval pipeline pending

- **MCP server is live in `.mcp.json`** (`scripts/gbp-mcp.py`): `gbp_diagnose` (reports
  the access-pipeline state — run it whenever something errors), `list_accounts`,
  `list_locations`, `performance_daily` (calls/website clicks/directions/impressions
  per location), `search_keywords` (what people searched to find each listing),
  `list_reviews`. Uses the shared service account.
- **Remaining pipeline (re-verified 2026-07-22, evening):**
  1. ❌ **Still pending:** enable the two companion APIs in the GCP project —
     [My Business Account Management](https://console.developers.google.com/apis/api/mybusinessaccountmanagement.googleapis.com/overview?project=156236120118)
     and
     [My Business Business Information](https://console.developers.google.com/apis/api/mybusinessbusinessinformation.googleapis.com/overview?project=156236120118)
     (confirm Business Profile Performance is enabled too). `gbp_diagnose` still
     returns SERVICE_DISABLED for Account Management.
  2. ❌ Submit the [GBP access request form](https://developers.google.com/my-business/content/prereqs#request-access)
     — quota stays 0 until Google approves (days).
  3. ✅ **Done 2026-07-22:** the service account was added to the Business Profile
     (per Joe). Once steps 1–2 land, `gbp_diagnose` should flip straight to
     "Access WORKS."
- **Already partially measured meanwhile:** GBP links are UTM-tagged → ~770
  sessions/30d in GA4. ⚠️ Two casings (`GBP / Organic` / `gbp / organic`) split the
  data — standardize.
- Note: Cardinal also recommends a **grid tracker** (Local Falcon/BrightLocal) for true
  local-pack visibility % — separate small tool decision, not a GBP API feature.

## 7. Bing Webmaster Tools — MCP wired, key pending

- **MCP server is live in `.mcp.json`** (`scripts/bing-wmt-mcp.py`): `query_stats`,
  `page_stats`, `rank_and_traffic_stats`, `crawl_stats`, `url_submission_quota`.
- **Status 2026-07-22:** `BING_WEBMASTER_API_KEY` added to the environment settings
  by Joe. ⚠️ **Blocker found same day: the API host `ssl.bing.com` is not in the
  environment's network allowlist** (proxy 403 on connect) — add `bing.com` and
  `*.bing.com` to the allowlist (applies live). Then verify with `query_stats` (or
  `uv run scripts/bing-wmt-mcp.py --selftest`) and flip this to ✅.
- Small direct traffic (bing organic ≈ 247 sessions/30d) but **Bing's index feeds
  Copilot and ChatGPT search** — it punches above its weight for AEO/GEO.

## 8. Bing Places & ZocDoc — no clean APIs; treat as manual

- **Bing Places:** no stats API. Keep the listing synced from GBP; spot-check quarterly.
- **ZocDoc:** official API is booking-partner integration, not practice reporting.
  Monthly dashboard export into the drop folder. Context: the Zocdoc cost/capture
  analysis in `brand/current-state.md` already concluded spend should shift toward the
  website booking path — ZocDoc data mainly needs to confirm that shift.

## 9. Interim standard for anything not yet API-connected

Drop scheduled/manual exports into **`data/<source>/<YYYY-MM-DD>/`** (e.g.
`data/rater8/2026-08-01/reviews-by-physician.csv`) with a README noting export
settings. Sessions analyze CSVs immediately; when a source graduates to an API, its
folder becomes archive.

## Data-hygiene flags (fix at the source)

1. **`(not set)` landing page** — 1,310 sessions/90d at 3.6% engagement: tagging gap;
   ~6% of traffic measured badly. (Also relevant: Cardinal found the site's CSP was
   blocking Clarity/Cloudflare analytics — same "we're blinding ourselves" family.)
2. **GBP UTM casing** — `GBP / Organic` vs `gbp / organic` splits reporting.

## Security & compliance

Read-only credentials only, stored in Claude Code environment settings (never in the
repo — `.gitignore` guards key files). Aggregate marketing data only; any source
touching patient interactions (Liine, Rater8, ZocDoc) enters the repo **de-identified
or not at all** (HIPAA). GA4 itself must not collect patient-identifying URLs — flag
any found during analysis as a collection-configuration problem.
