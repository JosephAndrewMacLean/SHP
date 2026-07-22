# Reputation / Review-Velocity Baseline — July 2026 (from Rater8)

**What this is:** the first measured baseline for Cardinal's Phase-3 **review velocity
program**. Cardinal's KPI framework lists *"Review velocity per location — Baseline:
unknown"* and slots BirdEye/Podium as the instrument; our stack fills that slot with
**rater8**, and its first exports landed 2026-07-22 (`data/rater8/2026-07-22/`).
Companion asset: `brand/gbp-profile-directory.md` (all 50 GBP listings, links, Place IDs).

**Data window:** 85 reviews pulled 2026-07-22; velocity math uses the 54 reviews carrying
exact dates (Jun 27 – Jul 21, 2026). ⚠️ Export appears filtered (every review is 5★ /
"Happy") — treat volumes as a floor and see caveats in the data README.

---

## 1. Headline: the program Cardinal asked for is already running — unmeasured and with gaps

Cardinal Phase 3 says *"Implement review velocity program with HIPAA-safe protocol…
BirdEye, Podium, or similar."* The rater8 stack **already does the collection mechanics**:
review requests are routed and balanced across 50 Google listings (22 physicians ×
locations + 5 location profiles) **and** non-Google platforms, and Google reviews get
fast owner responses. What's missing is not a tool — it's **targets, coverage, and an
SOP**:

| Cardinal ask | Status 2026-07-22 |
|---|---|
| Review program running, tied to care milestones | 🟠 Running in rater8 (request routing + balancing live). Milestone timing (3–5 days post-visit / 4–6 wks post-procedure) unverified — ask rater8 rep how request triggers are configured |
| Baseline per location | ✅ **Now measured** (below) — was "unknown" |
| Steady monthly growth per location | ❌ No targets set; now settable |
| Platform diversification beyond GBP (Healthgrades/Vitals/WebMD/Doximity — HIGH) | 🟠 **Better than Cardinal assumed**: 28% of dated reviews land on WebMD/Healthgrades/Vitals by design (rater8 routes there). Doximity unverified |
| HIPAA-safe response protocol before launch | 🟠 Responses are live (likely automated) with no documented SOP — see §4 |

## 2. Velocity baseline (the number that was "unknown")

**~15 dated reviews/week org-wide** (54 in 25 days), all 5★ in this export, avg rater8
sentiment 0.97/1.0.

| Cut | Reviews (of 85) | Notes |
|---|---|---|
| Google | 70 (82%) | 40 have owner responses (57%), median response same-day |
| WebMD / Healthgrades / Vitals | 9 / 4 / 2 (18%) | Zero owner responses on these platforms |
| SHP: Livonia | 38 | Largest volume — matches its 47% share of location review routing |
| SHP: Sterling Heights | 23 | |
| SHP Clinic: Southfield | 8 | Podiatry-heavy (Southfield is the near-term deepening market) |
| SHP Clinic: Port Huron | 1 | |
| **SHP Clinic: Troy** | **0** | **No GBP linked in rater8 + 0.8% routing → structurally zero reviews in the #1 growth market** |
| (no location — non-Google sites) | 15 | Platform exports don't carry location |

**Per-physician (provider-attributed reviews, ~4 weeks):** Oddo 6 · S. Mendelson 6 ·
Salar 5 · A. Mendelson 4 · Lee 4 · Bohm 4 · Klein 3 · D. Mendelson 3 · J. Mendelson,
Yacisen, Sorensen, Kassa, McCarty, R. Leff, Abood 2 each · Munk, Singh, Mayo 1 each ·
**Varghese, Maslak, Bhullar, Green 0**.

**Spine lens (the growth priority):** the 5 spine surgeons in the program earned only
**8 of 52** provider-attributed reviews — and two of them (**Varghese, Maslak**) got zero,
while **Zamorano isn't enrolled in rater8 at all**. Spine review velocity trails the
pain/ortho bench exactly where local trust signals matter most for the spine plan.

## 3. What the reviews say (theme frequency across all 85)

Patient language corroborates the brand differentiators — this is the third-party
corroboration Cardinal says the "96% recommend" claim lacks (*"not surfaced… where AI
systems look"*):

- **Explains clearly / educates** — 41% of reviews
- **Listens / doesn't rush** — 39%
- **Would recommend / trust** — 36%
- **Staff friendliness** — 26%
- **Fast access / short waits** — 11% *(note: "same-week access" is the brand's #2
  differentiator but shows up least in review language — worth watching)*
- Outcome/relief mentions — 6%

Use for: AggregateRating/review schema inputs (Cardinal Pillar 6, agency-owned), AIO/GEO
corroboration, and creative ("what patients actually say" — real, typical, FTC-disclosed;
never scripted).

## 4. Response practice — working, but pre-SOP

40 of 70 Google reviews (57%) carry owner responses, median lag same-day (max 4 days) —
the response texts read templated/automated (likely rater8 auto-response). The unanswered
set is concentrated on one profile: **the SHP: Livonia location listing (0 of 25
responded)**, while provider-attributed reviews run ~89% responded — so response coverage
is a single-profile configuration fix, not a broad process problem. Cardinal flags
a MEDIUM risk here: responses must **never confirm a patient relationship** (HIPAA), and
negative reviews need a private-resolution invite. This export contains no negative
reviews, so the SOP is untested where it matters most. Before scaling: write the
HIPAA-safe response SOP (Cardinal's spec), spot-check the auto-response templates against
it, and decide whether the 43% unanswered Google reviews + 0% non-Google responses are
deliberate.

## 5. Actions (small, owned)

1. **Troy (P1, already task GOV-A.1 — Paul, due 7/26):** this data is the evidence — no
   GBP linked in rater8, 0.8% routing, zero reviews. After the profile fix, have the
   rater8 rep link it and raise Troy's routing share.
2. **Coverage (Joe + rater8 rep):** enroll Rochester (and any other missing locations),
   **Lucia Zamorano** (spine!), and Fred Leff; verify Alice Mendelson's Livonia pin
   (details in `brand/gbp-profile-directory.md` gaps list).
3. **Data feed (Joe → rater8 rep):** confirm what filter "Patient Feedback report #18"
   applies; request an **unfiltered** scheduled weekly export or API access
   (`docs/data-sources-roadmap.md` §5). Also ask how request timing maps to Cardinal's
   care-milestone spec (3–5 days post-visit / 4–6 weeks post-procedure).
4. **HIPAA-safe response SOP (Marketing + compliance review):** document per Cardinal's
   spec; audit the auto-response templates; set response-coverage policy. Draft = good
   `pr-specialist` task, human compliance review required before adoption.
5. **Targets (set at next monthly tracker re-verify):** per-location monthly review
   velocity vs. this baseline; spine-surgeon share of provider reviews (8/52 today).

---

*Update cadence: refresh with each rater8 drop in `data/rater8/<date>/`; statuses roll up
to `audits/cardinal-recommendation-tracker.md` (§4 review-velocity gate, §7 instruments).*
