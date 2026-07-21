# Spine Page Inventory & Improvement Register

**Owner:** Joe · **Working register — updates as V-items resolve and work ships**
**Status: DRAFT — pending clinical (Mitch) + compliance review**
**Evidence base:** July index crawl (Semrush/Google, 7/21) · GA4 new-site export (5/21–7/21) ·
Google Ads exports (Jan 1–Jul 19, era-mixed) · June 2026 Cardinal audit. Direct page renders
still unverified (V6) — statuses marked accordingly.
**Companions:** `playbooks/spine-semantic-model.md` (the target model) ·
`playbooks/spine-page-templates.md` (what "good" looks like per type) ·
`playbooks/routing-clinical-intelligence-process.md` (gates) · `playbooks/spine-website-game-plan.md` (when).

---

## 1. The performance bar (what EVERY page needs — the 8-point check)

From the templates doc; a page "performs" when all eight hold:

1. **One patient-language H1** matching its concept's promise; semantic heading outline.
2. **E-E-A-T block** — named author + physician reviewer + credentials + review date + citations
   (today: zero spine pages carry one).
3. **Grade 6–8 copy** (new `/conditions/` pages pass; legacy pages don't).
4. **Speed** — LCP < 2.5s mobile; hub mobile score is 6/10 and CWV collapsed ~May 1
   (post-migration); no render-blocking third parties.
5. **Intent CTA above the fold + next-phase bridge CTA** (online booking first, ONE tracked
   number — three numbers are currently live).
6. **Internal-link modules** = the semantic model's `related` edges (condition ↔ treatment ↔
   surgeon ↔ guide ↔ location) — visible, curated, no mega-nav dumps.
7. **Schema slot** filled per type (content spec ours; deployment Cardinal's).
8. **Measurement** — `data-cta` attributes wired to a real money event (see §6: GA4 key events
   are currently inflated and channel attribution is broken).

---

## 2. HUB pages

| Page (evidence) | Today | Gaps | Actions | Mitch input | Santosh/Joel input |
|---|---|---|---|---|---|
| `/specialty/spine-neck-back` — **the live hub** (GA4: 322 converting sessions; 41 kw, mostly branded incl. "mendelson kornblum") | Receives paid + organic; branded-only visibility | No symptom entry; no differentiation band; no team module; no guide rail; branded-dependent | **Rebuild as the pillar** per template §3.1 once V6 confirms it as the winner | Triage buzzwords for the symptom router; sign-off on red-flag block; differentiation claims review | D1 condition volumes (grid order); GA4 fixes so hub conversion is measurable |
| `/specialties/spine-back-and-neck/` + 10 children (index: parents the surgical procedure pages; GA4: **1 session**) | Indexed, likely pre-migration leftover | Entire branch ranks for zero top-100 kw | **V6 decides direction**; migrate child procedure content into canon, then 301 | — | — |
| `/specialty/spine-neck-back/sterling-heights` (GA4 11 sessions; paid $3,017) · `/livonia` (GA4 4) | Live city×spine LPs | Not on the location template; access promises unverified | Rebuild per template §3.2 as the paid-LP variants (message-match "spine specialist {city}") | Confirm which spine physicians sit at each site, days | Liine per-location call tagging |

## 3. CONDITION pages (the six canons + twins)

**Systemic:** every canon needs E-E-A-T block, "what you might be feeling" symptom opening,
standardized red-flag block, treatment-spectrum links, guide rail, FAQ schema. Priority
weighting waits on **V1** (Joel Carr: verify "98% from 3–4 terms" + NP volume by condition).

| Concept | URLs found | Today | Key actions |
|---|---|---|---|
| Spinal stenosis | `/conditions/spinal-stenosis` + `/conditions/lumbar-stenosis` + S3 twin — **×3** | ≤1 kw each; best red-flag block on site (bladder/bowel) | Consolidate ×3→1; link MILD page (it ranks, 33 kw, unlinked); standardize its red-flag block sitewide |
| Sciatica | `/conditions/sciatica` + S3 twin | **0 kw** despite good "symptom not condition" copy | Consolidate; symptom opening; guide rail ("options in order") |
| Herniated disc | `/conditions/herniated-disc` + root orphan `/herniated-disc-microdiscectomy/` (paid $485/conv) | Split ranking; orphan carries endoscopic copy | Migrate copy → canon + endoscopic page; 301 orphan; repoint its ads |
| Degenerative disc disease | `/conditions/degenerative-disc-disease` + legacy LP `/degenerative-disc-disease-treatment/` (paid **$1,304/conv**, 0.96%; holds 3-T MRI copy) | Legacy LP burns paid money | Migrate 3-T MRI copy; 301; repoint ads to canon |
| Spondylolisthesis | `/conditions/spondylolisthesis` + S3 twin | Near-zero | Consolidate; E-E-A-T; spectrum links |
| Radiculopathy / pinched nerve | `/conditions/cervical-radiculopathy` only (clinical-term title) | Symptom-searchers can't find it | **NEW patient-language "pinched nerve" entry**; altLabel work per model §A3.3 |
| (Protect) Neck fracture / back fracture | `/conditions/neck-fracture-broken-neck` (132 kw/388 visits, #4 sitewide) + S3 twin cannibalizing | The template's proof it can rank | KEEP/protect; 301 the S3 twin into it carefully |

**Mitch:** assign one physician reviewer per condition; validate red-flag wording; approve
symptom-language maps. **Santosh/Joel:** V1 + D1 volumes; GSC non-branded per condition
(baseline + 4-week OODA readout).

## 4. TREATMENT pages

| Cluster | URLs found | Today | Key actions |
|---|---|---|---|
| **Endoscopic (Maslak)** | copy buried on `/treatment/microdiscectomy/` (0 rank) | The differentiator invisible | **NEW page** (pilot of the whole program); migrate "dime-size incision" copy; Maslak interview |
| **SI fusion (Varghese — V4)** | `/specialties/.../sacroiliac-joint-fusion` + `/treatment/sacroiliac-joint-fusion` ×2; iFuse copy stranded on Munk pages | Duplicate + misplaced | Consolidate ×2→1; resolve V4 (Varghese tryout vs. Munk iFuse legacy); surgeon module |
| **T-Lift / "bone bag" (McCarty — V3)** | none | Doesn't exist | **NEW page** after V3 names the real procedure |
| **ACDR (motion preservation)** | S1 child slugged `anterior-cervical-discectomy-fusion` but titled ACDR; also on Salar bio | Mislabeled — fusion-alternative searchers can't find it | Fix URL/title mismatch; comparison content (fusion vs. ACDR) |
| Microdiscectomy / laminectomy / fusion / decompression | ×2–3 URLs each across `/treatment/` + S1 children | Split ranking | One canon each per V6 direction; candidacy + alternatives modules |
| **Injections (front door)** | `/treatment/caudal-esi` (**ranks: 13 kw/80 visits — best pain performer**; paid $115/conv) · lumbar ESI ×2 · RFA (25 kw) · medial branch · SI injection · SCS ×2 · trigger point · occipital · pain-management twins | Working quietly | KEEP winners; consolidate twins; add "need relief now" routing from conditions/hub (the injection-intent paid bucket at $859 CPA should land here organically) |
| MILD | `/minimally-invasive-lumbar-decompression-mild-procedure/` (33 kw — outranks all of S1) | Ranks but orphaned | KEEP; link from stenosis canon + hub differentiation band |
| Kyphoplasty | `/treatment/kyphoplasty-vertebroplasty` (26 kw) | Fine | KEEP plain (explicitly not a differentiator) |

**Mitch:** V3/V4; candidacy criteria (CCM Plus Phase 2, ~mid-Sept); honest indications per
step; broker the three surgeon interviews. **Santosh/Joel:** D1 surgeon×procedure volumes for
the surgeon modules; CODE outcomes when publishable (V2 substitute).

## 5. PROVIDER pages

| Page | Today | Actions |
|---|---|---|
| Salar (**#1 page sitewide**, 1,376 est. visits, 52% from "dr. salar" 2,900/mo) | Branded-capture engine | **KEEP/protect**; add "procedures I perform" module (ACDR/motion preservation); Arabic pages stay gated on coaching decision |
| McCarty (29 GA4 conv. sessions) | Mazor X claim stranded on his bio + Southfield page | Aggregate claim to hub (V2 substantiation first); procedures module; plain-English "complex spine + robotics" label |
| Maslak (20) | Deformity/revision subspecialty in prose only | Procedures module; **I3b revision positioning** ("failed back surgery, adjacent segment disease"); endoscopic link |
| Varghese (14) | **Thinnest bio**; elite Moe fellowship untranslated | Rewrite: fellowship translated, SI fusion module (post-V4), sports-spine angle (phase 2 hook) |
| Munk (8) | Stale "starting Tuesday, Aug 12" copy; misfiled hub-child duplicate; location conflict | Fix staleness; fold hub-child into bio + Port Huron location page; V5 locations |
| Zamorano | Page conflicting/absent (crawl found none; her own sites outrank SHP for her name); medical-director attribution conflict vs. Salar | **V5**: create/fix page; resolve attribution before the team module ships |
| Lee | "3 of 4 / 8 of 10" unsourced stats | V2: source or remove; fusion-avoidance positioning is the front-door story — keep, sourced |
| Directory `/providers/` (1,030 kw, ~7 visits converting) + `/our-providers/` + dupes (hanish/hainish-singh ×2, Oddo ×2, Gappe ×2) | Ranks, doesn't convert; QA mess | Dedupe; retire `/our-providers/`; fix find-a-doctor filter (verify live); **NEW: Meet-the-spine-team module + matching guide** (post-V5, Mitch matrix) |

## 6. LOCATION pages + local layer

- `/locations/livonia` (GA4 33) · `/sterling-heights` (31) · `/southfield` (24) ·
  `/port-huron` (58) + legacy `/full-service-clinics/port-huron/` (paid $644) + Southfield's
  7–9 indexed variants → consolidate variants; spine module per clinic (which spine docs, days,
  true access promise). **Sequencing per the location-intent roadmap: main hubs (SH, Livonia)
  first, then Troy** — the Oakland unlock with no spine campaign and no spine module.
- **GBP listings are converting** (location-listing campaigns: 375+ GA4 sessions) — but GBP is
  a **separate track, not blended with the website program** (Joe 7/21); the Oakland MRI
  listing and Troy GBP are explicitly excluded from website work. The `scct`/UTM attribution
  fix (§8) stays in scope here because it breaks GA4, not because it's listings work.
- Hyperlocal city pages: **gated on D3** (Joel Carr first-party city counts) — none built until
  the threshold list exists. Canonical self-referential (Paul).

## 7. LEARNING HUB + guides

- **Converting proof:** `/mri-facts-that-you-may-have-not-known` = 55 GA4 converting sessions —
  education content converts when it meets a real question (and it's an **ancillary/imaging**
  topic: Mitch's domain — see §9).
- Existing decision-page proof: the knee replacement guide (root post) — the pattern for spine guides.
- Legacy: Mendelson-era posts (one still pulls 162 visits — **redirect, don't delete**);
  Lasater sports post (phase 2 decision); dated stock refresh per model §A3.6.
- **Missing (all NEW):** the six guides (model §A3.7): Do I need spine surgery? · First spine
  surgery · **Failed back surgery / adjacent segment (I3b)** · Sciatica options in order ·
  Injection vs. surgery · Which spine surgeon do I need? Plus per-condition FAQ blocks.

## 8. Systemic fixes (cross-page; mostly Santosh's world)

| Fix | Evidence | Owner |
|---|---|---|
| **GA4 channel attribution broken** — 1,565 "Paid Search" sessions with `google / organic` source; 661 `(not set)`; likely `scct`/UTM mangling | GA4 export | Santosh (design) + Paul (implement) |
| **Key events inflated** (~3.3/session) — no single money event | GA4 export | Santosh: define ONE money event (booking submitted / Liine qualified call); everything reports on it |
| **Liine online-booking signal ≈ dead** (1.4 conversions counted) | Ads conv. actions | Paul + Joe (bug), Santosh visibility |
| Unfiltered GA4 exports (current one = converting sessions only, no denominator) | GA4 export | Joel Carr: standing monthly export spec |
| **One phone number** (three live: 855-750-5757 / 947-243-2604 / 800-387-9740) | Crawl | Joe + Kelly + Paul |
| CWV collapse ~May 1 (days post-migration) + mobile speed 6/10 | Audit + Ads LP report | Paul diagnose; Cardinal owns CWV queue |
| Parameter-URL index pollution (`?y_source=`, GMBSocialClimb, `{ignore}?scct=`) | Crawl + Ads | Paul (canonicals/param handling) — part of V6 |
| E-E-A-T apparatus sitewide | Crawl (zero markers) | Content pipeline + Mitch's reviewer roster |

## 9. The clinical-input list, PRIORITIZED (four lanes + Cardinal weighting)

### Lane A — Mitch can likely answer fast (this week; from his head or one conversation)

| # | Ask | Why fast | Unblocks |
|---|---|---|---|
| A1 | **V3:** real name/description of the "T-Lift / bone bag" procedure | One question to McCarty | T-Lift page build |
| A2 | **V4:** SI-fusion ownership (Varghese tryout vs. Munk/iFuse legacy) | He knows the practice patterns | SI-fusion page + surgeon module |
| A3 | **V5 (partial):** medical-director attribution; Munk/Yacisen true locations | Org knowledge | Team module accuracy |
| A4 | **Triage buzzword list** — pull the 2023/24 Oddo/Kelly workflows ("two or three words") | Friday meeting already set; artifact exists | Symptom router + call-center sync |
| A5 | **Reviewer roster:** name one physician reviewer per condition/treatment/guide | A decision, not a build | The entire E-E-A-T lane (P2) |
| A6 | **Red-flag block sign-off** (standardize the stenosis page's bladder/bowel pattern) | Pattern already exists on-site | Every condition page + symptom router |
| A7 | Validate the consumer-language ↔ condition map (batch review) | Wed cage-match batch | altLabel/routing layer |
| A8 | Which spine physicians sit at each clinic + days | Scheduling knowledge | Location spine modules, Troy first |
| A9 | Intro emails brokering the three physician hours (Maslak/Varghese/McCarty) | Two-line emails with Gautam's mandate | Lane B interviews |
| A10 | Imaging-routing wording ("bring your MRI / we can order imaging if you need it") | His ancillary domain | The MRI-first bucket module on every LP |

### Lane B — Takes time (build- or politics-dependent; weeks, not days)

| # | Item | Clock | Notes |
|---|---|---|---|
| B1 | Candidacy criteria blocks ("is this right for me?") | CCM Plus ~8 wks (mid-Sept) | Don't hand-write ahead of the tool; interim = physician-reviewed general indications |
| B2 | Surgeon matching matrix formalized + routing-ops sign-off | Weeks; **politically sensitive** (Salar redirection is a leadership call) | Gates team module + "which surgeon" guide — ship team module with neutral labels first if needed |
| B3 | The three physician interview hours + their content review cycles | Physician calendars | The differentiation pages themselves |
| B4 | Salar coaching outcome → Arabic/Farsi pages | 3-month window (~Oct) | Hard gate; no spend before |
| B5 | Zamorano page resolution | Depends on her engagement + V5 attribution outcome | Politically loaded (equipment history); do last in provider QA |
| B6 | Insurance-clarity / Turning Point-derived content | Phase 3 is "never done" | Publish plan-acceptance basics now (D7); deep coverage content follows the tool |
| B7 | Ongoing per-page clinical review throughput | Standing Wed batches | The pilot times it; escalate if the batch overflows |

### Lane C — Needs data before it can ship (CODE surveys / Joel Carr pulls)

| # | Item | Data needed | Rule |
|---|---|---|---|
| C1 | **Every outcome stat** (replacing the V2 removals: 90%×2, 92%, 89%, 91%, 3-of-4/8-of-10) | CODE PRO surveys with n + instrument + date, or peer-reviewed citation | No number publishes without its source displayed |
| C2 | "96% recommend" + "90% timely scheduling" trust-strip claims | Name the instrument (CODE? Rater8? survey vintage) | Source it or drop it from the hub hero |
| C3 | Differentiation proof points (Mazor X, endoscopic recovery claims) | CODE/literature | Capability claims OK meanwhile ("first in Michigan" needs its own verification), outcome claims wait |
| C4 | Recovery-timeline ranges on treatment pages | Clinically validated ranges (Mitch) ± CODE | Ranges, not promises |
| C5 | Condition-page priority weighting | **V1** (the "98%" claim) + D1 NP volumes — Joel Carr | Build all six regardless; weight effort only after data |
| C6 | Hyperlocal city list | **D3** first-party city counts — Joel Carr | Zero city pages before the threshold list |

### Lane D — Needs Rater8 testimonial/review quality screen (trust + validity)

Rater8 is the review source of record; nothing patient-voiced ships without this screen:
**(a)** authentic + current, **(b)** typical result (no outlier-outcome implication — FTC),
**(c)** documented consent for marketing reuse beyond the review platform (HIPAA),
**(d)** accurate attribution (right physician, right practice era), **(e)** no superlative/
superiority framing ("best spine surgeon in the Midwest" cannot run as-is).

| # | Item | Screen focus |
|---|---|---|
| D1 | Surgical testimonials for treatment/differentiation pages (the 7/21 plan: "leverage surgical testimonials from our reviews") | a–e; match testimonial to the actual procedure |
| D2 | Provider-page review modules (ratings + quotes) | a, d, e; volume + recency per surgeon |
| D3 | The **Kornblum-credited robotic-spine testimonial** currently live | Re-attribute or replace (rebrand + attribution) |
| D4 | Patient-story videos (in production) | Consent chain BEFORE edit lock; typicality framing |
| D5 | Hub trust strip review counts | Only if Rater8 is the named source |

### Cardinal-audit weighting (what to do first, per confirmed findings)

| Priority | Work | Cardinal finding it clears | Lanes it draws on |
|---|---|---|---|
| **P0 — risk now** | V2 substantiation sweep: unsourced stats + superlative testimonial down/replaced | Substantiation/FTC risk (confirmed live on 7+ URLs) | C1, D3, D5 |
| **P1 — the unlock** | URL consolidation + canonicals (V6 → 301 map) | 4-to-6 parallel structures; condition hubs built but strangled (their own 90-day work depends on it) | A2 (SI URLs), Paul |
| **P2** | E-E-A-T apparatus on every clinical page | YMYL failure — zero "medically reviewed" markers (also feeds their AIO workstream) | A5, A6, B7 |
| **P3** | Symptom-entry layer (hub router + condition openings + pinched-nerve entry) | "Built for the already-diagnosed" — zero symptom URLs sitewide | A4, A6, A7 |
| **P4** | Decision/guide layer (6 guides) | Zero decision-support pages (knee page = proof) | A5, B1 interim, C4 |
| **P5** | Differentiation aggregation + the two NEW procedure pages | "Spine has no differentiation" (partially contradicted — exists but scattered) | A1, A2, A9→B3, C3, D1 |
| **P6** | Team module + provider QA (dedupe, Zamorano, matching) | Providers strong but no choosing journey; broken filters | A3, B2, B5, D2 |
| **P7** | Location pages + hyperlocal (GBP = separate track) | GEO targeting gaps (no Troy) | A8, C6 |
| **P8** | Learning-hub refresh + purge | Dated content + rebrand remnants | A5, D3 |

**Reading:** P0 is compliance exposure and needs no new content — do it immediately. P1 is the
multiplier for everything Cardinal already built. P2–P4 are the patient-facing gap-closers and
run on Lane A answers. P5–P8 ride behind the interviews, data, and Rater8 screens.

## 10. How Santosh helps (consolidated ask list)

1. **Measurement spine first (§8):** one money event; fix channel attribution + `scct` UTM
   design; unfiltered GA4 export spec; Liine OB signal visibility. Without this, LP
   improvements can't be judged.
2. **Joel Carr standing pack (monthly):** D1 NP volume by condition + surgeon×procedure ·
   V1 verification · D3 city counts (gates hyperlocal) · CODE outcomes when releasable ·
   post-migration-window paid/GA4 splits.
3. **Triage decision tree rollout** (co-owned with Joe): spine module next after shoulder;
   fix the traditional-Medicare gap; hackathon training; the tree's branches and the website
   symptom router must share the same map.
4. **Ecosystem diagram:** add the website/content/measurement stack (GSC, GA4, Synergy
   Content, Liine, Ads) so this program's tooling is visible at EMT next week.
5. **Governance:** Synergy Content plugin's Claude account migration inside his AI-rollout
   discipline; PHI-secured patterns if candidacy logic ever touches patient data.

## 11. Sequencing

Everything above maps to the game plan waves: **W0** = §8 measurement fixes fired + V-items +
baselines · **W1** = endoscopic pilot + hub wireframe · **W2** = consolidation tranche +
condition rescue + guides 1–2 · **W3** = team module, matching guide, hyperlocal, learning-hub
refresh · **W4** = purge + proof. Gate scoreboard in `playbooks/spine-website-game-plan.md` §5.
