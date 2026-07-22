# Update for Paul (website developer) — verified items needing action (2026-07-22)

> Ready-to-send draft (email or Slack). Scope: website/dev items only — ads-side
> questions live in `ads-owner-questions-2026-07-22.md`. Everything below is verified
> with dates and data; sources in `audits/cardinal-recommendation-tracker.md`.

---

## ⭐ TL;DR — the top 3 for this week

1. **Ship the CLS fix (image width/height template change).** Speed recovered
   (LCP 3.5s → ~1.4s) but layout shift is 0.11–0.12 — just over Google's 0.10 pass
   line — on every key page, so the whole site still fails Core Web Vitals and
   rankings can't recover. ~203 images missing width/height; done = CLS < 0.10.
2. **Cloudflare: stop blocking AI crawlers; un-challenge llms.txt.** Managed
   robots.txt disallows GPTBot/ClaudeBot/Google-Extended/CCBot and the bot challenge
   fronts /llms.txt. Done = AI-block off for retrieval bots + WAF skip rules for
   /llms.txt and /robots.txt. (+5 min: audit log Apr 25–May 3 for the regression
   trigger.)
3. ~~**Password-protect `synergy.egowebdev.com`.**~~ ✅ **DONE — shipped same day
   (7/22), re-verified HTTP 401.** Nothing further needed.

Full detail and the non-urgent punch list below.

---

Paul — we now have live measurement running against the Cardinal audit
recommendations, and it surfaced a tight list of website items. Ordered by impact;
each one is verified, not assumed.

## 1. Core Web Vitals: the speed fix worked — CLS is the one thing keeping us out of "Good"

- Good news first (PageSpeed field data, run 7/22): **LCP has recovered to
  1.36–1.57s** across homepage, spine hub, carpal tunnel, TKA, and Sterling Heights
  (it was a failing 3.5s at audit), and lab scores roughly doubled (52–79 vs 28/100).
  Whatever performance work shipped — it worked.
- **But CLS is 0.11–0.12 on every one of those pages — just over the 0.10 pass line —
  so the entire site still fails "Good" CWV status.** Cardinal named the cause:
  **203 images missing width/height attributes** (the 8 body-part SVGs and 18
  affiliate logos are called out specifically) plus the testimonial-slider DOM
  (3,126 elements). Template-level fixes, and the last thing between us and green.
- Context on why it's urgent: the May–July failing period cost us roughly half our
  organic traffic, rankings are still sliding (avg position 10.9 → 13.3), and ranking
  recovery can't start until pages flip to "Good."
- **Action:** ship the image width/height template fix; virtualize or trim the
  testimonials slider when you can. We re-verify with one command
  (`scripts/cwv-check.py`) and will report the flip.

## 2. Cloudflare settings are blocking the AI crawlers our strategy targets

- Verified by direct fetch 7/22: a **Cloudflare-managed robots.txt block** disallows
  **GPTBot, ClaudeBot, Google-Extended, CCBot** (+ `Content-Signal: ai-train=no`),
  and the bot challenge serves "Just a moment…" to non-browser agents — including on
  **/llms.txt**, the file that exists specifically for AI crawlers.
- Regular Google indexing is unaffected (Googlebot isn't blocked), but Claude can't
  index us at all and Gemini grounding is cut — the opposite of the audit's "do not
  block bots that serve live user queries."
- **Action:** in the Cloudflare dashboard, review the zone's managed robots.txt /
  "block AI bots" setting and disable it for retrieval bots; add WAF skip rules for
  `/llms.txt` and `/robots.txt`. (If leadership wants to keep blocking AI *training*,
  that's a legitimate choice — but it should be a decision, not a default.)
- While you're in there: **pull the Cloudflare audit log for Apr 25 – May 3** — if bot
  protection, security level, or a CSP change landed in that window, that's the likely
  trigger of the original May 1 regression, and we want to make sure it can't
  silently happen again. Also note Semrush flags **1 malformed line in robots.txt**
  — worth a quick look while editing.

## 3. The staging site is still publicly open

- `synergy.egowebdev.com` returns **HTTP 200** to anyone (verified 7/22). Cardinal
  flagged this as "password-protect immediately" — duplicate-content and link-equity
  leak.
- **Action:** password-protect or IP-restrict it.

## 4. Measurement plumbing on the site — we're partially blind

- **CSP is blocking Microsoft Clarity and Cloudflare Beacon** on every page load
  (Cardinal's finding; their "5-minute allowlist fix": add `scripts.clarity.ms` and
  `static.cloudflareinsights.com` to `script-src`).
- **1,310 sessions/90d land in GA4 with landing page "(not set)"** at 3.6%
  engagement — a tagging or consent-timing gap; ~6% of traffic measured badly.
- **GBP UTM casing is split** (`GBP / Organic` vs `gbp / organic`), halving
  listing-click reporting — if the GBP website links are yours, standardize one
  casing; otherwise we'll route to whoever manages the listings.

## 5. While you're in the templates — dev punch-list (Semrush crawl, Jul 21)

- **21 pages missing H1** (Cardinal's priority set: /book-an-appointment/, the
  insurance pages, /about-us/)
- **754 broken internal links** and **8 pages returning 4xx**
- **2 wrong entries still in the XML sitemap** + **57 orphaned sitemap pages**

None of these individually moves the needle like items 1–2, but they're all
trust/crawl hygiene the audit called out, and they're cheap while template work is
open.

---

Everything above sits in our live tracker
(`audits/cardinal-recommendation-tracker.md`) with the instrument that measures it —
each fix will show up in the data within days, and we'll report the before/after.
Shout if you want the raw pulls behind any of these.

— Joe
