# Check-in timestamps and MMC notes — review of the Oct 29 activity export

**Date:** 2026-10-29 · **Source:** Map My Customer All Activity Report exported Oct 29 (99,244 activity rows; completed check-ins Feb 2022 → Oct 28, 2026, almost all from 2023 on), collapsed to one check-in per liaison × practice × day. **Workbooks:** `pm/pl-checkin-timestamp-review-2026-10-29.xlsx` (timestamps) and `pm/spine-signals-in-mmc-notes-2026-10-29.xlsx` (notes). **Status:** internal working file for Joe; signals about logging practice and accounts, not a scorecard. Nothing here is a finding until it has been talked through with the liaison.

## 1. What the timestamps say

**Program era, Aug 3 → Oct 28 (practice-day check-ins): Kristen 537 · Jasmine 526 · Coty 632.** Seven timestamp tests come back clean for all three: nothing logged from the web (every check-in came from the mobile app), no check-in time edited after the fact, nothing logged a day or more after its stated time, no check-in time set later than the moment it was created, nothing before 7am, after 7pm or on a weekend, and no impossible travel between consecutive check-ins. The timestamps are phone-clock times recorded at the tap; they were not typed in.

**Location is the one signal that needs reading, and it needs reading carefully.** MMC verifies each row against the address on that row: the practice row against the practice address, a contact row against that contact's own address. Taken at face value that cuts both ways — a real visit looks "outside allowed distance" when one contact's record carries another address, and a sister site logged from miles away looks verified when a contact's address happens to match. This review therefore uses the practice row (or the practice's own verified GPS spot) to decide whether a check-in was at the practice (within 0.3 miles, the threshold MMC itself uses).

**Far from the practice on that basis: Kristen 56 of 537 (10%), Coty 39 of 632 (6%), Jasmine 5 of 526 (1%).** Each row is classified by a mechanical rule, in this order (full detail on the "Far check-ins (all classes)" tab):

| Class | Rule | Kristen | Jasmine | Coty |
|---|---|---|---|---|
| A | Attorney account. SOP §4: "her attorney accounts are worked by phone (no drive route)" — the touch is logged as a visit from wherever she is | 31 | 0 | 0 |
| R | Logged from one fixed remote point: a GPS spot with 163 far check-ins across the whole export and no practice ever verified there except a record named "Test". Non-attorney offices — chiropractic, physical therapy (four Ivy Rehab locations in seven minutes on one morning), pediatrics, one primary care | 10 | 0 | 0 |
| B | Sister site of the organization the liaison was verified at within 15 minutes (Neuro Pain Consultants Clarkston from Shelby; Core Institute Southfield and Brighton from Novi; Silver Pine Sterling Heights from Silver Pine Washington) | 3 | 1 | 28 |
| D | Logged from the spot where the liaison was verified at an unrelated practice that day — a touch logged from another practice's doorstep, or a related or duplicate MMC record | 6 | 4 | 9 |
| C | Never verified at its address and repeatedly logged from one other spot (MMC address probably wrong) | 0 | 0 | 0 |
| X | Far from the practice and matching none of the patterns above | 6 | 0 | 2 |

A class is a rule, not a conclusion; what each row was is a question for the liaison.

Three things stand out. First, 34 of Kristen's 56 come from one fixed GPS point — 24 of the 31 attorney rows and all 10 R rows — which reads as one logging habit rather than several separate events; what that point is and what those touches were is a question for Kristen. SOP §4 says she "may substitute a text/call at some offices"; the open question is only how such touches are logged, because the system treats a logged visit as in person. Second, 28 of Coty's 39 are sister sites of an organization he was verified at within 15 minutes — multi-site organizations logged once per site from the site he was standing at, which the Friday tracker then counts as several visits — and 9 more were logged within a quarter mile of a verified check-in at an unrelated practice. Third, Jasmine's 5 were invisible before this basis change: MMC had verified them through a contact's address, not the practice's (16 of Coty's and 1 of Kristen's rows were verified the same way).

**The ask list (D + X, 27 rows, tab "Ask list (D + X)").** These are the rows the data cannot explain on its own. The D rows were logged from where the liaison was verified somewhere else that day; the X rows have nothing nearby. The question is the same for all of them — was this an in-person visit, a phone or text touch, or a record that should be merged — and it is a question, not an answer (practice names and cities as written in MMC):

- Coty · X · 2026-08-11 15:06 · **Frederick Karoub MD PC** (Royal Oak, Tier 3) — 32.7 mi from the practice; nearest verified check-in that day Epic Primary Care - Ferndale (46 min, 16.62 mi away)
- Coty · D · 2026-08-18 15:26 · **Macomb Pain Management** (Shelby Township) — 13.1 mi from the practice; nearest verified check-in that day Michigan Neurology Associates - Clinton Township (2 min, 0.00 mi away)
- Coty · D · 2026-09-01 15:12 · **Movement Orthopedics** (Clinton Township, Prospect) — 8.5 mi from the practice; nearest verified check-in that day Michigan Center For Regenerative Medicine (1 min, 0.00 mi away)
- Coty · D · 2026-09-01 15:12 · **Jagannathan Neurosurgery** (Troy, Prospect) — 6.6 mi from the practice; nearest verified check-in that day Michigan Center For Regenerative Medicine (1 min, 0.00 mi away)
- Coty · X · 2026-09-03 13:04 · **Farrah Ahmad MD** (MI 48310, Prospect) — 0.4 mi from the practice; nearest verified check-in that day Epic Primary Care - Ferndale (22 min, 6.07 mi away)
- Coty · D · 2026-09-11 12:34 · **CMG Bloomfield - Revankar - CLOSED** (Bloomfield Hills) — 12.2 mi from the practice; nearest verified check-in that day Dixie Highway Internal Medicine (1 min, 0.00 mi away)
- Coty · D · 2026-09-14 10:58 · **iCare Urgent Care** (Dearborn Heights, Prospect) — 7.9 mi from the practice; nearest verified check-in that day GREAT LAKES ORTHOPAEDICS (39 min, 0.00 mi away)
- Coty · D · 2026-09-21 13:04 · **Movement Orthopedics** (Clinton Township, Prospect) — 8.5 mi from the practice; nearest verified check-in that day Michigan Center For Regenerative Medicine (0 min, 0.00 mi away)
- Coty · D · 2026-09-21 13:04 · **Jagannathan Neurosurgery** (Troy, Prospect) — 6.5 mi from the practice; nearest verified check-in that day Michigan Center For Regenerative Medicine (1 min, 0.00 mi away)
- Coty · D · 2026-10-16 13:09 · **Henry Ford Main Internal Medicine - Grosse Pointe** (Grosse Pointe, Tier 1) — 15.4 mi from the practice; nearest verified check-in that day Romeo Plank Family Practice (1 min, 0.00 mi away)
- Coty · D · 2026-10-22 12:31 · **Madison Medical Arts** (Madison Heights, Tier 1) — 20.2 mi from the practice; nearest verified check-in that day Millennium Orthopedics (1 min, 0.00 mi away)
- Jasmine · D · 2026-08-26 14:36 · **SHEBA MEDICAL CENTER** (DEARBORN, Prospect) — 2.7 mi from the practice; nearest verified check-in that day Dearborn Family Doctors (0 min, 0.00 mi away)
- Jasmine · D · 2026-09-08 14:15 · **WARREN MEDICAL** (DEARBORN) — 8.8 mi from the practice; nearest verified check-in that day SOUTHFIELD URGENT CARE (0 min, 0.00 mi away)
- Jasmine · D · 2026-09-21 14:35 · **icare urgent care** (DEARBORN HEIGHTS, Prospect) — 6.1 mi from the practice; nearest verified check-in that day AMC Primary Care (0 min, 0.00 mi away)
- Jasmine · D · 2026-10-27 14:07 · **WARREN MEDICAL** (DEARBORN) — 8.7 mi from the practice; nearest verified check-in that day SOUTHFIELD URGENT CARE (0 min, 0.00 mi away)
- Kristen · D · 2026-08-10 11:41 · **Hesselberg Chiropractic** (Ypsilanti, Tier 1) — 43.1 mi from the practice; nearest verified check-in that day Applebaum & Stone (1 min, 0.00 mi away)
- Kristen · X · 2026-08-27 15:22 · **Team Rehabilitation  - Washington** (Washington, Tier 1) — 21.6 mi from the practice; nearest verified check-in that day METROPOLITAN MEDICAL ASSOCIATES (69 min, 16.36 mi away)
- Kristen · X · 2026-09-03 15:40 · **Lakewood Primary Care** (Sterling Heights, Tier 1) — 2.5 mi from the practice; nearest verified check-in that day Silver Pine Medical Group - Sterling Heights (16 min, 1.55 mi away)
- Kristen · X · 2026-09-16 17:39 · **Pryde Athletics and Physical Therapy** (Canton, Tier 1) — 5.3 mi from the practice; nearest verified check-in that day iTest Health Family Medicine (77 min, 9.73 mi away)
- Kristen · D · 2026-09-17 13:11 · **Henry Ford Medical Center - East Jefferson** (Saint Clair Shores, Tier 1) — 4.1 mi from the practice; nearest verified check-in that day Cornerstone Lakefront Internists (28 min, 0.01 mi away)
- Kristen · X · 2026-09-17 15:00 · **Ivy Corporate** (Troy) — 14.9 mi from the practice; nearest verified check-in that day Masonic Medical Center - Ascension (64 min, 18.02 mi away)
- Kristen · D · 2026-09-23 13:24 · **Pryde Athletics and Physical Therapy** (Canton, Tier 1) — 30.7 mi from the practice; nearest verified check-in that day Henry Ford Primary Care Center - 160 (34 min, 0.00 mi away)
- Kristen · X · 2026-10-06 14:05 · **NXTGEN Physical Therapy** (Washington) — 23.3 mi from the practice; nearest verified check-in that day Metropolitan Orthopedic Associates (177 min, 18.30 mi away)
- Kristen · D · 2026-10-07 09:08 · **Primal Recovery and PT** (Livonia, Tier 1) — 26.0 mi from the practice; nearest verified check-in that day Team Rehab - SMA Bloomfield Hills (5 min, 0.01 mi away)
- Kristen · D · 2026-10-07 14:07 · **Ivy Corporate** (Troy) — 14.6 mi from the practice; nearest verified check-in that day Macomb Pediatrics - Clinton Township (5 min, 0.00 mi away)
- Kristen · X · 2026-10-08 10:37 · **Souva PT and Performance** (Shelby Township, Tier 2) — 8.2 mi from the practice; nearest verified check-in that day Associates in Family Practice (4 min, 1.64 mi away)
- Kristen · D · 2026-10-22 15:02 · **Providence Park Pediatrics - Novi** (NOVI, Tier 1) — 12.9 mi from the practice; nearest verified check-in that day COMMERCE PRIMARY CARE, PC (23 min, 0.00 mi away)

**Why it matters beyond whether the check-in was in person.** The route clock runs on logged check-ins: a touch logged as a visit resets a Tier 1 practice's 14-day clock and counts as a visit in the Friday tracker. In the program era 31 far check-ins on 22 Tier 1 practices did exactly that (attorney 15, fixed point 5, sister site 1, doorstep 7, unexplained 3). The SOP already says "High-value text/call touches on Tier-1 accounts *may* be quick-logged; this is optional pending the team's decision" — this is that decision waiting to be made. Two clean options: log phone and text touches as **Call** activities (they stay visible, the visit clock does not reset), or keep logging them as visits and accept that the tracker and the clock count them. Either way, sister sites should be logged only where the liaison actually stood.

**Co-located practices are not flagged.** Medical buildings hold several practices, so several check-ins within a minute from one GPS point is normal when each practice verifies at its own address.

**Day shape (program era, medians):** first check-in Kristen 09:49 · Jasmine 09:54 · Coty 10:22; last check-in 14:42 · 15:44 · 15:11; check-ins per day 10 · 9.5 · 10; minutes between check-ins 21 · 30 · 25. Check-ins run 8am–6pm and concentrate 9am–4pm; nothing in the hour-by-hour distribution is unusual.

**Historical context (all MMC users, 2024–2025, context tabs).** Edited check-in times do appear in the export's history: 651 of 3,639 check-in days under one account outside the current program (Jim Pratt's, 18%), all of them in Feb–May 2025 — which may reflect how that role used MMC rather than anything else. Web logging and times set after logging are rare; the latter sits mostly under the same account, the former on rows with no owner. None of the three current liaisons shows these patterns in 2026.

## 2. What the notes say about potential spine accounts

**The headline: there are no MMC notes in 2026.** The export holds 13,757 distinct notes (14,770 rows); the last one is dated 2025-05-13. Notes in MMC were overwhelmingly one earlier user's practice (11,926 of them, 2023-01 → 2025-05); the current liaisons' accounts hold 3 (Kristen, 2024-08), 49 (Jasmine, 2024-12) and none (Coty, whose account began 2025-05-15, after the last note). So the note field was never part of how this team works MMC. The SOP makes the Spine Routes app the daily driver, so this year's one-line business notes may live there or in the Friday export — but they are not in MMC, where the routing and this kind of review could use them.

**Oct 30 correction.** The statement above is true of the activity export only. Notes in MMC live on the company record, and the All Companies export of Oct 30 holds 8,279 dated note entries on 1,856 companies, 2,943 of them in 2026 (Kristen 1,403 · Coty 773 · Sean 369 · Jasmine 288; since Aug 1: Kristen 375 · Coty 323 · Jasmine 117 · Sean 8). The activity export never carries them, which is why they were missed. Coty's and Jasmine's entries since August are in `pm/mmc-company-notes-coty-jasmine-since-aug-2026-10-30.xlsx`; the spine-lead scan in this section should be re-run on the companies export.

**What the 2023–2025 notes still give us.** 86 notes mention a spine keyword in the text itself (matches that were only a spine practice's own name were excluded); 32 of them mention a patient, or were saved alongside one that does, and are withheld in full; 54 are quoted in the workbook (phone numbers and long numbers masked; staff and provider names stay as written). Grouped by practice and checked against today's spine book (names flagged closed / remove in MMC set aside as cleanup): **22 practices not in the book** (candidates to add), **25 prospects or Tier 2s** with a spine mention (candidates to promote after re-qualifying), and 16 Tier 1s where the note simply confirms the relationship. Most of the add-candidates come from a Sep–Oct 2024 "Spine BAT line" collateral sweep of podiatry and chiropractic offices. Chiropractic is one of the highest spine-share referrer types in this year's data; podiatry offices sent five B2B referrals in 2026 and none were spine, so those are a hypothesis to test rather than a proven channel.

The 22 add-candidates, strongest signals first (snippets and the promote list in the workbook):

- **Family Footcare, PC** (Southfield) — Not in spine book; 2 notes, last 2024-10; says sends/sent, other provider named, Synergy spine doctor named; not visited since Aug 3
- **TLC Chiropractic** (Northville) — Not in spine book; 2 notes, last 2024-10; interest/asked, other provider named, Synergy spine doctor named; not visited since Aug 3
- **Michigan Surgery Specialists - Auburn Hills** (Auburn Hills) — Not in spine book; 2 notes, last 2024-07; says sends/sent, other provider named, Synergy spine doctor named; not visited since Aug 3
- **MICHIGAN FOOT AND ANKLE** (Southfield) — Not in spine book; 1 note, last 2024-10; interest/asked, other provider named, Synergy spine doctor named; not visited since Aug 3
- **Atlas Foot,Ankle and Wound Care** (Canton) — Not in spine book; 1 note, last 2024-10; other provider named, Synergy spine doctor named; not visited since Aug 3
- **Recovered Chiropractic** (Waterford Township) — Not in spine book; 1 note, last 2024-09; other provider named, Synergy spine doctor named; not visited since Aug 3
- **Alternative Healing Chiropractic** (Wixom) — Not in spine book; 1 note, last 2024-08; says sends/sent, other provider named; not visited since Aug 3
- **Michigan Surgery Specialists PC** (Livonia) — Not in spine book; 1 note, last 2024-07; says sends/sent, Synergy spine doctor named; not visited since Aug 3
- **Foot and Heel Pain Institute of Michigan, PLC** (Southfield) — Not in spine book; 2 notes, last 2024-09; other provider named; not visited since Aug 3
- **DOWNRIVER SPECIALISTS, PC** (WOODHAVEN) — Not in spine book; 1 note, last 2024-12; interest/asked; not visited since Aug 3
- **Clarkston Foot and Ankle Clinic** (Clarkston) — Not in spine book; 1 note, last 2024-09; other provider named; not visited since Aug 3
- **Livernois Primary and Urgent Care** (Detroit) — Not in spine book; 1 note, last 2024-09; says sends/sent; not visited since Aug 3
- **Wellness Physical Medicine Center** (Clinton Township) — Not in spine book; 1 note, last 2024-06; interest/asked; not visited since Aug 3
- **Trinity Health Pain Clinic  Brighton** (Brighton) — Not in spine book; 1 note, last 2023-03; other provider named; not visited since Aug 3
- **Hosey & Murphy Foot & Ankle - Clinton Twp** (Clinton Township) — Not in spine book; 2 notes, last 2024-09; not visited since Aug 3
- **MICHIGAN FOOT AND ANKLE** (Milford Charter Township) — Not in spine book; 1 note, last 2024-09; not visited since Aug 3
- **Great Lakes Foot & Ankle Inst** (Clinton Township) — Not in spine book; 1 note, last 2024-09; visited since Aug 3
- **MICHIGAN FOOT AND ANKLE CENTER, PC** (Livonia) — Not in spine book; 1 note, last 2024-09; not visited since Aug 3
- **PREMIER FOOT AND ANKLE** (Rochester Hills) — Not in spine book; 1 note, last 2024-09; not visited since Aug 3
- **Falkner Chiropractic & Sports Medicine** (Independence charter Township) — Not in spine book; 1 note, last 2024-09; not visited since Aug 3
- **REHABILITATION PHYSICIANS, PC** (NOVI) — Not in spine book; 1 note, last 2024-08; not visited since Aug 3
- **Rehabilitation Physicians - Novi** (Novi) — Not in spine book; 1 note, last 2024-08; visited since Aug 3

These are leads to re-qualify, not current intent: the newest is from spring 2025. The practical move is to hand the chiropractic and podiatry names to the liaison whose cell they fall in as prospects, and to get the one-line note flowing into MMC again so this list refreshes itself.

**Data hygiene seen on the way:** 11 program-era check-ins were at practices whose MMC name says closed / remove / mark as no; 8 of them are in the Sep 22 spine book, so the route sent the liaison there, and 10 were verified at the door. The names, or the book, need cleaning — not the liaison. List on the "Closed-named practices visited" tab.

## 3. Suggested next steps

1. Decide the phone-touch rule (Call activity vs. visit) and the sister-site rule (log only where you stand), tell the team, then re-run the Friday true-up under whichever rule is chosen.
2. Walk the "Ask list (D + X)" rows with Kristen, Coty and Jasmine — a two-minute conversation each, framed as "help me read these".
3. Check the related MMC records that surface on the "Far check-ins (all classes)" tab after step 2 (CMG Bloomfield - Revankar - CLOSED, the Enhance Center and Core Institute sister records, duplicate practice records at one address) and merge where the team agrees.
4. Get the one-line note flowing into MMC (or agree where notes live) — the spine lead list depends on it.
5. Re-qualify the chiropractic and podiatry candidates and add them as prospects in the right cells; clean the closed / remove names in MMC and the book.

**Compliance notes:** referrer-side and practice-level data only; no patient identifiers; notes that mention a patient (or were saved alongside one) are withheld in full and the remaining snippets carry no patient references; this is a signal list for a conversation, not a scorecard or a disciplinary record.