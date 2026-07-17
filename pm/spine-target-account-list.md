# Spine Target-Account List + First-Week PL Action Plan

**Owner:** Kristen (PL lead) · **Team:** Cody, Jasmine · **Sponsor:** Gautam · **Ops:** Joe / Santosh
**Fills tracker tasks:** PL-A (tiered spine target-account universe) + PL-B (recover & expand spine referrals)
**Status:** operating artifact, ready to run this week · **Date:** 2026-07-17

> **Honesty flag on data.** Every account row below is marked **[SEED — replace with real Map My
> Customer export]**. Practice names, cities, historical NP counts, and payer notes are illustrative
> placeholders that show the team exactly what a "done" row looks like. They are **not** confirmed SHP
> accounts. Do not visit, tier, or report on any seed row until it is replaced by a real MMC/NextGen
> record. See §5 for the real data gaps.

> **Reality anchor.** Referral spine is already **above budget (79 vs. ~65)**. This list is a
> **realistic qualified lift** — recover Sean's ~2–3 NP/week, then a tiered-expansion push toward
> **~95–110 qualified spine NPs/month** — NOT a run at 79 → 150. Lead KPI is **qualified spine NPs
> per PL** and **NP per 100 visits**, never raw visits or touches.

> **Guardrails (blocking).** Relationships are earned on **clinical merit, service, and same-week
> access — never payment or inducement** (anti-kickback / Stark). **No PHI** in any referral comm
> without authorization. Closed-loop report-back is **HIPAA-compliant** only. SHP **takes no
> Medicaid** — payer fit is a tiering criterion, not an afterthought.

---

## 1. Tiering rubric — the rule anyone can apply

Tier is a function of three scored dimensions. Score each account, sum, then assign the tier. A
**payer-fit gate** can override the score downward (a Medicaid-dominant practice cannot be Tier 1
no matter its volume, because SHP cannot serve most of those patients).

### Dimension A — Qualified spine-NP potential (0–5)
Blend of demonstrated + estimated yield of **qualified** spine patients (symptomatic + imaging-
appropriate + **accepted insurance** + a real surgical-or-interventional candidate).

| Signal | Points |
|---|---|
| Historical spine NPs to SHP ≥ 3/mo, OR a departed-liaison account that was producing | 5 |
| Historical 1–2/mo, OR high-volume spine feeder type (ortho, pain mgmt, high-volume chiro/PI) with no current relationship | 4 |
| Plausible spine flow but unproven (mid-volume PCP, PT, urgent care) | 2–3 |
| Low spine relevance / low volume | 0–1 |

### Dimension B — Proximity to a hub (0–3)
Referrers send where access is fast. Same-week access is the pitch, so drive time matters.

| Distance to nearest SHP hub w/ spine coverage | Points |
|---|---|
| ≤ 10 min / same city as hub | 3 |
| 10–20 min | 2 |
| 20–30 min | 1 |
| > 30 min (defensive/edge only) | 0 |

### Dimension C — Payer fit (0–3) — **also a gate**
SHP takes **no Medicaid**. Commercial + Medicare mix is the target (patient base is trending
commercial 42%→52%).

| Payer mix | Points | Gate effect |
|---|---|---|
| Predominantly Commercial / Medicare | 3 | eligible for any tier |
| Mixed, meaningful Commercial share | 2 | eligible for any tier |
| High Medicaid share but a workable Commercial/Medicare slice, OR WC/PI (often commercial-equivalent) | 1 | **cap at Tier 2** |
| Predominantly Medicaid | 0 | **cap at Tier 3 or exclude**; route non-covered/uninsured candidates to **Harmony Health Direct Pay** rather than chase referrals |

### Tier assignment from total score (A+B+C, max 11)

| Total | Tier | Meaning | Default cadence |
|---|---|---|---|
| **8–11** | **Tier 1** | Proven or high-probability qualified-spine producers, close to a hub, good payer fit. Defend and deepen. | Every **14 days** (in person) |
| **5–7** | **Tier 2** | Real potential, unproven or moderate. Develop and prove. | Every **21–30 days** |
| **0–4** | **Tier 3** | Long-tail / prospecting / drop-candidates. Validate cheaply. | Every **45–60 days** or touch-only; **cut after 2 validated zero-yield cycles** |

**Decision rules baked in:**
- Payer gate always wins over score (no Medicaid-dominant Tier 1).
- A former Sean account that was producing enters as **Tier 1 by default** (recovery priority) until re-scored on real data.
- Tier 3 accounts that produce **0 qualified spine NPs over 2 cadence cycles** get **dropped** — reallocate that field time to a Tier-1 backlog account (OODA loop, PL-C).

---

## 2. Account table — template + seeded examples

**CRM/sheet columns (copy these headers straight into MMC or the shared sheet):**

`Account/Practice · City · Account Type · Territory · Assigned PL · Tier · Historical spine NPs · 90-day spine NPs · Planned cadence (days) · Payer/eligibility risk · Status`

Account Type ∈ {ortho, chiro, pain mgmt, urgent care, PCP, PT, PM&R, ER, WC-PI attorney}.
Territory ∈ {Livonia, Sterling Heights, Southfield, Troy, Port Huron}.
Assigned PL ∈ {Kristen, Cody, Jasmine}.

> All rows below are **[SEED]**. Replace with the real MMC export (PL-A.1). Seeded so each feeder
> type × hub shows a realistic, complete row — copy the *shape*, not the data.

| Account/Practice | City | Account Type | Territory | Assigned PL | Tier | Hist. spine NPs | 90-day spine NPs | Cadence (days) | Payer/eligibility risk | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| [SEED] Metro West Orthopaedic Group | Livonia | ortho | Livonia | Jasmine | 1 | 9 | — | 14 | Low — commercial/Medicare | Active |
| [SEED] Livonia Family PCP Associates | Livonia | PCP | Livonia | Jasmine | 2 | 2 | — | 30 | Low | Active |
| [SEED] Riverside Physical Therapy | Livonia | PT | Livonia | Jasmine | 3 | 0 | — | 60 | Low | Prospect |
| [SEED] Sterling Spine & Pain Center | Sterling Heights | pain mgmt | Sterling Heights | Cody | 1 | 11 | — | 14 | Low — verify no Medicaid line | Active (defend) |
| [SEED] Lakeside Chiropractic | Sterling Heights | chiro | Sterling Heights | Cody | 1 | 6 | — | 14 | Med — WC/PI mix, screen payer | Active (defend) |
| [SEED] M-59 Urgent Care | Sterling Heights | urgent care | Sterling Heights | Cody | 2 | 1 | — | 21 | Low | Active |
| [SEED] Macomb PM&R Associates | Sterling Heights | PM&R | Sterling Heights | Cody | 2 | 3 | — | 21 | Low | Active |
| [SEED] Northland WC/PI Law (attorney) | Southfield | WC-PI attorney | Southfield | Kristen | 1 | 7 | — | 14 | Low — WC/PI commercial-equiv | Active |
| [SEED] Southfield Pain Institute | Southfield | pain mgmt | Southfield | Kristen | 1 | 5 | — | 14 | Med — confirm Medicaid share | Active (ramp) |
| [SEED] Greenfield PCP Partners | Southfield | PCP | Southfield | Kristen | 2 | 1 | — | 30 | **High — screen Medicaid** | Prospect |
| [SEED] Oakland Ortho Specialists | Troy | ortho | Troy | Kristen | 1 | 8 | — | 14 | Low — commercial-heavy | Active (ramp) |
| [SEED] Troy Spine Chiropractic | Troy | chiro | Troy | Kristen | 2 | 2 | — | 21 | Med — WC/PI mix | Active (ramp) |
| [SEED] Big Beaver Urgent Care | Troy | urgent care | Troy | Kristen | 3 | 0 | — | 60 | Low | Prospect |
| [SEED] Beaumont-area ER referral desk | Troy | ER | Troy | Kristen | 2 | 2 | — | 30 | Low | Prospect |
| [SEED] Port Huron Pain & Spine | Port Huron | pain mgmt | Port Huron | Jasmine | 2 | 3 | — | 30 | Med — confirm payer | Active |
| [SEED] Blue Water PCP Group | Port Huron | PCP | Port Huron | Jasmine | 3 | 0 | — | 60 | Med | Prospect |

**Status vocabulary:** `Active (defend)` · `Active (ramp)` · `Active` · `Prospect` · `Recover-Sean` ·
`Watch` · `Drop-candidate` · `Dropped`.

---

## 3. Territory assignment across the 5 hubs

Assignment principle: **one account = one PL = one hub owner.** No account appears in two books.
Weighting follows the mandate — **defend Sterling Heights** (Corewell/Beaumont pressure) and
**ramp Southfield + Troy** (Oakland County is the under-penetrated unlock).

| Hub | Primary PL | Strategic posture | Weighting |
|---|---|---|---|
| **Sterling Heights** | **Cody** | **Defend** vs. Corewell/Beaumont — hold every producing account, tight 14-day cadence | Heavy |
| **Southfield** | **Kristen** | **Ramp** — Oakland deepening; Kristen models the top-producer method on new accounts | Heavy (growth) |
| **Troy** | **Kristen** | **Ramp** — the Oakland ortho/spine unlock; net-new Tier-1 hunting | Heavy (growth) |
| **Livonia** | **Jasmine** | **Rebalance from ortho toward spine feeders** — hold base, convert coverage to spine | Medium |
| **Port Huron** | **Jasmine** | **Maintain** — defensive edge, lower cadence, prove before investing | Light |

**Overlap to eliminate (PL-A.4 — "zero overlap"):**
- The paid-media audit flagged heavy Livonia + Sterling Heights coverage overlap. Mirror the fix here:
  **any account currently touched by 2+ PLs gets a single named owner by hub** in the recovery pass.
- **Sterling Heights ↔ Troy border** (Macomb/Oakland line): assign strictly by hub proximity (Dimension
  B), not by who visited last.
- Kristen carries ~51% of B2B volume today — this split **intentionally moves her to the two ramp hubs**
  (Southfield, Troy) so her method builds new Tier-1 accounts instead of concentrating risk on existing ones.
- **Rule:** if two PLs both claim an account, it goes to the PL who owns that account's **hub**; the other PL removes it from their book same day.

---

## 4. First-week action plan (Jul 17–24) — owner-assigned, day-by-day

Ties directly to tracker **PL-A.1 → PL-A.3** and **PL-B.1**. The week's outcome: a real (non-seed)
account universe exported, feeder-crosswalked, first-pass tiered, Sean's accounts re-owned and
re-visited, and cadence rules set.

| Day | Owner | Action | KPI / definition of done | Decision rule |
|---|---|---|---|---|
| **Thu 7/17** | **Kristen + Santosh** | Pull the **Map My Customer export** of all current accounts; request the **NextGen spine-NP-by-referrer** cut for the crosswalk (PL-A.1). | Raw account universe in the sheet; NextGen request logged. | If NextGen referrer field is billing-overwritten, flag to Santosh/Joe now — attribution fix (PL-D) is a dependency, don't wait on it to start tiering. |
| **Thu 7/17** | **Kristen** | Reconstruct **Sean's book**: list every account he owned + last-known spine yield (PL-B.1). Mark each `Recover-Sean`, default **Tier 1**. | Sean account list complete; owners reassigned by hub. | Any Sean account with a live contact → **re-visit within 7 days**. |
| **Fri 7/18** | **Kristen + team** | Build the **feeder crosswalk** — bucket every account into the 9 types (ortho, chiro, pain mgmt, urgent care, PCP, PT, PM&R, ER, WC-PI attorney) (PL-A.2). | 100% of accounts typed; untyped = 0. | Untypeable/duplicate accounts → merge or mark `Watch`, don't tier yet. |
| **Fri 7/18** | **Cody** | **Sterling Heights defense sweep**: confirm every producing SH account still owned, no lapses since Sean. | SH producing accounts all `Active (defend)` with a named owner. | Any lapsed SH account → schedule visit next week. |
| **Mon 7/21** | **Kristen, Cody, Jasmine** | **First-pass tiering** using §1 rubric (score A+B+C, apply payer gate) (PL-A.3). | Every non-seed account has a Tier + payer/eligibility risk note. | Missing payer data → default **payer risk = High**, cap at Tier 2 until confirmed. |
| **Mon 7/21** | **Kristen + Joe** | **Territory de-overlap pass**: resolve every 2-owner account to a single hub owner per §3. | Overlap count = 0. | Tie → account goes to hub-proximity owner. |
| **Tue 7/22** | **Cody + Jasmine** | Begin **Sean-recovery + Tier-1 visits**; reserve **same-week access** as the opening pitch; leave the referrer one-pager (deep spine bench, conservative-to-surgical pathway). | First recovery visits logged; qualified-NP tracking (not visit count) started. | Practice asks "how do I refer?" → give the named coordinator + secure path same visit. |
| **Wed 7/23** | **Kristen** | **Set cadence per tier** (14 / 21–30 / 45–60) and stamp `Planned cadence (days)` on every account (PL-A.5 preview). | Cadence populated for 100% of tiered accounts. | Tier 3 gets touch-only until it proves a qualified NP. |
| **Thu 7/24** | **Kristen + Joe** | **Week-1 OODA review**: qualified spine NPs per PL, NP/100 visits, accounts tiered, overlap eliminated, Sean accounts re-visited. | Baseline scorecard populated; PL-A marked from Not Started → In Progress. | Cody's run-rate feeds the **4th-PL trigger** (sustained 15 NP/wk before any hire). |

**Standing rules for the week (and after):**
- **Measure qualified NP yield, not visits.** A visit that doesn't produce a qualified, insured,
  candidate spine patient is not a win. Coach toward Kristen's ~70 NP/100 method — ride-alongs start next week (PL-C).
- **Route surgical candidates to the higher-converting surgeons** (McCarty / Maslak / Varghese) and use
  interventional (Oddo, Lee, Kassa, Singh) as the conservative front door. Routing itself is a
  clinical/ops decision — surface to Katie, don't act unilaterally.
- **Closed-loop report-back** to the referring provider (seen + plan) is the single biggest driver of
  repeat referrals — HIPAA-compliant only, automate as tracking allows.

---

## 5. What must come from the practice (real data gaps to fill)

The list can't be trusted until these replace the seed data. Owners noted; this is the blocker list.

1. **MMC full account export** — every current account with contact, type, last-visit date. → Kristen (PL-A.1)
2. **NextGen spine-NP-by-referring-practice** — the historical + 90-day spine NP counts that fill the
   two volume columns. **Blocked by the referring-physician field being overwritten by billing** and
   **no MMC↔NextGen crosswalk** — this is the attribution dependency (PL-D). Until fixed, historical
   columns are best-estimate. → Santosh + Joe
3. **Sean's account book** — the actual list of accounts and their yields he owned before departure. → Kristen
4. **Payer mix per account** — enough to apply the payer-fit gate (esp. **Medicaid share**, since SHP
   takes none). Where unknown, default to High risk / cap at Tier 2. → practice + intake/Kelly
5. **Same-week access confirmation** — how many spine slots ops can actually reserve for referrals, so
   PLs don't over-promise speed the schedule can't deliver. → Joe + Katie
6. **Named referral coordinator + secure referral path** (line/fax/portal) — the "how to refer"
   answer PLs give on every visit. → Joe
7. **Provider roster confirmations** — confirm A. Munk's listing/role and the higher-converting-surgeon
   routing with the practice before using for referral routing. → practice / Katie

---

### Cross-references
- Strategy: `/home/user/SHP/playbooks/b2b-physician-liaison-strategy.md`
- 90-day plan: `/home/user/SHP/playbooks/spine-90day-plan.md` (§4C referral engine, §4A routing)
- Roster / routing: `/home/user/SHP/brand/provider-roster-by-service-line.md`
- Tracker tasks filled: **PL-A, PL-A.1–.5, PL-B, PL-B.1** in `/home/user/SHP/pm/master-task-list.csv`
