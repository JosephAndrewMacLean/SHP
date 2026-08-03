# Blue Ox call — Shaun Elley / Jake Reardon — 2026-08-03

Follow-up to the "Updates?" email. Decisions below supersede the corresponding parts of
`playbooks/spine-keyword-expansion-2026-07.md` (see the revision banner there) and the
keyword sheet has been regenerated to match (`pm/spine-keyword-build-2026-07.csv`).

## Decisions

1. **No broad match. Anywhere. Not even paused-and-gated.** Jake: past tests (AI Max,
   earlier broad experiments) pulled chiropractor / massage / PT queries and internal teams
   pulled the plug. Joe agrees — Evan's "just use broad" advice assumed clean conversion
   signals we don't have. The 11-per-geo gated broad keywords are **removed from the build**,
   not just paused.
2. **Condition / top-of-funnel keywords go into the existing separate campaigns**
   (`BOD - Spine Conditions - {geo}` and the paused "pain" campaigns' shells) — **not** into
   the geo NBS campaigns. Jake's reasoning: the geo campaigns run on target ROAS; loading
   them with lower-converting upper-funnel terms raises spend without proportional
   conversions, tROAS recalibrates, and the proven low-funnel terms get choked. This
   **reverses** the build spec's §2.4 (which migrated the condition campaigns *into* the geo
   campaigns). Instead: **add budget to the condition campaigns** and expand there.
3. **Low-funnel expansion stays in the geo campaigns**: specialist / surgeon / "near me" /
   surgery terms. Blue Ox will also map **treatment-type keywords (ACDF, TLIF, disc
   replacement, etc.) with keyword-level final URLs** to the matching treatment pages —
   these searchers are educated, often prior surgical patients, highest value.
4. **"Pain management" is retired as a concept in this account.** Clinical reality: pain
   doctors are full, spine doctors are open; scheduling protocol changed so injection
   callers are booked with a spine doctor who quarterbacks care (insurance requires the
   consult anyway). The old "pain" campaigns' keyword shells may be reused for condition
   terms, but nothing targets injection/pain-management intent. (Consistent with the 7/25
   removal of Pain Management from the build.)
5. **Port Huron spine: stopping.** Dr. Munk is leaving and there's no spine replacement
   yet; keep Port Huron **ortho** running. **Southfield spine: end bids** — the half-day is
   gone and calls routed to Livonia anyway. This **supersedes** the build's "Port Huron
   core four + build the Port Huron page" recommendation — the $339 CPA was real, but the
   capacity behind it is going away. Budget from both frees up for the condition campaigns.
6. **Budgets: hold August at current levels.** No spine reduction (Gautam's direction; he
   was irritated Evan ever suggested it). Incremental condition-campaign budget comes from
   Port Huron spine + Southfield spine wind-down before any new money.

## Things Blue Ox told us that close open questions from the 7/25 brief

- **The 90%-generic landing page mystery is (probably) explained**: Blue Ox found ~2 weeks
  ago that **Livonia spine ads pointed at the generic page** even though the Livonia page
  existed, and fixed it. My GA4 window (Jun 1 – Jul 24) mostly predates the fix. → Verify
  in GA4 with a post-fix window (≈Jul 20 – Aug 15) before treating it as resolved; the
  Sterling-vs-generic split still needs eyes.
- **Typos** ("Evrey" / "Specialits" / "Conditons"): Blue Ox will fix.
- **Liine's numbers were misleading Cardinal**: undefined/no-channel bookings were Google
  Ads traffic whose parameters weren't passing (consent tag fired too late). Paul's fix
  restored passing for some surfaces — but parameters currently confirmed passing for
  **Bing and GBP, still not Google Ads**. Liine (Kelly, 3 months in; Eric the co-founder
  now shadowing) still working it.
- **The 147→112→105 ortho slide** may have been caused by **existing-patient events sitting
  as primary conversions** — Joe turned them off; new patients trending up since.
- **$75 NP-intent value is Joe's math** (GA4 click→book→keep rates), unlike the $125/$150/$5
  values which were Kelly-at-Liine's guesses. Jake's watch-item below.

## Blue Ox's watch-item (add to daily checks)

Dropping NP intent $125→$75 under target ROAS may push the algorithm toward **phone calls**
(some carry $150) and away from ZocDoc scheduler conversions — same failure mode as the old
tCPA era: call volume up, call quality down. **Watch daily: ZocDoc bookings vs. call
conversions mix.** If scheduler bookings sag while $5/$150 calls swell, the value mix needs
rebalancing.

## In flight at Blue Ox

- **Zip-code conversion analysis** (Jake): conversion rate by zip over the past year.
  Proposal coming: a third "in-between corridor" campaign for the Livonia↔Sterling Heights
  gap, pointed at the generic page, toggled by weekly capacity; could also let the two geo
  campaigns run tighter tROAS. Rule of thumb: 30–50 conversions in 30 days before it can
  carry its own tROAS.
- **Capacity-aware budgeting** already runs Mon–Wed: push budget/ad copy toward whichever
  doctor/office has openings early-week.
- **Keyword research for condition campaigns** starting now; sciatica first (page exists).

## Capacity notes (context for weekly numbers, not marketing actions)

- Spine Thursdays/Fridays are thin (one doctor + one cross-town); consistent Thu/Fri
  Sterling Heights availability would let demand actually land. Every-other-week doctor
  schedules make performance unpredictable.
- Ortho: 130–140/wk target = ~26/day. Monday <25 predicts a bad week. Seasonality tailwind
  starting (Aug ramps; Sep–Oct peak; deductible-reset urgency).

## Action items

| # | Item | Owner |
|--:|---|---|
| 1 | Regenerate keyword sheet: no broad, no Port Huron/Southfield spine, condition ad groups → Spine Conditions campaigns | Joe (done — v2 sheet) |
| 2 | Keyword research + build for condition campaigns, sciatica first | Blue Ox |
| 3 | Treatment-type keywords (ACDF/TLIF/disc replacement) with keyword-level URLs | Blue Ox |
| 4 | Stop Port Huron spine; end Southfield spine bids | Blue Ox |
| 5 | Fix the three ad typos | Blue Ox |
| 6 | Zip-code analysis + in-between-campaign proposal | Jake |
| 7 | Daily watch: ZocDoc bookings vs. phone-call conversion mix post value change | Joe |
| 8 | Verify Livonia landing page fix in GA4 (post-Jul-20 window); check Sterling too | Joe |
| 9 | Chase Liine on Google Ads parameter passing (works for Bing/GBP, not Ads) | Joe |
| 10 | ZocDoc Branded Directory decision paused until Santosh returns (this week) | Joe/Santosh |
