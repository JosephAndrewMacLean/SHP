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

## Data sources

- **Google Analytics (GA4)** — wired in via Google's official Analytics MCP server
  (`.mcp.json` + `scripts/ga-mcp.sh`), so the team can query real page and channel
  performance, current and historical, straight from GA4 instead of assuming.
  One-time credential setup: [docs/google-analytics-mcp-setup.md](docs/google-analytics-mcp-setup.md).

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
audits/                Cardinal (June 2026) audit texts + live recommendation tracker
brand/brand-brief.md   shared brand, voice, audience, and compliance guardrails
ops/                   clinical-operations SOPs (clinic utilization, physician PTO / patient access) + change reviews
playbooks/             strategy playbooks (master game plan, spine, call center, physician liaison)
pm/                    task list, ideas bank, scripts, and PM ecosystem working files
.mcp.json              MCP servers (Google Analytics, Search Console) loaded into every session
scripts/               MCP launchers (ga-mcp.sh, gsc-mcp.sh — shared credential handling)
docs/                  setup guides + data-sources roadmap (what measures what)
CLAUDE.md              project context loaded into every session
```
