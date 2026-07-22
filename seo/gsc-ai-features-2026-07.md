# GSC "AI Features" Analysis — synergyhealth.org (May 18 – Jul 19, 2026)

**Source:** GSC Performance export filtered to **Generative AI features** (AI Overviews /
AI Mode surfaces), pulled Jul 21, 2026. Raw CSVs: `seo/data/2026-07-21-ai-features/`;
script: `seo/data/analyze_gsc_ai.py`. Companion to `gsc-analysis-2026-07.md` (classic web).

**Read the export's limits first:** Google reports **impressions only** for this view — no
clicks, CTR, position, and **no query-level data**. Data begins **May 18, 2026** (when GSC
started reporting AI-feature data for the property), so this is a **9-week window**, not 16
months. AI-feature impressions are a **subset of** the web report's totals — an overlay,
never additive.

---

## Headline findings

1. **AI surfaces are ~7.6% of SHP's impressions and steady** — 52,141 AI-feature impressions
   vs 685K total web impressions in the same window (~5–7K/week; peak 7,347 mid-June).
   Mobile-heavy (60%).
2. **THE structural finding: Google's AI cites the new URL structure almost exclusively.**
   `/conditions/` + `/treatment/` pages earned **34,925 AI impressions**; the legacy
   `/specialties/` + `/conditions-we-treat/` structures earned **111 — a 315:1 preference**,
   even though the legacy structure still holds most classic-search impressions (2.2M vs
   416K over 16 months, largely historical accumulation). Google has effectively already
   chosen the site's canonical architecture. Consolidation direction updated in
   `spine-content-cluster-map.md` §4a.
3. **One page is 23% of all AI visibility:** `/conditions/neck-fracture-broken-neck/` —
   **11,859 AI impressions in 9 weeks.** SHP is already a go-to AI citation for broken-neck
   questions. This *explains* its 0.26% classic CTR (the AI answer absorbs the click) and
   defines its role: **authority and brand halo, not bookings.** Because AI amplifies this
   page, its named medical reviewer, review date, and "call 911 / ER now" banner are urgent,
   not cosmetic.
4. **AI impressions are not local demand — 26.5% aren't even American.** 13,821 impressions
   from 176 non-US countries (UK 3,065, India 2,328, Canada 1,638, Australia 1,227). Never
   report AI-feature impressions to leadership as pipeline; the KPI remains qualified calls/
   bookings. One real exception: **Canada + `/mri-for-canadian-patients/` (367 impressions)
   is the genuine Windsor cross-border MRI niche** — an existing page worth polishing, not a
   build project.
5. **The young new-structure spine hubs already get cited:** cervical-radiculopathy (276) and
   spondylolisthesis (274) earn AI citations despite thin content and weak classic rankings —
   evidence the hub rebuilds on `/conditions/` URLs will compound in AI surfaces. Meanwhile
   **ACDF/cervical fusion have zero AI presence** — no new-structure page exists and AI
   ignores the old ones. The same pages wasting 100K classic impressions are invisible where
   patients increasingly get answers.
6. **76 provider bios are cited (4,242 impressions), led by the founders** — David Mendelson
   (421) and Stephen Mendelson (365). Legacy-brand authority is transferring into AI answers;
   the Mendelson→Synergy bridge content matters there too.
7. **The insurance page gets cited (415)** — payer questions are an answer-engine surface.
   Keep it accurate against the real payer taxonomy in `brand/current-state.md` (Medicaid
   varies by provider — an AI answer overstating coverage is a patient-trust and compliance
   problem we'd be feeding directly to Google).

## AI impressions by content bucket (9 weeks)

| Bucket | AI impressions | Share | Note |
|---|---|---|---|
| Spine-ish (incl. fractures) | 16,774 | 29.8% | Neck-fracture alone is 11,859 |
| Other (blog, MRI, misc.) | 12,582 | 22.3% | Flying-with-joint-replacement 2,008 |
| Ortho | 12,020 | 21.3% | TKA guides 1,686 + 980 |
| Hand | 6,497 | 11.5% | Finger-amputation 1,975, Dupuytren's 1,013 |
| Providers | 4,242 | 7.5% | 76 bios |
| Locations | 2,352 | 4.2% | Livonia 558 leads |
| Foot | 1,608 | 2.9% | Stress fracture 861 |
| PT | 302 | 0.5% | Near-absent despite huge classic impressions |

## New vs old structure — the head-to-head pairs (AI impressions, 9 wk)

| Topic | New structure | Old structure |
|---|---|---|
| Finger amputation | `/treatment/finger-amputation-surgery/` **1,975** | `/specialties/hand-upper-extremity/finger-amputation/` 71 |
| Dupuytren's | `/conditions/dupuytrens-contracture/` **1,013** | `/conditions-we-treat/...dupuytrens-disease/` ~0 |
| Laminectomy | `/treatment/lumbar-laminectomy/` **509** + `/treatment/laminectomy/` 244 | `/specialties/spine-back-and-neck/lumbar-laminectomy/` ~0 |
| SI joint fusion | `/treatment/sacroiliac-joint-fusion/` **370** | `/specialties/.../sacroiliac-joint-fusion/` ~0 |
| TKA | `/total-knee...guide.../` 1,686 + `/treatment/...tka/` **980** | `/specialties/orthopedic-services/...tka.../` ~0 |
| Carpal tunnel | `/conditions/carpal-tunnel-syndrome/` **195** | `/conditions-we-treat/...carpal-tunnel.../` ~0 |

Classic-search corroboration: where both variants exist, the new-structure URL usually holds
the better *position* too (laminectomy 10.1 vs 28.6; microdiscectomy 8.3 vs 54.2; the
fracture pages living at `/conditions/` at pos 7–9). The old URLs' bigger impression totals
are 16 months of history, not a current-preference signal.

## What this changes (actioned in the other docs)

1. **Consolidation direction flips to the new structure** — cluster map §4a. New content
   (hubs, ACDR, revision cluster) builds on `/conditions/` + `/treatment/` URLs. Confirm with
   Paul/Cardinal that this is the migration's intended end-state **before any redirect ships**.
2. **Neck-fracture page hardening** (reviewer, date, 911 banner) moves up — it's SHP's most
   AI-amplified content.
3. **Wave-1 titles/metas unchanged** (titles are per-URL and reversible) — with one target
   swap noted in `quick-wins-title-meta.md` (Dupuytren's row).
4. **Monthly loop now exports both views** — classic + AI features — into sibling dated
   folders (workflow §3). Watch: AI share of impressions, neck-fracture's share, whether
   rebuilt hubs pick up AI citations, ACDF/fusion appearing at all.
5. **Expectation-setting for leadership:** AI visibility is a real and growing surface where
   clicks won't follow proportionally — the strategy there is being *the cited source* (schema,
   E-E-A-T, llms.txt — Cardinal's lane; our lane is the content quality that earns citation).
