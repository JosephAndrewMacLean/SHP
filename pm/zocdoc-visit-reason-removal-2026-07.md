# Zocdoc Marketplace — Visit-Reason Removal Decision Memo

**Date:** 2026-07-22 · **Prepared by:** in-house marketing (Joe) · **Owner:** Paul (task B2C-B.2) ·
**Status: DRAFT — pending Paul/leadership sign-off before the email goes to Zocdoc**

**Analysis window: Jan 1 – Jun 30, 2026 only.** *(Revised 2026-07-22 at Joe's request — an earlier
draft used the trailing 12 months. Everything below is recomputed on 2026 bookings alone; where the
shorter window changes a conclusion, it is called out.)*

**Sources:** `Zocdoc_NG_Integrated_Analysis_Jul2025_Jun2026_SM7.20.xlsx` (tabs: `MP Visit Reason
Review`, `2026 Cost Efficiency`, `Visit Reasons 2026`, raw `Matched Detail` + `Unmatched Zocdoc`).
All figures were **independently recomputed from the row-level data and match the workbook's
tables exactly**. The 7/20 "SM" file is the base analysis plus the three review tabs; underlying
data is identical in both uploaded versions.
**Visual decision aid:** `https://claude.ai/code/artifact/942b53ec-dc23-46af-b205-66f57dce6b93`

---

## TL;DR

Remove **7 visit reasons account-wide** plus **2 provider-specific listings** (Dr. Salar and
Dr. Munk on "Orthopedic Consultation (Spine & Back)") from Zocdoc **Marketplace/Discovery**
(search, Sponsored, partner syndication). In 2026 the set is **8.8% of marketplace spend but only
4.3% of kept patients** — it converts at **33% vs 60% for everything else** and costs **$225 per
kept patient, double the $110 marketplace average**. H1 spend $7,878 → **≈$15,750/yr annualized**.
Marketplace capture improves 57.6% → 59.6% and cost per kept drops $110 → $104.

Spine coverage is not reduced: the structured spine consult reasons stay live and convert better.

## 2026 marketplace baseline (Jan–Jun)

$89,876 spend · 1,869 bookings (1,376 new) · **57.6% effective capture** (820 of 1,424 matched) ·
**$110 per kept patient** · **$36,524 spent on bookings that never became a visit** ·
**604 blocked slots**.

## The removal list (2026 figures)

Effective capture = booked patient kept a visit within 45 days, **including** later self-reschedules
and staff rebooks (generous). Capture measured on NextGen-matched bookings; cost is fully loaded.

| # | Visit reason | Service line | 2026 spend | 2026 capture (kept/matched) | 2026 $/kept |
|---|---|---|---|---|---|
| 1 | Pain Management Consultation | Pain Management | $3,131 | 38.5% (20/52) | $157 |
| 2 | Back Pain | Spine/Back/Neck | $2,222 | 34.6% (9/26) | $247 |
| 3 | Surgery Consultation | Orthopedics General | $404 | **0% (0/5)** | — |
| 4 | Ultrasound | Other | $404 | **0% (0/6)** | — |
| 5 | Acupuncture | Other | $202 | 50% (1/2) | $202 |
| 6 | Pain Medication Prescription | Other | $101 | (1/1) | $101 |
| 7 | Chronic Pain | Other | $101 | 0% (0/1) | — |
| 8 | Ortho Consultation (Spine & Back) — **Dr. Salar only** | Spine/Back/Neck | $808 | 37.5% (3/8) | $269 |
| 9 | Ortho Consultation (Spine & Back) — **Dr. Munk only** | Spine/Back/Neck | $505 | 16.7% (1/6) | $505 |
| | **Total removal set** | | **$7,878** | **32.7% (35/107)** | **$225** |
| | *Marketplace average* | | *$89,876* | *57.6% (820/1,424)* | *$110* |
| | *Marketplace after removal* | | *$81,998* | *59.6% (785/1,317)* | *$104* |

### Which calls are statistically firm on 2026 data alone

Screening every reason with a 90% Wilson upper bound against the 57.6% benchmark — "is this below
average even in the best case this sample allows" — **five reasons are certain underperformers,
and all five survive the shorter window:**

| Reason | 2026 spend | Kept/matched | Capture | Upper bound | On the list? |
|---|---|---|---|---|---|
| **Annual Physical** | $8,505 | 93/218 | 42.7% | 48% | **No — see §Annual Physical** |
| Pain Management Consultation | $3,131 | 20/52 | 38.5% | 50% | Yes |
| Back Pain | $2,222 | 9/26 | 34.6% | 51% | Yes |
| Surgery Consultation | $404 | 0/5 | 0% | 35% | Yes |
| Ultrasound | $404 | 0/6 | 0% | 31% | Yes |

**What the 2026-only window changes:** items 5–7 (Acupuncture, Pain Medication Prescription,
Chronic Pain) are **near-dormant in 2026** — $404 of combined spend on 4 bookings. There is
effectively no 2026 evidence for or against them. They stay on the list on **service-fit grounds**
(medication-seeking bookings; acupuncture isn't a listed SHP service line), and removal is cheap
insurance against recurrence — but do not defend them to Zocdoc with conversion data. The honest
line is: *"these barely book any more; we'd rather they weren't bookable at all."*

### Why each one

1–2. **Pain Management Consultation & Back Pain** — the two material offenders and the two most
expensive kept patients we buy in 2026. "Back Pain" is the *generic symptom* reason; spine demand
still reaches us through **Ortho Consultation (Spine & Back)** and **Spinal Cord Surgery
Consultation** (57.6% capture, $69/kept in 2026 — one of the most efficient reasons in the
channel), so part of this demand re-routes rather than disappears. Pain is also a declining,
non-priority service line per the June 2026 audits.
3–4. **Surgery Consultation & Ultrasound** — **zero kept patients in 2026** on 5 and 6 matched
bookings respectively. Ultrasound requires an order; it is not a self-book acquisition service.
5–7. **Acupuncture, Pain Medication Prescription, Chronic Pain** — service-fit removals, see the
caveat above. Confirm with clinical ops that acupuncture is genuinely not offered before sending.

## Per-provider view (how Zocdoc will actually action this)

Zocdoc configures visit reasons **per provider profile**, so the request is provider-explicit.
Figures below are **2026 Jan–Jun**.

### A. The 7 account-wide removals — who booked them in 2026

| Visit reason | 2026 bookings by provider (kept/matched) |
|---|---|
| Pain Management Consultation | Dr. Kevin Lee (10/31) · Dr. Hanish Singh (4/5) · Dr. Brian Kassa (2/6) · Dr. Joseph Yacisen (1/5) · Dr. Anthony Oddo (3/4) · Dr. Lucia Zamorano (0/1) |
| Back Pain | Dr. Mohamed Salar (2/8) · Dr. Scott McCarty (2/6) · Dr. Andres Munk (1/5) · Dr. Jeffrey Varghese (1/3) · Dr. Joseph Maslak (2/2) · Dr. Kevin Lee (0/1) · Dr. Anthony Oddo (1/1) |
| Surgery Consultation | Dr. Benjamin Mayo (0/3) · Dr. Joseph Maslak (0/1) · Dr. Jeffrey Varghese (0/1) |
| Ultrasound | Dr. Benjamin Mayo (0/6) |
| Acupuncture | Dr. Anthony Oddo (1/2) |
| Pain Medication Prescription | Dr. Anthony Oddo (1/1) |
| Chronic Pain | Dr. Anthony Oddo (0/1) |

**Important:** these are 2026 *bookings*. The reasons remain **configured** on other providers'
profiles too (Dr. Yacisen on Ultrasound and Chronic Pain, Dr. Kassa on Pain Medication Prescription
and Acupuncture, and several more on Back Pain — all booked in H2-2025 but not in 2026). Ask Zocdoc
for **account-wide** removal so dormant-but-listed configurations are cleared as well.

### B. Provider-specific removals (reason stays live for all other providers)

| Provider | Visit reason to remove | 2026 | Why safe |
|---|---|---|---|
| Dr. Mohamed Salar, MD | Ortho Consultation (Spine & Back) | 37.5% (3/8), $269/kept, $808 | Keeps Spinal Cord Surgery Consultation, Sciatica, Lower Back Pain, Spine Specialist Consultation, Neck Pain |
| Dr. Andres Munk, MD | Ortho Consultation (Spine & Back) | 16.7% (1/6), $505/kept, $505 | Keeps Spinal Cord Surgery Consultation (his best reason), Ortho (Neck), Sciatica, Back Problems, Neck Pain |

Account-wide this reason runs 52% capture / $154 per kept in 2026 — itself below par (it is on the
renegotiation list). Salar and Munk are the weakest listings on it; removing just their two
profiles lifts the rest.

### C. Consequences leadership must sign off on knowingly

**On 2026 data this is sharper than the annual view suggested.** After the removals, four
providers have **essentially no paid marketplace presence left in 2026**:

| Provider | 2026 MP bookings removed | Remaining 2026 MP spend |
|---|---|---|
| Dr. Brian Kassa, DO | **11 of 11 (100%)** | **$0** |
| Dr. Kevin Lee, MD | 41 of 44 (93%) | $202 |
| Dr. Hanish Singh, MD | 12 of 13 (92%) | **$0** |
| Dr. Anthony Oddo, DO | 23 of 30 (77%) | **$0** |

Their profiles retain other listed reasons (which booked in 2025 but not 2026), so they are not
de-listed — but **this decision effectively exits the pain-management group from paid marketplace
discovery.** That is consistent with strategy (pain is declining and non-priority; these four run
37–48% capture), but it is a **service-line decision, not a cleanup**. Get it said out loud.

By contrast Dr. Salar keeps 60% of his 2026 volume and $1,515 of spend; Dr. Munk keeps 45% and
$505; Dr. Mayo and Dr. Yacisen lose only 7% and 5% respectively.

## Annual Physical — the biggest line item, and not a marketing call

| Measure | 2026 (Jan–Jun) |
|---|---|
| Spend | **$8,505 — 9.5% of all marketplace spend**, 100% Dr. Tony Abood |
| Capture | **42.7%** (93 of 218) — worst of any major reason, but **up from 37.8% in H2-2025** |
| Never kept | **125 patients** — 21% of all blocked slots in the channel |
| Cost per kept | **$91 — well below the $110 average** |
| At benchmark capture | +33 more patients from the same spend, $68 each |

**Recommendation: don't pull it — put it on the clock.** It is the firmest statistical
underperformer in the account, but at $91 a patient the economics are fine and **the trend is
improving** (37.8% → 42.7%). The problem is show rate, which is an operations fix (faster
confirmation, reminder cadence, waitlist backfill). Set a floor — **50% capture by the Q4
export** — and remove it if the number hasn't moved.

The strategic question underneath is leadership's: growth priority is spine and ortho, and this is
primary care on one provider. If PCP acquisition is off-mission, this is a one-line addition to the
same Zocdoc request.

## Recommended addition — 20 non-acquisition reasons ($1,089 in 2026, ≈$2,200/yr)

We are paying a new-patient finder's fee for imaging report reviews, injections, follow-ups and
paperwork. Small money, but a category error: nothing is lost by removing them.

| Group | # reasons (2026) | 2026 spend | Kept/matched |
|---|---|---|---|
| Imaging & report reads — MRI Report (Knee / Back-Spine / Shoulder) | 3 | $505 | 3/5 |
| Follow-ups & second opinions — Orthopedic / Foot / Spine / Trauma / Hand Follow Up, Hip & Knee Surgery Follow Up, Orthopedic Second Opinion | 7 | $202 | 2/2 |
| Weight-loss & wellness (all Dr. Abood) — Weight Loss, Obesity / Weight Loss, Wellness Care, Medicare Annual Wellness | 4 | $180 | 2/7 |
| Injections & procedures — Pain Medicine Injection, Cortisone Shots, Back Injection, Joint Injection | 4 | $101 | 2/5 |
| Admin & accident — Motor Vehicle Accident, Car Accident Injury | 2 | $101 | 0/2 |
| **Total** | **20** | **$1,089** | **9/21 (43%)** |

Follow-ups keep at 2/2 and are *still* wrong to buy — those are existing patients we'd have seen
anyway. **A further 10 reasons in this family booked in 2025 but not 2026** (CT Scan Report – Head,
X-ray, MRI Report – Other, Epidural/Knee/Facet Injection, Worker's Comp Evaluation, Pain Medicine
Follow Up, Yearly Wellness Visit) — still listed, so include them in the same account-wide ask.

## Not for removal — renegotiate the price instead

Converting acceptably but costing too much per kept patient in 2026: **Ortho Consultation (Spine &
Back)** $154 · **Knee Problems** $185 (46%) · **Ortho (Arm & Elbow)** $162 · **Carpal Tunnel** $152
· **Back Problems** $168 · **Wrist Pain** $168 (38%). Plus the high-volume consults: Ortho Leg &
Knee $139, Shoulder $135, Hand & Wrist $133, Foot & Ankle $130, Toenail Problem $145, Ingrown
Toenail $112, Foot Consultation $115.

**Keep (efficient in 2026):** Hand Surgery Consultation $34/kept · Primary Care Consultation $68 ·
Foot Problems $69 · Spinal Cord Surgery Consultation $69 · Ortho Consultation $82 · Knee Pain $88 ·
Foot Pain $89.

**New watch item:** Pediatric Orthopedics Consultation — **0 kept of 3** in 2026 ($202). Too small
to act on; revisit with the Q3 export.

## One provider needs a profile clean-up, not a reason removal

**Dr. Joseph Yacisen** is the worst-performing high-spend provider on the 2026 marketplace:
**$8,282 spend, 49% capture, $162 per kept patient** (vs. Dr. Leff at 70% / $116 on nearly twice
the spend). He is listed under **39 reasons in six months**, 21 of which booked exactly once.

His generic **"Orthopedic Consultation" kept 0 of 8 in 2026** — patients booking a general ortho
slot with a hand and foot specialist land in the wrong place.

**Suggested ask:** prune his profile to the reasons that match his practice (hand/wrist,
foot/ankle and the sub-specialty consults that keep well) rather than removing reasons one at a
time. **Confirm scope with Dr. Yacisen before sending.** Note the "reasons listed" count is
naturally noisier over six months — Dr. Mayo shows 59% once-only bookings on a healthy 64% capture
— so the case here rests on the outcome metrics ($162/kept, 49% capture, 0/8 on the generic
reason), not the count alone.

## What it adds up to (2026)

| | 2026 spend | Annualized | Share of spend | Share of kept patients |
|---|---|---|---|---|
| Removal set (7 + 2 provider) | $7,878 | ≈$15,750 | 8.8% | 4.3% |
| Recommended addition (20 non-acquisition) | $1,089 | ≈$2,180 | 1.2% | 1.1% |
| **Combined** | **$8,967** | **≈$17,930** | **10.0%** | **5.4%** |
| On the clock (Annual Physical) | $8,505 | ≈$17,010 | 9.5% | 11.3% |

Combined removal lifts marketplace capture **57.6% → 59.9%** and drops cost per kept **$110 → $104**.

## Scope — critical detail for the Zocdoc request

Removal applies to **Marketplace/Discovery surfaces only**: Zocdoc Marketplace search, **Sponsored/
boosted placements**, and partner discovery syndication ("Google and others" / Healthgrades in our
export). **Do not touch the direct booking flow from synergyhealth.org** — the website path is
$0-cost and captured **73.2% in 2026** vs. the marketplace's 57.6%. If a reason can't be scoped
that way, decide reason-by-reason (Ultrasound and Pain Medication Prescription come out everywhere).

## Verification after the change

1. Zocdoc confirms effective date in writing + that **no per-booking fees accrue** on these reasons
   after that date; already-booked future appointments unaffected.
2. Next monthly export: these reasons go to zero on Marketplace/Discovery rows; spot-check that
   spine demand shifts into the structured consult reasons.
3. GA4 `zocdoc handoff` events and website-source bookings unaffected (website path out of scope).
4. Update this memo + `pm/master-task-list.csv` B2C-B.2 when confirmed.

**The email draft to send:** `pm/zocdoc-enterprise-removal-email-2026-07.md`

*Compliance note: all figures are de-identified aggregates (patient hashes only in source data —
no PHI in this memo or the email). Internal working analysis, not cleared to publish.*
