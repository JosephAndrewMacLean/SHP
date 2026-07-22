# Synergy Health Partners — Current State (from June 2026 audits)

> Synthesized from three external audits: **Power Digital / Cardinal — Organic Search + AIO
> Audit**, **Creative + UX Audit**, and **Paid Media Audit** (all June 2026). This is the
> team's shared ground truth. Where audits disagree or data is a snapshot, it's noted.

## Who Synergy actually is

- **Integrated orthopedic + spine practice** in **metro Detroit, Michigan** — "everything
  under one roof," same-week access, coordinated care. Website: **synergyhealth.org** (WordPress + Rank Math PRO).
- **8 locations**, notably Livonia, Sterling Heights, Southfield, Troy, Rochester. Each clinic
  effectively owns its county (61–73% of patients local) — this is a **location-specific
  business, not a metro brand**.
- **~42 physicians** (MD/DO/DPM) + ~38 allied-health providers. Provider content is already
  indexed and strong (Providers section = 182,107 impressions).
- **Rebrand in progress from "Mendelson Orthopaedic" (Mendelson Kornblum)** to Synergy —
  and it's **incomplete behind the scenes**: `payment.mendelsonortho.com` bill-pay, YouTube
  `@mendelsonortho`, and LinkedIn are all still legacy-branded.
- Service lines: **Spine/Neck/Back, Orthopedics (knee, hip, shoulder, joint, sports med),
  Hand & Wrist, Foot & Ankle (podiatry), Pain Management, Physical Therapy, Imaging/MRI.**

## The business priority (confirmed)

**New-patient growth in SPINE and ORTHO**, and proving marketing efficiency/profitability.
Spine is a top growth line (**+89% growth**; Foot +114%; Pain declining). Patient base is
trending **younger (median age 60→56, 18–34 share 15%→21%) and more commercial-pay
(42%→52%)** — driven by the service-line shift.

## Market opportunity (quantified)

- **~4,800 obtainable ortho (Commercial + Medicare) patients/year currently going to
  competitors**, concentrated in **under-penetrated Oakland County**. **Troy is the unlock**
  for Oakland ortho/spine; **Southfield podiatry** is a near-term deepening opportunity.
- Competitive tiers: **Win now** — independents (Michigan Orthopaedic Specialists, Detroit
  Bone & Joint). **Primary competition** — regional systems (Henry Ford, Corewell/Beaumont).
  **Long-term** — national (Cleveland Clinic, Mayo, HSS).
- **Differentiators to lean on everywhere:** integrated ortho+spine under one roof, same-week
  access, **96% recommend rate**, 82/100 patient sentiment (strengths: coordination, speed, clarity).

## What's already in motion (external agencies)

External partners are engaged, so the in-house team should **complement, not duplicate**
*(ownership corrected 2026-07-22)*:

- **Power Digital / Cardinal** — authored the June 2026 **audits** (Organic/AIO, Creative/UX,
  Paid Media) and runs the **90-day Organic + AIO plan** (schema deployment, technical
  fixes, spine condition hubs, local/AIO, measurement).
- **Blue Ox Digital** — the **Google Ads agency** (run by **Shaun Elley and Jake**). They
  operate the paid account day-to-day; Cardinal's Paid Media audit (Google Ads
  restructure, Liine conversion values, GEO/location targeting, PMax test) is a set of
  recommendations **about the account Blue Ox runs** — execution questions route to
  Shaun/Jake, not Cardinal.
- **Liine** (call tracking + lead qualification) went live **June 2026** — the new source of
  truth for new-patient conversions. Online scheduling tracking not yet functional.

## The core problem in one line

Synergy has the **search footprint of a dominant regional provider but converts like a much
smaller one**: **1.18M organic impressions / 90 days → 13,668 clicks (1.15% CTR vs 3–5%
benchmark); 80% of clicks are branded** (people who already know them), while **58% of
impressions are non-branded** patients in research mode who never click.

## Key gaps the audits surfaced (by discipline)

**Technical / Organic (Power Digital / Cardinal owns most of this):**
- Mobile performance **28/100**, **Core Web Vitals FAILED** — regression ~**May 1, 2026** took
  238 Good URLs → 0, persisted 6 weeks. Logo.svg is 1MB.
- Schema broken/partial: **Hospital @type cascade error on 234 pages** (incl. all 42 bios,
  22–61 errors each), **zero FAQPage**, homepage wrong entity type, **sameAs pointing to
  competitor `@mendelsonortho` YouTube**. **0 rich results in GSC. No llms.txt.**
- On-page: **120 duplicate titles, ~85 missing meta descriptions (incl. homepage), 14 missing H1.**
- **URL architecture mess:** 4 parallel structures for the same content (carpal tunnel has 3
  URLs, TKA 4–15), legacy `/full-service-clinics/` and `/shp-*` URLs, Southfield has 9 variants.
- **Content too complex:** 80% of pages read at **Grade 12+** (AI/patients want Grade 6–8);
  **zero patient FAQ / decision-support pages**.
- **Topical authority 31.8** vs 70 benchmark; **5 foundational spine hubs (stenosis, herniated
  disc, sciatica, DDD, spondylolisthesis) at near-zero** presence.
- **Thin backlinks:** 130 referring domains (82 are Google properties), **oldest editorial link
  2012**, **0 links from Michigan hospital systems / medical associations** (competitors 400+).

**Creative / UX / Messaging:**
- Site is **built for patients who already know their diagnosis** — no symptom-aware entry
  path for people still figuring out what's wrong.
- **Nav overwhelm** (300+ links, 8 panels), **"Why Synergy" buried** low on nearly every page.
- **Trust-eroding bugs:** "Disgnostics" typo, dead links, PT page CTA points to a spine
  specialist, broken find-a-doctor filters, **Hand & Wrist page still shows spine template copy**.
- **Not true paid landing pages** (full nav, easy exit); Sterling Heights LP **duplicates** the
  general Ortho page (canonical points to parent).
- **Compliance flags:** accessibility handled by a **bolted-on overlay widget** (ADA-lawsuit
  risk) + WCAG contrast failures; **efficacy stat "92% report significant pain reduction" next
  to an education disclaimer reads as a guarantee**; stats sourced to a **non-peer-reviewed
  internal database** (substantiation risk).
- **Spine has NO differentiation** — spine page uses the same generic "fellowship-trained,
  coordinated care" as every specialty; the real spine story (younger surgeons, minimally
  invasive, innovative tech) **isn't messaged anywhere**.
- Organic social is **off-brand and weaker than the website**; **16:9 videos** underperform in
  feed (need 9:16); videos open too clinical with dated renders and **double Mendelson end cards**.
- **What's working:** PT-led, UGC-style storytelling with athletes; natural straight-on
  provider shots (e.g., "Dr. Kyle" in-office). Scale this.

**Paid Media:**
- New-patient volume grew in 2025 but **flat since Q4 2025; CPA rising**; conversion volume
  just tracks spend. Quality Score **~4/10**, Ad Strength average.
- Conversion tracking mid-overhaul: moving off Calls-from-Ads/ZocDoc to **Liine qualified
  leads / booked calls / online scheduling**. "Website New Patient Intent" is **overvalued at
  $125 → should be $5**; new-patient booked call ≈ **$150** value.
- **GEO targeting gaps:** nearly all spend on Livonia + Sterling Heights; **no Troy coverage,
  Southfield near-zero, heavy location overlap.**
- Spine ad campaign has only **4 ad groups** — needs ~10 (Back Pain, Neck Pain, Sciatica,
  Herniated Disc, Spinal Stenosis, Spine Specialist, Spine Surgery, Injections, Spinal Fusion,
  Pinched Nerve). PMax test recommended for Ortho.

## Where the in-house team has white space (not covered by the agencies)

1. **PR / earned media & authority** — audits flag **no media-relations or link program since
   2012** and **0 hospital/medical-association links**. This is the single biggest un-owned lever
   and it *also* feeds AIO citations. → `pr-specialist`
2. **Referral-network engine** — PCPs, PT, chiro, pain management, ER, workers' comp. Not
   addressed by any audit (they're all digital-demand focused). → `pr-specialist` + practice
   leadership; see `playbooks/spine-patient-acquisition.md` Engine B.
3. **Guerilla / community** — Oakland County / Troy activations, workshops, partnerships. → `guerilla-marketing-specialist`
4. **Content production at scale** — physician-reviewed spine hubs, FAQs, recovery guides,
   Grade 6–8 rewrites, candidacy content, UGC-style video scripts. → `content-creator`
5. **Governance / brand consistency** — finish the Mendelson→Synergy migration; hold one
   brand standard; keep marketing promises (speed) aligned with what scheduling can deliver. → `marketing-director`

## Business operating reality (from internal data — Jan–Jul 2026)

Four internal datasets (B2C-vs-B2B attribution, the Spine Growth Operating Report, the
Zocdoc+NextGen booking analysis, and the site crawl) show how the business actually runs.

### Volume & channel mix (Jan–Jul 15, 2026)
- **6,409 total new patients**: **25.1% B2B** (referral / physician-liaison driven) and
  **74.9% B2C** (direct / consumer). B2C is the majority of every line.
- By line: **Ortho 2,966** (27% B2B) · **Spine 1,360** (**32% B2B — highest referral
  dependency**) · Foot 1,042 (12% B2B, most consumer-driven) · Hand 749 · Pain 292 (33% B2B).
- Takeaway: **spine leans on referrals more than any other line**, so the referral engine
  (Engine B in the spine playbook) is the highest-leverage spine lever — exactly what
  leadership is now pushing on.

### The spine mandate ("Gautam Direction")
- **June 2026 baseline: 248 spine NPs = 79 B2B + 169 B2C. Target: 317/month (+69).**
- Plan: **hold B2C flat, drive the gap through referrals** — lift PL/B2B spine from 79 →
  **~150/month** (B2B mix rises 32% → 47%). Weekly spine target **72** (up from the 46–48 range).
- Tracked on a **Weekly Spine Scorecard through Sept 2026** (currently unfilled) and a
  **Universal Spine Target-Account list** (currently **empty — 0 accounts loaded**).
- 30-day experiments already assigned: 2× spine target accounts; 2× PL spine field time;
  build a tiered feeder account list (ortho, pain, chiro, urgent care, PCP, PT); shift ~80%
  of SEO to spine; validate Liine booked-patient tracking before changing paid bidding.

### The physician-liaison (referral) engine
- Field team using **Map My Customer (MMC)** CRM. Q2-2025 productivity baseline:
  **2,208 practice visits → 743 new patients (33.6 NP per 100 visits).**
- **Huge producer variance:** Kristen ~**70 NP/100 visits** vs. others 6–40. Kristen (KJ)
  carries **~51% of all B2B volume** (812 patients, 31% of her book is spine). Others: Jasmine
  (JJ) 23%, Coty (CO) 12%, plus a ramping liaison (since March) and one whose volume stopped
  after May. → **Concentration risk + a clear "coach everyone toward Kristen's playbook" opportunity.**

### B2C booking behavior (Zocdoc + NextGen, Jul 2025–Jun 2026)
- **The website is the best booking source, and it's free.** Effective new-patient capture:
  **Synergy website 74.7%** and Booking Link 74.3% (both **$0 cost**) vs. **Zocdoc
  Marketplace/Discovery 56.9%** (**$182,292 cost** over the year).
- **Zocdoc "Sponsored"** is the least efficient: 1,408 new appts, **$100K cost, ~52% capture,
  ~$136 cost per captured patient.** Spine via marketplace ≈ **$127 per captured patient**;
  the same spine patient via the website costs nothing.
- **Myth busted:** raw Zocdoc cancellation/churn (~41–54%) **overstates** leakage —
  reschedules were NextGen-Kept in 439/445 cases. Real loss is the **~23–38% "no later kept
  found."** And **166 canceled/no-show patients later self-rescheduled online and kept** —
  a signal of **call-center / access friction** (patients booking around the phone).
- Implication: **shift spend from paid Zocdoc toward the website booking path, and fix
  phone/scheduling access** — both improve cost per captured patient without new demand.

### Systems landscape
- **NextGen** (EMR / new-patient source of truth) · **OrthoPlex** · **Map My Customer**
  (liaison CRM) · **Liine** (call tracking, live June 2026) · **Zocdoc** (booking) · Google Ads.
- Scheduling is **fragmented across NextGen / OrthoPlex / hybrid** — a "one source of truth"
  evaluation is underway. Attribution is an **operational best-estimate** until the
  NextGen-to-MMC crosswalk and Liine tracking are validated (don't present inferred B2C as confirmed).

### People / roles referenced
Joe (marketing/ops — the primary contact) · Gautam (leadership direction) · Kristen (PL team
lead + top producer) · Coty, Jasmine (liaisons) · Randall (SEO) · **Paul (website
developer — corrected 2026-07-22; earlier notes wrongly listed him as paid/tracking.
Ads-side ownership sits with Cardinal unless/until an internal ads owner is named;
paid tasks in `pm/master-task-list.csv` assigned to Paul likely belong to Blue Ox
Digital — Shaun Elley / Jake — or Joe as their internal counterpart)** ·
Santosh (analytics + scheduling systems). External: Power Digital / Cardinal (agencies).

## ⚠️ Budget reconciliation — the spine gap is a B2C problem, not a referral problem

The **2026 New Patients by Channel budget** reframes the whole spine target and exposes why the
"lift referrals 79 → 150" plan is both **misdiagnosed and likely impossible**.

**2026 spine budget:** **3,295 NPs/year** (~305–315/month at plan). Channel split baked into the
budget: **B2C + Natural 2,589 (79%)** and **B2B / referral only 706 (21%)**.

**June 2026, budget vs. actual:**

| June spine | Budget | Actual | Variance |
|---|---|---|---|
| Total | ~305 | 248 | **−57** |
| B2C + Natural | ~240 | 169 | **−71 (the hole)** |
| B2B / referral | ~65 | 79 | **+14 (above plan)** |

**The shortfall is almost entirely on the B2C / natural / organic side. Referrals are already
running ABOVE budget.** So the plan to close a ~57–69 gap by nearly **doubling** the referral team
(79 → 150) tries to plug a **consumer-demand hole with referral effort** — it misreads where the
gap is, and 150 would be ~2× the budgeted B2B contribution for the whole line.

**Realistic implication (drives `playbooks/spine-90day-plan.md` — being revised):**
1. **Fix the actual hole: B2C / organic spine demand + capture** — the −71 lives here. This is the
   spine SEO/AIO condition hubs, website-booking share, access/phone fixes, and the (currently
   missing) spine differentiation that makes the deep bench visible.
2. **Grow the referral engine realistically, not impossibly** — it's already above plan; push it
   from 79 toward a credible **~95–110** (quality of qualified candidates, not a near-double).
3. **Qualify, don't just fill** — route the right patient to the right door (conservative/
   interventional vs. surgical) using the 9-physician spine bench; marketing can raise candidate
   quality but **cannot fix the clinical/surgical-conversion problem leadership flagged** — that's
   an ops/clinical dependency, not a marketing deliverable.

*(Note: internal notes indicate leadership already leans toward over-delivering on ortho to offset
the spine shortfall — consistent with treating a 150-referral spine target as unrealistic.)*

## ⚠️ Payer reality (corrected from the real insurance taxonomy, Feb 2026)

Earlier notes said "SHP takes **no Medicaid**." The real `insurance_carrier` taxonomy (29 carriers,
17 plan types, 2,333 provider-location-plan rows; Notion "Insurance Page — Content Spec") shows a
more accurate picture — use this everywhere:

- **Commercial (accepted):** Aetna · BCBSM (PPO + BCN HMO) · Cigna · Cofinity/PPOM · Coventry/First
  Health · HAP · Humana · McLaren · Molina · MultiPlan/PHCS · Priority Health · United Healthcare.
- **Medicare (accepted):** Traditional Medicare + MA (Aetna, BCN Advantage, HAP, Humana, Meridian,
  Molina, Priority Health, UHC/AARP).
- **Medicaid: accepted at SELECT providers only — VARIES by provider, not universal** (Blue Cross
  Complete, HAP Empowered, Meridian, Molina, Priority Health, McLaren Medicaid). **Verify per provider;
  do not treat as a flat "no."** For spine, confirm which spine physicians take which Medicaid plans.
- **Referral required (HMO):** BCN HMO · HAP HMO · McLaren HMO · Priority Health HMO · BCN Advantage
  (PCP referral before the visit). PPO / Traditional Medicare / Self-Pay / Auto / WC = no referral.
- **Auto No-Fault PIP (all carriers) + Workers' Comp (all carriers):** accepted, no referral, no
  copay for auto — a **high-value spine channel** (ties to the WC/PI attorney feeders).
- **Uninsured / truly out-of-network:** **Harmony Health Direct Pay** + financing + self-pay bundles —
  route, don't lose.
- Surgery centers (Synergy Surgery Center + Genesys, Livonia) and imaging (Pure Open MRI/Instant
  Imaging) have **separate** participation — verify facility coverage independently.

## Guardrails reinforced by the audits

- **Substantiation:** internal-database efficacy stats need real backup; never place a hard stat
  next to a disclaimer such that it reads as a guaranteed outcome (FTC).
- **Accessibility:** move toward native WCAG remediation, not just the overlay widget (ADA).
- **Don't over-promise speed** the scheduling system can't deliver — wait-time complaints are
  the top sentiment risk and would poison AIO citations.
