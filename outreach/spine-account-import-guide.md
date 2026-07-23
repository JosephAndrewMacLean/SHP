# How to Import Spine Accounts into MapMyCustomers — Quick Guide

**For:** the physician-liaison team · **Owner:** Kristen (PL lead), with Joe + Santosh on setup
**Goal:** get our spine target practices into MapMyCustomers (MMC) once, cleanly, with the
right spine-fit tags — so no more re-typing and no duplicates.

Use the file **`spine-account-import-template.csv`** in this folder. It's already set up
with the right columns. Just replace the three EXAMPLE rows with real practices.

---

## Do this once, before importing

1. **Have MMC create the spine fields first.** Joe is asking the vendor to add the
   `Spine Fit` fields to accounts (see `mapmycustomers-api-support-email.md`). Wait until
   they're created — otherwise your tags won't land anywhere.
2. **Ask MMC to turn on "match / update existing" for the import**, matching on practice
   **name + address**, so we update accounts we already have instead of creating copies.

## Filling in the sheet

- **One practice per row.** Fill the practice's name, address, and phone at minimum.
- **For the spine columns, type the value exactly as shown below.** MMC will ignore or
  blank anything that doesn't match — spelling and dashes matter (e.g. `A – Priority`, not
  `A-Priority` or `Priority A`).
- **If you haven't assessed a practice yet,** leave `Spine Fit` blank or put
  `Not Yet Assessed`. It becomes part of the to-do list, not a mistake.
- **Only fill `Spine Not-a-Fit Reason` when Spine Fit is `Not a Fit`.** Leave it blank
  otherwise.
- How to decide A / B / C / Not a Fit: use the one-page rubric in
  **`spine-fit-account-qualification-spec.md`** (the quick decision tree at the bottom of
  Section 3 is the fast version).

## Allowed values (copy these exactly)

| Column | Type exactly one of |
|---|---|
| **Spine Fit** | `A – Priority` · `B – Develop` · `C – Maintain` · `Not a Fit` · `Not Yet Assessed` |
| **Spine Not-a-Fit Reason** | `No spine referrals generated` · `Competitor-owned / employed` · `In-house / exclusive spine` · `Payer mismatch` · `Out of area` · `Closed / defunct / bad data` |
| **Spine Feeder Type** | `Ortho (non-spine)` · `Pain Management` · `Chiropractic` · `PM&R` · `PCP / Family Med` · `Urgent Care` · `Physical Therapy` · `ER / Hospital` · `WC-PI Attorney` · `Other` |
| **Spine Volume Potential (NP/mo)** | `0` · `1–2` · `3–5` · `6–10` · `10+` |
| **Relationship Strength** | `None (cold)` · `Aware` · `Sending occasionally` · `Active referrer` · `Champion inside` |
| **Nearest Spine Site** | `Livonia` · `Sterling Heights` · `Southfield` · `Troy` · `Rochester` · `Port Huron` |
| **Miles to Nearest Spine Site** | a whole number (e.g. `4`) |
| **Payer Fit** | `Strong (commercial/Medicare/Auto/WC)` · `Mixed` · `Weak (heavy HMO/Medicaid — verify)` |

> **A practice can be more than one feeder type** (e.g. a combined ortho + pain group).
> If you need to list two, check with Joe on how MMC wants multiple values separated in the
> file (usually a semicolon) — this is one of the questions in the vendor email.

## When the sheet is ready

1. Save it as a **.csv**.
2. Hand it to Joe / Santosh to run the import (or import it yourself in MMC → Import,
   mapping each column to the matching field).
3. After import, spot-check 5–10 accounts in MMC to confirm the spine tags came through.

## After import: what to write in your visit notes

The import gets practices *into* MMC. From there, **every visit or call gets a note** so we
have a running history. Log it as an **Activity / Check-in** in MMC (not on the account
itself), and set the **Activity Type** (Visit / Call / Email / Drop-off) so our visit
counts stay accurate.

Keep each note to about four lines:

1. **Who I met** — name + role (e.g., "Dr. Patel, and Maria the office manager").
2. **What we covered / what they said** — the substance ("they send spine to a competitor
   out of habit; open to trying us").
3. **Blocker or objection** — the reason they're not sending, if any ("worried about
   wait times for a first appointment").
4. **Next step** — what you committed to do next.

**Put the follow-up itself in its own fields, not just the note**, so it shows up on a due
list instead of getting lost:
- `Next Action` — short text, e.g. "drop off referral pads"
- `Next Action Date` — the date it's due

## Two rules that keep the data clean

- **Never put the spine tag in the Notes field** — it can't be reported on. Always use the
  columns/fields above.
- **No patient information anywhere** — practice-level details only (HIPAA). Never a
  patient name, condition, or story in a note.

---

*Questions on a practice's tag → Kristen. Questions on the import/fields → Joe.*
