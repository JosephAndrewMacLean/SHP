# Routing & Clinical Intelligence → Website — Working Process (Mitch × Santosh × Marketing)

**Owner:** Joe (marketing) · **Clinical partner:** Mitch (Director, Clinic & Surgical Ops + Ancillary)
**Data/systems partner:** Santosh (VP Business Intelligence / systems leader) — analytics via **Joel Carr**
**Scope:** SPINE FIRST; sports medicine deferred to Phase 2 · **Window:** Jul 21 – Sept 30, 2026
**Status: DRAFT — pending clinical (Mitch) + compliance review**
**Grounded in:** the 7/21 Spine Division Strategy Meeting, the 7/21 Paul/Randall SEO meeting,
`brand/current-state.md` (June 2026 Cardinal audits), the 7/21 live-index site map, and
`playbooks/spine-90day-plan.md`.

> Companion docs: `spine-semantic-model.md` (what to build — the SKOS model and change plan)
> and `spine-page-templates.md` (how each page is built — layout, elements, CTAs). This doc is
> **who does what, with what data, behind what gates.**

---

## 1. Mandate & why this process exists

From the 7/21 meeting, Gautam's directive to Joe was explicit: **"Your clinical partner is
Mitch. Not Scott. Not any of our spines. Go to him."** Mitch is on the executive team for this
purpose and will supply the comments on web pages and the specific procedures discussed —
**endoscopic (Maslak), SI fusion (Varghese), and OptiLIF — the "T-Lift/bone bag" real name,
V3 ✅ 7/22 (McCarty)** — with an
integrated-spine approach, because "we don't have a spine division today… a collection of
individual spine physicians."

The spine problem decomposes three ways (Gautam): **new patients = Joe · surgical orders /
practice patterns = Mitch · ASC scheduling & capacity = Katie.** Spine runs at a **65–70%
new-patient rate**, and the website is the largest untapped router of the right patient to the
right door: today the elective-spine funnel (stenosis / herniated disc / sciatica → injection →
surgery) contributes **~zero organic traffic** while a single provider bio
(`/providers/mohamed-salar-md/`) carries **~21% of all site traffic**. Clinical intelligence is
what makes the website *clinically accurate at the patient level* — solving their problem (I1),
explaining their cause (I2), or matching them to the right surgeon (I3) — instead of generic.

**One correction of record:** Otter attributed "send timelines for the three spine workflow
phases by end of day" to Joe. In the transcript the speaker is **Mitch** (it directly follows
Gautam describing the three phases Mitch owns). Treat those timelines as **Mitch's deliverable
that marketing consumes.**

---

## 2. The two counterparts, precisely

### 2a. Mitch — the clinical-intelligence supply

Mitch's **Project Cage Match** is the clinical pipeline the website draws from. Its three
phases (timelines due from Mitch; reviewed at his **Wednesday-afternoon cage-match** task list):

| Phase | What it is | Website relevance |
|---|---|---|
| **1. Manual chart review / coaching** (~8 weeks, Mitch + McCarty) | Chart review + coaching the spine docs; Salar under a 3-month coaching decision | Which surgeons are differentiated and *promotable*; the Salar gate on Arabic/Farsi pages (~$10K) — **do not build until his status is decided** |
| **2. Orthoplex / CCM Plus integration** (8-week build) | Surgical criteria layer in the EMR + "easy button" surgical ordering; Synergy Access Suite (schedulers → surgical counselors); Axle boarding | Surgical-candidacy criteria become **candidacy content** on treatment/guide pages; same-week access claims must match what Access Suite + Axle can actually schedule |
| **3. Insurance approval / template notes (Turning Point)** | AI documentation checker (Santosh's PHI-secured backend), template notes that fire with the order, appeal letters, denial tracking → payer escalation | Insurance-clarity modules on pages; "is it covered" guide content; the **monitoring doctrine** (below) |

**Mitch supplies (inputs to marketing):**
- Procedure comments + differentiation specifics for the three tryout pages (endoscopic / SI
  fusion / OptiLIF). **Both open questions answered 7/22** (`pm/mitch-review-answers-2026-07-22.md`):
  "T-Lift/bone bag" = **OptiLIF** (ultra-minimally invasive, tiny tube, muscle-sparing,
  expandable spacer); SI fusion = **Varghese go-forward**, with Munk's iFuse history told as
  the "trained alongside on-staff pioneers" story on the SI page (exact wording in
  substantiation review — the national superlative can't run unverified).
- **Triage buzzwords** — the 2023/2024 workflows Dr. Oddo built with Kelly ("as simple as
  radiculopathy… there's two or three"), refined at the **Friday Katie + Mitch + Kelly meeting**.
  These become the patient-language symptom layer on the site (same words, all channels).
- Clinical accuracy review (the blocking sign-off) on every condition, treatment, and guide page.
- Practice-pattern context: which surgeon is the right destination for which candidate — the
  clinical half of the surgeon-matching content (routing surgical candidates is a
  **clinical/ops decision — Mitch/Katie/leadership, never marketing acting alone**).

**Mitch gets back (outputs from marketing):** draft pages on his cadence (batched to Wednesdays),
the consumer-language ↔ clinical-term map for validation, the publish calendar, and
content-performance readouts (which routing content is actually pulling qualified patients).

**Mitch's data-freshness doctrine applies to us too:** "our stuff is only as good as the most
updated information we have… monitoring, monitoring, monitoring." Website clinical claims get
a named reviewer + review date and a re-verification cycle, exactly like his payer-criteria tool.

### 2b. Santosh — the data supply, with a door protocol

Santosh is the **systems leader**; his role is **design choices and problem-framing, not doing
the work** ("He will establish the process… his team will actually do the work"). Joe's own
observed constraint: deep 1:1 Santosh time is scarce. So:

- **Default door: Joel Carr** — revenue-side analytics for Joe, Katie, and Mitch. Every data
  request in this process routes to Joel first.
- **Santosh personally:** design decisions (e.g., how first-party data is anonymized and
  refreshed; how triage-tree rollout works), escalations Joel can't resolve, and anything
  touching PHI-secured AI infrastructure (he built Mitch's Turning Point checker backend).
- **Standing artifacts:** his **systems ecosystem diagram** (draft at next week's EMT) — we
  attach the website/content stack to it; the **five-stage transformation governance** applies
  to any new system this process introduces; **Claude Enterprise** rollout is his call
  (disciplined, overspend-aware) — the Synergy Content plugin's move to the practice's Claude
  account (agreed 7/21 with Paul) should land inside that governance.
- **Co-owned with Joe:** call-center rollout of **Steve's triage decision tree** (per the
  meeting: "Santosh and Joe"), body-part modules, hackathon training day, and the flagged gap
  (no traditional-Medicare pathway; "three steps max" UX rule).

---

## 3. The data contract (what BI supplies, on what cadence, gating what)

| # | Data feed | Owner | Cadence | Gates (what it clears for publish) |
|---|---|---|---|---|
| D1 | Spine NP volume by condition + surgeon (Orthoplex/EMR) | Joel Carr | Monthly + on request | Condition-page priority; surgeon-matching content; **verifying the "98%" claim (V1)** |
| D2 | GSC non-branded spine queries; high-impression/low-CTR pages | Randall (via Synergy Content) + Paul | Weekly export | Which pages get title/meta fixes first; new-cluster targets; the wait-for-reindex measurement window |
| D3 | First-party patient-city counts (anonymized, last 2 yrs, count-only) | Joel Carr | Quarterly | Hyperlocal page priority ("cities four and five on that list") |
| D4 | CODE survey outcomes (spine + joint PROs, ~6-mo post-op) | Joel Carr / clinical | Per release | The **only** approved source for outcome/proof-point stats — with n, source, and date shown |
| D5 | Call-center triage tags + Liine call data | Kelly + Paul | Weekly | Whether routing content is producing *qualified* calls; known bug: Liine↔Zocdoc booked-online signal not reaching Google Ads (Joe + Paul tracking) |
| D6 | Weekly Spine Scorecard (activity / output / efficiency) | Joe + Joel Carr | Weekly | The 4-week OODA review of every published change |
| D7 | Payer/coverage reality (accepted plans by provider) | Sarah's team + Mitch Phase 3 | On change | Insurance-clarity modules; **Medicaid varies by provider — never a flat "no"** (`brand/current-state.md`) |
| D8 | **Rater8 reviews/testimonials** (review source of record) | Joe + compliance screen | Per release | All patient-voiced content: testimonials, review modules, trust-strip counts — each passes the Rater8 quality screen (authentic · typical · consented for reuse · correctly attributed · no superlatives) before publish; see the register §9 Lane D |

**Verification queue (claims that block work until verified):**

| ID | Claim | Verifier | Blocks |
|---|---|---|---|
| V1 | "98% of spine surgeries come from 3–4 search terms (sciatica, DDD, herniated disc, radiculopathy)" — said in the 7/21 meeting, unverified | Joel Carr (D1) | Condition-page *priority weighting* (build the six anyway; don't claim the mix) |
| V2 | Every live efficacy stat found on the site: 90% heal-without-surgery (×2 pages), 92% ankle, 89% Mayo bio, 91% Fox bio, 3-of-4 / 8-of-10 Lee bio, "national top surgeon" | Clinical + compliance | **Substantiate with a named source or remove before any migration to new pages** |
| V3 | ✅ **ANSWERED 7/22:** "T-Lift/bone bag" = **OptiLIF** — ultra-minimally invasive low back procedure (tiny tube, spares major back muscles, expandable spacer). Trademark/manufacturer attribution check before publish | Mitch (done); McCarty hour deepens | McCarty page unblocked — drafting now |
| V4 | ✅ **ANSWERED 7/22:** **Varghese go-forward**; Munk = the "trained alongside on-staff pioneers" story on the SI page. ⚠ Mitch's suggested "more SI fusions than any practice in the country" is an unsubstantiated superiority claim — variants A/B in the decision log; superlative does not run as-is | Mitch (done); wording → substantiation | SI page's surgeon module unblocked; final wording gated |
| V5 | ✅ **ANSWERED 7/22 (partial):** **McCarty is Medical Director of Spine** — stated on his bio + one team-module line, deliberately light ("not so heavy that he trumps traffic to all other docs"); Zamorano = basic generic page (neuro + balance training). **Still open: Yacisen locations** | Mitch (done); Yacisen → practice ops | Team module unblocked; labels now inclusive per Mitch |
| V6 | Canonical-tag + URL-resolution state of all duplicate URL pairs (crawl was index-based) | Paul (live check) | The canonical consolidation plan (NO redirects) in `spine-semantic-model.md` |

---

## 4. Sample-size & relevancy gates (publish/no-publish rules)

**Definitions.** *Relevancy* = the page answers one of the four patient intents in the
patient's own language: **I1 solve my problem · I2 learn what's causing it · I3 choose my
surgeon · I3b returning/revision patient** (failed back surgery, adjacent segment disease — a
smaller, high-value cohort currently absent from the site). *Sample size* = the minimum
evidence bar for each claim type before it's published or used to prioritize work.

| Claim / decision type | Minimum evidence bar | Verifier | Rule if bar not met |
|---|---|---|---|
| Outcome / efficacy stat on a page | CODE survey or peer-reviewed source, with n, source, and date displayed; never adjacent to a disclaimer so it reads as a guarantee | Clinical + compliance | **Do not publish.** No unsourced percentages, ever |
| Condition-page priority | D1 NP volume **and** D2 GSC demand both confirm | Joel Carr + Randall | Build at normal priority, not "98%-claim" priority |
| Hyperlocal city page | City clears the D3 first-party count threshold (top cities after the 8 clinic homes — "cities four and five on that list") | Joel Carr | Don't build; a page with no patient base is index pollution |
| New cluster / topic | High-impression low-CTR signal in GSC, **or** explicit foundational-content decision (build → index → measure → improve; Paul's doctrine: real Google data, not SEMrush estimates) | Joe | Label as foundational; set the reindex wait window before judging |
| Small-cohort content (I3b revision, second-opinion) | Justified by **specificity and fit**, not volume: documented cohort existence (D1 revision/returning counts when available) + clinical confirmation that we treat it (revision is a confirmed service; per Mitch 7/22 it stays a content lane, not a bio label — and never scoliosis/deformity framing) | Mitch + Joel Carr | Ship as guide/learning content first; promote to pillar module when data confirms |
| Surgeon-matching statement ("failed fusion → Dr. X") | Mitch-approved matching matrix; consistent with the call-center rubric; **no scoliosis pathway (no one at SHP offers it — Joe 7/22); pain-management docs (incl. Dr. Lee) are the interventional lane, never the surgeon set** | Mitch (+ Katie for routing ops) | Do not imply routing the practice hasn't approved |
| Access/speed promise ("same-week") | Confirmed schedulable by Katie/Kelly (Access Suite + Axle reality) | Katie/Kelly | Say "often within the week" only if true; never over-promise (top sentiment risk) |
| Any published change's success | 4-week OODA review on D6 scorecard + D2 GSC (1/2/3/4-week checkpoints) | Joe + Joel Carr | Iterate or revert; no "it feels better" |

---

## 5. Work map — every Synergy employee (input → output)

| Person | Input they provide | Output they owe / receive |
|---|---|---|
| **Joe** | Orchestration; consumer-language maps; GSC/paid analysis; agent direction | The publish calendar; drafts routed to gates; scorecard readout at Mon/Fri funnel meetings |
| **Mitch** | §2a: procedure comments, triage terms, matching matrix, clinical review; three-phase timelines | Signed-off clinical content; **V3/V4/V5 + A5/A6/A10 delivered 7/22 via the review packet** (`pm/mitch-review-answers-2026-07-22.md`); Wednesday batch review |
| **Santosh** | Design decisions; PHI-secured AI patterns; triage-tree rollout (with Joe); ecosystem diagram | The website/content stack represented in the EMT ecosystem view; Claude account governance |
| **Joel Carr** | D1/D3/D4/D6 data pulls; V1 verification | Standing monthly spine content-data pack |
| **Katie** | ASC/scheduling reality (access promises); triage co-design; spine-first protocol context | Content aligned to what ops can deliver; flags when marketing over-promises |
| **Kelly** | Call-center scripts; the 2023/24 Oddo workflows; triage tags (D5) | The same consumer-language map the website uses (omni-channel rule, §7) |
| **Kristen** | PL/B2B field intel: what referrers ask, which procedures they don't know we do | Referrer-facing versions of differentiation pages (one-pagers from the same source content) |
| **Paul** | Synergy Content backend; GSC integration; canonical-tag execution — NO redirects; V6 live check | Consolidation plan executed; plugin moved to the practice Claude account; Liine signal bug fix (with Joe) |
| **Randall** | Gap-analysis runs; title/meta fixes **spine-first**; plugin content drafts | **Bounded runway:** works inside Synergy Content on titles/metas + plugin-guided content; no architecture changes, no off-page campaigns; config changes logged and reviewed (Paul or Joe) — per Paul's own governance concern |
| **Anna** | Surgical-scheduling rebuild (Sept 1) | What "book surgery" actually looks like post-rebuild → informs treatment-page expectations |
| **Steve (physician)** | The Claude triage decision tree (built; not rolled out) | Rollout co-owned Santosh + Joe; his tree's branches inform the site's symptom-entry logic |
| **Dr. Maslak** | The 1-hour endoscopic interview + articles ("differentiate you in the sea of sameness") | The endoscopic page + his authored/reviewed content; bio nuance = **robotic** (Mitch 7/22, inclusive doctrine — never scoliosis/deformity); revision/I3b remains a content lane he can review |
| **Dr. Varghese** | SI-fusion interview; sports-spine crossover interest | SI-fusion page (**V4 ✅ — go-forward surgeon**); thinnest bio today — needs the fellowship story told in plain English; bio nuance = SI |
| **Dr. McCarty** | OptiLIF specifics (via Mitch — V3 ✅ named 7/22); medical-director perspective (**V5 ✅ — Medical Director of Spine, stated light**) | OptiLIF page — drafting now; guide #1 named reviewer; Mazor X first-in-Michigan claim aggregation (pending substantiation review) |
| **Dr. Salar** | (Coaching outcome pending — 3-month window) | Arabic/Farsi pages **gated** on his performing status; his bio is the #1 page sitewide — protect it during consolidation |
| **Gautam** | Sponsorship; differentiation bar ("first in the nation/state or bust") | Monthly readout that the website is producing qualified spine patients, not just traffic |

**A note on the Paul/Randall meeting (who knows what):** Paul is strong on operational
mechanics — GSC-over-SEMrush, title/meta gap fixes, canonical discipline, 6–9-month honesty —
and his warning about single-page AI edits was correct. His "every spine update de-ranks ortho"
framing overstates the mechanism (the real risks are cannibalization and authority dilution,
which the semantic model manages); Joe's position — grow spine via internal linking + the
learning hub without restructuring ortho — is the plan of record. Randall is motivated and
coachable but self-describedly "knows enough to be dangerous": he was feeding single pages to a
GPT, and he pitched the Reddit/WebMD seeding idea (rejected below). Hence the bounded runway.

---

## 6. Claude marketing-agent delegation map (what the agents do vs. human gates)

| Pipeline step | Agent | Produces | Human gate after |
|---|---|---|---|
| Topic/cluster research from GSC exports | `seo-specialist` | Cluster priorities, cannibalization map, the canonical consolidation plan | Paul executes (V6 first); Joe approves |
| Condition/treatment/guide page drafts (Grade 6–8, from Mitch-approved clinical outline) | `content-creator` | Draft copy per `spine-page-templates.md` | **Mitch clinical review → compliance → publish** |
| Symptom-entry + FAQ answer blocks; PAA targeting | `aeo-specialist` | Question-formatted sections + FAQ schema content | Clinical review (same gate) |
| AI Overviews / citability formatting | `aio-specialist` + `geo-specialist` | Citable summaries, entity consistency, llms.txt recommendation | Joe |
| Internal-link modules (the skos:related layer made visible) | `seo-specialist` | Link map per page | Paul implements |
| Consumer-language ↔ clinical-term map maintenance | `content-creator` + `call-center-manager` | The shared vocabulary file (website + scripts + triage tree) | Mitch validates terms; Kelly deploys |
| Referrer one-pagers from differentiation pages | `content-creator` + `physician-liaison-manager` | PL leave-behinds | Kristen |
| Earned-media alternative to link seeding | `pr-specialist` | Disclosed expert commentary, HARO/press sourcing, physician bylines off-site | Joe + compliance |
| Campaign orchestration across the above | `marketing-director` | Sequenced briefs | Joe |

**Standing rule:** agents draft, humans clear. Nothing clinical, statistical, or claims-bearing
publishes on agent output alone.

---

## 7. Cadence — attached to existing meetings only (no new standing meetings)

| Ritual | When | This process's slot |
|---|---|---|
| Funnel meeting (Joe chairs) | Mon + Fri | Pipeline status; scorecard readout; unblock list |
| **Cage match** (Mitch) | Wed PM | Clinical review batch: Mitch reviews queued drafts + resolves V3/V4/V5 items |
| Katie + Mitch + Kelly triage meeting | Fri (starting this week) | Triage-language sync: website symptom layer = call-center questions |
| EMT | Weekly | Santosh's ecosystem diagram; escalations only |
| 4-week OODA | Rolling | Every published change reviewed at 1/2/3/4 weeks (D6 + D2) |

**Weekly flow:** clinical inputs (Mitch/Wed) → agent drafts → clinical sign-off (next Wed) →
compliance check → Paul/Randall implement → GSC/Liine measure → scorecard (Mon/Fri).

**Escalation:** content blocked on clinical input >1 week → Mitch directly. Data blocked
>1 week → Joel Carr, then Santosh. Ops-reality conflicts (access promises) → Katie.
Anything touching payer/PHI systems → Santosh by design.

---

## 8. The omni-channel consistency rule

Joe's doctrine from the meeting, now policy: **"What it says on your website in terms of what
[each surgeon] is good at should be the same thing that the call center is saying. Omni-channel.
Everything, everywhere, we are saying the same thing."**

One shared **consumer-language ↔ clinical-term ↔ destination map** (maintained per §6) drives:
1. the website's symptom-entry layer and internal routing links,
2. Kelly's call-center scripts and the intake qualification script
   (`pm/spine-intake-qualification-script.md` — still pending clinical sign-off),
3. Steve's triage decision tree (Santosh + Joe rollout; three-steps-max; traditional-Medicare
   gap must be fixed before rollout),
4. PL leave-behinds (Kristen).

Change the map in one place; every channel updates. The map itself lives in
`spine-semantic-model.md` as the altLabel layer.

---

## 9. Risks & compliance gates (blocking)

1. **Astroturfing — REJECTED.** The Reddit/WebMD "guerrilla" seeding idea from the Paul/Randall
   meeting is undisclosed endorsement (FTC), banned by most health forums, low SEO value
   (UGC/nofollow), and a reputational hazard for a healthcare brand. The compliant replacement
   is `pr-specialist`-owned earned media: disclosed physician commentary, press sourcing,
   real community partnerships.
2. **Substantiation.** V2 stats: source-or-remove before reuse. CODE surveys are the approved
   outcomes source. No "best/#1/guarantee" language (the indexed "best spine surgeon in the
   Midwest" testimonial must be handled per FTC testimonial rules).
3. **Testimonials & patient stories** (including the patient-story videos in production):
   documented HIPAA consent, typical-results framing, disclosure.
4. **E-E-A-T/YMYL:** every clinical page ships with named physician author/reviewer +
   credentials + review date + citations. Physician-authored drafts (the "more relevance"
   doctrine from the meeting) still pass clinical + compliance review.
5. **Accessibility:** WCAG AA native (not the overlay widget), Grade 6–8 patient copy.
6. **Access promises** match scheduling reality (Katie/Kelly sign-off).
7. **Salar gate:** no Arabic/Farsi build until the 3-month coaching decision; his bio is the
   site's #1 page — any URL work near it is a Paul-supervised change.
8. **Randall governance:** full Synergy Content settings access exists as of 7/21; pair it
   with a change log and Paul/Joe review of config changes (Paul's own stated concern).
9. **Complement Cardinal, don't duplicate:** Cardinal/Power Digital owns schema deployment,
   technical fixes, and the 90-day condition-hub program (the five condition pages now exist —
   the July index shows their problem is duplication/authority, not absence). Our lane:
   differentiation content, routing intelligence, the decision/guide layer, consolidation
   *specification* (Paul executes), and E-E-A-T apparatus. Share the canonical plan with
   Cardinal before execution — and tell them explicitly: **NO redirects (Joe directive,
   7/21)**; consolidation is canonical-tag only, and their technical queue must not 301 our URLs.
10. **No redirects, ever (standing directive — Joe, 7/21).** Consolidation = rel=canonical +
   internal-link discipline + noindex for parameter junk; twins stay live; legacy pages get
   rebranded in place, never deleted to a 404. Full mechanics: `spine-semantic-model.md` §B2.

---

## 10. First 30 days (sequenced)

**Week 1 (Jul 21–27):** Mitch's three-phase timelines received · V1 data request to Joel Carr ·
V3/V4/V5 questions to Mitch (Wed) · Friday triage meeting produces the first buzzword list ·
Maslak hour booked · Paul: V6 canonical live-check + plugin account migration · Randall: first
spine gap-analysis pass (titles/metas only).

**Week 2:** Consumer-language map v1 (from triage list + GSC queries) validated by Mitch ·
`seo-specialist` consolidation plan drafted against V6 results · endoscopic page outline from
the Maslak hour · guide #1 ("Do I need spine surgery?") outlined per the semantic model.

**Weeks 3–4:** First differentiation page (endoscopic) through the full gate chain as the
**process pilot** — time every gate, fix the bottlenecks, then scale to SI fusion, OptiLIF,
symptom-entry layer, and the guide layer per `spine-semantic-model.md` §C2 priorities.

**Success measure (through D6):** non-branded spine impressions + clicks rising (D2), qualified
spine calls rising (D5), consolidation losses avoided (no ranking regressions on canonicalized pairs),
and the elective-spine funnel finally contributing organic NPs — reviewed on the 4-week OODA.
