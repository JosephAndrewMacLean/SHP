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
| Radiculopathy / pinched nerve | `/conditions/cervical-radiculopathy` only (clinical-term title) | Symptom-searchers can't find it | **NEW patient-language "pinched nerve" entry**; altLabel work per model §3.3 |
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
  true access promise). **Troy first for build-out — the Oakland unlock has no spine campaign
  and no spine module.**
- **GBP listings are converting** (location-listing campaigns: 375+ GA4 sessions) → listing
  hygiene (categories, spine services, photos, Q&A) joins the location work; fix the
  `scct`/UTM mangling that's breaking GA4 channel attribution (§8).
- Hyperlocal city pages: **gated on D3** (Joel Carr first-party city counts) — none built until
  the threshold list exists. Canonical self-referential (Paul).

## 7. LEARNING HUB + guides

- **Converting proof:** `/mri-facts-that-you-may-have-not-known` = 55 GA4 converting sessions —
  education content converts when it meets a real question (and it's an **ancillary/imaging**
  topic: Mitch's domain — see §9).
- Existing decision-page proof: the knee replacement guide (root post) — the pattern for spine guides.
- Legacy: Mendelson-era posts (one still pulls 162 visits — **redirect, don't delete**);
  Lasater sports post (phase 2 decision); dated stock refresh per model §3.6.
- **Missing (all NEW):** the six guides (model §3.7): Do I need spine surgery? · First spine
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

## 9. How Mitch helps (consolidated ask list)

1. **This week:** V3 (T-Lift real name) · V4 (SI-fusion ownership) · V5 (Zamorano page,
   medical-director attribution, Munk/Yacisen locations) · Friday triage buzzword list.
2. **Reviewer roster:** one named physician reviewer per condition/treatment/guide page — the
   E-E-A-T engine. His Cage Match cadence (Wed) is the review batch slot.
3. **Candidacy criteria** as CCM Plus matures (~mid-Sept): the "is this right for me?" blocks
   on treatment pages and guides come from his surgical-criteria layer.
4. **Surgeon matching matrix** (deformity/revision → Maslak; SI → per V4; motion preservation →
   Salar; fusion-avoidance → Lee; complex/robotic → McCarty) — gates the team module + matching guide.
5. **Broker the physician hours:** Maslak (endoscopic), Varghese (SI/sports), McCarty (T-Lift).
6. **Ancillary routing content (his other hat):** the "I need an MRI first" paid bucket, the
   converting MRI-facts post, and imaging/injection scheduling integration = ancillary-services
   content he owns clinically — "bring your MRI / we can order imaging" modules, imaging
   what-to-expect, 3-T MRI positioning.
7. **Red-flag standardization** — one clinically approved escalation block, used everywhere.

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
