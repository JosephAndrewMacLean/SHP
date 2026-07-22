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
| Search Console | Organic CTR (1.15%→1.8–2.2%), branded share (80%→65–70%), **CWV Good URLs (0→100+)**, rich results, non-branded growth | 🟡 **Wired — one 2-min grant pending** | trivial |
| PageSpeed API | CWV field data — the **May 1 regression tripwire** | 🟡 needs free API key | trivial |
| Liine | Cardinal's "largest unlock": qualified new-patient calls/bookings by channel | ⬜ **real API exists** | vendor ask |
| Rater8 | Review velocity program (Phase 3), per-physician/location ratings | ⬜ | vendor ask |
| Google Business Profile | Local pack visibility (target 45–50%), listing calls/directions | 🟠 partial (UTM'd clicks in GA4) | moderate (API approval) |
| Bing Webmaster Tools | Bing/Copilot visibility (feeds AEO/GEO) | ⬜ | small (API key) |
| Bing Places | listing presence only | ⬜ no API | manual |
| ZocDoc | booking-channel cost/capture (already analyzed in `brand/current-state.md`) | ⬜ no reporting API | manual export |
| Local grid (Local Falcon/BrightLocal) | local pack visibility % by geo | ❌ gap | tool decision |
| AIO citations (Profound) | AIO citation rate (target 10–15% of 75 queries) | ❌ gap — interim: Semrush AIO report + manual prompts | tool decision |

## 0. Two 5-minute environment unlocks (do these first)

1. **Network allowlist:** add `synergyhealth.org` and `synergy.egowebdev.com` to this
   Claude Code environment's network policy. Today the gateway 403s all direct fetches,
   so page-level checks (titles, schema, security headers, staging lockdown) can't run
   from sessions. This single change unlocks them.
2. **PageSpeed Insights API key** (free, [console.cloud.google.com](https://console.cloud.google.com)
   → enable "PageSpeed Insights API" → create API key; same project as the service
   account is fine). Add env var `PAGESPEED_API_KEY`. Unlocks scripted CWV field-data
   checks — the direct test of Cardinal's most urgent finding.

## 1. Google Search Console — the single highest-value connection (2 minutes)

- **Why (Cardinal):** GSC is the system of record for half their KPI table — organic
  CTR, branded/non-branded split, CWV Good URL count, Search Appearance rich results,
  striking-distance queries. It's also the fastest confirmation of whether the **May 1
  CWV regression** (GA4 shows organic down ~50% since March) is fixed or still live.
- **Verified today:** API enabled, our service account authenticates — **zero properties
  shared with it yet.**
- **The one step** (any Search Console owner): [search.google.com/search-console](https://search.google.com/search-console)
  → Settings → Users and permissions → Add user →
  `ga4-claude-readonly@synergy-health-partners.iam.gserviceaccount.com` → **Restricted** → Add.
- Already wired in `.mcp.json` → `scripts/gsc-mcp.sh` (pinned community `mcp-server-gsc@0.3.0`;
  Google ships no official GSC MCP). Start a new session after the grant.
- GSC keeps ~16 months of history; it also replaces the manual CSV exports in `seo/`
  (open PR #3 branch) with fresh pulls.

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
  — needs a developer token (MCC) + read access to the account (agency-run, per
  `brand/current-state.md`) — or ask Cardinal to confirm the settings changes in their
  reporting.

## 4. Liine — Cardinal's "largest unlock," and it has a real API

- Cardinal's conversion strategy runs entirely through Liine (lead calls, booked calls,
  online-scheduling actions with assigned values). GA4 shows the intent-level events
  (`new_patient_intent` 3,981/30d, `click_to_call` 1,328) but **booked-patient truth
  lives in Liine**.
- [api-docs.liine.com](https://api-docs.liine.com/) documents interaction/call-record
  endpoints (channel, lead status). **Ask the Liine account manager for an API key** →
  store as `LIINE_API_KEY` env var → we wire a launcher like the others.
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

## 6. Google Business Profile

- **Already partially measured:** GBP links are UTM-tagged → ~770 sessions/30d in GA4.
  ⚠️ Two casings (`GBP / Organic` and `gbp / organic`) split the data — standardize.
- **What the API adds:** on-listing behavior (search appearances, calls, direction
  requests) + programmatic reviews — the inputs to Cardinal's local-pack visibility
  target (45–50% by month 3).
- **To connect:** [Business Profile API access request](https://developers.google.com/my-business/content/prereqs)
  for our GCP project (approval takes days), then a listings manager adds the service
  account as Manager. Interim: monthly Performance export from the GBP dashboard.
- Note: Cardinal also recommends a **grid tracker** (Local Falcon/BrightLocal) for true
  local-pack visibility % — that's a separate small tool decision, not a GBP API feature.

## 7. Bing Webmaster Tools

- Small traffic (bing organic ≈ 247 sessions/30d) but **Bing's index feeds Copilot and
  ChatGPT browsing** — it punches above its weight for the AEO/GEO workstream.
- Key-based API: [Bing Webmaster](https://www.bing.com/webmasters) → Settings → API
  access → generate key → store as `BING_WEBMASTER_API_KEY` → wire a small launcher.

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
