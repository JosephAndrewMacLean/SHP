# SHP Spine Growth — Project-Management Ecosystem (Google Sheets)

A self-building operating system for the spine game plan: **granular tasks in a hierarchy, assigned
by owner and authorizer, with time estimates, a live process tracker, and an evidence-based Ideas
Bank scored by impact/effort/cost.**

## Files here
- **`SHP-PM-Ecosystem.gs`** — Apps Script that builds the entire multi-tab ecosystem. This is the install.
- **`master-task-list.csv`** — the full task hierarchy (16 parent tasks → 63 granular subtasks) as data.
- **`ideas-bank.csv`** — 28 evidence-based ideas with impact/effort/cost.
- **`heyl-launch-tasks.csv`** — the Dr. Jonathan Heyl (Pain Medicine) launch: 10 tasks → 63
  subtasks, ~293 est. hours, same schema as `master-task-list.csv` so the rows paste straight
  into **Master Tasks**. Randall's working checklist is
  `playbooks/heyl-launch-randall-todo.md`; the data and rationale behind it are in
  `playbooks/heyl-launch-reference.md`.

## Install (5 minutes)
1. Create (or open) a Google Sheet — or use the one already created in your Drive:
   **"SHP — Spine Growth Operating System."**
2. **Extensions → Apps Script.** Delete any default code.
3. Paste **all** of `SHP-PM-Ecosystem.gs`. **Save.**
4. Run **`buildEcosystem`** once and authorize when prompted.
5. Reload the Sheet. A **"SHP PM"** menu appears. Done — 7 tabs are built.

## The tabs
| Tab | What it does |
|---|---|
| **README** | The operating rhythm (Mon/Wed/Fri) and how to update tasks |
| **Dashboard** | Process tracker: effort-weighted % done, needle-mover progress, health (On Track/At Risk/Behind), owner load |
| **Master Tasks** | The hierarchy — shaded **Task** rows auto-roll-up from their **Subtasks** (Est, % done, Actual, Health) |
| **Ideas Bank** | Evidence-based ideas scored Impact/Effort/Cost with an auto **Quadrant**; promote winners to tasks |
| **Weekly Spine Scorecard** | Enter weekly actuals (yellow cells); attainment vs the 65→72 ramp auto-calculates |
| **Decisions & Blockers** | Open leadership decisions + the Line-tracking blocker |
| **By Owner** | Filter tasks by owner; "Generate owner tabs" makes one per person |

## How the machine runs (weekly)
- **Mon** — Dashboard review; clear **Blocked** + **Overdue** first; confirm this week's owners/tasks.
- **Wed** — Unblock/re-route; promote 1–2 **Ideas Bank Quick Wins** into Master Tasks.
- **Fri** — Fill the **Weekly Spine Scorecard**; run the OODA read (activity vs output vs efficiency).
- Every task has an **Owner** (does it) and an **Authorizer** (approves it). Nothing ships without its authorizer.

## Updating a task
Edit the **Subtask** row: set **Status**, type **% Done** (0–100) and **Actual Hours**. The parent
**Task** row rolls up automatically, and **Health** flags itself (Behind if past due; At Risk if
over-estimate or due ≤3 days & <50%). Then **SHP PM → Refresh dashboard**.

> Rebuilding (SHP PM → Build/Rebuild) is safe — it preserves your Status / % Done / Actual Hours
> edits by matching task ID.
