# Update for Paul — verified items needing action (2026-07-22)

> Ready-to-send draft (email or Slack). Context: this week we wired live measurement
> against the Cardinal June audits (GA4, Search Console, Semrush, direct site checks).
> Everything below is verified with dates and data — sources in
> `audits/cardinal-recommendation-tracker.md`.

---

Paul — we now have live measurement running against the Cardinal audit recommendations,
and it surfaced six things in your lane. Ordered by urgency; each one is verified, not
assumed.

## 1. Core Web Vitals: the speed fix worked — CLS is the one thing keeping us out of "Good"

- Good news first (PageSpeed field data, run 7/22): **LCP has recovered to 1.36–1.57s**
  across homepage, spine hub, carpal tunnel, TKA, and Sterling Heights (it was a
  failing 3.5s at audit time), and lab scores roughly doubled (52–79 vs 28/100).
  Whatever performance work shipped — it worked.
- **But CLS p75 is 0.11–0.12 on every one of those pages — just over the 0.10 pass
  line — so the entire site still fails "Good" CWV status.** Cardinal named the cause:
  **203 images missing width/height attributes** (plus the testimonial-slider DOM).
  That's a template-level fix, and it's the last thing between us and green.
- Meanwhile the traffic damage from the May–July failing period hasn't healed: GA4
  organic is at roughly half of March (6,163 → ~2,750/mo), GSC impressions/day are
  **−27%** since the audit, average position slid **10.9 → 13.3**, and the carpal
  tunnel page that ranked **#1.37** is now at **position ~17**. Rankings lag CWV
  repair — which is exactly why finishing CLS now matters.
- **Action:** ship the image width/height template fix (Cardinal's list, Phase 1–2),
  then we watch GSC flip URLs to "Good" and track ranking recovery week by week. Worth
  5 minutes too: the **Cloudflare audit log for Apr 25 – May 3** to confirm what
  triggered the original regression, so it can't silently happen again.

## 2. Cloudflare is blocking the AI crawlers our AIO strategy targets

- Verified by direct fetch 7/22: a "Cloudflare Managed content" robots.txt block
  disallows **GPTBot, ClaudeBot, Google-Extended, CCBot** (+ `Content-Signal:
  ai-train=no`), and the bot challenge serves "Just a moment…" to non-browser agents —
  including on **/llms.txt**, the file built specifically for AI crawlers.
- Regular Google indexing is unaffected (Googlebot isn't blocked), but Claude can't
  index us at all and Gemini grounding is cut — the opposite of the audit's "do not
  block bots that serve live user queries."
- **Action (whoever holds Cloudflare — happy to route):** review the zone's managed
  robots.txt / "block AI bots" setting and turn it off for retrieval bots; add WAF skip
  rules for `/llms.txt` and `/robots.txt`. If blocking AI *training* is a deliberate
  policy choice that's fine — but it should be a decision, not a default.

## 3. The staging site is still publicly open

- `synergy.egowebdev.com` returns **HTTP 200** to anyone (verified 7/22). Cardinal
  flagged this as "password-protect immediately" — duplicate content + link-equity leak.
- **Action:** password-protect or IP-restrict it.

## 4. Conversion tracking — three confirmations we can't see from our side

Cardinal's paid roadmap hinges on these; GA4 shows the events firing but not the
Ads-side settings:

- Was **"Website – New Patient Intent" revalued $125 → $5**? It fired **3,981 times in
  the last 30 days** — if it's still $125, it's drowning Smart Bidding in low-quality
  value exactly as the audit warned.
- Were the **existing-patient Liine actions moved to Secondary**?
- **Liine online-booking ("OB") conversions were 0 / not functional** at audit time —
  where does that stand?
- **Action:** confirm/complete these, and after any value change, re-baseline the
  campaign ROAS targets per Cardinal's recalculation method (their paid deck, slides
  12–14). Tell us what changed and when, so our before/after reads are clean.

## 5. Analytics hygiene — ~6% of traffic is being mis-measured

- **1,310 sessions/90d land on "(not set)"** with 3.6% engagement — a tagging or
  consent gap.
- **GBP UTM casing is split** — `GBP / Organic` and `gbp / organic` both exist,
  halving our listing-click reporting. Standardize one casing in the GBP links.
- Cardinal also found the **CSP blocking Microsoft Clarity and Cloudflare Beacon** on
  every page load (analytics data loss; their "5-minute allowlist fix").
- **Action:** fix the tag/consent gap, standardize the GBP UTMs, add the two domains
  to the CSP allowlist.

## 6. FYI — decisions Cardinal is waiting on (visible in our campaign data)

As of 7/22 the account still runs the audited per-location structure (BOD-Ortho-
Livonia/SH, BOD-NBS-Livonia/SH, etc.) — **no GEO/consolidation decision applied, no
Troy coverage, Southfield near-zero, no PMax test live.** If the consolidation call
(their slide 17: per-location vs. shared budget vs. per-service-line) has been made,
let us know; if not, it's gating the rest of their paid roadmap.

---

Everything above sits in our live tracker
(`audits/cardinal-recommendation-tracker.md`) with the instrument that measures it —
so each fix you ship will show up in the data within days, and we'll report the
before/after. Shout if you want the raw pulls behind any of these.

— Joe
