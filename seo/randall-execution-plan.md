# Randall — SEO Execution Plan (starts Tue Jul 22, 2026)

**Owner:** Randall · **Approvals:** Joe · **Blocking gates:** medical review (physician sign-off
on clinical copy), Paul/Cardinal confirmation before any redirect.
**Time split every week: ~80% spine / 20% everything else** (leadership decision — protect it).
**Aligned to:** Gate 1 Aug 30 (65 spine NPs/wk) · Gate 2 Sep 30 (72/wk) in
`playbooks/spine-90day-plan.md`. Sources: `gsc-analysis-2026-07.md`,
`gsc-ai-features-2026-07.md`, `spine-content-cluster-map.md`, `quick-wins-title-meta.md`.

**The ordering logic, one line:** ship the zero-risk CTR recovery first (titles/metas, spine
rows before everything), harden what AI already amplifies, then rebuild spine content on the
new `/conditions/` + `/treatment/` structure closest-to-ranking first — and let consolidations
wait for their gate.

---

## WEEK 1 (Jul 22–28) — all quick wins ship this week

### Day 1 (Tue) — setup + the two asks that have lead time
- [ ] Confirm access: Rank Math edit rights, GSC (annotations), the repo, Paul's plugin dashboard.
- [ ] Send Paul/Cardinal the two blocking asks (Joe cc'd): **(1)** confirm `/conditions/` +
      `/treatment/` is the migration end-state (cluster map §4a) — needed before ANY redirect;
      **(2)** the mobile-render bug ticket (workflow §6) — needed before batches can be
      verified on phones.
- [ ] Ask Joe to name the **physician reviewers for spine content** (need 2: one surgical, one
      interventional) and agree the turnaround SLA (target: 3 business days per page).
      This is the long pole for Weeks 2–8 — start it today.
- [ ] Verify the ⚠️ items for quick-win rows you'll ship this week (reviewer-name claims,
      same-week wording, on-site amenities — ask ops; drop any claim you can't verify today,
      ship the row anyway with the safe wording).

### Day 2 (Wed) — **Batch 1: SPINE titles/metas** (rows 1–10 of `quick-wins-title-meta.md`)
ACDF · cervical fusion · lumbar laminectomy · microdiscectomy · broken neck · back fracture ·
spondylolisthesis · spine pillar · thoracic/lumbar decompression · Southfield spine-neck.
- [ ] Enter titles/metas in Rank Math exactly as approved; **nothing else on those pages.**
- [ ] Log in `seo/change-log.md` + same-day GSC annotation ("Batch 1 spine titles 2026-07-23").
- [ ] Mobile spot-check 3 of the 10 on a real phone; if stale → ping Paul, note in log.
- **Why first:** ACDF alone is 21K impressions at position 3 with 4 clicks. This is the single
  fastest spine-demand recovery available anywhere on the site. ~Half a day of work.

### Day 3 (Thu) — **Batch 2: brand-bridge + biggest site-wide gaps** (rows 11–15)
Contact · company history ("Mendelson Kornblum Is Now Synergy") · legacy Mendelson post ·
flying-with-joint-replacement · lymphedema.
- [ ] Same discipline: implement → log → annotate → mobile spot-check.

### Day 4 (Fri) — **Batch 3: remaining quick wins** (rows 16–25, skipping any unverified ⚠️)
- [ ] Ship, log, annotate. All 25 rows are now live ≤ Day 4. **Do not touch them again for
      14 days** no matter how tempting.
- [ ] 30-min Friday ritual (every week from now on): GSC UI → filter to this week's shipped
      URLs → eyeball only (no reactions before the 2-week read). Update Joe in 5 bullets max.

### Days 4–5 — start the spine content engine (the "2 spine pages this week")
- [ ] Draft hub rebuild #1: **`/conditions/spondylolisthesis/`** (closest to ranking: pos 10.6,
      already 274 AI citations). Draft in this workspace with the cluster map loaded — never a
      bare chat window. Standards: cluster map §3 (Grade 6–8, FAQ block, symptom-aware entry,
      spine differentiation, insurance block, one booking CTA, reviewer + date placeholder).
- [ ] Draft hub rebuild #2: **`/conditions/spinal-stenosis/`** (pos 18.9; the flagship hub).
- [ ] Friday: both drafts → medical review queue. **Nothing publishes without sign-off.**

## WEEK 2 (Jul 29–Aug 4) — hubs 3–5 + the proven-demand treatment pages

- [ ] Publish hubs #1–2 as reviews clear; internal links per cluster map §2 (up to pillar,
      across to 2–3 siblings, down to learning hub, out to surgeon bios + locations).
- [ ] Draft hubs #3–5: **`/conditions/herniated-disc/`** (18.2) · **`/conditions/cervical-radiculopathy/`**
      (16.1, 276 AI citations) · **`/conditions/sciatica/`** (15.8). → review queue.
- [ ] **Harden the AI monster:** `/conditions/neck-fracture-broken-neck/` (23% of ALL AI
      visibility) — named reviewer, review date, "call 911 / go to the ER now if…" banner up
      top, FAQ block. Same for back-fracture. These are drafts → review → publish.
- [ ] **ACDF content rebuild** on the existing page (keep URL until Cardinal confirms
      structure): rewrite to §3 standards — this is where 21K impressions/16mo are waiting.
- [ ] Learning-hub articles 1–2 (cadence = 2/week from here): **"Laminectomy recovery
      week-by-week"** (query already sits at pos 6.3) and **"Do I need surgery for spinal
      stenosis?"** → review queue.

## WEEK 3 (Aug 5–11) — ACDR + laminectomy + Troy

- [ ] Publish hubs #3–5 + learning-hub 1–2 as reviews clear.
- [ ] **NEW page: `/treatment/cervical-disc-replacement-acdr/`** — ~10K impressions of "acdr"
      demand with no page. FIRST: Joe confirms which surgeons actually perform ACDR
      (credential accuracy — blocking). Companion learning-hub: **"Fusion vs. disc
      replacement"** (decision-stage, clicks).
- [ ] **Laminectomy content merge:** best copy from the 87K-impression `/specialties/` page
      rewritten into **`/treatment/lumbar-laminectomy/`** (AI-preferred, pos 10.1). Publish
      improved page; **no redirect yet** — that waits for the gate + Wave-1 data.
- [ ] **Troy spine page** (location layer #1 — the Oakland County unlock; 788 impressions of
      current footprint): surgeons who sit there, same-week availability (verify!), directions,
      insurance, local FAQs, "communities we serve: Clawson, Madison Heights, Royal Oak…".
- [ ] Learning-hub 3–4: **"Signs your back pain needs a specialist"** · **"What happens at a
      first spine visit?"**

## WEEK 4 (Aug 12–18) — first data read + DDD + Sterling Heights

- [ ] **Day 14+ read of Batches 1–3** (script + GSC UI): CTR deltas per row → 5-bullet note to
      Joe. Rows that moved: leave alone. Rows flat where Google shows a *different* title in
      the SERP: iterate once, log as Batch 4. Rows flat otherwise: wait to Day 28.
- [ ] Rebuild **`/conditions/degenerative-disc-disease/`** (last of the 5 hubs).
- [ ] **Sterling Heights + Livonia spine pages** (copy the Troy template).
- [ ] Learning-hub 5–6: **"Herniated disc: when it heals on its own"** · **"Injections before
      surgery: the conservative path."**
- [ ] If Cardinal has confirmed structure: hand them the §4/§4a consolidation list as the
      formal redirect ticket (they execute; you verify content parity first).

## WEEKS 5–8 (Aug 19–Sep 15) — consolidate, then the revision cluster

- [ ] **Consolidations execute** (Cardinal ships redirects; you: content parity check before,
      rank watch after — never 301 a page-1 URL into a weaker one without moving content first).
      Order: microdiscectomy → laminectomy → SI fusion → kyphoplasty → condition-hub legacy
      variants → medial branch blocks. One topic per batch, logged.
- [ ] **Revision/returning-patient cluster** (cluster map §5A — the CEO's target patient,
      currently zero presence): `/treatment/revision-spine-surgery/` + `/conditions/failed-back-surgery/`
      + `/conditions/adjacent-segment-disease/` + second-opinion learning-hub set. Surgeon
      review is non-negotiable here; tone rules per §5A.
- [ ] Remaining spine-at-location pages (Southfield refresh, Rochester).
- [ ] **Aug 30 = Gate 1.** Your contribution to the gate review: Wave-1 CTR deltas, hubs
      published + indexed count, spine non-branded impressions trend vs the 66.7K baseline.

## WEEK 9+ (Sep) — second wave from fresh data

- [ ] **Sep 1: full monthly export** (both views) → `seo/data/2026-09-01*/` → run both
      scripts → compare vs July baseline → pick title/meta Wave 2 + next striking-distance
      targets from what the data says THEN (don't pre-plan it now).
- [ ] Day-28 read on everything shipped in Aug; iterate flat rows once.
- [ ] Port Huron + "orthopedic urgent care" opportunities with the 20% non-spine time.

---

## Every week, without exception
**Mon:** pick the batch, verify ⚠️ facts, draft. **Wed:** ship what's approved, log, annotate,
mobile-check. **Fri:** 30-min data eyeball + 5-bullet update to Joe + push drafts to review
queue. **Always:** 80% spine · one batch = one theme · nothing publishes without its reviewer ·
nothing gets edited twice inside its 14-day window.

## Your scoreboard (so you're measured on the right things)
| Metric | Baseline (Jul 21) | Expect movement |
|---|---|---|
| Wave-1 pages CTR | per-row in quick-wins file | 2–4 weeks |
| Spine non-branded impressions | 66,738 /16mo (~1,500 commercial) | 6–12 weeks after hubs publish |
| Spine non-branded queries appearing | 48 | 150+ by Oct |
| Hubs published to §3 standard | 0 of 5 (+ACDF, ACDR) | 5 by Aug 18 |
| AI citations of rebuilt hubs | radiculopathy 276 / spondylo 274 | watch monthly, no target yet |
| Ortho tripwire (non-branded clicks) | 746 /16mo pace | must NOT drop >15% 2 months running |

Clicks are the proxy; **Liine-qualified spine calls are the business KPI** — that plumbing is
workstream D in the 90-day plan, not yours, but flag Joe if pages convert clicks and calls stay flat.

## If you're blocked
Reviewer slow → keep drafting, escalate to Joe at 5 business days; never publish around the
gate. Cardinal silent on structure → everything above still proceeds EXCEPT redirects; re-ask
weekly. Mobile bug unfixed → keep shipping, verify desktop, note "mobile unverified" in the
log, escalate week 2. Rank Math/access issues → Paul. Anything ambiguous → the cluster map
decides; if it doesn't, ask Joe rather than improvising a new URL or topic.

## Never (recap — these burned us)
One-page GPT edits with no cluster context · new URLs for topics that have a primary ·
**creating or shipping ANY redirect yourself — redirects are Cardinal's to execute, and only
after the §4a structure gate clears** · suburb/doorway pages (decided: real clinics only) ·
redirecting the legacy Sterling Heights or Port Huron URLs · touching ortho architecture,
provider-page structure, or the big legacy blogs beyond approved titles/metas · publishing
clinical copy without a named reviewer · promising speed scheduling can't deliver ·
SEMrush-driven decisions.
