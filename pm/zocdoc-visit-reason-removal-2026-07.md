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

Remove **7 visit reasons account-wide** plus **2 provider-specific listings** (Dr. Salar and
Dr. Munk on "Orthopedic Consultation (Spine & Back)") from Zocdoc **Marketplace/Discovery**
(search, Sponsored, partner syndication). Together the set is **8.8% of 2026 marketplace spend but
only 4.3% of kept patients** — it converts at ~33% booking-to-kept vs ~60% for everything else and
costs **~$225 per kept patient, double the $110 marketplace average**. Annualized savings
**≈ $15.8K at the 2026 pace** (~$18.4K at the trailing-12-month pace), and marketplace
cost-per-kept improves to ~$105. Spine coverage is not reduced: the structured spine consult
reasons stay live and convert far better (see the per-provider section for the Salar/Munk safety
check).

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
| 8 | Ortho Consultation (Spine & Back) — **Dr. Salar only** | Spine/Back/Neck | $808 | 37.5% (3/8) | $269 | $1,616 | 41.2% (7/17) | $231 |
| 9 | Ortho Consultation (Spine & Back) — **Dr. Munk only** | Spine/Back/Neck | $505 | 16.7% (1/6) | $505 | $808 | 40.0% (4/10) | $202 |
| | **Total removal set (7 account-wide + 2 provider-specific)** | | **$7,878** | **32.7% (35/107)** | **$225** | **$18,382** | **37.9% (92/243)** | **$200** |
| | *Marketplace average (2026)* | | *$89,876* | *57.6% (820/1,424)* | *$110* | | | |
| | *Marketplace after removal* | | *$81,998* | *59.6% (785/1,317)* | *$105* | | | |

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

## Full breakdown by cost and keep rate — and what else qualifies

*(Added 2026-07-22 after a complete pass over all 191 marketplace visit reasons. Visual decision
aid: `https://claude.ai/code/artifact/942b53ec-dc23-46af-b205-66f57dce6b93`)*

**Marketplace baseline, FY Jul 2025–Jun 2026:** $182,292 · 3,623 bookings · 56.9% effective
capture (1,626 of 2,859 matched) · **$112 cost per kept patient** · **$75,680 estimated spend on
bookings that never became a visit** · **1,233 blocked slots**.

### Which calls are statistically firm vs. judgement

Screening every reason with a 90% Wilson upper bound against the 56.9% benchmark — i.e. "is this
below average even in the best case the sample allows" — only **five** reasons are certain
underperformers:

| Reason | FY spend | Kept/matched | Capture | Upper bound | On the list? |
|---|---|---|---|---|---|
| **Annual Physical** | $20,520 | 195/516 | 37.8% | 41% | **No — see below** |
| Pain Management Consultation | $7,575 | 46/117 | 39.3% | 47% | Yes |
| Back Pain | $4,141 | 21/52 | 40.4% | 52% | Yes |
| Ultrasound | $1,010 | 0/12 | 0% | 18% | Yes |
| Surgery Consultation | $404 | 1/6 | 16.7% | 50% | Yes |

Everything else in the removal set (Pain Medication Prescription, Chronic Pain, Acupuncture, and
the two provider-specific spine listings) rests on **service fit plus corroborating weak
conversion** — state it that way if Zocdoc pushes back on statistical grounds.

### ADDITION 1 — 30 reasons that were never new-patient acquisition ($3,031/yr)

The cleanest ask in the whole exercise: we are paying a new-patient finder's fee for imaging
reads, injections, follow-ups and paperwork. Combined capture 36%. **Nothing is lost by removing
them** — these are existing patients or non-acquisition events.

| Group | # reasons | FY spend | Kept/matched | Capture |
|---|---|---|---|---|
| Imaging & report reads — MRI Report (Knee/Back/Shoulder/Other), CT Scan Report, X-ray | 6 | $1,212 | 6/14 | 43% |
| Injections & in-office procedures — Cortisone Shots, Epidural/Back/Knee/Joint/Facet Injection, Pain Medicine Injection | 7 | $606 | 3/11 | 27% |
| Follow-ups & second opinions — Orthopedic/Foot/Spine/Trauma Follow Up, Hip & Knee Surgery Follow Up, Pain Medicine Follow Up | 9 | $505 | 4/6 | 67% |
| Weight-loss & wellness (all Dr. Abood) — Obesity/Weight Loss, Wellness Care, Medicare Annual Wellness | 5 | $405 | 4/13 | 31% |
| Admin, legal & accident — Worker's Comp Evaluation, Motor Vehicle Accident, Car Accident Injury | 3 | $303 | 0/3 | 0% |
| **Total** | **30** | **$3,031** | **17/47** | **36%** |

Follow-ups keep at a healthy 67% and are *still* wrong to buy — those are existing patients we'd
have seen anyway. **Recommend adding all 30 to the Zocdoc request.**

### ADDITION 2 — Annual Physical: put it on the clock, don't pull it yet

The biggest single line item in the account and the firmest statistical underperformer, but the
economics argue against removal:

- $20,520 = **11.3% of all marketplace spend**, 100% on Dr. Tony Abood
- 37.8% capture (42.7% in 2026) — worst of any material reason
- **321 patients booked and never kept** — a quarter of all blocked slots in the channel
- **but $105 per kept patient, *below* the $112 average** — the cheapest patients Zocdoc sells us
- at benchmark capture the same spend would yield **+99 more patients** at $70 each

**Recommendation: set a floor of 50% capture by the Q4 export; remove if it hasn't moved.** The
fix is show-rate operations (faster confirmation, reminder cadence, waitlist backfill), not
delisting. The strategic question underneath is leadership's: growth priority is spine and ortho,
and this is primary care — if PCP acquisition is off-mission, this becomes a one-line addition to
the same request.

### ADDITION 3 — Dr. Yacisen needs a profile prune, not a reason removal

| Provider | Reasons listed | Booked once only | FY spend | Capture | $/kept |
|---|---|---|---|---|---|
| **Dr. Joseph Yacisen, DO** | **63** | **38 (60%)** | $15,150 | 48% | **$170** |
| Dr. Benjamin Mayo, MD | 43 | 21 (49%) | $14,342 | 67% | $110 |
| Dr. Randy Leff, DPM | 27 | 6 (22%) | $30,906 | 69% | $118 |

Worst cost per kept patient of any high-spend provider, and his generic **"Orthopedic
Consultation" keeps 1 of 9** — patients booking a general ortho slot with a hand/foot specialist
land in the wrong place. Dr. Leff is the counter-example: highest spend, tightest list, best
performance. **Ask: prune Yacisen's profile to hand/wrist, foot/ankle and the sub-specialty
consults that keep at 60–100%.** Confirm scope with him before sending.

### Not for removal — pricing renegotiation instead

Converting acceptably but costing too much per patient: Ortho Consultation (Neck) $152/kept and
worsening to $303 in 2026 · Cyst(s) $177 · Trigger Finger $152 · Arthritis $252 · Pediatric
Orthopedics $168 · Spine Specialist Consultation $168 · Spinal Stenosis $168 · Toenail Removal
$166 · Tingling/Numbness $404. Plus the high-volume consults already flagged: Ortho Leg & Knee
$127, Shoulder $133, Hand & Wrist $130, Spine & Back $132, Foot Consultation $114.

### Revised totals if leadership approves the addition

| | FY spend | Share of spend | Share of kept patients |
|---|---|---|---|
| Already in the email (7 + 2 provider) | $18,382 | 10.1% | 5.7% |
| Recommended addition (30 non-acquisition) | $3,031 | 1.7% | 1.0% |
| **Combined removal** | **$21,413** | **11.7%** | **6.0%** |
| On the clock (Annual Physical) | $20,520 | 11.3% | 12.0% |

Combined removal lifts marketplace capture **56.9% → 59.2%**, drops cost per kept **$112 → $109**,
and frees roughly **150 appointment slots/year**.

## Per-provider view (how Zocdoc will actually action this)

Zocdoc configures visit reasons **per provider profile**, so the request is provider-explicit.
All figures FY Jul 2025–Jun 2026, Marketplace/Discovery only.

### A. The 7 account-wide removals — who carries them today

| Visit reason | Providers currently listed (FY kept/matched) |
|---|---|
| Pain Management Consultation | Dr. Kevin Lee (14/43, 33%) · Dr. Anthony Oddo (13/24, 54%) · Dr. Hanish Singh (9/22, 41%) · Dr. Brian Kassa (7/17, 41%) · Dr. Joseph Yacisen (3/10, 30%) · Dr. Lucia Zamorano (0/1) |
| Back Pain | Dr. Mohamed Salar (7/15, 47%) · Dr. Andres Munk (3/10, 30%) · Dr. Scott McCarty (3/9, 33%) · Dr. Jeffrey Varghese (3/7, 43%) · Dr. Joseph Maslak (3/6, 50%) · Dr. Kevin Lee (1/3) · trace: Oddo, Singh, Kassa |
| Surgery Consultation | Dr. Benjamin Mayo (1/4, 25%) · Dr. Joseph Maslak (0/1) · Dr. Jeffrey Varghese (0/1) |
| Ultrasound | Dr. Benjamin Mayo (0/9) · Dr. Joseph Yacisen (0/3) |
| Pain Medication Prescription | Dr. Anthony Oddo (4/9, 44%) · Dr. Brian Kassa (1/3) |
| Chronic Pain | Dr. Anthony Oddo (4/5) · Dr. Hanish Singh (0/1) · Dr. Joseph Yacisen (0/1) · Dr. Brian Kassa (0/1) |
| Acupuncture | Dr. Anthony Oddo (2/6, 33%) · Dr. Brian Kassa (2/3) |

### B. Provider-specific removals (reason stays live for all other providers)

| Provider | Visit reason to remove | FY | 2026 H1 | Why safe |
|---|---|---|---|---|
| Dr. Mohamed Salar, MD | Orthopedic Consultation (Spine & Back) | 41% (7/17), $231/kept, $1,616 | 38% (3/8), $808 | Keeps Spinal Cord Surgery Consultation (62%, his best reason), Sciatica, Lower Back Pain, Spine Specialist Consultation, Neck Pain |
| Dr. Andres Munk, MD | Orthopedic Consultation (Spine & Back) | 40% (4/10), $202/kept, $808 | 17% (1/6), $505 — worsening | Keeps Spinal Cord Surgery Consultation (75%, his best reason), Ortho (Neck), Sciatica, Back Problems, Neck Pain |

Supporting stat for the email: on this reason, **all other providers convert ~67%** (35/52 FY) —
Salar and Munk (41%/40%) are the drag. Removing just their two listings lifts the surviving
reason to healthy and preserves both surgeons' spine discovery through better-converting reasons.

### C. Consequences leadership should sign off on knowingly

- **This effectively exits the pain-management doctors from paid marketplace discovery.** The
  blanket 7 remove 80–90% of FY marketplace volume for Dr. Lee (56 of 64 appts), Dr. Oddo (63/76),
  Dr. Singh (37/45), and Dr. Kassa (36/44); only trace long-tail reasons remain on their profiles.
  Consistent with strategy (pain is a declining, non-priority line, and these four run 40–48%
  capture overall) — but it is a service-line decision, not just a cleanup. Confirm with Paul +
  leadership explicitly.
- **Annual Physical is entirely Dr. Tony Abood** ($20,520 FY, 195/516 kept, 38%) — he is 100% of
  the reason's volume, so the "fix show-rate first" decision is a one-provider ops conversation,
  and a one-line change later if leadership opts to pull it.
- **No provider is fully de-listed** by this request: every affected doctor retains bookable
  marketplace reasons (verified per-profile against the FY booking data).

### D. Per-provider watch list (weak but below volume threshold — revisit with Q3 export)

- Dr. Joseph Yacisen: generic "Orthopedic Consultation" 1/9 (11%) FY; "Ortho (Foot & Ankle)" 5/12
  (42%) FY but 50% in 2026 — trending up, hold.
- Dr. Kristina Green, DPM: "Foot Pain" 3/10 (30%) FY, only $392 — cheap, watch.
- Non-acquisition trace reasons to bundle into a future cleanup: "MRI Report – *", "Pain Medicine
  Follow Up", "Cortisone Shots", "Orthopedic Follow Up", "Worker's Compensation Evaluation" —
  follow-ups/reports shouldn't be paid new-patient discovery reasons regardless of conversion.
- Dr. Zamorano's profile still links to the legacy `mendelsonortho` Zocdoc page (rebrand remnant,
  per `brand/provider-roster-by-service-line.md`) — separate fix, don't mix into this request.

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
