# Spine Paid Search — Jan 1 → Jul 19, 2026 (Google Ads exports)

**Analyst:** Joe + Claude session · **Feeds:** `playbooks/spine-website-game-plan.md` W0 baselines ·
`playbooks/spine-90day-plan.md` §4D · Cardinal paid-media handoff
**Sources:** Google Ads exports (search-terms, landing-page, campaign/conversion-action reports).
**Caveats:** search-terms report shows **reported terms only** ($182K visible; Google's
"other search terms" rollup hides the rest — LP-level spine spend is ~$431K for the same window).
"Conversions" is a **mixed bag of actions** (see §3) — treat CPA as directional, not bookings.
**Status: internal analysis — not patient-facing.**

> **✅ ERA SPLIT RESOLVED (7/21 daily re-export) — see §8.** The original exports blended
> pre/post-migration performance; the daily keyword export now separates them. Headlines: the
> new site converts **materially better** (CR 6.2% → 8.7%; June 11.0%, July 11.7%), CPA is
> flat (~$293) because clicks fell as conversion rate rose, and the intent pattern **survives
> the split**. Caveat that remains: June's Liine go-live changed conversion counting
> mid-window, so part of the June/July CR jump is definitional — judge trends within eras,
> not across June. §1–§4 below stay as the blended historical record; **§8 is the operative
> view** for baselines and decisions.

## 1. Where the spend goes (spine campaigns, reported terms)

| Campaign | Cost | Conv | CPA |
|---|---|---|---|
| BOD Neck/Back/Spine — Sterling Heights | $90,700 | 407.9 | $222 |
| BOD Neck/Back/Spine — Livonia | $79,562 | 265.3 | $300 |
| BOD Neck/Back/Spine — Port Huron | $5,357 | 17.1 | $313 |
| BOD Neck/Back/Spine — Southfield | $2,235 | 3.2 | $690 |
| BOD Spine Conditions — Sterling Heights | $2,141 | 1.0 | **$2,141** |
| BOD Spine Conditions — Livonia | $2,061 | 2.0 | **$1,026** |

**The audit's GEO gap is confirmed in the data: there is no Troy campaign at all**, Southfield is
near-zero (and inefficient), and ~94% of visible spend sits on Sterling Heights + Livonia.

## 2. What converts in paid — and what doesn't (term buckets)

| Bucket | Clicks | Cost | Conv | Conv rate | CPA |
|---|---|---|---|---|---|
| Generic doctor ("back/spine doctor") | 1,326 | $25,031 | 225.7 | 17.0% | **$111** |
| Near me / local | 3,610 | $66,480 | 434.9 | 12.0% | **$153** |
| Pain management | 407 | $7,637 | 48.7 | 12.0% | $157 |
| Branded (practice/surgeon names) | 309 | $4,913 | 45.4 | 14.7% | $108 |
| Surgery intent | 2,936 | $53,142 | 138.6 | 4.7% | $383 |
| **Condition terms** (sciatica, stenosis, herniated…) | 817 | $11,935 | 21.2 | **2.6%** | **$564** |
| **Injection intent** | 436 | $10,752 | 12.5 | 2.9% | **$859** |
| Chiro/PT-adjacent | 164 | $4,276 | 9.3 | 5.7% | $458 |
| MRI/imaging | 8 | $370 | 0.0 | 0% | — |

**Reading:** paid is good at **I1 "find me a doctor now"** demand ($111–157 CPA) and bad at
**I2 condition-research** demand ($564–859 CPA, ~2.6% conv). That is the empirical case for the
game plan's division of labor: **let paid own I1; capture I2 with the organic condition + guide
layer** (which costs $0 per click) instead of buying research-mode clicks the site can't convert.
The two "Spine Conditions" campaigns ($1,026–2,141 CPA) are pause/restructure candidates —
Cardinal's call (they own paid), our data handoff.

Waste floor: **230 reported terms spent >$100 each with zero conversions = $38,440** (e.g.
"laminectomy" $986/0) → negative-list fodder. Notably, **zero Medicaid-containing search terms**
— the Medicaid-mismatch bucket Joe saw happens **post-click** (intake/Liine), not at query time;
it's a qualification fix, not a keyword fix.

## 3. The conversion mix is soft (why CPA ≠ patients)

Spine-campaign conversions by action: **ZocDoc NP 549.8** (the paid marketplace we're trying to
shift away from) · **Website "New Patient Intent" 329.9** (the action leadership already flagged
as overvalued $125 → should be $5) · Calls-from-ads 222.6 · Liine call family ~400 combined ·
**Liine NP Online Booking = 1.4** — the broken Liine↔Zocdoc→Ads booking signal is visible right
here. **Standing rule holds: no bidding changes until the conversion values are fixed** (Liine
booked-call ≈ $150; NP Intent ≈ $5).

## 4. Landing pages — paid is funding the duplicate architecture

| Landing page | Cost | Conv | CPA | CTR |
|---|---|---|---|---|
| `/specialty/spine-neck-back/` (duplicate hub S2) | **$199,754** | 562.8 | $355 | 3.38% |
| `/specialties/spine-back-and-neck/` (canonical hub S1) | **$172,125** | 502.2 | $343 | 3.80% |
| McCarty bio (broad-query LP) | $9,231 | 17.1 | $539 | 0.31% |
| Salar bio (broad-query LP) | $8,844 | 21.8 | $406 | 0.33% |
| Munk misfiled hub child (Port Huron) | $8,155 | 27.4 | $298 | 5.86% |
| Maslak bio | $7,722 | 21.5 | $360 | 0.36% |
| Varghese bio | $6,792 | 14.1 | $482 | 0.38% |
| `/degenerative-disc-disease-treatment/` (legacy LP) | $5,315 | 4.1 | **$1,304** | 5.29% |
| Sterling Heights spine LP (S2 child) | $3,017 | 6.7 | $453 | 3.83% |
| `/herniated-disc-microdiscectomy/` (root orphan) | $2,428 | 5.0 | $485 | 1.33% |

**~$372K of paid traffic was split across the two duplicate spine hubs** — the URL consolidation
in `spine-semantic-model.md` §B2 is therefore also a **paid-efficiency play** (one hub
accumulating Quality Score + conversion history instead of two halves). Mobile speed score on
the hubs: **6/10** (CWV work matters for paid too). Provider bios used as broad-query LPs run
0.31–0.38% CTR at $360–539/conv — wrong page for the query; post-rebuild, "doctor near me"
queries should land on the hub/team module, and bios should catch **name** queries.

## 5. Why Salar's page is the #1 spine page (data answer)

His organic traffic is **name demand, not spine content**: "dr. salar" = **2,900 US
searches/month**, his page ranks **#1** and that single term drives ~52% of the page's traffic
(719 of ~1,376 est. visits) — vs. "scott mccarty" at 210/month (27 visits). Drivers, in
evidence order: (1) **paid has been broadcasting him** — his bio took 124,181 ad impressions as
a landing page this period; (2) **community word-of-mouth concentration** (Arabic-speaking
patient base searching his name; he holds ~21% of spine NPs); (3) directory/review vetting
behavior (name-Googling before booking); (4) the site's only "Meet Dr." video. **Caveat:**
Semrush volume is US-national — some "dr. salar" searches are other Salars elsewhere; his page
wins the SERP regardless. **Implication:** the #1 spine asset is *branded capture of one
surgeon's name*, while the elective condition funnel contributes ~0 — the exact imbalance the
game plan exists to fix. Protect the page (KEEP) during consolidation.

## 6. Landing-page conversion fixes (the "make them convert" list, in priority order)

Grounded in this data + the June audit + the templates doc. Owners in brackets.

1. **Fix what the machine is learning first.** Liine online-booking recorded 1.4 conversions
   (broken signal), "NP Intent" is valued $125 → should be ~$5, ZocDoc NP (549.8) is the
   biggest counted action. Smart bidding is optimizing toward soft/paid-marketplace events —
   every other fix underperforms until values are corrected. [Paul + Joe; no bid changes until done]
2. **Booking above the fold, online-first, one number.** Website booking captures ~75% at $0;
   patients demonstrably route around phones (166 self-reschedulers). Every paid LP gets a
   sticky mobile CTA bar (Book online + Call), online listed first, ONE tracked number (three
   numbers are live today), and a 3-field mini-form (name, callback, reason + ZIP) instead of
   a link-out. [Paul builds; templates §2]
3. **True LP variants — kill the exits.** Audit finding stands: paid lands on full-nav pages
   (300+ links = easy exit). Paid variants strip to logo + phone + book, single goal, no mega-nav.
   The Sterling Heights LP that duplicates the general ortho page gets its own spine variant.
   [Paul; Cardinal coordination]
4. **Message match: query → H1.** Quality Score is ~4/10 and bios catch broad queries at
   0.31–0.38% CTR. "spine specialist near me" ads must land on a page whose H1 says exactly
   that for that city, with that clinic's spine team and true access promise — not a generic
   hub, not a bio. Bios receive **name** queries only. [Cardinal restructure + content-creator copy]
5. **Answer the three buckets on the page** (Joe's own paid-traffic analysis):
   - **"I need an MRI first"** → the imaging module (**final wording delivered by Mitch 7/22**
     — two branches, templates §2 approved blocks: have-an-MRI → "we'll review it with you and
     decide next steps together"; no-MRI → "see us first and make sure you need one… if you do,
     we can order it, perform it, and review it with you")
   - **"I want an injection now"** → visible route to the interventional pain team ("image-guided
     injections, often within the week") — the conservative front door captures them instead of
     losing them.
   - **Medicaid/coverage mismatch** → compliant pre-qualification: accepted-plans module
     ("varies by provider — we verify yours in one call") + Harmony direct-pay path so
     non-covered visitors aren't a dead end and mismatched leads self-deflect before the form.
     (Zero Medicaid search terms exist — this bucket arrives post-click; the page must handle it.)
6. **Speed.** Hub mobile speed score is 6/10 and CWV collapsed ~May 1 (days after migration —
   likely migration-caused; confirm). Paid pays twice for slow pages (QS + abandonment).
   Apply the templates performance budget to LP variants first. [Paul; Cardinal owns CWV queue]
7. **Trust above the fold:** 96% recommend (sourced), fellowship-trained spine team, real
   provider photos (the natural straight-on style that works), honest access promise. No
   unsourced stats — the 90%/92% figures stay off until substantiated (V2).
8. **Retire the worst LPs:** `/degenerative-disc-disease-treatment/` ($1,304/conv, 0.96% conv
   rate — attracts clicks, doesn't convert) and `/herniated-disc-microdiscectomy/` ($485) →
   repoint campaigns to the canonical condition pages post-consolidation; keep the pages live with rel=canonical to the canon — NO redirects. [Paul, after V6]
9. **Set the handoff expectation:** LP tells the visitor what happens next ("we verify your
   insurance on the first call") so the call center's qualification script
   (`pm/spine-intake-qualification-script.md`) starts warm, not cold. [Kelly]

Measure it: post-fix, judge LPs on **Liine qualified calls + real online bookings per click**
(not NP Intent), on post-migration windows only, at the 4-week OODA cadence.

## 7. GA4 post-migration read (May 21 – Jul 21 export, "SHP - New Site")

First clean post-migration window. **Read the caveats first** — this export is only partially
usable:

**Data-quality issues (fix in GA4 before trusting any LP conversion metric):**
- The export appears **filtered to converting sessions** (session-key-event rate = 1 on every
  row; engagement 99.4%) — there is no denominator, so conversion *rates* per LP cannot be
  computed from it. Re-export unfiltered (all sessions) with the same dimensions.
- **"Key events" is inflated** (7,837 events across 2,398 sessions ≈ 3.3/session) — soft events
  are counted as key events. Define ONE money event (booking submitted / qualified call) and
  report on it; today's number is not bookings.
- **Channel attribution is broken:** 1,565 sessions classified "Paid Search" carry
  source/medium `google / organic`, and 661 are `(not set)`. Likely UTM/`scct` parameter
  mangling or channel-group misconfig. → Santosh/Paul queue; until fixed, paid-vs-organic LP
  splits in GA4 are unreliable.
- Row sums (3,401) exceed the grand total (2,398) — sessions double-count across
  dimension combos; use the grand total for level-setting only.

**What it still shows (directionally):**
- **The live new site runs on the `/specialty/` structure.** Converting sessions land on
  `/specialty/*` 1,445 : 1 over `/specialties/*` — `/specialty/spine-neck-back` (322 sessions)
  is the operating spine hub; `/specialty/orthopedic-services/livonia` (459) is the top
  service LP; homepage 803. **This flips the era assumption in §4** (the `/specialties/` hub
  was likely the *pre*-migration structure) and is why the semantic model's hub canonical is
  now marked V6-decides.
- **Spine share of converting sessions is 13.2%** (449 of 3,401 row-sessions) — the funnel
  weakness confirmed on the new site: one hub page + thin provider-bio tail (McCarty 29,
  Salar 27, Maslak 20, Varghese 14), with `/conditions/*` pages effectively absent from
  converting entries.
- **GBP location listings are a real converting channel** (location-listing campaigns:
  MKOLI 192+ sessions etc.) — local-listing hygiene belongs in the location-page work.
- A legacy Mendelson blog post still lands converting sessions (7) — purge-list confirmation.
- **First AI-assistant referrals appeared** (3 sessions) — the GEO channel exists; baseline it.

## 8. Era-split resolution + monthly insights (7/21 daily keyword export, Jan 1–Jul 19)

**Total spine paid, full picture: $457,704** ($210,131 pre-migration + $247,573 post) —
larger than either earlier export showed.

### The eras
| Era | Cost | Clicks | Conv | CPA | Conv rate |
|---|---|---|---|---|---|
| Pre-migration (Jan 1–Apr 21) | $210,131 | 11,521 | 710.1 | $296 | 6.2% |
| **Post-migration (Apr 22–Jul 19)** | $247,573 | 9,728 | 848.8 | $292 | **8.7%** |

**Monthly:** Jan $315 CPA/6.7% → Feb $365/4.6% → Mar $258/6.3% → Apr $315/6.0% →
**May $407/5.4% (the migration + CWV-collapse dip)** → **Jun $258/11.0% on a near-doubled
$107.8K budget** → Jul $238/11.7% (best CPA of the year). Reading: May was the migration
casualty; June recovered strongly — but June is also when **Liine actions entered the
conversion column**, so the 11% CRs are partly a measurement change. Within-era trend is
real; the June step-change is mixed signal.

### The intent pattern, confirmed post-migration (keyword-level)
| Bucket | Cost | Conv | CPA | CR |
|---|---|---|---|---|
| Generic doctor ("spine doctors," "orthopedic spine surgeon") | $129,020 | 566.0 | **$228** | 11.1% |
| Near me / local | $43,564 | 276.3 | **$158** | 14.3% |
| Pain management | $27,338 | 112.8 | $242 | 11.4% |
| Injection | $22,120 | 54.0 | $410 | 8.5% |
| **Surgery keywords** ("spinal fusion," "back surgery") | **$60,656** | 88.2 | **$688** | **3.6%** |
| Condition keywords | $3,670 | 5.0 | $734 | 1.5% |

The blended-era conclusion holds and sharpens: **$60.7K post-migration went to surgical-intent
keywords converting at 3.6%** — surgery researchers are I3 patients who need content and
surgeon pages, not ads. The fusion family is the worst of it (spinal fusion $2,267/0 · back
fusion $1,346/0 · neck fusion $1,163/0 · back fixation $1,146/0). Post-migration zero-conv
waste (>$100 terms): **$17,571**.

### Four new actionables (Cardinal handoff — they own paid)
1. **Weekend dayparting:** Sat+Sun post-migration = **$40,436 at $480–505 CPA, 4.6–5.0% CR**
   vs. Monday's $199/12.5%. Nobody answers the phone on weekends and online booking's signal
   is broken — bid down weekends until the online-booking path + tracking are fixed, then
   retest (the self-rescheduler data says weekend demand is real; it just can't convert today).
2. **Winners are maxed — growth needs new coverage, not more budget:** top converters already
   run 74–95% impression share ("spine specialist near me" at 95% IS, $115–127 CPA). The
   headroom argument for the **Troy campaign** is now quantitative: the efficient terms have
   no room left in existing geos.
3. **Negative-list the fusion family + trim surgical keywords** ($60.7K at 3.6% — keep only
   proven surgical terms like "spine surgery" SH at $305 if the qualified-call data supports it).
4. **Southfield confirmed kill/restructure** ($1,063 CPA post-migration, 1.5% CR) vs.
   **Port Huron quietly efficient** ($170 CPA on $4.1K — small, keep). Spine Conditions
   campaigns: still dead post-migration ($3.3K, 4 conv) — fold into the organic condition plan.

## 9. Actions (routed per the process doc)

1. Hand this analysis to **Cardinal** (paid owner): Spine Conditions campaigns
   pause/restructure; Troy campaign gap; negative list from the $38K zero-conv tail;
   LP consolidation timing aligned with the canonical plan (V6 first; no redirects).
2. **Paul + Joe:** fix conversion values/actions before any bidding change (NP Intent → $5;
   Liine booked-call ≈ $150; repair Liine NP Online Booking signal).
3. **Game plan W0 baseline:** this file is the paid baseline; GSC organic baseline cut in
   parallel this week.
4. **Semantic model:** confirms hub consolidation, bio KEEP flags, and the I1-paid / I2-organic
   division of labor.
