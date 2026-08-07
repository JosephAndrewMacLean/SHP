# B2B Spine Routing & Planning — Parking Lot (living doc)

**Started 2026-08-07** (Joe + Kristen). Every open routing/planning question lands here with its
current answer, what shipped, and what still needs a human call. Feed new items to Joe any time —
this page gets updated on every refresh.

---

## Week 1 recap (Aug 3–7, from the live MMC activity export)

| PL | Planned stops | Completed (MMC check-in) | Off-plan book accounts also visited | Person-touch rows logged |
|---|---|---|---|---|
| Kristen | 50 | **27 (54%)** | 3 | 186 |
| Coty | 50 | **29 (58%)** | 8 | 172 |
| Jasmine | 50 | **12 (24%)** | 1 | 100 |

How to read it: "person-touch rows" overcount real stops (MMC logs one row per person seen), so
the honest units are unique accounts. **80 book accounts got a real check-in in W1; 68 of them
were planned stops** — when the team was in the book, they were overwhelmingly *on plan*. The
gap is completion volume, not wandering: the export cut Thursday night, W1 was the first week on
new routes, and ~18% of visit rows went to accounts outside the spine book (ortho field days —
by design). No blame reading on Jasmine's 24% — worth a simple "what got in the way?" at Monday's
huddle (coverage, PTO, or route friction) before any conclusion.

**The big mechanical change this week:** the cadence clock now runs on **actual logged check-ins**
(Aug 7 export), not on planned credit. Whatever was really visited counts; whatever wasn't stays
due. This true-up reruns every Friday from the MMC export — that's the whole refresh loop.

---

## The parking-lot items — status

### 1. Multiple practices in one building ✅ shipped
The book has **60 shared buildings holding 152 accounts** (same street number + city). They are
now *atomic*: same home day, consecutive stops, and when any of them is due, the building-mates
ride along on the same scheduled day. Marked 🏢 in the workbooks' *Stops by Day* tab and listed
per account in *Account List → Same-building with*.

### 2. Finish a route early — what next? ✅ shipped (rule below)
Every scheduled day now carries **"Finish early? Add these"** — the 2 nearest accounts that come
due *next* week (pull-forwards). Rule of thumb, in order:
1. Work the bonus stops printed on the day (nearest, already due-soon).
2. Still have time? Open the app's **Protect Radar** and take the closest producer on it.
3. Log everything — Friday's true-up credits any pull-forward automatically, and next week's
   plan adjusts itself. **Do not** start tomorrow's route unannounced; that breaks the huddle's
   date-stamping in MMC.

### 3. New / added accounts — list + how they enter ✅ shipped
**11 accounts entered the book today** (auto-detected from MMC + Kristen's adds):

| Account | PL | Why |
|---|---|---|
| Enhance Center – Clinton Township | Coty | Kristen: "Enhance Medical Center → CO" (Livonia location was already in the book) |
| Michigan Neurology Associates – Clinton Twp | Coty | Was in book as "Not sure" → **confirmed keep** per Kristen. ⚠️ Kristen said *Warren* — MMC only has the Clinton Twp record; confirm whether the Warren office needs its own record |
| Abood Law (Birmingham) | Kristen | Created in MMC Aug 3 |
| NeuroRestorative (Farmington Hills) | Kristen | Created Jul 30 |
| Blue Water Primary Care | Kristen | Created Jul 23 — **no street address in MMC; add one** |
| Yousif Orthopedic Surgery (Troy) | Coty | Created Jul 17 |
| The Keiser Clinic (Chelsea) | Coty | Created Jul 16 |
| Macomb Orthopedics | Coty | Created Jul 16 — **no street address in MMC; add one** |
| Corewell Health Family Medicine (New Baltimore) | Coty | Created Jul 16 |
| Michigan MSK Medicine | Coty | Created Jul 16 — **no street address in MMC; add one** |
| infinity Primary Care (Livonia) · Skywalk Internal Medicine (Sterling Hts) | Coty | Created Jul 16 |

**The standing process (no forms, no emails):** create the account in MMC like normal → the
Friday refresh detects anything created since the last export → it lands in the owner's book as
a NEW prospect (green in the workbook), gets a home day by its coordinates, and rides into the
schedule. It gets vetted at the next monthly scrub.

### 4. List scrub — how often? ✅ proposed cadence (needs Kristen's OK)
- **Weekly (automatic, Fridays):** export → true-up visits, pull in new accounts, refresh plan.
- **Monthly (first Monday huddle, ~15 min):** review NEW accounts, Non-Spine additions/reversals,
  promote/hold/park reads due that month.
- **Quarterly:** full eyeball pass (the Jul 31 exercise), per the SOP.

### 5. Current routing inefficient — continue or re-sort by city? ✅ rerouted — and the tier worry is a non-issue
Done today, properly: every account now has **exact MMC coordinates**, and all home days were
re-clustered from scratch on real geometry (76 of 79 days are exactly 10 stops; same-building
groups kept intact; stop order is a nearest-neighbour drive chain).

**The important reassurance: re-sorting by geography does NOT mess up the T1/T2 algorithm.**
Geography and cadence are two separate layers now — home days are *where accounts live*; the
weekly schedule picks *who is due* (T1 21d · T2 30d · T3 45d) and then drives them as one area.
A scheduled day consumes **everyone due in that area in one drive**, which is exactly the fix for
"drive past an account Tuesday and come back Thursday." Where a city still shows up twice in a
week (≈14% of city-weeks), it's a big city with two genuinely separate clusters (Warren and
Sterling Heights each hold 2–3), or more than 10 due accounts — not drive-by waste.

### 6. "Stops in Order" tab doesn't match "Weekly Plan" ✅ fixed
Fair catch — the old tab listed territory (home days) while Weekly Plan listed calendar days.
The workbook now has **Stops by Day**, which mirrors the Weekly Plan **row for row** (same days,
same order, stop-by-stop), and the territory reference lives on its own tab
(*Territory (Home Days)*), clearly labeled as the map, not the calendar.

### 7. SS accounts combined with KJ ✅ done
Ex-Sean accounts are woven into Kristen's re-clustered geography — no more bolt-on R19–R22 days.
(They keep their "new-PL intro" flag until first visited.)

### 8. Account moves ✅ done
- **MI Family Practice → Coty** (matches MMC, where Coty already owns it).
- ⚠️ Same situation, needs Kristen's call: **Aquino Integrative Internal Medicine** and
  **Allied Internists** are ex-Sean accounts on Kristen's list that MMC says *Coty* owns.
  Move them too, or transfer MMC ownership back?

---

## Open items (human calls, owners)

| Item | Owner | Note |
|---|---|---|
| 18 ex-Sean accounts still **owned by Sean Sweeney in MMC** | Santosh (bulk owner transfer → Kristen) | Import updates our plan fields, not record ownership |
| Aquino + Allied Internists — Kristen or Coty? | Kristen | See §8 |
| Michigan Neurology Associates **Warren** office | Kristen/Coty | MMC only has Clinton Twp; add Warren record if it's a real second location |
| 3 new accounts missing street addresses | Their owners | Blue Water Primary Care · Macomb Orthopedics · Michigan MSK Medicine — can't be routed accurately until fixed |
| MNA record's `Company - ID` field holds junk text in MMC | Santosh | Custom field was mis-filled; repair so imports can match it |
| Jasmine W1 completion (12/50) | Kristen | "What got in the way?" — huddle question, not a verdict |
| Monthly scrub cadence (§4) | Kristen | Say yes/no/modify |
