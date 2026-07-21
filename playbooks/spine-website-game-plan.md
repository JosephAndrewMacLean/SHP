# Spine Website Game Plan — Routing & Clinical Intelligence, Jul 21 → Sept 30

**Owner:** Joe · **Clinical:** Mitch · **Data:** Joel Carr (Santosh escalation) · **Ops:** Katie/Kelly
**Build:** Paul + Randall (bounded) · **Sponsor:** Gautam
**Status: DRAFT — pending clinical (Mitch) + compliance review · Spine first; sports = Phase 2**

**This is the execution layer for:** `routing-clinical-intelligence-process.md` (who/gates/data)
· `spine-semantic-model.md` (what to build — initiatives 1–11) · `spine-page-templates.md`
(how each page is built). It plugs into `master-game-plan.md` **Workstream 4 (B2C/organic
demand rebuild)** and `spine-90day-plan.md` **§4B**, and answers to the same two gates:
**Aug 30 (65 floor) and Sept 30 (72/week)**.

---

## 1. Objective (tied to the business number)

The spine shortfall is a **B2C/organic hole (−71 vs. budget in June), not a referral hole** —
and the website is the lever this program owns: lever B in the 90-day plan is sized at
**+7 to +11 qualified spine NPs/week**. Today the elective-spine organic funnel contributes
**~zero** (six duplicate URL structures; five condition pages ranking for ≤1 keyword;
differentiators stranded off-hub), while ~80% of clicks are branded. The job by Sept 30:

1. **Make the elective-spine funnel exist organically** — non-branded impressions → clicks →
   qualified calls/bookings, measured on GSC (D2) + Liine (D5) + the weekly scorecard (D6).
2. **Route every visitor to the right door** (conservative / interventional / surgical; right
   surgeon) using Mitch-validated clinical intelligence — the website says what the call
   center says.
3. **Do it inside the gates** — every clinical claim through Mitch, every stat substantiated,
   every URL change through the V6 canonical check and Cardinal coordination.

**Not owned here (named so it isn't conflated):** surgical conversion / order-writing (Mitch's
Cage Match + Katie/physicians), ASC capacity (Katie), paid-media restructure (Cardinal), and
the referral engine (Kristen — `b2b-physician-liaison-strategy.md`).

---

## 2. The program at a glance (initiatives → waves)

Initiative numbers reference `spine-semantic-model.md` §5.

| Wave | Window | Ships | Initiatives |
|---|---|---|---|
| **W0 — Unblock** | Jul 21–27 | Verifications fired, baselines cut, interviews booked | V1–V6, D3 request |
| **W1 — Pilot + plumbing** | Jul 28–Aug 10 | Endoscopic page (pilot), consolidation plan, language map v1, hub wireframe | 1, 2, 6 (spec) |
| **W2 — Consolidate + rescue** | Aug 4–24 (overlaps W1) | 301 tranche 1, hub rebuild live, 6 conditions rescued, SI fusion + T-Lift pages, guides #1–2 | 1, 3, 4, 5, 7 |
| **GATE 1** | **Aug 30** | See §5 scoreboard | — |
| **W3 — Deepen** | Sept 1–21 | Team module + matching guide, remaining guides, hyperlocal tranche, learning-hub refresh, CCM-candidacy content | 7, 8, 9, 10 |
| **W4 — Prove** | Sept 22–30 | Rebrand purge done, full-funnel measurement readout | 11 |
| **GATE 2** | **Sept 30** | Website contribution to 72/week, documented | — |

---

## 3. Week-by-week

### W0 · Jul 21–27 — Unblock (this week)
| Day | Action | Owner |
|---|---|---|
| Mon 7/21 | Mitch's three-phase timelines received (his EOD commitment) · V1 data request to **Joel Carr** (verify "98% of spine surgeries from 3–4 terms" + NP volume by condition/surgeon) · D3 request (first-party city counts) | Joe |
| Tue 7/22 | V2 stat inventory delivered to clinical/compliance (every live efficacy stat: 90%×2, 92%, 89%, 91%, 3-of-4/8-of-10, "national top surgeon") — substantiate-or-remove ruling requested | Joe + compliance |
| Wed 7/23 | **Cage match:** V3 (T-Lift real name, via McCarty), V4 (SI-fusion ownership: Varghese tryout vs. Munk/iFuse), V5 (medical-director attribution, Zamorano page, Munk/Yacisen locations) put to Mitch | Joe + Mitch |
| Wed–Thu | **V6:** live canonical/redirect check across all duplicate pairs · plugin migrated to the practice Claude account (inside Santosh's governance) | Paul |
| Fri 7/25 | **Triage meeting (Katie + Mitch + Kelly):** buzzword list v1 (the 2023/24 Oddo workflows — "radiculopathy… there's two or three") → seed of the consumer-language map | Katie/Mitch/Kelly, Joe observes |
| All week | **Baselines cut and filed:** GSC non-branded spine (impressions/clicks/CTR, brand terms filtered incl. Mendelson/Kornblum misspellings), rankings for the 6 condition canons, Liine spine call quality, scorecard snapshot · Maslak hour booked · Randall: spine gap-analysis pass #1 (titles/metas only) · **All baselines use post-migration windows only (site migrated Apr 22; prefer Jun 1–Jul 19, post-Liine)** — paid baseline: `pm/spine-paid-search-analysis-jan-jul2026.md` (re-export month-segmented) | Joe / Randall |

### W1 · Jul 28–Aug 10 — Pilot + plumbing
- **The endoscopic page is the pilot that times the gate chain:** Maslak hour → outline →
  `content-creator` draft (Grade 6–8, template §3.4) → **Wed 7/30 cage-match clinical review**
  → compliance → Paul publishes → measurement hooks live. **Log the elapsed time of every
  gate** — this throughput number sizes everything after it.
- `seo-specialist` consolidation plan finalized from V6 results (301 map per semantic model §2)
  → **shared with Cardinal before execution** (they own technical deployment; no collisions).
- Consumer-language map v1 (triage list + GSC query language) validated by Mitch → shared to
  Kelly (scripts) and the triage-tree build (Santosh + Joe).
- Hub rebuild wireframe on template §3.1 (dual entry, differentiation band, team module slots)
  → Paul starts template dev. Guide #1 ("Do I need spine surgery?") outlined on §3.7.
- **Liine↔Zocdoc→Google Ads signal bug:** fix scoped with Paul; until fixed, paid judgment
  stays frozen (no bid changes on broken tracking — standing rule).

### W2 · Aug 4–24 — Consolidate + rescue
- **301 tranche 1** (hub twin, stenosis ×3→1, sciatica twin, microdiscectomy ×3→1) executed by
  Paul, **content migrated before redirecting** (McKenzie/endoscopic/3-T MRI copy) · rankings
  watched daily for a week per pair — any regression pauses the tranche.
- **Hub rebuild live:** dual entry + symptom router (Mitch-approved red-flag block),
  differentiation band (V2-cleared claims only), condition grid, guide rail. Team module ships
  **only if V5 is resolved**; otherwise it ships in W3.
- **Condition rescue at 2–3 pages/week:** E-E-A-T blocks (named reviewer + date + citations),
  "what you might be feeling" symptom openings, treatment-spectrum + guide rails on the six
  canons. Reviewer assignments come from Mitch (which physician reviews which condition).
- **SI fusion page** (post-V4, Varghese interview) and **T-Lift page** (post-V3, McCarty via
  Mitch) through the gate chain. ACDR mislabel fixed (title/content now motion-preservation;
  URL decision per V6 findings).
- **Guides #1–2 live** ("Do I need spine surgery?", "Sciatica treatment: your options in
  order"). Pinched-nerve patient-language entry published.
- Aug 18 board meeting: one-slide readout (baseline → current D2/D5 movement, pilot gate-chain
  time, what ships by Gate 1).

### GATE 1 · Aug 30 — see §5

### W3 · Sept 1–21 — Deepen
- **Sept 1 convergence:** Anna's scheduling rebuild goes live + Dr. Heil starts → update
  "Guide to your first spine surgery" + treatment-page what-to-expect timelines to the real
  post-rebuild journey; Heil's profile enters the care-team packaging (program, not
  individual doctor).
- **CCM Plus lands (~8 weeks from 7/21 ≈ mid-Sept):** surgical-candidacy criteria become the
  candidacy blocks on treatment pages + guides (Mitch supplies; clinical sign-off).
- **Meet-the-spine-team module + "Which spine surgeon do I need?" matching guide** (requires
  V5 + Mitch's approved matrix + Katie's routing-ops OK). Provider-page upgrades: procedures
  modules, fellowship translation (Varghese's Moe fellowship told in plain English), dedupe +
  `/our-providers/` retirement.
- **Hyperlocal tranche 1:** top cities from D3 (the "cities four and five on that list" rule),
  Clawson-pattern template, canonical self-referential.
- **Learning-hub refresh:** physician-author pipeline live (LLM-drafted, physician-edited,
  named byline); remaining guides incl. the **I3b revision guide** (Maslak) and
  "Injection vs. surgery" (Oddo/Lee).
- Salar decision expected (~3-month coaching window): if "performing," scope Arabic/Farsi
  pages (~$10K) as a W4+ item; if not, the gate held and nothing was wasted.

### W4 · Sept 22–30 — Prove
- Rebrand/staleness purge completed (legacy Mendelson posts redirected — the chronic-pain post
  still pulling 162 visits gets a redirect, not a delete; Kornblum testimonial re-attributed or
  replaced; stale Munk copy fixed).
- Full-funnel readout built for Gate 2: baseline → Sept 30 on every §5 metric, plus the
  gate-chain throughput log (how fast clinical intelligence now reaches the website).

---

## 4. Operating rhythm (unchanged, attached to existing meetings)

**Mon/Fri funnel** — pipeline status, unblock list · **Wed cage match** — Mitch's clinical
review batch + V-item resolutions · **Fri triage meeting** — language sync (website = call
center = triage tree) · **EMT** — Santosh's ecosystem diagram; escalations · **4-week OODA** —
every published change reviewed at 1/2/3/4 weeks. Escalations: clinical input >1 week → Mitch;
data >1 week → Joel Carr → Santosh; access-promise conflicts → Katie.

Agent assignments per step are in `routing-clinical-intelligence-process.md` §6; agents draft,
humans clear — no clinical, statistical, or claims-bearing content publishes on agent output
alone.

---

## 5. Scoreboard (what the gates check)

Baselines cut in W0; targets are directional where no baseline exists yet — set the absolute
numbers the week baselines land, not before (no invented targets).

| Metric | Source | Gate 1 (Aug 30) | Gate 2 (Sept 30) |
|---|---|---|---|
| Non-branded spine impressions + clicks | D2 (GSC, brand-filtered) | Rising vs. W0 baseline | Sustained rise; CTR moving toward the 3–5% benchmark |
| Condition-canon rankings (6 pages) | D2 | No consolidation regressions; duplicates de-indexing | Canons ranking where twins used to split |
| Elective-funnel organic contribution | D1 + D5 attribution | First measurable qualified calls from condition/treatment/guide pages | Counted contribution toward lever B (+7–11/wk) |
| Qualified spine calls (routing quality) | D5 (Liine tags) | Trending up; triage language live in scripts | Website-sourced qualified share up |
| Pages through the gate chain | Program log | Pilot + ≥8 pages live (hub, 3 differentiation, conditions started, 2 guides) | All W2–W3 scope live; gate-chain time known and shrinking |
| E-E-A-T coverage | Program log | 100% of new/updated clinical pages carry reviewer + date | Same, plus learning-hub refresh underway |
| Weekly spine NPs (context — whole plan, not this program alone) | D6 scorecard | **≥65 floor** | **72/week (4-wk avg)** |

---

## 6. Dependencies & risks

| Risk | Mitigation |
|---|---|
| **V6 shows canonicals already partially correct/wrong in unexpected ways** | The 301 plan is drafted *against* V6 findings, not before them; tranche execution with per-pair ranking watch and a pause rule |
| **Physician hours don't materialize** (Maslak/Varghese/McCarty interviews) | Booked via Mitch with Gautam's mandate behind them ("tell him Scott and Gautam are looking for ways for you to add differentiated value"); fallback: Mitch supplies the clinical content directly |
| **Consolidation dents the branded workhorses** (Salar bio #1 sitewide, neck-fracture page) | Both flagged KEEP/protect; no URL work near them without Paul supervision |
| **Liine signal bug persists** | Judge on GSC + Liine call quality; paid bidding stays frozen on broken tracking (standing rule from the 90-day plan) |
| **Gate-chain bottleneck at clinical review** | The W1 pilot times every gate; if Wed batches overflow, Mitch decides the split (delegate reviewers per condition) — surfaced at cage match, not worked around |
| **Cardinal collision on technical work** | Consolidation plan + schema content specs handed to them before execution; they own deployment |
| **Scope creep into sports** | Phase 2 boundary holds; sports-division concept parked in `spine-semantic-model.md` §6 |
| **Compliance drift under speed pressure** | The gates are blocking by design; the astroturfing idea stays rejected; V2 stats stay down until substantiated |

---

## 7. Leadership asks (decisions needed, not FYI)

1. **Mitch:** confirm the three-phase timelines + reviewer assignments per condition; resolve
   V3/V4/V5 at Wednesday's cage match.
2. **Santosh:** bless the data contract cadence through Joel Carr; add the website/content
   stack to the EMT ecosystem diagram; confirm plugin/Claude account governance.
3. **Katie/Kelly:** confirm the access promises the templates may state ("often within the
   week" where true); Friday triage list delivered.
4. **Gautam:** confirm this program reports as Workstream 4's website lever against the
   existing gates — no new targets invented outside the 65/72 frame.
