# Map My Customers sync — getting the spine plan into the CRM

**Owner:** Santosh (import) + Joe (fields/design) · **Date:** 2026-07-21
**Goal:** the plan lives where the PLs already work — MMC map filters, visit frequencies, and
past-due flags — instead of in a spreadsheet nobody opens in the field.

## Files here

| File | What it is |
|---|---|
| `mmc-company-update-IMPORT.csv` | **848 rows** — one per account in the scored book (808) + Sean's routed 40. Keyed on **Company ID** (from MMC's own export, so matching is exact). Adds spine plan fields; keeps each account's existing Groups. |
| `mmc-import-TEST-3rows.csv` | First 3 rows only — run this first. |

## Columns → MMC mapping

| CSV column | Map to | Notes |
|---|---|---|
| `Company ID` | Company ID (match key) | **Update-existing import — do not create new records.** MMC's import supports updates when Company ID is supplied. |
| `Company Name` | Name | For eyeballing only — don't remap names. |
| `Groups` | Groups | Pre-built as *existing groups + the new spine group* (`Spine T1 – 14d` / `T2 – 21d` / `T3 – 30d` / `Spine Prospect – 45d`, plus `Spine Wave 1` and `Spine Sean Priority`), so a replace-style import is safe. Verify on the 3-row test that existing groups persist. |
| `Spine Tier` · `Spine Wave` · `Spine Target Score` · `Referral Evidence` · `2026 Spine Patients` · `Route Day` · `First Planned Week` · `Next Action` | **Custom fields** (create once) | These make the map filterable by the plan. `Route Day` = e.g. `K-D05` (Kristen Day 05); `Backlog (Oct+)` = deferred tail. |
| `Visit Frequency Days` | reference only | Set frequency **on the 4 spine groups in-app** (Settings → Groups) rather than per company — one setting each, and MMC's past-due engine starts flagging lapses automatically. Today only **64 of 2,349 owned accounts have any frequency configured**, which is why nothing ever shows past due. |

## Run order (≈30 minutes)

1. **Import the 3-row TEST file** (Settings → Import). Match on `Company ID`; map fields as above;
   save the matching as **"Spine plan sync"** (MMC lets you save and reuse field matchings).
2. Check the 3 companies in-app: existing groups intact, new spine group added, custom fields populated.
3. Run the full `mmc-company-update-IMPORT.csv` with the saved matching. Review the import-history
   page for errors.
4. Settings → Groups: set visit frequency on the four `Spine …` groups (14 / 21 / 30 / 45 days).
5. Tell the PLs: filter the map by `Spine Wave 1` (or Route Day custom field) → build the day's
   route in-app → check in on arrival. The Google-Maps links per route day are also in the
   operating workbook's Routes tabs.

## Weekly refresh loop

Each Friday: re-export completed activities from MMC → the scorecard reads actuals; if the plan
shifts (accounts dropped/promoted per the OODA rule), regenerate this import CSV from
`pm/pl-weekly-visit-schedule.csv` and re-run with the saved matching (minutes, not hours).

## Phase 2 — API automation (optional, ~Aug)

MMC has a **Public API (access by request)**: email **integrations@mapmycustomers.me** for
credentials; developer docs at **developers.mapmycustomers.me/reference** (REST endpoints,
Postman collection, sandbox). What we'd automate:
- **Push:** weekly planned-visit schedule + tier/wave changes (no more manual imports).
- **Pull:** completed visits nightly → auto-fill the Weekly Spine Scorecard (visit-days per PL,
  protect-list lapses, % visits into the spine book) and fire a lapse alert when a repeat-spine
  account passes 21 days unvisited.
Owner: Santosh; pairs with the MMC↔NextGen crosswalk already tracked (ATTR-B.1).

## Cautions

- **Never remap Name/Address fields in an update import** — Company ID is the only key needed;
  remapping name/address risks overwriting good records.
- The `Groups` column here was built from the **Jul 16 export**; if teams changed groups since,
  re-export and rebuild before running (ask Joe — it's one script).
- DO NOT CALL / CLOSED accounts were already excluded from the book upstream.
