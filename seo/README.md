# SEO Workspace — synergyhealth.org

Working area for the in-house organic program (Randall + Joe), stood up Jul 21, 2026 after the
strategy reset with Paul. **One rule above all: no page gets edited outside this system's
context** — see `content-update-workflow.md`.

| File | What it is |
|---|---|
| `gsc-analysis-2026-07.md` | Ground truth: what 16 months of Google Search Console data says (branded dependency, spine invisibility, cannibalization, quick-win math) |
| `spine-content-cluster-map.md` | The strategy: spine cluster architecture, primary-URL decisions, hyperlocal plan, new content clusters (revision patients, ACDR), ortho guardrails, roadmap |
| `quick-wins-title-meta.md` | Wave 1 implementation: 25 title/meta rewrites, drafts pending human review |
| `content-update-workflow.md` | The operating process: batches, change log, monthly GSC loop, roles, what we never do |
| `change-log.md` | Every shipped batch, dated — mirrors GSC annotations |
| `data/2026-07-21/` | The raw GSC export this cycle ran on (Web, last 16 months) |
| `data/analyze_gsc.py` | Re-runnable analysis — point it at next month's export folder |

Monthly cycle: export → `data/YYYY-MM-DD/` → run script → compare → pick batch → draft →
review → implement → log. Companion strategy lives in `playbooks/spine-90day-plan.md`
(workstream B) and the guardrails in `brand/brand-brief.md` + `brand/current-state.md`.
