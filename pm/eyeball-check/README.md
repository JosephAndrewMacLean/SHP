# Per-PL Spine Eyeball Files — the quick vetting pass

**Created 2026-07-23 (from the Joe/Kristen call).** One file per PL, spine accounts only,
tabbed **Tier 1 / Tier 2 / Tier 3 / Prospects**, sorted highest spine yield first.

**How it works (the whole process):**
1. Each PL opens THEIR file only. Yellow column = **EYEBALL: Spine-worthy?** — dropdown
   **Yes / No / Not sure**. One-line note only where it helps ("has own spine," "closed,"
   "Medicaid-heavy," "worth a look").
2. **MMC Company ID is column A on every row** — everything joins back to Map My Customers
   with zero name-matching.
3. Red-shaded **Auto Pre-Flag** cells = accounts our filters already suspect (pediatric,
   in-house spine, competitor, addiction, Medicaid-likely). Confirm or override — the PL's
   read wins.
4. Files come back to Joe → the **"No" rows auto-generate an MMC import that tags them into
   Kristen's new "Non-Spine" group** (per the call — group, not a field, so nothing else is
   disturbed), and the plan/routes/app regenerate without them. "Not sure" rows go to the
   Jul 31 review with Joel.

This is the lightweight PL-facing step of the validation sprint (`pm/joel-validation/`):
PLs touch these simple files; Joel's master workbook is where consolidation happens.

---

## Results — all four files returned (Jul 31)

**848 of 848 rows answered — zero blanks.** Full verdict log: `eyeball-results-2026-07-31.csv`.

| PL | Yes | Not sure | No |
|---|---|---|---|
| Kristen | 170 | 5 | 5 |
| Jasmine | 298 | 0 | 12 |
| Coty | 170 | 82 | 66 |
| Sean | 40 | 0 | 0 |

*(Sean's 40 reviewed accounts were merged into Kristen's book later on Jul 31 — route days
K-R19…K-R22. His verdicts stand; only the owner changed.)*

What happened with them:
- **766 accounts validated in** (679 Yes + 87 Not sure) → routes/schedule/app regenerated
  (`pm/route-days-v2/`, `pm/pl-route-days.csv`, `pm/spine-routes-app.html`).
- **82 accounts out** → `pm/mmc-import/mmc-non-spine-group-IMPORT.csv` tags them into Kristen's
  **Non-Spine** group (per the promise above — group only, nothing else altered; reversible).
  Removals skew exactly where they should: 74 of 82 are prospects; competitor spine practices,
  podiatry, a closed practice, and one Medicaid-heavy urgent care.
- **1 reassignment, not a removal:** Coty marked **Levan Internists** "No — not my account, being
  called on by Jasmine." It moved into Jasmine's routes (J-R26) **pending Kristen's confirmation**.
- **The lone producer removal:** Blue Water Urgent Care (Tier 1, 1 spine patient, Wave 2) —
  Kristen's note "95% Medicaid." Worth a quick Kelly verification before the import runs, but the
  call is hers and the removal is reversible.
- **Coty's 82 "Not sure" rows stay in his routes** (amber-flagged in his workbook and counted per
  day) and go to the **Jul 31 consolidation with Joel**. Wave 1 came through untouched — zero of
  the 90 first-priority accounts were removed.
