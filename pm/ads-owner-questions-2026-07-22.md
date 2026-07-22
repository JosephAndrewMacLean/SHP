# For whoever owns Google Ads (Cardinal?) — conversion & structure questions (2026-07-22)

> Moved out of Paul's update — Paul is the website developer, not the ads manager.
> Per `brand/current-state.md`, paid media is run by Cardinal; route these there
> unless there's an internal ads owner. All items trace to Cardinal's own Paid Media
> audit; we can see events fire in GA4 but not the Ads-side settings.

## Conversion tracking — three confirmations

1. Was **"Website – New Patient Intent" revalued $125 → $5** (their audit, slide 11)?
   It fired **3,981 times in the last 30 days** — if it's still $125, it's drowning
   Smart Bidding in low-quality value exactly as their audit warned.
2. Were the **existing-patient Liine actions switched to "Secondary"** (slide 10)?
3. **Liine online-booking ("OB") conversions were 0 / not functional** at audit time —
   current status?

After any value change: re-baseline campaign ROAS targets per their own recalculation
method (slides 12–14), and tell us what changed and when, so before/after reads stay
clean.

## Structure decisions their roadmap is gated on

As of 7/22, GA4 shows the account still running the audited per-location structure
(BOD-Ortho-Livonia/SH, BOD-NBS-Livonia/SH, BOD-Hand, BOD-Podiatry-Southfield,
BOD-Port Huron, BOD-Branded, BOD-Doctors):

- **GEO/consolidation decision** (their slide 17: per-location vs shared budget vs
  per-service-line) — not visible as applied. Has the call been made?
- **No Troy coverage, Southfield near-zero** — unchanged from the audit.
- **No PMax test live** yet.

## Spend context (GA4, last 30 days, for reference)

Ortho Livonia ~$73.9k · Ortho Sterling Heights ~$49.5k · Spine (NBS) Livonia+SH
~$82.9k · Hand ~$13.5k · Podiatry Southfield ~$12.8k · Branded ~$3.8k · Doctors ~$4.4k
