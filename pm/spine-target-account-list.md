# Spine Target-Account List + First-Week PL Action Plan

**Owner:** Kristen (PL lead) · **Team:** Coty, Jasmine · **Sponsor:** Gautam · **Ops:** Joe / Santosh
**Fills tracker tasks:** PL-A (tiered spine target-account universe) + PL-B (recover & expand spine referrals)
**Status:** operating artifact · **Date:** 2026-07-17 · **Updated 2026-07-21 with real referral yield**

> **✅✅ v2 — REAL REFERRAL YIELD NOW WIRED IN (Jul 21).** The Jul 17 proxy tiering below is
> **superseded** by the referral-weighted scored book from the v4 operating report:
> **`pm/spine-target-accounts-SCORED.csv`** — **808 accounts** (Kristen 180 · Jasmine 310 · Coty 318),
> scored 0–100 on actual 2026 attributed patients, tiered (**Tier 1 = 146 proven-spine · Tier 2 = 156
> ortho · Tier 3 = 37 other · Prospect = 469**), **Wave 1 = 90**, with per-account spine/ortho/other
> counts, visit→appt lag, stamped cadence and next action. Companion files:
> `pm/spine-referral-company-outcomes.csv` (the 385-company referral ledger),
> `pm/sean-prospects-DATA.csv`, `pm/pl-route-days.csv` (85 built route days).
> **Read the mined insights + this week's actions in `pm/spine-pl-account-insights.md`.**
> `pm/spine-target-accounts-DATA.csv` (1,975 accounts) remains the wider prospecting universe only.

## 0. Account universe — corrected picture (Jul 21)

- **Proxy tiers (Jul 17: T1 209 · T2 356 · T3 1,410) are retired.** Real evidence tiers: only
  **146 accounts have ≥1 attributed 2026 spine patient** (54 repeat + 92 one-spine); 365 spine
  patients total in the 808 book; **top 10 accounts = 41%** of it.
- **🚨 Correction to the Jul 17 orphan finding: Sean has NOT departed — Kessia did.** Sean Sweeney
  is a current owner (272 accounts, producing since March, 40 routed priorities) — though his last
  logged visit is **Jun 9 (verify)**. **Kessia's** volume ended Mar–May, her owner-email matches
  nothing in MMC, and the ~290 companies she visited Jan–Mar are the real orphan pool (~6 B2B
  spine/mo before wind-down). **PL-B.1 = Kessia-book recovery + Sean coverage check.**
- Ownership snapshot (spine-relevant, Jul 16 MMC): Coty 1,029 · Kristen 562 · Jasmine 486 ·
  Sean 272 · unowned (incl. Kessia-era) — reassign per `pm/spine-pl-account-insights.md` §1.

> The §1 rubric below still governs **payer gating and qualified-yield re-tiering** — payer fit is
> Unknown on all 808 accounts (Kelly is scoring Tier 1 first), and "qualified" still means
> insurance-accepted + imaging-appropriate + pathway-fit, which attributed counts can't prove.

---

> **Note on the seed rows below.** They predate the real export and remain only to illustrate a "done"
> row and the tiering rubric. **Work from the CSV, not the seed rows.** See §5 for remaining data gaps.

> **Reality anchor.** Referral spine is already **above budget (79 vs. ~65)**. This list is a
> **realistic qualified lift** — protect the 60-account repeat-spine base (~46/mo), recover the
> Kessia-era book (~6 spine/mo) and cover Sean's stall, then convert one-spine accounts toward
> **~95–115 qualified spine NPs/month** — NOT a run at 79 → 150 (the per-account math doesn't
> close; see `pm/spine-pl-account-insights.md` §2). Lead KPI is **qualified spine NPs per PL**
> and **NP per 100 visits**, never raw visits or touches.

> **Guardrails (blocking).** Relationships are earned on **clinical merit, service, and same-week
> access — never payment or inducement** (anti-kickback / Stark). **No PHI** in any referral comm
> without authorization. Closed-loop report-back is **HIPAA-compliant** only. **Medicaid is accepted
> at select providers only — verify per provider** (`brand/current-state.md` Payer reality); payer
> fit is a tiering criterion, not an afterthought.

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
Commercial + Medicare is the target mix (patient base trending commercial 42%→52%). **Medicaid is
accepted only at *select* SHP providers (varies) — not universal** (see `brand/current-state.md`
Payer reality), so a Medicaid-dominant practice is a poor spine-referral fit unless a spine provider
is confirmed in-network with that plan. WC/PI and Auto No-Fault are commercial-equivalent and welcome.

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
- A former **Kessia** account that was producing enters as **Tier 1 by default** (recovery priority) until re-scored on real data.
- Tier 3 accounts that produce **0 qualified spine NPs over 2 cadence cycles** get **dropped** — reallocate that field time to a Tier-1 backlog account (OODA loop, PL-C).

---

## 2. Account table — template + seeded examples

**CRM/sheet columns (copy these headers straight into MMC or the shared sheet):**

`Account/Practice · City · Account Type · Territory · Assigned PL · Tier · Historical spine NPs · 90-day spine NPs · Planned cadence (days) · Payer/eligibility risk · Status`

Account Type ∈ {ortho, chiro, pain mgmt, urgent care, PCP, PT, PM&R, ER, WC-PI attorney}.
Territory ∈ {Livonia, Sterling Heights, Southfield, Troy, Port Huron}.
Assigned PL ∈ {Kristen, Coty, Jasmine}.

> All rows below are **[SEED]**. Replace with the real MMC export (PL-A.1). Seeded so each feeder
> type × hub shows a realistic, complete row — copy the *shape*, not the data.

| Account/Practice | City | Account Type | Territory | Assigned PL | Tier | Hist. spine NPs | 90-day spine NPs | Cadence (days) | Payer/eligibility risk | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| [SEED] Metro West Orthopaedic Group | Livonia | ortho | Livonia | Jasmine | 1 | 9 | — | 14 | Low — commercial/Medicare | Active |
| [SEED] Livonia Family PCP Associates | Livonia | PCP | Livonia | Jasmine | 2 | 2 | — | 30 | Low | Active |
| [SEED] Riverside Physical Therapy | Livonia | PT | Livonia | Jasmine | 3 | 0 | — | 60 | Low | Prospect |
| [SEED] Sterling Spine & Pain Center | Sterling Heights | pain mgmt | Sterling Heights | Coty | 1 | 11 | — | 14 | Low — verify no Medicaid line | Active (defend) |
| [SEED] Lakeside Chiropractic | Sterling Heights | chiro | Sterling Heights | Coty | 1 | 6 | — | 14 | Med — WC/PI mix, screen payer | Active (defend) |
| [SEED] M-59 Urgent Care | Sterling Heights | urgent care | Sterling Heights | Coty | 2 | 1 | — | 21 | Low | Active |
| [SEED] Macomb PM&R Associates | Sterling Heights | PM&R | Sterling Heights | Coty | 2 | 3 | — | 21 | Low | Active |
| [SEED] Northland WC/PI Law (attorney) | Southfield | WC-PI attorney | Southfield | Kristen | 1 | 7 | — | 14 | Low — WC/PI commercial-equiv | Active |
| [SEED] Southfield Pain Institute | Southfield | pain mgmt | Southfield | Kristen | 1 | 5 | — | 14 | Med — confirm Medicaid share | Active (ramp) |
| [SEED] Greenfield PCP Partners | Southfield | PCP | Southfield | Kristen | 2 | 1 | — | 30 | **High — screen Medicaid** | Prospect |
| [SEED] Oakland Ortho Specialists | Troy | ortho | Troy | Kristen | 1 | 8 | — | 14 | Low — commercial-heavy | Active (ramp) |
| [SEED] Troy Spine Chiropractic | Troy | chiro | Troy | Kristen | 2 | 2 | — | 21 | Med — WC/PI mix | Active (ramp) |
| [SEED] Big Beaver Urgent Care | Troy | urgent care | Troy | Kristen | 3 | 0 | — | 60 | Low | Prospect |
| [SEED] Beaumont-area ER referral desk | Troy | ER | Troy | Kristen | 2 | 2 | — | 30 | Low | Prospect |
| [SEED] Port Huron Pain & Spine | Port Huron | pain mgmt | Port Huron | Jasmine | 2 | 3 | — | 30 | Med — confirm payer | Active |
| [SEED] Blue Water PCP Group | Port Huron | PCP | Port Huron | Jasmine | 3 | 0 | — | 60 | Med | Prospect |

**Status vocabulary:** `Active (defend)` · `Active (ramp)` · `Active` · `Prospect` · `Recover-Kessia` ·
`Watch` · `Drop-candidate` · `Dropped`. *(The SCORED csv's `Operating Lane` / `Next Action` columns
now carry this role — Protect / Reactivation / Expansion / Cross-Sell.)*

---

## 3. Territory assignment across the 5 hubs

Assignment principle: **one account = one PL = one hub owner.** No account appears in two books.
Weighting follows the mandate — **defend Sterling Heights** (Corewell/Beaumont pressure) and
**ramp Southfield + Troy** (Oakland County is the under-penetrated unlock).

| Hub | Primary PL | Strategic posture | Weighting |
|---|---|---|---|
| **Sterling Heights** | **Coty** | **Defend** vs. Corewell/Beaumont — hold every producing account, tight 14-day cadence | Heavy |
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

> **⚠️ Superseded mid-week (Jul 21):** the export/crosswalk/tiering rows below landed via the v4
> operating report (PL-A.1–A.3 effectively done), and the recovery target is **Kessia's book, not
> Sean's**. Work from the current action table in `pm/spine-pl-account-insights.md` §4 —
> re-protection sweep first, route dates stamped, Sean stall verified. Rows kept for the record.

Ties directly to tracker **PL-A.1 → PL-A.3** and **PL-B.1**. The week's outcome: a real (non-seed)
account universe exported, feeder-crosswalked, first-pass tiered, the departed-book accounts re-owned
and re-visited, and cadence rules set.

| Day | Owner | Action | KPI / definition of done | Decision rule |
|---|---|---|---|---|
| **Thu 7/17** | **Kristen + Santosh** | Pull the **Map My Customer export** of all current accounts; request the **NextGen spine-NP-by-referrer** cut for the crosswalk (PL-A.1). | Raw account universe in the sheet; NextGen request logged. | If NextGen referrer field is billing-overwritten, flag to Santosh/Joe now — attribution fix (PL-D) is a dependency, don't wait on it to start tiering. |
| **Thu 7/17** | **Kristen** | Reconstruct the **departed liaison's book** (**Kessia**, per Jul 21 correction): list every account + last-known spine yield (PL-B.1). Mark each `Recover-Kessia`, default **Tier 1**. | Kessia account list complete; owners reassigned by hub. | Any Kessia account with a live contact → **re-visit within 7 days**. |
| **Fri 7/18** | **Kristen + team** | Build the **feeder crosswalk** — bucket every account into the 9 types (ortho, chiro, pain mgmt, urgent care, PCP, PT, PM&R, ER, WC-PI attorney) (PL-A.2). | 100% of accounts typed; untyped = 0. | Untypeable/duplicate accounts → merge or mark `Watch`, don't tier yet. |
| **Fri 7/18** | **Coty** | **Producing-account defense sweep**: confirm every producing account still owned, no lapses since the Kessia wind-down / Sean stall. | Producing accounts all `Active (defend)` with a named owner. | Any lapsed producing account → schedule visit next week. |
| **Mon 7/21** | **Kristen, Coty, Jasmine** | **First-pass tiering** using §1 rubric (score A+B+C, apply payer gate) (PL-A.3). | Every non-seed account has a Tier + payer/eligibility risk note. | Missing payer data → default **payer risk = High**, cap at Tier 2 until confirmed. |
| **Mon 7/21** | **Kristen + Joe** | **Territory de-overlap pass**: resolve every 2-owner account to a single hub owner per §3. | Overlap count = 0. | Tie → account goes to hub-proximity owner. |
| **Tue 7/22** | **Coty + Jasmine** | Begin **Kessia-recovery + Tier-1 protect visits**; reserve **same-week access** as the opening pitch; leave the referrer one-pager (deep spine bench, conservative-to-surgical pathway). | First recovery visits logged; qualified-NP tracking (not visit count) started. | Practice asks "how do I refer?" → give the named coordinator + secure path same visit. |
| **Wed 7/23** | **Kristen** | **Set cadence per tier** (14 / 21–30 / 45–60) and stamp `Planned cadence (days)` on every account (PL-A.5 preview). | Cadence populated for 100% of tiered accounts. | Tier 3 gets touch-only until it proves a qualified NP. |
| **Thu 7/24** | **Kristen + Joe** | **Week-1 OODA review**: qualified spine NPs per PL, NP/100 visits, accounts tiered, overlap eliminated, Kessia-era accounts re-visited. | Baseline scorecard populated; PL-A marked from Not Started → In Progress. | Coty's run-rate feeds the **4th-PL trigger** (sustained 15 NP/wk before any hire). |

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
*(Status refreshed 2026-07-21 after the v4 operating report.)*

1. ~~**MMC full account export**~~ **✅ DONE (Jul 21)** — 3,529 companies + activity in the v4 report;
   scored book in `pm/spine-target-accounts-SCORED.csv`. → Kristen (PL-A.1)
2. **NextGen spine-NP-by-referring-practice** — **~82.5% now solved** via the report's deterministic
   referral→MMC match (`pm/spine-referral-company-outcomes.csv`); **278 rows / 31 spine patients
   still unresolved** (top-15 disambiguation list in `pm/spine-pl-account-insights.md` §1.9); the
   referring-physician overwrite fix is still open. → Santosh + Joe
3. ~~**Sean's account book**~~ **✅ CORRECTED + DONE (Jul 21)** — Sean is active
   (`pm/sean-prospects-DATA.csv`); the departed book to recover is **Kessia's** (~290 visited
   companies, no current owner). → Kristen
4. **Payer mix per account** — **still the #1 gap: Payer Fit = Unknown on all 808.** Kelly scores
   the 146 Tier-1 accounts first (esp. **Medicaid share** — select-provider acceptance only — and
   HMO referral-required plans). Where unknown, default High risk / cap at Tier 2. → intake/Kelly
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
