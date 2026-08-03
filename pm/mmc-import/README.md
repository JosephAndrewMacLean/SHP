# Map My Customers sync — getting the spine plan into the CRM

**Owner:** Santosh (import) + Joe (fields/design) · **Updated:** 2026-07-31 (post-validation)
**Goal:** the plan lives where the PLs already work — MMC map filters, visit frequencies, and
past-due flags — instead of in a spreadsheet nobody opens in the field.

## Files here

| File | What it is |
|---|---|
| `mmc-company-update-IMPORT.csv` | **762 rows** — one per validated company (766 locations; 4 two-location practices share one Company ID). Keyed on **Company ID** (from MMC's own export, so matching is exact). Adds spine plan fields incl. the **v2 route days (K-R01…)** and each account's first planned week of the Aug 3 → Sep 28 cycle; keeps each account's existing Groups. |
| `mmc-non-spine-group-IMPORT.csv` | **82 rows** — the accounts PLs marked **"No"** in the Jul 31 eyeball pass. Tags them into Kristen's **`Non-Spine`** group and strips only our `Spine …` plan groups; every other existing group is preserved. `Next Action` carries the PL's reason (e.g. "95% Medicaid," "closed," "competition"). **Reversible** — remove the group tag and the account re-enters the next regeneration. |
| `mmc-import-TEST-3rows.csv` | First 3 rows of the company update — run this first. |

## Columns → MMC mapping

| CSV column | Map to | Notes |
|---|---|---|
| `Company ID` | Company ID (match key) | **Update-existing import — do not create new records.** MMC's import supports updates when Company ID is supplied. |
| `Company Name` | Name | For eyeballing only — don't remap names. |
| `Groups` | Groups | Pre-built as *existing groups + the spine plan group* (`Spine T1 – 21d` / `Spine T2 – 30d` / `Spine T3 – 45d` / `Spine Prospect – 45d`, plus `Spine Wave 1` and `Spine Sean Priority`), so a replace-style import is safe. Verify on the 3-row test that existing groups persist. In the non-spine file this column is *existing groups minus `Spine …` + `Non-Spine`*. |
| `Spine Tier` · `Spine Wave` · `Spine Target Score` · `Referral Evidence` · `2026 Spine Patients` · `Route Day` · `First Planned Week` · `Next Action` | **Custom fields** (create once) | These make the map filterable by the plan. `Route Day` = the **v2** day, e.g. `K-R01` (Kristen Route day 01). `First Planned Week` is a date (cycle 2, W1 = Aug 3), `Touched Jul 22–31 — next per 90-day read`, or `Backlog (Oct+)`. |
| `Visit Frequency Days` | reference only | Set frequency **on the spine groups in-app** (Settings → Groups) rather than per company — one setting each, and MMC's past-due engine starts flagging lapses automatically. Cadence per Kristen (Jul 22): **T1 = 21 · T2 = 30 · T3 = 45 · Prospect = 45**. Today only **64 of 2,349 owned accounts have any frequency configured**, which is why nothing ever shows past due. The `Non-Spine` group gets **no frequency** — that's the point. |

## Run order (≈30 minutes)

1. **Import the 3-row TEST file** (Settings → Import). Match on `Company ID`; map fields as above;
   save the matching as **"Spine plan sync"** (MMC lets you save and reuse field matchings).
2. Check the 3 companies in-app: existing groups intact, spine group added, custom fields populated.
3. Run the full `mmc-company-update-IMPORT.csv` with the saved matching. Review the import-history
   page for errors.
4. Run `mmc-non-spine-group-IMPORT.csv` with the same saved matching — 82 accounts pick up the
   `Non-Spine` group and drop their `Spine …` plan groups.
5. Settings → Groups: set visit frequency on the `Spine …` groups (**21 / 30 / 45 / 45** days). No
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
  account passes 21 days unvisited.
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
