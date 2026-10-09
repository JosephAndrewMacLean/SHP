# Map My Customers sync — getting the spine plan into the CRM

**Owner:** Santosh (import) + Joe (fields/design) · **Updated:** 2026-09-22 (new cadence, effective Sep 28)
**Goal:** the plan lives where the PLs already work — MMC map filters, visit frequencies, and
past-due flags — instead of in a spreadsheet nobody opens in the field.

## Files here

| File | What it is |
|---|---|
| `mmc-company-update-IMPORT.csv` | **971 rows** — one per book account (Sep 22: Ruffini duplicate and the closed MD Urgent Care removed). Keyed on **Company ID**. Sep 22 fields: refreshed `Spine Tier` (Joel's tracking, 2026 evidence — see `tier-reconciliation-sep22.csv`), the new **cells** in `Route Day` (`K-A01…` = Tier-1 cell, `…B…` = Tier-2/3 cell, `…C…` = prospect cell; `Phone cadence` = Kristen's attorney accounts), `Visit Frequency Days` on the new cadence (**14 / 24 / 24 / 75**, attorneys 30), and `First Planned Week` = the first W9–W14 day the account is on (or an honest reason it isn't). |
| `mmc-non-spine-group-IMPORT.csv` | **78 rows** — the accounts PLs marked **"No"** in the Jul 31 eyeball pass. Tags them into Kristen's **`Non-Spine`** group and strips only our `Spine …` plan groups; every other existing group is preserved. `Next Action` carries the PL's reason (e.g. "95% Medicaid," "closed," "competition"). **Reversible** — remove the group tag and the account re-enters the next regeneration. |
| `mmc-import-TEST-3rows.csv` | First 3 rows of the company update — run this first. |

## Columns → MMC mapping

| CSV column | Map to | Notes |
|---|---|---|
| `Company ID` | Company ID (match key) | **Update-existing import — do not create new records.** MMC's import supports updates when Company ID is supplied. |
| `Company Name` | Name | For eyeballing only — don't remap names. |
| `Groups` | Groups | Pre-built as *existing groups + the spine plan group* (`Spine T1 – 14d` / `Spine T2 – 24d` / `Spine T3 – 24d` / `Spine Prospect – 75d` / `Spine Attorney – phone cadence`, plus `Spine Wave 1` and `Spine Sean Priority`), so a replace-style import is safe. Verify on the 3-row test that existing groups persist. In the non-spine file this column is *existing groups minus `Spine …` + `Non-Spine`*. |
| `Spine Tier` · `Spine Wave` · `Spine Target Score` · `Referral Evidence` · `2026 Spine Patients` · `Route Day` · `First Planned Week` · `Next Action` | **Custom fields** (create once) | These make the map filterable by the plan. `Route Day` = the account's **cell** since Sep 22 (`K-A01…` Tier-1 cell, `…B…` Tier-2/3, `…C…` prospects; `Phone cadence` = Kristen's attorney accounts). `First Planned Week` is the Monday of the first W9–W14 day the account is on (Sep 28 → Nov 2), or `Not in W9–W14 plan — <tier> due <date>`, `Outpost — pair with a nearby day…`, or `Phone cadence (Kristen) — no drive route`. |
| `Visit Frequency Days` | reference only | Set frequency **on the spine groups in-app** (Settings → Groups) rather than per company — one setting each, and MMC's past-due engine starts flagging lapses automatically. Cadence per Kristen (Sep 19 call, effective Sep 28): **T1 = 14 · T2 = 24 · T3 = 24 · Prospect = 75** (attorneys: phone cadence, 30 in-person). Today only **64 of 2,349 owned accounts have any frequency configured**, which is why nothing ever shows past due. The `Non-Spine` group gets **no frequency** — that's the point. |

## Run order (≈30 minutes)

1. **Import the 3-row TEST file** (Settings → Import). Match on `Company ID`; map fields as above;
   save the matching as **"Spine plan sync"** (MMC lets you save and reuse field matchings).
2. Check the 3 companies in-app: existing groups intact, spine group added, custom fields populated.
3. Run the full `mmc-company-update-IMPORT.csv` with the saved matching. Review the import-history
   page for errors.
4. Run `mmc-non-spine-group-IMPORT.csv` with the same saved matching — 78 accounts pick up the
   `Non-Spine` group and drop their `Spine …` plan groups.
5. Settings → Groups: set visit frequency on the `Spine …` groups (**14 / 24 / 24 / 75** days; none on `Spine Attorney – phone cadence`). No
   frequency on `Non-Spine`.
6. Tell the PLs: filter the map by `Spine Wave 1` (or the Route Day custom field) → build the day's
   route in-app → check in on arrival. Google-Maps links per route day are in each PL's
   `pm/route-days-v2/` workbook and inside the Spine Routes app.

## Weekly refresh loop

Each Friday: re-export completed activities from MMC → the scorecard reads actuals; if the plan
shifts (promote/hold/park at the Monday huddle, Joel's consolidation), regenerate these imports
from `pm/pl-weekly-visit-schedule.csv` and re-run with the saved matching (minutes, not hours).

## Phase 2 — API automation (optional, ~Aug)

MMC has a **Public API (access by request)**: email **integrations@mapmycustomers.me** for
credentials (contact: Alexa Ordoñez); developer docs at **developers.mapmycustomers.me/reference**
(REST endpoints, Postman collection, sandbox). What we'd automate:
- **Push:** weekly planned-visit schedule + tier/wave changes (no more manual imports).
- **Pull:** completed visits nightly → auto-fill the Weekly Spine Scorecard (visit-days per PL,
  protect-list lapses, % visits into the spine book) and fire a lapse alert when a repeat-spine
  account passes its cadence (14 / 24 / 75 days) unvisited.
Owner: Santosh; pairs with the MMC↔NextGen crosswalk already tracked (ATTR-B.1).

## Cautions

- **Never remap Name/Address fields in an update import** — Company ID is the only key needed;
  remapping name/address risks overwriting good records.
- The `Groups` columns were built from the **Jul 16 export**; if teams changed groups since,
  re-export and rebuild before running (ask Joe — it's one script).
- A few removed accounts keep a pre-existing group literally named `Spine` (their clinical
  specialty — e.g. competitor spine clinics). That's **their** taxonomy, not our plan group; we
  don't touch it, so `Spine; Non-Spine` together is expected and means "spine practice, out of our
  referral rotation."
- **Levan Internists is in the company-update file under Jasmine** (Coty's eyeball: "not my
  account — being called on by Jasmine") — confirm with Kristen before the import if ownership is
  still open.
- **Sean's 40 accounts are assigned to Kristen** (merged Jul 31, route days `K-R19`…`K-R22`). Their
  group tag changes from `Spine Sean Priority` to **`Spine Reassigned – ex-Sean book`** and the
  `Spine Wave` field reads `Reassigned (ex-Sean)`, so the history stays filterable under the right
  owner. If MMC account ownership itself should change (owner field, not just our plan fields),
  that's a separate in-app step for Kristen — this import doesn't touch record ownership.
- DO NOT CALL / CLOSED accounts were already excluded from the book upstream; "closed" discovered
  in the eyeball pass (Kids First Pediatrics) rides the Non-Spine import instead.
