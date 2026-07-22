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
- **Then check `decisions.md` and `sources.md` (repo root).** `decisions.md` is the dated
  log of settled leadership decisions — do not re-litigate anything on it. `sources.md`
  maps every Synergy knowledge source: the `seo/` program, all conversation branches and
  their contents (much prior work lives on unmerged branches — check before rebuilding
  something that exists), shareable artifact URLs, Notion pages, Otter meeting recordings,
  and external systems (GSC, GA4, Liine, rater8, Bing WMT).
- **SEO/content work runs through `seo/`** — the analysis, cluster map, execution plan,
  and workflow there are binding (batched changes, change log + GSC annotation, 14-day
  freeze, no single-page GPT edits, no redirects by this team, GSC data not SEMrush).
- **Privacy rule (standing, from Joe):** this workspace covers Synergy Health Partners
  business only. Never add personal conversations or non-Synergy matters to this repo,
  its documents, or its indexes — when in doubt, leave it out.
- **End-of-session habit:** new decision → `decisions.md`; new asset/source/data →
  `sources.md`; then commit and merge the branch so the master copy stays whole.
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

## Working norms

- Deliver prioritized, implementation-ready work — not aspirational decks.
- State when you're working from assumption vs. confirmed SHP facts, and flag gaps
  in `brand/brand-brief.md` that would improve the output if filled in.
- Coordinate across disciplines: content feeds SEO/AEO/GEO/AIO; PR and guerilla
  create the amplification and third-party corroboration.
