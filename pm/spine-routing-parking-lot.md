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
The book has **50 shared buildings holding 131 accounts** (same MMC map pin). They are
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
**11 new accounts entered the book today** (1 from Kristen's list + 10 auto-detected MMC creations):

| # | Account | PL | Why |
|---|---|---|---|
| 1 | Enhance Center – Clinton Township | Coty | Kristen: "Enhance Medical Center → CO" (the Livonia location was already in the book) |
| 2 | Abood Law (Birmingham) | Kristen | Created in MMC Aug 3 |
| 3 | NeuroRestorative (Farmington Hills) | Kristen | Created Jul 30 |
| 4 | Blue Water Primary Care | Kristen | Created Jul 23 — **no street address in MMC; add one** |
| 5 | Yousif Orthopedic Surgery (Troy) | Coty | Created Jul 17 |
| 6 | The Keiser Clinic (Chelsea) | Coty | Created Jul 16 |
| 7 | Macomb Orthopedics | Coty | Created Jul 16 — **no street address in MMC; add one** |
| 8 | Corewell Health Family Medicine (New Baltimore) | Coty | Created Jul 16 |
| 9 | Michigan MSK Medicine | Coty | Created Jul 16 — **no street address in MMC; add one** |
| 10 | infinity Primary Care (Livonia) | Coty | Created Jul 16 |
| 11 | Skywalk Internal Medicine (Sterling Hts) | Coty | Created Jul 16 |

Not new, but decided today: **Michigan Neurology Associates – Clinton Twp** was already in the
book flagged "Not sure" → **confirmed keep** per Kristen. ⚠️ She said *Warren* — MMC only has the
Clinton Twp record; confirm whether the Warren office needs its own MMC record.

Also cleaned up: **4 duplicate records removed** (Forum Medical Clinic, MDWell, Beaumont Urgent
Care by Wellstreet, AMC Primary Care each appeared twice with two address strings but one MMC
pin). The book is now **773 accounts**, one row per MMC record. If any of those really has a
second office, create it as its own MMC record and Friday's refresh picks it up.

**The standing process (no forms, no emails):** create the account in MMC like normal → the
Friday refresh detects anything created since the last export → it lands in the owner's book as
a NEW prospect (green in the workbook), gets a home day by its coordinates, and rides into the
schedule. It gets vetted at the next monthly scrub.

### 4. List scrub — how often? ✅ proposed cadence (needs Kristen's OK)
- **Weekly (automatic, Fridays):** export → true-up visits, pull in new accounts, refresh plan.
- **Monthly (first Monday huddle, ~15 min):** review NEW accounts, Non-Spine additions/reversals,
  promote/hold/park reads due that month.
- **Quarterly:** full eyeball pass (the Jul 31 exercise), per the SOP.

### 5. Routing — v3: WHOLE-ROUTE DAYS (the Joe + Kristen decision, end of Aug 7 call) ✅
Two rounds of field review got us here. Round one killed cross-town days. Round two, walking
Coty's week together, caught the remaining sin: two accounts a block apart on 17 Mile Rd landed
on *different days* because tier priority was still composing each day stop-by-stop. The closing
decision on the call: **"start from start, sort it by city, run the whole thing, and see if the
mix takes care of itself."** That is now literally how it works:

- **A scheduled day IS a home route.** The Weekly Plan says `K-R05` — the same R-number as the
  Territory tab — and you run that whole route, every stop, in its stored drive order. No
  cherry-picking, nothing to cross-reference. One ID system, calendar = map.
- **Which routes run each week is still cadence-driven** (T1 21d · T2 30d · T3 45d on actual
  MMC check-ins): a route comes due when its most-overdue producer does; lapsed producers jump
  the line; **2 protect slots a week** keep the highest-value routes on rhythm while first
  passes continue ("business coming in while we build new business" — encoded).
- **Both routes in the same city run back-to-back days the same week** — the "I was right there
  yesterday" fix.
- **Prospect-only routes run once** (first pass), then wait for the 90-day read. Prospects
  inside producer routes get re-visited when the route reruns (up to 3 polite touches this
  cycle — the 3rd shows as "huddle read due" so promote/park decisions happen on schedule).

**The strategy check, on the final model:** Tier-1 median interval **21 days for all three PLs**
(max 28 Coty / 35 Jasmine / 42 Kristen); every producer route runs at least once; zero Tier-1s
missed. The weekly tier mix is on each workbook's **Weekly Mix** tab, the book-by-city on
**By City**. The deferral tail is now just **42 prospect accounts in 12 prospect-only routes**
(Jasmine 35 · Coty 7) that don't fit this cycle — they hold for September or the 90-day read.
Trade named honestly: running whole routes means Tier-2s/3s inside T1-heavy routes get seen more
often than their minimum (extra touches, not missed ones), and route rhythm beats per-account
rhythm — which is exactly what "does it really matter, if by the end of the week we get it done"
decided.

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

### 9. Flag the accounts with good notes ✅ shipped
**684 of 773 accounts carry real field notes in MMC** (Coty's and Jasmine's are often detailed).
They're flagged **📝** on the *Stops by Day* and *Account List* tabs, with the full note text in
*Account List → MMC Field Notes* — read it before you walk in.

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
| MMC hygiene lists (Joe's idea): no-activity-in-5-years, duplicates to delete, missed-account review | Joe | Easy to auto-generate from the Friday export — say the word |
| **From the W1 field notes** (full brief: `pm/kristen-field-notes-brief-aug7.md`) — park Alliance Washington Twp, Great Lakes Ortho Garden City, Brackney Chiro (structurally blocked, notes are the evidence); VillageMD/Dr. Rosenberg network play | Kristen (huddle) | Non-Spine group, reversible; VillageMD = one relationship, several sites |
| Henry Ford / Corewell **vendor credentialing** for SHP | Joe finds process · Kristen signs | Both PLs keep hitting "no vendors" walls at system sites; unlocks a class of blocked accounts |
| **Office hours into routing** ("closes at 3", "(M,W,TH)", closed-door stops) | Joe | Capture from notes at Friday refresh; early-close offices go first on the route |
| **Notes-back pilot** at Macomb Family Medical Center | Joe + clinic side | Their only objection is the closed loop — prove it here, the prospect converts (feeds PL-D.3) |
| Kristen's book vs clean-drive capacity — **42 of her 95 Tier-1s get only 1 visit this cycle** | Kristen + Gautam | With city-clean routing (no cross-town scatter) her book supports ~40 stops/week honestly; the T1 median holds at 21 days for accounts in rotation, but the tail gets one touch. The fix is unchanged: move east-side geography to Coty, or accept the coverage |
