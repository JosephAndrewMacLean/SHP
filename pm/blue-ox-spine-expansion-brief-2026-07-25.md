# For Blue Ox Digital (Shaun Elley / Jake) — Spine keyword expansion brief (2026-07-25)

> **Ready-to-send draft.** Context: Blue Ox runs the Google Ads account. Spine is materially
> below its new-patient budget (46–53/week against a 72–80 target), and Cardinal's follow-up
> consult on 7/24 landed on keyword universe expansion as the priority action. This is the
> spec for that, plus six things we can't see from GA4.
>
> Tone: collaborative. We've done the analysis so Blue Ox doesn't have to start from scratch —
> this is a spec to react to and improve, not an instruction. Several items below are questions
> where Blue Ox will know something we don't, and two of them are probably worth more than the
> expansion itself.
>
> **Attachments to send with this:** `pm/spine-keyword-build-2026-07.csv` (the keyword sheet),
> `playbooks/spine-keyword-expansion-2026-07.md` (analysis + ad copy),
> `playbooks/spine-keyword-implementation-runbook.md` (staging + owners).

---

Shaun / Jake —

Following Cardinal's consult on Thursday, spine keyword expansion is our priority action, and
Gautam has been clear that spine spend is not being reduced. We've done the analysis end to end
and built the keyword sheet so you're not starting from a blank page. Everything here is open to
your judgment — you see things in the account we can't.

Short version: **spine is spending 22% of its daily budget caps while losing 0% impression share
to budget.** Those are the same fact twice — the keyword universe is too small to absorb the
money we've already authorized. So the ask is structural, not financial.

## Six things we can't see from GA4 — and two are urgent

**1. `"spine doctors"` (phrase, Livonia / Specialist) is paused. Why?**
In Jun 1 – Jul 24 it spent **$21,223** and produced **76.1 conversions at a $279 CPA** — the #2
spine keyword by spend, at a CPA better than the campaign average. If it was paused for a
search-term or quality reason, we want to understand it, because several keywords in the
attached sheet are close cousins and would need negatives rather than reactivation. If it came
out accidentally, it's the fastest volume recovery available to us right now.

**2. Do the geo landing pages redirect?**
GA4 shows **1,677 of 1,871** tracked paid spine sessions (90%) landing on the *generic*
`/specialty/spine-neck-back` page, even though the Sterling Heights and Livonia ads point at the
geo URLs. Port Huron and Southfield together only drew ~230 clicks in that window, so they can't
explain it. It matters a lot:

| Landing page | Paid sessions | Key events | Key events/session |
|---|---:|---:|---:|
| `/specialty/spine-neck-back/sterling-heights` | 109 | 134 | **1.229** |
| `/specialty/spine-neck-back/livonia` | 85 | 101 | **1.188** |
| `/specialty/spine-neck-back` (generic) | 1,677 | 612 | 0.365 |

If it's a redirect, we're paying geo-page prices for generic-page conversion rates across
almost the whole spine account — worth more than the entire keyword expansion, and free to fix.
We're checking the site side in parallel; anything you can see from the Ads side on final URLs
and redirects would help.

**3. Something is leaking `{ignore` into a live URL.**
GA4 recorded sessions on `/specialty/spine-neck-back/{ignore` — looks like an unresolved
tracking-template parameter. Low volume, but it means at least one ad or template is broken.

**4. Current daily budgets per spine campaign — can you confirm?**
Our arithmetic from the Jan 1 – Jul 24 export:

| Campaign | Daily budget | Actual/day | Utilisation |
|---|---:|---:|---:|
| NBS Livonia | $5,000 | $1,097 | 22% |
| NBS Sterling Heights | $5,000 | $1,097 | 22% |
| **NBS Port Huron** | **$50** | **$67** | **134%** |
| NBS Southfield | $50 | $26 | 51% |
| Spine Conditions (both) | $500 | $46 | 9% |

Two questions. Are the $5,000 caps current? And is **Port Huron** actually capped at $50/day —
because Port Huron / Specialist is running the **best cost per new patient in the entire account
at $339**, and if it's throttled that's the cheapest volume available to us anywhere.

**5. Conversion actions in the `Conversions` column.**
Confirm which actions each spine campaign is currently optimizing toward, and that no
existing-patient actions remain in there. Joe spotted a few above the fold on 7/24 that looked
like they might still be counting. Everything in the attached build is measured on
`New Patient (ZocDoc)` + `Liine NP BC or BF` only.

**6. "Some ads limited by policy" on the two Spine Conditions campaigns.**
That flag is on both. Those ad groups are due to migrate into the geo campaigns, and we don't
want to carry a policy problem across with them. What's the disapproval?

## The expansion spec — what's in the attached sheet

**491 keyword rows + 22 ad-group negative lists**, grouped by match type, with Phase 1 and
Phase 2 final URLs per row. Structure goes from 4 ad groups per geo to 9:

Spine Specialist · Back Pain Specialist · Neck Pain Specialist · Sciatica ·
Herniated / Bulging Disc · Spinal Stenosis · Pinched Nerve / Radiculopathy · Spine Surgery ·
Minimally Invasive / Disc Surgery

Full build in Sterling Heights and Livonia (195 keywords each — 75 exact, 109 phrase, 11 broad);
four core ad groups in Port Huron.

**Three deliberate choices worth flagging, all open to your view:**

- **Broad match ships paused.** 11 per geo, built and ready, but off until the Liine/ZocDoc
  online-booking signal is posting back to Ads and we have 30+ qualified conversions in a 30-day
  window per campaign. Broad match steers by conversion signal and ours is still ambiguous. Per
  Cardinal's guidance, 1–2 per ad group, all high-intent "near me" phrasings — no bare category
  terms.
- **Every strong performer gets both an exact and a phrase entry.** `back doctors near me` exact
  runs a 2.00 ROAS; the phrase version runs 0.43. We'd rather run both and let CPA tell us which
  to fund than guess.
- **Pain management and injection terms are excluded** from the expansion by Joe's decision.
  Which leaves an open question for you — see below.

**Where the money should go.** Measured on real new patients only, Jan 1 – Jul 24:

| Theme | Spend | Real new patients | Cost per NP |
|---|---:|---:|---:|
| **Specialist** | $203,224 | 355.4 | **$572** |
| Surgery | $206,928 | 186.9 | $1,107 |
| Injection | $37,355 | 24.7 | $1,514 |
| Fusion | $21,467 | 11.1 | $1,939 |

Specialist takes 42% of spend and returns 61% of new patients. The expansion is weighted toward
that theme and toward "near me" phrasings, which run a **$109 cost per conversion against $289
for everything else** in the account.

## Two decisions we'd like your recommendation on

**Injection ad groups.** They're live at **$37,355 / $1,514 per new patient** and are no longer
being expanded. We're inclined to **contain** — exact match only, cap bids, let the impressions
flow to Specialist and the new condition groups — rather than pause outright, since those terms
are how a non-surgical spine patient converts. With Fusion, containment frees roughly $58,800
sitting at a $1,608 CPA. Does that match what you'd do?

**Orphaned Spine Conditions campaigns.** $9,357, 8 real new patients, tiny separate budgets at
9% utilisation, and they hold the only condition-specific landing pages in paid use. We want to
migrate all four ad groups into the geo campaigns and pause the standalone campaigns. Any reason
not to?

## Staging — one change per week, deliberately

Gautam's operating requirement is that we can attribute an effect to an action week over week,
so we're **not** launching 491 keywords at once even though the sheet is ready.

| Week | What ships |
|---|---|
| 1 | Free fixes only: three live ad typos, unpin the two "Poor" customizer assets, reactivate `"spine doctors"` if #1 clears, Port Huron budget if #4 confirms |
| 2 | **Pilot:** Sciatica ad group, Sterling Heights only. Daily search-term review, pass/fail at day 5 |
| 3 | Back Pain Specialist split out, both geos + Fusion/Injection containment |
| 4 | Sciatica in Livonia + Herniated/Bulging Disc both geos |
| 5 | Surgery split into Spine Surgery + Minimally Invasive |
| 6 | Neck Pain, Spinal Stenosis, Pinched Nerve + Port Huron core four |

Full detail and per-wave checklist in the runbook. If your build process wants a different
sequence, we're flexible on order — the constraint we'd ask you to hold is **one attributable
change per week**, so the weekly review can say what caused what.

## What we expect, so we're judged against a number we stated in advance

Two independent estimation methods, bracketed rather than averaged:

**Incremental impressions/month, Sterling Heights + Livonia: 4,400–11,000 central** (+5% to
+13% on the current 86,514). Which converts to **+2 to +7 new spine patients per week, central
~4**, at **$6k–17k/month of incremental spend — all inside existing budget caps.**

We'd rather put an honest range on record now than claim precision we don't have. Two caveats we
already know about: new keywords launch with low quality score, so the first 2–3 weeks will look
worse than steady state — we plan to judge at week 4. And if the geo-page redirect in #2 turns
out to be real, every number above is understated, because the baseline was measured on traffic
landing on the wrong page.

## Two things from our side

**Ad copy is drafted and attached** — 15 headlines and 4 descriptions per ad group, no shared
headlines across ad groups. Worth knowing why: Sterling Heights / Specialist runs distinct
geo-specific copy at a **6.71% CTR and $396 per new patient**; Livonia / Specialist shares 9 of
12 headlines across all four of its ad groups and runs **3.82% CTR at $806**. Same service line,
same weeks. Everything clinical or claim-based in the new copy is marked pending our compliance
review, and we won't send it live until that clears — including two claims already running
("Walk-ins welcome," "Same-Day Appointments") that we're pulling until verified.

**Landing pages.** Every ad group launches against `/specialty/spine-neck-back/{geo}/`, not the
condition pages — those convert at 0.025 key events/session against the geo pages' 1.21, so
they stay organic assets. Randall is building condition variants on the geo template, and
`/specialty/spine-neck-back/port-huron/` doesn't exist yet, which is why Port Huron is last in
the sequence.

Happy to jump on a call to walk through the sheet if that's faster than email. And genuinely —
if the analysis has something wrong in it, we'd rather hear it now than after six weeks of
building.

— Joe

---

## Internal notes (do not send)

- **Ownership**: per `brand/current-state.md`, Blue Ox operates the account day-to-day; Cardinal's
  paid audit is recommendations *about* Blue Ox's account. Execution questions route to
  Shaun/Jake, not Evan. Keep Cardinal's name out of anything that reads as an inspection.
- **Don't lead with the CPA table.** Items 1–4 are worth more than the expansion and are things
  Blue Ox can answer in a day. If the email gets skimmed, those are what should land.
- **Port Huron budget** is the softest number here — 134% of a $50/day cap over 205 days is
  arithmetic from the export, and the budget may have changed mid-period. It's framed as a
  question for that reason. Don't assert it.
- **The $125 → $75 New Patient Intent change** is a separate thread (ortho, agreed with Gautam
  and Evan on 7/24) — deliberately not bundled here so the spine expansion isn't gated on it.
- **Cardinal follow-up is late August.** Ideally waves 1–3 are live and measured by then so that
  conversation is about results rather than plans.
- If Blue Ox pushes back on staging and wants a single bulk upload: the thing to hold is
  attribution, not the schedule. Offer to compress to 3 waves rather than 6, but not to 1.
