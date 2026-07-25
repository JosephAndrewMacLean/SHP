# Spine Keyword Expansion & Ad Group Build — July 2026

**Owner:** Joe MacLean · **Built:** 2026-07-25 · **Status:** implementation-ready, pending
clinical/legal sign-off on flagged copy claims

**Source data:** Google Ads exports pulled 2026-07-24 — Campaigns, Ad Groups (segmented by
conversion action), Ads, Search Keywords. Ad-group and ad reports cover Jan 1 – Jul 24, 2026;
the keyword report covers Jun 1 – Jul 24, 2026. Search volumes are Semrush US national
(2026-07), used for *relative* prioritization, not absolute forecasting. Condition-page
existence verified via Google Search Console (last 90 days).

**Keyword discovery:** Semrush `phrase_fullsearch` (broad-match/alternate-query discovery) run
against seeds *sciatica, spine specialist, back doctor, neck pain doctor, herniated disc,
spinal stenosis, pinched nerve, spine surgeon, pain management*, plus `phrase_these` for batch
volume validation. **§8 records what discovery changed** — it corrected several numbers in an
earlier draft of this document that were built from a hand-generated candidate list.

**Companion file — the actual build sheet:** [`pm/spine-keyword-build-2026-07.csv`](../pm/spine-keyword-build-2026-07.csv)
— 513 rows (491 keywords + 22 ad-group negative lists), **grouped by match type within each
ad group**, with volume and whether each keyword is new / existing / reactivated. Google Ads
Editor–importable. §9 explains the match-type logic; **§10 is the full list in readable form.**

**Scope change 2026-07-25:** the Pain Management & Injections ad group and all injection /
epidural / nerve-block / ablation terms have been **removed from the build** at Joe's
direction. §2.8 covers what that means for the existing Injection ad groups.

This answers three questions, in the order Cardinal's guidance says to answer them:

1. Which spine ad groups deserve the money — and why, from the data.
2. Where the keyword universe expands, and what it's worth.
3. What ad copy goes in each ad group.

---

## 0. The logic chain (read this to Gautam first)

> Spine campaigns lose **0% impression share to budget** and lose the rest to rank. So more
> money cannot buy more patients — the eligible-impression denominator is the constraint.
> Eligible impressions = keywords targeted × geography. Geography is fixed. Therefore the only
> lever that grows spine volume is **keywords**.
>
> When I looked at where the current keywords actually send the money, I found spine spend is
> split roughly in half between two themes that perform *twice as differently* as each other:
> **Specialist** ad groups deliver a real new patient for **$572**; **Surgery** ad groups
> deliver one for **$1,107**. Specialist takes 42% of spend and returns 61% of new patients.
>
> So expansion is not "add more keywords everywhere." It is: **grow the themes that convert,
> and split the themes that don't, so the money has somewhere efficient to flow.** Keyword
> discovery found **66 new keywords**, of which **49 are doctor / specialist / "near me" terms
> worth ~50,500 US searches a month** — the exact pattern our own data proves converts 2.7x
> better than everything else we run. Every condition keyword in the build lands on a page
> that already exists on our site.
>
> The ask: approve the build below. Spend stays flat. The denominator grows.

**Definition used throughout — "real new patient."** Google Ads counts 15 conversion actions
of wildly different quality. Everything in this document is measured on the two that
represent a confirmed booking: `New Patient (ZocDoc)` + `Liine NP BC or BF` (new patient
booked call). It **excludes** `Website - New Patient Intent` — the wide, ambiguous signal
currently overvalued at $125 that we agreed to walk down to $75. Wherever a number counts all
conversion actions, it is labeled.

---

## 1. Biggest bang for the buck — where the money should go

### 1.1 By theme (Jan 1 – Jul 24, 2026, all spine campaigns)

| Theme | Spend | Real new patients | Cost per real NP | % of spend | % of NPs |
|---|---:|---:|---:|---:|---:|
| **Specialist** | $203,224 | 355.4 | **$572** | 42% | **61%** |
| Surgery | $206,928 | 186.9 | $1,107 | 43% | 32% |
| Injection | $37,355 | 24.7 | $1,514 | 8% | 4% |
| Fusion | $21,467 | 11.1 | $1,939 | 4% | 2% |
| Spine Conditions campaigns (HD/DDD) | $9,357 | 8.0 | $1,170 | 2% | 1% |
| Pain Management | $0 | 0.0 | — | 0% | 0% |
| **Total spine** | **$478,331** | **586.0** | **$816** | | |

**The headline number:** $275,107 currently sits in Surgery + Injection + Fusion + Conditions
and returns 231 new patients. At the Specialist theme's $572, that same money returns **481**.
The gap is **250 new patients over ~30 weeks — 8.3 per week**, against a 72–80/week target
we are currently missing by 25–30.

That is the size of the prize, and it does not require one extra dollar of budget.

### 1.2 By individual ad group — the actual ranking you asked for

| Rank | Campaign / Ad group | Spend | Real NPs | **CPA** | Verdict |
|---:|---|---:|---:|---:|---|
| 1 | Port Huron / Specialist | $7,753 | 22.9 | **$339** | Best CPA in the account. Starved — only 1,165 impressions in 8 weeks. |
| 2 | Sterling Heights / Specialist | $70,007 | 176.8 | **$396** | **The workhorse. Expand here first.** 6.71% CTR. |
| 3 | Livonia / Specialist | $125,459 | 155.7 | **$806** | 2x the CPA of Sterling on the *same theme*. Copy problem — see §3.1. |
| 4 | Port Huron / Surgery | $5,401 | 5.3 | $1,013 | Small; leave. |
| 5 | Livonia / Surgery | $70,129 | 64.9 | $1,081 | Split into sub-themes (§2.3). |
| 6 | Sterling Heights / Surgery | $126,155 | 113.7 | $1,109 | Largest single line item, 2.8x Sterling Specialist's CPA. |
| 7 | Spine Conditions - Livonia / Herniated Disc | $2,443 | 4.0 | $611 | Promising CPA, no volume. Merge into geo campaigns (§2.4). |
| 8 | Livonia / Injection | $17,897 | 15.2 | $1,180 | Not expanded — contain and harvest (§2.8). |
| 9 | Livonia / Fusion | $11,499 | 6.7 | $1,724 | Restrict to exact match. |
| 10 | Southfield / Surgery | $5,243 | 3.0 | $1,754 | Geo has almost no impressions. |
| 11 | Sterling Heights / Injection | $18,863 | 9.5 | $1,986 | Worst large-spend group. Contain (§2.8). |
| 12 | Sterling Heights / Fusion | $9,958 | 4.4 | $2,263 | Worst CPA in spine. |

### 1.3 Where to put the effort — ranked, with the reason

**Tier 1 — do this week. Highest return per hour of your time.**

1. **Sterling Heights / Specialist** — $396 CPA, proven copy, 6.71% CTR. It is efficient and
   impression-limited. Every keyword you add here converts at the account's best rate. This is
   where expansion compounds fastest.
2. **Livonia / Specialist** — $806 CPA on $125K. It runs the *same theme* as Sterling at 2x
   the cost because the copy is generic boilerplate shared across all four Livonia ad groups
   (§3.1). Porting Sterling's copy structure is a one-hour job against the largest
   inefficiency in spine.
3. **Harvest the paused Pain Management ad groups** — 168 keywords across four geos sit idle
   there, including **every sciatica keyword we own** and the only stenosis and pinched-nerve
   terms in the account. Move those into the new condition ad groups. The ad group itself is
   *not* being rebuilt (§2.8); we are taking the spine keywords out of it and leaving the
   injection terms behind.

**Tier 2 — next two weeks.**

4. **Split Surgery into sub-themes** (§2.3). $206,928 at $1,107 is the second-largest pool of
   waste in spine, and it is caused by one ad group absorbing everything from "spine surgery"
   to "back disc surgery" to "neck fusion" behind one generic ad.
5. **Build the condition ad groups** (§2.2) — sciatica, stenosis, pinched nerve, herniated
   disc — into the geo campaigns where the budget actually lives.

**Tier 3 — contain, don't grow.**

6. **Fusion and Injection** — $58,822 at $1,608 combined, and neither is being expanded. Move
   both to exact match only and cap bids so the freed impressions flow to Specialist, Back Pain
   and the new condition groups. Do not delete Fusion: those terms are how a surgical patient
   with real intent finds us, they are just badly matched today. Injection is a live question —
   see §2.8.

**Do not touch:** total spine budget. Impression share lost to budget is 0% — cutting spend
cuts volume we cannot afford to lose, and adding spend has nowhere to go until the keyword
universe grows.

---

## 2. Keyword expansion — where the universe grows

### 2.1 Four structural findings that explain the volume gap

**Finding 1 — Sciatica is completely dark.** The single largest spine condition category in
consumer search has **zero live keywords** in the account. Every sciatica keyword we own sits
in the paused Pain Management ad groups or is individually paused. The one exception,
"epidural injection sciatica," ran in the Injection ad group and drew **17 impressions in
eight weeks**.

| Sciatica keyword we own | Ad group | Status |
|---|---|---|
| sciatica treatment | Pain Management (Sterling, Livonia, Port Huron) | Paused |
| sciatica pain relief | Pain Management (Sterling) | Paused |
| sciatic nerve pain relief | Pain Management (Sterling) | Paused |
| physical therapy for sciatica near me | Pain Management (Sterling) | Not eligible — ad group paused |
| sciatica treatment southfield | Pain Management (Southfield) | Paused |

US demand for the sciatica cluster: **sciatica treatment 27,100/mo · sciatica pain relief
40,500/mo · sciatica treatment near me 1,900/mo · sciatica doctor near me 720/mo.** We are
bidding on none of it. Randall's sciatica landing page work is aimed at exactly the right
target — but the ad groups that would use it do not exist yet.

**Finding 2 — "near me" is our most efficient keyword pattern and it is 8% of our impressions.**

| Keyword pattern (Jun 1 – Jul 24) | Spend | Conversions* | Cost/conv* | Share of spine impressions |
|---|---:|---:|---:|---:|
| Contains "near me" | $22,291 | 204.6 | **$109** | **8.3%** |
| Everything else | $158,549 | 547.8 | $289 | 91.7% |

\* All conversion actions, not the real-NP definition — the keyword report cannot be segmented
by conversion action. Directional, but the 2.7x spread is far too large to be signal noise.
Worth re-confirming at the real-NP level once you build the custom columns Evan suggested.

Your instinct to go after "conditions and treatments + near me" is correct, and this is the
number that proves it. We have 56 near-me keywords. The build below adds 70 more.

**Finding 3 — Zero broad match anywhere in spine.** All 379 unique spine keywords are phrase
(538 instances) or exact (173). Evan's guidance — 1–2 high-intent broad match per ad group —
is currently implemented zero times. That is a deliberate gap to close, carefully: broad match
is only safe once conversion signals are clean, so §2.6 sequences it.

**Finding 4 — 58 keywords flagged "low quality" burned $18,097 on 22,084 impressions.** These
are Quality Score 1–4 terms. They consume eligible impressions at bad rank and drag the
account-level quality score. The ad group split in §2.3 fixes most of them by giving them
relevant ad copy; the rest should be paused.

### 2.2 The condition expansion — with volumes and existing landing pages

**Critical and load-bearing:** every condition below **already has a live page on
synergyhealth.org**, confirmed in Search Console. Randall does not need to build these before
you can launch — he needs to *improve* them. That removes the dependency you raised with Evan.

| Condition ad group | Anchor keywords (US vol/mo) | Existing landing page | GSC impr (90d) / avg pos |
|---|---|---|---|
| **Sciatica** | sciatica pain relief 40,500 · sciatica treatment 27,100 · sciatica treatment near me 1,900 · sciatica doctor near me 720 · sciatica specialist near me 260 | `/conditions/sciatica/` | 91 · pos 15.6 |
| **Spinal Stenosis** | spinal stenosis treatment 8,100 · spinal stenosis specialist near me 260 · spinal stenosis treatment near me 210 · lumbar stenosis treatment 90 | `/conditions/spinal-stenosis/` · `/conditions/lumbar-stenosis/` | 526 · pos 18.5 |
| **Herniated / Bulging Disc** | herniated disc treatment 22,200 · bulging disc treatment 6,600 · herniated disc treatment near me 1,600 · herniated disc specialist 260 | `/conditions/herniated-disc/` | 434 · pos 18.0 |
| **Pinched Nerve / Radiculopathy** | cervical radiculopathy treatment 4,400 · pinched nerve in neck treatment 1,600 · pinched nerve treatment near me 590 · pinched nerve doctor near me 110 | `/conditions/cervical-radiculopathy/` | 759 · pos 15.9 |
| **Spondylolisthesis & Spine Arthritis** | spondylolisthesis treatment 1,600 · si joint pain treatment 1,000 · neck arthritis treatment 880 · arthritis in back treatment 480 | `/conditions/spondylolisthesis/` · `/conditions/si-joint-pain/` · `/conditions/arthritic-back-pain/` | 1,118 / 197 / 1,027 |
| **Degenerative Disc Disease** | degenerative disc disease treatment 1,300 · DDD keywords already built in the orphaned Conditions campaign | `/conditions/degenerative-disc-disease/` | 57 · pos 24.1 |
| **Scoliosis (adult)** | scoliosis specialist near me 880 · scoliosis doctor near me 720 · scoliosis treatment for adults 1,900 | `/conditions/scoliosis/` | 330 · pos 23.3 |
| **Injury / Trauma** | whiplash treatment near me 1,900 · whiplash doctor near me 480 · compression fracture treatment 880 | `/conditions/back-fracture-break/` · `/conditions/neck-fracture-broken-neck/` | 17,155 / 70,229 |

**Note on the Injury/Trauma row:** `/conditions/neck-fracture-broken-neck/` pulls **70,229
organic impressions** at position 7. That is by far our strongest-ranking spine asset and it
has no paid ad group pointed at it. It also overlaps the existing `BOD - Auto Accident`
campaign ($1,677 spend, 99 clicks all year) — coordinate before building, so you don't bid
against yourself.

### 2.3 Splitting the two bloated ad groups

**Surgery ($206,928 @ $1,107) → four ad groups.** One ad group currently absorbs every
surgical query behind one generic ad. Evidence it's a matching problem, not a demand problem:
`back disc surgery` spent $2,978 for 1 conversion; `spine disk surgery` $2,205 for 1;
`spinal fusion` $1,892 for 0; `neck fusion` $1,502 for 0.

| New ad group | Keywords moved in | Landing page |
|---|---|---|
| Spine Surgery (general) | spine surgery, spinal surgery, back surgery, back surgeons in michigan, spine surgeon near me | `/specialty/spine-neck-back/{geo}/` |
| Neck / Cervical Surgery | neck surgery, cervical fusion surgery, acdf surgery, anterior cervical discectomy | `/conditions/cervical-radiculopathy/` |
| Minimally Invasive & Disc Surgery | microdiscectomy, discectomy, minimally invasive spine surgery near me 390, endoscopic spine surgery near me 210, laminectomy | `/conditions/herniated-disc/` |
| Second Opinion & Non-Surgical | second opinion spine surgery 110, alternatives to back surgery 210, non surgical back pain treatment 320, do i need spine surgery | `/specialty/spine-neck-back/{geo}/` |

The Second Opinion group is the sleeper. Sterling Heights' Specialist ad already uses "Spine
Surgery Second Opinions" as a headline and that ad group runs a 6.71% CTR. The intent is
proven; it has never had its own ad group.

**Injection — not rebuilt.** An earlier draft proposed rebuilding this as a Pain Management &
Injections ad group with 27 keywords. That is **removed from the build** (§2.8).

### 2.4 Fold the orphaned Spine Conditions campaigns into the geo campaigns

`BOD - Spine Conditions - Livonia` and `- Sterling Heights` hold four ad groups, $9,357 spend,
8 real new patients, and campaign status **"some ads limited by policy; search volume limited;
missing enough relevant keywords."** Nine keywords are flagged low quality and ten "rarely
served." They are structurally starved: separate campaigns with their own tiny budgets,
competing against the geo campaigns for the same auctions.

They also hold the only two condition-specific landing pages currently in use
(`/conditions/herniated-disc/`, `/degenerative-disc-disease-treatment/`) — and the Livonia
Herniated Disc group posted a **$611 CPA**, the best of any non-Specialist group.

**Action:** migrate all four ad groups into the corresponding geo campaigns as condition ad
groups, keep the condition landing pages, then pause the standalone campaigns. Resolve the
"limited by policy" flag before relaunch — that's an ad disapproval that needs reading.

### 2.5 Target build — from 4 ad groups per geo to 9

| # | Ad group | Status today | Priority |
|---:|---|---|---|
| 1 | Spine Specialist | Exists — best performer | Expand |
| 2 | Back Pain Specialist | Merged into #1 | Split out |
| 3 | Neck Pain Specialist | Merged into #1 | Split out |
| 4 | Sciatica | **Paused** | **Un-pause + build** |
| 5 | Herniated / Bulging Disc | Orphaned campaign | Migrate + build |
| 6 | Spinal Stenosis | 2 keywords, 1 low-quality | Build |
| 7 | Pinched Nerve / Radiculopathy | Does not exist | Build |
| 8 | Spine Surgery | Exists — bloated | Split (§2.3) |
| 9 | Minimally Invasive / Disc Surgery | Merged into #8 | Split out |

Run the full 9 in **Sterling Heights and Livonia** (where 92% of spine spend and nearly all
impressions live). Port Huron gets 4 — Specialist, Sciatica, Herniated Disc, Surgery — because
its Specialist group is the cheapest in the account at $339 and deserves more surface area.
Southfield stays minimal until its impression base justifies more.

### 2.6 Broad match — one to two per ad group, and not until the signal is clean

Evan's warning applies precisely to our situation: broad match works when the conversion signal
is strong enough to steer it. Ours is not yet — ZocDoc online-booking completions still aren't
posting back to Google Ads, so the algorithm cannot see our best outcome. **Sequence it:**

- **Now:** launch the new ad groups **phrase + exact only.** 15–20 keywords each.
- **After** the Liine/ZocDoc integration is fixed **and** 30+ qualified conversions land in a
  30-day window per campaign: add the broad match keywords below, one to two per ad group.
- **Then** retire `Website - New Patient Intent` as an optimization target.

| Ad group | Broad match keyword 1 | Broad match keyword 2 |
|---|---|---|
| Spine Specialist | spine specialist near me | orthopedic spine surgeon near me |
| Back Pain Specialist | back pain specialist near me | back doctor near me |
| Neck Pain Specialist | neck pain specialist near me | — |
| Sciatica | sciatica specialist near me | sciatica treatment near me |
| Herniated / Bulging Disc | herniated disc specialist near me | herniated disc treatment near me |
| Spinal Stenosis | spinal stenosis specialist near me | — |
| Pinched Nerve / Radiculopathy | pinched nerve doctor near me | — |
| Spine Surgery | spine surgeon near me | — |
| Minimally Invasive / Disc Surgery | minimally invasive spine surgery near me | — |

All nine are specific, high-intent, and "near me"-anchored — the pattern that already converts
2.7x better than everything else in the account. None is a bare category term like "spine" or
"back pain," which is exactly the failure mode Evan flagged.

### 2.8 What happens to the Injection ad groups now

Removing Pain Management from the build leaves an open question, and it should be answered
rather than left implied.

The Sterling Heights and Livonia Injection ad groups are live today and spending
**$37,355 for 24.7 real new patients — $1,514 each.** That is 2.6x the Specialist CPA. They
were the weakest large-spend groups in spine before this change and nothing about removing the
expansion plan improves them.

There are three options and they are not equal:

| Option | Effect | Recommendation |
|---|---|---|
| **Contain** — exact match only, cap bids, no new keywords | Spend falls, impressions free up for Specialist / Back Pain / condition groups | **Do this.** Lowest risk, keeps the surgical-intent tail. |
| **Pause entirely** | Frees the full $37K immediately | Only if the weekly data still shows $1,500+ CPA after containment. Don't lead with it. |
| **Expand** | — | Off the table per this build. |

**Contain, and let the money move.** Combined with Fusion, containment frees roughly **$58,800
of annualized spend** sitting at a $1,608 CPA. If even half of it reaches the Specialist and
Back Pain groups at their current rates, that is **~50 additional new patients** from money we
are already spending. That is the real upside of taking Pain Management out — not just the
avoided compliance exposure.

**One thing that gets lost, and you should decide it consciously:** injections are how a
non-surgical spine patient converts. Removing that ad group means we bid on people looking for
a *doctor* and people looking for *surgery*, but not people looking for the treatment in
between. If the clinical side considers interventional pain a growth service line, this
decision should be revisited with them rather than settled here.

### 2.7 Estimated universe growth

Actuals from the build sheet, not estimates:

| | Today | After build |
|---|---:|---:|
| Keyword rows across spine campaigns | 711 | 1,202 (491 added) |
| Unique keyword texts | 379 | 522 (143 in the build, 66 of them new) |
| Unique "near me" keywords | 56 | 113 (57 in the build) |
| Ad groups (Sterling + Livonia) | 8 | 18 |
| Ad groups (Port Huron) | 4 | 4, fully rebuilt |
| Broad match keywords | 0 | 28 (11 unique per geo), phase 2 |
| Added US search volume — transactional subset | — | **~50,500/mo** |

The transactional subset — doctor / specialist / surgeon / "near me" terms — is the number to
quote. Condition-term volume skews informational (§8.2) and should not be counted as demand we
can convert. This is down from ~71,000/mo in the pre-removal draft; roughly 20,000/mo of that
was the pain management cluster.

Sterling Heights spine drew 14,000 impressions against ortho's 26,000 in Evan's screen share.
This build should close most of that gap on keyword count alone, before broad match.
**Do not promise a specific impression number to Gautam** — eligible impressions depend on
auction dynamics we can't model from the export. Promise the mechanism, measure the result
weekly, and report the actual.

---

## 3. Ad copy by ad group

### 3.1 The proof point — why copy is worth your time

Same service line. Same offer. Same weeks. Different copy:

| | Sterling Heights / Specialist | Livonia / Specialist |
|---|---|---|
| Copy style | Geo-specific, benefit-led, distinct per ad group | Generic; 9 of 12 headlines shared with Surgery/Injection/Fusion |
| **CTR** | **6.71%** | 3.82% |
| **Cost per real new patient** | **$396** | $806 |
| Spend | $70,007 | $125,459 |

Livonia's four ad groups run near-identical ads. "Expert Spine Care," "Trusted Spine Health,"
"Leading Spine Surgeons," "Comprehensive Spine Care" appear in the Fusion ad, the Injection
ad, the Specialist ad and the Surgery ad. Google scores ad relevance per keyword-to-ad match —
identical ads across four themes means three of them are always wrong. That is one third of
quality score, and it is the cheapest fix available.

**Three typos are live right now on high-spend ads. Fix these today:**

| Typo | Correct | Where | Spend behind it |
|---|---|---|---|
| "Treat **Evrey** Patient" | Every | Livonia Specialist + Livonia Fusion + Sterling Surgery descriptions | $125,459 + $11,499 + $126,155 |
| "Spine, Neck & Back **Specialits**" | Specialists | Sterling Heights Specialist headline | $70,007 |
| "Neck, Spine, & Back **Conditons**" | Conditions | Sterling Heights Surgery description | $126,155 |

**Two live claims need verification before they run another day** — Section 1557 / FTC
exposure, and they're in the ad group with our best CPA:
- "**Walk-ins welcome**" (Sterling Heights Specialist) — is this true at Sterling Heights?
- "**Same-Day Appointments**" / "Same-Day Appointments Open" (Sterling Heights Specialist) — availability-dependent; if it isn't reliably true, it's an unsubstantiated claim.

Route both to compliance. If they're accurate, keep them — they are almost certainly part of
why that ad group outperforms.

### 3.2 Copy rules for every spine ad group

1. **Headline 1 mirrors the ad group theme, verbatim where possible.** "Sciatica Treatment in
   Livonia," not "Expert Spine Care." This is the single biggest ad relevance lever.
2. **Name the geography in at least two headlines.** Sterling Heights does this; Livonia
   barely does.
3. **Lead with the patient's problem, then the outcome, then the credential** — never the
   institution first.
4. **No shared headlines across ad groups.** Maximum two generic brand headlines per ad, and
   they go last.
5. **Keep the `{CUSTOMIZER.Doctor Name}` and `{CUSTOMIZER.Count}` assets** — but note both ads
   carrying a pinned customizer score "Poor" ad strength. Unpin and let Google rotate.
6. **Conservative-care-first framing converts in spine.** Most people with back pain are
   terrified of surgery. "Start with non-surgical options" lowers the barrier to booking.
7. **Every claim must be substantiable.** No "best," no "#1," no outcome promises, no implied
   superiority. Credentials (board-certified, fellowship-trained) are fine if true and
   verifiable against `brand/provider-roster-by-service-line.md`.

### 3.3 Ad copy — 9 ad groups

Format: 15 headlines (30 char max) + 4 descriptions (90 char max), per Google RSA specs.
`{Geo}` = Sterling Heights / Livonia / Port Huron. Character counts are within limits at
"Sterling Heights" length — the longest geo — so all variants fit.

> **All copy below is a draft pending clinical and legal review.** Claims marked ⚠ require a
> confirmed SHP fact before they run.

---

#### 1. Spine Specialist — *the workhorse; model on Sterling's proven structure*
**Landing page:** `/specialty/spine-neck-back/{geo}/`

**Headlines**
1. Spine Specialists in {Geo}
2. Board-Certified Spine Experts
3. Back & Neck Pain Relief
4. See a Spine Doctor This Week ⚠
5. Fellowship-Trained Surgeons ⚠
6. Non-Surgical Options First
7. Spine Care Without a Referral ⚠
8. Metro Detroit Spine Care
9. Book Your Spine Consult
10. Relief From Chronic Back Pain
11. Spine Surgery Second Opinions
12. On-Site MRI & Therapy ⚠
13. {CUSTOMIZER.Doctor Name} Has Openings
14. {CUSTOMIZER.Count} Appts. This Week
15. Synergy Health Partners

**Descriptions**
1. Back or neck pain? Board-certified spine specialists in {Geo}. Book your consult today.
2. We start with non-surgical care and recommend surgery only when it's the right answer.
3. Surgeons, pain specialists and physical therapists coordinating on one care plan.
4. Most insurance accepted. Ask about the soonest available appointment near you. ⚠

---

#### 2. Back Pain Specialist
**Landing page:** `/specialty/spine-neck-back/{geo}/`

**Headlines:** Back Pain Specialists {Geo} · Lower Back Pain Treatment · See a Back Doctor
Near You · Back Pain Relief in {Geo} · Chronic Back Pain Care · Non-Surgical Back Pain Care ·
Find the Cause of Your Pain · Board-Certified Back Doctors · Book a Back Pain Consult ·
Back Pain? Get Answers · Treatment Beyond Painkillers · Metro Detroit Back Specialists ·
{CUSTOMIZER.Doctor Name} Has Openings · Most Insurance Accepted ⚠ · Synergy Health Partners

**Descriptions**
1. Living with back pain? Get a real diagnosis from a board-certified back specialist.
2. From physical therapy to injections to surgery — we start with the least invasive option.
3. Back pain has many causes. We find yours before we treat it. Book a consult in {Geo}.
4. Same practice, full spectrum of care: diagnosis, therapy, pain management and surgery.

---

#### 3. Neck Pain Specialist
**Landing page:** `/specialty/spine-neck-back/{geo}/`

**Headlines:** Neck Pain Specialists {Geo} · Neck & Cervical Spine Care · See a Neck Doctor
Near You · Neck Pain Relief in {Geo} · Chronic Neck Pain Treatment · Pinched Nerve in Neck? ·
Neck Pain Radiating to Arm? · Board-Certified Neck Doctors · Non-Surgical Neck Care First ·
Book a Neck Pain Consult · Cervical Spine Specialists · Metro Detroit Neck Care ·
{CUSTOMIZER.Doctor Name} Has Openings · Most Insurance Accepted ⚠ · Synergy Health Partners

**Descriptions**
1. Neck pain, stiffness or numbness in your arm? See a cervical spine specialist in {Geo}.
2. We treat neck pain with therapy, injections and surgery — in that order, when possible.
3. Board-certified neck and spine doctors. Book an appointment near you.
4. Get a clear diagnosis for neck pain that isn't going away on its own.

---

#### 4. Sciatica — *the biggest new opportunity*
**Landing page:** `/conditions/sciatica/`

**Headlines**
1. Sciatica Treatment in {Geo}
2. Sciatica Specialists Near You
3. Leg Pain From Your Back?
4. Sciatic Nerve Pain Relief
5. See a Sciatica Doctor
6. Non-Surgical Sciatica Care
7. Sciatica Pain Down Your Leg?
8. Find the Cause of Sciatica
9. Book a Sciatica Consult
10. Treat Sciatica, Not Just Pain
11. Physical Therapy for Sciatica
12. Metro Detroit Sciatica Care
13. Board-Certified Spine Doctors
14. {CUSTOMIZER.Doctor Name} Has Openings
15. Synergy Health Partners

**Descriptions**
1. Pain shooting from your lower back down your leg? That may be sciatica. Get it diagnosed.
2. Most sciatica improves without surgery. We start with therapy and targeted injections.
3. Sciatica specialists in {Geo}. Find the nerve that's compressed and treat the cause.
4. Don't wait out sciatica. Book a consult with a board-certified spine specialist.

---

#### 5. Herniated / Bulging Disc
**Landing page:** `/conditions/herniated-disc/`

**Headlines**
1. Herniated Disc Treatment {Geo}
2. Herniated Disc Specialists
3. Bulging or Slipped Disc?
4. Disc Pain Relief Near You
5. See a Herniated Disc Doctor
6. Non-Surgical Disc Treatment
7. Microdiscectomy Specialists
8. Minimally Invasive Disc Care
9. Book a Disc Consult in {Geo}
10. Herniated Disc? Get Answers
11. Disc Surgery Second Opinions
12. Metro Detroit Disc Specialists
13. Board-Certified Spine Doctors
14. {CUSTOMIZER.Doctor Name} Has Openings
15. Synergy Health Partners

**Descriptions**
1. Herniated or bulging disc? Most improve without surgery. Start with a real diagnosis.
2. Disc specialists in {Geo}. Therapy and injections first; minimally invasive surgery if needed.
3. Considering disc surgery? Get a second opinion from a board-certified spine surgeon.
4. Back or neck pain with numbness or weakness deserves a specialist. Book a consult.

---

#### 6. Spinal Stenosis
**Landing page:** `/conditions/spinal-stenosis/`

**Headlines:** Spinal Stenosis Care {Geo} · Spinal Stenosis Specialists · Lumbar Stenosis
Treatment · Leg Pain When You Walk? · See a Stenosis Specialist · Non-Surgical Stenosis Care ·
Spinal Decompression Options · Stenosis Treatment Near You · Book a Stenosis Consult ·
Cervical Stenosis Treatment · Metro Detroit Spine Care · Board-Certified Spine Doctors ·
{CUSTOMIZER.Doctor Name} Has Openings · Most Insurance Accepted ⚠ · Synergy Health Partners

**Descriptions**
1. Leg pain or numbness that eases when you sit or lean forward? That may be spinal stenosis.
2. Stenosis specialists in {Geo}. Therapy, injections and decompression surgery when needed.
3. Spinal stenosis is treatable at any age. Get evaluated by a board-certified specialist.
4. Understand your options before deciding on surgery. Book a stenosis consult in {Geo}.

---

#### 7. Pinched Nerve / Radiculopathy
**Landing page:** `/conditions/cervical-radiculopathy/`

**Headlines:** Pinched Nerve Treatment {Geo} · Pinched Nerve Specialists · Numbness or
Tingling? · Nerve Pain in Arm or Leg? · Cervical Radiculopathy Care · See a Nerve Pain
Specialist · Non-Surgical Nerve Treatment · Find the Compressed Nerve · Book a Consult in
{Geo} · Weakness in Your Arm? · Metro Detroit Spine Care · Board-Certified Spine Doctors ·
Nerve Pain Relief Near You · {CUSTOMIZER.Doctor Name} Has Openings · Synergy Health Partners

**Descriptions**
1. Numbness, tingling or weakness in an arm or leg often starts in the spine. Get it checked.
2. Pinched nerve specialists in {Geo}. We locate the nerve and treat the compression.
3. Most pinched nerves respond to therapy and targeted injections before surgery is needed.
4. Nerve symptoms that don't resolve deserve a specialist evaluation. Book a consult.

---

#### 8. Spine Surgery (general)
**Landing page:** `/specialty/spine-neck-back/{geo}/`

**Headlines:** Spine Surgeons in {Geo} · Board-Certified Spine Surgeons · Back Surgery
Specialists · Fellowship-Trained Surgeons ⚠ · Spine Surgery Second Opinions · Minimally
Invasive When Possible · Michigan Spine Surgeons · Book a Surgical Consult · Do You Really
Need Surgery? · Complete Care Before & After · Metro Detroit Spine Surgery · Surgery Only When
It's Right · {CUSTOMIZER.Doctor Name} Has Openings · Most Insurance Accepted ⚠ · Synergy Health Partners

**Descriptions**
1. Board-certified spine surgeons in {Geo}. We recommend surgery only when it's the answer.
2. Considering back or neck surgery? Get a second opinion before you decide.
3. From diagnosis through surgery to recovery, one coordinated team in Metro Detroit.
4. Minimally invasive techniques where appropriate. Book a surgical consult in {Geo}.

---

#### 9. Minimally Invasive / Disc Surgery
**Landing page:** `/conditions/herniated-disc/`

**Headlines:** Minimally Invasive Spine {Geo} · Microdiscectomy Specialists · Endoscopic Spine
Surgery · Small Incision Spine Surgery · Discectomy Specialists Near You · Laminectomy
Specialists · Faster Recovery Techniques ⚠ · Disc Surgery Second Opinions · Book a Surgical
Consult · Board-Certified Spine Surgeons · Metro Detroit Spine Surgery · Modern Spine Surgery
Options · {CUSTOMIZER.Doctor Name} Has Openings · Most Insurance Accepted ⚠ · Synergy Health Partners

**Descriptions**
1. Minimally invasive spine surgery in {Geo} by board-certified, fellowship-trained surgeons. ⚠
2. Microdiscectomy, laminectomy and endoscopic techniques for the right candidates.
3. Not everyone is a candidate for minimally invasive surgery. Find out if you are.
4. Get a second opinion on disc surgery from a Metro Detroit spine specialist.

---

---

## 4. Landing pages — the ask for Randall

Every condition ad group above points to a page that **already exists**. The work is
optimization, not creation. Priority order, by ad-group spend potential:

| Priority | Page | Current state | Ask |
|---:|---|---|---|
| 1 | `/conditions/sciatica/` | Live, 91 impr, pos 15.6 | Add scheduler CTA above the fold, "when to see a specialist," geo variants for Sterling + Livonia |
| 2 | `/conditions/herniated-disc/` | Live, in paid use, $611 CPA | Already the best-converting condition page — replicate its structure everywhere else |
| 3 | `/conditions/spinal-stenosis/` | Live, 526 impr | Add CTA + non-surgical-options section |
| 4 | `/conditions/cervical-radiculopathy/` | Live, 759 impr | Add CTA; retitle around "pinched nerve" language patients actually use |

**Two things to confirm before launch:** (a) every page above carries the same
conversion/scheduler tracking as `/specialty/spine-neck-back/{geo}/`, or the new ad groups
will look like they're failing when they aren't; (b) the "some ads limited by policy" flag on
the Spine Conditions campaigns is resolved.

---

## 5. Sequence — what happens when

**This week (no dependencies, do it now)**
- [ ] Fix three live typos: "Evrey" → Every, "Specialits" → Specialists, "Conditons" → Conditions
- [ ] Route "Walk-ins welcome" and "Same-Day Appointments" to compliance
- [ ] Harvest sciatica / stenosis / pinched-nerve keywords out of the paused Pain Management
      ad groups into the new condition ad groups (do **not** rebuild Pain Management — §2.8)
- [ ] Port Sterling Heights Specialist copy structure to Livonia Specialist — largest single inefficiency in spine
- [ ] Unpin the `{CUSTOMIZER}` assets on the two "Poor" ad-strength ads
- [ ] Build Sciatica ad group in Sterling Heights + Livonia, phrase + exact, pointed at `/conditions/sciatica/`
- [ ] Reduce ortho New Patient Intent value $125 → $75 (separate from this build; confirm with Google rep)

**Next two weeks**
- [ ] Build Herniated Disc, Spinal Stenosis, Pinched Nerve ad groups in Sterling + Livonia
- [ ] Split Surgery into four sub-groups (§2.3)
- [ ] Migrate Spine Conditions campaigns into geo campaigns; pause the standalone campaigns
- [ ] Split Back Pain and Neck Pain out of Specialist
- [ ] Restrict Fusion + Injection to exact match, cap bids (§2.8) — frees ~$58,800 at a $1,608 CPA
- [ ] Build Port Huron's four ad groups — cheapest CPA in the account, most starved

**Gated on the Liine/ZocDoc integration fix**
- [ ] Add 1–2 broad match keywords per ad group (§2.6)
- [ ] Once 30+ qualified conversions land in 30 days per campaign, retire `Website - New Patient Intent` as an optimization target
- [ ] Verify no existing-patient conversion signals remain in any conversion column

**Weekly, starting the week of the build**
- [ ] Cost per conversion **by conversion action**, by week — never averaged across weeks
- [ ] New ad groups: impressions, CTR, quality score, cost per real new patient
- [ ] Impression share lost to rank vs. budget — the number that tells you whether the universe actually grew
- [ ] Report the delta, not the average: did this week beat last week, and which action caused it

---

## 6. What I don't know yet, and how I'll find out

Stating these explicitly so nothing here reads as more certain than it is.

1. **The near-me efficiency gap ($109 vs $289) is measured on all conversion actions**, not
   real new patients. The keyword report can't be segmented by conversion action. Build Evan's
   custom columns and re-confirm at the real-NP level before I present the 2.7x to anyone.
2. **Search volumes are Semrush US national.** Metro Detroit is roughly 1–2% of US search
   volume, but the ratio isn't uniform by term. These numbers rank the opportunities correctly;
   they do not forecast our impressions.
3. **I cannot see current impression-share-lost-to-rank per ad group** from these exports —
   that comes from the Google Ads UI. Pull it before and after the build; it is the direct
   measure of whether expansion worked.
4. **Real new patients here means Google Ads conversion actions, not the data lake.** Until the
   data lake is reliable, I can't close the loop from booked to kept. Everything above measures
   booking efficiency, which is the part paid media controls.
5. **The `{CUSTOMIZER.Doctor Name}` / `{CUSTOMIZER.Count}` feed** needs to be verified as
   accurate per geo before the new ad groups inherit it — a stale appointment count is an
   unsubstantiated claim.

---

## 7. Compliance gate

Nothing in §3 runs before:

- **Clinical review** of every treatment description against
  `brand/provider-roster-by-service-line.md` — specifically that fellowship-trained and
  board-certified spine surgeons practice at each named location.
- **Legal/compliance review** of every ⚠ claim: same-day appointments, walk-ins, no referral
  needed, insurance acceptance, on-site MRI, "faster recovery."
- **No superiority claims.** "Best," "#1," "leading" have been removed from all new copy.
  Existing ads still carrying "Top Rated Spine Doctors," "Premier Spine Care Destination" and
  "Michigan spine leaders" should be reviewed for substantiation on the same pass.
- **No outcome promises.** All copy above describes process and access, not results.
- **Accessibility:** condition landing pages must meet WCAG AA before receiving paid traffic.

---

## 8. What Semrush discovery changed

The first pass of this document validated a keyword list I generated myself. That is not
discovery — it confirms ideas rather than finding them. Running Semrush's actual
broad-match/alternate-query discovery against nine seeds produced four corrections. Recording
them here because the corrections matter more than the original estimates.

### 8.1 I badly understated the "near me" cluster

My hand-built list missed the highest-volume phrasings of our best-converting pattern:

| Keyword | My estimate | **Actual (Semrush)** | Currently targeted? |
|---|---:|---:|---|
| spine specialist near me | untested | **5,400** | Yes — 41.4 conv @ $91 |
| spine surgeon near me | untested | **5,400** | Barely — 2.3 conv, $609 spend |
| back doctor near me | untested | **4,400** | Yes — exact, ROAS 1.23 |
| back doctors near me | untested | **2,900** | Yes — exact, **ROAS 2.00** |
| pain management doctors near me | untested | **5,400** | **No** |
| back pain doctor near me | untested | **2,400** | Phrase only — 16.5 conv @ $105 |
| pain management doctor near me | 2,400 | 2,400 | **No** |
| spine surgeons near me | untested | **1,900** | **No** |
| lower back pain doctor near me | 140 | 140 | No |

The pattern: I guessed at long-tail phrasings and got the small ones right while missing the
head terms entirely. **`spine surgeon near me` at 5,400/mo drew $609 of spend and 2.3
conversions in eight weeks** — that is the single largest untapped term in spine.

### 8.2 Condition keywords are mostly informational — I over-promised on them

This is the correction that most changes the plan. Semrush intent coding on the condition
clusters:

| Cluster | Total discovered volume | Transactional / commercial share |
|---|---:|---|
| Sciatica | ~800,000/mo | **~3,300/mo** (doctor / specialist / treatment near me) |
| Spinal stenosis | ~290,000/mo | **~600/mo** |
| Herniated disc | ~350,000/mo | **~2,000/mo** |
| Pinched nerve | ~180,000/mo | **~750/mo** |

"sciatica" itself is 368,000/mo — and it is people looking for stretches, ice packs, how long
it lasts, and whether it's related to pregnancy. That is an **SEO and content opportunity**,
not a paid one, and it belongs to Randall's landing-page work and the organic team rather than
to this build.

**What this means for §2.2:** build the condition ad groups, but build them *narrow* — the
doctor/specialist/treatment-near-me subset only, with aggressive negative lists. My earlier
"~3,150/mo of added demand" figure conflated informational and commercial volume and was
optimistic. The honest number for **paid-viable** added demand across all condition groups is
roughly **6,500–7,000/mo**, and the larger share of the real prize sits in §8.3.

### 8.3 The bigger paid prize isn't conditions — it's "back doctor" and "pain management"

Two clusters with genuine commercial intent, real CPCs (advertisers pay $3–5, which means they
convert), and almost no coverage from us.

> **Superseded in part.** The pain management half of this finding is **not being built**
> (§2.8). The rows below are kept as the record of what discovery found, so the decision can be
> revisited with the clinical side if interventional pain becomes a priority service line. The
> "back doctor" half stands and is fully in the build.


| Keyword | Volume | CPC | Our status |
|---|---:|---:|---|
| doctors for back injuries | 12,100 | $5.22 | Not targeted |
| doctor in back pain | 8,100 | $4.52 | Not targeted |
| back pain doctor | 5,400 | $4.04 | Exact only, 1.5 conv |
| back doctor | 5,400 | $4.76 | Exact only, 7.5 conv |
| pain management doctors near me | 5,400 | $3.15 | **Ad group paused** |
| interventional pain management | 5,400 | $5.11 | Not targeted |
| medial branch block | 8,100 | $1.77 | Not targeted |
| facet joint injection | 3,600 | — | Not targeted |
| pain management clinic near me | 2,900 | $2.69 | **Ad group paused** |
| lower back pain doctor | 1,900 | $4.60 | Not targeted |

Note the pattern in the CPCs: **the highest-CPC spine-adjacent terms in the market are the
"back doctor" ones, and we own almost none of them.** Meanwhile our Back Pain keywords that
*are* live post the best ROAS in the account (`back doctors near me` exact, ROAS 2.00). This
is the strongest single argument for splitting Back Pain out of Specialist as its own ad group.

### 8.4 A high-performing keyword is sitting paused

`"spine doctors"` (phrase, Livonia / Specialist) is **paused**. In the Jun 1 – Jul 24 window it
spent **$21,223** and produced **76.1 conversions at a $279 CPA** — the #2 spine keyword by
spend. Whoever paused it shrank the keyword universe by roughly 15% of Livonia's spine
impressions at a CPA better than the campaign average.

**Find out why it was paused before reactivating it.** If there was a search-term or quality
reason, that reason still applies and needs a negative list instead. If it was an accident, it
is the fastest volume recovery available to you. Either way, this is the kind of thing the
weekly review is supposed to catch.

### 8.5 Discovery also produced the negative lists

The most valuable by-product. `phrase_fullsearch` on "back doctor" returns *back to the future
doctor* (1,000/mo), *doctor recommended mattress for back pain* (2,900/mo), *is doctor odyssey
coming back* (590/mo). On "spine surgeon" it returns *spine surgeon salary* (2,400/mo) and
*top 10 spine surgeons in nyc*. These are exactly what broad match would buy us.

Every ad group in the CSV ships with an ad-group-level negative list built from its own
discovery output — 22 lists in total, printed in full in §10.

The opioid / drug-seeking negative list that was written for the Pain Management ad group is
**no longer needed**, because that ad group is not being built (§2.8). Removing it removes the
compliance exposure at the source rather than managing it with negatives — which is the
stronger answer of the two.

### 8.6 What I could not get

- **Competitor paid data.** `phrase_adwords` returned no results for our head terms in the US
  database, so I have no view of who else is bidding on spine in Metro Detroit or what they're
  paying. Get this from the Google Ads **Auction Insights** report instead — it's account-level
  and more accurate for our geo than Semrush would be.
- **Michigan-specific volume.** All figures are US national. Metro Detroit is roughly 1–2% of
  US search volume but the ratio varies by term. These numbers rank opportunities correctly;
  they do not forecast our impressions.
- Discovery surfaced **`spine specialists of michigan` (480/mo)** — a competitor's brand name.
  Conquesting is legal but it is a strategic and legal call, not a build decision. Flagging it;
  not including it in the CSV.

---

## 9. Match type by keyword — the logic, and the file

The full list is in [`pm/spine-keyword-build-2026-07.csv`](../pm/spine-keyword-build-2026-07.csv).
491 keyword rows plus one negative list per ad group. 195 keywords per full geo build, run across Sterling Heights and Livonia (all 9 ad
groups) and Port Huron (4 core ad groups), plus one negative list per ad group.

### 9.1 The rule I applied

| Match type | When | Count per ad group |
|---|---|---:|
| **Exact** | Terms with proven conversion history in our own data, plus the highest-intent "near me" head terms. Maximum control, lowest wasted spend, best Quality Score. | 4–15 |
| **Phrase** | The expansion body. Variants, treatment names, and condition phrasings where we want reach but still need the core term present. | 9–15 |
| **Broad** | 1–2 only, per Evan. Specific and high-intent — never a bare category term. **Uploaded paused**, enabled only after the ZocDoc fix. | 1–2 |

Two deliberate choices worth defending if challenged:

**Every high-performer gets both an exact and a phrase entry.** `back doctors near me` exact
posts a 2.00 ROAS; the phrase version posts 0.43. That spread is the argument for exact match —
so where a term converts, we run exact to capture the head cleanly and phrase to catch the
tail, and we let the CPA data tell us which to fund. It costs nothing to run both and it
generates the comparison the weekly review needs.

**All 11 broad match keywords per geo ship paused.** They are built, loaded and ready, so enabling them
is a checkbox rather than a project — but they stay off until the Liine/ZocDoc integration
posts online-booking completions back to Google Ads. Broad match steers by conversion signal;
ours is ambiguous today. Turning them on now would spend real money teaching the algorithm the
wrong lesson.

### 9.2 Build size

| Ad group | Exact | Phrase | Broad | Total | New | Reactivated |
|---|---:|---:|---:|---:|---:|---:|
| Spine Specialist | 11 | 15 | 2 | 28 | 12 | 2 |
| Back Pain Specialist | 15 | 15 | 2 | 32 | 15 | 1 |
| Neck Pain Specialist | 8 | 11 | 1 | 20 | 9 | 3 |
| Sciatica | 6 | 10 | 1 | 17 | 11 | 5 |
| Herniated / Bulging Disc | 10 | 15 | 1 | 26 | 8 | 1 |
| Spinal Stenosis | 5 | 9 | 1 | 15 | 12 | 1 |
| Pinched Nerve / Radiculopathy | 4 | 10 | 1 | 15 | 13 | 1 |
| Spine Surgery | 8 | 15 | 1 | 24 | 10 | 0 |
| Minimally Invasive / Disc Surgery | 8 | 9 | 1 | 18 | 10 | 2 |
| **Per geo** | **75** | **109** | **11** | **195** | **100** | **16** |

Sterling Heights and Livonia take the full 195 each. Port Huron takes the four core ad groups
— Spine Specialist, Back Pain Specialist, Sciatica, Spine Surgery — because its Specialist
group runs the cheapest CPA in the account ($339) on 1,165 impressions and deserves more
surface area before we build depth there. Southfield stays minimal until its impression base
justifies more.

Against 379 unique keywords today, this adds **491 keyword rows and 66 genuinely new terms**,
weighted toward the patterns our own data already proves convert.

### 9.3 Five keywords to watch daily in week one

Not because they're wrong — because they're the ones most likely to spend fast in an
unexpected direction:

| Keyword | Ad group | Risk |
|---|---|---|
| "sciatica pain relief" (40,500) | Sciatica | Informational intent at scale. If CPA runs hot in 48h, pause and keep only the near-me set. |
| "sciatica treatment" (27,100) | Sciatica | Same. |
| "spinal stenosis treatment" (8,100) | Spinal Stenosis | Same. |
| "spinal decompression" | Minimally Invasive | Dominated by chiropractic decompression-table intent, not surgical. |
| "doctors for back injuries" (12,100) | Back Pain Specialist | Highest volume in the build, $5.22 CPC. Also attracts workers-comp and legal intent — may be good, may not. Watch it. |

That watchlist *is* the daily conversion analysis Evan described, scoped to something you can
actually do in ten minutes a morning.

---

## 10. The keyword list, organized by match type

Nine ad groups. Every keyword below, grouped under the match type it should be
built with. Identical build for **Sterling Heights** and **Livonia**; **Port Huron**
takes the four marked `[PH]`. Volumes are Semrush US national, monthly.

`ACTION` — **NEW** = does not exist today · **EXISTING** = already live, keep
· **REACTIVATE** = exists but paused · **MOVE** = exists in a different ad group.


### Spine Specialist `[PH]`

_28 keywords — 11 exact, 15 phrase, 2 broad_

**EXACT MATCH** (11)

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `[spine specialist near me]` | 5400 | EXISTING | 8.9 conv, ROAS 0.81 |
| `[spine specialist]` | 4400 | EXISTING | 16.7 conv |
| `[spine doctor near me]` | — | NEW | phrase ver = $51 CPA, best in spine |
| `[spine doctors]` | — | REACTIVATE | phrase ver paused w/ $21,223 spend, 76 conv |
| `[orthopedic spine specialist near me]` | 590 | NEW |  |
| `[ortho spine specialist]` | — | EXISTING | 5.0 conv |
| `[spine pain specialist near me]` | 170 | NEW |  |
| `[best spine specialist near me]` | 210 | NEW |  |
| `[back and spine specialist near me]` | 320 | NEW |  |
| `[spine doctors in my area]` | — | EXISTING |  |
| `[best spine doctors in michigan]` | — | EXISTING | 4.0 conv |

**PHRASE MATCH** (15)

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `"spine specialist near me"` | 5400 | EXISTING | 41.4 conv @ $91 CPA |
| `"spine doctor near me"` | — | EXISTING | 28.9 conv @ $51 CPA - best CPA in spine |
| `"spine doctors"` | — | REACTIVATE | PAUSED - was #2 kw by spend, $279 CPA |
| `"spine specialist"` | 4400 | EXISTING |  |
| `"spine pain specialist"` | — | EXISTING | 30.6 conv @ $244 |
| `"spine pain specialist near me"` | 170 | EXISTING | 13.0 conv @ $78 |
| `"orthopedic spine specialist"` | 1600 | NEW |  |
| `"spine and orthopedic specialists"` | 1600 | NEW |  |
| `"back and spine specialist"` | 320 | NEW |  |
| `"cervical spine specialist"` | 210 | NEW |  |
| `"spine center near me"` | 170 | NEW |  |
| `"spine clinic near me"` | 210 | NEW |  |
| `"non surgical spine specialist"` | 170 | NEW |  |
| `"ortho spine specialist"` | — | EXISTING | 18.0 conv @ $71 |
| `"best spine doctor near me"` | — | EXISTING |  |

**BROAD MATCH** (2) — upload **paused**, enable only after the Liine/ZocDoc fix

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `spine specialist near me` | 5400 | GATED | after ZocDoc fix |
| `orthopedic spine surgeon near me` | 390 | GATED | after ZocDoc fix |

**Ad-group negatives**

```
-salary -jobs -"icd 10" -"what is a" -school -residency -nyc -nj -"new jersey" -"long island" -dallas -texas -florida
```


### Back Pain Specialist `[PH]`

_32 keywords — 15 exact, 15 phrase, 2 broad_

**EXACT MATCH** (15)

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `[back doctors near me]` | 2900 | EXISTING | 4.0 conv, ROAS 2.00 - best ROAS in spine |
| `[back doctor near me]` | 4400 | EXISTING | 11.0 conv, ROAS 1.23 |
| `[back specialist near me]` | — | EXISTING | 13.0 conv, ROAS 1.00 |
| `[back dr near me]` | — | EXISTING | 8.5 conv, ROAS 1.01 |
| `[back pain doctor near me]` | 2400 | NEW | phrase ver = 16.5 conv @ $105 |
| `[back doctor]` | 5400 | EXISTING | 7.5 conv |
| `[back pain doctor]` | 5400 | EXISTING | 1.5 conv |
| `[back pain specialist]` | — | EXISTING | 9.2 conv @ $286 |
| `[back pain specialist near me]` | — | EXISTING | 1.0 conv |
| `[back pain doctors near me]` | 390 | NEW |  |
| `[lower back pain doctor]` | 1900 | NEW |  |
| `[orthopedic back doctor near me]` | 260 | NEW |  |
| `[best back doctor near me]` | 320 | NEW |  |
| `[back and spine doctor near me]` | 210 | NEW |  |
| `[doctor for back pain near me]` | 260 | NEW |  |

**PHRASE MATCH** (15)

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `"back doctors near me"` | 2900 | EXISTING | 17.0 conv @ $140 |
| `"back pain doctor near me"` | 2400 | EXISTING | 16.5 conv @ $105 |
| `"back specialist near me"` | — | EXISTING | 15.5 conv @ $127 |
| `"back doctor near me"` | 4400 | EXISTING |  |
| `"back specialist"` | — | EXISTING | 16.0 conv @ $261 |
| `"back pain specialist near me"` | — | EXISTING | 2.0 conv |
| `"doctor in back pain"` | 8100 | NEW | CPC $4.52, commercial intent |
| `"doctors for back injuries"` | 12100 | NEW | CPC $5.22 - highest vol commercial term found |
| `"lower back pain doctor"` | 1900 | NEW |  |
| `"back problem doctor"` | 1600 | NEW |  |
| `"lower back specialist doctors"` | 320 | NEW |  |
| `"back and spine doctors"` | 260 | NEW |  |
| `"back pain doctors near me"` | 390 | NEW |  |
| `"chronic back pain doctor near me"` | 30 | NEW |  |
| `"back pain treatment near me"` | — | REACTIVATE | 0 impr - sitting in paused Pain Mgmt |

**BROAD MATCH** (2) — upload **paused**, enable only after the Liine/ZocDoc fix

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `back pain specialist near me` | — | GATED | after ZocDoc fix |
| `back doctor near me` | 4400 | GATED | after ZocDoc fix |

**Ad-group negatives**

```
-"back to the future" -mattress -chiropractor -chiropractic -salary -"icd 10" -exercises -stretches -"what is a back doctor" -"doctor odyssey" -"doctor who" -"doctor stone" -pillow -brace -massage
```


### Neck Pain Specialist

_20 keywords — 8 exact, 11 phrase, 1 broad_

**EXACT MATCH** (8)

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `[neck pain doctor near me]` | 390 | NEW |  |
| `[neck specialist]` | — | EXISTING | 3.0 conv |
| `[neck and back specialist near me]` | — | EXISTING |  |
| `[orthopedic neck specialist near me]` | — | EXISTING |  |
| `[neck pain specialist]` | — | NEW |  |
| `[neck doctor near me]` | — | NEW |  |
| `[best neck pain doctor near me]` | 210 | NEW |  |
| `[neck and spine specialist near me]` | 170 | NEW |  |

**PHRASE MATCH** (11)

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `"neck pain specialist"` | — | EXISTING | 35.2 conv @ $169 - strongest neck term |
| `"neck pain specialist near me"` | — | EXISTING | 2.5 conv |
| `"neck specialist near me"` | — | EXISTING | 3.0 conv |
| `"neck doctor near me"` | — | EXISTING | 5.5 conv @ $87 |
| `"neck pain doctor"` | 1300 | NEW |  |
| `"neck pain doctor near me"` | 390 | NEW |  |
| `"cervical spine specialist"` | 210 | NEW |  |
| `"neck and back pain doctor near me"` | 210 | NEW |  |
| `"neck pain treatment near me"` | — | REACTIVATE | 0 impr - in paused Pain Mgmt |
| `"neck pain treatment"` | — | REACTIVATE | in paused Pain Mgmt |
| `"neck physical therapy near me"` | — | REACTIVATE | in paused Pain Mgmt |

**BROAD MATCH** (1) — upload **paused**, enable only after the Liine/ZocDoc fix

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `neck pain specialist near me` | — | GATED | after ZocDoc fix |

**Ad-group negatives**

```
-"icd 10" -"red flags" -"when to see" -stretches -exercises -pillow -massage -chiropractor -"lump on back of neck" -salary
```


### Sciatica `[PH]`

_17 keywords — 6 exact, 10 phrase, 1 broad_

**EXACT MATCH** (6)

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `[sciatica treatment near me]` | 1900 | NEW | highest transactional sciatica term |
| `[sciatica doctor near me]` | 720 | NEW |  |
| `[sciatica specialist near me]` | 260 | NEW |  |
| `[sciatica pain doctor]` | 260 | NEW |  |
| `[sciatica specialist]` | 170 | NEW |  |
| `[doctor for sciatica]` | 170 | NEW |  |

**PHRASE MATCH** (10)

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `"sciatica treatment near me"` | 1900 | NEW |  |
| `"sciatica doctor near me"` | 720 | NEW |  |
| `"sciatica specialist near me"` | 260 | NEW |  |
| `"sciatica specialist"` | 170 | NEW |  |
| `"sciatica pain doctor"` | 260 | NEW |  |
| `"sciatica treatment"` | 27100 | REACTIVATE | PAUSED. High vol but mostly informational - watch CPA daily |
| `"sciatica pain relief"` | 40500 | REACTIVATE | PAUSED. Informational-heavy - start paused, test 2nd |
| `"sciatic nerve pain relief"` | 22200 | REACTIVATE | PAUSED. Same caution |
| `"physical therapy for sciatica near me"` | — | REACTIVATE | in paused Pain Mgmt |
| `"sciatica treatment southfield"` | — | REACTIVATE | Southfield campaign only |

**BROAD MATCH** (1) — upload **paused**, enable only after the Liine/ZocDoc fix

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `sciatica specialist near me` | 260 | GATED | after ZocDoc fix |

**Ad-group negatives**

```
-stretches -exercises -"icd 10" -pregnancy -pregnant -"how to" -"what is" -"how long" -mattress -chiropractic -chiropractor -cream -brace -"at home" -"ice pack" -symptoms -"feel like" -medication -pillow -"does it go away" -meaning
```


### Herniated / Bulging Disc

_26 keywords — 10 exact, 15 phrase, 1 broad_

**EXACT MATCH** (10)

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `[herniated disc treatment near me]` | 1600 | NEW | CPC $2.65, transactional |
| `[herniated disc doctor near me]` | 140 | NEW |  |
| `[herniated disc specialist near me]` | 70 | NEW |  |
| `[herniated disc specialist]` | 260 | NEW |  |
| `[discectomy]` | — | EXISTING | migrate from Spine Conditions campaign |
| `[surgery for herniated disc]` | — | EXISTING | migrate |
| `[disc herniation surgery]` | — | EXISTING | migrate |
| `[disc surgery]` | — | EXISTING | migrate |
| `[discectomy surgery]` | — | EXISTING | migrate |
| `[acdf surgery]` | — | EXISTING | migrate - flagged low quality, needs relevant ad |

**PHRASE MATCH** (15)

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `"herniated disc treatment near me"` | 1600 | NEW |  |
| `"herniated disc surgery"` | 8100 | EXISTING | migrate from Spine Conditions |
| `"herniated disc treatments"` | — | EXISTING | migrate |
| `"herniated disc doctor near me"` | 140 | EXISTING | 2 impr only |
| `"herniated disc specialist"` | 260 | NEW |  |
| `"bulging disc treatment"` | 6600 | NEW | zero coverage today |
| `"bulging disc doctor near me"` | 10 | NEW |  |
| `"slipped disc specialist"` | — | REACTIVATE | paused |
| `"slipped disc surgeon"` | — | EXISTING | migrate |
| `"ruptured disk treatment"` | — | EXISTING | migrate |
| `"ruptured disc surgery"` | — | EXISTING | migrate |
| `"treatment for herniated disc"` | — | EXISTING | migrate |
| `"degenerative disc disease treatment"` | 1300 | EXISTING | migrate |
| `"degenerative disc surgery"` | — | EXISTING | migrate |
| `"degenerative disc repair"` | — | EXISTING | migrate |

**BROAD MATCH** (1) — upload **paused**, enable only after the Liine/ZocDoc fix

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `herniated disc specialist near me` | 70 | GATED | after ZocDoc fix |

**Ad-group negatives**

```
-"icd 10" -exercises -stretches -"how to" -"what is" -symptoms -"vs bulging" -"versus bulging" -sza -"pain killer" -painkiller -medication -"heal quickly" -"recovery time" -"feel like" -"l5 s1" -"self-care" -"signs"
```


### Spinal Stenosis

_15 keywords — 5 exact, 9 phrase, 1 broad_

**EXACT MATCH** (5)

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `[spinal stenosis specialist near me]` | 260 | NEW |  |
| `[spinal stenosis treatment near me]` | 210 | NEW |  |
| `[spinal stenosis specialist]` | 110 | NEW |  |
| `[spinal stenosis doctor near me]` | 30 | NEW |  |
| `[spinal stenosis surgery]` | 5400 | EXISTING | flagged low quality - fix w/ relevant ad + LP |

**PHRASE MATCH** (9)

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `"spinal stenosis specialist near me"` | 260 | NEW |  |
| `"spinal stenosis treatment near me"` | 210 | NEW |  |
| `"spinal stenosis treatment"` | 8100 | NEW | informational-heavy - monitor |
| `"spinal stenosis surgery"` | 5400 | NEW |  |
| `"surgery for spinal stenosis"` | 1000 | NEW |  |
| `"lumbar spinal stenosis treatment"` | 880 | NEW |  |
| `"lumbar stenosis treatment"` | 90 | NEW |  |
| `"spinal stenosis specialist"` | 110 | NEW |  |
| `"spinal stenosis therapies"` | — | REACTIVATE | in paused Pain Mgmt, flagged low quality |

**BROAD MATCH** (1) — upload **paused**, enable only after the Liine/ZocDoc fix

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `spinal stenosis specialist near me` | 260 | GATED | after ZocDoc fix |

**Ad-group negatives**

```
-"icd 10" -exercises -symptoms -"what is" -disability -"kill you" -"final stages" -hereditary -"to avoid" -"cured" -"painkiller" -"newest treatment" -"which is worse"
```


### Pinched Nerve / Radiculopathy

_15 keywords — 4 exact, 10 phrase, 1 broad_

**EXACT MATCH** (4)

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `[pinched nerve treatment near me]` | 590 | NEW |  |
| `[pinched nerve doctor near me]` | 110 | NEW | CPC $4.24 |
| `[pinched nerve specialist near me]` | 50 | NEW |  |
| `[radiculopathy doctor near me]` | 20 | NEW | CPC $3.27 |

**PHRASE MATCH** (10)

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `"pinched nerve treatment near me"` | 590 | NEW |  |
| `"pinched nerve doctor near me"` | 110 | NEW |  |
| `"pinched nerve specialist near me"` | 50 | NEW |  |
| `"pinched nerve treatment"` | 4400 | NEW |  |
| `"treatment for pinched nerve in neck"` | 3600 | NEW |  |
| `"neck nerve pinch treatment"` | 4400 | NEW |  |
| `"cervical radiculopathy treatment"` | 4400 | NEW | CPC $1.21 |
| `"pinched nerve therapy neck"` | 5400 | NEW |  |
| `"treatment for pinched nerve in lower back"` | — | REACTIVATE | in paused Pain Mgmt |
| `"radiculopathy treatment"` | — | NEW |  |

**BROAD MATCH** (1) — upload **paused**, enable only after the Liine/ZocDoc fix

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `pinched nerve doctor near me` | 110 | GATED | after ZocDoc fix |

**Ad-group negatives**

```
-shoulder -hip -"how to" -"what is" -"how long" -symptoms -"feel like" -"icd 10" -stretches -exercises -"relieve" -"fix a"
```


### Spine Surgery `[PH]`

_24 keywords — 8 exact, 15 phrase, 1 broad_

**EXACT MATCH** (8)

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `[spine surgeon near me]` | 5400 | NEW | LARGEST MISS - 5,400/mo, not targeted |
| `[spine surgeons near me]` | 1900 | NEW |  |
| `[orthopedic spine surgeon near me]` | 390 | NEW |  |
| `[orthopedic spine surgeon]` | 1000 | EXISTING |  |
| `[michigan orthopedic spine surgeons]` | — | EXISTING | 15.0 conv @ $122 |
| `[spine surgeon]` | 4400 | NEW |  |
| `[back surgeon near me]` | — | EXISTING | 1.0 conv |
| `[best spine doctors in michigan]` | — | EXISTING |  |

**PHRASE MATCH** (15)

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `"orthopedic spine surgeon"` | 1000 | EXISTING | #1 spine kw: 126.6 conv @ $213 |
| `"spinal surgery"` | — | EXISTING | 29.4 conv @ $417 |
| `"spine surgery"` | — | EXISTING | 29.0 conv @ $357 |
| `"back surgeons in michigan"` | — | EXISTING | 25.6 conv @ $300 |
| `"spinal surgeons near me"` | — | EXISTING | 8.3 conv @ $90 - strong |
| `"spine surgeon near me"` | 5400 | EXISTING | 2.3 conv - underfunded |
| `"spine surgeons near me"` | 1900 | NEW |  |
| `"orthopedic spine surgeon near me"` | 390 | EXISTING |  |
| `"spine orthopedic surgeon"` | 1000 | NEW |  |
| `"spine surgery surgeon"` | 2900 | NEW |  |
| `"lower back surgery"` | — | EXISTING |  |
| `"neck surgery"` | — | EXISTING | 6.5 conv @ $740 - watch |
| `"cervical fusion surgery"` | 1900 | NEW |  |
| `"lumbar fusion surgery"` | 1900 | NEW |  |
| `"minimally invasive spine surgeon"` | 260 | NEW |  |

**BROAD MATCH** (1) — upload **paused**, enable only after the Liine/ZocDoc fix

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `spine surgeon near me` | 5400 | GATED | after ZocDoc fix |

**Ad-group negatives**

```
-salary -"how much" -"top 10" -jobs -residency -"make" -nyc -nj -"new jersey" -"long island" -dallas -texas -florida -"united states" -"icd 10" -"best in the"
```


### Minimally Invasive / Disc Surgery

_18 keywords — 8 exact, 9 phrase, 1 broad_

**EXACT MATCH** (8)

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `[minimally invasive spine surgery near me]` | 390 | NEW |  |
| `[endoscopic spine surgery near me]` | 210 | NEW |  |
| `[microdiscectomy near me]` | 110 | NEW | CPC $3.06 |
| `[microdiscectomy]` | — | EXISTING | move from Surgery |
| `[laminectomy]` | — | REACTIVATE | paused |
| `[laminectomy surgery]` | — | EXISTING | move from Surgery |
| `[decompression surgeries]` | — | EXISTING | move from Surgery |
| `[artificial disc replacement near me]` | 140 | NEW |  |

**PHRASE MATCH** (9)

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `"minimally invasive spine surgery near me"` | 390 | NEW |  |
| `"minimally invasive spinal surgery"` | — | EXISTING | move from Surgery |
| `"endoscopic spine surgery near me"` | 210 | NEW |  |
| `"microdiscectomy"` | — | NEW |  |
| `"lumbar laminectomy"` | — | EXISTING | move from Surgery, 1.0 conv |
| `"cervical disc replacement"` | 2900 | NEW |  |
| `"lumbar disc replacement"` | 1000 | NEW |  |
| `"artificial disc replacement near me"` | 140 | NEW |  |
| `"spinal decompression"` | — | REACTIVATE | CAUTION: chiro decompression-table intent, watch search terms |

**BROAD MATCH** (1) — upload **paused**, enable only after the Liine/ZocDoc fix

| Keyword (as entered) | Vol/mo | Action | Note |
|---|---:|---|---|
| `minimally invasive spine surgery near me` | 390 | GATED | after ZocDoc fix |

**Ad-group negatives**

```
-chiropractic -chiropractor -table -machine -"at home" -inversion -salary -cost -"how much" -nyc -nj -dallas -"recovery time"
```
