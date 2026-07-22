# Synergy Health Partners — Knowledge Map (all systems, one index)

**Purpose:** every Synergy marketing conversation, file, and data source in one place, so any
session (or human) can find prior work instead of rediscovering it.
**Privacy rule (standing):** this index and everything it links covers **Synergy Health
Partners business only**. Personal conversations and non-Synergy matters are deliberately
excluded and must never be added to this repo, its documents, or its indexes. When in doubt,
leave it out. *(Maintained: Jul 22, 2026.)*

---

## 1. This repo (the master filing cabinet)

| Folder | What it holds |
|---|---|
| `brand/` | Ground truth: brand brief, current-state (June 2026 audit synthesis + internal data), provider roster |
| `playbooks/` | Strategy: master game plan, spine 90-day plan, spine patient acquisition, B2B liaison, call center, ideas bank |
| `seo/` | The SEO program: GSC + AI-features analyses, spine cluster map, quick wins, Randall's execution plan, crawl review, medical-review guide, workflow, change log, dated data exports, Title & Meta Studio source |
| `pm/` | Project management: task lists, target accounts, intake scripts, meeting agendas |
| `decisions.md` | Dated log of every leadership decision — check before re-opening any settled question |
| `sources.md` | This file |

**Folders that exist only in unmerged branches** (see §2): `docs/` (data-sources roadmap,
GA4/Liine specs), `audits/` (Cardinal recommendation tracker, rater8 baseline), `hiring/`
(JDs), `data/rater8/` (GBP scorecards).

## 2. The 14 conversation branches (unmerged parallel work — the fragmentation problem)

Each Claude conversation works on its own branch; **work is invisible to other sessions until
merged**. Status as of Jul 22:

| Branch (short name) | What it contains | Size | Note |
|---|---|---|---|
| **content-desktop-mobile-sync** | THIS branch: the entire `seo/` program (PR #3) | 25 files | Ready to merge |
| **synergy-marketing-team-setup** | The de-facto master: brand docs, playbooks, agents | base | PR #3's target |
| **routing-clinical-intelligence-process** | ⚠️ **Overlaps seo/**: spine website game plan, page templates, semantic model, location-intent roadmap, its own Randall task list, Mitch's review answers, paid-search analysis, frozen 7/22 spine baseline | 30 commits, 3.6K lines | **Reconcile with seo/ before Randall works from either** |
| **b2b-physician-spine-accounts** | Referral engine: 809-row scored target-account CSV, Kristen's canonical deck, visit cadence v2, Joel validation | 18 commits, 5.9K lines | Edits shared files (current-state, 90-day plan) |
| **rater-8-gmb-profiles** | Reputation/local: rater8 exports, GBP profile directory, review-velocity baseline | 11 files | Feeds hyperlocal + AIO |
| **session-fssj54** | Bing Webmaster verified live (486d history, same CTR failure pattern); GBP estate notes | 2 commits | Overlaps rater8 branch's GBP notes |
| **ga4-event-filters** | Liine→GA4 event filter specs | 3 files | |
| **google-analytics-mcp** | GA4 MCP connection (property 370514163) + setup docs | 6 files | Edits CLAUDE.md — merge-conflict risk |
| **bing-query-stats** | Data-sources roadmap updates (Bing AEO/GEO) | 1 file | `docs/data-sources-roadmap.md` is edited by **5 branches** — resolve once |
| **spine-imaging-pain-scheduling** | MRI×Spine×Pain journey: call-review pack, Kelley/Mitch meeting materials | 3 files | |
| **marketing-meeting-agenda** | 7/22 marketing meeting agenda + NP week tracker | 3 files | |
| **team-performance-budget** | NP-growth fix-now matrix (7/22) | 2 files | |
| **zocdoc-visit-reasons-removal** | Zocdoc visit-reason removal memo + Enterprise email | 3 files | |
| **job-description-gautam** | Hiring: Marketing Technology Analyst + Digital Marketing Specialist JDs | 6 files | |

**Merge plan (recommended):** small/clean ones first (zocdoc, team-performance, meeting-agenda,
hiring, spine-imaging, bing, ga4, session-fssj54, google-analytics-mcp, rater8 — resolving the
data-sources-roadmap and GBP-notes overlaps once), then **b2b-physician** (shared-file
conflicts), then **routing-clinical-intelligence** only after its spine plans are reconciled
with `seo/` into one Randall workstream.

## 3. Shareable assets (claude.ai artifacts — source copies live in this repo)

| Asset | URL | Source |
|---|---|---|
| Randall — SEO Execution Plan | claude.ai/code/artifact/e9ae1729-8bd2-44d7-aa19-325e425d3f6d | `seo/randall-execution-plan.md` |
| Spine Content Review — Reviewer's Guide (physicians) | claude.ai/code/artifact/98c3df89-d2cc-4fcd-9f36-bb3b78af4a08 | `seo/medical-review-guide.md` |
| Title & Meta Studio (interactive tool + guided tour) | claude.ai/code/artifact/6fc806e0-af28-420a-9f51-b05407ebadaf | `seo/tools/title-meta-studio.html` |

Artifacts are private until Joe shares them from the page's share menu.

## 4. Notion (Synergy pages — titles, dates)

Core documents:
- **Insurance Page — Content Spec & Copy** (Feb 2026) — the payer taxonomy source of truth (29 carriers; Medicaid varies by provider)
- **2026 Budget — Synergy Health Partners** (Sep 2025) — channel splits, spine NP budget
- **Web Dev Handoff — ZocDoc URLs, Insurance Pages & Site Structure Notes** (May 2026)

Meeting notes (@-dated pages, Jul 2026 series): SEO Strategy Meeting — Spine Content Plan
(Jul 21) · Randall's 4 spine SEO pages task (Jul 20) · Spine-doctor referral scheduling
(Jul 20) · Marketing & Rebranding Strategy (Jul 15) · Troy Location Marketing & Ops (Jul 15) ·
SEO data-collection/content-creation walkthrough (Jul 16) · Spine Marketing Analytics & B2B
Visit Tracking (Jul 13) · Marketing Attribution & Partnership Planning (Jul 9) · Kristen /
physician-liaison background (Jul 8). Earlier: Synergy explainer-video notes (Jan 8) ·
Synergy marketing what-has-worked notes (Mar 4).

*Search Notion for "Synergy" to pull any of these; IDs resolve via notion-search.*

## 5. Otter (Synergy meeting recordings — the leadership record)

**Anchor meetings for the current program:**
- **Spine Division Strategy Meeting — Jul 21, 2026 (2h52)** — otter.ai/u/kwneayOjfWdTMQXCKLwmDw7y888
  The source of the SEO reset (Paul/Randall canonical-content conversation), plus: Kristen's
  848 spine-adjacent B2B accounts split into 3 cohorts; Katie's Axle scheduling tool (OR
  utilization 58%→78%); Mitch's physician practice-pattern coaching; **Anna's rebuild
  presentation due Aug 1 for a Sept 1 go-live**; Paul granting Randall full Synergy Content
  settings access; Joe's action items (spine workflow-phase timelines; integrated spine web
  content with Mitch — endoscopic, SI fusion, bone-bag/T-Lift procedure pages; landing pages
  with testimonials + patient-story videos).
- **Compliance & Marketing Strategy — Apr 7, 2026 (1h57)** — otter.ai/u/8LAi-RYc_mTNRmXFxmYBdpup6LM
  New AI-powered website launch decision (launched that Thursday — the migration `seo/crawl-review-2026-07.md` documents), Q2 target 4,408 NPs, 71 spine orders/month.
- **Marketing Strategy Meeting — Feb 13, 2026 (2h19)** — otter.ai/u/RLG7D-Is_ULHCIVPJeLTfKTf64U
  Same-week USP, Troy launch marketing, scheduling constraints, referral/fax workflow.
- **Team Performance Evaluation — Jul 14, 2026 (2h)** — otter.ai/u/StkrbdVkVKsP5Ye3UwpMi_Ec8WY
  Kristen's B2B team 12-month flat growth review (context for the realistic referral plan).

**Weekly NP/ops series (performance numbers over time):** Feb 3 · Feb 10 (spine surgery
process) · Apr 6 · Apr 14 (×2: alignment + surgical orders) · Apr 21 (×2: NP growth +
team collaboration) · May 11 · May 26 · Jun 1 · Jun 2 (quarterly revenue/ASC shortfall) ·
Jun 8 · Jun 10 (Liine implementation, "Recording 100") · Jun 23 · Jul 8 (patient data
targets) · Jul 9 (ortho scheduling). *Search Otter for "Synergy spine" + date to pull any.*

*Excluded from this index by the privacy rule: non-Synergy conversations and sensitive
personnel sessions. Do not add them.*

## 6. External systems (where live data lives)

| System | What | Access/notes |
|---|---|---|
| Google Search Console | Organic + AI-features performance | Monthly exports → `seo/data/` (Jul 21 baseline in) |
| WordPress + Rank Math (synergyhealth.org) | The live site; titles/metas entered here | Site migrated to new URL structure (see crawl review) |
| Paul's "Synergy Content" backend | AI content generation w/ GSC integration | Account moving to Joe; Randall granted full access (Jul 21) |
| GA4 | Web analytics, property 370514163 | MCP connection built in `google-analytics-mcp` branch |
| Bing Webmaster Tools | Verified live, 486 days history | Notes in `session-fssj54` branch |
| Liine | Call tracking / qualified leads (source of truth for conversions) | Tracking validation = 90-day plan workstream D |
| rater8 | Reviews/reputation per provider + GBP | Exports in `rater-8-gmb-profiles` branch |
| Map My Customer | Physician-liaison CRM | B2B branch work |
| NextGen / OrthoPlex | EMR / scheduling (NP source of truth) | Ops-owned |
| Zocdoc | Booking channel (being de-emphasized per data) | Removal memo in `zocdoc` branch |
| Notion / Otter | Docs + meeting record | Indexed above (§4–5) |

## 7. How to keep this map alive

End every working session by asking: did this session create a decision (→ `decisions.md`),
an asset (→ §3), a data pull (→ dated folder), or a new source (→ §6)? Update the line here.
Merge the branch. One cabinet, one master copy.
