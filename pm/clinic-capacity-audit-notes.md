# Clinic Capacity Audit — Ortho & Spine (workbook notes)

**File:** `pm/Clinic_Capacity_Audit.xlsx` · **Built:** 2026-08-10, updated 2026-08-11 (Zamorano/Munk
excluded from spine counts) · **Status:** ready for Kelley/Katie use

A 16-week physician clinic-capacity audit workbook (weeks of Aug 10 – Nov 23, 2026), rebuilt from
Katie/Kelley's template with the Ortho & Spine physician roster embedded. Kelley (scheduling / call
center) enters the yellow cells; Katie (operations) reviews statuses; the Dashboard connects capacity
to new-patient performance for the executive view.

## Business rules (centralized on the Start Here tab, referenced by every formula)

- Clinic-day measure: full day = 1.0, half-day = 0.5; not weighted by physician/location/day.
- Spine: 9 days/week standard, 8 = exception floor. ≥9 Meets · 8–<9 Exception · <8 Below Floor.
- Ortho: 16 required with 0 physicians out · 15 with 1 out · 14 with 2 out · >2 out = PTO/Coverage
  Review. Blank "physicians out" is treated as 0 (full roster required).
- New-patient success benchmarks: Spine 60+/week, Ortho 130+/week.
- Historical Benchmarks tab computes average clinic days during successful weeks to validate the
  standards.

## Physician Roster tab (the addition this branch is for)

Ortho & Spine physicians only, from `brand/provider-roster-by-service-line.md` (July 15, 2026
synergyhealth.org crawl), cross-checked against the Sept 7 ASC/clinic schedule — all 17 listed
physicians appear on that schedule:

- **Spine surgeons counted (4):** Varghese, Salar, Maslak, McCarty. Spine new-patient YTD counts
  included (counted surgeons total 1,260; volume ≠ conversion).
- **Not counted toward Spine capacity (practice direction, Aug 11, 2026):** Zamorano (neurosurgeon)
  and Munk — kept on the tab for reference since both are on the Sept 7 schedule, with their NP
  figures (51 / 113) excluded from the spine totals.
- **Spine interventional pain (4):** Oddo, Lee, Kassa, Singh.
- **Ortho surgeons (7):** Jeffrey/David/Stephen/Alice Mendelson, Bhullar, Mayo, Yacisen — the 7 behind
  the "16 days with 0 out" assumption.

**Confirm with the practice** (flagged on the tab): J. Heyl (on the Sept 7 schedule, Sept 1 start, not
on the website roster), S. Zaremba (schedule-only, Pain), and an Ortho block labeled "Jerry" with no
matching roster name.

Excluded by request: hand, foot & ankle, primary care, PT/OT, PA staff.

## Notes

- No PHI: physician-level schedule/roster data only; new-patient counts are aggregates.
- The Sept 7 schedule workbook itself is not committed (operational file, lives with the practice).
