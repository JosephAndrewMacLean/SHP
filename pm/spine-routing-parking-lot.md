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

## Sep 22 refresh — NEW CADENCE from Mon Sep 28 (T1 14d · T2/T3 3–4 wks · prospects sprinkled)

**Why:** Kristen wants the Tier 1/Tier 2 touches expedited (Joe + Kristen call, Sep 19). **Effective Monday Sep 28 = W9.**
Basis = the Sep 3 workbooks (the loosened-T2 book — every account kept) with Joel's tier tracking and the PL-chat
corrections applied; cadence clock from the Sep 22 MMC activities export (visits through Sep 22).

**The cadence (all three PLs):** Tier 1 every **14 days** · Tier 2 **and Tier 3** every **3–4 weeks** (due at 24 days —
T3s are kept and counted like T2s, "they're already sending") · prospects every **60–90 days** (due at 75), **sprinkled
into every week — a prospect slot is held on every day and filled whenever a prospect is due within 8 miles, and a day
with fewer due producers fills up with prospects; never a prospect-only week**. A stop is listed in the week its due date
falls, so revisits land 10–17 days apart for Tier 1 and 21–28 for Tier 2/3. Kristen runs the same cadence and may swap a
text/call at some offices; her **18 attorney accounts (13 T1 · 4 T2 · 1 P) are off the drive routes** — MMC group
`Spine Attorney – phone cadence`.

**Book: 973 → 971** (Kristen 320 · Jasmine 317 · Coty 334 | **T1 237 · T2 238 · T3 36 · Prospect 460**). PL-chat corrections
applied exactly: Glazer Spine Center stays with **Coty under the Glazer name** and absorbs the Ruffini DC duplicate (same
building, Ruffini record dropped; Santosh to switch Glazer's MMC owner to Coty) · **THE CORE INSTITUTE NOVI → Coty** ·
**Allied Internists → Coty** · **Aquino Integrative → Coty** · **MD Urgent Care removed (permanently closed)** · South East
Michigan Medical Associates stays on Kristen (it was already hers; read the thread as another PL flagging it and Kristen
claiming it — shout if that's backwards).

**Tiers (Joel's `mmc_tier_tracking`, applied with one rule):** his moves are applied where the evidence is **2026** — the
"sent since we started" test — and **no proven sender is demoted**. 68 moves applied (21 up to Tier 1, incl. the six
Aug 31-week spine-list senders; 35 to Tier 2; 12 to Tier 3); promoted Tier 1s carry their spine evidence in the
import and Account List. **225 not applied**, all logged with reasons in `pm/mmc-import/tier-reconciliation-sep22.csv`:
29 Tier-1 moves rest on 2025-only spine referrals (Joel's file counts from Jan 2025), 83 more on a 2025 spine referral
plus a 2026 referral of unknown service line (Joel to classify), 63 Tier-2/3 moves on 2025-only ortho/other, and
**50 are demotions** — 23 of Tier-1 accounts that have 2026 spine patients (11 of them Joe's Sep 3 adds, e.g. Great
Lakes Medicine, 5 spine) and 27 of Tier 2/3 senders. Joel's attribution source clearly differs from the master
workbook; Joel + Santosh to align the definition before the next file.

**The routes are now cells** (71: Kristen 30 · Jasmine 18 · Coty 23 — `K-A01…`): up to ~10 producers that sit together
(check-in GPS; never-visited accounts sit at their zip/town centroid) plus the prospects nearest to them. `A` = holds
Tier 1s (14-day rhythm) · `B` = Tier 2/3 only · `C` = prospects only (runs on slack). **A day = the due stops in and
around a cell**: the cell's due producers plus due producers within 8 miles (12 when a day would otherwise run short),
Tier 1 first, most overdue first; then the day's prospect slot(s) from pools within 8 miles of the day's producers.
Nothing inside its window is listed — the skip-flag era is over. Far pockets run as short flagged days (3+ stops, per
Kristen's Aug 7 rule); 6 accounts sit alone or in pairs too far from anything to make a day — flagged "Outpost" in
the import (e.g. Tedd March – Monroe, a Tier 1): pair them with a nearby trip. Prospect-only far pockets never run as
a day this cycle: Jasmine 5 cells, Coty 7, Kristen 0 — 47 of their prospects get no touch and carry honest "Not in W9–W14
plan" labels in the import (the rest ride along on neighbouring days).

**W9 (Sep 28) is the transition week, per Kristen:** every T1/T2/T3 drive stop on the Sep 3 W9 plan is kept — by Sep 3
tiers Kristen 35 · Jasmine 16 · Coty 17 (only Kristen's two attorney stops back out); with the Sep 22 promotions the kept
stops read Kristen 36 · Jasmine 22 · Coty 19 — matched by MMC Company ID, marked "kept from Sep 3 plan" wherever they land, and a
kept stop visited <10 days earlier says "your call". The plan's prospects gave way to due producers within 10 miles of
the kept stops; a day's prospect slot goes to its own Sep 3 prospects only if they are due, so W9 carries few prospects
(Kristen 1 · Jasmine 0 · Coty 6) and the sprinkle runs in full from W10.

**What the cadence actually delivers in W9–W14 (30 days × ~10 stops per PL):**

| | Tier 1 visits per account | Tier 2 | Tier 3 | Prospects touched | Prospects per week W9→W14 |
|---|---|---|---|---|---|
| Jasmine | **41 at 3×** | 49 at 2×, 6 at 1× | 9 at 2×, 1 at 1× | 54 of 211 | 0 · 5 · 10 · 23 · 5 · 11 |
| Coty | 54 at 3×, 5 at 2×, 1 at 1×, 1 none | 14 at 2×, 38 at 1×, 3 none | 9 at 1×, 2 none | 40 of 207 | 6 · 5 · 11 · 8 · 6 · 4 |
| Kristen | 8 at 3×, 83 at 2×, 31 at 1× | **13 at 2×, 19 at 1×, 92 none** | 5 at 1×, 10 none | 22 of 41 | 1 · 5 · 4 · 4 · 4 · 4 |

(7 of the 75 W10–W14 days carry no prospect — none was due within 8 miles that week.) Kristen's line is the
capacity truth, not a bug: 122 drive Tier 1s at 14 days need 61 stops/week before a single Tier 2. Per her call ("tier
ones every two weeks — I may skip some and text"), the plan is **Tier-1-first**: 92 of her 124 drive Tier 2s and 10 of
15 Tier 3s get no drive visit in the six weeks (they keep their due dates in the import), and 31 of her Tier 1s get one
visit rather than two or three. The alternative is one switch away for next Friday: **balanced** (T1 and T2 both about
every 6 weeks). Her decision — and the Gautam capacity conversation (`pm/pl-capacity-model-sep9.xlsx`) just got sharper:
the team's 224 drive Tier 1s alone at 14d = **112 stops/week of 150**.

**Check-ins, filled from the export (company-day):** W5 **143** (K 37 · J 46 · C 60; T1 share 19%) · W6 **120** (K 42 · J 36 · C 42; T1 share 22%) · W7 **140** (K 54 · J 37 · C 49; T1 share 29%). Activity held; the T1
share is what the new cadence should move.

**For Joe:** `pm/ownership-mismatches-sep22.csv` — 10 more book-vs-MMC-owner mismatches between active PLs (e.g. Premiere,
Hartland and Livingston Pediatrics on Coty's routes but Kristen-owned; Macomb Internal Medicine and Emcura on Kristen's,
Coty-owned; Epic Medical Center on Jasmine's, Coty-owned) — Y/N and I'll move them. **Add candidates:** MedCare Urgent
Care (Aug 31-week spine sender, no MMC record at all) and five accounts Joel's file moved to Tier 1 since Aug 3 that
aren't in the book — Surgeons Choice Medical Center, Katherine A Repp NP, Crossover Health Royal Oak, Waterford Clinic &
UC, Elite Internal Medicine.

**Geography, honestly:** coordinates come from check-in GPS with a PL's home/hub check-in points excluded (37 such spots;
one Kristen point carried 394 check-ins across 45 companies) and each company's check-in cluster validated against its
address zip; never-visited accounts sit at their zip or town centroid. 4 accounts check in 14/10/25/54 miles from their
MMC address — placed at the address zip and flagged "verify" in the import (St Clair Orthpaedics & Sports Medicine - Macomb; MICHIGAN ORTHOPEDIC SPECIALISTS - Farmington Hills; Hesselberg Chiropractic; Elia & Ponto Law): MMC address or
the office the PL actually visits? 10 book accounts have no city in MMC (parsed from the address; one bad zip). Days are
mostly compact: 10 of 90 days span more than 20 miles (Jasmine W9 J-A06, Jasmine W9 J-A01, Kristen W10 K-A27, Jasmine W10 J-A08, Jasmine W11 J-A06, Jasmine W11 J-A04…) and 1 single legs exceed 15 miles — rural
Port Huron/Croswell runs, W9 transition days built on the Sep 3 geography, and metro days where the 8→12→15-mile borrow
rule reached across town to fill a day. A day's cell ID is its anchor, not a promise of content — read "Primary Area" for
where the day actually goes.

**Data-ops:** the activities export was cut off mid-row (one row lost; export straight from MMC next time) · Ruffini →
Glazer merge in MMC (the app's W5 history day for Coty's R15 no longer shows the dropped Ruffini record; the ledger keeps
it) · "S. Crossley MD" hangs off the HENRY FORD HEALTH umbrella record · the four "verify" addresses above · Joel's tier
definitions vs the program's 2026 rule (above).

---

## Sep 3 refresh — the 111 adds land; W4 recap; the adherence finding

**Book: 862 → 973** (Kristen 322 · Jasmine 320 · Coty 331 | T1 216 · T2 217 · T3 34 ·
Prospect 506). Joe's Y/N pass on the referral-evidence list: **111 added** (52 straight to
Tier 1 on spine receipts), 35 declined, 6 ownership flags honored — 2 adds reassigned (Epic Medical →
Jasmine; Trust Family Care → Kristen) and 4 marked another PL's account and declined
(Pulmonary & IM Specialists, Trinity IHA Neuro AA — Coty's; Trinity IHA Peds Domino's,
Farah Podiatry — Jasmine's). **8 Non-Spine reversals** are deliberate re-adds (Great Lakes
Medicine, Joel Wellness Clinic, Beacon Orthopedics, Michigan Spine Institute, et al.) —
pulled from the Non-Spine import (now 76). Placement: 70 into existing routes ≤10 stops,
**6 new routes** — K-R34 (Sterling Hts/Shelby ×10), K-R35 (Troy/Royal Oak), K-R36
(Bloomfield/Franklin), K-R37 (Hamtramck/Grosse Pointe ×10), K-R38 (Novi/South Lyon),
C-R43 (Rochester Hills). Two W4-evidence candidates (Crossover Health Royal Oak, Waterford
Clinic & UC) arrived after Joe's sheet — on next week's review list.

**Where every add landed in the schedule.** 106 of the 111 ride a scheduled W6–W9 run of
their home route. 3 join this week's still-unrun W5 routes — Kristen's R21 (Pediatric and
Adolescent Care Associates, Michigan Urgent Care & Occupational Health) and Coty's R14
(Foot & Ankle Specialists of SE Michigan – Warren) had zero check-ins as of the Sep 3
export, so the new stops were appended to those day cards (both now 10 stops). 2 prospect
adds wait for next cycle with honest labels in the import (Pediatric Consultants of Troy –
Shelby Twp on K-R12; Imlay City Family Practice on K-R32 — every slot those routes could
take is held by a more-overdue producer run). All 52 Tier-1 adds ride scheduled runs; **the
four that would otherwise have missed the cycle are rescued:**
Franklin Medical Consultants, Burhani Medical Center and Alan L Feldman DO ride K-R19's
W8 return (Kristen ran R19 on Sep 1–2, before Joe's sheet landed — the route comes back
exactly at its 21-day mark, week of Sep 21), and Western Wayne Physicians rides J-R16's
W8 return. Three swaps made room, each trading up: **K-R19** (6 T1, incl. the 3 T1 adds) in
for K-R28 (1 T1, due Jun 30) · **J-R16** (2 T1, incl. the T1 add) in for J-R34 (0 T1, due Jul 30) ·
**J-R08** (two active T1 spine senders due Sep 17 + University Pain Clinic add) in for
J-R21 (a Tier-2 reactivation route lapsed since Oct 2025 — first in line next cycle,
flagged, not forgotten). Every displaced route keeps its due date in the import
("Deferred to next cycle — route due …").

**W4 recap (Aug 24–28) — the adherence finding.** Check-ins: 149 stops (Kristen 47 ·
Jasmine 48 · Coty 54). Everyone is working the book (136/148 unique accounts visited are
book accounts ✓) — but the *week assignment* slipped: **Jasmine 32/47 planned stops (68%) ·
Kristen 19/43 (44%) · Coty 0/49 (0%)**. Coty instead ran three complete book routes in W4
(R21, R27, R28 at 10/10) plus R15/R16 at 8/10 — none from his W4 plan — and opened W5 by
running R30 and R13 in full (Aug 31 / Sep 2). Nothing restarts — the
cadence engine credits every visit where it landed and reschedules accordingly. The real
cost: **the most-overdue Tier-1 blocks keep not being the ones that get run** (his R17/R20,
overdue since early Aug, slipped again). Huddle framing: route-ORDER discipline, not effort —
volume is fine, sequence is the plan's whole value.

**Capacity, restated with the bigger book:** 973 accounts at 21/30/45/45 cadences ≈ **200
stops/week needed vs ~135 delivered** — the gap grew with the adds. W6–W9 schedules the 60
most-overdue runs (due-order verified); **57 due runs deferred** to next cycle (incl. the
W5 routes' own 21/30-day returns and the 3 swap evictions), each logged with its due date
in the plan files and the import. Options unchanged: Wave-1-first weighting, more field days, a 4th PL, or
accept ~6-week effective T1 rhythm.

---

## Aug 21 refresh — W3 recap + entering W4 (no early repeats)

**W3 (Aug 17–21) planned vs checked in:** Coty **36/46 (78%)** · Jasmine 32/47 (68%) ·
Kristen 29/49 (59%) — best week yet (last-activity basis; exact per-stop stats when the
activities export arrives). **W4–W9 was repaired, not rebuilt:** every route's next run is
recomputed from actual visits, and the no-early-repeat rule is asserted — nothing visited in
W1–W3 comes back before its cadence. Stops visited <14 days before their route runs carry a
**"visited — skip unless needed"** flag.

**Changes this refresh:**
- **NeuroRestorative → Non-Spine** (team request). It leaves K-R11 (now 9 stops); already in
  the Non-Spine import.
- **Commerce Primary Care, PC → Tier 1, Kristen** (Joe's ask): 8800 Commerce Rd, on **K-R23,
  first run W4 (Aug 24)** — R23 was pulled forward from Sep 14; the whole block was ~87 days
  stale. The receipts: **Sydney Frantz NP (the Aug 11 spine referral to Dr. McCarty) practices
  at Commerce Primary Care** — Kristen's last visit there was May 26, a 77-day visit→referral
  lag. This closes the last unresolved W2 spine-referrer mapping.
- W3-planned routes that didn't check in during W3 come back **when actually due, not
  blindly at W4**: K-R04 → W4; C-R10 → W5; **J-R06 → W7** (its stops were mostly worked in
  W2, so a W4 rerun would have repeated 2-week-old visits — the no-repeat rule held it to
  early September). Routes whose only planned run was W3 get their cadence comeback:
  **K-R11, K-R13, J-R07/R09/R10, C-R01, C-R25** (7 routes). **10 runs deferred to next
  cycle** (all repeats, non-producers, or due past Sep 21). Honest flag on one: **J-R33
  (prospect-only) slipped NOT because it can wait — its 90-day reads are ~3 months overdue —
  but because Jasmine's book is 30 routes for 30 slots with zero slack.** Producers outranked
  it; it goes first in line next cycle (or a W9 finish-early bonus run if she has a light day).

**W2 spine referrers — all 18 now mapped** (fresh people export): Kotsonis DO → **Silver Pine
Medical Group – Sterling Heights** (in book, Kristen strategic; visited Jun 22, 51d lag) ·
Frantz NP → **Commerce Primary Care** (above) · Turfe DO → **Corewell IM – Dearborn Heights**
(OFF-BOOK; visited Aug 6 — 5-day lag!) · **Sam Bernstein Law** (off-book; visited Jul 9, 34d
lag) · **Giroux and Pappas Law** (off-book; visited May 28, 76d lag). **Add candidates with
referral evidence:** Corewell IM Dearborn Heights, Sam Bernstein Law, Giroux & Pappas — the
two firms are direct-to-spine attorney referrers now, same evidence rule that seated Morse;
attorney-channel handling is Kristen/Gautam's call (compliance guardrails apply).

**Skip-flag rule (made explicit this week):** a scheduled stop whose last visit is still inside
its tier window (21/30/45/45) at that week's Friday shows **"visited &lt;date&gt; — skip (next due
&lt;date&gt;)"** — 130 of 793 planned stops carry it. The 90-day prospect *read* stays what it always
was: a promote/hold/park huddle decision at the 3rd touch, not a drive-past rule.

**Adversarial verification findings (6-agent check before shipping, all fixed or logged):**
- Two Aug-14 restored accounts had tier/group mismatches in the MMC import — **Nova Health UC
  (T2) and HF Primary Care Orchard Lake N (T1) were still tagged `Spine Prospect – 45d`**, so
  MMC's past-due engine would have tracked them at the wrong cadence. Fixed to T2-30d / T1-21d.
- The import's **First Planned Week column was still carrying Aug-14 dates** (109 rows pointed
  at weeks that no longer exist). Recomputed for all 862 rows from the actual W4–W9 schedule;
  deferred-route accounts now say so explicitly.
- **Structural finding, not fixed (a decision, not a bug):** at 15 route-days/week, each account
  appears **once** in the 6-week horizon — an effective ~42-day revisit vs the 21-day T1 target.
  The book's stated cadences need ~175 stops/week; capacity is ~135 (July insight §5, still
  true, now bigger book). Options for Joe/Kristen: give T1-heavy routes second runs at the
  expense of prospect blocks (Wave-1-first), add field days, or accept ~5–6-week T1 rhythm.
- Two never-visited prospects (The Keiser Clinic, Total UC – Romeo) sit on deferred routes and
  get no first pass this cycle — queued next cycle.
- MMC has **56 company names duplicated across 123 records** — name-based joins misattribute
  visits (a verifier initially "found" 6 extra early repeats that way; by ID it's 0). We join
  by ID everywhere; noted for the data-ops list.
- **21 off-cycle prospect accounts carried a stale "Touched since Jul 22" label** in the MMC
  import (incl. The Keiser Clinic — never visited at all, and three urgent cares last visited
  in 2023). Relabeled honestly ("Never visited — needs first touch" / "Not scheduled this
  cycle — last visit <date>"). These 69 off-cycle prospects are the next scrub's raw material.

**Sep 3 data-ops notes:** (1) one book row has a Company ID that no longer exists in MMC —
Ruffini DC PC, Richard J (C-R15, Coty; visits log by name with no company link). The update
import will no-op that row; Santosh: recreate/link the record. (2) Sep-3 adds that landed on
W5-plan routes are all handled in-cycle: 3 join this week's un-run day cards (K-R21, C-R14)
and 4 ride the W8 returns of K-R19/J-R16 (those routes ran their W5 day Sep 1–2, before the
adds); only 2 prospect adds (K-R12, K-R32) wait for next cycle, labeled in the import.

**Data ask:** this refresh ran on companies + people exports only, using each account's
last-activity date (all 862 book accounts matched the export; one account's latest activity is
an email masking an older visit; 7 never-visited prospects have no activity at all). **Include
the activities export Friday** to fill the tracker's W3 check-in row and restore
multi-visit stats.

---

## Aug 14 refresh — W2 recap + what changed

**W2 (Aug 10–14) planned vs checked in:** Jasmine **35/49 (71%)** · Kristen 28/48 (58%) ·
Coty 26/45 (58%). Jasmine tripled her W1 rate — the city routes are getting worked. The W3–W9
plan is rebuilt from these actual check-ins: **everything the team did is credited; nothing
restarts** (standing rule, per Kristen's Aug 14 ask — a refresh always picks up where the field
left off).

**Book changes (now 862 accounts):**
- **4 restored per Kristen** — Nova Health UC Southfield (T2), Corewell UC Farmington Hills N
  (Prospect), One Health Orchard Lake (Prospect), HF Primary Care Orchard Lake N (T1). Root
  cause: they were **never in the Jul 16 cut** — not removed, not eyeballed; she'd been working
  them all along. The safety net for this now runs every Friday: any account a PL actually
  visited that sits outside the book+Non-Spine surfaces on an **off-book watch list** (117
  currently — mostly ortho-book by design; top spine-relevant candidates: **Draugelis &
  Draugelis** (15 visits — the auto/BI firm), Rehabilitation Physicians – Novi (physiatry, 11)).
- **All urgent cares are in the spine list** (Joe's rule, Aug 14): 85 owned urgent cares added
  as prospects. Exception kept out: Blue Water UC (Kristen's own "95% Medicaid" eyeball) —
  reverse it if she wants it back.
- **1 removal via field read:** MEDICAL GROUP PRACTICE PC (Olympia) → Non-Spine — Jasmine's
  notes show three visits concluding they only refer inside the Olympia network.
- NextGen Vitality (Kristen's new MMC account, Aug 11) auto-entered as a prospect.

**⚠️ One urgent hygiene item — patient names in CRM notes.** The thank-you entries frequently
name referred patients (an initial + last name, sometimes full names, occasionally with
insurance details). The program rule is **no patient-identifying information in writing** — MMC
is a third-party CRM and these notes travel in exports. Fix going forward: log *"TY for recent
referral"* with **no patient identifiers** — the discreet in-person thank-you stays exactly as
is. Ask Santosh about scrubbing the historical pattern. This needs Kristen's voice at the
huddle, framed as protecting the team.

**Kristen's asks from the Aug 14 call (logged):**
1. **One place to enter tier/visit data** instead of a daily spreadsheet → Joe/Joel to propose:
   the check-in flow already writes MMC; the missing piece is her rollup view. On the list.
2. **Referral→tier→company tracking** → that's the referral-match pipeline (Santosh) feeding the
   Weekly Mix; will demo at the next huddle.
3. **MMC account-update requests come as one packaged import + a walkthrough**, not ad-hoc
   lists of seven accounts. Adopted.

**Influence tracking is live (Aug 14 PM).** The weekly B2B results report is now matched
referrer-side against MMC visit activity: **91% of the 75 new patients came from providers a
PL had visited; median visit→appointment lag 30 days (spine 43)**. Two standing artifacts:
`pm/spine-influence-weekly.csv` (+ `.md` method doc) — visits by tier vs. B2B spine referrals
per week, updated each Friday refresh — and `pm/b2b-time-to-referral-insights-aug14.md`, the
shareable brief for Santosh/Gautam. This is the first cut of Kristen's ask #2. Aggregates
only; no patient data in either file.

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

> **Superseded Sep 22:** days are now cells' due stops on the 14/24/24/75 cadence — see the Sep 22 section. Kept for the Aug 7 reasoning.
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
  Move them too, or transfer MMC ownership back? **Sep 22: resolved — both moved to Coty per the PL chat (see the Sep 22 section).**

### 9. Flag the accounts with good notes ✅ shipped
**684 of 773 accounts carry real field notes in MMC** (Coty's and Jasmine's are often detailed).
They're flagged **📝** on the *Stops by Day* and *Account List* tabs, with the full note text in
*Account List → MMC Field Notes* — read it before you walk in.

---

## Open items (human calls, owners)

| Item | Owner | Note |
|---|---|---|
| 18 ex-Sean accounts still **owned by Sean Sweeney in MMC** | Santosh (bulk owner transfer → Kristen) | Import updates our plan fields, not record ownership |
| Aquino + Allied Internists — Kristen or Coty? | **Resolved Sep 22: Coty** (PL chat) | See §8 |
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
| Kristen's book vs capacity — **Sep 22: 31 of her 122 drive Tier 1s get one visit in W9–W14, 92 of 124 Tier 2s none** (Tier-1-first per Kristen; balanced option available) | Gautam (capacity call) | See the Sep 22 section |
