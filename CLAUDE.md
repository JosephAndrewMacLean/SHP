# Synergy Health Partners — Marketing Workspace

This repository is the marketing workspace for **Synergy Health Partners (SHP)**, a
healthcare organization. It contains a team of specialized marketing subagents.

## Context for every task

- **Read `brand/brand-brief.md` and `brand/current-state.md` first.** The brief is the
  source of truth for brand, voice, audience, and compliance guardrails. `current-state.md`
  is the ground truth from the June 2026 audits (Organic/AIO, Creative/UX, Paid Media):
  who Synergy actually is, the numbers, the gaps, what external agencies already own, and
  where this in-house team has white space. Don't duplicate work the agencies own —
  complement it.
- **The Cardinal (June 2026) audits anchor all measurement and opportunity work.** The
  extracted audit texts live in `audits/cardinal-2026-06/`; the live status ledger —
  every Cardinal recommendation, its verified website status, and the instrument that
  measures it — is **`audits/cardinal-recommendation-tracker.md`**. Frame findings as
  "status against Cardinal's recommendation X," and update the tracker when you verify
  something new. Note: this environment's network policy blocks fetching synergyhealth.org
  directly — verify site state via Semrush (project "SHP Spine 2026", ID 30453033),
  GA4, or GSC instead.
- This is **healthcare marketing**. Non-negotiables on all work:
  - No PHI or unconsented patient stories (HIPAA).
  - No unsubstantiated health claims or superiority claims (FTC).
  - E-E-A-T / YMYL rigor: cite credible sources, credentials, medical review, dates.
  - Accessibility and non-discrimination (Section 1557 / ADA / WCAG AA).
  - Anything clinically or legally substantive is a **draft pending human review** —
    never present it as cleared to publish.

## The team (`.claude/agents/`)

- `marketing-director` — strategy & orchestration; start here for multi-discipline asks.
- `pr-specialist` — public relations, media, reputation, crisis.
- `guerilla-marketing-specialist` — low-cost, high-creativity local/experiential.
- `seo-specialist` — traditional organic search.
- `aeo-specialist` — answer engines / featured snippets / voice.
- `geo-specialist` — generative engines (ChatGPT/Perplexity/Gemini citations).
- `aio-specialist` — Google AI Overviews / in-search AI answers.
- `content-creator` — the content engine feeding all of the above.

## Analytics data (GA4 via MCP)

- The official Google Analytics MCP server is configured in `.mcp.json` (tools appear
  as `mcp__google-analytics__*`: `get_account_summaries`, `run_report`,
  `run_realtime_report`, …). **Use it to ground any claim about page, channel, or
  content performance in real GA4 numbers — current and historical — instead of
  assuming.** Typical use: `run_report` with page/landing-page dimensions over the
  date ranges being compared.
- SHP GA4 property ID: **370514163** ("SHP - New Site - GA4", under account 24916876
  "Synergyhealth.org - New June 2024"). Verified working 2026-07-22. GA4 data begins
  **2023-04-20** — no earlier history exists in this property.
- The specialist subagents have restricted tool lists and don't get MCP tools: pull
  GA4 data in the main session and pass the relevant numbers into subagent prompts.
- If the GA tools are missing, the credential isn't set up in this environment —
  see `docs/google-analytics-mcp-setup.md`.
- **Also connected:** Semrush MCP (`mcp__Semrush__*` — site audit, rankings, backlinks,
  SERP/AIO features) and Google Search Console MCP (`mcp__google-search-console__*` —
  live since 2026-07-22; `search_analytics` is the workhorse). A `PAGESPEED_API_KEY`
  env var (CWV field data) is available in sessions started after 2026-07-22.
  Full source map: `docs/data-sources-roadmap.md`.

## Turning data into opportunities for clinical stakeholders

A primary use of the GA4 / Search Console data: find **low-hanging-fruit page
opportunities** and package them for people who have clinical knowledge but no SEO
or digital-marketing background (physician partners, clinical reviewers). For those
briefs:

- **Plain language only.** Say "people who found us on Google," not "organic
  sessions"; "stayed and read," not "engagement rate." Define any number shown.
- **Lead with the patient/practice outcome** ("patients searching spinal stenosis
  never see this page"), then the evidence, then the ask.
- **Make the ask small and concrete** — confirm a clinical fact, review a title,
  approve a paragraph. Never "help us with SEO."
- Clinical reviewers own accuracy and priorities; marketing mechanics stay with
  this team.

## Working norms

- Deliver prioritized, implementation-ready work — not aspirational decks.
- State when you're working from assumption vs. confirmed SHP facts, and flag gaps
  in `brand/brand-brief.md` that would improve the output if filled in.
- Coordinate across disciplines: content feeds SEO/AEO/GEO/AIO; PR and guerilla
  create the amplification and third-party corroboration.
