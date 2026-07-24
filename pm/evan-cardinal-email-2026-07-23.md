# For Evan (Cardinal) — questions ahead of tomorrow's call (2026-07-23)

> Ready-to-send draft. Context: Monday's ops check-in + the 7/23 1:53 PM call both
> flagged this as a send-ahead item — the Evan/Cardinal conversation is **TODAY
> (7/24)**, so this needs to go out first thing to give Cardinal the questions before
> we talk (answers, not discovery). Framing per the meeting: ortho new patients up, spine new
> patients down after the Liine go-live — cause unclear. Below pairs the room's
> questions with what our live measurement already shows, so Cardinal can respond
> precisely. Tone: collaborative — Cardinal is our partner on the readout.
> Evidence + instruments: `audits/cardinal-recommendation-tracker.md`.

---

## ⭐ TL;DR — the three things I need from Cardinal before we talk

1. **Do you agree the May 1 Core Web Vitals regression is the primary driver of the
   organic decline** — or did Cardinal make keyword/targeting changes in that same
   window that could explain the ortho-up / spine-down split?
2. **Help me separate the two "spine declines"** — organic spine was already near-zero
   before any of this (52 organic sessions to the spine hub in 90 days), so a
   "spine new-patient" drop is almost certainly a **paid/conversion or capacity**
   story, not an SEO one. Which lever is Cardinal seeing move?
3. **The Gemini/Cloudflare block we put up after the privacy incident** also disallows
   GPTBot/ClaudeBot/Google-Extended — does that conflict with the AIO/GEO
   recommendations in your audit, and how do you want to reconcile it?

Detail and the data behind each below.

---

Evan — ahead of today's call, wanted to send the questions in advance with the numbers
we're seeing on our side, so we can spend our time on answers.

First, the good news on your audit: the **speed regression is fixed.** PageSpeed field
data (run 7/22) shows LCP recovered from a failing **3.5s to ~1.4s** across the
homepage, spine hub, carpal tunnel, TKA, and Sterling Heights pages — lab scores
roughly doubled. Whatever dev work shipped, it worked.

## 1. Ortho up, spine down — what actually moved, and when

The framing from our side was that ortho new patients rose and spine fell after the
Liine go-live, and we couldn't explain it. Two things I want to pressure-test with you:

- **The organic timeline points at May 1, not at Liine.** GA4 organic sessions:
  Mar 6,163 → Apr 5,264 → **May 3,027 (−42%)** → Jun 3,209 → Jul ~2,750. That −42%
  cliff lands exactly on the CWV regression your audit documented (238 "Good" URLs → 0
  by May 13). GSC agrees: impressions/day −27% and average position slid 10.9 → 13.3
  post-audit. Most concrete casualty — **the carpal-tunnel page fell from position
  ~1.4 to ~17, impressions −92%.** So the organic decline looks like a
  sitewide CWV/ranking event, and it predates Liine. **Does Cardinal's data agree, or
  did any keyword/targeting/content changes land in the same April–May window that
  we should factor in?**

- **Liine is call-tracking, not optimization** — so if ortho/spine new-patient volume
  really tracks to the Liine go-live, the mechanism is more likely **attribution or
  the signal it feeds into Blue Ox's bidding** than anything organic. Is that how
  you're reading it too? (We just turned on Liine→GA4 forwarding on 7/22, so we can now
  see booked-patient events next to campaigns — happy to share whatever helps.)

## 2. Which "spine decline" are we actually solving?

This is the disambiguation I most want aligned before we go deep:

- **Organic spine was already near-zero** long before this — the spine hub gets 2,803
  sessions in 90 days but only **52 from organic search (~4/week)**, and the stenosis
  page gets 4 visits/90 days at 0% engagement. Organic spine can't "decline"
  meaningfully because it was never there. So a spine **new-patient** drop is almost
  certainly a **paid-conversion, referral, or clinic-capacity** story (the ops team is
  already working the clinic-day-balance and provider-schedule side).
- **Where is Cardinal seeing the spine decline register** — paid conversions, call
  volume, or organic? That tells us whether tomorrow is a Blue Ox / paid conversation,
  a scheduling conversation, or an SEO one. Our read: the SEO fix for spine is
  net-new (the 5 condition hubs in your Phase-2 roadmap), not recovering something lost.

## 3. The Gemini / Cloudflare block vs. your AIO recommendations

Heads-up on a live tension. After the incident where an orphaned page with personal
family info got indexed by Gemini, we blocked Gemini at the Cloudflare level. But the
**same managed rule now disallows GPTBot, ClaudeBot, Google-Extended and CCBot**, and a
bot challenge is fronting **/llms.txt** — which cuts against your audit's "do not block
bots that serve live user queries" and the whole AIO/GEO program. **How do you want to
reconcile the privacy block with AI visibility** — a narrower rule that keeps retrieval
bots in while keeping the specific page out? (Regular Googlebot indexing is unaffected.)

## 4. Two quick asks to close out Phase 1

- **The 75-query AIO tracking set** — can you share the query list + baseline so we
  measure AIO on the same set you do?
- **The exact CWV regression trigger** — if you have the change that landed ~May 1
  (Cloudflare/security/CSP), it helps us make sure it can't silently recur. Our one
  remaining CWV blocker is CLS at 0.11–0.12 (just over the 0.10 line) — a
  width/height template fix that's already teed up with Paul.

Not looking to relitigate the readout — just want tomorrow to be productive. Happy to
send the raw GA4/GSC pulls behind any of the above.

— Joe
