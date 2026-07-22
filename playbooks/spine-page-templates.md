# Spine Page Templates — Layout, On-Page Elements, and the CTA Journey System

**Owner:** Joe · **Clinical review:** Mitch · **Build:** Paul (templates/dev) + Randall
(titles/metas + plugin content, bounded runway) · **Companions:**
`spine-semantic-model.md` (what to build) · `routing-clinical-intelligence-process.md` (gates)
**Status: DRAFT — pending clinical (Mitch) + compliance review**

> Every template exists to answer **the patient's reason for being on the page** — solve my
> problem (I1), learn what's causing it (I2), choose my surgeon (I3), or plan a revision (I3b) —
> and to move them one honest step forward. Performance context from the audit: mobile
> PageSpeed 28/100, Core Web Vitals failed, a 1MB logo.svg — these templates must be lean.

---

## 1. Universal rules (apply to every template below)

**Structure & semantics**
- One `<h1>` per page = the prefLabel promise in patient language. Logical `<h2>/<h3>` outline —
  heading levels never skip. Semantic HTML5: `<header> <nav> <main> <article> <section> <aside>
  <footer>`; landmarks make screen-reader navigation work.
- The internal-link modules are **structural, not decorative** — they are the semantic model's
  `related` edges rendered on-page (condition ↔ treatment ↔ surgeon ↔ guide ↔ location).
  **The per-page link requirements (OUT and IN lists, anchor rules, link budgets) live in the
  model's §D2 internal-link contract — a missing link from that contract is a launch blocker.**
- No inherited mega-nav dumps into page body (audit: 300+ links / 8 panels). Page-level
  navigation is the hub's job; body links are curated `related` edges only.

**Language & accessibility**
- Grade 6–8 reading level for patient copy (new `/conditions/` pages already achieve this —
  match them, don't regress to the legacy clinical register).
- WCAG AA native: 4.5:1 contrast, visible focus states, alt text that describes, labels on
  every form control, no reliance on the overlay widget. Language-access note in the footer.

**Performance budget (per page)**
- LCP < 2.5s mobile / CLS < 0.1 / INP < 200ms. Hero image ≤ 120KB AVIF/WebP with explicit
  `width`/`height`; everything below the fold `loading="lazy"`. Max 2 font families,
  `font-display: swap`. No render-blocking third-party scripts; video embeds are
  click-to-load facades. SVGs optimized (the 1MB logo is the cautionary tale).

**E-E-A-T block (mandatory on every clinical page)**
- Named author · named physician **medical reviewer + credentials** · last-reviewed date ·
  citations list. Rendered near the top (trust) and in full at the foot. Today **zero** spine
  pages carry a "medically reviewed" marker — this block is both the ranking fix and the
  compliance fix.

**Schema (content spec — Cardinal owns deployment; coordinate, don't duplicate)**
- Hub: `MedicalWebPage` + `MedicalSpecialty`. Condition: `MedicalCondition` (+ `FAQPage` where
  a FAQ block exists). Treatment: `MedicalProcedure`. Provider: `Physician` (fix the audited
  Hospital @type cascade — Cardinal's queue). Location: `MedicalClinic` + `LocalBusiness` NAP.
  Guide/article: `MedicalWebPage`/`Article` + `FAQPage`.

**Claims (blocking)**
- No unsourced stats (the live 90%/92%/89%/91% figures migrate nowhere until V2 clears them).
  Outcomes only from CODE surveys/peer-reviewed sources, shown with n + source + date, never
  adjacent to a disclaimer so they read as a guarantee. No "best/#1/guarantee." Testimonials:
  consented, typical, disclosed.

---

## 2. The CTA journey system

One CTA ladder, tuned per intent phase. **Every page carries its intent's primary CTA above the
fold, plus one next-phase bridge CTA.** Never a hard surgical-consult push on an I2 education
page; never bury the booking path on an I1 page.

| Phase | Patient state | Primary CTA | Bridge CTA | Never |
|---|---|---|---|---|
| **I2 LEARN** | Researching, anxious, undiagnosed | "Read the guide" / "Check your symptoms" / "Not sure where to start? Start here" | "See a spine specialist — often within the week" | Surgical consult push; lead-gate walls on basic education |
| **I1 SOLVE** | In pain, wants an appointment | **Book online** (website is the $0, ~75%-capture channel — always first) + call | "Learn what's causing this" (condition link) | Phone-only paths (patients route around phones); over-promised speed |
| **I3 CHOOSE** | Needs surgery, comparing surgeons | "Meet the spine team" / "Book a consult with Dr. X" | "Request a second opinion — bring your MRI" | Pressure language; unverifiable superiority claims |
| **I3b REVISION** | Prior surgery, symptoms returned | "Request a second opinion" + records/imaging-transfer help | "Read: your revision options" | Implying the prior surgeon failed (tone: options, not blame) |

**System rules**
1. **One phone number sitewide.** The crawl found three different numbers in play
   (855-750-5757 / 947-243-2604 / 800-387-9740) — pick the tracked line (Liine), standardize,
   and let location pages show their direct line *in addition*, labeled.
2. Online booking + phone always **both** offered; online listed first.
3. Access promises stated only as scheduling reality allows (Katie/Kelly sign-off): "often
   within the week," not a guarantee.
4. Every CTA carries a `data-cta` attribute (see §4) so Liine/GSC/scorecard can attribute it.
5. Red-flag escalation block is not a CTA — it interrupts the ladder wherever symptoms warrant
   (clinically signed-off wording; 911/urgent-care routing).

---

## 3. Per-page-type templates

Skeletons are semantic outlines with schema slots and CTA placements — Paul builds them as
WordPress templates; comments mark constraints. CSS classes are illustrative BEM.

### 3.1 HUB (pillar) — `/specialties/spine-back-and-neck/`

**Purpose/intent:** orient all four intents in one screen; route fast; carry the
differentiation band. **The dual entry is the core fix** — the site currently serves only the
already-diagnosed.

Element order:
1. Hero: H1 promise + subline (integrated care, conservative-first) + **I1 primary CTA** +
   trust strip (96% recommend — sourced; same-week access if true).
2. **Dual entry block** (the routing moment): "I have symptoms" → symptom router ·
   "I know my condition" → condition grid.
3. Symptom router (I1/I2): patient-language chips (back pain · neck pain · leg pain/numbness ·
   arm pain/tingling) → condition or urgent-care destinations. Red-flag interrupt beneath.
4. Care-pathway band (I2): conservative → interventional → surgical, honestly framed
   ("most back pain never needs surgery — we start conservative").
5. **Differentiation band (I3):** Mazor X first-in-Michigan outpatient robotics · endoscopic
   ("incision smaller than a dime") · ACDR motion preservation · MILD — aggregated here at
   last (each claim V2-cleared, linked to its treatment page).
6. **Meet the spine team** module: surgeon cards with plain-English subspecialty labels +
   "which surgeon do I need?" guide link (I3).
7. Condition grid (the 6 canons) + treatment spectrum links (the `narrower` edges).
8. Guide rail: "Do I need spine surgery?" + first-visit guide (I2→I3 bridge).
9. Locations module: 8 clinics, Troy featured; map; one number + online booking.
10. FAQ block (schema) → E-E-A-T footer.

```html
<main class="hub hub--spine"> <!-- schema: MedicalWebPage + MedicalSpecialty -->
  <section class="hub__hero"> <!-- LCP element: single AVIF ≤120KB, width/height set -->
    <h1>Spine, Back &amp; Neck Care in Metro Detroit</h1>
    <p class="hub__promise">Conservative first. Surgery when it's right. One team, one roof.</p>
    <div class="cta-row">
      <a class="cta cta--primary" data-cta="hub-book-i1" href="/schedule/">Book online</a>
      <a class="cta cta--ghost" data-cta="hub-call-i1" href="tel:+18557505757">Call us</a>
    </div>
    <ul class="trust-strip"><!-- sourced stats only (V2) --></ul>
  </section>

  <section class="hub__entry" aria-label="Start here">
    <a class="entry entry--symptom" data-cta="hub-symptom-i1" href="#symptoms">I have pain or symptoms</a>
    <a class="entry entry--diagnosed" data-cta="hub-diagnosed-i2" href="#conditions">I know my condition</a>
  </section>

  <section id="symptoms" class="hub__router"> <!-- patient-language chips = altLabel layer -->
    <h2>What are you feeling?</h2>
    <!-- chips: back pain / neck pain / leg pain or numbness / arm pain or tingling -->
    <aside class="redflag" role="note"><!-- clinically approved escalation wording --></aside>
  </section>

  <section class="hub__pathway"><h2>How we treat spine problems</h2>
    <!-- conservative → interventional → surgical; honest indications; links -->
  </section>

  <section class="hub__diff"><h2>What's different here</h2>
    <!-- Mazor X / endoscopic / ACDR / MILD cards -> treatment pages; V2-cleared claims only -->
  </section>

  <section class="hub__team"><h2>Meet the spine team</h2>
    <!-- surgeon cards: plain-English subspecialty + bio link; guide link (I3) -->
  </section>

  <section id="conditions" class="hub__conditions"><h2>Conditions we treat</h2></section>
  <section class="hub__guides"><h2>Not sure what you need?</h2>
    <a class="cta cta--soft" data-cta="hub-guide-i2" href="/guides/do-i-need-spine-surgery/">Do I need spine surgery?</a>
  </section>
  <section class="hub__locations"><h2>Eight locations near you</h2><!-- MedicalClinic refs --></section>
  <section class="hub__faq"><!-- FAQPage schema --></section>
  <footer class="eeat"><!-- author / physician reviewer + credentials / date / citations --></footer>
</main>
```

**Not on this page:** the full provider directory; unsourced stats; autoplay video; the
misfiled doctor-location hybrid child (relocating per the model).

### 3.2 LOCATION — clinic page + hyperlocal city variant

**Purpose/intent:** I1 local capture; prove "near me" + "can I get in."
Element order: H1 "Orthopedic & Spine Care in {City}" → NAP + hours + **map embed
(click-to-load)** → book online + labeled direct line → spine module (what's treated here,
which spine physicians sit here, days) → same-week promise *only if true for this clinic* →
insurance snippet (D7; varies by provider — link, don't overclaim) → local reviews (consented,
typical) → cross-links: hub + nearby-city pages. Schema: `MedicalClinic` + `LocalBusiness`,
one canonical NAP.
**Hyperlocal variant ({City} spine treatment, e.g. Clawson):** same skeleton minus clinic
facts; opens with the city ("Seeing spine patients from Clawson at our Troy office — 12
minutes away"); canonical **self-referential** (Paul's call); D3-gated existence; routes to
the nearest real clinic. **Not:** thin doorway duplication — each needs the local proof points
(distance, directions, that clinic's spine team) or it doesn't ship.

### 3.3 CONDITION — e.g. `/conditions/sciatica`

**Purpose/intent:** I2 workhorse. The patient asks *"what is this and how do I make it
stop?"*
Element order:
1. H1 (condition) + plain-English definition ("Sciatica is a symptom, not a condition — here's
   what's usually behind it").
2. **"What you might be feeling"** — the symptom-aware opening in patient words (the fix for
   built-for-the-already-diagnosed), mapping sensations → this condition vs. its neighbors.
3. Red-flag interrupt (standardized block, clinically approved).
4. Causes (links to cause conditions — herniated disc, stenosis) · Diagnosis (what we'll do:
   exam, imaging, 3-T MRI where relevant) · **Treatment, in order:** conservative →
   interventional → surgical with honest "when each is right" (links = `related` edges).
5. "Who treats this" mini-team module (I3 seed).
6. Guide rail: the condition's decision guide (I2→I3 bridge CTA).
7. FAQ block (schema) → **soft I2 primary CTA + specialist bridge CTA** → E-E-A-T footer.

```html
<main class="condition condition--sciatica"> <!-- schema: MedicalCondition + FAQPage -->
  <header class="condition__intro">
    <h1>Sciatica</h1>
    <p class="reviewed-by"><!-- Medically reviewed by [Physician, MD] · [date] --></p>
    <p class="plain-answer"><!-- 2-sentence Grade 6-8 definition --></p>
  </header>
  <section class="condition__feels"><h2>What you might be feeling</h2>
    <!-- patient-language symptom mapping; altLabels: shooting leg pain, pinched nerve -->
  </section>
  <aside class="redflag" role="note"><!-- escalation block --></aside>
  <section class="condition__causes"><h2>What causes it</h2></section>
  <section class="condition__dx"><h2>How we find the cause</h2></section>
  <section class="condition__tx"><h2>Treatment options, in order</h2>
    <!-- stepped list -> PT / injection / endoscopic; honest indications -->
  </section>
  <section class="condition__team"><h2>Who treats sciatica here</h2></section>
  <section class="condition__guide">
    <a class="cta cta--soft" data-cta="cond-guide-i2" href="/guides/sciatica-treatment-options/">Your options, explained in order</a>
  </section>
  <section class="condition__faq"><!-- FAQPage --></section>
  <div class="cta-row">
    <a class="cta cta--primary" data-cta="cond-book-i1" href="/schedule/">See a spine specialist</a>
    <a class="cta cta--ghost" data-cta="cond-call-i1" href="tel:+18557505757">Call us</a>
  </div>
  <footer class="eeat"><!-- full E-E-A-T block + citations --></footer>
</main>
```

### 3.4 TREATMENT — e.g. endoscopic spine surgery

**Purpose/intent:** I2→I3 bridge. The patient asks *"is this right for me, and who's good at
it?"*
Element order: H1 + one-line plain answer → **"Is this right for me?" candidacy block**
(clinically reviewed; CCM Plus criteria when live) → how it works (the dime-size-incision
story) → **conservative-alternatives module** (required for balance: what we try first) →
recovery expectations (honest timeline) → **differentiated-surgeon module** ("Dr. Maslak
trained in this technique" — the Bullard/Hip-Insight pattern; links to bio) → gated outcomes
slot (CODE only; empty until cleared) → comparison rail (fusion vs. ACDR; open vs. MI vs.
endoscopic) → FAQ (schema) → **I3 primary CTA (consult with the named surgeon) + I2 bridge
(read the decision guide)** → E-E-A-T footer. Schema: `MedicalProcedure`.
**Not:** minimizing risks; "routinely done elsewhere" procedures dressed as differentiators
(kyphoplasty stays a plain page); surgical CTAs without the alternatives module present.

### 3.5 PROVIDER — e.g. Dr. Maslak

**Purpose/intent:** I3 decision surface (bios already carry 20%+ of site traffic — make them
convert). Element order: name/credentials/photo (natural, straight-on — the creative audit's
working style) → **plain-English subspecialty line** ("Revision spine surgery: failed prior
fusions, adjacent segment" — never scoliosis: no one at SHP offers it, Joe 7/22) → "Procedures I perform" module (links to treatment pages —
the `related` edges) → fellowship translated ("what a Cleveland Clinic spine fellowship
means") → philosophy quote (conservative-first) → video slot (click-to-load; the Salar "Meet
Dr." video is the pattern) → consented reviews → locations + days → **I3 primary CTA (book
with Dr. Maslak / request second opinion) + team bridge CTA** → E-E-A-T applies (bio is the
author). Schema: `Physician` (correct @type per Cardinal fix).
**Not:** unsourced bio stats (V2); credential overstatement; a dead end without the
procedures/team links.

### 3.6 LEARNING HUB article

**Purpose/intent:** I2 long-tail; AEO/AIO/GEO citability. Element order: question-formatted
H1 → **the answer in the first 2 sentences** (snippet/AI-quotable) → depth sections with
question H2s → "related on this topic" rail (parent condition + sibling articles + the guide)
→ soft CTA only → E-E-A-T footer (physician-authored byline is the differentiator — "because
it's authored by them, it has more relevance"). Schema: `Article` + `FAQPage` where used.
**Not:** commodity filler ("everyone can spin up an article"); publishing without the named
physician author/reviewer; burying the answer.

### 3.7 GUIDE — e.g. `/guides/do-i-need-spine-surgery/`

**Purpose/intent:** the decision-support bridge I2→I3 (and I3b). Lives under `/guides/`;
reached mainly via condition/treatment `related` links (see `spine-semantic-model.md` §A3.7).
Element order:
1. H1 as the patient's question + **honest short answer up front** ("Most people with back
   pain never need surgery. Here's how to tell which group you're in.").
2. "Who this guide is for" (and who should skip to urgent care — red-flag interrupt).
3. **Decision framework:** the stepped pathway conservative → interventional → surgical with
   plain-language indications for each step (Mitch-approved).
4. Symptom → pathway mapping table (altLabels at work).
5. **Candidacy checklist** (clinically reviewed; mirrors CCM Plus criteria when live).
6. What-to-expect timeline: first visit → imaging → decision → (if surgery) scheduling &
   recovery (Anna's post-Sept-1 journey).
7. Insurance & coverage clarity (D7: plans vary by provider — "we'll verify yours" + link;
   self-pay/Harmony option so no one is dead-ended).
8. FAQ block (schema).
9. **Dual CTA:** soft primary "Get your specific answer — see a spine specialist" (I2) +
   bridge "Meet the spine team / request a second opinion" (I3). For the revision guide
   (I3b): "Request a second opinion — we'll help transfer your records and imaging."
10. E-E-A-T footer: named physician author + reviewer + date + citations.

```html
<main class="guide guide--decision"> <!-- schema: MedicalWebPage + FAQPage -->
  <header>
    <h1>Do I Need Spine Surgery?</h1>
    <p class="reviewed-by"><!-- author + physician reviewer + date --></p>
    <p class="plain-answer"><!-- the honest short answer, 2 sentences --></p>
  </header>
  <section class="guide__audience"><h2>Who this guide is for</h2>
    <aside class="redflag" role="note"><!-- escalation --></aside>
  </section>
  <section class="guide__framework"><h2>The path most people take</h2>
    <!-- stepped pathway visual: conservative → interventional → surgical -->
  </section>
  <section class="guide__mapping"><h2>Match your symptoms to a next step</h2>
    <!-- table in an overflow-x wrapper; patient language rows -->
  </section>
  <section class="guide__candidacy"><h2>When surgery starts to make sense</h2>
    <!-- clinically reviewed checklist -->
  </section>
  <section class="guide__timeline"><h2>What happens next</h2></section>
  <section class="guide__coverage"><h2>Will insurance cover it?</h2></section>
  <section class="guide__faq"><!-- FAQPage --></section>
  <div class="cta-row">
    <a class="cta cta--soft" data-cta="guide-book-i2" href="/schedule/">Get your specific answer</a>
    <a class="cta cta--bridge" data-cta="guide-team-i3" href="/specialties/spine-back-and-neck/#team">Meet the spine team</a>
  </div>
  <footer class="eeat"><!-- citations --></footer>
</main>
```

---

## 4. Measurement hooks (per the process data contract)

- Every CTA carries `data-cta="{template}-{action}-{intent}"`; click events → GA4/Liine so D5/D6
  can answer "which routing content produces qualified calls/bookings."
- Known dependency: the **Liine↔Zocdoc booked-online signal isn't reaching Google Ads** (bug;
  Joe + Paul) — until fixed, judge pages on GSC (D2) + Liine call quality, not paid conversion.
- Per-template review at the 4-week OODA: hub (entry-path split I1 vs I2), condition
  (non-branded impressions/clicks + guide-rail CTR), treatment (consult requests per visit),
  provider (book/second-opinion rate — Salar bio is the baseline), guide (assisted
  conversions: guide-touched sessions that later book), location (calls + direction clicks).

## 5. Build notes (the real stack)

- WordPress + Rank Math + the Synergy Content plugin (now GSC-connected; moving to the
  practice's Claude account). **Cardinal owns technical/schema deployment — hand them the
  schema content specs and the canonical map (NO redirects — Joe directive); don't double-implement.**
- Template/dev changes: **Paul**. Titles/metas + plugin-guided content: **Randall** (bounded
  runway; config changes logged). Clinical/compliance gates per the process doc before any
  publish.
- Ship order follows `spine-semantic-model.md` §C2 initiatives; the endoscopic page is the
  pilot that times the full gate chain.
