# Reply to Shaun (Blue Ox) — "Updates?" — 2026-08-03

> Draft reply to Shaun Elley's 8/3 email asking for tracking updates, budget direction
> for August, and whether the current strategy is working. Tracking updates sourced from
> the Notion transcripts: 7/29 Liine platform review, 7/30 ZocDoc branded-directory call,
> 7/31 ZocDoc tracking discussion. Attachments to include:
> `pm/spine-keyword-build-2026-07.csv`, `playbooks/spine-keyword-expansion-2026-07.md`,
> `playbooks/spine-keyword-implementation-runbook.md`.

Subject: Re: Updates?

Hi Shaun,

This week is off to a good start, I just hope our cancellation rates are not above
average — that's been the ugly pattern on the ZocDoc marketplace side and I don't want it
hiding in the strong topline.

**Tracking:**

A lot moved this week, most of it good:

- **Root cause found on the online-booking signal.** ZocDoc confirmed a tracking bug in
  their white-label product: bookings made through our white-label scheduler are being
  recorded as *marketplace* bookings, which is why the booking conversion never posts back
  to Google Ads and the campaigns aren't getting attribution for online scheduling. Their
  white-label rebuild isn't due until end of August; they've proposed moving us to their
  Branded Directory (where the Liine integration works correctly) as the interim fix.
  We're working the terms this week — I'll confirm the path as soon as it's settled.
- **Existing-patient conversion actions are now secondary** — new patients are trending
  roughly 10 ahead of the prior two weeks since, which suggests the account really was
  spending signal on existing patients.
- **New Patient Intent value is down $125 → $75.** Plan of record: once the ZocDoc booking
  signal is flowing into Ads and we've collected 30+ qualified conversions in 30 days per
  campaign, we retire NP Intent as an optimization target entirely and lean on the Liine
  booked-call / online-booking actions.
- **The Liine tracking-code gap on the site is resolved** (web updates went in last week),
  so interactions that were previously unattributed are now landing in a channel.
- One insight from Liine worth having in the back of your head for signal quality: the top
  reasons spine PPC callers *don't* book are Medicaid/insurance mismatch, scheduling, and
  "meant to call a competitor." We're working the intake side of that; it's not a campaign
  problem, but it explains some of the gap between conversions and kept patients.

**Budget:**

Plan on similar budgets for August — and specifically no reduction on spine; that's
direction from the top. Worth saying out loud: Livonia and Sterling Heights spine are each
pacing around $1,100/day against $5,000 caps with 0% impression share lost to budget, so
the money isn't the constraint — the keyword universe is. That's the action item below.
One thing to confirm on your side: is Port Huron still capped at $50/day? Our export math
shows it running past its cap, and that campaign has our best cost per booked new patient
in the account, so if anything gets more room in August it should be that one.

**Action Items:**

As it relates to the game plan for Spine, we want to expand the keyword universe inside
the Livonia and Sterling Heights spine campaigns. We've built the full spec so this is
executable, not conceptual — keyword sheet attached, ready for Ads Editor:

1. **Structure:** each campaign goes from 4 ad groups to 9 — Spine Specialist / Back Pain
   Specialist / Neck Pain Specialist / Sciatica / Herniated & Bulging Disc / Spinal
   Stenosis / Pinched Nerve / Spine Surgery / Minimally Invasive & Disc Surgery.
   195 keywords per campaign (75 exact, 109 phrase, 11 broad), each ad group with its own
   negative list and tailored RSA copy (drafted; going through our clinical/compliance
   review now).
2. **Match-type logic:** proven converters and high-intent "near me" terms run exact +
   phrase; the expansion body is phrase; broad match is 1–2 per ad group, uploaded
   **paused** until the ZocDoc booking signal is live — no point letting broad match steer
   on an ambiguous signal.
3. **Landing pages:** everything points at the geo specialty pages
   (`/spine-neck-back/sterling-heights/`, `/livonia/`) — GA4 shows they convert ~3x better
   than the generic spine page and ~50x better than the condition pages. Related question
   for you: 90% of paid spine sessions are landing on the *generic* page even though the
   ads carry geo URLs — can you check final URLs/tracking templates on your side for a
   redirect? There's also a stray `{ignore` showing up in a landed URL, which looks like an
   unresolved template parameter.
4. **Sequencing:** we want to stage this roughly one change per week so we can attribute
   effects — pilot Sciatica in Sterling Heights first, then Back Pain split, then the
   disc/stenosis groups, then the Surgery split. If your build process prefers a different
   order, that's fine; the one thing we'd hold is one attributable change at a time.
5. **Two quick ones while you're in there:** three live typos to fix ("Evrey,"
   "Specialits," "Conditons" — they're on our highest-spend ads), and can you tell us why
   `"spine doctors"` (phrase, Livonia/Specialist) is paused? It did $21K and 76 conversions
   at a $279 CPA before it went dark — if that was deliberate we want to understand the
   reason before we reactivate it.

Attached: the keyword sheet (CSV), the build spec with ad copy, and the phased runbook.
Happy to walk through it on a call this week if that's faster.

Thanks,
Joe

---

## Internal notes (do not send)

- Tracking claims sourced from Notion transcripts 7/29 (Liine review: NP intent $125→$75
  done, existing-patient → secondary, +10 NP trend, tracking-code fix, reasons-not-booked),
  7/30 (ZocDoc branded directory: white-label bug root cause, rebuild end of August,
  Jasmine/order form), 7/31 (white-label misattribution possibly causing incorrect
  ZocDoc charges — being confirmed).
- Deliberately NOT shared with Blue Ox: branded-directory pricing/contract details
  (~$35k/yr, day-61 opt-out, Dec 31 clause ask), the possible incorrect ZocDoc charges,
  internal error-report/front-desk discussion, ZocDoc-marketplace-spend reallocation idea
  (~$34k → Google Ads) — that last one directly affects Blue Ox's scope and should come
  from Joe deliberately, not as a status line.
- "Existing patient → secondary" may have been executed by Blue Ox themselves — the email
  states it as fact rather than news; harmless either way.
- The +10/week new-patient trend is early and unverified against the data lake (which was
  down that week). It's framed as "trending" not as a result.
