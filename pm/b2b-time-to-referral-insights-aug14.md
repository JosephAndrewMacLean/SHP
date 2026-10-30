# B2B: time from PL visit → new-patient appointment

**For:** Santosh, Gautam · **From:** Joe MacLean (PL program analytics) · **Date:** Aug 14, 2026
**Basis:** the Aug 14 new-patient report (75 patients, appointments mostly Aug 3–7) with each
referring provider matched against completed PL field visits in Map My Customers.
Internal referral-operations analytics — aggregate counts only, no patient-level data.

## Headlines

- **91% of new patients came from a provider a PL had already visited** (68 of 75 referring
  providers matched to logged visit history). **65% had a visit within 60 days** of the
  appointment.
- **Median time from PL visit to new-patient appointment: 30 days.** Among fresh
  relationships (visit ≤60 days prior) it's 21 days.
- **Spine converts slower than everything else** — median **43 days**, vs. 25 days for
  other lines and 16 days for podiatry. A spine referrer typically sits ~6 weeks between
  the visit and the first patient arriving.
- Conversion timing distribution (all 68 matched): 0–7 days **13** · 8–30 days **21** ·
  31–60 days **15** · 61–90 days **12** · 90+ days **7**. Half land within a month;
  72% within two.
- **Spine was 31% of the report** (23 of 75 new patients, treating providers Salar / Maslak /
  McCarty / Varghese / Zamorano); 35% of the report was flagged B2B at intake, and the
  visit-history match suggests that flag undercounts — 44 of the 69 W1-week patients had a
  ≤60-day PL touch.
- **Account-level yield:** of 584 unique accounts visited in the five weeks before the report,
  27 (4.6%) produced at least one patient on this single report — a per-week yield, not
  lifetime conversion.

## Time to referral by service line

| Service line | n (matched) | Median visit→appt | Fresh (≤60d) median |
|---|---|---|---|
| Spine | 18 | **43 days** | 30 days |
| Other (ortho / PM&R / etc.) | 37 | 25 days | 20 days |
| Podiatry | 7 | 16 days | 5 days (small n) |
| Attorney / telehealth intake | 6 | 24 days | 21 days |
| **All matched** | **68** | **30 days** | **21 days** |

## Which practice types feed which service lines

Referring practice type (from our CRM classification of the matched referrer) × the SHP
service line the patient was referred **to**:

| Referring practice type | Spine | Podiatry | Ortho / other | Telehealth intake | Total | % to spine |
|---|---|---|---|---|---|---|
| PCP | **12** | 4 | 21 | 0 | **37** | 32% |
| Urgent care | 1 | 2 | 9 | 1 | 13 | 8% |
| No MMC record (unmatched) | **5** | 0 | 2 | 0 | 7 | **71%** |
| Pediatrics | 0 | 1 | 3 | 1 | 5 | 0% |
| Orthopedic | 1 | 0 | 3 | 0 | 4 | 25% |
| Attorney / Legal | 0 | 0 | 0 | 4 | 4 | 0% |
| Pain | 1 | 0 | 1 | 0 | 2 | 50% |
| Chiropractor / PT / other | 3 | 0 | 1 | 0 | 4 | — |
| **Total** | **23** | **7** | **39** | **6** | **75** | 31% |

Reads worth noting:

- **PCPs are the volume engine and the spine engine** — half the report, and a third of
  their referrals landed in spine. The tiered PCP book is pointed at the right people.
- **Urgent care skews ortho, not spine (1 of 13)** — they're valuable, but as a general
  ortho feeder; spine expectations for the UC sweep should be set accordingly.
- **The referrers we've never tracked skew hardest to spine (5 of 7)** — spine patients are
  arriving from providers with no CRM record. Those names go on the add-to-book list each
  week; this row shrinking over time is a health metric for list coverage.
- **Attorney/legal feeds the telehealth intake channel exactly as designed** (4 of 4).

## What this changes

1. **The visit cadence is sitting on the conversion curve.** Tier 1 accounts are worked every
   ~21 days and the median conversion is 21–30 days — most referrals arrive between one visit
   and the next, which is exactly where you want the reminder to land.
2. **Judge spine relationships on a ~6-week clock.** A new spine target that hasn't referred
   after one visit isn't cold — median payoff is two visit cycles out. Hold the cadence
   through the quiet window.
3. **This is now tracked weekly** in `pm/spine-influence-weekly.csv`: target-account visits by
   tier next to that week's B2B spine referrals, updated every Friday refresh, so the
   influence lag becomes visible over time instead of anecdotal.

## Method & caveats

- Matching is referrer-side: provider name / practice → MMC person or company record, then the
  most recent completed visit before the appointment date. 68/75 matched; the 7 unmatched
  have no MMC record (those are add-to-book candidates, three of them spine referrers).
- One report, one week of outcomes — medians will firm up as weekly snapshots accumulate.
- A prior visit is **evidence of influence, not proof of causation**; long-lag matches
  (>180 days, 2 rows) were treated as legacy touches, not program wins.
