# Randall's Task List — Executing Mitch's 7/22 Input (with the growth layer on top)

> **▶ Interactive workbench (send Randall this link):**
> https://claude.ai/code/artifact/331b2076-94a3-43d8-8f02-2d89f5df060c
> Same tasks as this file, plus: editable deliverable copy per task (his edits persist in his
> browser and export), per-step checkboxes, status tracking, and one-click paste-ready
> exports — the full work document and the Friday report to Joe.

**For:** Randall · **Manager:** Joe · **Clinical authority:** Mitch (nothing clinical
publishes without his sign-off) · **Dev partner:** Paul (modules/templates) — you never touch
architecture, schema deployment (Cardinal), or anything off-page.
**Sources of truth:** `pm/mitch-review-answers-2026-07-22.md` (what Mitch said) ·
`pm/spine-meta-execution-list.md` (per-URL specs) · `playbooks/spine-page-templates.md` §2
approved copy blocks · `playbooks/spine-semantic-model.md` §D2 (link contract).

**The rule of this list:** every task does three jobs at once —
1. **Mitch's ask, faithfully** (his words, his order, his clinical framing — never "improved"),
2. **Visibility** (title/meta/H1/H2s + FAQ/snippet formatting that earns impressions),
3. **Traffic → conversion action** (query-matched copy in, then book-online-first CTA,
   tracked phone, `data-cta` attributes, and the objection-removing modules on the page).

**Standing guardrails (non-negotiable):**
- NO redirects, ever. NO new stats/superlatives/guarantees — if a number has no displayed
  source, it doesn't go in. DO-NOT-TOUCH titles: Salar bio · neck-fracture · caudal-esi ·
  MILD (desc/content only).
- Draft ≠ publish: metas/copy edits in your lane can go live per the meta list; anything
  clinical (condition copy, red-flag, bios, candidacy, guides) queues for **Mitch's Wednesday
  batch**. Log every change (URL, field, before/after, date) — Paul or Joe reviews configs.
- No same-URL collisions with Cardinal in the same window. GBP/listings = separate track.
- Scoliosis appears NOWHERE as a service; Dr. Lee is pain management, never a surgeon;
  no Rochester location (Troy is on Rochester Rd).

---

## SPRINT 1 — this week (7/22–7/27): ship Mitch's direct asks

### T1 · Hub conditions vocabulary — Mitch's five words (Stop 1)
**Mitch asked:** the first conditions surface must carry **pinched nerve · radiculopathy ·
degenerative disc disease · bulging disc · disc herniation**.
**Do:** on `/specialty/spine-neck-back` — put all five words verbatim in the condition grid
and symptom-router chips. Mapping (never new pages): bulging disc + disc herniation → the
herniated-disc canon (shown as "Herniated disc (bulging disc, disc herniation)") · pinched
nerve + radiculopathy → the radiculopathy canon · DDD → its canon.
**Visibility:** these five ARE query language — work them into the hub's H2s and the meta
description naturally; each grid entry is a crawlable altLabel anchor (D2 rule 2).
**Traffic→conversion:** each chip routes to a canon carrying the dual CTA; hub keeps
book-online-first above the fold.
**Gate:** copy live this week (vocabulary is Mitch's own); full hub rebuild stays on the W2
plan. **Done when:** all five words render on the hub + GSC baseline snapshotted first.

### T2 · MRI-facts article — the nitrogen edit + the module (Stop 6)
**Mitch asked:** remove the "magnets get very hot and cooled with nitrogen" line ("will
scare patients"); imaging wording is final.
**Do:** on `/mri-facts-that-you-may-have-not-known` — 1) delete that line; 2) insert the
two-branch imaging module **verbatim from templates §2** (have-an-MRI / don't-have-an-MRI);
3) add E-E-A-T byline slot; 4) links to the EMG page + spine hub (D2).
**Visibility:** head the module with a question H2 — "Do I need an MRI before seeing a spine
doctor?" — direct People-Also-Ask/snippet target; keep everything that already ranks.
**Traffic→conversion:** this page already converts (55 GA4 conv. sessions) — add
book-online CTA + `data-cta="mri-book-i1"`; the module itself removes the #1 objection
("I need imaging first") documented in the paid-search analysis §6.
**Gate:** none — A10 is answered; executable now. **Done when:** live + logged.

### T3 · Caudal-ESI — reorder the ladder (Stop 3)
**Mitch asked:** candidacy verbiage is correct; conservative order is
**activity modifications → medications → PT → injections**.
**Do:** on `/treatment/caudal-esi/` — re-sequence the conservative-context copy to that exact
order (he reversed our draft). Title untouched (DO-NOT-TOUCH); desc refresh OK.
**Visibility:** keep the page's ranking equity — no H1/URL changes; FAQ block additions only.
**Traffic→conversion:** candidacy block stays (confirmed correct) with soft
"see if injections are your next step" CTA + `data-cta`.
**Gate:** copy reorder = clinical sequencing → include in Wednesday batch for a 30-second
Mitch nod, then publish. **Done when:** ladder order live on the page.

### T4 · Six condition canons — reviewer scaffolds + red-flag standard (Stop 2)
**Mitch gave:** red-flag = the stenosis wording, standardized (A6 ✅); reviewers =
**McCarty ×2, Maslak ×2, Varghese, Salar** (proposed mapping: stenosis + spondylolisthesis →
McCarty · herniated disc + sciatica → Maslak · DDD → Varghese · radiculopathy/pinched nerve →
Salar — **confirm Wednesday before names go live**).
**Do, per canon (sciatica · stenosis · herniated-disc · DDD · spondylolisthesis · +the new
pinched-nerve entry when Mitch clears it):** 1) extract the stenosis red-flag block verbatim
→ insert on all six; 2) build the "medically reviewed by [Name], MD · [date]" E-E-A-T block
with the proposed name **in draft**; 3) re-sequence every "treatment options, in order"
section to the Mitch ladder; 4) metas from the execution list go live now (they're your lane).
**Visibility:** this is the audit's #1 YMYL/E-E-A-T fix (P2) — named reviewers are what the
five dead condition hubs are missing; add FAQ content blocks (PAA-formatted questions).
**Traffic→conversion:** "what you might be feeling" openings target symptom queries; every
canon gets dual CTA (soft I2 + specialist bridge), near-you chips to 5 locations, guide rail.
**Gate:** names publish only after Wednesday's mapping confirm; everything else drafts now.
**Done when:** six scaffolds staged in the plugin + metas live + baselines cut.

### T5 · Provider bios — the inclusive reframe (Stop 4)
**Mitch asked:** "all our spine docs do all the stuff… a 10% nuance is fair" — full-spectrum
line + one nuance each: **Varghese SI · McCarty OptiLIF · Salar minimally invasive · Maslak
robotic · Lee non-surgical options**; McCarty's Medical-Director line stated once, light;
Zamorano = basic generic page leaning neuro + balance training.
**Do:** draft all five surgeon bios to the pattern "Dr. X treats the full range of spine
conditions, with particular depth in [nuance]" (template §3.5); strip every
scoliosis/deformity implication (Maslak, Varghese) and Munk's SI-specialist label (his iFuse
story moves to the SI page); Lee's bio joins the pain-management front door with
"non-surgical options" framing; draft Zamorano's basic page. Salar = add-only, title
untouched.
**Visibility:** bios carry 20%+ of site traffic — do NOT dilute their branded rankings
(titles stay stable except where the meta list says otherwise); nuance lines add non-branded
long-tail ("robotic spine surgeon michigan").
**Traffic→conversion:** each bio gets "procedures I perform" links (D2), clinic-days line
(pending Katie), book-with-Dr.-X primary CTA + team bridge, `data-cta="bio-book-i3"`.
**Gate:** all five + Zamorano to Wednesday's batch — bios are clinical-adjacent labels; Mitch
marks up, then publish. **Done when:** six drafts in the batch folder.

### T6 · Knee guide — bracing to bullet 2 (Stop 7)
**Mitch asked:** bracing & support moves from bullet 4 to bullet 2 in non-surgical options.
**Do:** on `/how-do-i-know-if-i-need-knee-replacement-surgery/` — that one reorder. Nothing
else; the page is the format proof for the spine guides.
**Gate:** none. **Done when:** live + logged (ortho-side heads-up in the change log).

---

## SPRINT 2 — gated queue (start drafts now, publish on gate)

### T7 · OptiLIF page draft (V3 ✅)
Draft from Mitch's description ONLY (tiny tube · avoids cutting major back muscles ·
expandable spacer · ultra-minimally invasive; altLabel "bone bag procedure") on template
§3.4; meta from the execution list (`/treatment/optilif/` ⚠ slug confirm); McCarty
differentiated-surgeon module; conservative-alternatives on the ladder; D2 links in AND out
(≥3 inbound before it ships: hub differentiation band, herniated-disc/DDD treatment
sections, McCarty bio). **Publish gate:** McCarty hour + Mitch draft sign + trademark/
manufacturer attribution check. **Visibility:** we'd own the only patient-language OptiLIF
page in the market — question-H2 FAQ for "what is the bone bag procedure."

### T8 · SI-fusion page draft (V4 ✅, wording gated)
§3.4 build; Varghese surgeon module; Munk woven in as the "trained alongside on-staff
pioneers" lineage story. **The national superlative does NOT go in any draft** — leave two
wording slots exactly as specified in the decision log (Variant A: internal count via Joel;
Variant B: pioneer-lineage pending Munk-role documentation). **Publish gate:** substantiation
+ Mitch sign. **Conversion:** candidacy block ("injections/PT tried first" per ladder) +
consult CTA naming Varghese.

### T9 · Guide #1 — "Do I need spine surgery?" (reviewer: McCarty)
Draft on §3.7 with Mitch's lede from templates §2: comforting, passive tone; the 90% figure
ONLY with a displayed peer-reviewed citation (flag to Joe if none found — then it waits);
guarantee phrase already replaced; framework on the ladder; bracing second in non-surgical
options. **Visibility:** the H1 is the query; answer-first lede is the AI-Overview/snippet
play; FAQ schema content. **Conversion:** dual CTA (soft "get your specific answer" +
"meet the spine team"). **Gate:** McCarty review via Wednesday batch.

### T10 · Internal-link pass on every page you touch (D2 contract)
For each URL in T1–T9: walk its OUT list and its destinations' IN lists from model §D2 —
anchors are altLabels in sentence context, canons only, ladder order for treatment links.
A missing link from the contract is a launch blocker. Log each added link (from → anchor →
to).

---

## The conversion-action checklist (apply to EVERY page you touch)

1. **Book-online-first** CTA row + the one tracked phone number (Liine line) — never
   phone-only.
2. `data-cta` attribute on every CTA (`templates §4` naming) so Liine/GSC attribute it.
3. The right **intent CTA pair** per templates §2 (I2 soft + bridge on education; I1 booking
   on hub/locations; I3 named-surgeon consult on treatment/bios).
4. **Objection modules** where the journey stalls: imaging module (I2/LP), insurance-clarity
   line (D7 — "varies by provider, we'll verify"), near-you chips (I1).
5. No dead ends: guide rail or team module at the bottom of every I2 surface.

## Measurement (how we know it worked)

- **Before any edit:** GSC snapshot per URL (impressions, clicks, CTR, avg position, top
  queries) — file it.
- **After:** 1/2/3/4-week GSC checks per URL (the OODA cadence); Liine `data-cta` counts
  weekly; the non-branded baseline (brand terms filtered incl. Mendelson/Kornblum
  misspellings) refreshed weekly.
- **Targets (audit-anchored):** CTR toward the 3–5% benchmark on fixed titles/metas;
  non-branded spine share up from ~20%; five words from T1 generating first non-branded hub
  impressions; conversion actions attributable per page.
- **Report:** one short Friday note to Joe — URLs shipped, URLs staged for Wednesday, GSC
  deltas, anything blocked and by which gate.

## Coverage check — every Mitch answer has a home

| Mitch's 7/22 input | Task |
|---|---|
| Five patient words on the hub conditions surface | T1 |
| Red-flag standard = stenosis wording (A6) | T4 |
| Reviewer roster counts (McCarty ×2, Maslak ×2, JV, MS) | T4 |
| Sciatica order "yes" + ladder refinement (activity mods → meds → PT → injections) | T3, T4, T7–T9 |
| OptiLIF = the T-Lift/bone-bag real name | T7 |
| SI fusion: Varghese go-forward + pioneer lineage (wording gated) | T8 |
| McCarty Medical Director — stated light | T5 |
| Inclusive labels, 10% nuance, don't pigeonhole | T5 |
| Zamorano basic page (neuro + balance) | T5 |
| Locations days-only publishing: "agree" | (Paul's roster modules — your metas only, per list) |
| MRI article: remove nitrogen line | T2 |
| Imaging module final wording | T2 (+T4 DDD, Livonia row when Paul builds) |
| Knee guide: bracing to bullet 2 | T6 |
| Guide #1: McCarty, comforting tone, his lede (compliance-edited) | T9 |
