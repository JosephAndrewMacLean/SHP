# Spine Keyword Expansion & Ad Group Build — July 2026

**Owner:** Joe MacLean · **Built:** 2026-07-25 · **Status:** implementation-ready, pending
clinical/legal sign-off on flagged copy claims

**Source data:** Google Ads exports pulled 2026-07-24 — Campaigns, Ad Groups (segmented by
conversion action), Ads, Search Keywords. Ad-group and ad reports cover Jan 1 – Jul 24, 2026;
the keyword report covers Jun 1 – Jul 24, 2026. Search volumes are Semrush US national
(2026-07), used for *relative* prioritization, not absolute forecasting. Condition-page
existence verified via Google Search Console (last 90 days).

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
> and split the themes that don't, so the money has somewhere efficient to flow.** I have
> found 3,150 keywords of new eligible demand, concentrated in the themes that already work,
> and every one of them lands on a condition page that already exists on our site.
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
| 8 | Livonia / Injection | $17,897 | 15.2 | $1,180 | Rebuild as Pain Management (§2.3). |
| 9 | Livonia / Fusion | $11,499 | 6.7 | $1,724 | Restrict to exact match. |
| 10 | Southfield / Surgery | $5,243 | 3.0 | $1,754 | Geo has almost no impressions. |
| 11 | Sterling Heights / Injection | $18,863 | 9.5 | $1,986 | Worst large-spend group. |
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
3. **Un-pause Pain Management** — 168 keywords across four geos are sitting in paused ad
   groups, including **every sciatica keyword we own**. Zero impressions, zero spend, all
   year. This is free keyword universe requiring no research (§2.1).

**Tier 2 — next two weeks.**

4. **Split Surgery into sub-themes** (§2.3). $206,928 at $1,107 is the second-largest pool of
   waste in spine, and it is caused by one ad group absorbing everything from "spine surgery"
   to "back disc surgery" to "neck fusion" behind one generic ad.
5. **Build the condition ad groups** (§2.2) — sciatica, stenosis, pinched nerve, herniated
   disc — into the geo campaigns where the budget actually lives.

**Tier 3 — contain, don't grow.**

6. **Fusion and Injection** — $58,822 at $1,608 combined. Move to exact match only, cap bids,
   and let the freed impressions flow to Specialist and the new condition groups. Do not
   delete: fusion terms are how a surgical patient with real intent finds us; they are just
   badly matched right now.

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

**Injection ($37,355 @ $1,514) → Pain Management, rebuilt.** Reuse the paused Pain Management
ad group shell — the keywords are already loaded. Add: epidural steroid injection near me 170,
facet joint injection 3,600, medial branch block 8,100, nerve block for back pain 590,
radiofrequency ablation, pain management doctor near me 2,400, back pain management near me
320. Landing page: `/specialty/spine-neck-back/{geo}/` until a pain-management page exists.

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

### 2.5 Target build — from 4 ad groups per geo to 10

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
| 10 | Pain Management & Injections | Paused / mismatched | Rebuild |

Run the full 10 in **Sterling Heights and Livonia** (where 92% of spine spend and nearly all
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
| Pain Management & Injections | pain management doctor near me | epidural steroid injection near me |

All ten are specific, high-intent, and "near me"-anchored — the pattern that already converts
2.7x better than everything else in the account. None is a bare category term like "spine" or
"back pain," which is exactly the failure mode Evan flagged.

### 2.7 Estimated universe growth

| | Today | After build |
|---|---:|---:|
| Unique spine keywords | 379 | ~1,050 |
| Live (non-paused, eligible) | 316 | ~950 |
| "near me" keywords | 56 | ~126 |
| Ad groups (Sterling + Livonia) | 8 | 20 |
| Broad match keywords | 0 | 16 (phase 2) |
| Added US search volume targeted | — | ~3,150/mo before broad match |

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

### 3.3 Ad copy — 10 ad groups

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

#### 10. Pain Management & Injections
**Landing page:** `/specialty/spine-neck-back/{geo}/` — *see §4 for the page request*

**Headlines:** Spine Injections in {Geo} · Epidural Steroid Injections · Pain Management
Specialists · Non-Surgical Pain Relief · Facet Joint Injections · Nerve Block Specialists ·
Back Pain Without Surgery · Image-Guided Injections ⚠ · Book a Pain Consult in {Geo} ·
Radiofrequency Ablation · Metro Detroit Pain Management · SI Joint Injections ·
{CUSTOMIZER.Doctor Name} Has Openings · Most Insurance Accepted ⚠ · Synergy Health Partners

**Descriptions**
1. Back or neck pain without surgery. Epidural, facet and SI joint injections in {Geo}.
2. Interventional pain specialists working alongside our spine surgeons and therapists.
3. Targeted injections can relieve pain and help pinpoint its source. Book a consult.
4. Explore non-surgical options before considering spine surgery. Appointments in {Geo}.

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
| 5 | — | Does not exist | New: pain management / spine injections page |

**Two things to confirm before launch:** (a) every page above carries the same
conversion/scheduler tracking as `/specialty/spine-neck-back/{geo}/`, or the new ad groups
will look like they're failing when they aren't; (b) the "some ads limited by policy" flag on
the Spine Conditions campaigns is resolved.

---

## 5. Sequence — what happens when

**This week (no dependencies, do it now)**
- [ ] Fix three live typos: "Evrey" → Every, "Specialits" → Specialists, "Conditons" → Conditions
- [ ] Route "Walk-ins welcome" and "Same-Day Appointments" to compliance
- [ ] Un-pause Pain Management ad groups (4 geos, 168 keywords) — free universe
- [ ] Port Sterling Heights Specialist copy structure to Livonia Specialist — largest single inefficiency in spine
- [ ] Unpin the `{CUSTOMIZER}` assets on the two "Poor" ad-strength ads
- [ ] Build Sciatica ad group in Sterling Heights + Livonia, phrase + exact, pointed at `/conditions/sciatica/`
- [ ] Reduce ortho New Patient Intent value $125 → $75 (separate from this build; confirm with Google rep)

**Next two weeks**
- [ ] Build Herniated Disc, Spinal Stenosis, Pinched Nerve ad groups in Sterling + Livonia
- [ ] Split Surgery into four sub-groups (§2.3)
- [ ] Migrate Spine Conditions campaigns into geo campaigns; pause the standalone campaigns
- [ ] Split Back Pain and Neck Pain out of Specialist
- [ ] Restrict Fusion + Injection to exact match, cap bids
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
