# GSC 16-Month Analysis — synergyhealth.org (Mar 2025 – Jul 21, 2026)

**Source:** Google Search Console performance export (Web search, last 16 months), pulled
Jul 21, 2026. Raw CSVs in `seo/data/2026-07-21/`; re-runnable script in `seo/data/analyze_gsc.py`.
**Why it exists:** decided in the Jul 20–21 Joe/Randall/Paul meetings — content decisions run on
GSC data (real Google data), not SEMrush estimates. This file is the shared ground truth that
`spine-content-cluster-map.md` and `quick-wins-title-meta.md` are built from.

---

## Headline findings

1. **76.6% of all clicks are branded or provider-name searches.** Non-branded queries are 65%
   of impressions (674K) but convert at **1.01% CTR** — people who already know SHP click;
   people researching symptoms/treatments see SHP constantly and don't click.
2. **Visibility exploded; clicks didn't.** Monthly impressions grew ~101K → ~400K and average
   position improved from ~36 to ~10–11 (big jump Oct 2025), yet clicks have been flat at
   **~4.3–4.9K/month for a year**. The site earns rankings and wastes them at the click.
3. **Spine is the priority line and the weakest commercial presence.** Only **48 non-branded
   spine queries** (66.7K impressions, **0.36% CTR** — the worst click-through of any line
   relative to its avg pos 11.2). Spine pages = ~9.5% of site impressions but **~2.2% of
   clicks**.
4. **The spine impressions we do get are mostly the wrong intent — or wasted rankings.** The
   single biggest spine query is **"acdf" (21K impressions, position 3.0, 0.02% CTR — 4 clicks
   in 16 months)**; next is the "broken neck / neck fracture" trauma-info cluster (~20K+
   impressions). The commercial queries that feed the spine funnel ("spine surgeon near me",
   "spine specialist near me", "back doctor near me") total only **~1,500 impressions in
   16 months** — SHP barely appears for them.
5. **The foundational condition hubs are effectively invisible in classic search.** Legacy
   `/conditions-we-treat/` versions: spinal stenosis pos **78.7 (0 clicks)** · sciatica pos
   50.9 · cervical radiculopathy pos 61.4 (0 clicks). Newer `/conditions/` versions exist but
   are thin (stenosis 509 impr pos 18.9 · herniated disc 417 impr pos 18.2 · DDD 25 impr) —
   splitting each topic across two weak URLs. The `/conditions/` versions are the ones
   Google's AI already cites (`gsc-ai-features-2026-07.md`) — rebuild there.
6. **Zero revision-patient presence.** Not one query in the top 1,000 for failed back surgery,
   revision, adjacent segment, hardware pain, or spine second opinion — the exact
   returning-surgery patient leadership wants is a total content gap.
7. **URL cannibalization is measurable, not theoretical** (details below): laminectomy split
   across 3 URLs, TKA across 7, carpal tunnel 5, Southfield 8, "spine hub" intent across
   3+ competing paths. Every split divides link equity and query mapping — this is the
   mechanism behind "every page we update de-ranks another."
8. **Title/meta is the cheapest lever on the table.** Multiple pages rank top-10 with CTR
   10–20× below position benchmark (ACDF: pos 3.0, 0.02% CTR on 21K impressions;
   spondylolisthesis: pos 6.0, 0.09%; cervical fusion: pos 9.0, 0.18% on 80K impressions).
   Recovering even a third of the modeled gap ≈ **+900–1,000 clicks/month (+20%)** with no
   new pages and no architecture risk.

---

## Intent split (all 1,003 exported queries)

| Intent | Queries | Clicks | % of clicks | Impressions | CTR | Avg pos |
|---|---|---|---|---|---|---|
| Branded (synergy/mendelson/kornblum) | 235 | 16,971 | 57.9% | 277,164 | 6.12% | 5.6 |
| Provider names | 133 | 5,482 | 18.7% | 80,510 | 6.81% | 5.3 |
| **Non-branded** | **632** | **6,835** | **23.3%** | **674,332** | **1.01%** | **16.9** |

## Non-branded by service line

| Line | Queries | Clicks | Impressions | CTR | Avg pos | Read |
|---|---|---|---|---|---|---|
| ortho (incl. TKA terms) | 117 | 746 | 213,284 | 0.35% | 24.4 | Biggest impression pool, barely clicked |
| pt (incl. lymphedema) | 48 | 354 | 139,497 | 0.25% | 19.0 | "physical therapy near me" pos 65 = invisible |
| other (urgent care, ASC, misc.) | 228 | 3,250 | 115,219 | 2.82% | 11.4 | Healthiest CTR — navigational-ish |
| **spine (incl. ACDF/ACDR)** | **48** | **240** | **66,738** | **0.36%** | **11.2** | **Priority line, worst CTR-for-position** |
| hand | 24 | 107 | 65,348 | 0.16% | 12.1 | Ranks, doesn't get clicked |
| imaging | 106 | 1,553 | 36,055 | **4.31%** | 12.7 | **Best non-branded performer** (open MRI) |
| pain | 18 | 130 | 20,550 | 0.63% | 8.0 | Thin |
| foot | 43 | 455 | 17,641 | 2.58% | 4.6 | Small but healthy (Southfield podiatry) |

## What spine demand SHP actually appears for

Top non-branded spine queries by impressions — note the intent problem:

| Query | Clicks | Impr | CTR | Pos | Intent |
|---|---|---|---|---|---|
| acdf | 4 | 21,041 | **0.02%** | **3.0** | Abbreviation lookup + patients researching a prescribed surgery — a page-1 ranking wasted at the title |
| acdr / acdr surgery | 28 | 10,317 | 0.27% | ~6.0 | Disc-replacement research — **no dedicated ACDR page exists** |
| broken neck (+ 9 variants) | ~40 | ~20,600 | ~0.3% | 5–10 | Trauma info — not bookable demand |
| laminectomy / laminectomy surgery | 14 | 6,440 | 0.2% | 47–65 | Treatment research — we're on page 5+ |
| neck fracture | 4 | 3,059 | 0.13% | 10.3 | Trauma info |
| thoracic decompression (+surgery) | 5 | 3,226 | 0.15% | 9–11 | Treatment research — page 1, no clicks |
| back specialist near me | 6 | 380 | 1.58% | 9.1 | **Commercial — tiny impression share** |
| spine specialist near me | 13 | 347 | 3.75% | 7.0 | Commercial |
| spine surgeon near me | 8 | 236 | 3.39% | 7.3 | Commercial |
| spinal stenosis | 3 | 102 | 2.94% | 38.7 | Condition — page 4 |

**The read:** when SHP shows for commercial spine queries it earns decent CTR — it just almost
never shows. GSC only reports queries where the site already appears, so tiny impression counts
on commercial terms mean **low impression share, not low demand**. That's why foundational
cluster content has to come before optimization can matter (build → index → measure → improve).

**Revision/returning-patient queries (failed back surgery, revision, adjacent segment, second
opinion, hardware): zero in the export.** Confirmed whitespace.

## URL cannibalization (the "every update de-ranks something" mechanism)

Same topic live on multiple competing URLs (clicks / impressions / avg pos, 16 mo):

- **Laminectomy — 3 URLs:** `/specialties/spine-back-and-neck/lumbar-laminectomy/` (342c /
  87.5K i / pos 28.6) · `/treatment/laminectomy/` (4c / 6.6K / 17.6) · `/treatment/lumbar-laminectomy/`
  (2c / 2.3K / 10.1). 87K impressions stuck on page 3 while two stubs split the query.
- **Neck fracture — 2 URLs** both ranking pos ~7: `/conditions/neck-fracture-broken-neck/`
  (69.3K i) and `/conditions-we-treat/spine-neck-back-conditions/neck-fracture-broken-neck/` (39.6K i).
- **Back fracture — 2 URLs:** `/conditions/back-fracture-break/` (17.2K i, pos 8.7) vs
  `/conditions-we-treat/...` (12.3K i, pos 32.1).
- **Microdiscectomy — 3 URLs:** `/treatment/microdiscectomy/` (pos 8.3, **0.00% CTR**) ·
  `/specialties/.../microdiscectomy/` (pos 54.2) · blog `/herniated-disc-microdiscectomy/` (pos 12.4).
- **TKA / knee replacement — 7 URLs**, incl. 229K impressions at pos 25.1 on one and 56K at
  pos 9.3 on another. (Ortho's biggest single impression pool, split seven ways.)
- **SI joint fusion — 3 · spinal cord stimulator — 2 · thoracic/lumbar decompression — 4+ ·
  kyphoplasty — 3 · medial branch block — 4 · carpal tunnel — 5.**
- **Spine hub intent split across** `/specialties/spine-back-and-neck/` (66.5K i, pos 24.7),
  `/specialty/spine-neck-back/` (4.7K i), `/conditions-we-treat/spine-neck-back-conditions/` (3.4K i).
- **Locations:** Sterling Heights on 4 URLs — the legacy `/full-service-clinics/sterling-heights-2/`
  is still the strongest location asset on the site (2,566c / 94K i). Southfield on **8** URLs.
  Troy split across 3 URLs (6.9K + 0.5K + 0.1K impressions). Legacy `/full-service-clinics/` +
  `/shp-*` paths still carry 5,199 clicks / 181K impressions.

Primary-URL decisions per topic are in `spine-content-cluster-map.md` §4. Redirect/canonical
execution belongs to Power Digital/Cardinal's technical workstream — we hand them the list.

## Page-level quick wins (impressions ≥ 20K, CTR below position benchmark)

Modeled click gap = impressions × (benchmark CTR for position − actual CTR), over 16 months.
Benchmarks are directional; informational queries increasingly lose clicks to AI
Overviews/snippets regardless of title. Full rewrites in `quick-wins-title-meta.md`.

| Page | Clicks | Impr | CTR | Pos | Gap /16mo |
|---|---|---|---|---|---|
| /contact-us/ | 387 | 128,940 | 0.30% | 6.2 | +5,415 |
| /specialties/physical-therapy/lymphedema-management/ | 569 | 222,596 | 0.26% | 8.7 | +4,996 |
| /flying-with-joint-replacement/ | 676 | 122,984 | 0.55% | 6.4 | +4,858 |
| /mendelson-kornblum-orthopedics-…/ (legacy blog) | 1,711 | 106,459 | 1.61% | 5.9 | +3,080 |
| /specialties/hand-upper-extremity/finger-amputation/ | 268 | 60,225 | 0.44% | 4.6 | +3,044 |
| /conditions/neck-fracture-broken-neck/ | 182 | 69,252 | 0.26% | 7.0 | +2,242 |
| /about-us/company-history/ | 2,643 | 86,443 | 3.06% | 5.3 | +2,111 |
| /locations/clinic-locations/ | 1,074 | 117,985 | 0.91% | 9.2 | +1,876 |
| /specialties/spine-back-and-neck/cervical-fusion/ | 148 | 80,362 | 0.18% | 9.0 | +1,861 |
| /our-providers/ | 425 | 125,211 | 0.34% | 10.0 | +1,453 |
| /treatment/total-knee-arthroplasty-tka/ | 10 | 56,356 | 0.02% | 9.3 | +1,399 |
| (…full 25-row list reproducible via script) | | | | | |

Top-25 modeled total ≈ **47K clicks/16 mo ≈ 2,900/mo at full benchmark**. Planning number:
**capture ⅓ ≈ +950/mo vs current ~4,300/mo baseline.**

## Trend (monthly)

| Month | Clicks | Impr | CTR | Pos |
|---|---|---|---|---|
| 2025-04 | 3,989 | 265K | 1.50% | 36.8 |
| 2025-08 | 4,524 | 339K | 1.33% | 35.5 |
| 2025-10 | 4,591 | 215K | 2.13% | **13.2** ← position breakthrough |
| 2026-01 | 4,940 | 371K | 1.33% | 13.7 |
| 2026-03 | 4,672 | 396K | 1.18% | 10.8 |
| 2026-05 | 4,308 | **423K** | **1.02%** | 10.5 ← CWV-failure window (May 1 regression) |
| 2026-06 | 4,455 | 356K | 1.25% | 11.6 |
| 2026-07 (thru 7/21) | 2,305 | 150K | 1.53% | 14.1 |

Rankings and impressions were won; CTR fell as low-intent informational visibility grew.
The job is not "more impressions" — it's **better-intent impressions + click recovery**.

## Devices

| Device | Clicks | Impr | CTR | Pos |
|---|---|---|---|---|
| Mobile | 37,480 | 2.35M | 1.60% | 12.8 |
| Desktop | 30,213 | 2.63M | 1.15% | 28.7 |
| Tablet | 1,029 | 54K | 1.92% | 7.2 |

Mobile (where local-intent searches happen) ranks 16 spots better than desktop — the desktop
number is dragged by national informational blog queries. Context for the original
"content shows on desktop, not mobile" ticket: that's a rendering/caching bug to fix
(see `content-update-workflow.md` §6) — but Google indexes **mobile-first**, so mobile parity
is non-negotiable. The audit's mobile CWV failure (28/100) remains Cardinal's technical fix.

## Bright spots to protect (do not disturb while pushing spine)

- **Provider pages: 106 paths, 23,405 clicks (~34% of all clicks), 844K impressions.** The
  single strongest asset class. Spine cluster should link *through* surgeon bios, never
  restructure them.
- **MRI/imaging: 4.31% non-branded CTR** ("open mri near me" 7.09% CTR @ pos 4.2). A working
  local playbook to copy for spine-at-location pages.
- **Southfield podiatry** ("podiatrist southfield" pos 2.7) and foot line (2.58% CTR, pos 4.6).
- **Port Huron**: 1,208 clicks / 40.8K impressions on a legacy URL + real "orthopedic port
  huron" query demand — a location strength not in the usual 8-location narrative (verify
  current clinic status before investing).
- Legacy ortho blog earners (shoulder-injury guide 145K i, flying-with-joint-replacement 123K i):
  title/meta polish only — no rewrites, no URL moves, no content surgery.

## Companion dataset

The **Generative AI features** view (AI Overviews / AI Mode) is analyzed separately in
`gsc-ai-features-2026-07.md` — impressions-only, 9-week window. Its headline: Google's AI
cites the new `/conditions/` + `/treatment/` structure 315:1 over the legacy structures,
which set the consolidation direction in the cluster map (§4a).

## What GSC cannot tell us (honesty box)

- Demand SHP never appears for (impression share). Absent spine commercial volume here ≠
  absent demand — it means we're not in the auction. Fix by building, then measuring.
- Query→page mapping in this export is inferred (separate CSVs). Use GSC UI page-filtered
  queries when a mapping decision is load-bearing.
- Clicks ≠ booked patients. Pair monthly GSC pulls with Liine qualified-call data once its
  tracking is validated (90-day plan, workstream D).
