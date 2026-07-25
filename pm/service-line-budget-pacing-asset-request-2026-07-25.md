# Asset request — capacity-aware service-line budget & pacing analysis (2026-07-25)

> Context: incoming ask was to figure out what's needed to tie paid-media budget and
> pacing to actual clinic capacity and forecasted demand, by service line. That's a
> natural next step from the Blue Ox conversation already in flight
> (`pm/ads-owner-questions-2026-07-22.md`) — this doc is the asset checklist so the
> analysis can actually be run. **Assumption flagged:** the exact deliverable (e.g.
> a monthly pacing dashboard vs. a one-time budget reallocation memo) wasn't specified
> — confirm before a next session builds it out.

## What this team already has (no new asset needed)

| Source | What it covers here | Status |
|---|---|---|
| GA4 (MCP) | Session/conversion volume by channel, landing page, service line; campaign-level Ads spend/clicks via the GA4↔Ads link (e.g. Ortho Livonia ~$73.9k/30d) | ✅ live |
| Semrush | Organic/paid SERP context, competitive share | ✅ live |
| Search Console | Organic demand signal (impressions/clicks by query → service line) | ✅ live |
| `pm/ads-owner-questions-2026-07-22.md` | Current campaign structure, spend by location/service line, open Blue Ox decisions | ✅ in repo |
| `brand/current-state.md` | Service-line growth rates (Spine +89%, Foot +114%, Pain declining), the ~4,800 obtainable-patient/year opportunity | ✅ in repo |

None of this tells us **capacity** (can the clinic actually see more patients?) or
**forward demand** (Power BI forecast) or **documented budget targets/pacing rules** —
that's the gap below.

## What's missing — four asset asks

### 1. Clinic capacity report
Needed to avoid recommending spend that generates demand a clinic can't fulfill.
- Per **location** and per **service line** (Ortho, Spine, Hand, Podiatry, Pain,
  PT, Imaging): available new-patient appointment slots per week/month, and
  current utilization (% booked).
- Time horizon: current-state snapshot is enough to start; trend (last 3–6 months)
  is better if it exists.
- Format: whatever export exists today (Excel/CSV/PDF) — drop into
  `data/clinic-capacity/2026-07-25/` per the interim standard in
  `docs/data-sources-roadmap.md` §9.
- Who likely owns it: clinic operations / practice management, not marketing —
  flag if this needs a request routed through Joe/practice ops.

### 2. Power BI "future new patient" report
Needed as the demand-forecast side of the capacity/demand pairing.
- What it forecasts, specifically: new-patient volume by service line? by
  location? by month/quarter? Confirm the grain — the analysis is only as
  useful as the finest shared dimension between this and the capacity report.
- Access path — pick one:
  - Export (PDF/Excel/CSV) dropped into `data/powerbi-new-patient-forecast/2026-07-25/`
    (fastest, matches the interim standard already used for Rater8/ZocDoc).
  - Or a Power BI workspace share / API credential if this needs to run on a
    recurring cadence rather than a one-time pull.
- Confirm the forecast's own assumptions (does it already account for capacity
  constraints, or is it pure demand-side?) — that determines whether this
  analysis is "compare two independent forecasts" or "capacity-adjust a
  demand number."

### 3. Google Ads data beyond what GA4 shows
GA4 already gives campaign-level spend/clicks/sessions by service line. Missing
for a true pacing view:
- **Monthly budget by campaign/service line** and **month-to-date spend vs.
  that budget** (pacing %) — this lives in Google Ads, not GA4.
- Conversion-action values and Smart Bidding targets (the $125→$5 "New Patient
  Intent" revaluation from the Cardinal audit — status still unconfirmed per
  the open Blue Ox thread).
- Two ways to get it: (a) Blue Ox Digital (Shaun Elley / Jake) sends a
  budget-vs-actual export alongside answers to the open questions in
  `pm/ads-owner-questions-2026-07-22.md`, or (b) stand up the official
  read-only Google Ads MCP (needs a developer token + MCC read access) per
  `docs/data-sources-roadmap.md` §3. (a) is faster; (b) is reusable every
  session going forward.

### 4. Service-line goals, budget, and pacing definition
The one asset that's pure internal decision, not a data pull:
- Documented annual/quarterly **new-patient targets by service line** (Spine
  and Ortho are the confirmed priorities per `brand/current-state.md` — but
  targets in numbers, not direction, are needed to pace against).
- **Marketing budget by service line** (not just current Ads spend, which we
  can already see — the *approved* budget ceiling and any seasonal shape to it).
- How pacing is defined internally today, if at all (e.g., "spend should track
  linearly to day-of-month," or "pace to bookings, not spend") — so the
  analysis matches how the practice already thinks about it rather than
  inventing a new framework.

## Suggested drop location

Per `docs/data-sources-roadmap.md` §9: `data/<source>/<YYYY-MM-DD>/` with a short
README noting export settings. Proposed folders:
- `data/clinic-capacity/2026-07-25/`
- `data/powerbi-new-patient-forecast/2026-07-25/`
- `data/google-ads-budget-pacing/2026-07-25/`

Once these land, the analysis pairs capacity × forecasted demand × current
pacing, by service line, and flags where paid spend is (a) generating demand
a clinic can't absorb, or (b) under-pacing relative to open capacity —
prioritized the same way the Cardinal recommendations are: implementation-ready,
not aspirational.

⚠️ Compliance note: none of these four sources should carry patient-identifying
data into this repo — aggregate counts/rates/dollars only (HIPAA), consistent
with how Liine/Rater8/ZocDoc are already handled.
