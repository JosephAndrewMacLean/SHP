# Synergy Health Partners — Marketing Team

A team of specialized Claude Code subagents that cover the full modern marketing
stack for Synergy Health Partners (SHP), with healthcare compliance built in.

## The team

| Agent | Discipline | Use it for |
|-------|-----------|-----------|
| **marketing-director** | Strategy & orchestration | Plan campaigns, decompose goals, delegate to the right specialist. **Start here** for anything multi-discipline. |
| **pr-specialist** | Public Relations | Press releases, media pitches, thought leadership, reputation, crisis comms. |
| **guerilla-marketing-specialist** | Guerilla Marketing | Low-budget, high-creativity local activations, stunts, experiential ideas. |
| **seo-specialist** | SEO | Organic Google rankings — keywords, site architecture, technical + local SEO. |
| **aeo-specialist** | AEO (Answer Engine Optimization) | Featured snippets, People Also Ask, voice search, direct answers. |
| **geo-specialist** | GEO (Generative Engine Optimization) | Getting cited in ChatGPT / Perplexity / Gemini / Claude answers. |
| **aio-specialist** | AIO (AI Overviews Optimization) | Being a source inside Google AI Overviews and in-search AI answers. |
| **content-creator** | Content Creation | Articles, pages, FAQs, email, social, scripts — the engine that feeds everyone else. |

## How the acronyms fit together

They're a funnel of search surfaces, from oldest to newest:

- **SEO** — rank in the classic blue links.
- **AEO** — win the featured snippet / direct answer on the results page.
- **AIO** — be cited *inside* the search engine's own AI summary (Google AI Overviews).
- **GEO** — be cited inside standalone AI assistants (ChatGPT, Perplexity, Gemini).

**Content Creation** produces the substrate all four optimize. **PR** and
**Guerilla Marketing** create the moments, links, and third-party mentions that
amplify everything — and, increasingly, the corroboration that makes AI engines
trust and cite SHP.

## How to use the team

In Claude Code, delegate to an agent by name, e.g.:

- *"Use the marketing-director to plan a Q3 campaign to grow primary-care patients in [market]."*
- *"Have the seo-specialist audit our diabetes-care pages."*
- *"Ask the content-creator to draft a patient guide on preparing for a knee replacement."*
- *"Get the geo-specialist to run a citation-gap analysis for '[condition] care near me'."*

The **marketing-director** can coordinate several specialists for a single campaign.

## Before you rely on the output

1. **Fill in `brand/brand-brief.md`.** The agents share it as their source of truth;
   right now key details are placeholders. The more real SHP specifics it has, the
   better and less assumption-driven the output.
2. **Everything is a draft pending review.** These agents follow healthcare
   guardrails (no PHI, no unsubstantiated claims, E-E-A-T, FTC/HIPAA awareness), but
   anything clinically or legally substantive must get human medical/legal sign-off
   before it's published.

## Structure

```
.claude/agents/        the eight specialist agents
brand/brand-brief.md   shared brand, voice, audience, and compliance guardrails
CLAUDE.md              project context loaded into every session
```
