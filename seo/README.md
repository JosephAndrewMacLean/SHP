# SEO Workspace — synergyhealth.org

Working area for the in-house organic program (Randall + Joe), stood up Jul 21, 2026 after the
strategy reset with Paul. **One rule above all: no page gets edited outside this system's
context** — see `content-update-workflow.md`.

| File | What it is |
|---|---|
| `gsc-analysis-2026-07.md` | Ground truth: what 16 months of Google Search Console data says (branded dependency, spine invisibility, cannibalization, quick-win math) |
| `gsc-ai-features-2026-07.md` | AI Overviews / AI Mode view: 315:1 citation preference for the new URL structure, neck-fracture dominance, international noise |
| `spine-content-cluster-map.md` | The strategy: spine cluster architecture, primary-URL decisions (§4 + §4a correction), hyperlocal plan (real clinics only — decided), new content clusters (revision patients, ACDR), ortho guardrails, roadmap |
| `quick-wins-title-meta.md` | Wave 1 implementation: 25 title/meta rewrites, drafts pending human review |
| `randall-execution-plan.md` | Randall's week-by-week execution checklist (starts Jul 22) — quick wins first, spine always in front |
| `medical-review-guide.md` | Physician review process: the 3-question review, accuracy checklist, expertise-boost contributions, SLA, attestation, queue |
| `content-update-workflow.md` | The operating process: batches, change log, monthly GSC loop, roles, what we never do |
| `change-log.md` | Every shipped batch, dated — mirrors GSC annotations |
| `data/2026-07-21/` | Raw GSC classic-web export (Web, last 16 months) |
| `data/2026-07-21-ai-features/` | Raw GSC "AI features" export (impressions only; data begins 2026-05-18) |
| `data/analyze_gsc.py`, `data/analyze_gsc_ai.py` | Re-runnable analyses — point at next month's export folders |

Monthly cycle: export → `data/YYYY-MM-DD/` → run script → compare → pick batch → draft →
review → implement → log. Companion strategy lives in `playbooks/spine-90day-plan.md`
(workstream B) and the guardrails in `brand/brand-brief.md` + `brand/current-state.md`.
