# Marketing Meeting Agenda — Wednesday, July 22, 2026

**Chair:** Joe · **Timebox:** 60 min · **Rhythm slot:** Wednesday check-in (unblock / re-route /
promote Quick Wins per `pm/README.md`)
**Required:** Joe · Kristen (B2B/PL) · Kelly (phone/patient access) · Randall (SEO/B2C) · Santosh (analytics)
**First 15 min only (optional):** Katie (ops — triage sign-off + routing dependency) · Paul is covered
by the send-ready memo (D1), no need to attend.
**Scribe:** decisions → *Decisions & Blockers* tab; new tasks → *Master Tasks*; scorecard gets its
first fill **Friday 7/24**.

> **Framing for the hour.** Everything on this agenda hangs off the three capture pathways:
> **B2C** (consumer/organic demand) and **B2B** (physician-liaison referrals) create spine demand,
> and the **PHONE** (call center) converts it — qualify, route, book, capture source. Sources:
> this morning's verified tracker re-run (`audits/cardinal-recommendation-tracker.md`, 2026-07-22)
> and yesterday's six leadership meetings (Otter, 7/21). Where a 7/21 verbal number conflicts with
> a repo number, it's flagged for reconciliation — don't silently pick one.

---

## Pre-reads (10 min, before the meeting)

1. `audits/cardinal-recommendation-tracker.md` **§1 Headline status only** — what the data said this morning.
2. `pm/paul-action-update-2026-07-22.md` — send-ready dev memo (decision D1).
3. `pm/ads-owner-questions-2026-07-22.md` — send-ready Blue Ox memo (decision D2).
4. `pm/spine-target-account-list.md` §0 — the real 1,975-account universe + orphaned-accounts finding.
5. `pm/spine-intake-qualification-script.md` header — v1.0 status: **pending clinical sign-off**.
6. New attendees: `playbooks/master-game-plan.md` for the full system.

---

## 0 · The number (5 min) — Joe

- **Spine is ~46–48/week vs. this week's ramp step of 51** → 65 floor by **Aug 30 (Gate 1)** →
  72/week by **Sept 30 (Gate 2)**. June actual: **248 spine NPs = 169 B2C + 79 B2B**;
  B2C ran **−71 vs. budget**, B2B ran **+14 over**. The hole is consumer demand, not referrals.
- From yesterday's Q2 review: spine finished **~70% of Q2 goals** (May was the worst miss), ortho
  is over-delivering and carries the shortfall (hold 130–140/wk), and **20 ASC staff were exited in
  June** — Sept 30 is a hard line, not a stretch goal.
- **The Weekly Spine Scorecard is still unfilled.** First row goes in **Friday 7/24** (Santosh + Joe).

## 1 · What changed since Monday (10 min) — Joe + Santosh

Measurement went from assumed to verified this week; three findings change today's priorities:

1. **The measurement stack is live.** GSC (validated against Cardinal's own audit numbers), Bing
   Webmaster (486 days history), GA4 + Ads campaign spend, PageSpeed API. Still pending: GBP
   (Google approval pipeline) and **Liine MCP — blocked on someone with a Liine login** (§5).
2. **CWV verdict (PSI field data, run 7/22): the speed regression is beaten — LCP 3.5s → ~1.4s —
   but CLS 0.11–0.12 fails every page** (pass line 0.10). One template fix (203 images missing
   width/height) stands between us and "Good" status + ranking recovery. This is the #1 item in
   the Paul memo.
3. **🚨 New finding: Cloudflare is blocking the AI crawlers our AIO/GEO strategy targets**
   (GPTBot, ClaudeBot, Google-Extended, CCBot) and bot-challenges `/llms.txt`. Claude can't index
   the site at all; Gemini grounding is cut. Needs a policy decision today (D3).
4. Quiet wins: staging site locked down same-day (✅ verified HTTP 401), missing meta
   descriptions 55 → 0, llms.txt live, Semrush site health 75/100.
5. **Organic is still bleeding while we fix the plumbing:** sessions Mar 6,163 → Jul ~2,750
   run-rate; avg position 10.9 → 13.3; the carpal tunnel page fell #1 → ~17. Expect the recovery
   case to be argued from GSC once CLS ships — not before.

## 2 · Pathway 1: B2C — consumer/organic demand (10 min) — Randall + Joe

*The −71 June hole lives here. Pathway number to watch: organic sessions/wk + spine-hub organic
arrivals (baseline: only **52 of the spine hub's 2,803 sessions/90d arrive from organic** — ~4/wk).*

- **Cadence check:** 80% of SEO time on spine — 2 pages last week, **3 due this week**. Status of
  the 5 condition hubs (stenosis, herniated disc, sciatica, DDD, spondylolisthesis). New evidence
  the hubs matter: **the same failure pattern shows on Bing** (spondylolisthesis: 174 impressions,
  0 clicks) — one content fix now pays on Google *and* Bing/Copilot.
- **New from 7/21 (Mitch partnership):** integrated spine web content + **procedure
  differentiation pages — endoscopic spine surgery, SI fusion, the bone-bag/T-Lift procedure** —
  plus refreshed spine landing pages, conditions, testimonials, patient-story videos.
  ⚠️ Blocked until **Paul grants Randall access to the Synergy Content settings** (in the memo).
- **Spine differentiation messaging** (Quick Win, unshipped): the deep-bench story — 5 spine
  surgeons incl. a neurosurgeon + 4 interventional-pain physicians, conservative-to-surgical under
  one roof. Feeds pages, paid LPs, and the PL one-pager. Who ships it this week?
- **Production window is tight:** photo/video resource is remote Thursday and on vacation the
  next two weeks — **this week + the week of Aug 10 are the only windows**. Kyle + the new PA
  (starts Aug 3) headshots target **Mon Aug 10, 10–11am**. Decide today what gets scripted/shot
  in the Aug 10 window (patient-story videos? differentiation b-roll?) so briefs are ready.
- Site blockers riding on the Paul memo: CLS fix, AI-crawler unblock, **missing
  surgical/non-surgical conditions in the website menu** (flagged 7/21 — add to his punch list).
- Compliance gate reminder: all spine condition/procedure content is **draft pending physician
  review** (E-E-A-T/YMYL) — build the review step into the Mitch workflow from page one.

## 3 · Pathway 2: B2B — physician-liaison referrals (10 min) — Kristen

*Referrals are already above budget — this pathway's job is a realistic, qualified lift.
Pathway numbers to watch: qualified spine NPs/wk from referrals · NP per 100 visits · accounts
touched/wk vs. the 150 goal.*

- **Target restated in yesterday's meetings: 79 → 110 spine referrals/month by October** — the
  top of the playbook's 95–110 band, via reactivating lapsed accounts, converting one-time
  referrers, and high-potential focus. Lock it as the official number today (D4).
- **Account-universe reconciliation (must resolve before the team works the list next week):**
  the repo CSV has **1,975 spine-relevant accounts (T1 = 209, T2 = 356)**; yesterday's meetings
  worked from a **~848-account spine-adjacent set** to be scrubbed and split into
  **three equal-distribution cohorts**. Kristen + Joel scrub is the deciding step — today we
  confirm which universe is the working list and when the scrub lands.
- **Fastest win — the orphaned accounts:** **Sean's 251 + 139 unowned = ~390 spine-feeder
  accounts have no active liaison.** Reassignment needs zero prospecting. Status of re-ownership?
- **Weekly operating process (from 7/21):** ~150 account touches/week, tiering by referral
  evidence, MMC route planner; Joe automating MMC → tracking-sheet ingestion (→ dashboard →
  Orthoplex later). Kristen trains the team on voice notes + clean data entry.
- Logistics: Thursday Teams intro with Kristen is on — confirm time.
- Guardrail: relationships on clinical merit and service only — **no inducements**
  (anti-kickback / Stark); KPI is qualified NPs and NP/100 visits, never raw touches.

## 4 · Pathway 3: PHONE — call-center capture & conversion (10 min) — Kelly (+ Katie, first 15)

*Every B2C and B2B lead lands here; it's the cheapest lever on the spine number. Pathway numbers
to watch: source-capture % (→100) · qualified-booking rate · self-reschedulers recovered/wk.*

- **Intake qualification + routing script v1.0 is drafted and blocked on clinical sign-off.**
  Yesterday Katie + Mitch + Kelly were tasked with defining **simple, clinically safe triage
  questions, reusing the existing 2023/2024 workflows** — that IS the sign-off path. Set the date
  today (D5; recommend Fri 7/24 so the script runs next week).
- **From the Q2 review: update call-center + scheduling scripts to the correct spine-first
  workflow** — accurate imaging instructions and referral routing. Fold into the same script
  release, one change management push, not two.
- **Insurance pre-screen + mandatory "how did you hear":** source is captured on only 60–70% of
  calls, and a liaison still burns 6–8 hrs/week listening to calls to reconstruct it. Required
  field + script = the free attribution fix.
- **Self-reschedule recovery queue** (166 canceled/no-show patients later self-rebooked online —
  phone-friction signal): stand up the daily worklist (Quick Win candidate, D6).
- Access SLAs: answer <30s, abandonment <5%, callback <1 business hr; protect same-week spine
  slots — and never promise speed the schedule can't deliver (top sentiment risk).
- Sequencing reminder: the **AI call-center rollout comes after** script + attribution
  foundations are in — automate a good process, not a broken one.

## 5 · Cross-pathway plumbing: attribution & the conversion-signal loop (5 min) — Santosh + Joe

- **🚨 Single-focus directive from 7/21: the Zocdoc ↔ Liine ↔ Google Ads conversion-signal loop
  is broken and must be stabilized before Aug 15** (Zocdoc's own fix ETA: end of August — keep
  pressing). **~$240k/30d of paid spend is currently optimizing on a broken signal.** Reaffirm:
  **no paid-bidding or optimization changes until the loop is stable** (B2C CPA already blew up
  $200 → $2,000 once this year).
- **Liine truth gap:** booked-patient truth lives in Liine; the official Liine MCP guide sits
  behind a customer login — need one person with Liine credentials to copy the setup page into
  the workspace. Owner + date today.
- MMC ↔ NextGen crosswalk status (per-account spine-NP yield is the missing tiering input).
- GBP access: two Google API enablements + the access form are the remaining steps (~15 min +
  Google's approval clock). Data hygiene while we wait: fix the split GBP UTM casing and the
  1,310 "(not set)" sessions.
- Santosh: macro systems-ecosystem diagram lands at next week's EMT meeting (7/21 action).

## 6 · Decisions to make today (8 min) — Joe facilitates

| # | Decision | Recommendation | Owner |
|---|---|---|---|
| **D1** | Send the **Paul memo** (CLS fix #1, Cloudflare AI-crawler settings + Apr 25–May 3 audit-log pull, punch list + menu bug) | Approve + send **today** | Joe |
| **D2** | Send the **Blue Ox memo** (Shaun/Jake: $125→$5 revaluation, secondary conversions, Liine OB status, GEO consolidation, Troy/Southfield, PMax) | Approve + send **today** | Joe |
| **D3** | **AI-crawler policy:** unblock retrieval bots (GPTBot, ClaudeBot, Google-Extended) + WAF skip for `/llms.txt` | Unblock retrieval now; AI-*training* block stays a deliberate leadership choice, not a Cloudflare default | Joe → leadership if contested |
| **D4** | **B2B operating baseline:** lock **110/month by October**; confirm working account universe (1,975 CSV vs ~848 scrubbed set), 3-cohort split, 150 touches/wk | Lock 110; universe = whatever survives the Kristen + Joel scrub, due before next week's fieldwork | Kristen |
| **D5** | **Clinical sign-off date** for the intake triage script (Katie + Mitch + Kelly, reusing 2023/24 workflows) | **Fri 7/24**, script live in the phone room next week | Katie |
| **D6** | **Promote 2 Quick Wins to Master Tasks** (Wednesday rhythm) | ① 166 self-reschedulers daily re-book queue (Kelly) · ② Troy Maps/GBP + "Oakland MRI" misdirect fix (Paul — riding the memo) | Joe |

**Carry-overs (do not re-litigate, just status):** 317 vs 321 spine target — Santosh reconciles ·
Salar surgical-candidate routing — **clinical/ops call (Katie + leadership), tracked as a
dependency, not a marketing decision** · 4th PL hire — gated on Cody sustaining 15 NP/wk.

## 7 · Assignments recap (owner · due)

| Owner | Item | Due |
|---|---|---|
| Joe | Three spine-workflow phase timelines (chart-review/coaching · Orthoplex/CCM+ integration · insurance/template notes) — **was due EOD 7/21, confirm sent** | today |
| Joe | Zocdoc/Liine/Ads signal loop — single focus; stabilization | Aug 15 hard stop |
| Joe | Send D1 + D2 memos; MMC-ingestion automation v1 | today / this week |
| Kristen | Scrub account list with Joel → 3 cohorts, equal distribution; team trained | before next week |
| Kristen | Reassign the ~390 orphaned accounts (Sean's 251 + 139 unowned) | this week |
| Kelly | Triage script to sign-off; source field required; recovery queue live | Fri 7/24 / next week |
| Randall | 3 spine pages this week; differentiation messaging draft; Mitch procedure-page outlines (once access granted) | Fri 7/24 |
| Santosh | Scorecard first fill (with Joe); 317-vs-321 reconcile; ecosystem diagram for EMT | Fri 7/24 / next week |
| Katie | Triage-question session with Mitch + Kelly | by Fri 7/24 |
| (via memo) Paul | CLS template fix · Cloudflare AI-bot settings + audit log · Randall content access · menu conditions bug | this week |
| Anna | Rebuild presentation final (Sept 1 go-live) — visibility for marketing dependencies | Aug 1 |

## 8 · Parking lot + next touchpoints (2 min)

- **Parked (revisit after Gate 1, Aug 30):** sports-division concept · pre-op/post-op Friday
  clinics (ops re-evaluates in Sept) · AI call-center rollout timing · local-grid + AIO-citation
  tool decisions.
- **Ops dependencies we track but don't own:** surgical conversion (3 of 4 spine surgeons below
  ratio; physician practice-pattern coaching underway per Mitch) · OR utilization tooling (Katie's
  scheduling pilot: 58% → 78% in 60 days) · return-to-spine protocols for auto/conservative-care
  patients (flagged in Q2 review as a revenue-per-case driver).
- **Next:** daily 4pm access check-in continues · **Fri 7/24** — scorecard first fill + OODA read ·
  Thursday — Kristen Teams intro · **week of Aug 10** — production/shoot week + headshots (Aug 10).

---

*Compliance floor on everything above: no PHI or unconsented patient stories (HIPAA) · no
unsubstantiated or superiority claims (FTC) · physician review on all clinical content
(E-E-A-T/YMYL) · WCAG AA / Section 1557 · clinical + legal items ship only after human review.*

*Document map: `playbooks/master-game-plan.md` (system) · `playbooks/spine-90day-plan.md` (targets)
· `playbooks/b2b-physician-liaison-strategy.md` · `playbooks/call-center-strategy.md` ·
`audits/cardinal-recommendation-tracker.md` (live status) · meeting sources: Otter 7/21 ×6.*
