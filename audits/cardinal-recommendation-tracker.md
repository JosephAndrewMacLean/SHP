# Cardinal Recommendation Tracker — Website Status & Measurement

**Purpose:** one ledger answering three questions for every Cardinal (June 2026) audit
recommendation — *what did they recommend, what is the verified status on our website
today, and which instrument measures it going forward.* All opportunity work in this
workspace hangs off this document.

**Last verified: 2026-07-22** · Sources: GA4 API (property 370514163), Semrush
(project "SHP Spine 2026", Site Audit snapshot Jul 21), and the audit texts in
`cardinal-2026-06/`. Direct fetching of synergyhealth.org is **blocked by this
environment's network policy** — items needing a page-level look are marked ❓ with the
unlock listed. GSC API access is wired but awaiting the property grant.

**Legend:** ✅ done/confirmed · 🟠 partial/in motion · ❌ not done · ❓ not verifiable
from here yet (unlock noted) · ⬜ scheduled later in Cardinal's roadmap

---

## 1. Headline status (what the data says today)

1. **🚨 Cardinal's #1 urgent item appears UNRESOLVED — and it's still costing us.**
   GA4 organic sessions: **Mar 6,163 → Apr 5,264 → May 3,027 → Jun 3,209 → Jul ~2,750
   (run-rate)**. The −42% May cliff lands exactly on Cardinal's documented **May 1 CWV
   regression** (238 Good URLs → 0 by May 13; LCP 3.5s; mobile score 28/100). No
   recovery visible through Jul 21. *Caveat: correlation + seasonality possible — the
   GSC CWV report (pending grant) or a PageSpeed API key confirms in minutes.*
2. **Two Phase-1 items verified DONE:** `llms.txt` is live and validly formatted, and
   missing meta descriptions went from 55 (June) to **0 flagged** (Semrush Jul 21).
   Rank Math work is landing.
3. **Schema remains the big open item:** **446 structured-data markup errors** still
   flagged (Cardinal: Hospital @type cascade, 22–61 errors/page on 42 physician bios;
   sameAs → competitor `@mendelsonortho`). **0 FAQ rich-result keywords** in Semrush —
   unchanged from Cardinal's "zero rich results" baseline.
4. **New flags Cardinal didn't have:** 754 broken internal links, 1 malformed
   robots.txt line, 57 orphaned sitemap pages (Semrush Jul 21).
5. **Paid still carries the site:** google/cpc 4,865 sessions vs google/organic 1,666
   (last 30d). The spine hub gets 2,803 sessions/90d at 78% engagement — but only
   **52 of them arrive from organic search** (~4/week). Cardinal's "massive
   visibility, near-zero conversion" diagnosis is unchanged.

## 2. Verified snapshot — numbers to re-pull each check-in

| Metric | Cardinal baseline (Jun 2026) | Today (2026-07-22) | Instrument |
|---|---|---|---|
| Semrush Site Health | — (not in audit) | **75/100** (+2 vs Jul 16) | Semrush Site Audit, project 30453033 |
| Organic sessions/month | ~5,000+ (Mar–Apr level) | **~2,750 run-rate, falling** | GA4 `sessionDefaultChannelGroup` |
| Organic CTR (GSC) | 1.15% (target 1.8–2.2% by day 90) | ❓ pending GSC grant | GSC API |
| CWV Good URLs (mobile) | **0** since May 13 | ❓ pending GSC grant / PSI key | GSC CWV report · PSI API |
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
| 1 | CWV regression identified & fixed; Good URLs recovering | ❌ *likely not* | Organic cliff May→Jul unrecovered (GA4). Confirm: GSC grant or PSI API key. **Chase this with Cardinal/dev first.** |
| 2 | Zero 404s + zero 301s in XML sitemap | 🟠 | Semrush: 2 wrong sitemap pages + 8 pages 4xx remain (was 10+17+10) |
| 3 | Zero CSP errors; Clarity + Cloudflare data restored | ❓ | Needs page-level check (env blocks site) or ask Paul: is Clarity data flowing? |
| 4 | logo.svg <20KB; Hotjar deferred; LCP improved | ❓ | PSI API key answers all three in one call |
| 5 | Security headers on 100% of pages | ❓ | Needs direct fetch (blocked) — one `curl -I` from any laptop |
| 6 | llms.txt live at /llms.txt | ✅ | Semrush Jul 21: found, valid format. Review content quality manually. |
| 7 | Homepage meta description live | ✅ | Confirmed in audit (Rank Math) + Semrush: 0 missing sitewide |
| 8 | Carpal tunnel + TKA titles/metas rewritten | ❓ | Page-level look blocked; GSC CTR trend proves it once granted (baseline: 0.03% / 0.02% CTR) |
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
  booked-patient loop still needs Liine API/Ads visibility
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
| Finalize Liine conversion tracking (incl. scheduler/online-booking) | 🟠 | Liine live (June); GA4 shows intent events; Liine "OB" online-booking action was 0-volume in audit — confirm with Paul/Liine |
| Reduce "Website – New Patient Intent" value $125→$5; recalc ROAS targets | ❓ | Ads-side setting — needs Google Ads read access (official Ads MCP) or agency confirmation. GA4 still shows 3,981 `new_patient_intent`/30d firing. |
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
| GSC (core) | GSC MCP wired | 🟡 one 2-min grant pending (see `docs/data-sources-roadmap.md` §1) |
| Semrush or Ahrefs (rank/authority/backlinks) | **Semrush MCP — already connected**, project "SHP Spine 2026" (ID 30453033) with Site Audit running | ✅ |
| CallRail or similar (call attribution) | **Liine** (live June 2026, documented API) | 🟠 API key = vendor ask |
| BirdEye/Podium/ReviewTrackers (review velocity) | **Rater8** | 🟠 vendor ask (API or scheduled export) |
| Local Falcon / BrightLocal (local grid) | none | ❌ gap — decide at Phase-2 check-in |
| Profound (AIO citation tracking) | none | ❌ gap — interim: Semrush AIO-keyword report + monthly manual prompt testing of the 75-query set (get set from Cardinal) |
| Screaming Frog monthly re-crawl | Semrush Site Audit (weekly snapshots already running) | ✅ equivalent for tracking |

**Two 5-minute unlocks for full verification from this workspace:**
1. **Add `synergyhealth.org` (and `synergy.egowebdev.com`) to the Claude Code
   environment's network allowlist** → enables direct page/header/schema checks.
2. **Create a free PageSpeed Insights API key** and add env var `PAGESPEED_API_KEY` →
   enables scripted CWV field-data checks (the regression tripwire).

## 8. How to re-verify (monthly, or after any fix ships)

In a new session, ask:
> "Re-verify the Cardinal tracker: pull the Semrush Site Audit latest snapshot, domain
> SERP features, and backlinks; pull GA4 organic-by-month, key events, and campaign
> spend; pull GSC CTR/CWV if granted; update the status columns and snapshot table in
> `audits/cardinal-recommendation-tracker.md` with a new 'Last verified' date."

Statuses here are evidence-based only — where a claim can't be verified from data, it
stays ❓ rather than assumed done.
