# Spine Keyword Expansion — Implementation Runbook

**Owner (decisions):** Joe MacLean · **Owner (execution in Google Ads):** Blue Ox Digital
(Shaun Elley / Jake) · **Owner (pages):** Randall · **Built:** 2026-07-25

**What this is.** The build spec is [`spine-keyword-expansion-2026-07.md`](spine-keyword-expansion-2026-07.md);
the keyword sheet is [`../pm/spine-keyword-build-2026-07.csv`](../pm/spine-keyword-build-2026-07.csv).
This is the *process* for getting them into the account — who does what, in what order, what has
to be true before each stage, and how we know it worked.

**The Blue Ox constraint shapes everything below.** Blue Ox operates the Google Ads account
day-to-day. This build is a **specification we hand them**, not something we implement over the
top of them. The runbook is written so Joe owns the decisions and the measurement, and Blue Ox
owns the clicks in the interface. Where that split is wrong — if Joe is building directly — the
stages still hold; only the owner column changes.

---

## 0. Read this first: the expansion is not the biggest lever

Before anyone builds anything, the honest forecast (§6) says the keyword expansion is worth
roughly **+2 to +7 new spine patients a week**, central estimate **~4**. Spine is missing target
by **25–30 a week**.

So the expansion is worth doing and it is not sufficient. Three things in the same account are
worth more per hour of effort, and two of them are free:

| Lever | Estimated weekly gain | Cost | Confidence |
|---|---|---|---|
| **Landing page / redirect fix** (§1, step 2) | Potentially large — 3.3x conversion on 90% of paid spine traffic | $0 | Needs verifying first |
| **Theme reallocation** — Surgery/Injection/Fusion money at Specialist CPA | ~+8/wk | $0 | Medium-high |
| **Keyword expansion** (this build) | +2 to +7/wk | ~$6–17k/mo, already budgeted | Medium |
| **Reactivate `"spine doctors"`** | Recovers ~14,750 impr/mo at a $279 CPA | Already budgeted | High, pending reason for pause |

**Sequence accordingly.** Do the free, high-confidence things first. That is what §1 is.

---

## 1. Stage 0 — Pre-flight (nothing gets built until these are answered)

Owner: Joe, with Blue Ox. Target: **before any keyword upload.** Every item here either
invalidates part of the build or is worth more than the build.

| # | Check | Why it blocks | Who answers |
|---:|---|---|---|
| 1 | **Why is `"spine doctors"` (phrase, Livonia/Specialist) paused?** It spent $21,223 and produced 76.1 conversions at a $279 CPA in 54 days. | If there was a search-term or quality reason, that reason applies to several new keywords too and we need negatives instead of reactivation. If it was accidental, this is the fastest volume recovery available. | Blue Ox |
| 2 | **Do `/specialty/spine-neck-back/{geo}/` URLs redirect to the generic page?** 90% of tracked paid spine sessions (1,677 of 1,871) land on the generic page despite the ads pointing at geo URLs. | Geo pages convert at 1.21 key events/session, generic at 0.365. If this is a redirect, fixing it is worth more than the whole expansion. | Randall / web + Blue Ox |
| 3 | **What is producing `/specialty/spine-neck-back/{ignore`?** An unresolved tracking-template parameter is reaching live URLs. | Broken destination URLs waste spend and corrupt landing-page data. | Blue Ox |
| 4 | **Confirm current daily budgets per spine campaign.** Our arithmetic says spine is at **22% of its budget caps** ($2,333/day actual vs $10,600/day budgeted) while NBS Port Huron looks like it is running **~134% of a $50/day cap**. | Determines whether the expansion has room to spend (it does) and whether Port Huron — the best CPA in the account — is being throttled. | Blue Ox |
| 5 | **Confirm which conversion actions are in the `Conversions` column** for each spine campaign, and that no existing-patient actions remain. | The whole build is optimized against new-patient value. Leftover existing-patient signals corrupt it. | Blue Ox |
| 6 | **Resolve the "some ads limited by policy" flag** on the two Spine Conditions campaigns. | Those ad groups migrate into the geo campaigns in Stage 3. Migrating a policy problem spreads it. | Blue Ox |

**Gate:** items 1–3 must be answered before Stage 1. Items 4–6 before Stage 3.

---

## 2. Stage 1 — Free fixes (Week 1, no new keywords)

Owner: Blue Ox executes, Joe verifies. These are independent of the expansion and should ship
first so their effect is measurable on its own.

- [ ] Fix three live typos: **"Evrey"** → Every (Livonia Specialist, Livonia Fusion, Sterling
      Surgery — $263k of spend behind it), **"Specialits"** → Specialists (Sterling Specialist),
      **"Conditons"** → Conditions (Sterling Surgery)
- [ ] Unpin the `{CUSTOMIZER}` assets on the two ads scoring "Poor" ad strength
- [ ] Pull **"Walk-ins welcome"** and **"Same-Day Appointments"** pending compliance sign-off
      (§7 of the build spec) — do not simply leave them running while the review is open
- [ ] Reactivate `"spine doctors"` **if** pre-flight #1 clears
- [ ] Raise NBS Port Huron's daily budget **if** pre-flight #4 confirms it is capped — best CPA
      in the account ($339) should not be the most throttled campaign

**Measure before you move on.** One week of clean data on these alone. They change CTR and
quality score, which changes the baseline the expansion gets measured against. Ship them
together, measure, *then* start Stage 2.

---

## 3. Stage 2 — Pilot the expansion in one ad group, one geo (Week 2)

Owner: Blue Ox builds, Joe reviews before enable.

**Do not launch 491 keywords at once.** Gautam's requirement is that we learn week over week
and can attribute an effect to an action. A simultaneous 232-row launch in two campaigns is
unattributable by construction. Pilot first.

**Pilot = Sciatica ad group, Sterling Heights only.** Chosen because it is 100% new (no existing
performance to disturb), it is the largest untapped condition, and Sterling Heights is our
best-converting geo.

Build steps:

1. Create ad group `Sciatica` in `BOD - Neck, Back, Spine - Sterling Heights`
2. Add the 6 exact + 10 phrase keywords from the sheet (filter: Campaign = Sterling Heights,
   Ad Group = Sciatica). **Leave the 1 broad match keyword paused.**
3. Apply the Sciatica ad-group negative list from the sheet — *before* enabling, not after
4. Build the RSA from §3.3 #4 of the build spec — 15 headlines, 4 descriptions
5. Final URL: `https://synergyhealth.org/specialty/spine-neck-back/sterling-heights/`
   — **not** `/conditions/sciatica/` (§4.1 of the build spec)
6. Inherit the campaign's bid strategy and target ROAS. Do not set an ad-group-level override
7. Enable

**Then watch it daily for five business days** on: impressions, CTR, quality score by keyword,
search terms (this is the one that matters most — sciatica volume is heavily informational),
cost, and conversions by conversion action.

**Pilot pass/fail, decided at day 5:**

| Signal | Pass | Fail → action |
|---|---|---|
| Search-term relevance | ≥70% of spend on clearly clinical intent | Expand negatives, re-run 5 days |
| Cost per real new patient | ≤$900 (below the $828 spine blend + tolerance) | Cut phrase match, keep exact only |
| Quality score | ≥5 on the exact keywords | Landing page or ad relevance is wrong — fix before scaling |
| `"sciatica pain relief"` / `"sciatica treatment"` | Not more than 40% of ad group spend | Pause those two, keep the near-me set |

A failed pilot is a **cheap, successful experiment** — it tells us condition ad groups need
tighter match types before we build eight more. Say that out loud when reporting it.

---

## 4. Stage 3 — Roll out in waves (Weeks 3–6)

Owner: Blue Ox builds, Joe sequences and reviews each wave.

One wave per week. Each wave is one thing we can attribute an effect to. Never two waves in the
same week.

| Wave | Week | What ships | Why this order |
|---:|---|---|---|
| **1** | 3 | **Back Pain Specialist** split out of Specialist, both geos (32 kw each) | Highest-volume commercial cluster found (§8.3), and `back doctors near me` exact already posts the best ROAS in spine (2.00). Most likely to work. |
| **2** | 4 | **Sciatica** in Livonia + **Herniated / Bulging Disc** both geos | Sciatica is pilot-proven by then; herniated disc migrates the existing Spine Conditions keywords in at the same time |
| **3** | 5 | **Surgery split** into Spine Surgery + Minimally Invasive / Disc Surgery, both geos | Biggest waste pool ($206,928 @ $1,107) but also the biggest disruption risk — do it after two successful waves |
| **4** | 6 | **Neck Pain Specialist**, **Spinal Stenosis**, **Pinched Nerve**, both geos | Smaller volume; safe to batch |
| **5** | 6 | **Port Huron** four core ad groups | Gated on the Port Huron landing page existing (§4.3 of build spec) |

Per-wave checklist — identical every time:

- [ ] Filter the CSV to that wave's campaign + ad group rows
- [ ] Create ad group, add exact keywords, add phrase keywords, **leave broad paused**
- [ ] Apply the ad-group negative list **before enabling**
- [ ] Build the RSA from the build spec §3.3 — no shared headlines with other ad groups
- [ ] Set Final URL to the Phase 1 geo URL from the sheet
- [ ] Move any keywords the sheet marks `MOVE` out of their old ad group in the same change —
      never leave duplicates competing across ad groups
- [ ] Screenshot the ad group's settings before enabling (rollback reference)
- [ ] Enable, then log the date and time in the change log (§7)

**Concurrent, not sequential:** Tier 3 containment can run alongside the waves —
restrict Fusion and Injection to exact match and cap bids (§2.8 of the build spec) in Week 3.
That frees impressions for the new ad groups as they come online.

---

## 5. Stage 4 — Gated items (not on the weekly clock)

These wait on external dependencies. Do not let them hold up Stages 1–3.

**Gated on the Liine/ZocDoc integration fix + 30 qualified conversions in 30 days per campaign:**
- [ ] Enable the 11 broad match keywords per geo, one ad group at a time
- [ ] Retire `Website - New Patient Intent` as an optimization target

**Gated on Randall's page builds:**
- [ ] Repoint each ad group's Final URL to its Phase 2 condition page **as each page ships,
      one at a time**, and compare cost per real new patient for two weeks before and after.
      One page at a time is the whole point — a simultaneous repoint teaches us nothing.

---

## 6. What we expect — the forecast we will be measured against

Full method and assumptions in the `paid-forecast` skill (`.claude/skills/paid-forecast/`).
Two independent methods, deliberately bracketed rather than averaged into false precision.

**Method A — bottom-up.** New transactional search volume (50,450/mo) × a capture ratio
calibrated from 20 spine keywords where we know both US volume and our own actual impressions.
Median ratio 0.088, interquartile range 0.038–0.255.

**Method B — top-down.** 232 new keyword rows × the historical share that get any impressions
(53%) × median impressions per active keyword row (89/mo).

| | Method A | Method B |
|---|---:|---:|
| Low | 1,917 | 1,949 |
| Central | 4,440 | 10,943 |
| High | 12,865 | 20,660 |

**Incremental impressions/month, Sterling Heights + Livonia: 4,400–11,000 central.** Against a
current 86,514/mo that is **+5% to +13%**.

Converting to patients, across CTR 5–8%, CPC $19–25, and cost per real new patient $572–828:

| Scenario | Incremental clicks/mo | Incremental spend/mo | **New patients/week** |
|---|---:|---:|---:|
| Low | 220–350 | $5.5k–6.7k | **1.5 – 2.7** |
| Central | 400–640 | $10k–12k | **2.8 – 4.9** |
| High | 550–880 | $13.8k–16.7k | **3.8 – 6.8** |

**Headline: +2 to +7 new spine patients per week, central ~4.**

**The spend fits inside existing budgets with room to spare.** Spine campaigns are budgeted at
$10,600/day and spending $2,333/day — **22% utilisation, $248k/month of authorized budget the
current keyword universe cannot absorb.** This is the quantified version of Evan's point:
0% impression share lost to budget plus 22% budget utilisation are the same fact stated twice.
We are not asking for money. We are asking to be able to spend the money we already have.

**What would make this forecast wrong:**
- New keywords launch with low quality score, so early CTR and CPC will be worse than the
  ranges above. Expect the first 2–3 weeks to look bad. Judge at week 4, not week 1.
- The 0.088 capture ratio has a 6.7x interquartile spread. It is an order-of-magnitude tool,
  not a forecast engine.
- If the geo-page redirect (pre-flight #2) is real, every conversion number here is understated,
  because the baseline CPA was measured on traffic landing on the wrong page.
- Sciatica and stenosis volume is heavily informational. If the negatives underperform, the
  condition ad groups will spend at high CPA before the search-term data lets us prune.

---

## 7. Measurement, and the weekly learning loop

The point of the staging is that every week has exactly one change to learn from. Keep it that
way in the reporting too.

**Daily, 10 minutes** (this is the "daily conversion analysis" Evan asked for, scoped to
something actually doable):
- Cost per conversion **by conversion action**, spine campaigns — is the Liine new-patient
  booked call getting cheaper or dearer?
- Search-term report for whichever ad group launched most recently
- The six-keyword watchlist in §9.3 of the build spec

**Weekly, in the Wednesday marketing meeting:**

| Metric | Where | Why |
|---|---|---|
| New spine patients (kept) | Data lake | The outcome. Never averaged across weeks. |
| Cost per **real** new patient by ad group | Ads, custom columns | The build's actual scorecard |
| Impressions + impression share lost to **rank** vs **budget** | Ads | Direct test of whether the universe grew |
| Quality score by new keyword | Ads | Tells us if ad relevance and landing page are working |
| Key events/session by landing page | GA4 | Tracks the Phase 2 page work |
| Budget utilisation % | Ads | Should climb from 22% as the universe grows |

**Build the custom columns before Stage 2, not after.** Cost per `New Patient (ZocDoc)` and cost
per `Liine NP BC or BF`, as named columns. Without them, every weekly review re-derives the
same arithmetic by hand and the review gets skipped.

**Change log.** One row per change, in `pm/master-task-list.csv` or a dated log: date, what
changed, who made it, what we expected, what happened. This is what turns "we made changes and
things moved" into "this action caused this effect." Without it, the weekly learning loop is a
memory exercise.

---

## 8. Rollback

Every stage is reversible; know how before you need it.

| Change | Rollback |
|---|---|
| New ad group | Pause the ad group. Keywords and history are retained. |
| Keyword moved between ad groups | Re-add to the original ad group; performance history does not follow, so note the break in the change log |
| Match type restriction (Fusion/Injection) | Re-enable the phrase variants — they are retained, not deleted |
| Landing page repoint | Revert the Final URL. Do this per ad group, not campaign-wide. |
| Broad match enabled too early | Pause immediately, then audit the search-term report for negatives to add before re-trying |

**Do not delete anything in this build.** Pause it. Deleted keywords lose their performance
history, and history is the only thing that makes next month's decision better than this
month's guess.

---

## 9. RACI in one table

| Activity | Joe | Blue Ox | Randall | Compliance |
|---|---|---|---|---|
| Keyword selection, match types, ad group structure | **A/R** | C | — | — |
| Ad copy drafting | **R** | C | — | **A** (claims) |
| Building in Google Ads | A | **R** | — | — |
| Negative lists | **A/R** | R | — | — |
| Landing page builds + tracking parity | A | C | **R** | — |
| Bid strategy + budgets | **A** | **R** | — | — |
| Conversion action hygiene | **A** | **R** | — | — |
| Daily conversion analysis | **R** | C | — | — |
| Weekly report to Gautam | **A/R** | C | C | — |
| Forecast vs actual | **A/R** | C | — | — |

A = accountable (owns the outcome), R = responsible (does the work), C = consulted.
