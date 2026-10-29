# New-patient tracker — rows the record does not support on its own

**Date:** 2026-10-29 · **Status:** internal working file for Joe; signals about rows and lists, not a scorecard. Nothing here is a finding about a person: every class is a mechanical rule on the row and the MMC export, and what a row actually was is a question for whoever coded it. · **Source:** `2025-2026 PL NPT AUTO MASTER 26.xlsx` as uploaded Oct 29 — 101 weekly sheets (appointments 2025-01-02 → 2026-10-23), 10,599 patient rows, the AUTO sheet (381 rows) and the quarterly total sheets — cross-referenced with the Map My Customer (MMC) All Activity export of Oct 29 (visits only; calls are not in that export) and the referrer-to-practice map in `pm/b2b-referrer-company-2026.csv`. **Row-level results are in a workbook sent to Joe directly and deliberately not committed:** its rows carry appointment dates. No patient name or chart number appears there or here; each flagged row is pointed at by sheet name and Excel row number in the master file.

## 1. How the sheet counts, as far as it can be reverse-engineered

Each weekly sheet lists new-patient appointments with a liaison code in the Mrkt Comments column (KJ Kristen · JJ Jasmine · CO Coty · KG Kessia · SS Sean · JP Jim). 9,605 of the 10,599 rows carry a code: Kristen 4,927 · Jasmine 2,049 · Coty 1,221 · Kessia 889 · Sean 274 · Jim 245. From mid-2025 a Channel column records what the patient said on the call (B2B, B2C, Natural, No call, Not asked), and the summary block under each sheet reports a count per liaison plus B2B / B2C / Natural / Undetermined lines.

The per-liaison block was reproduced best by one rule: **code present, no "?" or qualifier, and Channel either B2B or blank** (5,663 rows). Rows with a code but a consumer channel (3,183 rows) are not counted; the sheet's "Overlap" label is presumably for them, though its value cell is blank on every sheet. Taking the week-total block where a month-end sheet carries two or three (9 do; the partial blocks are added up when there is no total), 79% of the 451 sheet-by-liaison pairs match the rule exactly and 90% are within one once the telehealth rows listed again and same-sheet duplicates (§3) are removed; the remaining differences run both ways (47 pairs where the block is higher than the adjusted rows, 58 lower); the widest remaining gap is sheet 7.20.26, Kristen 26 reported against 37 adjusted rows. The quarterly sheets tell the same story: 5,197 credited new patients reported for Jan 2025 → Sep 2026 against 5,395 rows inside the rule by appointment month, 5,120 adjusted; by liaison the differences are small and run both ways (Kristen +7 · Jasmine +38 · Coty +18 · Kessia +9 · Sean +6 · Jim -1). **So the reported totals track the rows to within about 1.5% either way; the exposure is in which rows carry a code at all.** The rule is not written anywhere in the file, the "revised" and "confirmed" sheet titles show it is applied by hand, and one sheet (8.10.26) labels its Channel column "Sts", which any formula-based rebuild would trip over. Monthly totals ran between 82% and 118% of the budget line on the quarterly sheets (the annual "2026 TL" sheet carries slightly different May and June 2026 figures from the Q2 2026 sheet; the quarterly sheets are used here).

## 2. The ask list — 229 rows (126 inside the counting rule)

Joe asked for the rows that look fishy. This is that list, framed as questions: in each case the record on the row does not support the liaison credit on its own. By liaison code: Kristen 124 · Jasmine 37 · Coty 32 · Kessia 27 · Sean 5 · Jim 4. Workbook tab "Ask list".

| Class | Rule | Rows | Inside rule | By code |
|---|---|---|---|---|
| A | Referrer field holds the liaison's own name or a Synergy clinician (date-aware: a clinician counts as internal only from the first week they appear in the Res column) | 8 | 7 | Kristen 6 · Jasmine 2 |
| B | Source field is not a referring provider — "Other", "Urgent Care" with no practice, "None, None", "Need primary care provider", "Social Media", "Atty - other" | 15 | 1 | Kristen 7 · Jasmine 3 · Coty 1 · Kessia 2 · Sean 2 |
| C1 | Same chart number listed twice in the same weekly sheet (the workbook notes where the sheet already marks the second row DUPLICATE) | 33 | 24 | Kristen 16 · Jasmine 6 · Coty 5 · Kessia 4 · Jim 2 |
| C2 | Same chart number credited again with a different appointment date within 120 days (telehealth-to-in-person pairs and rows the sheet already adjudicated are excluded) | 10 | 8 | Kristen 5 · Jasmine 3 · Coty 1 · Jim 1 |
| D | Credited before any field contact: the credited liaison's first MMC visit to the practice (any MMC record of it — same provider, same street address) came 30+ days *after* the appointment (median 151 days; attorney and phone-cadence accounts excluded) | 46 | 38 | Kristen 27 · Jasmine 4 · Coty 15 |
| E | Credited liaison had no MMC visit to the practice before the appointment; another liaison active at the time had (book owner shown in the workbook) | 88 | 48 | Kristen 41 · Jasmine 16 · Coty 7 · Kessia 20 · Sean 3 · Jim 1 |
| F | Channel or status note says duplicate or former patient, and the code is still on the row (rows the sheet marked "good to count" excluded) | 37 | 1 | Kristen 26 · Jasmine 4 · Coty 4 · Kessia 1 · Jim 2 |

Class A is 8 rows: 5 carry a liaison's own name in the referrer field (possibly how a liaison-sourced patient gets recorded — the sheet has no field for that) and 3 name a Synergy clinician as the referrer. Both are questions for whoever coded the row, not conclusions. Classes D and E are the bulk, and they are the cleanest test of "credit follows the relationship": the practice is in MMC under at least one record and nobody with that code had logged a visit to any of its records before the patient was seen. Top practices in D are Corewell Urgent Care - Warren, Triumph chiropractic, Trinity IHA Primary Care - Rochester Hills, Dedicated Senior Medical Center - Warren; in E, MEDPRO PRIMARY CARE - Waltz Rd, New Horizons Medical Center, Associated Orthopedists of Detroit-Shelby Township. Some of these will be territory hand-offs or practices worked by phone, which the visit test cannot see — the workbook names who did visit and when the first visit came, so the question is easy to ask.

## 3. Worth a look — 1,261 rows

| Class | Rule | Rows | Inside rule | By code |
|---|---|---|---|---|
| G | Telehealth patient listed again: the telehealth row re-listed in the in-person week with the same (telehealth) date, or the in-person appointment listed as a second new-patient row | 258 | 255 | Kristen 232 · Jasmine 17 · Coty 5 · Sean 4 |
| H | Credited before any field contact, first visit 1–30 days after the appointment | 79 | 66 | Kristen 15 · Jasmine 21 · Coty 28 · Kessia 5 · Sean 10 |
| I | Credited liaison never visited; only a liaison who had already left had (territory hand-off) | 16 | 11 | Kristen 8 · Jasmine 1 · Coty 3 · Kessia 3 · Sean 1 |
| J | Chart number 5+ years older than the appointment (established chart; a patient not seen for years may count as new — this is the list where "new" depends on the rule) | 829 | 444 | Kristen 338 · Jasmine 224 · Coty 98 · Kessia 109 · Sean 27 · Jim 33 |
| K | Liaison code marked uncertain ("KJ?", "? CO", "which one") | 38 | 0 | Kristen 14 · Jasmine 7 · Coty 7 · Kessia 4 · Sean 4 · Jim 2 |
| L | Last visit by the credited liaison more than a year before the appointment | 20 | 11 | Kristen 8 · Jasmine 2 · Coty 6 · Kessia 1 · Jim 3 |
| M | Appointment date blank, malformed or outside 2025–2026 (mostly rows dated 2024, plus blanks, typos and one each 2006, 2016 and 2029) | 17 | 14 | Kristen 8 · Jasmine 5 · Kessia 2 · Jim 2 |
| N | Same patient name with a different chart number (possible duplicate registration; the other registration is pointed to) | 29 | 15 | Kristen 13 · Jasmine 8 · Coty 3 · Kessia 2 · Sean 3 |
| O | No liaison had ever visited the practice before the appointment | 3 | 3 | Coty 3 |

**G is the one structural thing in the file.** 297 credited chart numbers appear on two or more credited rows. The telehealth pattern produces 258 second rows (256 chart numbers): 256 are the telehealth row re-listed in the week the in-person appointment lands, 2 are the in-person appointment itself listed as a new-patient row. The first listing carries a code on 253 of them, the second row is inside the counting rule on 255, and both rows are inside it on 246. Checked against the AUTO sheet, 254 of the 256 re-listed rows have an in-person date there and 251 of those land in the week they were re-listed in. Whoever keeps the blocks already leaves most of them out — taking them out moves Kristen's 2026 weekly residual from about -4 to +1 per week — but the code is on both rows, so anyone counting rows instead of blocks double-counts the auto program.

## 4. Not flagged, for context

- **Attorney-sourced rows:** 551 credited (548 KJ) — the auto / telehealth program, phone-worked by design. Excluded from the visit classes (D, E, H, I, O); they do appear in the date and duplicate classes where the rule fires (G 171, J 19, C1 3, M 3, B 2, F 2, C2 1, L 1). Listed by month in the workbook.
- **Code on a consumer-channel row:** 3,183 rows — outside the counting rule.
- **Referrer not found in MMC:** 719 credited rows (406 inside the rule) across 490 referrer strings could not be matched to an MMC practice, so the visit test could not run. Some are spelling variants; the rest are providers credited to a liaison with no CRM record at all. Tab "Referrers not in MMC" lists the 683 of those rows (468 strings) that are not already in class B or attorney-sourced, aggregated by referrer with counts by code.
- **The other direction:** 75 rows say B2B on the call but carry no liaison code (52 of them in 2026); 142 rows are coded "NO PL" (sometimes with a liaison's initials after it) and 730 are a bare "?". Tab "Uncredited B2B rows" lists the first group with pointers; the other two are counts only.
- The two "Spine for Joe" sheets (Aug–Oct 2026) were not reviewed separately; they are subsets of the weekly rows.

## 5. What would make this unnecessary next time

1. **Write the counting rule down** on the sheet (code + B2B-or-blank channel; telehealth rows listed again and same-sheet duplicates excluded) so the blocks can be rebuilt by formula — and label the Channel column the same way on every sheet.
2. **One row per patient per episode:** the telehealth intake and the in-person appointment are one new patient; keep the AUTO sheet as the second-appointment tracker, not a second NPT row.
3. **No code without a provider:** "Other", unspecified urgent care and "Social Media" rows stay uncoded until a provider is captured; a liaison-sourced patient gets its own marker rather than the liaison's name in the referrer field.
4. **Credit needs a touch on record before the appointment** — a visit or a logged call in MMC. Where the account is phone-worked, log the call (the same Call-vs-Visit rule proposed in the Oct 29 check-in review).
5. **Internal referrers are not B2B credit.** Rows naming a Synergy clinician as the referrer get re-sourced.
6. **Dedupe within the sheet** before the block is filled, fix the malformed dates, and give the 75 uncredited B2B rows a second look — if the patient named a provider, someone owns that relationship.

Caveats: the MMC export carries visits only, so a phone-only relationship reads as "never visited"; the referrer map covers 93% of credited rows (exact map, first-and-last-name matching against MMC contacts, and MMC records at the same street address); the chart-age estimate assumes sequential chart numbers at the observed rate of about 60 a day. **Draft for Joe's review; nothing here is a finding about a person, no patient identifiers are included, and the row-level workbook stays inside the PL program.**
