---
name: paid-forecast
description: >
  Estimate the expected performance of a Google Ads change before it launches — keyword
  expansion, ad group restructure, budget shift, landing page swap — and then score the
  forecast against what actually happened. Use when asked "what will this deliver," "what's
  the estimated impact," "is this worth doing," "how many new patients will this add," or when
  a paid-media recommendation needs a number attached before it goes to Gautam, the board, or
  Blue Ox. Also use to run the actual-vs-estimate review after a change has been live 2+ weeks.
---

# Paid Media Forecasting — SHP

You are producing a forecast that Joe will be held to in a weekly review, in front of a CEO who
treats false precision as evidence you don't understand the problem. **A defensible range beats
a confident point estimate every time.** If you cannot bracket the answer, say so and say what
data would let you.

Read `brand/current-state.md` and `audits/cardinal-recommendation-tracker.md` for context before
forecasting anything.

## The non-negotiables

1. **Never forecast on raw "conversions."** The SHP account runs ~15 conversion actions of wildly
   different quality. Always define the outcome as **real new patients** =
   `New Patient (ZocDoc)` + `Liine NP BC or BF` (+ `Liine NP OB` once the ZocDoc integration is
   fixed). Explicitly exclude `Website - New Patient Intent` — it is an intent click, it was
   overvalued at $125, and it is being phased out. State the definition in the output.
2. **Two independent methods, bracketed — never averaged.** If a bottom-up and a top-down method
   disagree by 3x, that disagreement *is* the finding. Report both and use the overlap. Averaging
   them manufactures precision that doesn't exist.
3. **Calibrate from SHP's own data, not from benchmarks.** Industry CTR and conversion benchmarks
   are the lazy answer and they are usually wrong for a specific account in a specific geo.
4. **State what would make the forecast wrong** before anyone asks. This section is mandatory.
5. **No PHI, no unsubstantiated clinical claims** if the output touches ad copy or patient-facing
   language. Anything clinical is a draft pending human review.

## Data sources

| Need | Source |
|---|---|
| Actual keyword/ad group/campaign performance | Google Ads exports (Campaigns, Ad Groups, Ads, Search Keywords). Ad Group exports segmented by conversion action **zero out cost/clicks/impressions** — get cost from the Ads or Keywords export and conversions-by-action from the Ad Groups export. |
| Search volume, CPC, competition, intent | Semrush MCP — `phrase_these` (batch volume), `phrase_fullsearch` (discovery), `phrase_related`. Volumes are **US national** unless you scope the database. |
| Landing page conversion rates | GA4 MCP (`run_report`, property **370514163**) — `landingPage` × `sessionDefaultChannelGroup`, metrics `sessions` + `keyEvents`. Filter to Paid Search. |
| Page existence, organic demand | Google Search Console MCP (`search_analytics`) |
| Impression share lost to rank vs budget | **Google Ads UI only** — not in the standard exports. Ask for it; don't estimate it. |

Note: network policy blocks fetching synergyhealth.org directly. Verify site state via
Semrush / GA4 / GSC.

## Method

### Step 1 — Establish the baseline, scoped tightly

Compute for the *specific* campaigns/ad groups being changed, not the whole account:
impressions, clicks, cost, CTR, CPC, real new patients, cost per real new patient, and budget
utilisation (actual spend/day ÷ daily budget cap).

**Always compute budget utilisation.** At SHP it has repeatedly been the buried headline — spine
was found running at 22% of a $10,600/day cap while showing 0% impression share lost to budget.
Those are the same fact stated twice, and it reframes the whole ask from "give us money" to
"let us spend what we have."

### Step 2 — Calibrate a capture ratio from our own data

For every keyword where you know **both** the Semrush US monthly volume **and** SHP's actual
impressions:

```
ratio = (actual_impressions × 30 / days_in_period) / US_volume_per_month
```

This bundles Metro Detroit's share of US search × our impression share × match-type reach into
one empirically observed number — which is exactly what you want for forecasting comparable
keywords in the same geos.

**Report the median and the interquartile range, and split by match type** (exact and phrase
behave very differently — phrase captures variants far beyond its seed term's volume, which
produces ratios above 1.0). If the IQR spans more than ~3x, say plainly that this is an
order-of-magnitude tool and not a forecast engine.

*Calibration on file (spine, Sterling Heights + Livonia, Jun 1 – Jul 24 2026, n=20):
median 0.088, IQR 0.038–0.255; exact median 0.054, phrase median 0.132. Re-derive rather than
reusing this if the geo, service line, or account structure differs.*

### Step 3 — Method A, bottom-up

```
incremental impressions/mo = (new transactional search volume) × (calibrated ratio)
```

Run it at the ratio's p25, median, and p75. **Use only transactional/commercial volume** — filter
by Semrush intent, or by the presence of "near me" / doctor / specialist / surgeon / treatment.
Condition head terms like "sciatica" (368,000/mo) are overwhelmingly informational and counting
them will overstate the opportunity by an order of magnitude. This is a mistake that has already
been made once on this account; don't repeat it.

### Step 4 — Method B, top-down

```
incremental impressions/mo = (new keyword rows) × (share of rows that get any impressions)
                             × (median impressions/mo per active row)
```

**Use the median, never the mean.** Paid keyword distributions are extremely long-tailed — in the
spine account the top 5 rows of 218 carried 30% of all impressions, and mean impressions/row was
397 against a median of 89. The mean will inflate the forecast ~4x.

### Step 5 — Convert impressions to new patients

Walk the funnel with a **range at every step**, drawn from actual observed performance in the
ad groups most similar to what's being built:

```
clicks         = impressions × CTR
spend          = clicks × CPC
new patients   = spend ÷ cost per real new patient
```

Sanity checks that have mattered here:
- **"Near me" keywords behave differently** — higher CTR (7–10% vs a 4% blend), lower CPC, better
  CPA. Don't apply blended rates to a near-me-weighted build.
- **New keywords launch with low quality score**, so weeks 1–3 will underperform the steady-state
  range. Say this explicitly and name the week at which the forecast should be judged.
- **Check the incremental spend against budget headroom.** If it doesn't fit, the forecast is a
  budget request and must be labelled as one.

### Step 6 — Rank the lever against the alternatives

A forecast in isolation invites the wrong decision. Always compare the change to the other levers
available in the same account, with cost and confidence:

| Lever | Est. weekly gain | Cost | Confidence |
|---|---|---|---|

Free, high-confidence fixes (broken tracking, a wrongly paused high performer, a landing page
redirect, reallocating spend from a high-CPA theme to a low-CPA one) frequently outrank the
headline project. **Say so even when the headline project is the one you were asked to forecast.**

### Step 7 — State what would make it wrong

Mandatory. Cover at minimum: sample size on any rate you used, whether a measurement problem
could be corrupting the baseline, informational-vs-transactional intent risk, quality-score
ramp, and any dependency (integration fix, page build, compliance approval) the forecast assumes.

## Output shape

```
FORECAST: <change> — <campaigns/ad groups>
Outcome measured as: real new patients = New Patient (ZocDoc) + Liine NP BC or BF
                     (excludes Website - New Patient Intent)

BASELINE           impressions/mo, clicks, cost, CTR, CPC, real NPs, cost/NP, budget utilisation %
CALIBRATION        n, median ratio, IQR, by match type — and whether it's trustworthy
METHOD A           low / central / high
METHOD B           low / central / high
BRACKET            incremental impressions/mo, and % vs baseline
FUNNEL             clicks → spend → new patients/week, as a range
BUDGET FIT         incremental spend vs available headroom
RANKED LEVERS      this change vs the alternatives, with cost and confidence
WHAT WOULD MAKE THIS WRONG
JUDGE AT           the week number when the forecast should first be scored
```

## Scoring the forecast afterwards

Run this once the change has been live **at least 2 weeks** (4 for anything involving new
keywords, because of the quality-score ramp).

1. Pull actuals for the same scoped metrics as the baseline.
2. Report actual vs the forecast range: **inside / above / below** — not a percentage error
   against the central estimate. A result inside the range is a hit even if it's nowhere near
   the midpoint.
3. **Attribute.** If several changes shipped in the same period the forecast is unscoreable — say
   that, and flag it as a process failure to fix, not a measurement footnote. One attributable
   change per week is the standard.
4. Update the calibration ratio with the new observations. The ratio should get better every
   month; that improvement is the actual deliverable of this skill.
5. Note which assumption was most wrong and by how much. That is what makes the next forecast
   better.

**Never quietly revise a forecast after seeing the result.** State the original, state the actual,
state the gap. The weekly learning loop only works if the prediction is on record before the
outcome is known.

## Communicating it

The audience is a CEO who has said explicitly that talking fast and using buzzwords signals a
lack of mastery, and that the standard is connecting the dots simply.

- **Lead with the number and the range**, in one sentence, then the logic chain.
- **Present the logic in causal order**: what the data showed → what it implies → therefore this
  action → therefore this expected result. Never action-first.
- **Plain language for clinical stakeholders**: "people who found us on Google," not "organic
  sessions." Define every number shown.
- **"I don't know" is an acceptable and preferred answer** where the data doesn't support a claim.
  Say what you'd need to find out and when you'll have it.
- Round honestly. "+2 to +7 new patients a week, central around 4" is better than "+3.8/wk."
