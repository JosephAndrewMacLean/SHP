# Spine Content Cluster Map — synergyhealth.org

**Status:** working strategy, drafted Jul 21, 2026 from `seo/gsc-analysis-2026-07.md` (16-mo GSC
data), `brand/current-state.md`, and the Jul 20–21 Joe/Randall/Paul meetings. All patient-facing
copy produced from this map is **draft pending medical + compliance review** before publish.
**Feeds:** `playbooks/spine-90day-plan.md` workstream B (the −71/mo B2C spine hole; 80% of SEO
effort to spine; "2 spine pages this week, 3 next").

---

## 1. The strategic answer from the meeting (settled, so we stop relitigating it)

**Question fought over:** "does pushing spine de-rank ortho?"
**Answer:** promoting spine costs ortho only if we change the *architecture* (swap hierarchy
levels, redirect ortho URLs, rewrite ortho pages to say spine). We are not doing that.

- **Ortho keeps its taxonomy position and its URLs.** Ortho is the parent discipline; spine is
  the specialty cluster we deepen. Nobody touches ortho pillar pages, the high-earning ortho
  blogs, or provider pages except title/meta polish (`quick-wins-title-meta.md`).
- **Spine grows by addition, not subtraction:** new/rebuilt spine condition + treatment +
  location + learning-hub pages, densely interlinked, each answering questions ortho pages
  never targeted. Different queries → no cannibalization of ortho.
- **Emphasis shifts are allowed where they're cheap and reversible:** internal links (homepage,
  footer, hub cross-links) may weight spine more heavily. That can nudge relative crawl/em­phasis —
  acceptable and monitorable — vs. structural demotion, which is what actually tanks a line.
- **Tripwire:** monthly GSC section watch (§8). If ortho non-branded clicks drop >15% for two
  consecutive months without a seasonal/SERP explanation, we pause spine internal-link
  expansion and diagnose before continuing.

**Why one-page-at-a-time GPT edits are banned** (the mechanism, for the record): a single page
optimized in isolation drifts toward the cluster's head terms ("spine surgery," "back pain"),
overlapping siblings that already target them. Google then re-picks which URL to rank per query —
the pages trade positions instead of both rising (visible today: neck fracture ×2 both pos ~7,
laminectomy ×3, microdiscectomy ×3). Every edit ships with this map + current GSC data as
context. Process in `content-update-workflow.md`.

---

## 2. Cluster architecture (hub-and-spoke, many-to-many by links — never by duplicate copy)

```
SPINE PILLAR  /specialties/spine-back-and-neck/            [rebuild — pos 24.7 today]
│
├─ CONDITIONS  /conditions-we-treat/spine-neck-back-conditions/<condition>/
│   spinal stenosis · herniated disc · sciatica · degenerative disc disease (NEW) ·
│   spondylolisthesis · cervical radiculopathy · neck (cervical) fracture · back
│   (vertebral) fracture · failed back surgery / adjacent segment (NEW — §5) ·
│   arthritic back pain / facet arthritis
│
├─ TREATMENTS  /specialties/spine-back-and-neck/<treatment>/
│   Surgical: lumbar laminectomy · microdiscectomy · ACDF · cervical disc replacement
│   (ACDR — NEW) · cervical fusion · thoracic/lumbar fusion · thoracic/lumbar
│   decompression · SI joint fusion · kyphoplasty/vertebroplasty · revision spine
│   surgery (NEW — §5)
│   Non-surgical (pain mgmt URLs stay in pain mgmt — cross-linked, not moved):
│   ESIs · medial branch blocks / RFA · spinal cord stimulator · MILD procedure
│
├─ PEOPLE  /providers/<surgeon>/  [strongest asset on the site — link INTO, don't restructure]
│   Surgical: McCarty · Maslak · Varghese · Salar · Munk · Zamorano
│   Conservative/interventional: Oddo · Lee · Kassa · Singh
│
├─ PLACES  spine service pages under each real clinic (§6)
│   Livonia · Sterling Heights · Southfield (exists — pos 15.4, fix) · Troy (PRIORITY) · Rochester
│
└─ LEARNING HUB  /patient-center/learning-hub/… (797 impressions today — the answer engine, §7)
    question-level articles feeding conditions ↔ treatments both ways
```

**Many-to-many rule** (sciatica ↔ {PT, injections, microdiscectomy, laminectomy}; fusion ↔
{DDD, spondylolisthesis, trauma}): each entity gets **one canonical page**; relationships are
expressed as **link blocks with unique 2–3 sentence context**, never copied treatment paragraphs
on condition pages (that's how duplicate-content sprawl started). Condition pages own
"do I have this / what happens next"; treatment pages own "how it works / recovery"; learning-hub
articles own single specific questions and funnel to both.

## 3. Page standards (every spine page, per audits + brand brief)

Grade 6–8 reading level (site is 80% Grade 12+ today) · named physician reviewer + review date
(E-E-A-T/YMYL — **blocking**, no publish without it) · FAQ block answering 3–5 real patient
questions (site has zero FAQ pages; FAQPage schema itself is Cardinal's deployment) · symptom-aware
entry ("not sure what's wrong?" path — audit: site assumes a diagnosis) · the spine
differentiation story (deep bench: 6 surgeons incl. neurosurgery + 4 interventional physicians,
conservative-to-surgical under one roof, minimally invasive focus — currently messaged nowhere) ·
insurance/access block (verify per `brand/current-state.md` payer taxonomy — Medicaid varies by
provider, never a flat yes/no) · one clear next step (book online — the $0 channel that captures
at ~75%) · trauma topics (fractures) carry a "call 911 / go to the ER now if…" banner ·
no outcome guarantees, no "best/#1", stats only with substantiation and never adjacent to
disclaimers (FTC).

## 4. Primary-URL decisions (kills the cannibalization; Cardinal executes redirects/canonicals)

| Topic | PRIMARY (keep + rebuild) | Consolidate into it (301) | Data basis |
|---|---|---|---|
| Laminectomy | `/specialties/spine-back-and-neck/lumbar-laminectomy/` | `/treatment/laminectomy/`, `/treatment/lumbar-laminectomy/` | 87.5K impr on primary vs 6.6K + 2.3K stubs |
| Neck fracture | `/conditions/neck-fracture-broken-neck/` | `/conditions-we-treat/spine-neck-back-conditions/neck-fracture-broken-neck/` | 69K vs 40K impr, both pos ~7 — merge strongest copy into primary |
| Back fracture | `/conditions/back-fracture-break/` | `/conditions-we-treat/.../back-fracture-break/` | pos 8.7 vs 32.1 |
| Microdiscectomy | `/specialties/spine-back-and-neck/microdiscectomy/` *(cluster-consistent)* | `/treatment/microdiscectomy/`, blog `/herniated-disc-microdiscectomy/` | /treatment/ ranks 8.3 today — redirect only AFTER primary carries its content, verify no rank loss |
| SI joint fusion | `/specialties/spine-back-and-neck/sacroiliac-joint-fusion/` | `/treatment/sacroiliac-joint-fusion/` | 17.5K vs 3.1K impr (SI *injection* stays in pain mgmt) |
| Decompression | `/specialties/spine-back-and-neck/thoracic-lumbar-decompression/` | `/treatment/thoracic-lumbar-decompression/`, `/treatment/spinal-decompression/` | MILD blog stays separate (distinct procedure) but cross-links |
| Cervical fusion | `/specialties/spine-back-and-neck/cervical-fusion/` | `/treatment/lumbar-cervical-fusion/` (split: cervical→here, lumbar→fusion page) | 80K impr @ pos 9.0 on primary |
| Kyphoplasty | `/treatment/kyphoplasty-vertebroplasty/` → migrate to `/specialties/spine-back-and-neck/kyphoplasty-vertebroplasty/` | `/specialties/pain-management/kyphoplasty/` | 6.7K vs 0.4K impr |
| Spinal cord stimulator | `/specialties/pain-management/spinal-cord-stimulator/` | `/treatment/spinal-cord-stimulator/` | Stays a pain-mgmt page; spine cluster links to it |
| Medial branch blocks | `/specialties/pain-management/lumbar-medial-branch-block/` (+cervical page kept) | `/treatment/medial-branch-blocks-cervical-lumbar/` | pos 6.2 on primary |
| Spine hub | `/specialties/spine-back-and-neck/` | `/specialty/spine-neck-back/`, `/specialties/spine-neck-back/` | 66.5K impr on primary |
| Sterling Heights | decision needed: legacy `/full-service-clinics/sterling-heights-2/` holds 94K impr / 2,566 clicks — **do NOT redirect until `/locations/sterling-heights/` is demonstrably stronger**; interim: canonical stays self, align titles | `/specialties/orthopedic-services/sterling-heights/`, `/specialties/hand-upper-extremity/sterling-heights/` → nearest real page | Biggest location asset on the site |
| Southfield | `/locations/clinic-locations/southfield/` (+ its spine/ortho/podiatry children) | `/locations/southfield/`, `/location/southfield/`, `/full-service-clinics/southfield/`, `/specialties/orthopedic-services/ortho-southfield/` | 83K impr on primary; 8 variants today |
| Troy | `/locations/troy/` | `/location/troy-clinic/`, `/locations/clinic-locations/troy/` | 6.9K vs 0.5K/0.1K |
| (Ortho, for Cardinal's list — not our build) TKA | strongest content of `/specialties/orthopedic-services/total-knee-arthroplasty-tka-comprehensive…/` (229K impr) vs `/treatment/total-knee-arthroplasty-tka/` (pos 9.3) — verify content depth first | 5 remaining variants | 7 URLs today |

Rules: never 301 a page-1 URL into a page-3 URL (move content to the primary first, watch 2–4
weeks, then redirect) · every consolidation is one batch, logged, measured (workflow §4) ·
sequence AFTER the first title/meta wave so effects are separable.

## 5. The two NEW content clusters (whitespace with a business case)

**A. Returning / revision spine patient** — leadership's target patient; **zero queries, zero
pages today.** Build: revision spine surgery treatment page (why revisions happen, candidacy,
how revision differs, imaging/records to bring) · failed back surgery (persistent pain after
surgery) condition page · adjacent segment disease condition page · learning-hub support:
"Why do I still have pain after back surgery?" · "Do I need my fusion extended?" · "Second
opinion on spine surgery: what to bring" · "Hardware pain: what it means." Tone: zero blame of
prior surgeons; realistic expectations; heavy E-E-A-T (surgeon-reviewed, cited). These searchers
are low-volume, extremely high value, and exactly the "smaller cohort" Joe described.
*(Also the natural home of the second-opinion offer — same-week access is the differentiator.)*

**B. Cervical disc replacement (ACDR).** The data shows real demand SHP accidentally ranks for
with no dedicated page: "acdf" 21K impr @ pos 3.0 (0.02% CTR), "acdr" + "acdr surgery" ~10.3K
impr @ pos ~6. Disc replacement is the motion-preserving, younger-patient alternative to fusion —
matches the younger-patient shift (18–34 share 15%→21%) and the "innovative tech" story. Build
ACDR treatment page + "fusion vs. disc replacement" learning-hub comparison (a classic
decision-stage page-1 winner). Verify which SHP surgeons perform ACDR before drafting
(credential accuracy — never overstate).

## 6. Hyperlocal spine (the meeting's open question, answered safely)

GSC city demand (non-branded): near-me 47K impr · Livonia 13K · Sterling Heights 8.4K · Warren
2.7K · Southfield 2.5K · Shelby Twp 2.5K · Royal Oak 1.3K · **Troy 788** · Clawson ~0.

- **Build real pages for real clinics only:** `spine-<condition/care>` service pages under the 5
  spine-relevant locations (§2 Places), modeled on what already works (Southfield spine-neck page
  exists — pos 15.4; MRI's local pattern earns 7% CTR). Each: unique local proof — the surgeons
  who actually practice there, same-week availability, directions/landmarks, insurance, local FAQs.
  **Troy first** (Oakland County unlock; ad spend currently $0 there; organic footprint 788 impr).
- **Do NOT spin up pages for every surrounding suburb** (the "hit every city — Troy, Clawson…"
  idea). City pages for cities without a clinic, written thin and templated, are **doorway pages**
  (Google spam policy) — the likely outcome is they don't rank, and at worst they drag sitewide
  trust on a YMYL domain. And canonicalizing a Clawson page to Troy (discussed in the meeting)
  just tells Google to ignore the Clawson page — it can't rank AND canonicalize away; pick one.
- **The compliant version of "hit every city":** each clinic's spine page carries a genuine
  "communities we serve" section (Troy page serves Clawson, Madison Heights, Royal Oak…) +
  GBP service-area settings + learning-hub content with local relevance. If a non-clinic city
  ever justifies a page, it must clear the bar of *unique, useful, defensible* content — decided
  case-by-case, never batched.
- Local ranking is also GBP/reviews/citations (Cardinal's local/AIO workstream) — pages alone
  won't win the map pack; don't measure them as if they should.

## 7. Learning hub = the answer engine (feeds AEO/AIO/GEO, not just rankings)

Reality check from the data: informational queries at good positions still get ~0 CTR (AI
Overviews and snippets absorb the click). So the hub's job is **(a)** decision-stage queries
that DO click (comparisons, candidacy, recovery timelines, cost/insurance), **(b)** being the
cited source in AI answers (E-E-A-T + schema + llms.txt — with `aio-specialist`/Cardinal), and
**(c)** internal-link fuel for the money pages. Launch set (each → one condition + one treatment
page): Laminectomy recovery week-by-week ("l4-l5 laminectomy recovery time" already pos 6.3) ·
Do I need surgery for spinal stenosis? · Herniated disc: when it heals on its own · Fusion vs.
disc replacement · Signs your back pain needs a specialist · Second-opinion guide (§5) ·
What does a spine surgeon do at a first visit? · Injections before surgery: the conservative
path. Cadence: 2/week within the "2 spine pages this week, 3 next" commitment. Every article:
reviewer + date + FAQ block; hub index page gets crawlable category links (it's invisible today).

## 8. Measurement (GSC-only loop, monthly — no SEMrush, per meeting decision)

Same-day-of-month export into `seo/data/YYYY-MM-DD/` → re-run `analyze_gsc.py` → compare:
spine non-branded clicks/impr/CTR/avg-pos (goal: 48 queries → 150+ by Oct; commercial spine
impressions up 5–10× off the tiny 1.5K base) · ortho tripwire (§1) · title/meta wave CTR deltas
at 2 and 4 weeks (annotate change dates in GSC) · cluster pages: indexed → impressions →
position bands (expect condition hubs to need 3–6 months; Paul's honest number for the site
moving is 6–9) · Liine-qualified spine calls once tracking is validated (the real KPI —
clicks are a proxy). Pair with Paul's plugin gap-analysis view for title/meta prompts, but the
canonical record is the monthly export in this repo.

## 9. Sequence (aligned to the 90-day plan gates)

| When | What | Why first |
|---|---|---|
| **Wk 1–2 (by Aug 1)** | Title/meta wave 1 (`quick-wins-title-meta.md`) — no URL/content changes · fix mobile-render bug (workflow §6) · learning-hub index made crawlable | Zero-risk CTR recovery; separable measurement |
| **Wk 2–4** | Rebuild spine pillar + 5 condition hubs (stenosis, herniated disc, sciatica, DDD-new, spondylolisthesis) to §3 standards · start medical-review pipeline · hand Cardinal the §4 consolidation list | The foundational build Google can't rank us without |
| **Wk 4–8** | Treatment primaries rebuilt (laminectomy, ACDF, microdiscectomy, cervical fusion) · ACDR page + fusion-vs-ACDR comparison · Troy spine page, Sterling Heights + Livonia next · learning hub 2/wk | Demand exists now (ACDF pos 3; laminectomy 87K impr stuck pos 28) |
| **Wk 8–12** | Revision/returning-patient cluster (§5A) · remaining locations · consolidations execute (post-wave-1 data) · title/meta wave 2 from fresh export | Highest-value, lowest-volume — needs the authority base built first |
| **Monthly** | Export → analyze → compare → next batch. Every batch logged (workflow §4) | The OODA loop leadership asked for |

**Honest expectations, for the CEO conversation:** titles/metas move in 2–4 weeks (clicks, not
patients, immediately) · new cluster content needs 3–6 months to rank on a 31.8-authority domain ·
site-level "needle moved" is the 6–9 month Paul quoted · none of it converts without the
booking/phone/qualification fixes in the 90-day plan — SEO fills the funnel it doesn't own.
