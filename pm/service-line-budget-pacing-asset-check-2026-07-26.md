# Service-Line Budget & Pacing — Asset Check (2026-07-26)

> Triggered by a voice-memo note listing four assets for a service-line budget/pacing
> analysis: the clinic capacity report, the Power BI future-new-patient report, GA4 +
> Google Ads data, and service line goals/budget/pacing. This is an inventory of what's
> actually reachable from this workspace right now, so the real gaps are named before
> building anything on top of them.

## What's confirmed available

**Service line goals & budget** — documented, not just verbal:
- Notion "2026 Budget - Synergy Health Partners": spine baseline ~150/mo (2025) →
  **321/mo by end of 2026**, broken out by hub — Livonia 90–100/mo, Sterling Heights
  80–90/mo, Southfield 20–25/mo, Port Huron 10–15/mo.
- `playbooks/master-game-plan.md` (this repo): working figure **317/mo (72/wk)** for
  spine, ortho held at **130–140/wk**. Flagged there as an open reconciliation item
  (317 vs. 321) — still unresolved as of this check.
- Current pacing (from the Notion "Consolidated Priority To-Do," last updated
  2026-07-26): **spine is -80 behind budget month-to-date; ortho is +64 over.** Spine is
  the active bottleneck.

**GA4 + Google Ads** — live, campaign-level:
- GA4 MCP (`mcp__google-analytics__*`) is wired and verified (property 370514163).
- Google Ads links to GA4: campaign cost/clicks/sessions are queryable (e.g. last-30d
  Ortho Livonia ~$73.9k, Spine Livonia+SH ~$82.9k, per `pm/ads-owner-questions-2026-07-22.md`).
- **Not available:** Ads settings-level data (conversion-action values, quality score,
  search terms) — needs the official Google Ads MCP with a Blue Ox-issued developer
  token, per `docs/data-sources-roadmap.md` §3. Not yet wired.

## What's named but not actually reachable

**Clinic capacity report** — the only matching file found (Google Drive title search)
is `Synergy Demand and Capacity Planning Tool v2.xlsx` (created 2026-07-17, owned by
mendelsonortho@gmail.com). **Its content is empty** — `read_file_content` returns
nothing. An older `Clinic Capacity - October` sheet exists but is 9+ months stale.
There's a live capacity view in Notion ("Week of July 13, 2026 — Demand & Capacity
Huddle," a weekly service-line/provider slot scorecard) but it's a single dated
snapshot (last refreshed July 9), not a connected feed.

**Power BI future-new-patient report** — no exported file exists in the connected
Google Drive or Notion workspace. Power BI is named once, in passing, as one system in
the Orthoplex/AutoFlow/E-intake stack (Notion note, 2026-07-15) — not as a report
we have access to. No Power BI API/export connector is configured in this repo's
`.mcp.json`.

## What this blocks

A real budget-vs-pacing analysis needs actual (not stale, not empty) capacity and
future-NP-forecast numbers to compare against the GA4/Ads demand-generation data and
the 321-vs-317 targets above. Right now that comparison can only be built from the
Notion snapshot (dated July 9) plus the qualitative pacing already tracked in the
Consolidated Priority To-Do — not from a live capacity/forecast source.

## Ask

1. Share a populated capacity export (CSV/xlsx of current provider/day slot data) —
   the v2 tool exists but is empty; either re-share it filled in or point to the
   source it should pull from.
2. Either export the Power BI future-new-patient report on a recurring basis into this
   workspace, or grant read access so it can be pulled directly.
3. Confirm the 317 vs. 321 spine target reconciliation (flagged open in the master
   game plan since mid-July) so pacing math has one number to run against.
