# For Blue Ox Digital (Shaun Elley / Jake) — Google Ads confirmations & decisions (2026-07-22)

> Ready-to-send draft. Context: Blue Ox runs the Google Ads account; Cardinal's June
> 2026 Paid Media audit made recommendations about it. We can see events firing in
> GA4 but not the Ads-side settings, so these are confirmations and open decisions —
> framed so everyone works from the same numbers. Tone: collaborative — this is
> alignment, not an inspection.

---

Shaun / Jake — we've stood up live measurement against the June audit
recommendations, and there are a few Ads-side items we can't see from GA4. Could you
confirm where these stand?

## Conversion tracking — three confirmations

1. **"Website – New Patient Intent" value** — the audit recommended revaluing it
   $125 → $5 (it's an intent click, not a booked patient). It fired **3,981 times in
   the last 30 days**, so at $125 it would dominate Smart Bidding's value signal.
   Has the revaluation happened?
2. **Existing-patient Liine actions** — moved to "Secondary" yet, so bidding
   optimizes only toward new patients?
3. **Liine online-booking ("OB") conversions** — these were 0 / not yet functional at
   audit time. Current status?

If values changed: per the audit's method, campaign ROAS targets need re-baselining
afterward — let us know what changed and when, so our before/after reporting stays
clean.

## Structure decisions the roadmap is gated on

As of 7/22, GA4 shows the audited per-location structure still running
(BOD-Ortho-Livonia/SH, BOD-NBS-Livonia/SH, BOD-Hand, BOD-Podiatry-Southfield,
BOD-Port Huron, BOD-Branded, BOD-Doctors):

- **GEO/consolidation approach** (per-location campaigns vs shared budgets vs one
  campaign per service line) — has a direction been chosen?
- **Troy has no coverage and Southfield is near-zero** — unchanged from the audit;
  Troy is the unlock for the under-penetrated Oakland County opportunity.
- **PMax Ortho test** — not visible yet; still planned?

## Spend context (GA4, last 30 days, for shared reference)

Ortho Livonia ~$73.9k · Ortho Sterling Heights ~$49.5k · Spine (NBS) Livonia+SH
~$82.9k · Hand ~$13.5k · Podiatry Southfield ~$12.8k · Branded ~$3.8k · Doctors ~$4.4k

One more heads-up from our side: the site's landing-page experience is mid-repair
(LCP recovered to ~1.4s; a CLS template fix is in flight) — Quality Scores should
benefit as that lands. We'll share the before/after.

— Joe
