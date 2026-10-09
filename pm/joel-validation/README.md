# Validation Sprint — Spine Target Accounts by PL (Joel C.)

**Owner:** Joe MacLean · **Assigned:** Joel C. · **Created:** 2026-07-21
**Working file:** `Spine-Target-Validation_Joel_v1.xlsx` (this folder)

## What this is
The 848-account referral-weighted book (Kristen 180 · Jasmine 310 · Coty 318 · Sean 40),
converted into **per-PL review queues** so each PL dispositions every account
(Keep / Remove / Reassign) using market knowledge, before full-scale outreach.

The workbook pre-fills everything we know per account — tier, evidence band, 2026
spine/ortho/B2B counts, last spine patient, last visit + days since, visit→appointment lag,
planned cadence, route day, known referring providers, and **54 auto pre-flags** from the
Jul 20 scrub criteria (pediatric ×24, in-house-spine verify ×15, possible competitor ×10,
neurosurgeon ×4, addiction ×2) plus Medicaid-likely payer flags. Yellow columns + dropdowns
are the PLs'. Summary tab auto-counts dispositions.

## Realistic timeline (adjusted from the request — two changes, both deliberate)
| Date | Milestone |
|---|---|
| **Wed Jul 23** | Review files distributed (**one day earlier** than requested — buys the weekend) |
| Thu Jul 24 | Walk-through at team debrief · Sean decision lands (gates his 40-account tab) |
| **Tue Jul 29 EOD** | PL dispositions complete (~60–90 min/day office time; the W1/W2 protect sweep is NOT paused for this) |
| Wed Jul 30 | Joel consolidates; resolves cross-PL conflicts (one account = one owner) |
| **Thu Jul 31** | Approved universe locked · routes regenerated (scripted) · summary to Joe + Kristen |
| Aug 3 → Sep 30 | Execution on the cleaned universe |

**The decision the Sept-30 deadline depends on (flag at Jul 31 sign-off, not after):**
"complete outreach by Sep 30" is only true under one of two explicitly chosen modes —
**A) protect-first** (current build: producers on 14/21-day cycles, ~3 spine days/PL/wk,
~270 of 466 prospects touched, tail rolls to Oct) or **B) full-coverage-once**
(every kept account visited: needs ~4.5–5 spine days/PL/wk from Aug 3 and thinner
producer cadence). Promising B while resourcing A is the failure mode.

## Route regeneration (Jul 30–31)
Scripted from the approved universe: rebuild `pm/pl-weekly-visit-schedule.csv` +
`pm/pl-route-days.csv` with removed accounts dropped, reassignments moved (one owner),
≤10 stops/day, protect-first ordering preserved. The Spine Routes app and MMC import
regenerate from the same files in minutes.

## Acceptance criteria coverage
Every account dispositioned with reason (queue columns) · no dual ownership (consolidation
step) · Tier 1/2 protected throughout (they stay on the live calendar during review) ·
last visit / frequency / referral history / lag visible (pre-filled) · final summary =
Summary tab + regenerated route-day counts · ">1 visit before Sep 30" list = all final
Tier 1 & 2 (14/21-day cadence implies 3–5 visits).
