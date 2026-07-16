# Synergy Health Partners — Marketing Workspace

This repository is the marketing workspace for **Synergy Health Partners (SHP)**, a
healthcare organization. It contains a team of specialized marketing subagents.

## Context for every task

- **Read `brand/brand-brief.md` first.** It's the shared source of truth for brand,
  voice, audience, and — critically — compliance guardrails.
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
