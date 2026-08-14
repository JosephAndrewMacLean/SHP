# Spine Influence Tracker — weekly visits vs. new-patient referrals

**Data:** `pm/spine-influence-weekly.csv` · **Owner:** Joe MacLean · **Started:** Aug 14, 2026
**Purpose:** one row per week showing what the PL team put in (field visits, by PL and by
target tier) next to what came out (new patients by service line), so the visit→referral
influence is visible as the program runs.

## The three visit levels (why numbers differ from MMC's raw count)

MMC logs one activity row **per person greeted** at a stop — walk into a clinic, check in
three providers, that's 3 "visits" in MMC. The tracker carries all three levels so it ties
out against what the team sees:

| Level | Column(s) | Definition |
|---|---|---|
| **Check-ins** | `checkins_total`, `checkins_<pl>` | Raw completed Visit rows — matches MMC's own activity counts. |
| **Stops** | `stops_total`, `stops_<pl>` | Unique account-days: one practice visited on one day = 1, no matter how many people were greeted. The honest "how many places did we go" number. |
| **Book stops** | `book_t1/t2/t3/prospect`, `book_total` | Stops at accounts **on the 862-account spine target book**, split by the account's current tier. |

Example (week of Aug 3): 482 check-ins → 103 stops → 84 book stops. All three are true;
they answer different questions.

## Remaining columns

| Column | Definition |
|---|---|
| `week_start` | Monday of the week. |
| `program_week` | Route-plan week label (W1 = week of Aug 3, 2026). Blank = pre-program backfill. |
| `offbook_stops` | Stops at companies **not on the spine target book** — includes accounts deliberately exited to Non-Spine and anything never added. Shrinking = book coverage improving (75/wk in June → 11 in W2); a spike feeds the Friday off-book watch list. |
| `newpts_total` | New patients on that week's B2B results report (by appointment week). |
| `newpts_spine / podiatry / ortho_other / telehealth` | Same patients split by the **service line of the treating SHP provider** (spine = Salar, Maslak, McCarty, Varghese, Zamorano; telehealth = the attorney/auto intake channel). |
| `newpts_pl_touch60` | Of that week's new patients, how many came from a referring provider with a completed PL visit ≤60 days before the appointment — our attribution proxy. |
| `newpts_spine_pl_touch60` | Same, spine only. |
| `newpts_source` | Which results report filled the row. Blank = no report covering that week yet. |

## Weekly update (part of the Friday refresh)

1. Fresh MMC activities export → recompute the closing week's visit columns (append the new
   row; earlier rows only change to correct data, never restart).
2. When the week's B2B results report arrives, match referrers → fill the `newpts_*` columns
   for the appointment week(s) it covers.
3. Aggregates only in this file — no patient names, chart numbers, or visit-level patient
   detail, ever.

## Caveats

- **Pre–Aug 3 `newpts_*` rows are carryover entries** that happened to appear in the Aug 14
  report (attorney/telehealth intake), not full-week counts. W1 (Aug 3) is the first real
  outcome week.
- `pl_touch60` is **correlation, not proven causation** — read trends, not single cells.
- Spine converts slower than other lines (median ~43 days visit→appointment vs ~30 overall),
  so expect the spine columns to respond to a T1 visit ramp ~4–6 weeks later.
- Sean's columns exist for pre-July backfill; historical reps before Jun 2026 (Jim, Kessia,
  etc.) are out of the backfill window entirely.
