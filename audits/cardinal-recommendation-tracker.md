# Cardinal Recommendation Tracker — Website Status & Measurement

**Purpose:** one ledger answering three questions for every Cardinal (June 2026) audit
recommendation — *what did they recommend, what is the verified status on our website
today, and which instrument measures it going forward.* All opportunity work in this
workspace hangs off this document.

**Last verified: 2026-07-22** · Sources: GA4 API (property 370514163), Semrush
(project "SHP Spine 2026", Site Audit snapshot Jul 21), direct site checks (network
allowlist added 2026-07-22 — note: Cloudflare serves a bot challenge to non-browser
requests, so page-level title/meta checks still need a real-browser pass or Cardinal
confirmation), **GSC API (granted 2026-07-22 — live)**, and the audit texts in
`cardinal-2026-06/`. Instrument validation: our GSC pull of Cardinal's exact audit
window (2026-03-16→06-13) returns 13,506 clicks / 1,167,350 impressions / 1.16% CTR —
matching their reported 13,668 / 1,186,066 / 1.15%, so statuses here are measured on
the same data Cardinal used.

**Legend:** ✅ done/confirmed · 🟠 partial/in motion · ❌ not done · ❓ not verifiable
from here yet (unlock noted) · ⬜ scheduled later in Cardinal's roadmap

> **Re-check 2026-07-22 (evening) — deltas since the morning pass:**
> - ✅ **Liine → GA4 event forwarding went LIVE** (configured by Joe today, all events,
>   no filters). `Liine_*` events now flow into GA4: AIC 67 · FTIC 38 · NP_LC 19 ·
>   **NP_OB 8 (online booking — the action that was 0/non-functional at audit)** ·
>   NP_BC_or_BF 5, in the first ~day. Cardinal's #1 immediate paid item ("finalize
>   Liine scheduler tracking") is substantially delivered; booked-patient truth is
>   now queryable next to sessions/campaigns in GA4. **Next:** mark `Liine_NP_BC_or_BF`
>   and `Liine_NP_OB` as GA4 Key Events; confirm Ads-side values with Blue Ox.
> - ✅ **GBP APIs enabled** (diagnose moved SERVICE_DISABLED → RESOURCE_EXHAUSTED).
>   Pipeline now waits only on Google's access-form approval.
> - ✅ Staging still locked (HTTP 401 re-verified).
> - 🟠 **Spine hub field CLS now reads 0.10 [FAST]** — at the pass line (was 0.11 this
>   afternoon); homepage still 0.12. Field data trails ~28 days, so keep watching.
> - 🟠 Sitemap evidence improved: GSC reports **0 errors / 0 warnings**, 343 URLs
>   submitted (audit: 412 with 128 non-indexable) — cleanup has landed; Semrush still
>   flags 2 wrong entries.
> - ❌ robots.txt AI-crawler block unchanged (re-verified: ClaudeBot/GPTBot/
>   Google-Extended still disallowed; WAF 403s AI user agents incl. on /llms.txt).
> - 🚨 **REGRESSION (late evening 2026-07-22): robots.txt itself is now behind the
>   Cloudflare challenge.** All day it was openly fetchable; as of the late-evening
>   check, a plain fetch of `/robots.txt` returns the "Just a moment…" JS challenge
>   (managed challenge). Consequence: unverified crawlers and tools can no longer
>   read crawl directives at all (verified Googlebot/Bingbot are typically exempt,
>   but this can't be confirmed from here). If a Cloudflare change was just made to
>   address the AI-bot items, the toggle tightened rather than loosened —
>   **`/robots.txt` and `/llms.txt` need WAF skip rules / challenge exemption**, and
>   the security level should be checked (an "Under Attack"-style setting sweeping
>   all paths would look exactly like this).
> - No new Semrush crawl since Jul 21 (issue counts stand).

---

## 1. Headline status (what the data says today)

1. **🚨 Cardinal's #1 urgent item appears UNRESOLVED — and it's still costing us.**
   GA4 organic sessions: **Mar 6,163 → Apr 5,264 → May 3,027 → Jun 3,209 → Jul ~2,750
   (run-rate)** — the −42% May cliff lands exactly on Cardinal's documented **May 1 CWV
   regression** (238 Good URLs → 0 by May 13; LCP 3.5s; mobile score 28/100). GSC
   (granted 2026-07-22) adds search-side evidence: post-audit (Jun 14–Jul 19) vs.
   audit window, **impressions/day −27%** (12,970→9,531) and **avg position worse by
   2.4** (10.9→13.3) while CTR ticked up 1.16%→1.38% — a visibility/rankings decline,
   not a click-through problem. Most concrete casualty: **the carpal tunnel page fell
   from position 1.37 to position ~17** (impressions −92%/28d) — Cardinal's fastest
   quick-win no longer has the ranking the win depended on.
   **Definitive CWV read (PSI field data, run 2026-07-22): the LCP regression is
   FIXED — p75 now 1.36–1.57s (was 3.5s), lab 52–79/100 (was 28) — but CLS p75 is
   0.11–0.12 on every page tested, just over the 0.10 threshold, so the site still
   fails "Good" status.** The remaining blocker is Cardinal's named CLS cause (203
   images missing width/height — one template fix). Rankings haven't recovered yet;
   Google re-ranking lags CWV repair, and the AI-bot/Cloudflare posture (items 2–3)
   is a second suppressor to clear while waiting.
2. **✅✅ AI-crawler access FULLY FIXED — externally verified 2026-07-27.** End-to-end
   tests all pass: `/robots.txt` and `/llms.txt` return real content to plain fetches
   **and to AI user agents (ClaudeBot UA → 200, GPTBot UA → 200)**; content pages no
   longer challenge plain requests (homepage → 200); the directives are a clean
   WordPress-standard robots.txt with **`Content-Signal: search=yes, ai-input=yes,
   ai-train=yes, use=full`** and no AI-bot Disallow block. Cardinal's "do not block
   bots that serve live user queries" is satisfied at every layer. Claude, ChatGPT,
   Gemini, and Perplexity can now crawl, read llms.txt, and cite the site. (Note for
   leadership: the signal also *allows training use* — more permissive than Cardinal
   required; deliberate is fine, just confirm it's intended.) Sequence for the
   record: block found + flagged 2026-07-22 → directives fixed (owner-verified) →
   challenge exemptions landed → full external verification 2026-07-27. *(Dating
   note: entries above stamped "2026-07-22 evening/late evening" occurred across
   the Jul 22–26 span of this working session.)*
3. **Cloudflare's bot challenge also fronts `llms.txt`** — the file exists (a Phase-1
   ✅), but non-browser requests get a "Just a moment…" challenge page instead of its
   content, so the AI crawlers it was written for may never read it. Review the
   challenge posture (and consider a WAF skip rule for `/llms.txt` and `/robots.txt`).
   **Also check the Cloudflare audit log around May 1** — if the bot-protection or
   security level changed then, it's a candidate trigger for the CWV/organic
   regression (challenge interstitials degrade real-user LCP).
4. **Staging domain — ✅ FIXED 2026-07-22 (same day it was flagged):**
   `synergy.egowebdev.com` was publicly reachable (HTTP 200) at morning check;
   password protection went live the same day — re-verified **HTTP 401**. Cardinal's
   "password-protect immediately" item is closed.
5. **Two Phase-1 items verified DONE:** `llms.txt` is live and validly formatted
   (with the challenge caveat above), and missing meta descriptions went from 55
   (June) to **0 flagged** (Semrush Jul 21). Rank Math work is landing.
6. **Schema remains the big open item:** **446 structured-data markup errors** still
   flagged (Cardinal: Hospital @type cascade, 22–61 errors/page on 42 physician bios;
   sameAs → competitor `@mendelsonortho`). **0 FAQ rich-result keywords** in Semrush —
   unchanged from Cardinal's "zero rich results" baseline.
7. **New flags Cardinal didn't have:** 754 broken internal links, 1 malformed
   robots.txt line, 57 orphaned sitemap pages (Semrush Jul 21).
8. **Paid still carries the site:** google/cpc 4,865 sessions vs google/organic 1,666
   (last 30d). The spine hub gets 2,803 sessions/90d at 78% engagement — but only
   **52 of them arrive from organic search** (~4/week). Cardinal's "massive
   visibility, near-zero conversion" diagnosis is unchanged.

## 2. Verified snapshot — numbers to re-pull each check-in

| Metric | Cardinal baseline (Jun 2026) | Today (2026-07-22) | Instrument |
|---|---|---|---|
| Semrush Site Health | — (not in audit) | **75/100** (+2 vs Jul 16) | Semrush Site Audit, project 30453033 |
| Organic sessions/month | ~5,000+ (Mar–Apr level) | **~2,750 run-rate, falling** | GA4 `sessionDefaultChannelGroup` |
| Organic CTR (GSC) | 1.15% (target 1.8–2.2% by day 90) | **1.38%** (Jun 14–Jul 19) — but on −27% impressions/day | GSC API ✅ |
| Avg position (GSC) | 10.9 (audit window) | **13.3** — rankings sliding | GSC API ✅ |
| Carpal tunnel page | pos 1.37 · 15,605 impr/90d · 0.03% CTR | **pos ~17 · 401 impr/28d (−92%)** | GSC API ✅ |
| TKA cluster | 0.06% CTR · 15 competing pages | **0.011% CTR** (18,060 impr/28d) — no consolidation visible | GSC API ✅ |
| Branded clicks (regex synergy\|mendelson\|kornblum) | ~80% of clicks (Cardinal's broader classification) | 964 clicks · 4.69% CTR · pos 7.1 (Jun 14–Jul 19; lower-bound share ~20% of all clicks — methodology differs, use this as the like-for-like baseline going forward) | GSC API ✅ |
| Rich-result types in Search Appearance | 1 (Translated Results only) | **still only TRANSLATED_RESULT** in the Jun 14–Jul 19 performance report — **but GSC URL Inspection now detects a Breadcrumbs rich result on the spine hub (verdict PASS, 2026-07-27)**: schema is starting to register. Watch Search Appearance for Breadcrumbs to appear as impressions accrue. | GSC API ✅ |
| CWV field data (CrUX p75, mobile) | LCP **3.5s** FAIL · CLS 0.11 · lab 28/100 | **LCP 1.36–1.57s FAST** ✅ · **CLS 0.11–0.12 — still > 0.10** ❌ · INP 102–120ms FAST · overall AVERAGE · lab 52–79/100 (5 pages, run 2026-07-22 via `scripts/cwv-check.py`) | PSI API ✅ |
| Structured-data markup errors | 22–61/page on 42 bios | **446 items** | Semrush Site Audit (issue 45) |
| FAQ rich-result keywords | 0 rich results in GSC | **0** | Semrush `serp_faq_keywords` |
| Featured-snippet keywords | — | 33 | Semrush domain_rank |
| Keywords where AI Overviews appear | near-zero citations | **2,276** (exposure, not citation) | Semrush `serp_ai_overview_keywords` |
| Local-pack keywords | GBP working (1,781 clicks/90d) | 1,681 | Semrush + GA4 GBP UTMs (~770 sessions/30d) |
| Referring domains | 130 (GSC, thin) | **408** (Semrush counts wider) · AS 29 | Semrush backlinks_overview |
| Duplicate titles / dup metas / missing H1 | 5 / 86 / 14 | **5 / 7 / 21** | Semrush issues 6, 15, 103 |
| Missing meta descriptions | 55 (incl. 7 location pages) | **0 flagged** ✅ | Semrush issue 106 |
| llms.txt | absent | **live, valid** ✅ | Semrush issues 137/219 |
| Broken internal links / 4xx pages | 10 internal 4xx | **754 / 8** | Semrush issues 8, 2 |
| GA4 key events (30d) | conversion tracking "unknown" | `new_patient_intent` 3,981 · `click_to_call` 1,328 · `zocdoc handoff` 1,252 | GA4 |
| Google Ads spend visibility | agency-side only | **linked to GA4** — campaign cost/clicks queryable | GA4 (advertiser metrics) |

## 3. Organic/AIO audit — Phase 1 (Days 1–30) checklist

Cardinal's own "What success looks like at Day 30," statused:

| # | Phase-1 success criterion | Status | Evidence / unlock |
|---|---|---|---|
| 1 | CWV regression identified & fixed; Good URLs recovering | 🟠 **LCP fixed, CLS still failing** | PSI field data 2026-07-22: LCP p75 recovered to 1.36–1.57s (was 3.5s); lab 52–79/100 (was 28). **CLS p75 = 0.11–0.12 on all 5 pages — just over the 0.10 pass line — so pages still aren't "Good."** Remaining fix is Cardinal's named CLS cause: 203 images missing width/height (template change) + testimonial-slider DOM. Rankings haven't recovered yet (GSC position 13.3) — re-ranking lags; finish CLS to complete the recovery case. |
| 2 | Zero 404s + zero 301s in XML sitemap | 🟠 **trending done** | GSC (Jul 22): sitemap_index 0 errors / 0 warnings, 343 submitted (audit: 412 incl. 128 non-indexable) — cleanup landed. Semrush still flags 2 wrong entries + 8 pages 4xx. |
| 3 | Zero CSP errors; Clarity + Cloudflare data restored | ❓ | Needs page-level check (env blocks site) or ask Paul: is Clarity data flowing? |
| 4 | logo.svg <20KB; Hotjar deferred; LCP improved | ❓ | PSI API key answers all three in one call |
| 5 | Security headers on 100% of pages | ❓ | Needs direct fetch (blocked) — one `curl -I` from any laptop |
| 6 | llms.txt live at /llms.txt | 🟠 | Exists & valid (Semrush Jul 21) — but served behind a Cloudflare bot challenge to non-browser agents (verified 2026-07-22), so its audience can't read it |
| 6b | Verify AI crawler access in robots.txt ("do not block bots") | ✅ **FULLY VERIFIED 2026-07-27** | External tests: robots.txt + llms.txt serve content to AI user agents (ClaudeBot/GPTBot UA → 200); no AI Disallow entries; `Content-Signal: ai-input=yes, ai-train=yes, use=full`. **Corroborated by GSC URL Inspection (Google's own crawler, same day): homepage + spine hub both `robotsTxtState: ALLOWED`, `pageFetchState: SUCCESSFUL`, crawled 2026-07-27 04:54 and 08:17 UTC** — so Cloudflare's protections are not obstructing verified crawlers. Item closed. |
| **Measurement caveat (not a site defect)** | ⚠️ **2026-07-27 · updated 2026-08-03** | Our monitoring egress range **`160.79.106.0/24`** is now firewall-blocked by Cloudflare (Ray ID `a21bf49b0c648b8e`) after repeated bot-UA test requests tripped bot-fight scoring. Consequence: direct curl checks of the site from sessions return 403 regardless of site state — **use GSC URL Inspection / Semrush / GA4 for verification instead**, or ask Paul for a WAF Skip rule on that range to restore the tripwire. **Re-test 2026-08-03 (~18:45 UTC):** posture shifted from hard firewall denial to the **managed challenge** — plain curl now receives the "Just a moment…" interactive page (HTTP 403), real-Chromium (Playwright, via session proxy) gets a TCP connection reset, and the harness fetcher gets 403; no session-side egress denial (proxy log clean for the host). Net: sessions still cannot render the site. **Googlebot unaffected — re-verified same time:** URL Inspection shows homepage crawled successfully 2026-08-03 14:58 UTC, verdict PASS, robots ALLOWED. Standing ask for Paul: a WAF **Skip** rule (the IP range above, or a secret-header match) for verification traffic. |
| 6c | Password-protect staging domain synergy.egowebdev.com | ✅ **fixed 2026-07-22** | Was HTTP 200 at morning check; re-verified same day: **HTTP 401** (auth required) |
| 7 | Homepage meta description live | ✅ | Confirmed in audit (Rank Math) + Semrush: 0 missing sitewide |
| 8 | Carpal tunnel + TKA titles/metas rewritten | ❌ **and worse** | GSC (Jun 22–Jul 19): TKA CTR 0.011% — unchanged, rewrite not landing. Carpal tunnel: the page **lost its #1 ranking entirely** (pos ~17, impressions −92%) — rewrite is now moot until rankings recover; treat as part of the regression damage |
| 9 | Archive template duplicate titles/metas fixed | 🟠 | Dup metas 86→7; dup titles still 5 (locations-type taxonomy) |
| 10 | MedicalOrganization + Physician schema live, error-free | ❌ | 446 markup errors persist; sameAs/competitor fix unverified; GSC Enhancements needs grant |
| 11 | 75-query AIO tracking baseline established | ❓ | Ask Cardinal for the query set + baseline. Interim: Semrush AIO-keyword report + manual prompt tests. |

## 4. Phase 2–3 gates (Days 31–90) — what to check next

- ⬜ **TKA cluster consolidated** to one canonical hub (baseline: 15 pages, 30,143
  impressions, 0.06% CTR) → GSC page report + Semrush organic_research
- ⬜ **5 spine condition hubs published** (stenosis, herniated disc, sciatica, DDD,
  spondylolisthesis — all near-zero today; GA4: stenosis page = 4 visits/90d, 0%
  engagement) → GA4 landing pages + GSC non-branded impressions
- ⬜ **MedicalClinic schema fixed on 8 location pages**; unique metas (✅ metas appear
  done per Semrush) → issue-45 count should drop
- ⬜ **Southfield 9-URL consolidation** + `/full-service-clinics/` + `/shp-*` 301s →
  Semrush issue 214 / GSC pages
- 🟠 **GA4 conversion + call tracking live** → key events exist now (`new_patient_intent`,
  `click_to_call`); Liine booked-call conversions live in Google Ads (not GA4) — the
  booked-patient loop still needs Liine API/Ads visibility. (Side note: Liine's
  native GA4 forwarding could mirror call events into GA4 for analysis — optional,
  low priority; notes in `docs/liine-ga4-event-filters.md`. GA4 showed zero Liine
  events as of 2026-07-22.)
- ⬜ **FAQPage + MedicalProcedure schema; rich results appearing** → Semrush
  `serp_faq_keywords` (0 today) is the tripwire
- ⬜ **Review velocity program** → Rater8 (see data-sources roadmap) — Cardinal's
  "BirdEye/Podium" slot is filled by Rater8 in our stack
- ⬜ **First hospital-system / association link** → Semrush backlinks_refdomains
  (baseline: 0 links from Henry Ford / Corewell / McLaren / AAOS / MI Orthopedic Society)

## 5. Creative/UX audit roadmap — status

Site-page items are ❓ until the network unlock (or a manual pass); they're cheap to
eyeball from any browser. Priority lane first:

| Cardinal item (lane) | Status | Who / measure |
|---|---|---|
| Reorganize value props ("Why Synergy" too low on every page) (PRIORITY) | ❓ manual | In-house + Cardinal; before/after scroll-depth in GA4/Clarity |
| Fix compliance: WCAG contrast, overlay-widget dependence (PRIORITY) | ❓ manual | Dev; Lighthouse a11y score (87 baseline) via PSI key |
| Trust-eroding bugs: "Disgnostics" typo, dead links, PT CTA→spine, broken find-a-doctor filters, Hand&Wrist spine template copy (PRIORITY) | ❓ manual | 30-min browser pass — good clinical-stakeholder brief material |
| Expand symptom-aware content (pre-diagnosis journey) (PRIORITY) | ❌ (no such pages exist) | Content — overlaps spine hubs; in-house white space |
| Nav cleanup (300+ links, 8 panels) (MEDIUM) | ❓ manual | Cardinal/dev |
| Dedicated stripped-nav paid LPs (MEDIUM) | ❌ (paid still lands on site pages — GA4 landing paths confirm) | Cardinal paid + dev |
| Spine differentiation messaging (younger surgeons, minimally invasive, tech) (MEDIUM) | ❌ (audit: "not messaged anywhere") | In-house content — feeds paid LPs + hubs |
| Brand consistency: social/video templates, 9:16, end-card rebrand, account consolidation (MEDIUM/SMALL) | ❓ manual | In-house social/video |
| Legacy Mendelson remnants: payment.mendelsonortho.com, YouTube @mendelsonortho, LinkedIn (SMALL but E-E-A-T-critical) | ❌ assumed (YouTube sameAs error persists in schema errors) — **2026-08-03: add `michfoot.com` to the remnant list.** Owner-confirmed SHP-owned; Semrush-verified still LIVE & ranking (AS 12, 136 referring domains; its own Randy Leff bio at #2 for "randy leff dpm" — splits the provider entity; #1–3 on foot-care posts). Not a kill-it fix: page-level 301 migration + GSC change-of-address planned in `playbooks/mis-foot-surgery-leff-plan.md` §B5 (Phase 2 — after redirect targets exist) | One-time fixes; recheck schema after |

## 6. Paid media audit roadmap — status

| Cardinal item | Status | Evidence / measure |
|---|---|---|
| Finalize Liine conversion tracking (incl. scheduler/online-booking) | ✅ **major step 2026-07-22** | Liine→GA4 forwarding live (all events, unfiltered): `Liine_NP_OB` online booking **firing (8/day-one)** — was 0/non-functional at audit. Remaining: mark NP_BC_or_BF + NP_OB as GA4 Key Events; Blue Ox confirms Ads-side values. |
| GA4 key-event hygiene (supports the same recommendation) | 🟠 **Liine events marked 2026-07-22; trim recommended** | ✅ Booked-patient events are now key: **all 8 `Liine_*` events marked** (verified via Admin API; 21 key events total). Calibration to schedule: (a) **un-mark `Liine_AIC`** (all inbound calls — every call now counts as a conversion) and the **`Liine_EP_*` existing-patient family** (Cardinal: existing-patient actions are secondary — keep NP_LC/NP_BC_or_BF/NP_OB, FTIC optional); (b) the standing review of the 13 legacy intent-click key events with Blue Ox (`i_am_existing_patient_click`, `get_directions`, `email_click` first). Goal: key events ≈ new patients, not phone activity. |
| Reduce "Website – New Patient Intent" value $125→$5; recalc ROAS targets | ❓ | Ads-side setting — needs Google Ads read access (official Ads MCP) or **Blue Ox** confirmation. GA4 still shows 3,981 `new_patient_intent`/30d firing. Note: the Ads account is run by **Blue Ox Digital**, not Cardinal — Cardinal's paid audit is recommendations about Blue Ox's account. |
| Switch existing-patient conversions to Secondary | ❓ | Same — Ads-side |
| GEO/campaign consolidation decision (per-location vs shared budget vs per-service-line) | ❌ decision not visible yet | GA4 campaign names (Jul 22) still show the audited per-location structure: BOD-Ortho-Livonia, BOD-Ortho-SH, BOD-NBS-Livonia, BOD-NBS-SH, BOD-Hand-SH/Livonia, BOD-Podiatry-Southfield, BOD-Port Huron, BOD-Branded, BOD-Doctors |
| No Troy coverage; Southfield near-zero | ❌ unchanged | No Troy campaign in GA4 spend data (30d); Southfield = podiatry only |
| Ad-group buildout (Spine 4→10 groups etc.), quality score 4→up | ⬜ scheduled "Medium" | Needs Ads API/MCP for QS; interim = agency reporting |
| PMax Ortho test | ⬜ | No PMax campaign visible in GA4 campaign spend yet (30d) |
| **Spend context (GA4, last 30d)** | — | Ortho Livonia ~$73.9k · Ortho SH ~$49.5k · Spine (NBS) Livonia+SH ~$82.9k · Hand ~$13.5k · Podiatry ~$12.8k · Branded ~$3.8k · Doctors ~$4.4k |

## 7. Measurement instruments — Cardinal's recommended stack vs. ours

| Cardinal recommended | Our equivalent | Status |
|---|---|---|
| GA4 (core) | GA4 MCP | ✅ live in every session |
| GSC (core) | GSC MCP | ✅ **live** — granted 2026-07-22, instrument validated against Cardinal's own numbers |
| Semrush or Ahrefs (rank/authority/backlinks) | **Semrush MCP — already connected**, project "SHP Spine 2026" (ID 30453033) with Site Audit running | ✅ |
| CallRail or similar (call attribution) | **Liine** (live June 2026, documented API) | 🟠 API key = vendor ask |
| BirdEye/Podium/ReviewTrackers (review velocity) | **Rater8** | 🟠 vendor ask (API or scheduled export) |
| Local Falcon / BrightLocal (local grid) | none | ❌ gap — decide at Phase-2 check-in |
| Profound (AIO citation tracking) | none | ❌ gap — interim: Semrush AIO-keyword report + monthly manual prompt testing of the 75-query set (get set from Cardinal) |
| Screaming Frog monthly re-crawl | Semrush Site Audit (weekly snapshots already running) | ✅ equivalent for tracking |

**Verification unlocks — status:**
1. ✅ **Network allowlist added (2026-07-22)** — direct fetches now work at the
   curl level (this is how the robots.txt block and live staging domain were found).
   Remaining caveat: Cloudflare challenges non-browser requests for HTML pages, so
   title/meta/schema page checks need either a Cloudflare WAF exception, a manual
   browser pass, or Cardinal's confirmation.
2. 🟡 **PageSpeed Insights API key** — still needed (keyless quota is exhausted;
   verified 429 on 2026-07-22). Enable "PageSpeed Insights API" in the
   `synergy-health-partners` GCP project → Credentials → create an API key
   (restrict it to PSI) → add env var `PAGESPEED_API_KEY` in the Claude environment.
3. 🟡 **Google Business Profile APIs** — Performance API enablement started
   2026-07-22. Verified same day: the companion **My Business Account Management**
   and **My Business Business Information** APIs are NOT yet enabled in the project
   (probed: 403 SERVICE_DISABLED). All three must be enabled, then the
   [GBP API access request form](https://developers.google.com/my-business/content/prereqs#request-access)
   approves the project (quota stays 0 until approved), then a listings owner adds
   the service account as a Manager of the Business Profile account.

## 8. How to re-verify (monthly, or after any fix ships)

In a new session, ask:
> "Re-verify the Cardinal tracker: pull the Semrush Site Audit latest snapshot, domain
> SERP features, and backlinks; pull GA4 organic-by-month, key events, and campaign
> spend; pull GSC CTR/CWV if granted; update the status columns and snapshot table in
> `audits/cardinal-recommendation-tracker.md` with a new 'Last verified' date."

Statuses here are evidence-based only — where a claim can't be verified from data, it
stays ❓ rather than assumed done.
