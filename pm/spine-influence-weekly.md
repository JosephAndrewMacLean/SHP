# Spine Influence Tracker — weekly visits vs. new-patient referrals

**Data:** `pm/spine-influence-weekly.csv` (weekly totals + per-PL splits) ·
`pm/b2b-newpts-by-company-weekly.csv` (new patients aggregated by referring company) ·
**Owner:** Joe MacLean · **Started:** Aug 14, 2026

## Definitions

**Check-in = a company visited on a day.** MMC logs one activity row per *person* greeted
at a stop; those person rows are collapsed and never counted here. One clinic on one day = 1
check-in, however many people were seen. (Week of Aug 3: 482 MMC activity rows → 103
company check-ins.)

**Every check-in is classified into exactly one bucket, and every bucket is split by PL** —
the buckets always sum to the check-in total, so nothing drops out of the table:

| Bucket | Meaning |
|---|---|
| `t1 / t2 / t3 / prospect` | Check-in at an account on the 862-account spine target book, by its current tier. |
| `nonspine` | Check-in at an account deliberately exited to the Non-Spine group. |
| `unlisted` | Check-in at a company on neither list — the ortho book, other campaigns (senior housing, OB/GYN, Ann Arbor), attorneys not yet added, and true gaps. June ran ~74/week unlisted; by W2 it's 9 — the book now covers what the team works. Spikes feed the Friday off-book watch. |

Column pattern in the CSV: `<bucket>_total`, `<bucket>_kristen`, `<bucket>_jasmine`,
`<bucket>_coty`, `<bucket>_sean` (Sean = pre-July backfill only), plus `checkins_*` overall.

## New-patient columns (from the weekly B2B results report)

Counted from the referring **people** on the report, then aggregated to their **company**:

- In the weekly CSV: `newpts_total`, split by treating service line — `newpts_spine`
  (Salar / Maslak / McCarty / Varghese / Zamorano), `newpts_podiatry` (DPMs),
  `newpts_ortho_other`, `newpts_telehealth` (attorney/auto intake) — placed in their
  **appointment week**; plus `newpts_pl_touch60` (referrer had a completed PL visit ≤60
  days before the appointment — the attribution proxy) and `newpts_spine_pl_touch60`.
- In `b2b-newpts-by-company-weekly.csv`: one row per referring company per report —
  company, book tier & PL, practice type, new patients by line, last PL visit, shortest
  visit→appt lag. Referrers with no CRM record get their own rows (add-to-book feed).
  New report weeks append; prior rows are never rewritten.

## Weekly update (part of the Friday refresh)

1. Fresh MMC activities export → append the closing week's check-in row (earlier rows only
   change to correct data, never restart).
2. Weekly B2B results report → fill that appointment week's `newpts_*` columns and append
   the company rollup rows.
3. Aggregates and referrer-side data only — no patient names, chart numbers, or
   patient-level detail, ever.

## Caveats

- Pre–Aug 3 `newpts_*` values are carryover entries appearing in the Aug 14 report
  (attorney/telehealth intake), not full-week counts — W1 (Aug 3) is the first real
  outcome week.
- `pl_touch60` is correlation, not proven causation — read trends, not single cells.
- Spine converts slower (median ~43 days visit→appt vs ~30 overall), so expect spine
  outcomes to respond to a T1 visit ramp ~4–6 weeks later.
