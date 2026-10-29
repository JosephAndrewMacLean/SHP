# New-patient tracker — rows the record does not support on its own

**Date:** 2026-10-29 · **Source:** `2025-2026 PL NPT AUTO MASTER 26.xlsx` as uploaded Oct 29 — 101 weekly sheets (appointments 2025-01-02 → 2026-10-23), 10,599 patient rows, the AUTO sheet (381 rows) and the quarterly total sheets. Cross-referenced with the Map My Customer (MMC) All Activity export of Oct 29 (visits only; calls are not in that export) and the referrer-to-practice map in `pm/b2b-referrer-company-2026.csv`. **Row-level results are in a workbook sent to Joe directly and deliberately not committed** (appointment-level rows). No patient name or chart number appears in the workbook or here; every flagged row is pointed at by sheet name and Excel row number in the master file.

## 1. How the sheet counts, as far as it can be reverse-engineered

Each weekly sheet lists new-patient appointments with a liaison code in the Mrkt Comments column (KJ Kristen · JJ Jasmine · CO Coty · KG Kessia · SS Sean · JP Jim). 9,605 of the 10,599 rows carry a code: Kristen 4,927 · Jasmine 2,049 · Coty 1,221 · Kessia 889 · Sean 274 · Jim 245. From mid-2025 a Channel column records what the patient said on the call (B2B, B2C, Natural, No call, Not asked), and the summary block under each sheet reports a count per liaison plus B2B / B2C / Natural / Undetermined / Overlap lines.

The per-liaison block was reproduced best by one rule: **code present, no "?" or qualifier, and Channel either B2B or blank** (5,740 rows). Rows with a code but a consumer channel (3,116 rows) are not counted; they are presumably the sheet's "Overlap" line, whose value cell is blank on every sheet. Under that rule 77% of the 451 sheet-by-liaison pairs match the block exactly (80% if any of the two or three blocks some sheets carry is accepted); where they differ, the block is almost always *lower* than the rows (95 pairs lower, 10 higher). The same holds for the quarterly sheets: 5,197 credited new patients reported for Jan 2025 → Sep 2026 against 5,472 rows inside the rule by appointment month, 5,198 once the re-listed telehealth rows and same-sheet duplicates (§3) are removed. **In aggregate the reported totals sit below the rows, not above; by liaison the remaining differences are small and run both ways (Kristen -42 · Jasmine +22 · Coty +8 · Kessia +9 · Sean +3 · Jim -1). The exposure is in which rows carry a code at all.** The rule itself is not written anywhere in the file, the "revised" and "confirmed" sheet titles show it is applied by hand, and one week stands out: sheet 8.10.26 reports Kristen 48 and Jasmine 17 against 93 and 33 coded rows after those removals. Monthly totals ran between 82% and 118% of the budget line on the quarterly sheets (the annual "2026 TL" sheet carries slightly different May and June 2026 figures from the Q2 2026 sheet; the quarterly sheets are used here).

## 2. The fishy list — 280 rows (168 inside the counting rule)

A class is a mechanical rule on the row and the MMC export, not a conclusion; what each row actually was is a question for whoever coded it. By liaison code: Kristen 162 · Jasmine 41 · Coty 41 · Kessia 25 · Sean 7 · Jim 4. Workbook tab "Fishy rows".

| Class | Rule | Rows | Inside rule | By code |
|---|---|---|---|---|
| A | Referring provider is the liaison herself or a Synergy clinician (one of our own doctors as the referrer, credited to a liaison) | 9 | 8 | Kristen 5 · Jasmine 2 · Kessia 2 |
| B | Source field is not a referring provider — "Other", "Urgent Care" with no practice, "None, None", "Need primary care provider", "Social Media", "Atty - other" | 15 | 1 | Kristen 7 · Jasmine 3 · Coty 1 · Kessia 2 · Sean 2 |
| C1 | Same chart number listed twice in the same weekly sheet | 31 | 23 | Kristen 15 · Jasmine 6 · Coty 4 · Kessia 4 · Jim 2 |
| C2 | Same chart number credited again with a different appointment date within 120 days | 16 | 10 | Kristen 9 · Jasmine 4 · Coty 2 · Jim 1 |
| D | Credited before any field contact: the credited liaison's first MMC visit to the referring practice came 30+ days *after* the appointment (median 171 days; attorney and phone-cadence accounts excluded) | 90 | 74 | Kristen 67 · Jasmine 4 · Coty 17 · Sean 2 |
| E | Credited liaison never visited the practice before the appointment; another active liaison had (book owner shown in the workbook) | 93 | 49 | Kristen 40 · Jasmine 19 · Coty 14 · Kessia 16 · Sean 3 · Jim 1 |
| F | Row is marked duplicate or former patient in Channel / Status, and the code is still on it | 37 | 4 | Kristen 25 · Jasmine 5 · Coty 4 · Kessia 1 · Jim 2 |

Class A is nine rows and worth reading first: four rows name Kristen Jones herself as the referring provider and carry KJ; the rest name Dr. Salar, Dr. Munk, Dr. Jerry and Dr. Green (DPM) as the referrer. Classes D and E are the bulk, and they are the cleanest test of "credit follows the relationship": the practice is in MMC and nobody with that code had logged a visit there before the patient was seen. Top practices in D are Corewell Health Farmington, Henry Ford Primary Care Center 160, Corewell Urgent Care Warren and NextGen Vitality; in E, MedPro Primary Care Waltz Rd, New Horizons Medical Center and Associated Orthopedists of Detroit Shelby. Some of these will be territory hand-offs (Kessia's and Jim's accounts) or practices worked by phone, which the visit test cannot see — the workbook names who did visit so the question is easy to ask.

## 3. Worth a look — 1,282 rows

| Class | Rule | Rows | Inside rule | By code |
|---|---|---|---|---|
| G | Telehealth row re-listed in a later sheet with the same chart number and the same (telehealth) date — the AUTO process posts the row again in the week the in-person appointment lands | 257 | 255 | Kristen 232 · Jasmine 17 · Coty 4 · Sean 4 |
| H | Credited before any field contact, first visit 1–30 days after the appointment | 94 | 80 | Kristen 25 · Jasmine 21 · Coty 31 · Kessia 6 · Sean 10 · Jim 1 |
| I | Credited liaison never visited; only a departed liaison (Jim, Roshelle) had | 23 | 17 | Kristen 11 · Jasmine 1 · Coty 3 · Kessia 6 · Sean 2 |
| J | Chart number 5+ years older than the appointment (established chart; a patient not seen for years may count as new — this is the list where "new" depends on the rule) | 829 | 458 | Kristen 338 · Jasmine 224 · Coty 98 · Kessia 109 · Sean 27 · Jim 33 |
| K | Liaison code marked uncertain ("KJ?", "? CO", "which one") | 38 | 0 | Kristen 14 · Jasmine 7 · Coty 7 · Kessia 4 · Sean 4 · Jim 2 |
| L | Last visit by the credited liaison more than a year before the appointment | 20 | 13 | Kristen 8 · Jasmine 2 · Coty 6 · Kessia 1 · Jim 3 |
| M | Appointment date blank, malformed or outside 2025–2026 (nine dated 2024, five blank or malformed, one each 2006, 2016 and 2029) | 17 | 14 | Kristen 8 · Jasmine 5 · Kessia 2 · Jim 2 |
| N | Same patient name with a different chart number (possible duplicate registration) | 29 | 15 | Kristen 13 · Jasmine 8 · Coty 3 · Kessia 2 · Sean 3 |
| O | No liaison had ever visited the practice before the appointment | 7 | 7 | Coty 3 · Kessia 4 |

**G is the one structural thing in the file.** 297 credited chart numbers appear on two or more credited rows; the telehealth pattern accounts for 257 re-listed rows (256 chart numbers). The first listing carries a code on 252 of them, the re-listed row is inside the counting rule on 255, and both rows are inside it on 246. Checked against the AUTO sheet, 255 of the 257 have an in-person appointment date there and 252 of those land in the week of the sheet they were re-listed in. Whoever keeps the blocks already removes most of them (taking them out moves Kristen's 2026 weekly residual from about −7 to −2 per week), but the code is on both rows, so anyone counting rows instead of blocks double-counts the auto program.

## 4. Not flagged, for context

- **Attorney-sourced rows:** 551 credited (548 KJ) — the auto / telehealth program, phone-worked by design. Listed by month in the workbook; not in any class.
- **Code on a consumer-channel row:** 3,116 rows — the sheet's own Overlap, outside the counting rule.
- **Referrer not found in MMC:** 719 credited rows (408 inside the rule) across 491 referrer strings could not be matched to an MMC practice, so the visit test could not run. Some are spelling variants; the rest are providers credited to a liaison with no CRM record at all. Tab "Referrers not in MMC" lists the 683 of those rows (469 strings) that are not already in class B or attorney-sourced, aggregated by referrer with counts by code.
- The two "Spine for Joe" sheets (Aug–Oct 2026) were not reviewed separately; they are subsets of the weekly rows.

## 5. What would make this unnecessary next time

1. **Write the counting rule down** on the sheet (code + B2B-or-blank channel; re-listed telehealth rows and same-sheet duplicates excluded) so the blocks can be rebuilt by formula.
2. **One row per patient per episode:** the telehealth intake and the in-person appointment are one new patient; keep the AUTO sheet as the second-appointment tracker, not a second NPT row.
3. **No code without a provider:** "Other", unspecified urgent care and "Social Media" rows stay uncoded until a provider is captured.
4. **Credit needs a touch on record before the appointment** — a visit or a logged call in MMC. Where the account is phone-worked, log the call (this is the same Call-vs-Visit rule proposed in the Oct 29 check-in review).
5. **Internal referrers are never B2B credit.** Rows naming a Synergy clinician or a liaison as the referrer get re-sourced.
6. **Dedupe within the sheet** before the block is filled, and fix the impossible dates.

Caveats: the MMC export carries visits only, so a phone-only relationship reads as "never visited"; the referrer map covers 93% of credited rows (exact map plus first-and-last-name matching against MMC contacts); the chart-age estimate assumes sequential chart numbers at the observed rate of about 60 a day. Nothing here is a finding about a person.
