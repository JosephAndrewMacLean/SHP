# Spine B2B Target-Account Insights — What the Real Referral Data Says

**Date:** 2026-07-21 · **Analyst:** in-house marketing team (Joe's workspace)
**Source:** `B2C_B2B_Spine_Growth_Operating_Report_JanJul_2026_4.xlsx` (v4, received Jul 21) —
B2B appointment records through **Jul 10, 2026**; MMC CRM activity through **Jul 16, 2026**.
**Fills tracker tasks:** PL-A.2/.3 (crosswalk + tiering — now data-backed), PL-B.1 (recovery
targeting), ATTR-B.3 (B2B split evidence), SP-B.2 (scorecard inputs).

**Working data wired into this repo (supersedes the Jul 17 proxy tiering):**

| File | What it is |
|---|---|
| `pm/spine-target-accounts-SCORED.csv` | The **808-account referral-weighted 2× book** (Kristen 180 · Jasmine 310 · Coty 318), scored 0–100, tiered, waved, with per-account 2026 spine/ortho/other patient counts, lag, cadence, next action |
| `pm/spine-referral-company-outcomes.csv` | The **referral ledger**: all 385 MMC companies deterministically matched to 2026 B2B patients (1,287 patients, 391 spine) |
| `pm/sean-prospects-DATA.csv` | Sean's 253-account overlay: 40 priority-routed, 102 route pool, 107 hold, 4 ownership reviews |
| `pm/pl-route-days.csv` | All **85 built route days** (10 stops max): 18 Kristen · 31 Jasmine · 32 Coty · 4 Sean |
| `pm/spine-pl-weekly-visit-plan.md` + `pm/pl-weekly-visit-schedule.csv` | **The week-by-week field calendar (added Jul 21):** Jul 22 → Oct 2, 987 scheduled stops — protect-first, prospects mixed into every day, per-PL money lists |

> **Caveats that ride with every number (from the report's own methodology):** patient counts are
> distinct attributed PER numbers, **not confirmed kept visits**; 82.5% of referral rows matched
> deterministically to one MMC company; visit→appointment lag is timing context, **not proven
> causation**; B2C is inferred (total − B2B) pending Analytics validation. Treat everything below
> as operational best-estimate, good enough to direct field time — not as validated finance data.

---

## 0. Two corrections to our own docs (important)

1. **Sean did not depart — Kessia did.** Our Jul 17 docs said "Sean departed, 251 accounts
   orphaned." The data: **Sean Sweeney (SS)** is a current MMC owner (272 companies), started
   producing in **March**, has 21 spine YTD and a routed 40-account priority overlay. **Kessia (KG)**
   is the real loss: volume wound down Mar→May to zero, her MMC owner-email no longer matches any
   account, and the ~290 companies she visited Jan–Mar are the true orphan pool. Her book was worth
   **~6 B2B spine/month** (5·6·7 in Jan–Mar) before wind-down — not the "~2–3 spine NP/week" our
   docs assumed. All repo docs corrected today.
2. **But Sean has a real problem anyway:** his **last completed MMC visit is June 9** — five-plus
   weeks of zero logged field activity (and 33 unlinked visit records, the team's worst hygiene).
   His 17 referral-positive accounts and 40-account route are uncovered until someone confirms
   whether that's a logging gap or a genuine stall. → **Kristen: verify with Sean this week.**

---

## 1. The ten insights that should change what the team does

### 1) The engine is far more concentrated than the plan prices in
- **Kristen's book = 245 of 391 matched spine patients (63%).** Jasmine 61, Coty 59, Sean 26.
- **10 accounts = 41%** of the 808-book's spine volume; **Mike Morse Law Firm alone = 75 spine
  (~1 in 5 of all matched spine)**.
- Only **163 of 3,529 MMC companies** produced even one spine patient in 2026; just **60 accounts
  (54 core + 6 Sean) are repeat-spine referrers** — and they generate ~46 spine/month (288 over
  6.2 months), i.e. more
  than half of the entire B2B spine line.

**So what:** one liaison, one law firm, and sixty practices *are* the B2B spine business. Any plan
that starts with expansion before locking these down is risking the base it's building on.
**Do:** treat the repeat-spine 60 as a named "franchise list" with explicit coverage rules
(no account goes 21+ days unvisited; a named backup PL per account when the owner is out). → Kristen, this week.

### 2) Protect emergency: 32 of the 54 repeat-spine referrers had zero visits in the last 4 weeks
- Those 32 unvisited accounts carry **120 of the 273 repeat-band spine patients** (44%).
- Worst offenders: **Hesselberg Chiropractic** (23 spine — #2 account overall — last visited
  **Apr 27**), **Michigan Auto Law** (10 spine, Apr 29), **Applebaum & Stone** (5, **Mar 16**),
  **Vanstone Injury Law** (5, **Feb 27**).
- Separately, **27 producers (≥2 spine) have sent no spine patient since mid-May** (~69 patients'
  worth of run-rate at risk) — overlapping but not identical to the unvisited list.

**So what:** the cheapest spine patients in Q3 are the ones already flowing that nobody is defending
— this is where Corewell/Beaumont-style competitors take share silently.
**Do:** first 10 field days = **re-protection sweep of the 32 + the quiet 27** (thank-you, service
check, same-week access reminder) before any cold Wave-2 prospecting. It's already flagged
`Protect` in the CSV's Next Action column. → all PLs, starting now.

### 3) The attorney / auto-no-fault channel is a third of spine — concentrated, under-visited, and compliance-sensitive
- **14 attorney accounts → 114 spine patients (31% of book spine)**; 8.1 spine/account vs 0.37 for
  PCPs. All 14 are **Kristen's**, clustered in **Southfield**; only 3 of 14 had a visit in the
  last 4 weeks — the unvisited include Michigan Auto Law (10 spine) and three firms at 5 spine each
  (Ross, Applebaum & Stone, Vanstone).
- Morse (75) + Michigan Auto Law (10) = 74% of attorney spine. The next 12 firms produced 0–5 each
  — the pattern replicates but is barely worked.

**So what:** WC/auto-no-fault is commercial-equivalent payer-wise (no referral, no copay — see
`brand/current-state.md` payer reality) and clearly the highest-yield feeder type per account. It's
also the channel where relationship missteps carry legal risk.
**Do:** (a) build a **second-attorney-tier development plan** (the 12 small firms + lookalikes) with
a service-based value prop only — same-week access for auto/WC evaluations, clean records
turnaround, clear billing/lien handling; (b) **route Morse like a key account** (named coordinator,
monthly service review), because a single relationship worth ~12 spine/month is a single point of
failure; (c) **compliance guardrail:** no payments, gifts, or referral inducements in either
direction (AKS/Stark hygiene even where payers are non-federal); any attorney-facing collateral goes
through legal/compliance review before use. → Kristen + Joe; collateral = draft pending human review.

### 4) Field capacity is falling exactly when the plan demands it double
Monthly team practice visit-days: **Jan 608 → Feb 808 → Mar 863 → Apr 738 → May 772 → Jun 668 →
Jul 292 through Jul 16 (~127/week pace, vs ~155/week in June and ~200 at peak).**
Kessia's ~200/month disappeared in March; Sean's ~160/month went to zero after June 9; Kristen's
July pace is roughly half her normal.

**So what:** with a **median visit→first-appointment lag of 31 days** (54% of patients appear ≤30
days after the last visit, 83% ≤60), **June–July's activity dip is already baked in as an
August B2B spine dip** — precisely when the 30-day experiment gets judged. The "2× field time"
mandate is really a **~+90% recovery just to get back to March**, before any expansion effect.
**Do:** report weekly visit-days per PL on the spine scorecard now (leading indicator); staff the
Sean gap (insight 0.2); protect Kristen's field days from meetings. → Joe (scorecard), Kristen (coverage).

### 5) The built-in cadence plan exceeds total team capacity — sequence it or it silently fails
The 808-account book's stamped cadences (14d × 146 Tier 1, 21d × 156 Tier 2, 30d × 37 Tier 3,
45d × 469 prospects) require **~207 practice visits/week — more than the whole team's June
actual (~155/week)**, and the 808 is only a slice of the 3,529-account universe they actually touch.

**So what:** run as written, the plan is arithmetically impossible; what will actually get dropped
is unmanaged.
**Do:** explicit sequencing — **Wave 1 (90 accounts @14d ≈ 45 visits/week) + the protect/quiet
lists are non-negotiable; Tier 2 ortho cross-sell at 21d only after Wave 1 is on cadence; the 469
prospects are route-fill, not commitments.** Also: **the 85 route days have zero planned dates** —
they're built but unscheduled. Stamp dates on Wave-1-heavy days first. → Kristen + each PL, this week.

### 6) Referrals follow visits — almost never the other way
Only **6 of 1,287 matched patients** arrived from a company with no prior MMC visit. And 73.5% of
YTD visit effort (3,488 of 4,748 visit-days) went to accounts that produced **zero** matched B2B
patients in 2026 — including **338 visit-days (7%) into pediatric-labeled accounts** with ~0 spine
relevance.

**So what:** field presence is genuinely load-bearing (good news: the lever works), but most of it
is pointed at non-producing books — largely a legacy-territory artifact (e.g., Kristen's MMC book is
labeled 287 PCP + **112 pediatrics**). Rebalancing existing effort *is* the "2× spine field time"
— no headcount required. (Caveat: some non-producing visits build other service lines and future
accounts; the target is rebalance, not zero.)
**Do:** shift ~20% of visit-days from never-produced, low-fit labels (pediatrics first) into the
Tier 1/2 spine book; make "visit-days into spine-book accounts / total" a scorecard ratio. → Kristen; Joe tracks.

### 7) Wave 1's even 30/30/30 split misallocates against the evidence
Kristen's 30 Wave-1 slots are all repeat-spine — but she owns **80 proven-spine accounts**, so
**50 proven accounts (53 spine patients' worth) sit in Wave 2**, while Jasmine/Coty spend 39 of
their 60 Wave-1 slots on one-spine accounts. Kristen also has the **fewest route days (18 vs
31/32)** and the most scattered geography (median 15.5 straight-line miles/day vs Jasmine 6.2).

**So what:** the strongest liaison is structurally under-covered on her own proven book.
**Do:** either extend Kristen's Wave 1 to her full repeat+one-spine set, or hand her Wave-2 proven
accounts that sit near Jasmine/Coty route clusters to those PLs **with explicit owner transfer**
(one account = one owner still holds). → Kristen decision, Joe referees overlap.

### 8) The territory map should follow the referral map — the 5-hub model misses 57% of spine value
Only **178 of 808 accounts (156 of 365 spine, 43%)** sit in the five named hub territories.
**Southfield is the #1 spine territory (106 — attorney cluster)**; then Livonia 35, **Farmington
Hills 25, Ypsilanti 23** (= Hesselberg), Canton 13, Warren 11 — four of the top six are outside
the hub model, and Sterling Heights (a "defend heavy" hub in our Jul 17 plan) holds just 19
accounts in the evidence-weighted book.

**So what:** our Jul 17 hub-weighting (defend Sterling Heights, ramp Troy) was built on hub
proximity, not on where referrals actually originate. The routes in this report already follow the
evidence — adopt that as the territory truth.
**Do:** assign territory ownership from the route clusters (`pm/pl-route-days.csv` Primary Area),
not from hub lists; fix MMC data hygiene while at it (case-duplicate territories like NOVI/Novi,
CANTON/Canton; configured visit frequency exists on only ~64 of 2,349 owned accounts — the cadence
field the plan depends on is effectively unused in the CRM). → Kristen + Santosh.

### 9) Attribution recovery is a one-week task worth ~visible credit for 60–80 patients
278 referral rows (17.5%) remain unresolved; **31 distinct spine patients** are unmatched. The top
of the list is a handful of provider-name disambiguations: **Kevin Green NP (19 patients,
ambiguous across MMC companies), Maan Askar MD (10), generic "Urgent Care" (8), Clara Kamath MD
(7), Eliezer Gomez MD (6)** — the full audit trail is in the `Referral Source Match` tab.

**So what:** this is the cheap end of ATTR-B (MMC↔NextGen crosswalk): resolving ~15 source groups
recovers most of the missing credit, sharpens per-PL fairness, and hardens the scorecard's B2B line.
**Do:** Santosh resolves the top 15 ambiguous/unmatched sources to a single MMC company (or splits
by location) — one week, alongside the referring-physician field-overwrite fix already tracked. → Santosh.

### 10) Payer fit is still Unknown on all 808 accounts — the one gate our rubric requires that the data can't fill
The report's own follow-up list agrees: payer mix per account remains unpopulated, so the
Jul 17 payer gate (Medicaid-dominant caps, HMO-referral flags) is currently theoretical.

**So what:** Wave-1 pitches promise same-week access; for BCN/HAP/McLaren/Priority **HMO** patients
that promise is only real *with* a PCP referral, and Medicaid is provider-specific (see corrected
payer reality). Overpromising to the wrong panel burns exactly the trust the visit is buying.
**Do:** Kelly's intake team scores payer mix for the **146 Tier-1 accounts only** (a week of
scheduling-data lookups, not a research project); stamp `Payer Fit` in the SCORED csv; PLs carry
the HMO-referral talk track. → Kelly + Kristen; script already in `pm/spine-intake-qualification-script.md`.

---

## 2. What the data says about 79 → 150 B2B spine/month

The honest ladder, using observed per-account rates (repeat-spine ≈ 0.81 spine/mo; one-spine ≈ 0.16):

| Move | Mechanism | Realistic 60–90 day yield |
|---|---|---|
| Protect the base | hold the current **~79/mo** run-rate; its fragile core is the 60-account repeat band (**~46/mo**), currently leaking via insight 2 | **79/mo held** (unprotected, expect −5 to −10) |
| Reactivate the quiet 27 | service-recovery visits on producers silent since mid-May (~11/mo historical run-rate, partly already out of the June number) | **+4–8/mo net** |
| Convert one-spine → repeat | 92 accounts; every 15 that reach repeat-average ≈ +10/mo | **+15–20/mo** (30 conversions is aggressive-but-possible) |
| Cover Sean/Kessia books | 40 routed Sean priorities + Kessia orphan re-ownership | **+4–6/mo** |
| Attorney tier-2 development | 12 small firms + lookalikes, service-based | **+3–6/mo** |
| 469 cold prospects | at one-spine rates, 100 worked ≈ +8/mo *after* the 31-day lag | **+3–8/mo by Oct** |
| Attribution recovery | credit, not new patients — but closes ~7/mo of phantom gap | (reporting) |

**Sum: 79 held + 29–48 incremental ≈ ~95–115/month by October** (net of slippage) is the
defensible range — consistent with the position already
in `playbooks/spine-90day-plan.md` (§ realistic referral lift) and roughly 2/3 of the 150 goal.
**150 would require the entire one-spine cohort to convert AND ~200+ cold accounts to produce at
historical rates inside 8 weeks — the math doesn't close.** Recommend presenting 95–115 as the
committed range with 150 as stretch, and reiterating that June's total-spine gap is mostly a
**B2C hole (−71 vs budget)** per `brand/current-state.md` — referrals were already +14 over plan.

**Timing expectation to set at the weekly review:** with a 31-day median lag, weeks 1–2 of the test
show *activity* movement only; patient movement reads in weeks 3–6. Do not re-plan at day 14 on a
flat patient line — and expect an August soft patch from the June–July activity dip regardless
(insight 4). Judge the test on **September**, not August.

## 3. Scorecard wiring (so the weekly review reads the right signals)

For `Weekly Spine Scorecard` (now in the workbook, still unfilled):
- **Active Spine Accounts** = companies with ≥1 spine patient in trailing 60 days (from
  `spine-referral-company-outcomes.csv` refresh; baseline at Jul 10 = **69**).
- **Leading:** visit-days/week per PL (insight 4) · Wave-1 on-cadence % · protect-list lapses
  (repeat-spine accounts >21 days unvisited — target 0) · % visit-days into spine book (insight 6).
- **Lagging:** B2B spine NPs (weekly, with the 31-day lag annotated) · NP per 100 practice
  visit-days by PL (2026 YTD: Kristen 67 · Jasmine 30 · Coty 18 · Sean 14 — the coaching gap
  PL-C exists to close).
- **Integrity:** row match-rate (82.5% baseline, target >90% after Santosh's pass) · unresolved
  source count (278 baseline).

## 4. This week's owner-assigned actions (rolled up)

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Re-protection sweep: 32 unvisited repeat-spine + 27 quiet producers (Next Action column pre-filled) | Kristen, Jasmine, Coty | start immediately |
| 2 | Verify Sean's June-9 activity stall (logging vs. real); cover his 40 routed priorities either way; resolve the 4 cross-owner reviews | Kristen | Jul 24 |
| 3 | Stamp planned dates on all 85 route days per the weekly calendar (`pm/spine-pl-weekly-visit-plan.md`) | each PL | Jul 24 |
| 4 | Kessia orphan pass: re-own her ~290 visited companies (the real PL-B.1) | Kristen | Jul 28 |
| 5 | Resolve top-15 unresolved referral sources in MMC | Santosh | Jul 28 |
| 6 | Payer-fit scoring for the 146 Tier-1 accounts | Kelly | Jul 31 |
| 7 | Attorney channel: Morse key-account plan + tier-2 firm development, compliance-reviewed collateral only | Kristen + Joe | Jul 31 |
| 8 | Scorecard live with §3 fields; present 95–115 vs 150 framing + August-lag expectation to Gautam | Joe | Fri Jul 25 review |
| 9 | Rebalance ~20% of visit-days out of pediatric/never-produced labels into Tier 1/2 | Kristen | ongoing, report Aug 1 |
| 10 | Verify-before-route pass on the 69 flagged accounts before anyone drives to them | each PL | rolling |

---

### Cross-references
- Working list + rubric context: `pm/spine-target-account-list.md` (updated today to point here)
- Strategy: `playbooks/b2b-physician-liaison-strategy.md` · 90-day plan: `playbooks/spine-90day-plan.md`
- Payer truth: `brand/current-state.md` §Payer reality · Intake script: `pm/spine-intake-qualification-script.md`
- Tracker: `pm/master-task-list.csv` (statuses updated 2026-07-21)
