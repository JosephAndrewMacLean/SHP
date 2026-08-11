# Extracted datasets

## `redirects-ready-to-implement-2026-08-11.csv`

The 127 **High-confidence** rows from the redirect map below, as a two-column
(source, target) path CSV importable straight into the WordPress Redirection plugin.
All targets verified live, no chains, no dupes; covers ~972K historical impressions.
The 32 Review rows are NOT in this file — resolve them in `redirect-map-2026-08-11.csv`
first. Implementation checklist: import as 301s → update internal nav/GBP links that
point at `/our-providers/` → regenerate the XML sitemap → watch the group regexes in
`docs/organic-page-groups-regex.md` for the consolidation lift.

## `redirect-map-2026-08-11.csv`

Draft 301 map (159 rows) consolidating the parallel URL structures and dead URLs found in
the page inventory below: source, destination, cleanup area (A–E), reason, confidence
(High = mechanical, Review = needs human judgment), and the GSC traffic at stake on each
source. Winners picked by current performance (90d impressions → 16mo clicks → GA4 views);
chains pre-flattened. **Draft pending SEO/dev review** — see
`docs/organic-page-groups-regex.md` for the companion regex groups that measure the
before/after.

## `synergyhealth-page-inventory-2026-08-11.csv`

Inventory of every **conditions, specialty, treatment, and provider** page on
synergyhealth.org that appears in Search Console or GA4. Built 2026-08-11 by merging:

- **GSC** (`https://synergyhealth.org/`): pages with ≥1 impression, 2025-04-11 → 2026-08-10
  (16 mo), plus a last-90-days pull for the recency column.
- **GA4** (property 370514163): `pagePath` + `pageTitle` + views, trailing 12 months, plus a
  recent (Jun 1 → Aug 10, 2026) pull used to set `status`.

561 rows: **478 live, 82 returning 404** (removed providers, legacy structures), 1 unknown.
**92 live spine-related pages.** URL query strings/fragments stripped; paths lower-cased with
trailing slash; pagination/`/embed/`/feed junk removed.

Columns:

| Column | Meaning |
|---|---|
| `section` | Conditions / Specialty / Treatment / Providers |
| `url_structure` | Which parallel URL hierarchy the page lives in (`/conditions/` vs `/conditions-we-treat/`, `/specialty/` vs `/specialties/`, `/providers/` vs `/our-providers/`, …). Cardinal flagged these competing structures for consolidation. |
| `subcategory` | Middle path segments (e.g. condition group, specialty the sub-page hangs off) |
| `page_name` | Humanized last URL slug |
| `page_title` | Title tag as recorded by GA4 (most-viewed live title) |
| `spine_related` | Yes = spine/neck/back topic keywords in the URL, or a provider on the spine bench in `brand/provider-roster-by-service-line.md` (surgeons, interventional pain, chiro, spine-certified PT) |
| `status` | `Live`, `404 - removed` (GA4 title says Page Not Found in the most recent window it was visited), or `Unknown` (no GA4 title data) |
| `gsc_clicks/impressions_apr2025_aug2026` | Google Search totals for the 16-month window |
| `gsc_impressions_last90d` | Recency signal — 0 with a big 16-mo number usually means removed/redirected mid-window |
| `ga4_pageviews_last12mo` | All-channel pageviews |

Sort order: section → live first → spine first → impressions desc.

Caveats: a page with zero GSC impressions in 16 months **and** zero GA4 views in 12 months
won't appear (rare for live pages). `status` reflects GA4's last observed title, not a live
crawl — the environment's network policy blocks fetching synergyhealth.org directly.
