# Spine Influence Tracker — weekly visits vs. new-patient referrals

**Data:** `pm/spine-influence-weekly.csv` · **Owner:** Joe MacLean · **Started:** Aug 14, 2026
**Purpose:** one row per week showing what the PL team put in (target-account visits by tier)
next to what came out (new patients referred from B2B sources, spine and total), so the
visit→referral influence is visible as the program runs.

## How to read it

| Column | Definition |
|---|---|
| `week_start` | Monday of the week. |
| `program_week` | Route-plan week label (W1 = week of Aug 3, 2026). Blank = pre-program backfill. |
| `visits_t1/t2/t3/prospect` | Completed MMC visits to accounts **in the spine target book**, by the account's current tier. One account-day = one visit (MMC logs a row per person greeted; those are deduped so a 3-provider stop counts once). |
| `visits_book_total` / `unique_book_accounts` | Total book account-days / distinct book accounts touched that week. |
| `visits_offbook` | Account-days at companies **not** in the book (includes Non-Spine-grouped accounts). Shrinking number = book coverage improving; a spike = feed for the off-book watch list. |
| `visits_kristen/jasmine/coty/sean` | Book account-days by visiting PL (Sean retained for pre-July backfill). |
| `newpts_*` | From the weekly B2B results report, matched referrer-side against MMC activity. `b2b_marked` = flagged B2B at intake. `pl_touch60` = the referring provider had a completed PL visit ≤60 days before the appointment (our attribution proxy). `spine` = treating provider in the spine line (Salar, Maslak, McCarty, Varghese, Zamorano). |
| `newpts_source` | Which results report filled the row. Blank = no report covering that week yet. |

## Weekly update (part of the Friday refresh)

1. Fresh MMC activities export → recompute the closing week's visit columns (append the new row; earlier rows only change to correct data, never restart).
2. When the week's B2B results report arrives, match referrers → fill the `newpts_*` columns for the appointment week(s) it covers.
3. Aggregates only in this file — no patient names, chart numbers, or visit-level patient detail, ever.

## Caveats

- **Pre–Aug 3 `newpts_*` rows are carryover entries** that happened to appear in the Aug 14
  report (mostly attorney/telehealth intake), not full-week counts. Treat W1 (Aug 3) as the
  first real outcome week.
- `pl_touch60` is **correlation, not proven causation** — a referrer can convert for other
  reasons; conversely referrals that pre-date the program keep arriving. Read trends, not
  single cells.
- Spine converts slower than other lines (median ~43 days visit→appointment vs ~30 overall
  in the Aug 14 report), so expect `newpts_spine_pl_touch60` to lag the T1 visit ramp by
  ~4–6 weeks.
