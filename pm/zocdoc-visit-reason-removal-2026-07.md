# Zocdoc Marketplace — Visit-Reason Removal Decision Memo

**Date:** 2026-07-22 · **Prepared by:** in-house marketing (Joe) · **Owner:** Paul (task B2C-B.2) ·
**Status: DRAFT — pending Paul/leadership sign-off before the email goes to Zocdoc**

**Sources:** `Zocdoc_NG_Integrated_Analysis_Jul2025_Jun2026_SM7.20.xlsx` (tabs: `MP Visit Reason
Review`, `2026 Cost Efficiency`, `Visit Reasons 2026`, raw `Matched Detail` + `Unmatched Zocdoc`).
All figures below were **independently recomputed from the row-level data and match the workbook's
tables exactly** (2026 MP totals: 1,869 appts · $89,876 · 57.6% effective capture · $109.60 per kept
patient). The 7/20 "SM" file is the base analysis plus the three review tabs; underlying data is
identical in both uploaded versions.

---

## TL;DR

Remove **7 visit reasons** from Zocdoc **Marketplace/Discovery** (search, Sponsored, partner
syndication). Together they are **7.3% of 2026 marketplace spend but only 3.8% of kept patients** —
they convert at **33% booking-to-kept vs 59% for everything else** and cost **~$212 per kept patient,
double the $110 marketplace average**. Annualized savings **≈ $13K at the 2026 pace** (~$16K at the
trailing-12-month pace), and marketplace cost-per-kept improves to ~$106. Spine coverage is not
reduced: the structured spine consult reasons stay live and convert far better.

## The removal list (verified numbers)

Effective capture = booked patient kept a visit within 45 days, **including** later self-reschedules
and staff rebooks (generous). Capture measured on NextGen-matched bookings; cost is fully loaded.

| # | Visit reason | Service line | 2026 H1 spend | 2026 capture (kept/matched) | 2026 $/kept | Trailing-12m spend | 12m capture | 12m $/kept |
|---|---|---|---|---|---|---|---|---|
| 1 | Pain Management Consultation | Pain Management | $3,131 | 38.5% (20/52) | $157 | $7,575 | 39.3% (46/117) | $165 |
| 2 | Back Pain | Spine/Back/Neck | $2,222 | 34.6% (9/26) | $247 | $4,141 | 40.4% (21/52) | $197 |
| 3 | Surgery Consultation | Orthopedics General | $404 | 0% (0/5) | — | $404 | 16.7% (1/6) | $404 |
| 4 | Ultrasound | Other | $404 | 0% (0/6) | — | $1,010 | **0% (0/12)** | — |
| 5 | Pain Medication Prescription | Other | $101 | (1/1) | — | $1,212 | 41.7% (5/12) | $242 |
| 6 | Chronic Pain | Other | $101 | 0% (0/1) | — | $707 | 50.0% (4/8) | $177 |
| 7 | Acupuncture | Other | $202 | 50% (1/2) | — | $909 | 44.4% (4/9) | $227 |
| | **Total removal set** | | **$6,565** | **33.3% (31/93)** | **$212** | **$15,958** | **37.5% (81/216)** | **$197** |
| | *Marketplace average (2026)* | | *$89,876* | *57.6% (820/1,424)* | *$110* | | | |
| | *Marketplace after removal* | | *$83,311* | *59.3% (789/1,331)* | *$106* | | | |

### Why each one

1–2. **Pain Management Consultation & Back Pain** — the two material offenders: bottom-of-table
capture in *both* H1-2026 and the full 12 months (this is persistent behavior, not noise), and the
two most expensive kept patients we buy. "Back Pain" is the *generic symptom* reason — spine demand
still reaches us through **Orthopedic Consultation (Spine & Back)** (52%/$154) and **Spinal Cord
Surgery Consultation** (58%/$69), so part of this demand re-routes rather than disappears, making
the true patient loss smaller than 31/year. Pain is also a declining, non-priority service line per
the June 2026 audits.
3. **Surgery Consultation** — vague reason, attracts bookings we can't qualify; ~zero yield.
4. **Ultrasound** — **zero kept patients in 12 months** (0/12). Imaging generally requires an
order; it is not a self-book new-patient acquisition service. Pure waste.
5. **Pain Medication Prescription** — weak conversion, and as a bookable reason it invites
medication-seeking bookings (which the keep-rate confirms don't show). Reputational/stewardship
risk for a specialty practice; most of its spend was H2-2025, so removal prevents recurrence.
6. **Chronic Pain** — low volume; consolidates the pain cluster (with #1 and #5) into nothing —
consistent with removing the category, not cherry-picking it.
7. **Acupuncture** — not a listed SHP service line (flag to clinical ops to confirm); mismatch
bookings that mostly cancel. If clinical ops says we *do* offer it somewhere, drop it from the
email before sending.

Items 5–7 are low-volume (below the 20-matched threshold for a purely statistical call) — they're
included on **service-fit grounds, corroborated by** weak 12-month conversion.

## What we are NOT removing (and what to do instead)

- **Annual Physical** — $8,505 H1 spend, 42.7% capture, **but $91/kept (below the $110 average)**
  because PCP bookings are cheap. 125 of 218 matched bookings never kept — the **single biggest
  fixable pool**. Fix is operational (confirmation speed, reminder cadence, waitlist backfill per
  the call-center playbook), not removal. Revisit removal only if show-rate hasn't moved by Q4 —
  or earlier if leadership decides PCP acquisition is off-mission.
- **High-cost-per-kept consult reasons** — Foot Consultation ($115), Ortho Leg & Knee ($139),
  Ortho Spine & Back ($154), Hand & Wrist ($133), Shoulder ($135), Foot & Ankle ($130), Ingrown
  Toenail ($112), Toenail Problem ($145): capture is fine; the issue is **price per booking** →
  raise in the pricing conversation with Zocdoc (secondary agenda item in the email), not removal.
- **Keep (efficient):** Orthopedic Consultation ($82/kept), Spinal Cord Surgery Consultation ($69),
  Foot Problems ($69), Primary Care Consultation ($68), Foot Pain ($89), Knee Pain ($88),
  Hand Surgery Consultation ($34).

**Watch list (too few appts for a firm call now; revisit with the Q3 export, ~Oct 2026):**
Wrist Pain (37.5%/$168), Knee Problems (46%/$185), Carpal Tunnel (50%/$152), Back Problems
(50%/$168), Arthritis (40% 12m), Tingling/Numbness (25% 12m, dormant in 2026), MRI Report – Knee/Other
(consider bundling into a future cleanup — same "not an acquisition reason" logic as Ultrasound).

## Scope — critical detail for the Zocdoc request

Removal applies to **Marketplace/Discovery surfaces only**: Zocdoc Marketplace search, **Sponsored/
boosted placements**, and partner discovery syndication (the "Google and others" / Healthgrades
sources in our export). **Do not touch the direct booking flow from synergyhealth.org** — the
website path is $0-cost and captures at 74.7%; those visit reasons should remain bookable there.
The email asks Zocdoc to confirm this scoping is possible; if a reason can't be scoped, we decide
reason-by-reason (for Ultrasound and Pain Medication Prescription we'd remove everywhere).

## Verification after the change

1. Zocdoc to confirm effective date in writing + that **no per-booking fees accrue** on these
   reasons after that date; already-booked future appointments unaffected.
2. Next monthly Zocdoc export: filter these 7 reasons → Marketplace/Discovery rows should go to zero;
   spot-check that spine demand shifts into the structured consult reasons.
3. GA4 `zocdoc handoff` events and website-source bookings should be unaffected (website path
   out of scope).
4. Update this memo + `pm/master-task-list.csv` B2C-B.2 when confirmed.

**The email draft to send:** `pm/zocdoc-enterprise-removal-email-2026-07.md`

*Compliance note: all figures are de-identified aggregates (patient hashes only in source data —
no PHI in this memo or the email). This memo is internal working analysis, not a public claim.*
