# Spine Growth — August Execution & Measurement Plan (as of 2026-08-05)

> Built for the marketing meeting. Data sources: the week-of-8/3 new-patient export
> (`data__20260805`, new patients by service line × provider, first-appt dates 8/3–8/7)
> and the live `Consolidated Priority To-Do` (Notion) through the 8/4 transcripts.
> Goal figures use July's plan (spine 352/mo, ortho 522/mo) as the working target —
> **confirm against the actual August budget** (2026 Budget page).

---

## 1. Tracking to monthly August goals

**Week 1 (8/3–8/7) booked new patients — from the uploaded export:**

| Service line | Wk-1 booked | If pace holds (×4.4 wks) | Aug goal (July plan) | Run-rate % to plan | Board run-rate target |
|---|---|---|---|---|---|
| **Spine** | **67** | ~295 | 352 | **~84%** | 60+/wk → **beating it** |
| **Ortho** | **132** | ~580 | 522 | **~111%** | 120+/wk → **beating it** |
| Foot | 44 | ~195 | — | — | — |
| Hand | 9 | ~40 | — | — | — |
| Pain & Other | 6 | ~27 | — | — | — |
| Primary Care | 4 | ~18 | — | — | — |
| **Total** | **262** | ~1,160 | 1,333 | ~87% | — |

**Spine by provider (Wk 1):** Varghese 20 · Maslak 19 · **McCarty 16** · Salar 11 · Zamorano 1.

**Read:**
- Spine at 67 is a real step up from July's **56% of plan (201/352)** — if it holds it's ~84%, and it clears the 60+/week stabilization target. Varghese's return (20) is doing exactly what was predicted; Maslak (19) and McCarty (16) round out the core.
- **McCarty is the one converting new patients to surgery at benchmark (~8%)** — his 16 are the most valuable of the set. The other three spine surgeons convert at 2–4%, so volume ≠ revenue until that closes (a clinical-ops flag, but it caps this plan's payoff).
- **Caveats before you report this:** 8/6–8/7 are future bookings (today is 8/5), so the 67 can still move; Friday 8/7 looks light (7 spine). These are *booked*, not *kept* — pair with the booked-to-kept rate. Zamorano at 1 is worth a scheduling look.

---

## 1b. Booking behavior — patients book close-in (this reshapes the plan)

From the three lead-time exports (week-of-8/3 first appts × create date):

| Lead time (book → appt) | Spine | Ortho | All |
|---|---|---|---|
| Same day | 4.5% | 12.9% | 11.1% |
| 1–2 days | 22.4% | 17.4% | 22.5% |
| 3–6 days | 44.8% | 37.9% | 38.9% |
| 7–13 days | 16.4% | 22.0% | 18.3% |
| 14–29 days | 9.0% | 9.1% | 7.6% |
| 30+ days | 3.0% | 0.8% | 1.5% |
| **Avg lead time** | **6.8 days** | **5.6 days** | **5.7 days** |
| **Booked ≤7 days out** | **78%** | **75%** | **78%** |

**What this means for the meeting:**
- **There is almost no advance backlog.** ~78% of new patients book within a week of their visit and ~93% within two weeks. Weekly volume ≈ *that week's* demand capture — a lost call or slow response this week is a patient lost **this week**, not deferred.
- **So the P0 funnel fixes are the highest-ROI spine work**, right alongside keyword expansion: the ~30% spine call-routing leak, the broken "What Hurts" nav, the MRI script, and phone-answer speed all convert directly into same-week volume.
- **It validates the ZocDoc "turn on 1–2 weeks before clinic day" tactic** — that's exactly the window patients book in.
- **Spine books a touch longer-lead than ortho** (6.8 vs 5.6 days; 4.5% same-day vs ortho's 12.9%) — a slightly larger consideration window where condition pages, reviews, and E-E-A-T can tip the choice. Ortho skews same-day/impulse, so paid + instant availability dominate there.
- **Reading the scoreboard:** because booking is fast, keyword-expansion → visits will show up in the data within days (good for the 2-week board story) — and this week's **67 spine is a floor**, still filling for the 8/6–8/7 appts as same-week bookings land.

---

## 2. B2C — SEO & website actions for spine

| Action | Owner | What / this-week move |
|---|---|---|
| **Spine Google Ads keyword expansion (2–4 → 8–10 ad groups)** — the #1 lever; spine is keyword/rank-limited (14K eligible impressions vs ortho 26K, 0% share lost to budget) | Joe (+ Mendelson experiments, vendor) | Add 1–2 high-intent broad-match keywords per ad group; tailor ad copy per condition theme. **Fund it by trimming foot/pain ZocDoc lines, not hand** (hand is cost-efficient). |
| **Condition landing pages** (sciatica, stenosis, herniated disc, DDD, spondylolisthesis) to support the new ad groups | Randall | Ship sciatica first; **CTA above the fold** on each (per 7/29 note). |
| **Spine SEO content cluster** — GSC export → gap analysis → title/meta fixes → hyper-local pages (Troy, Clawson, Sterling Heights) by patient origin | Joe/Randall (contractor blocked on access — resolve) | Schedule the **Cardinal SEO readout this week** (Sauder + Rithika); ping Evan next week re keyword expansion. |
| **Fix "What Hurts" nav** — condition categories missing from the menu (funnel leak) | Paul | Likely a cloud-account reconnect. |
| **Doctor-profile CLS / Core Web Vitals** — image-heavy menu + satisfaction-widget flash | Paul/dev | Lazy-load + compress cautiously. |
| **Kevin Troy campaign** (new, from 8/4) + expand his Troy hours | Joe | Launch; test whether volume pulls him out of Southfield. |
| **Cloudflare AI-crawler unblock** — Profound has AI visibility at 4.8% | Blocked on Proactive (WAF access) | Escalate the access request. |

---

## 3. B2B — spine target-account actions

| Action | Owner | What / this-week move |
|---|---|---|
| **Confirm the B2B master list actually locked** — Santosh's protected spreadsheet is overdue (due 7/27) | Joe → Santosh | Run it down today; the PL team is already working off the ~800-account scrub. |
| **Tier-1 visits underway** — top ~90 proven senders within the 21-day window; ~150 account touches/week | Kristen / Cody / Jasmine | Routes went live **Mon 8/3** — confirm Tier-1 coverage started. |
| **Structured visit notes** — ~5 qualifiers (insurance mix, volume, hospital affiliation, existing spine-surgeon relationships) in MapMyCustomer | Kristen / Joe | Use Cody's notes as the playbook model. |
| **Somerset Pain Clinic** — hot target actively seeking a new referral destination | PL + spine MD | Bring **McCarty or Varghese** on the visit. |
| **PL dedication to spine-centric/adjacent accounts** — the board's named "extra" lever | Kristen | Recover the 2–3 refs/mo lost post-Sean; grow PL contribution 79 → 95–110/mo (stretch 150). |
| **Hospital gap** — no call on Ascension / St. Mary's / Corewell limits organic spine referral; primary targets = ortho spine surgeons + neurosurgeons | Kristen | Add to territory plan. |

---

## 4. Measurement of each initiative

Ties to the 8/4 board mandate: *track visits + eligible impressions weekly as the spine scoreboard.*

| Initiative | Primary metric | Instrument | Cadence | Baseline → Target |
|---|---|---|---|---|
| **Monthly goal tracking** | New patients by SL & provider | This export (rerun weekly) | Weekly | Spine 67/wk → 60+ stable, then 80 |
| **Spine keyword expansion** | Eligible impressions + impression share; spine paid new patients | Google Ads / GA4 | Weekly | 14K impressions → toward ortho's 26K |
| **Condition landing pages / SEO** | Non-branded spine impressions, clicks, avg position; LP sessions + engagement | GSC + GA4 + Semrush | Weekly/monthly | Spine hub ~52 organic sessions/90d → grow |
| **Website fixes (nav, CLS, CTA)** | CWV pass; nav crawlable; LP conversion rate | PSI + GA4 | On ship, then weekly | CLS < 0.10; nav restored |
| **B2B PL execution** | Visits/touches per week; Tier-1 coverage; B2B-matched spine referrals/mo | MapMyCustomer + referral report | Weekly | ~150 touches/wk; refs 79 → 95–110/mo |
| **AI visibility** | Profound AI-answer visibility % | Profound (post-unblock) | Monthly | 4.8% → set target after unblock |
| **Booking behavior** | Avg lead time + % booked ≤7 days | This booking-lead-time export | Weekly | Spine 6.8 days — watch for compression (capacity strain) or a lengthening tail (lost same-week capture) |

---

## Board slide (due Thu 8/6) — the 3 core metrics
1. **New-patient run-rate:** ortho 132/wk (>120 target) · spine 67/wk (>60 target) — spine recovering off July's 56%.
2. **Leading indicator the strategy is working:** spine eligible impressions + target visits (start tracking 8/5).
3. **The cap to name:** spine surgical conversion 2–4% vs 8% benchmark (only McCarty) + Q2 ASC miss (~$1M ortho, ~$1.2M spine) — marketing is filling the funnel; conversion is the downstream gate.
