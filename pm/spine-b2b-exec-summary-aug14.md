# Spine B2B Referral Program — Executive Summary

**Date:** Aug 14, 2026 · **Prepared by:** Joe MacLean · **Audience:** CEO, Head of Analytics
**Program:** 3 physician liaisons working an 862-account tiered spine target list on routed
weekly visit plans (live since Aug 3). Internal aggregate data only — no patient-level detail.

## Five numbers

1. **91% of last week's new patients came from a provider our liaisons had visited.**
   (68 of 75 referring providers on the Aug 14 new-patient report; 65% visited within 60 days
   of the appointment.)
2. **A liaison visit converts in about a month.** Median time from visit to new-patient
   appointment: 30 days. Half of conversions land within 30 days of a touch; 72% within 60.
3. **Spine referrals take ~6 weeks — slower than every other line.** Median 43 days
   (vs. 25 ortho/other, 16 podiatry). A spine target that hasn't referred after one visit is
   mid-cycle, not cold.
4. **Routing doubled time-on-target at the same effort.** Tier-1 visits went from ~15/week
   (June–July average) to 32 in the latest week; visits outside the plan fell from ~42/week
   to 9. Total volume held (~110–120 company visits/week).
5. **Spine was 31% of the report** (23 of 75 new patients), and Tier-1 accounts — 19% of the
   target list — produced 61% of the on-list referrals. The tiering is pointed at the right
   accounts.

## The coverage finding

**13 of the 23 spine patients came from practices that weren't on the target list** (8 from
practices in the CRM but off-list, 5 from practices with no CRM record at all). That is the
system working as designed: each weekly report now feeds the practices it discovers back onto
the target list — **22 practices queue for addition this week**. Watch this number shrink as
list coverage matures.

## What to expect

- **Spine lift from the visit ramp should surface ~mid-September** (Tier-1 visits doubled in
  early August; spine converts on a ~6-week lag).
- This is tracked in **one weekly table** — visits by tier next to spine referrals
  (`pm/spine-influence-weekly.csv`), updated every Friday, so influence becomes a trend line
  rather than an anecdote.

## For analytics (definitions & sources)

- **Sources:** Map My Customers activity export (completed field visits) × weekly new-patient
  report (referring provider, treating provider, appointment date).
- **A visit** = one company on one day (CRM person-level rows are deduplicated).
- **Attribution proxy** = referring provider had a completed liaison visit ≤60 days before the
  appointment. This is correlation, not proven causation; long-lag matches (>180 days) are
  treated as legacy, not program wins.
- **Match rate:** 68/75 referrers matched to CRM records (name/practice matching; no patient
  data used). The 7 unmatched are themselves an output — the add-to-list feed.
- **Known data limitations** are logged separately with the data-ops cleanup list
  (`pm/mmc-data-ops-cleanup.md`); the two highest-leverage fixes are capturing referrer NPI
  at intake and adding a Tier field in the CRM.
