# Prep: What We Need From Mitch & Santosh vs. What We Run Ourselves

**For:** Joe · **Use:** send §2 to Mitch before Wednesday's cage match; send §3 to Santosh
(or bring to EMT); §1 is our own runway — start it today.
**Sources:** the prioritized register (`spine-page-inventory-improvement-register.md` §9),
the process doc gates, the Cardinal-weighted P0–P8 order.
**Status: internal working doc.**

---

## 1. The independent track — Joe + Randall + Paul, no waiting on anyone

**Rule of thumb: we can DRAFT and DE-RISK everything ourselves; we only wait on clinical
sign-off (Mitch), data (Joel/CODE), and testimonial screens (Rater8). Removal is always safe;
addition needs gates.**

### Start today (this week)

| Who | Work | Notes |
|---|---|---|
| **Paul** | **V6 live check** — canonicals/redirects across every duplicate pair; which hub template actually serves | The P1 unlock; GA4 says `/specialty/` is live — confirm |
| Paul | **P0 substantiation sweep (removal half):** take down/park every unsourced stat (90%×2, 92%, 89%, 91%, 3-of-4/8-of-10, "national top surgeon") + the superlative testimonial + the Kornblum-credited testimonial | Removing risk needs no clinical input; replacements wait on Lanes C/D |
| Paul | One tracked phone number sitewide (Liine line); label local direct lines | Kelly heads-up, no approval needed |
| Paul | Fix `scct`/`y_source`/GMBSocialClimb parameter handling (canonical/param rules) | Kills index pollution + likely fixes half the GA4 channel mess |
| Paul | Liine online-booking signal bug (with Joe) — the 1.4-conversions problem | Standing rule: no bid changes until fixed |
| Paul | CWV diagnosis (the ~May 1 collapse; hub mobile 6/10) → hand findings to Cardinal (they own the queue) | Migration-regression hypothesis to confirm |
| Paul | Synergy Content plugin → practice Claude account | Flag to Santosh for governance, don't wait on it |
| **Randall** | Spine gap-analysis pass: titles/metas on high-impression/low-CTR spine pages (bounded runway) | Inside the plugin; log changes |
| Randall | Weekly GSC exports + the **brand-filtered non-branded baseline** (filter Synergy/Mendelson/Kornblum + misspellings) | The W0 baseline artifact |
| Randall | E-E-A-T **scaffold** on new/updated pages (block layout, empty reviewer/date slots) | Names drop in the moment Mitch answers A5 |
| **Joe (+ agents)** | Consumer-language map **v1 draft** from GSC queries + paid search terms | Goes to Mitch for validation (A7), not creation |
| Joe (+ content-creator agent) | Draft the six guide outlines + condition-page symptom openings + hub wireframe copy | All queue for Mitch's Wednesday batch |
| Joe (+ seo-specialist agent) | canonical/consolidation map **draft** (NO redirects) conditioned on V6's two possible outcomes | Execute only after V6 |
| Joe | Message-match map (winning paid intents → correct LP + H1) → hand to Cardinal | They own the paid restructure |
| Joe | GBP listing hygiene audit — **separate listings track, not part of the website program; Troy GBP + Oakland MRI explicitly excluded from any blending** (Joe 7/21) | Listings already convert (~375+ sessions) |
| Joe | Rater8 export of spine-relevant reviews → pre-screen queue for the D-lane | Screen criteria in register §9; compliance does final pass |
| Joe | Re-export Ads reports month-segmented + GA4 unfiltered (all sessions) | Clean baselines; spec in the paid analysis §7 |

### What we do NOT do without gates
No new clinical claims, no outcome numbers, no testimonials live, no canonical execution before V6 — and NO redirects ever (Joe directive),
no paid-bid changes before conversion values are fixed, no Arabic pages before the Salar
decision, no off-page seeding (rejected — pr-specialist owns the compliant alternative).

---

## 2. The Mitch one-pager (send before Wednesday's cage match)

**Subject: 10 quick answers that unlock the spine website program — ~45 min, most are one-liners**

Mitch — the website program is drafted and running; nothing below asks you to write anything.
Drafts come to you; you correct and sign. Ten items, grouped by effort:

**Instant answers (facts you have):**
1. What's the real name of Scott's "T-Lift / bone bag" procedure, in the words we should use
   with patients? *(unlocks the third differentiation page)*
2. SI fusion: is Varghese our go-forward SI surgeon (per the tryout), and how does Munk's
   iFuse history fit? *(unlocks the SI page + surgeon module)*
3. Confirm: who is Medical Director of Spine (site copy conflicts — Salar vs. Zamorano)? And
   Munk's + Yacisen's actual locations? *(unlocks the team module)*
4. Which spine physicians sit at which clinics, on which days? Troy first. *(location modules)*

**Decisions (one meeting, no homework):**
5. **Name one physician reviewer per condition/treatment/guide page** — our biggest unlock;
   every page's "medically reviewed by" line waits on this roster. We bring the page list.
6. Approve one standardized red-flag escalation block (we'll bring the draft, modeled on the
   stenosis page's bladder/bowel warning) for use on every symptom/condition surface.

**Reviews (we bring drafts; you mark up):**
7. The consumer-language map v1 (patient words → conditions → right door) — from Friday's
   triage list + search data. You validate the words; same map goes to Kelly's scripts and
   Steve's tree.
8. The imaging module wording ("No MRI yet? We can order imaging if you need it — and we read
   outside MRIs") — your ancillary call.

**Intros (two-line emails):**
9. Broker the three hours: Maslak (endoscopic), Varghese (SI/sports), McCarty (T-Lift) —
   framing per Gautam: "we want to market your differentiated value; help us build the page."

**Heads-up, no action now (the road ahead):**
10. Coming to you later: candidacy blocks once CCM Plus lands (~mid-Sept); the surgeon-matching
    matrix (we know Salar routing is leadership's call — we'll ship neutral labels first);
    weekly draft batches at cage match; Zamorano page last, after the attribution answer.

---

## 3. The Santosh one-pager (his door protocol respected: 3 design calls, the rest is Joel)

**Subject: 3 design decisions + a standing Joel Carr data pack for the spine website program**

Santosh — per your operating model, only the design choices come to you; execution routes to
your team. The program's gates honor your governance (nothing publishes on agent output alone;
plugin/AI usage sits inside your rollout discipline).

**Design decisions (you, ~30 min):**
1. **Define the one money event.** GA4 key events run ~3.3/session (soft events counted);
   Ads optimized toward ZocDoc + a $125-valued intent click. We propose: *Liine qualified
   call + real online booking submitted* as the only KPI events; everything else demoted.
   Your call on the exact definition + where it lives (GA4/Liine/Ads values).
2. **Channel/UTM attribution design.** 1,565 GA4 sessions are "Paid Search" with
   `google / organic` source; 661 `(not set)` — likely the `scct` parameter scheme. Paul can
   implement; we need your design for UTM/channel rules so paid vs. organic is trustworthy.
3. **Triage decision tree rollout plan** (co-owned with Joe, per the 7/21 meeting): spine
   module next, the traditional-Medicare gap fix, hackathon training, and one shared
   symptom-language map across tree/call center/website.

**Route to Joel Carr (standing monthly pack + three one-time pulls):**
- One-time: **V1** — validate "98% of spine surgeries come from 3–4 search terms" against real
  NP-by-condition data · **D3** — anonymized patient-city counts, last 2 yrs (gates hyperlocal
  pages) · post-migration re-cuts of Ads/GA4 baselines.
- Monthly: NP volume by condition + surgeon×procedure (D1) · CODE survey outcome releases
  (D4 — our only approved stat source) · scorecard feed (D6).

**FYI only (no action):** the ecosystem diagram you're presenting at EMT — please include the
website/content/measurement stack (GSC, GA4, Synergy Content + Claude account, Liine, Ads,
Rater8) so this program's tooling is visible in the holistic view.

---

## 4. The one-line version

**Mitch:** 10 answers, mostly one-liners, one roster decision — then drafts flow to his
Wednesday batch. **Santosh:** 3 design calls; everything else is a Joel Carr standing order.
**Us (Joe/Randall/Paul):** everything else is already ours — V6, the P0 risk sweep, baselines,
drafts, plumbing — and it starts today.
