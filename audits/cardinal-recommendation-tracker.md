# Cardinal Recommendation Tracker — Website Status & Measurement

**Purpose:** one ledger answering three questions for every Cardinal (June 2026) audit
recommendation — *what did they recommend, what is the verified status on our website
today, and which instrument measures it going forward.* All opportunity work in this
workspace hangs off this document.

**Last verified: 2026-08-10** · Sources: GA4 API (property 370514163), Semrush
(project "SHP Spine 2026", Site Audit snapshot **Aug 4**), **GSC API** (search
analytics + URL Inspection + sitemaps), **PSI API (field CrUX + lab, keyed —
`PAGESPEED_API_KEY` now live in the environment)**, and the audit texts in
`cardinal-2026-06/`. Direct site fetches remain unusable from this environment
(Cloudflare firewall-blocks our egress range — see the 2026-07-27 measurement
caveat below); all statuses are API-verified instead. Instrument validation: our
GSC pull of Cardinal's exact audit window (2026-03-16→06-13) returns 13,506
clicks / 1,167,350 impressions / 1.16% CTR — matching their reported 13,668 /
1,186,066 / 1.15%, so statuses here are measured on the same data Cardinal used.

**Legend:** ✅ done/confirmed · 🟠 partial/in motion · ❌ not done · ❓ not verifiable
from here yet (unlock noted) · ⬜ scheduled later in Cardinal's roadmap

> **Re-check 2026-08-10 — deltas since 2026-07-22/27 (SEO-focused pass):**
> - 📈 **The visibility slide has BOTTOMED and turned.** GSC daily impressions:
>   mid-June ~12.5k/weekday → mid-July trough ~6.8–7.4k → **first week of Aug back
>   to ~10.3k/day**. The upturn starts 2026-07-20→27 — exactly when the Cloudflare
>   challenge exemptions + robots.txt fixes landed. Clicks recovering more slowly
>   (weekly 890 → 936); GA4 organic sessions still flat at the bottom (Jul closed
>   3,025; Aug pace ~2,865). Impressions lead clicks lead sessions — watch order.
> - 🆕 **URL-architecture migration is LIVE** (the March rebuild's condition/treatment
>   post types — Cardinal's Phase-2 consolidation): old
>   `/conditions-we-treat/...carpal-tunnel-syndrome/` now **301s to
>   `/conditions/carpal-tunnel-syndrome/`, Google canonical accepted** (URL
>   Inspection 2026-08-10). Ranking equity has NOT yet transferred: new URL sits
>   pos ~16 / 197 impr/28d vs the old #1.37 / ~4,850 impr/28d at audit.
> - ✅ **All 5 spine condition hubs are PUBLISHED and indexed** under `/conditions/`
>   (stenosis, herniated disc, sciatica, DDD, spondylolisthesis — plus a bonus
>   lumbar-stenosis page): ~1,139 impr / 4 clicks / positions 13.6–21.1 over the
>   last 28d. The Phase-2 "publish" gate is met; the visibility ramp is the next gate.
> - 🟠 **TKA cluster consolidated in SERPs: 15 competing pages → 3** (hub
>   `/treatment/total-knee-arthroplasty-tka/` 9,316 impr + comprehensive guide 779 +
>   partial-knee 26). But **0 clicks on 10,121 impressions (CTR 0.00%)** — the
>   title/meta rewrite outcome still hasn't landed.
> - ❌ **Schema errors went UP: 446 → 671** (Aug 4 crawl; checks 2,367 → 3,008 — more
>   markup is being deployed, so the claim "schema was implemented" is visible in the
>   data, but it's failing validation). Issue-45 sample: **every error points at the
>   same `@graph` node (`/@graph/0`)** — one template-level block erroring sitewide;
>   one fix should clear hundreds. Search Appearance still shows **TRANSLATED_RESULT
>   only** — zero FAQ/Breadcrumb rich-result impressions.
> - 🟠 **CWV: LCP fix holding (p75 1.26–1.30s FAST everywhere); CLS still the blocker
>   at 0.12 on 4/5 pages — but the spine hub now PASSES at 0.10** (PSI field,
>   2026-08-10). Lab CLS is near-zero (0–0.032), so current templates look clean;
>   field is a trailing 28-day window — if the image width/height fix shipped, field
>   should follow. Verify with Paul whether it actually shipped.
> - Sitemap: **334 submitted, 0 errors / 0 warnings** (GSC) — down from 343, clean.
>   On-page cleanup continues: dup titles 5→2, dup metas 7→4, missing H1 21→20,
>   missing meta descriptions 0 holds. Site Health 75 (flat). Broken internal links
>   754→775 and 4xx 8→9, but link checks nearly doubled (47.5k→83.3k) — likely crawl
>   scope, re-read next snapshot. Orphaned sitemap pages 57→53.
> - Backlinks flat: AS 29→30, refdomains ~398. Hospital/association link gate unstarted.
> - **Owner context (2026-08-10 leadership sync, Gautam/Joe):** strategy framed as
>   L1 condition content + schema ("finish keyword expansion — the foundation"),
>   L2 physician-specific differentiation (procedure-mix data pull w/ Santosh →
>   "famous for" positioning per surgeon), L3 asset assembly (spine-institute
>   proof points). Asks: exemplar sites from Cardinal's SEO lead of pillar/schema
>   ecosystems done well, and a progress-measurement view (this tracker + the
>   instruments below are that view).
>
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

1. **📈 UPDATE 2026-08-10: the decline has bottomed and visibility is recovering —
   sessions haven't followed yet.** The full arc: GA4 organic sessions **Mar 6,163 →
   Apr 5,264 → May 3,027 → Jun 3,209 → Jul 3,025 → Aug ~2,865 pace** (flat at the
   bottom). But GSC daily impressions show a V: mid-June ~12.5k/weekday → mid-July
   trough ~6.8–7.4k → **~10.3k/day first week of Aug**, with the turn starting
   2026-07-20→27, right at the Cloudflare/robots fixes. 28d-vs-28d averages still
   read negative (impressions −12%, avg position 13.2→14.5) because the window
   straddles the trough — the daily curve is the truthful read. Two causes are now
   separable: (a) the May 1 CWV regression — **LCP fixed and holding (p75
   1.26–1.30s), CLS still failing at 0.12 on 4/5 pages (spine hub now passes at
   0.10)**; (b) a **URL-architecture migration** (March rebuild's `/conditions/`–
   `/treatment/` post types) that 301'd legacy URLs — e.g. the carpal tunnel page's
   old #1-ranked URL redirects to `/conditions/carpal-tunnel-syndrome/` (canonical
   accepted), which sits at pos ~16 with the ranking equity not yet transferred.
   Recovery case = finish CLS + let the migration settle + keep crawler access clean.
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
6. **Schema remains the big open item — and errors are UP: 446 → 671** (Aug 4 crawl).
   Checks grew 2,367→3,008, i.e. **more markup is being deployed** (consistent with
   Paul's "top 10 implemented" report), but it's failing validation. The issue-45
   sample shows **every error pointing at the same `/@graph/0` node** — a single
   template-level block (Cardinal's Hospital @type cascade) erroring on every page
   that carries it, so **one template fix should clear hundreds at once**. Outcome
   metric unchanged: **zero rich results** — GSC Search Appearance (Jul 13–Aug 9)
   still shows TRANSLATED_RESULT only.
7. **New flags Cardinal didn't have:** 775 broken internal links (754 on Jul 21;
   link-check scope nearly doubled between crawls, so treat the delta as noise until
   the next snapshot), 9 pages 4xx, 53 orphaned sitemap pages (Semrush Aug 4).
8. **Paid still carries the site:** google/cpc 4,865 sessions vs google/organic 1,666
   (last 30d). The spine hub gets 2,803 sessions/90d at 78% engagement — but only
   **52 of them arrive from organic search** (~4/week). Cardinal's "massive
   visibility, near-zero conversion" diagnosis is unchanged.

## 2. Verified snapshot — numbers to re-pull each check-in

| Metric | Cardinal baseline (Jun 2026) | Today (2026-08-10) | Instrument |
|---|---|---|---|
| Semrush Site Health | — (not in audit) | **75/100** (flat since Jul 21; errors −28 vs Jul 28) | Semrush Site Audit, project 30453033 |
| Organic sessions/month | ~5,000+ (Mar–Apr level) | **Jul closed 3,025 · Aug pace ~2,865 — flat at the bottom, no longer falling** | GA4 `sessionDefaultChannelGroup` |
| Organic CTR (GSC) | 1.15% (target 1.8–2.2% by day 90) | **1.49%** (Jul 13–Aug 9) | GSC API ✅ |
| Impressions/day (GSC) | 12,970 (audit window) | 28d avg 8,923, **but V-shaped: mid-Jul trough ~6.8–7.4k → ~10.3k first week of Aug** — recovering since the Jul 20–27 Cloudflare/robots fixes | GSC API ✅ |
| Avg position (GSC) | 10.9 (audit window) | **14.5** (28d avg — straddles the trough; daily reads improving post-Jul 27) | GSC API ✅ |
| Carpal tunnel page | pos 1.37 · 15,605 impr/90d · 0.03% CTR | **old URL 301s → `/conditions/carpal-tunnel-syndrome/` (canonical accepted); new URL pos 16.3 · 197 impr/28d · 0 clicks** — equity not yet transferred | GSC API + URL Inspection ✅ |
| TKA cluster | 0.06% CTR · 15 competing pages | **Consolidated to 3 URLs in SERPs** ✅ · but **0 clicks on 10,121 impr/28d (0.00% CTR)** ❌ | GSC API ✅ |
| 5 spine condition hubs | near-zero presence | **All 5 published + indexed under `/conditions/`** (+ lumbar-stenosis): 1,139 impr · 4 clicks · pos 13.6–21.1 (28d) | GSC API ✅ |
| Branded vs non-branded clicks | ~80% of clicks branded | **80.5% branded** (3,003 of 3,729); non-branded: 726 clicks · 0.63% CTR · pos 21.3 (Jul 13–Aug 9) — Cardinal's core diagnosis unchanged | GSC API ✅ |
| Rich-result types in Search Appearance | 1 (Translated Results only) | **still only TRANSLATED_RESULT** (Jul 13–Aug 9; 5 clicks / 2,090 impr). Breadcrumbs detected via URL Inspection on spine hub (2026-07-27) but not yet appearing in Search Appearance | GSC API ✅ |
| CWV field data (CrUX p75, mobile) | LCP **3.5s** FAIL · CLS 0.11 · lab 28/100 | **LCP 1.26–1.30s FAST** ✅ · **CLS 0.12 on 4/5 pages ❌ — spine hub now PASSES at 0.10** ✅ · INP FAST · overall AVERAGE · lab 60–76/100 · lab CLS ~0 (templates look clean; field trails 28d) (run 2026-08-10 via `scripts/cwv-check.py`) | PSI API ✅ (keyed) |
| Structured-data markup errors | 22–61/page on 42 bios | **671 items (was 446)** — checks 2,367→3,008 (markup expanding, single `/@graph/0` template node failing sitewide) | Semrush Site Audit (issue 45) |
| FAQ rich-result impressions | 0 rich results in GSC | **0** (no FAQ/Breadcrumb rows in Search Appearance, Jul 13–Aug 9) | GSC searchAppearance ✅ |
| Featured-snippet keywords | — | 33 (as of 07-22; not re-pulled 08-10) | Semrush domain_rank |
| Keywords where AI Overviews appear | near-zero citations | 2,276 (as of 07-22; not re-pulled 08-10) | Semrush `serp_ai_overview_keywords` |
| Local-pack keywords | GBP working (1,781 clicks/90d) | 1,681 (as of 07-22; not re-pulled 08-10) | Semrush + GA4 GBP UTMs |
| Referring domains | 130 (GSC, thin) | **398 · AS 30** (was 408 · AS 29 — flat; recount noise) | Semrush backlinks_overview |
| Duplicate titles / dup metas / missing H1 | 5 / 86 / 14 | **2 / 4 / 20** — steady cleanup | Semrush issues 6, 15, 103 |
| Missing meta descriptions | 55 (incl. 7 location pages) | **0 flagged** ✅ holds | Semrush issue 106 |
| llms.txt | absent | **live, valid** ✅ (externally verified 07-27; egress still blocked for re-check, no contrary signal) | Semrush issues 137/219 |
| Broken internal links / 4xx pages | 10 internal 4xx | **775 / 9** (link checks ~doubled between crawls — delta likely scope noise) | Semrush issues 8, 2 |
| XML sitemap | 412 URLs, 128 non-indexable | **334 submitted · 0 errors · 0 warnings** | GSC sitemaps ✅ |
| GA4 key events (30d) | conversion tracking "unknown" | not re-pulled this pass (SEO-focused; see 07-22 values + §6) | GA4 |
| Google Ads spend visibility | agency-side only | **linked to GA4** — campaign cost/clicks queryable | GA4 (advertiser metrics) |

## 3. Organic/AIO audit — Phase 1 (Days 1–30) checklist

Cardinal's own "What success looks like at Day 30," statused:

| # | Phase-1 success criterion | Status | Evidence / unlock |
|---|---|---|---|
| 1 | CWV regression identified & fixed; Good URLs recovering | 🟠 **LCP fixed & holding; CLS the last blocker — first page now passes** | PSI field 2026-08-10: LCP p75 1.26–1.30s FAST on all 5 pages; lab 60–76/100. **CLS p75 = 0.12 on 4/5 pages; the spine hub now PASSES at 0.10.** Lab CLS ≈ 0 on every page — current templates look clean, and field data trails ~28 days, so if the width/height fix shipped the rest should follow within weeks. Confirm with Paul it actually shipped, then watch field CLS cross 0.10. Impressions recovering since Jul 20–27 (see headline 1). |
| 2 | Zero 404s + zero 301s in XML sitemap | 🟠 **trending done** | GSC (Aug 10): sitemap_index **0 errors / 0 warnings, 334 submitted** (Jul 22: 343; audit: 412 incl. 128 non-indexable) — cleanup continues. Semrush (Aug 4) still flags 9 pages 4xx + 2 sitemap-format entries. |
| 3 | Zero CSP errors; Clarity + Cloudflare data restored | ❓ | Needs page-level check (env blocks site) or ask Paul: is Clarity data flowing? |
| 4 | logo.svg <20KB; Hotjar deferred; LCP improved | ❓ | PSI API key answers all three in one call |
| 5 | Security headers on 100% of pages | ❓ | Needs direct fetch (blocked) — one `curl -I` from any laptop |
| 6 | llms.txt live at /llms.txt | 🟠 | Exists & valid (Semrush Jul 21) — but served behind a Cloudflare bot challenge to non-browser agents (verified 2026-07-22), so its audience can't read it |
| 6b | Verify AI crawler access in robots.txt ("do not block bots") | ✅ **FULLY VERIFIED 2026-07-27** | External tests: robots.txt + llms.txt serve content to AI user agents (ClaudeBot/GPTBot UA → 200); no AI Disallow entries; `Content-Signal: ai-input=yes, ai-train=yes, use=full`. **Corroborated by GSC URL Inspection (Google's own crawler, same day): homepage + spine hub both `robotsTxtState: ALLOWED`, `pageFetchState: SUCCESSFUL`, crawled 2026-07-27 04:54 and 08:17 UTC** — so Cloudflare's protections are not obstructing verified crawlers. Item closed. |
| **Measurement caveat (not a site defect)** | ⚠️ **2026-07-27** | Our monitoring egress range **`160.79.106.0/24`** is now firewall-blocked by Cloudflare (Ray ID `a21bf49b0c648b8e`) after repeated bot-UA test requests tripped bot-fight scoring. Consequence: direct curl checks of the site from sessions return 403 regardless of site state — **use GSC URL Inspection / Semrush / GA4 for verification instead**, or ask Paul for a WAF Skip rule on that range to restore the tripwire. |
| 6c | Password-protect staging domain synergy.egowebdev.com | ✅ **fixed 2026-07-22** | Was HTTP 200 at morning check; re-verified same day: **HTTP 401** (auth required) |
| 7 | Homepage meta description live | ✅ | Confirmed in audit (Rank Math) + Semrush: 0 missing sitewide |
| 8 | Carpal tunnel + TKA titles/metas rewritten | ❌ **outcome still absent — now reframed by the URL migration** | GSC (Jul 13–Aug 9): TKA cluster **consolidated 15→3 URLs** (a real Phase-2 win) but **0 clicks on 10,121 impressions — 0.00% CTR** at pos 9.3: whatever title/meta is live isn't earning clicks; re-do against Cardinal's formulas. Carpal tunnel: old #1 URL **301s to `/conditions/carpal-tunnel-syndrome/`** (canonical accepted 2026-08-10); new URL pos ~16, 197 impr/28d — rewrite matters again once equity transfers; strengthen internal links to the new URL now. |
| 9 | Archive template duplicate titles/metas fixed | 🟠 **nearly done** | Dup metas 86→7→**4**; dup titles 5→**2** (Aug 4 crawl) |
| 10 | MedicalOrganization + Physician schema live, error-free | 🟠 **deployed in part, not validating — deep-dive 2026-08-10** | GSC URL Inspection (5 page types): **BreadcrumbList valid + detected sitewide (PASS)** ✅; **Review-snippet markup NEW since audit** — a "Synergy Health" rated entity on every page type + "Scott McCarty, MD" on his bio, so physician-entity work has visibly started ✅. But: **671 Semrush markup errors (was 446)**, every sampled error = the same `/@graph/0` sitewide template node (the org entity — where Cardinal located the Hospital @type cascade + sameAs errors) → one template fix clears the bulk. **FAQPage: not detected** on the tested condition (stenosis) or treatment (TKA) pages — Cardinal spec item, unstarted. **⚠️ New flag: sitewide org-level aggregateRating is "self-serving" per Google review-snippet policy (won't ever show stars) and needs a verifiable review-data source (FTC/healthcare substantiation)** — likely the very node erroring. Outcome gate unchanged: Search Appearance = TRANSLATED_RESULT only. sameAs fix (@mendelsonortho / /company/mkoss/) still unverified — needs view-source or Cardinal confirmation. Next Semrush crawl ~Aug 11 = first re-test after any fix. |
| 11 | 75-query AIO tracking baseline established | ❓ | Ask Cardinal for the query set + baseline. Interim: Semrush AIO-keyword report + manual prompt tests. |

## 4. Phase 2–3 gates (Days 31–90) — what to check next

- 🟠 **TKA cluster consolidated** to one canonical hub (baseline: 15 pages, 30,143
  impressions, 0.06% CTR) → **✅ consolidation live as of Aug 10: 3 URLs in SERPs,
  with `/treatment/total-knee-arthroplasty-tka/` the clear canonical (9.3k of 10.1k
  impr)**. Remaining gate: clicks (0 in last 28d) — title/meta + snippet work.
- 🟠 **5 spine condition hubs published** (stenosis, herniated disc, sciatica, DDD,
  spondylolisthesis) → **✅ ALL 5 PUBLISHED + indexed under `/conditions/` (verified
  2026-08-10; + a lumbar-stenosis page)**. Early visibility only: 1,139 impr /
  4 clicks / pos 13.6–21.1 per 28d. Next gates: non-branded impression growth,
  positions <10, GA4 engaged sessions, physician review + FAQPage schema on each.
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
| Legacy Mendelson remnants: payment.mendelsonortho.com, YouTube @mendelsonortho, LinkedIn (SMALL but E-E-A-T-critical) | ❌ assumed (YouTube sameAs error persists in schema errors) | One-time fixes; recheck schema after |

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
2. ✅ **PageSpeed Insights API key — LIVE** (verified 2026-08-10: `PAGESPEED_API_KEY`
   present in the environment; `scripts/cwv-check.py` ran keyed against all 5 pages).
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
