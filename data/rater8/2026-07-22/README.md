# Rater8 export — 2026-07-22

First rater8 data drop into the repo (convention: `docs/data-sources-roadmap.md` §9).
Supplied by Joe on 2026-07-22 as two Excel exports from rater8:

| Original export | What landed here |
|---|---|
| `Google_Business_Profile_Scorecard__Synergy_Health_Partners_Troy_MI.xlsx` | `gbp-scorecard.csv` — **full contents** (business data, no patient info) |
| `Patient_Feedback__Synergy_Health_Partners.xlsx` (report #18) | `patient-feedback-aggregates.csv` — **aggregates only** (see compliance note) |

**Human-readable outputs built from this drop:**
- `brand/gbp-profile-directory.md` — canonical GBP listing directory (links, Place IDs,
  routing shares, coverage gaps).
- `audits/rater8-reputation-baseline-2026-07.md` — review-velocity baseline against
  Cardinal's Phase-3 program.

## ⚠️ Compliance note (why the raw patient-feedback file is not committed)

The raw Patient Feedback export contains reviewer names and free-text review comments that
can include patient-written health details. Per the workspace standard
(`docs/data-sources-roadmap.md` §5 and "Security & compliance"), Rater8 data enters the
repo **de-identified/aggregated or not at all**. The raw file stays in the rater8
dashboard / Joe's files; only entity-level aggregates are committed here. Reviews are
public web content, but the repo standard is stricter on purpose — keep it that way.

## `gbp-scorecard.csv` — field definitions

One row per rater8-managed Google Business Profile listing (50 rows: 42 provider×location
listings across 22 physicians + 5 location profiles + PT Sterling Heights + Synergy
Ambulatory Surgery Center + corporate profile).

| Field | Meaning |
|---|---|
| `Listing Name` | rater8 listing label: `Provider (Location)` or a location/org profile |
| `Review Requests %` | Share of that entity's rater8 review requests routed to this Google listing (rater8 "review balancing"). Per-provider rows sum to ~100% across their listings; the 5 location profiles sum to ~100% of location-level requests. A provider total <100% means the remainder routes to non-Google review sites (Healthgrades/Vitals/WebMD). `-` = no requests routed. **Confirm exact denominator semantics with the rater8 rep.** |
| `Link` | Google reviews page (`search.google.com/local/reviews?placeid=…`). The write-a-review link is derivable: `…/local/writereview?placeid=<Place ID>` |
| `Place ID` | Google Place ID — stable key for schema `sameAs`/`hasMap`, citations, GBP API |
| `Scrape Date` | rater8 scrape date for that listing (2026-07-21 or 2026-07-22) |

Known blanks: **SHP Clinic: Troy has no Link/Place ID** (profile not linked in rater8 —
evidence for task GOV-A.1).

## `patient-feedback-aggregates.csv` — field definitions

Aggregated from 85 individual reviews (rater8 "Patient Feedback" report #18, pulled
2026-07-22). One row per **entity × source**, where entity is either a provider (review
attributed to a physician) or a location (review attributed to the clinic listing).

| Field | Meaning |
|---|---|
| `provider_or_location` | Physician name, or `SHP…` location, exactly as attributed by rater8 (`Employee/Question` column) |
| `entity_type` | `provider` or `location` |
| `source` | Review platform: Google, Healthgrades, Vitals, WebMD |
| `reviews` | Review count in this export |
| `avg_rating` | Mean star rating (this export: 5.0 everywhere — see caveats) |
| `avg_sentiment` | Mean rater8 sentiment score (0–1) |
| `responded` | Reviews with an owner response |
| `dated_reviews` | Reviews carrying an exact review date |
| `earliest_dated` / `latest_dated` | Exact-date range for dated reviews |

## Caveats on the patient-feedback export (read before citing numbers)

1. **Every review is 5★ / sentiment "Happy"** (avg sentiment 0.97). Almost certainly a
   filtered report (5★-with-comments or similar) — **do not cite as "SHP has zero negative
   reviews."** Ask the rater8 rep what filter report #18 applies and pull an unfiltered
   velocity report if possible.
2. **31 of 85 rows have no exact review date** (mostly Google reviews attributed to
   location listings). At least one undated row is old (owner response dated Aug 2024), so
   the export's `Comment Date` (Jun/Jul-2026) reflects the pull window, not necessarily
   the posting date. Velocity math uses the 54 exact-dated rows only.
3. Non-Google reviews (WebMD/Healthgrades/Vitals) carry no location attribution.

## Refresh

Drop the next export into `data/rater8/<YYYY-MM-DD>/` in the same shape. Standing ask
(roadmap §5): scheduled weekly CSV or API access from the rater8 rep, ideally unfiltered.
