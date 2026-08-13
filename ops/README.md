# Clinical Operations — SOPs & scheduling ground truth

Clinical Operations documents that govern clinic scheduling and patient access at
SHP. They live in this marketing workspace because scheduling capacity **is** the
marketing constraint: clinic days determine new-patient slot inventory, and the
utilization SOP names the Marketing Team as a formal escalation path.

## Documents

| File | What it is | Status |
|---|---|---|
| [sop-clinic-utilization-schedule-optimization.md](sop-clinic-utilization-schedule-optimization.md) | Daily utilization review: ≥90% target, patients-per-hour and double-booking standards, PA escalation at 100%/85%/70% thresholds, marketing-support triggers | Effective 6/24/2026 · Owner: Director of Clinical Scheduling |
| [sop-physician-pto-patient-accessibility.md](sop-physician-pto-patient-accessibility.md) | Physician PTO rules: 66% clinic-capacity floor per service line, 3-month notice for extended PTO, 16-week rolling coverage audit, escalation ladder | **Draft** — unfilled `[EMAIL ADDRESS]`, no effective date; publish directive issued week of Aug 10 |
| [sop-change-review-2026-08-13.md](sop-change-review-2026-08-13.md) | Reconciliation of both SOPs against the week's Otter/Notion meetings (Aug 5–12): decided changes, open conflicts, verification list | Review queue for SOP owners |

Both SOPs are faithful markdown conversions of the Word originals uploaded
2026-08-13; the Word files remain the formatting source of record. Anything
clinically or operationally substantive stays **draft pending human review** per
workspace rules.

## Why marketing cares — the built-in hooks

1. **Marketing is a named role in the utilization SOP.** When any physician drops
   below **70% schedule utilization**, Clinical Ops is instructed to send the
   findings to the Marketing Team and request: new patient campaigns,
   provider-level promotion, and Provider Liaison (PL) events.
2. **The PTO SOP is a new-patient-access guarantee.** The 66% capacity floor and
   the 16-week audit exist to protect new-patient appointment availability — the
   inventory every campaign in `playbooks/` sells against. The audit calendar is
   forward visibility for campaign timing.
3. **"Marketing Request Intake Process"** is listed in the utilization SOP's
   Related Reports & Tools but doesn't exist yet — a candidate build for this team
   (see change-review memo §3).

## Related

- `playbooks/call-center-strategy.md` — the phone room executes the access these
  SOPs protect (booking-channel scripting, slot protection, recovery queues).
- `playbooks/b2b-physician-liaison-strategy.md` — PL events are a named
  low-utilization remedy; referral demand needs the protected new-patient slots.
- `brand/provider-roster-by-service-line.md` — who's in each service line the PTO
  minimums apply to.
