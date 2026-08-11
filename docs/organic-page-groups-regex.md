# Organic page-group regexes — GSC & Bing

Purpose: one saved filter per page group so clicks/impressions can be tracked per group —
and so the effect of the URL consolidation (see `data/redirect-map-2026-08-11.csv`) shows up
as a before/after trend instead of an anecdote. Built and validated 2026-08-11 against the
full page inventory (`data/synergyhealth-page-inventory-2026-08-11.csv`).

## The regexes (Google Search Console)

GSC UI: **Performance → + New → Page… → Custom (regex)**. API/MCP: `pageFilter` with
`filterOperator: includingRegex`. GSC regex is RE2 and case-sensitive; site URLs are
lowercase so that's fine (prefix `(?i)` if you ever need case-insensitive).

| Group | Regex |
|---|---|
| Conditions | `^https://synergyhealth\.org/conditions(-we-treat)?/` |
| Specialty | `^https://synergyhealth\.org/specialt(y\|ies)/` |
| Treatment | `^https://synergyhealth\.org/treatment(s\|-type)?/` |
| Providers | `^https://synergyhealth\.org/(our-)?providers/` |

Each pattern intentionally covers **both the current and the legacy/parallel structure** for
its group (`/conditions/` + `/conditions-we-treat/`, `/specialty/` + `/specialties/`,
`/treatment/` + `/treatments/` + `/treatment-type/`, `/providers/` + `/our-providers/`), so
group totals stay comparable before, during, and after consolidation.

**Spine cross-section** (any spine-topic URL sitewide, incl. blog, plus every provider on the
spine bench from `brand/provider-roster-by-service-line.md`):

```
^https://synergyhealth\.org/[^?#]*(spine|spinal|neck|cervical|lumbar|thoracic|sciatica|scolio|spondyl|stenosis|herniat|kyph|vertebr|radicul|myelopath|laminect|laminoplast|discect|diskect|foraminot|facet|epidural|sacroiliac|coccy|whiplash|caudal|[-/]back[-/]|[-/]disc[-/]|[-/]disk[-/]|[-/]si[-/]|[-/]esi[-/]|varghese|salar|maslak|mccarty|zamorano|munk|oddo|kassa|elwart|truscott|langholff|taher|kornblum|fiani|kevin-r?-?lee|hanish-singh|sue-cash)
```

To scope spine to one group, swap the `[^?#]*` wildcard for the group prefix, e.g. spine
conditions only:
`^https://synergyhealth\.org/conditions(-we-treat)?/[^?#]*(spine|spinal|neck|…)` .

### Validation (Google, last 90 days: 2026-05-11 → 2026-08-10, aggregation byPage)

Regex-filtered GSC API totals matched the inventory's per-page sums **exactly** for
Conditions, Specialty, and Treatment; Providers was +154 impressions (0.08%) from
pagination/`/embed/` junk URLs deliberately excluded from the inventory. Spine flags agree
with the inventory's `spine_related` column with zero false positives/negatives.

| Group | Clicks | Impressions | CTR | Avg position |
|---|---|---|---|---|
| Conditions | 394 | 178,643 | 0.22% | 13.1 |
| Specialty | 147 | 36,180 | 0.41% | 29.6 |
| Treatment | 637 | 262,267 | 0.24% | 12.1 |
| Providers | 4,978 | 191,672 | 2.60% | 8.9 |
| Spine (sitewide) | 2,373 | 215,106 | 1.10% | 9.6 |

Read of the numbers: provider pages earn 4,978 clicks — ~4× the three clinical groups
combined (1,178) — on fewer impressions. Clinical pages have the reach (441K impressions)
but ~0.2% CTR: Cardinal's generic-title/thin-content finding, compounded by each topic's
impressions being split across duplicate URLs.

## Bing Webmaster Tools

Bing's UI (Search Performance / Page Traffic) has **no regex filter** — only
contains/equals. Two options:

1. **UI approximation** — "URL contains" filters that map 1:1 to the groups above
   (the `org/` prefix keeps them anchored to the start of the path):

   | Group | Bing "URL contains" |
   |---|---|
   | Conditions | `org/conditions` |
   | Specialty | `org/specialt` |
   | Treatment | `org/treatment` |
   | Providers | `providers` |

   Spine can't be expressed as a single contains-filter — use option 2.

2. **Exact parity** — export Page Traffic (or query the Bing Webmaster API) and apply the
   exact regexes above to the URL column: Google Sheets `REGEXMATCH()` is RE2 (same engine
   as GSC); Excel 365 `REGEXTEST()` also accepts these patterns. Drop the
   `^https://synergyhealth\.org` prefix and match on paths (`^/conditions(-we-treat)?/` …)
   if the export contains bare paths.

Note: a `bing-webmaster` MCP server is configured for this workspace but did not connect in
the 2026-08-11 session, so Bing numbers aren't pulled here. When it connects, pull page-level
stats and apply these same regexes programmatically, exactly as done for GSC.

## Cleanup & redirect map

`data/redirect-map-2026-08-11.csv` — 159 source → destination rows, grouped into five
cleanup areas (each row carries reason, confidence, and the traffic at stake):

| Area | Rows | What it is |
|---|---|---|
| A. Duplicate content — parallel structures | 71 | Same topic live at 2+ URLs (841K impressions/16mo across sources). Keep the URL Google already prefers; 301 the rest. |
| B. Dead URL → live equivalent | 25 | 404s with an obvious live twin (renamed slug, `/null/` children, `/treatments/`). |
| C. Departed providers | 35 | 404 profiles (Kornblum, Fiani, Abiola, Babushkina…) → live specialty directory or `/providers/`. |
| D. Dead URL → topical fallback | 23 | No true equivalent; nearest live topical page. All flagged Review. |
| E. Structure/index governance | 5 | Index-level calls (`/our-providers/`→`/providers/`, `/conditions-we-treat/`→`/conditions/`, `/specialty/` vs `/specialties/`, `/treatment-type/`) — Cardinal's "URL taxonomy governance" item. |

127 rows are mechanical (High confidence); 32 need human review. Chains are pre-flattened
(no destination is itself redirected). Winners were chosen by current performance
(90-day impressions, then 16-month clicks, then GA4 views) — in most pairs Google has
already migrated to the winner on its own (e.g. `/conditions/` now takes ~99% of conditions
impressions vs `/conditions-we-treat/`).

Deploy notes:
- **Draft pending review** — SEO/dev must approve before implementation, per Cardinal's
  taxonomy-governance recommendation; Review-flagged rows especially.
- Ship area A high-impression rows + area E's `/our-providers/`→`/providers/` first;
  update internal nav/GBP links that still feed `/our-providers/` (15.9K GA4 views/yr).
- Two destinations sit outside the inventory (`/orthopedic-urgent-care/`, marked in the
  CSV) — verify they're live before shipping those rows.
- Regenerate the XML sitemap after implementation (Cardinal: 10 404s + 17 redirecting
  URLs currently in it), then watch these regex groups for the consolidation lift.
