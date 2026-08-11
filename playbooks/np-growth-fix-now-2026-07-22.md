# New-Patient Growth — Fix-Now Matrix (refreshed 2026-07-22)

**Owner:** Joe · **Scope:** only areas Joe's remit now controls — marketing, call center
(Kelly → Joe since Jul 8), PL team via Kristen, website via Paul, tracking via Santosh —
mapped on effort/impact with an explicit **ASAP list**.

**What this refresh adds** over `ideas-bank-impact-effort.md` (authored ~Jul 16):
1. **Verified site status 7/22** (PSI field data, Semrush Jul 21, direct fetches): the LCP
   regression is FIXED; **CLS 0.11–0.12 is the one remaining CWV blocker**; Cloudflare is
   blocking AI retrieval bots and challenging `llms.txt`; staging lockdown is DONE ✅.
2. **Jun 1 – Jul 21 leadership transcripts** (Otter + Notion): the Zocdoc→Liine→Google Ads
   **conversion-signal break is the CEO-named root cause** of the spine B2C decline
   (stabilize-by-**Aug 15** directive); call-center abandonment ran **23% vs a 5–6% target**
   ("when that happens, he loses half of his new patients"); the June B2B numbers that drove
   two weeks of decisions were a **dashboard error (237 shown vs 284 actual)**; spine ad
   campaigns underperform partly from **too little conversion data per campaign → consolidate**.
3. **Leadership's sequencing rules, on the record:** no bidding changes until Liine tracking
   works · stay in "box one" ~30 days · **do not touch ortho** ("don't change anything, you're
   doing a great job") · prove-it culture — a standard exists only once hit repeatedly.

**Ordering logic:** (1) fix instruments before moving spend — leadership's own rule;
(2) convert demand that already exists ($0) before buying more; (3) unblock organic-ranking
recovery immediately — Google re-ranking lags the fix by weeks, so every week of delay pushes
recovery past Gate 1 (Aug 30, spine ≥65/wk); (4) then compound with content/authority big bets.

---

## ⚡ ASAP — implement this week (Jul 22–31)

High impact, low-to-medium effort, unblocked, and each is either a leadership deadline, a
gate blocker, or free conversion of existing demand. In priority order:

| # | Fix | Owner | Impact | Effort | Evidence / why now | Done when |
|---|---|---|---|---|---|---|
| 1 | **Ship the CLS template fix** (203 images missing width/height; trim testimonial-slider DOM) | Paul | Very High | Low | Only remaining CWV blocker (CLS 0.11–0.12 vs 0.10; LCP already 1.36–1.57s). May–Jul failing period cost ~half of organic sessions; rankings (avg pos 10.9→13.3) can't recover until pages flip Good | `scripts/cwv-check.py` shows CLS <0.10 on key pages |
| 2 | **Repair the Liine→Google Ads conversion signal** (incl. Zocdoc leg; resolve the compliance blocker) | Santosh + Paul + Joe (Blue Ox executes) | Very High | Med | CEO-named root cause of spine B2C decline; CPA history $200→$2,000 on broken tracking; **blocks every paid decision**; CEO deadline: funnel stable by **Aug 15**; Zocdoc's own ETA (end-Aug) already rejected | Qualified-lead conversions verified flowing into Google Ads; spot-checked against Liine |
| 3 | **Cloudflare: unblock AI retrieval bots + WAF skip for `/llms.txt` & `/robots.txt`; pull Apr 25–May 3 audit log** | Paul | High | Trivial | Managed robots.txt blocks GPTBot/ClaudeBot/Google-Extended — defeats the whole AIO/GEO program; audit log may identify the May 1 regression trigger | Direct non-browser fetch returns llms.txt; retrieval bots allowed; log reviewed |
| 4 | **Call-center conversion pack:** qualify→route→capture script, insurance pre-screen, mandatory "how did you hear," abandonment SLA 23%→≤6% with callback | Kelly (directed by Joe) | Very High | Low-Med | Abandonment 23% vs 5–6% target; source captured only 60–70%; converts existing demand at $0 — plan lever A/D (+3–5/wk alone) | Script live; source a required field; abandonment on the Friday scorecard |
| 5 | **Fix the B2B dashboard (237 vs 284) + start the NextGen↔MMC crosswalk** | Joe + Santosh | High | Low-Med | The error drove two weeks of wrong leadership reads in July; prove-it culture needs trusted numbers before the Sept 30 board decision | Dashboard reconciles to Kristen's records for June; crosswalk spec agreed |
| 6 | **Load + tier the spine target-account list (0 → full) and redistribute by territory** | Kristen (Joe's Jul 21 tool) | High | Low | List is EMPTY today; doubling accounts is Kristen's assigned Jul 15 action; referral goal 79→110/mo by Oct; tiering model already proven internally (attorney list) | Tiered list distributed; account counts on scorecard |
| 7 | **Recover Sean's lost referral accounts** | Kristen | Med | Low | ~2–3 spine NP/week walked out with him — fastest referral win | Accounts visited; referral flow restarted |
| 8 | **Work the 166 self-reschedulers as a daily re-book queue** | Kelly | Med | Low | 166 canceled/no-show patients later self-booked online and KEPT — pure recapture + access-friction signal | Queue live; recaptures counted weekly |
| 9 | **Fill the Weekly Spine Scorecard every Friday + OODA review** | Joe | High | Trivial | Currently unfilled; it's leadership's own ortho-turnaround method and the prove-it record for Aug 30 / Sept 30 | First filled scorecard this Friday |
| 10 | **GBP hygiene: fix UTM casing split + Troy Maps pin / "Oakland MRI" call misdirect** | Paul / Randall | Med-High | Low | Casing split halves listing-click reporting; local "near me" is highest-converting intent; Troy is the Oakland unlock | One casing standard; Troy pin/calls verified |

## 🎯 By Aug 15 — the funnel-stabilization wave (CEO deadline)

| Fix | Owner | Impact | Effort | Gate/dependency |
|---|---|---|---|---|
| **Consolidate spine Google Ads campaigns** (fewer campaigns → enough conversion data each) | Blue Ox (Shaun/Jake), Joe coordinating | High | Low-Med | After #2 (signal). Jul 7 finding: spine campaigns starve the algorithm of conversion volume |
| **Shift booking share to the free website path; trim worst Zocdoc "Sponsored" spine spend** | Joe + Blue Ox/Zocdoc | High | Med | After #2. Website captures 74.7% at $0 vs Sponsored ~52% at ~$136/captured; $182K/yr at stake |
| **Ship spine differentiation messaging** (deep bench, MIS, neurosurgeon, conservative-to-surgical path) on spine pages + referrer one-pager | Randall + content | Med-High | Low-Med | None — creative audit: spine has NO differentiation anywhere today |
| **Qualification rubric + surgeon routing table (SP-A)** — right patient, right door, higher-converting surgeons | Joe + Kristen; **Katie authorizes** | Very High | Med | Clinical sign-off required. Salar absorbs ~21% of spine NPs at ~3% conversion; plan lever A (+6–9/wk) |

## 🏗️ By Aug 30 (Gate 1) — big bets to have visibly moving

- **5 physician-authored spine condition hubs** (stenosis, herniated disc, sciatica, DDD,
  spondylolisthesis) + Grade 6–8 rewrites — Randall at 80% spine + content-creator; physician
  review is the blocking gate. Topical authority 31.8 vs 70; the −71 B2C hole lives here.
- **FAQ + schema for AIO citations** — worthless until ASAP #3 unblocks the crawlers; do after.
- **Kristen's playbook ride-alongs** (~70 NP/100 visits vs team 6–40) + closed-loop referrer
  report-back + reserved same-week spine slots.
- **Cody decision point (~Jul 30):** 15 NP/month standard per leadership — surface the number,
  Kristen owns the call.

## 🚫 Explicitly deferred / do-not-touch (leadership decisions on record)

- **Ortho campaigns — change nothing** ("you're doing a great job on Ortho"); hold 130–140/wk.
- **"Box three" bidding move** — deferred ~30 days (Jul 15); revisit ~Aug 15 only after #2.
- **PMax test** — Blue Ox's lane, and only after tracking is trustworthy.
- **AI call center** — after the script/qualification foundations (Kelly briefing pending).
- **4th PL hire** — gated on Cody sustaining 15 NP/week.
- **Hospital-system / association link building + PR program** — real, but long-lead; schedule,
  don't ASAP. (0 such links since 2012; competitors 400+.)
- **Scheduling-system consolidation** — Santosh's EMT recommendation owns this (12–18 mo).

## Coverage vs. the spine plan's levers (+25/wk needed)

| Plan lever | Weekly target | Covered by |
|---|---|---|
| A. Qualify + route existing traffic (+6–9) | ASAP #4, Aug-15 rubric/routing |
| B. Recover B2C/organic hole (+7–11) | ASAP #1, #3, #10; Aug-15 ads consolidation + differentiation; Gate-1 hubs |
| C. Referral engine (+5–8) | ASAP #6, #7; Gate-1 ride-alongs/report-back |
| D. Fix leaks: attribution/tracking/access (+3–5) | ASAP #2, #5, #8, #9 |

**Sources:** `audits/cardinal-recommendation-tracker.md` (verified 7/22) · `pm/paul-action-update-2026-07-22.md` ·
`brand/current-state.md` · `playbooks/spine-90day-plan.md` · Otter transcripts Jun 1–Jul 21 (incl. Jul 7 EMT,
Jul 8 & Jul 21 1:1s, Jul 9 ops, Jul 14 B2B review, Jul 21 Q2 review) · Notion meeting notes Jul 8/15/20 ·
GA4 property 370514163 · PSI field data 7/22 · Semrush crawl Jul 21. New ideas added to `pm/ideas-bank.csv`
as **I-29…I-34**; compliance guardrails per `brand/brand-brief.md` apply to all content items.
