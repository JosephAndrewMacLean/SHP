# SHP Marketing — Full Team Performance Update

**Date:** 2026-07-23 · **Prepared for:** Joe (marketing/ops)
**Data grounding:** GA4 (property 370514163), GSC (synergyhealth.org), Semrush (project
30453033), and the June 2026 Cardinal audits. Fresh pulls today; Cardinal tracker last
verified 2026-07-22. Every clinical/legal-substantive item below is a **draft pending
human review** — nothing here is cleared to publish.

Each of the seven discipline specialists gave a full "what we need to improve performance"
update, each in its own lane and complementing (not duplicating) the external agencies
(Cardinal = organic/AIO plan + schema/tech; Blue Ox = Google Ads; Liine = call tracking).

---

## Director's synthesis

### The problem in one line
SHP has the **search footprint of a dominant regional provider but converts like a small
one**: 1.18M organic impressions / 90 days → ~13,668 clicks (**1.15% CTR** vs 3–5%
benchmark); **~80% of clicks are branded** (people who already know us) while **~58% of
impressions are non-branded** patients in research mode who never click. On top of that,
organic **fell off a cliff in May** (Mar 6,163 → May 3,027 sessions, −42%, still sliding to
a ~2,750 July run-rate) and average position slipped **10.9 → 13.3** — a rankings/visibility
collapse, not a click-through problem.

### Where all seven specialists converge (do these regardless of discipline)
1. **Unblock the technical floor first.** Three things suppress everything else and are
   near-free to fix: (a) **CLS still fails** (p75 0.11–0.12 > 0.10; cause = 203 images
   missing width/height + testimonial slider — one template fix) so rankings can't recover;
   (b) **Cloudflare robots.txt blocks the AI crawlers** (ClaudeBot, GPTBot, Google-Extended,
   CCBot) and fronts `llms.txt` with a bot challenge — the entire GEO/AIO program is
   self-blocked at the door; (c) **446 schema errors** incl. `sameAs` pointing to a
   competitor's `@mendelsonortho` YouTube. **Owner: Paul-dev + Cardinal + whoever holds the
   Cloudflare zone.**
2. **Harvest what already ranks but earns ~0 clicks.** The **neck-fracture / back-fracture
   clusters** rank pos 4–6 across dozens of high-intent symptom queries (neck fracture 4.6 /
   1,913 impr; broken neck symptoms 6.8 / 1,815; +25 more) and convert essentially nothing.
   SEO, AEO, AIO, and Content all independently flagged this as the **fastest, most certain
   win** — a title/meta + answer-block rewrite on pages we've already earned.
3. **Fix extractability.** 80% of pages read at Grade 12+; there are **0 FAQPage entities**
   and **0 rich results** (only TRANSLATED_RESULT). Answer-first Grade 6–8 blocks + real FAQ
   schema on pages we already rank on is what turns exposure into snippets (AEO), AI-Overview
   citations (AIO, 2,276 keywords exposed / near-zero cited), and chatbot mentions (GEO).
4. **Build the 5 spine hubs** (stenosis, herniated disc, sciatica, DDD, spondylolisthesis —
   near-zero today; topical authority 31.8 vs 70). This is the **organic side of the June
   spine shortfall** (B2C −71 vs budget; referrals already above plan). Content drafts,
   physician reviews, Cardinal deploys, SEO/AEO/AIO structure.
5. **Start PR authority links now** (longest lead time). **0 links from any MI hospital system
   or medical association since 2012** while competitors have 400+. This is the single biggest
   *un-owned* lever and it feeds SEO authority **and** GEO/AIO citation at once.
6. **Plant the flag in Troy / Oakland County** (~4,800 obtainable ortho patients/yr going to
   competitors; zero paid coverage there today). Guerilla community presence + PR local
   relationships + SEO local pages, all routed to the free, best-converting website booking
   path via Liine-tracked numbers.

### Suggested sequence
- **This week (unblock, near-free):** CLS template fix · Cloudflare crawler + llms.txt WAF
  decision · start the 754 broken-link / 57-orphan cleanup list.
- **Weeks 1–4 (harvest, low effort/high certainty):** neck- & back-fracture rewrite + first
  FAQPage · Grade 6–8 lead-answer rewrites on top ~10 non-branded pages · pull physician
  association-membership roster to kick off PR links.
- **Weeks 2–8 (build):** spine hubs stenosis + sciatica first, then 1/week · spine
  differentiation messaging · referral-network content kit · Troy community activations
  (farmers market has a Sept 30 clock).
- **Ongoing:** review velocity (Rater8) · AIO citation monitoring (need Cardinal's 75-query
  set) · authority-link outreach cadence.

### Cross-cutting compliance guardrails
No PHI / unconsented stories (HIPAA) · no superiority or unsubstantiated efficacy claims
(FTC) — keep the internal-DB "92% pain reduction" stat out of published/earned copy and
never next to a disclaimer · YMYL E-E-A-T: medical-reviewer byline + credentials + date +
sourcing on every clinical page · move off the accessibility overlay widget (ADA) · **don't
over-promise same-week speed** the scheduling system can't deliver — it's the top sentiment
risk and AIO will repeat it.

---

# Discipline sections

*(Full detail from each specialist below. Each ends with its own "Top 3 do-this-first.")*

---

<!-- SEO -->
## SEO — What we need to improve

**Headline:** Our organic sessions have fallen off a cliff (Mar 6,163 → May 3,027, −42%, still sliding to a ~2,750 July run-rate) while avg position slid 10.9 → 13.3 — this is a rankings/visibility collapse, not a click problem, and it's now sitting on top of a non-branded footprint we already fail to convert (1.18M impressions/90d, ~80% of the 13,668 clicks are branded). The fastest gains are finishing the CLS fix so rankings can recover, then harvesting pages that already rank but earn ~0 clicks.

Cardinal owns the 90-day organic plan (schema, CWV, spine hubs, URL consolidation). Below I reinforce those where the data says they're the blocker, and stake out the in-house white space Cardinal does *not* own — **authority links and local**.

---

- **[P1] Finish the CLS fix to unblock the ranking recovery** — LCP is repaired (p75 3.5s → 1.36–1.57s) but **CLS p75 is 0.11–0.12 on every page tested, still over the 0.10 "Good" line**. Named cause is one template-level fix: **203 images missing width/height** + the testimonial slider. Until this clears, Google keeps us at position 13.3 and the May cliff persists. *Ask:* Paul-dev applies width/height attributes at the template level and reserves slider space; Cardinal re-validates CrUX at the next 28-day window. *Impact × Effort: High × Low.* This is the single highest-leverage item and it reinforces Cardinal's #1 open recommendation.

- **[P1] Harvest the neck-fracture & back-fracture clusters — strong positions, ~0 CTR** — `/conditions/neck-fracture-broken-neck/` already ranks **pos 4–6 across dozens of high-intent variants** (neck fracture 4.6 / 1,913 impr; broken neck symptoms 6.8 / 1,815; fractured neck 5.5 / 663; neck fracture symptoms 4.7 / 658 + ~20 more) and converts ~0. `/conditions/back-fracture-break/` (back break 6.7 / 594 + ~6 variants) same story. These are already ranked — the gap is a title/meta + on-page match problem, not a ranking build. *Ask:* rewrite title/meta to match symptom-seeker intent ("Neck Fracture: Symptoms, Causes & When to See a Specialist"), add a symptom-led H1 and a "when to seek care / book" CTA; **content-creator** drafts, physician review for accuracy (YMYL). *Impact × Effort: High × Low.* Complements Cardinal's on-page lane; overlaps AEO (these are FAQ/snippet candidates — handoff to AEO section).

- **[P1] Fix the internal-link decay: 754 broken internal links + 57 orphaned sitemap pages + 8 4xx** — broken links and orphans bleed crawl equity and PageRank exactly when we're trying to recover rankings; orphaned pages can't be found by crawlers or internal users. *Ask:* Paul-dev + in-house run a crawl-driven fix list — 301 or repair the 754 broken links, re-link or remove the 57 orphans, resolve the 8 4xx. *Impact × Effort: High × Medium.* In-house can own the audit/prioritization (Semrush issues 8, 2); Paul-dev executes. New flags Cardinal's June audit didn't have — white space to hand them a ready list.

- **[P2] Consolidate the TKA and duplicate-URL sprawl to one canonical hub each** — **TKA has 4–15 competing URLs** (tka pos 9.7 / 12,819 impr / 0.01% CTR; tka medical abbreviation 8.9 / 10,159), plus carpal tunnel (3 URLs) and Southfield (9 variants), across 4 parallel URL structures. The split cannibalizes ranking signals and the intent is weak/informational — so pick one canonical page, 301 the rest, and set expectations (huge impressions, low commercial intent; treat as an authority/AEO asset, not a conversion play). *Ask:* Cardinal owns this consolidation (it's on their Phase 2–3 gate); in-house supplies the URL inventory + preferred canonicals. *Impact × Effort: Medium × Medium.* Reinforces Cardinal — flag that the carpal tunnel page separately **lost its #1 ranking (pos 1.37 → ~17)** in the regression, so consolidation there waits on ranking recovery.

- **[P2] Build the 5 missing spine hubs — the −71 B2C spine hole lives here** — stenosis, herniated disc, sciatica, DDD, spondylolisthesis have **near-zero organic presence** (stenosis page = 4 visits/90d, 0% engagement); topical authority **31.8 vs 70 benchmark**. This is the organic side of June's spine shortfall (B2C −71 vs budget; referrals already above plan). *Ask:* Cardinal owns hub production in their 90-day plan; **content-creator** feeds physician-reviewed drafts at Grade 6–8 with symptom-aware entry paths. *Impact × Effort: High × High.* This is a shared build — SEO provides keyword/intent mapping + internal-linking architecture (hub-and-spoke: each condition hub links to symptom, treatment, and the spine-provider bios); content + AIO/AEO own the answer format. Don't duplicate — coordinate.

- **[P2] Start the authority-link + local program — the biggest un-owned lever** — referring domains ~408 but **Authority Score 29, oldest editorial link 2012, and 0 links from Michigan hospital systems or medical associations** (Henry Ford, Corewell, McLaren, AAOS, MI Orthopedic Society — competitors have 400+). Cardinal is digital-demand focused and does **not** own earned links — this is in-house white space that *also* feeds AIO/GEO citations. On local: GBP is working (1,681 local-pack keywords, ~770 sessions/30d) but each clinic owns its county, and **Troy/Oakland is under-penetrated (~4,800 obtainable patients/yr)**. *Ask:* **in-house/PR** lands the first hospital/association link and 1–2 location citations; SEO ensures NAP consistency and per-location page architecture (finish the Southfield/legacy URL cleanup so each location page is the canonical local landing page). *Impact × Effort: High × High (slow-burn).* Pure white space — hand PR the link targets; SEO owns NAP + location-page architecture.

- **[P3] Repair E-E-A-T/schema trust signals that suppress YMYL rankings** — **446 structured-data errors** (Hospital @type cascade on 234 pages incl. all 42 physician bios), **sameAs still points to competitor `@mendelsonortho` YouTube**, and legacy Mendelson remnants (payment.mendelsonortho.com, legacy LinkedIn) fracture the brand entity. For a YMYL health site Google holds these to a high bar. *Ask:* Cardinal owns the schema rebuild (MedicalOrganization/Physician/MedicalClinic, error-free); in-house **governance** finishes the Mendelson→Synergy migration so sameAs and NAP are internally consistent. *Impact × Effort: Medium × Medium.* Reinforces Cardinal's open schema item.

**Compliance / E-E-A-T flags:** the fracture and spine-hub rewrites are clinically substantive — **draft pending physician review**, no unsubstantiated or superiority claims, cite sources + medical-reviewer byline + date (YMYL). Do not place a hard efficacy stat next to a disclaimer (reads as a guarantee, FTC). Keep the sameAs/NAP fix accurate — never point schema at an entity we don't control.

**Assumption vs confirmed:** session/GSC/Semrush numbers are confirmed (2026-07-23 pulls). Impact/effort and owner assignments (Paul-dev vs Cardinal vs in-house) are my judgment — confirm the CLS template fix and TKA consolidation are on Cardinal's active sprint before we double-book them.

**Top 3 do-this-first:** (1) finish the CLS width/height template fix — unblocks all ranking recovery; (2) rewrite titles/meta on the neck- & back-fracture pages that already rank 4–6 but earn ~0 clicks; (3) clean the 754 broken internal links + 57 orphans so crawl equity flows while rankings recover.

---

<!-- AEO -->
## AEO — What we need to improve

**Headline:** SHP has the rankings to *appear* but nothing to get *extracted* — 0 FAQPage schema, 0 rich results (only TRANSLATED_RESULT), and 80% of pages reading at Grade 12+ mean search engines and voice assistants read a competitor's answer aloud even on the 33 queries where we already snippet-qualify and the symptom clusters where we rank 4–6. The fix is answer-first content blocks at Grade 6–8 on pages we *already rank on*, wired to truthful FAQ/QA schema. This wins the direct answer without waiting on new demand.

*Assumption vs. confirmed: all numbers below are confirmed from GSC/Semrush/GA4 via the shared data brief and Cardinal tracker. What's assumed: exact SERP-feature presence per query (I spot-verified two — see items 1 and 4 — but a full 33-keyword snippet audit is a next step, not done here).*

---

**[P1] Capture the "broken neck / neck fracture" snippet + PAA box — we rank 4–6 and get ~0 clicks**
- *Improve:* Add a 40–60 word answer-first block (symptom definition + "this is a medical emergency, call 911 / talk to a provider" framing) and a 4–6 item PAA-style FAQ at the top of `/conditions/neck-fracture-broken-neck/`, then FAQPage schema on the visible Q&A.
- *Evidence:* Cluster ranks pos 4–6 across dozens of high-intent variants — neck fracture (4.6, 1,913 impr), broken neck symptoms (6.8, 1,815), symptoms of a broken neck (6.0, 622), fractured neck (5.5, 663), +20 more — converting ~0 clicks. I verified live: SHP already appears on page 1 for "broken neck symptoms," but Cleveland Clinic / UCLA / UVA own the answer box because their copy is answer-first and liftable; ours isn't. This is the single densest snippet-capturable cluster we have.
- *Ask + owner:* content-creator drafts the answer block + FAQ copy (Grade 6–8); **one spine physician confirms the symptom list + emergency framing is clinically correct** before publish; SEO/Randall places the block above the fold and Cardinal deploys FAQPage schema.
- *Impact × Effort:* High × Low (page already ranks; this is copy + schema, not new demand).

**[P1] Ship the first FAQPage schema so any rich result can appear at all**
- *Improve:* Stand up truthful, visible FAQ blocks on the pages we already rank on and mark them up with FAQPage/QAPage. Right now the extraction surface is empty.
- *Evidence:* **Zero FAQPage sitewide; 0 FAQ rich-result keywords; the only rich result Google shows us is TRANSLATED_RESULT** (GSC Jun 14–Jul 19). Meanwhile 2,276 keywords already trigger AI Overviews we're barely cited in and 33 keywords are featured-snippet-eligible. We are structurally invisible to every answer surface that reads schema.
- *Ask + owner:* This is Cardinal's schema-deployment lane (Phase-2 gate) — my hand-off is the **prioritized page list + the actual Q&A content**; I specify *which* questions per page, content-creator writes them, Cardinal deploys. Guardrail: schema only on genuine visible Q&A (FTC/Google policy) — no phantom FAQs.
- *Impact × Effort:* High × Medium (dependency on Cardinal's deploy cadence).

**[P1] Rewrite the top-ranked answer paragraphs to Grade 6–8 so they're liftable and voice-readable**
- *Improve:* Engines lift concise, plainly-worded sentences; voice assistants won't read a Grade-12 clause aloud. Rewrite just the lead answer block (not whole pages) on our top symptom/procedure pages.
- *Evidence:* **80% of pages read at Grade 12+**; brand standard is ~8th grade / Grade 6–8. A snippet-length answer at Grade 12 loses to a Grade-7 competitor even at equal rank — this is *why* we rank 4–6 and don't get extracted.
- *Ask + owner:* content-creator owns the rewrites; I supply the answer-block template (question-as-H2 → 40–60 word direct answer → supporting detail). Physician sign-off on any clinical wording changed.
- *Impact × Effort:* High × Medium.

**[P2] Win the definition snippet on procedure/injection queries (caudal ESI, TKA)**
- *Improve:* Add a one-sentence "What is X" definition block (paragraph-snippet format) + short FAQ on the injection and procedure pages.
- *Evidence:* caudal esi (8.1, 2,698 impr), caudal esi injection (8.0, 1,378), ~0 clicks; TKA cluster 18,060 impr/28d at 0.011% CTR. I verified live that Cleveland Clinic owns the "caudal ESI" definition box — a plain 1–2 sentence "toward-the-tail" style definition is exactly the format Google is lifting, and we don't have one. Note TKA is informational/ambiguous intent and split across 4–15 URLs — pair the answer block with SEO's URL consolidation or the snippet won't consolidate.
- *Ask + owner:* content-creator writes definition + FAQ; **pain-management physician confirms procedure description + effectiveness framing** (do NOT paste a hard "70–80% relief" stat next to a disclaimer — FTC/substantiation risk flagged in current-state). SEO handles TKA URL consolidation.
- *Impact × Effort:* Medium × Low.

**[P2] Build patient-decision FAQs on the 5 missing spine hubs — voice + PAA from day one**
- *Improve:* When stenosis, herniated disc, sciatica, DDD, and spondylolisthesis hubs get built, architect each with a natural-language FAQ layer ("is sciatica serious," "how long does a herniated disc take to heal," "do I need surgery for spinal stenosis," "is X covered by insurance") — the exact PAA/voice phrasing patients use.
- *Evidence:* These 5 hubs are at near-zero presence (stenosis page = 4 visits/90d, 0% engagement); topical authority 31.8 vs 70 benchmark. The −71 June spine shortfall is a B2C/organic-demand hole — decision-support FAQs are how we capture research-mode patients (58% of impressions are non-branded, never click).
- *Ask + owner:* This complements Cardinal's spine-hub build — I provide the FAQ question set + answer blocks per hub; content-creator drafts; physician reviews; SEO owns hub on-page/IA. Insurance-coverage answers must use the corrected payer taxonomy (Medicaid = select-provider, not flat "no").
- *Impact × Effort:* High × Medium (gated on hub build timeline).

**[P2] "Near me" + auto-injury voice/local answer blocks**
- *Improve:* Add concise, spoken-length answers with local intent ("Where can I get an MRI near me in [city]," "orthopedic surgeon near me," auto-injury/PIP questions) tied to location pages.
- *Evidence:* mri near me (pos 2.9), auto injury specialist near me (9.5, 375), auto injury services (9.2, 1,414, 0 clicks), orthopedic surgeon port huron (7.0, 196). Auto No-Fault PIP is a confirmed high-value spine channel; "near me" is dominant voice-query phrasing and we rank top-3 on mri near me already.
- *Ask + owner:* content-creator + SEO (local); ties to per-location/county strategy. No physician gate (non-clinical), but confirm auto/PIP intake details with ops.
- *Impact × Effort:* Medium × Low.

---

### Top 3 do-this-first
1. **Neck-fracture / broken-neck answer block + FAQPage** — densest cluster, already ranks 4–6, ~0 clicks; physician confirms emergency framing (P1).
2. **First FAQPage schema live** on already-ranking pages — we have 0 rich results but for TRANSLATED_RESULT; hand the page list + Q&A to Cardinal (P1).
3. **Grade 6–8 rewrite of lead answer paragraphs** on top symptom/procedure pages — 80% Grade 12+ is why we rank but don't get extracted (P1).

### Compliance / E-E-A-T flags
- **Every clinical answer block is a DRAFT pending physician review** — symptom lists, emergency framing, procedure descriptions, effectiveness claims. Escalate diagnostic/treatment wording; include "talk to your provider" framing on anything diagnostic.
- **FAQ/QA schema only on genuine, visible Q&A** (Google policy + FTC) — no schema-only phantom FAQs.
- **No hard efficacy stat next to a disclaimer** (reads as a guarantee — FTC); effectiveness numbers need peer-reviewed/attributed sourcing, not the internal database.
- **Date-stamp + medical-reviewer byline** on every answer page (YMYL E-E-A-T).
- **Insurance/coverage answers** must reflect the corrected payer taxonomy (Medicaid varies by provider — never a flat "no").

---

<!-- GEO -->
## GEO — What we need to improve

**Headline:** SHP's generative-engine program is self-blocked at the front door — our own Cloudflare-managed robots.txt disallows ClaudeBot, GPTBot, Google-Extended and CCBot (plus `ai-train=no`), and our llms.txt sits behind a bot challenge AI crawlers can't clear. Fix the door, then feed the engines the corroboration (third-party links) and citable source pages (spine hubs, FAQs) they actually quote. Until then, SHP has exposure without citation: our content shows up in 2,276 AI-Overview keyword footprints but earns near-zero mentions.

---

**[P1] Unblock the retrieval AI crawlers — decide training vs. retrieval deliberately**
- *Improve:* The Cloudflare "block AI bots" managed rule disallows GPTBot, ClaudeBot, Google-Extended, CCBot (+ Amazonbot, Applebot-Extended, Bytespider, meta-externalagent) and sets `Content-Signal: ai-train=no`. Cardinal's audit says verbatim *"do not block bots that serve live user queries."* Net effect: Claude can't index us at all; Google-Extended block cuts Gemini grounding; OpenAI/Common-Crawl training is refused.
- *Evidence:* Verified by direct fetch 2026-07-22 (tracker items 2, 6b — status ❌ FAILED). Note the upside: ChatGPT-User / OAI-SearchBot and PerplexityBot are NOT blocked, so live-query citation is already possible today — this is why the content items below matter even before the crawler fix.
- *Ask + owner:* Cloudflare-dashboard owner (Paul-dev / whoever holds the zone) makes one policy decision: unblock the **retrieval** bots (ClaudeBot for Claude indexing, Google-Extended for Gemini grounding) while separately choosing whether to allow **training** use (CCBot / `ai-train`). These are two different levers — frame it as a deliberate choice, not an on/off switch. Stay in lane: I specify which bots and why; the dashboard change is theirs.
- *Impact × Effort:* Very high × very low (single config change). This gates everything else.

**[P1] Make llms.txt actually readable + fix the robots.txt line**
- *Improve:* llms.txt is live and validly formatted (a Phase-1 win) but Cloudflare serves non-browser agents a "Just a moment…" challenge instead of the file, so its intended audience never reads it. There's also 1 malformed robots.txt line flagged (Semrush Jul 21).
- *Evidence:* Verified 2026-07-22 (tracker items 3, 6). 754 broken internal links and 57 orphaned sitemap pages further fragment what a crawler can traverse once let in.
- *Ask + owner:* Cloudflare owner adds a WAF skip rule for `/llms.txt` and `/robots.txt` so bots get the file, not the interstitial; also check the Cloudflare audit log around May 1 (challenge posture is a candidate co-cause of the CWV/organic cliff). Dev/Cardinal clean the malformed robots line.
- *Impact × Effort:* High × low.

**[P2] Fix the Mendelson entity confusion that fragments our knowledge graph**
- *Improve:* Generative engines resolve a brand to a single entity before they'll confidently cite it. Ours is split: schema `sameAs` points to a competitor's `@mendelsonortho` YouTube, and legacy `payment.mendelsonortho.com` / legacy-branded LinkedIn remain live. Models can't reliably attribute facts to "Synergy Health Partners" when the web says we're partly Mendelson and partly a competitor.
- *Evidence:* 446 structured-data errors persist including the sameAs→competitor pointer (tracker item 10, ❌); rebrand "incomplete behind the scenes" per current-state. This is E-E-A-T-critical, not cosmetic.
- *Ask + owner:* Dev/Cardinal correct the `sameAs` targets and complete the Mendelson→Synergy migration; marketing-director owns the governance sweep. Downstream: a consistent NAP + description across authoritative directories (and a legitimate Wikidata entry) so models bind the right facts to the right entity.
- *Impact × Effort:* High × medium.

**[P2] Earn third-party corroboration — the strongest GEO trust signal (PR hand-off)**
- *Improve:* Generative engines cite facts that appear across many independent, credible sources. We have almost none of the kind health models trust. This is the single biggest un-owned lever and it's a PR job, not a GEO one.
- *Evidence:* 408 referring domains but **0 from Michigan hospital systems or medical associations** (competitors have 400+); oldest editorial link is **2012**; authority score 29. When an LLM answers "who offers coordinated spine care in metro Detroit," the corroborating sources it leans on don't mention us.
- *Ask + owner:* **Hand off to pr-specialist** — target links/mentions from Henry Ford, Corewell/Beaumont, McLaren referral networks, AAOS, and the Michigan Orthopaedic Society. GEO's role is to specify *which* facts and pages we want corroborated (see original-data item below) so earned mentions reinforce citable claims.
- *Impact × Effort:* Very high × high (relationship-driven, slow) — start now because of the lead time.

**[P2] Publish the citable spine source pages (hubs + FAQs) engines can quote**
- *Improve:* Models quote clear claims, definitions, named frameworks, and FAQ Q&A pairs. We have none for our top growth line. The 5 foundational spine hubs — stenosis, herniated disc, sciatica, DDD, spondylolisthesis — are near-zero presence, there are **zero FAQPage** entities sitewide, and 80% of pages read at Grade 12+ (models and patients prefer Grade 6–8).
- *Evidence:* Topical authority **31.8 vs 70 benchmark**; stenosis page = 4 visits/90d at 0% engagement; 0 FAQ rich-result keywords (tracker). Meanwhile huge non-branded footprints already exist to feed — e.g. the neck-fracture cluster (neck fracture pos 4.6 / 1,913 impr) and caudal ESI (pos 8.1 / 2,698 impr) rank but earn near-zero clicks and no citations.
- *Ask + owner:* **content-creator** drafts physician-reviewed spine hubs + FAQ blocks structured for extraction (clear topic sentences, definitions, Q&A, dates, author credentials, medical-review byline). Overlaps Cardinal's spine-hub deliverable — coordinate, don't duplicate. Every clinically substantive line is a **draft pending human review**.
- *Impact × Effort:* High × medium.

**[P3] Publish original, honest local data models will cite because nobody else has it**
- *Improve:* The most defensible GEO asset is proprietary data — models cite it because it's unique and attributable. SHP could publish local ortho/spine access, cost-transparency, or de-identified outcomes data.
- *Evidence:* We have differentiators worth stating (integrated ortho+spine, same-week access, 96% recommend, 82/100 sentiment) — but current stats are sourced to a **non-peer-reviewed internal database**, and the "92% report significant pain reduction" figure already sits next to a disclaimer in a way that reads as a guarantee.
- *Ask + owner:* content-creator + clinical reviewers substantiate any figure before it's published as a citable fact; marketing-director + compliance sign-off. **Do NOT fabricate statistics** — in health, invented numbers are an FTC and patient-safety problem. Only publish what's verifiably backed.
- *Impact × Effort:* Medium-high × medium.

---

### Top 3 do-this-first
1. **[P1] Unblock the retrieval AI crawlers in Cloudflare** (ClaudeBot + Google-Extended at minimum; decide training separately) — one config change, gates the whole program.
2. **[P1] WAF skip rule so llms.txt/robots.txt are readable to bots** — cheap, makes the file we already built do its job.
3. **[P2] Kick off PR authority-link building** (0 hospital/association links since 2012) — longest lead time, so start now even though the payoff is slower.

**Compliance / E-E-A-T flags:** No fabricated stats or "original data" (FTC + patient safety). Substantiate every citable figure; don't place a hard efficacy stat next to a disclaimer (reads as a guarantee). Spine hubs/FAQs carry medical-review byline, credentials, and dates (YMYL). All clinically substantive copy is a draft pending human review.

**Assumption vs confirmed:** Crawler block, llms.txt challenge, 408 ref domains / 0 hospital links / 2012 oldest link, 446 schema errors, topical authority 31.8, and the AIO-keyword exposure are all confirmed (Semrush/GSC/direct-fetch, verified 2026-07-22). Cloudflare-dashboard ownership (Paul-dev vs. other) is assumed — confirm who holds the zone. Whether legacy LinkedIn/payment subdomain are still live is assumed from current-state notes, not re-verified this session.

---

<!-- AIO -->
# AIO — What we need to improve

*Google AI Overviews & Bing/Copilot in-search AI answers. This lens = being a **source inside the search engine's own AI summary**, distinct from AEO (classic featured snippets) and GEO (off-Google chatbots like ChatGPT/Perplexity/Gemini app). Complements Cardinal, who owns the AIO plan and the 75-query AIO tracking baseline.*

**Headline:** AI Overviews already render on **2,276 keywords** SHP is associated with, but our citation inside those answers is **near-zero** — we have the exposure and none of the credit. The fix isn't more exposure; it's making pages *extractable and grounded* (unblock Google-Extended, rewrite to Grade 6–8, add FAQ/Q&A structure, ship the spine hubs, and win each clinic's county-level AI answer) so Google/Bing build their summary *from us* instead of over us.

---

**[P1] Unblock Google-Extended so Gemini/AIO can actually ground on our pages** — robots.txt (Cloudflare-managed) currently disallows **Google-Extended** plus a blanket `Content-Signal: ai-train=no`. Google-Extended controls whether Gemini/AI Overviews can *ground* answers on our content; blocking it caps AIO citation at zero no matter how good the passages are. Classic Googlebot is unaffected, so this is pure AIO/GEO upside with no SEO downside. *Evidence:* 2,276 AIO-exposed keywords, near-zero citation; robots block verified 2026-07-22. *Ask + owner:* **This is GEO's crawler-access item — I'm not re-owning it, only flagging the AIO consequence.** GEO/dev (Paul + Cloudflare) flip the Google-Extended disallow in the Cloudflare "block AI bots" setting; treat training-refusal as a deliberate policy choice but stop blocking the *retrieval/grounding* bot. *Impact × Effort:* High × Low (one dashboard toggle; unlocks everything below).

**[P2] Rewrite priority pages to Grade 6–8, self-contained passages AIO can lift** — AI Overviews stitch together short, self-contained paragraphs that each answer one sub-question. **80% of SHP pages read at Grade 12+** — too dense to extract cleanly, so the model paraphrases a competitor instead. *Evidence:* 80% Grade 12+ (Cardinal); topical authority 31.8 vs 70 benchmark. *Ask + owner:* content-creator drafts a one-paragraph, plain-language "quick answer" block (definition + when-to-see-a-doctor caveat) at the top of the ~10 highest-exposure non-branded pages already ranking 4–10 (neck-fracture cluster: 1,913+1,815+658+622+663 impr; caudal ESI 2,698; back-fracture; auto-injury) — physician-reviewed, dated. Start with neck-fracture (strong pos 4–6, converts ~0). *Impact × Effort:* High × Medium.

**[P3] Add FAQPage / structured Q&A — we have literally zero** — AIO decomposes a query into a fan-out of sub-questions; explicit H2/H3 question headers + concise answers are the most liftable format, and FAQPage schema signals the Q&A boundaries. SHP has **0 FAQPage markup and 0 FAQ rich-result keywords** — we're invisible to the mechanism AIO runs on. *Evidence:* 0 FAQPage / 0 rich results (only TRANSLATED_RESULT appears); 33 featured-snippet keywords show the raw ranking exists to build on. *Ask + owner:* content-creator + dev add a 4–6 question physician-reviewed FAQ block (structured as clean Q/A, not marketing copy) to the spine hubs and top condition pages; dev deploys FAQPage schema (coordinate with Cardinal's schema workstream — same 446-error cleanup). *Impact × Effort:* High × Medium.

**[P4] Ship the 5 spine condition hubs — the AIO answers we can't win because the page doesn't exist** — for stenosis, herniated disc, sciatica, DDD, spondylolisthesis, AIO is already answering these high-intent queries entirely from competitors because **SHP has near-zero presence** (stenosis page = 4 visits/90d, 0% engagement). No page = no possible citation, and this is exactly where the **B2C spine hole (June −71 vs budget)** lives. *Evidence:* topical authority 31.8 vs 70; 5 hubs near-zero; spine +89% growth line. *Ask + owner:* content-creator builds each hub as a fan-out map (condition → symptoms → causes → treatments → surgery vs. conservative → recovery → when to see a doctor), each sub-section a liftable Grade 6–8 passage with a named medical reviewer + date. Cardinal owns hub delivery in the 90-day plan — coordinate so structure is AIO-optimized, don't duplicate. *Impact × Effort:* High × High.

**[P5] Win the local AIO answer per county — each clinic owns its geography** — "orthopedic surgeon near me / [county]" and location queries increasingly get an AI Overview that names 2–3 providers; SHP is a location-specific business (61–73% of patients local, each clinic owns its county) yet **schema still misattributes entity type (Hospital @type cascade on 234 pages) and sameAs points to the competitor @mendelsonortho YouTube** — actively feeding the AI wrong/legacy identity. Local pack works (1,681 keywords) but that's the map pack, not the AI answer. *Evidence:* 446 schema errors; sameAs→competitor; Oakland/Troy under-penetrated (~4,800 obtainable ortho patients/yr); orthopedic surgeon port huron pos 7.0. *Ask + owner:* dev fixes MedicalClinic schema + sameAs on the 8 location pages (part of Cardinal's schema fix); content-creator adds a plain-language "what we treat + which insurance + book" answer block per location, esp. Troy (currently no coverage) and Southfield. *Impact × Effort:* Medium-High × Medium.

**[P6] Stand up AIO citation monitoring + a correction path — we're currently flying blind** — AI Overviews are volatile and *can misrepresent* content; in a YMYL/health context a wrong summary is a real harm-and-liability risk. Today we measure exposure (Semrush AIO-keyword report) but **not whether/how SHP is cited or summarized**, and there's no Profound-equivalent citation tracker (flagged as a gap). We also can't run Cardinal's 75-query AIO baseline because **we still don't have the query set from Cardinal** — flag this as the blocker. *Evidence:* 2,276 AIO keywords tracked for exposure only; Profound = ❌ gap; 75-query baseline = ❓ unverifiable (need set from Cardinal). *Ask + owner:* marketing-director requests the 75-query set + baseline from Cardinal; in-house runs monthly manual prompt tests on the top ~20 spine/ortho queries, logs who's cited and any factual misstatement about SHP, and defines an escalation path (Google's AI Overview feedback + a page-fix loop) for errors. *Impact × Effort:* Medium × Low.

---

## Compliance / E-E-A-T flags
- **Sentiment risk is amplified by AIO.** AI Overviews for "[provider] reviews / wait time" can surface and synthesize complaints. Wait-time and over-promise-on-speed are SHP's top sentiment risks — **do not add "same-week / fast scheduling" claims to pages we're trying to get cited** unless scheduling can deliver; an over-promise that AIO repeats is worse than silence.
- **YMYL accuracy first.** Every liftable passage must carry a named medical reviewer + credential + review date, cite primary sources, and include appropriate clinical caveats ("see a doctor if…"). An inaccurate passage that AIO summarizes can cause real harm and liability — accuracy gates publication.
- **Substantiation:** keep the internal-database efficacy stat ("92% report significant pain reduction") *out* of citable passages until it has peer-reviewed backup, and never place a hard stat next to a disclaimer (reads as a guaranteed outcome — FTC).
- **Legacy-brand E-E-A-T damage:** sameAs→@mendelsonortho and legacy payment/YouTube/LinkedIn tell the AI we're a different, older entity — this actively undermines AIO trust attribution and overlaps the migration-governance item.

## Assumption vs confirmed
- **Confirmed (data):** 2,276 AIO keywords, 0 FAQPage/0 rich results, 33 snippet keywords, 80% Grade 12+, robots.txt Google-Extended block, 446 schema errors + sameAs error, spine-hub near-zero presence, June B2C spine −71. All cited from the shared brief / Cardinal tracker (verified 2026-07-22).
- **Assumption (not yet measured):** *which* pages/competitors AIO currently cites for our target queries, and whether unblocking Google-Extended lifts citation — unverifiable until we get Cardinal's 75-query set and run the monitoring in P6. "Near-zero citation" is inferred from exposure data + the schema/crawler blocks, not from a direct citation audit.

---

## Top 3 do-this-first
1. **Unblock Google-Extended** (P1) — one Cloudflare toggle removes the hard cap on AIO grounding; owned by GEO/dev, I'm flagging the AIO stakes only.
2. **Ship Grade 6–8 "quick answer" + FAQ blocks on the top ~10 already-ranking non-branded pages** (P2+P3) — physician-reviewed, structured Q&A; turns existing exposure (neck-fracture, caudal ESI, auto-injury clusters) into extractable, citable passages.
3. **Build the 5 spine hubs as AIO fan-out maps + fix location/sameAs schema** (P4+P5) — creates the pages AIO literally cannot cite today and corrects the identity we're feeding the model, directly targeting the −71 B2C spine hole.

---

<!-- CONTENT -->
## Content — What we need to improve

We have the search footprint of a dominant regional provider but convert like a small one: 1.18M organic impressions / 90 days → ~13,668 clicks (1.15% CTR vs a 3–5% benchmark), and ~58% of those impressions are non-branded patients in research mode who never click. The content engine's job is to build the pages those researchers actually land on and read — the 5 missing spine hubs, a Grade 6–8 rewrite, real spine differentiation, symptom-aware/decision content, and patient-first rescues of the high-impression pages that convert at ~0. Every clinical asset below ships as a DRAFT pending physician review; sources, author/reviewer bylines, and dates are built in for E-E-A-T/YMYL. Assumptions are flagged.

---

**[P1] Build the 5 foundational spine condition hubs** — Write publish-ready hub pages for spinal stenosis, herniated disc, sciatica, degenerative disc disease (DDD), and spondylolisthesis. Each: answer-first definition, symptoms, causes, when to see a doctor, conservative vs. interventional vs. surgical options, what-to-expect, recovery, and an FAQ block — Grade 6–8, with CDC/NIH/NASS/AAOS citations and a "talk to your provider" frame. *Evidence:* these five have near-zero presence today; topical authority is 31.8 vs a 70 benchmark, and the existing spine hub gets only ~52 organic arrivals/90 days (~4/week) despite 2,803 sessions. This is the −71 B2C spine hole from the June budget (169 actual vs ~240 planned), which lives on the consumer/organic side, not referrals. *Ask + owner:* one spine physician (of the 9-surgeon bench) confirms clinical accuracy and options framing per hub — 30–45 min each; content-creator drafts, SEO sets target keyword/URL, AEO structures the FAQ. *Compliance:* clinical DRAFT pending physician review; cite peer-reviewed/society sources, no efficacy or superiority claims, dated byline + named medical reviewer. *Impact: High · Effort: Med (produce 2 first — stenosis + sciatica — then 1/week).*

**[P2] Grade 6–8 readability rewrite of core patient pages** — Rewrite the highest-traffic condition/service pages down from Grade 12+ to Grade 6–8: shorter sentences, defined jargon, scannable lists, answer-first intros. *Evidence:* ~80% of pages read at Grade 12+, which suppresses both patient comprehension and AI extractability (AEO/AIO/GEO all prefer plain, structured language). *Ask + owner:* no new clinical sign-off where facts are unchanged — clinical reviewer only re-confirms any claim I simplify; content-creator owns the rewrite, SEO confirms which pages by traffic. *Compliance:* preserve substantiation; do NOT place a hard stat (e.g. the "92% pain reduction" line) next to a disclaimer — that reads as a guarantee (FTC). *Impact: High · Effort: Med (batch the top ~15–20 pages; start with the spine hubs above so it's one pass).*

**[P3] Rescue the neck-fracture & back-fracture zero-click clusters** — Patient-first rewrite + FAQ block for /conditions/neck-fracture-broken-neck/ and /conditions/back-fracture-break/. Reframe clinical copy into "what this means, symptoms, what to do now, how it's treated, recovery," and answer the exact symptom questions people search. *Evidence:* neck-fracture ranks strong (positions ~4–6) across dozens of high-intent variants — neck fracture (4.6, 1,913 impr), broken neck symptoms (6.8, 1,815), symptoms of a broken neck (6.0, 622), fractured neck (5.5, 663) + ~20 more — yet converts ~0. Back-break variants (back break 6.7, 594 impr) same story. We already rank; the copy just doesn't serve or convert the patient. *Ask + owner:* spine/trauma physician confirms the "when to seek emergency care" language (safety-critical) — 20 min; content-creator drafts, AEO structures FAQPage, SEO rewrites title/meta. *Compliance:* clinical DRAFT pending review; fracture = urgent-care territory, so triage/ER language must be reviewer-approved, sourced, and non-alarmist. *Impact: High · Effort: Low (2 existing pages, ranking already earned).*

**[P4] Spine DIFFERENTIATION messaging** — Write the spine story that "isn't messaged anywhere": a rewritten spine service-line page plus reusable messaging blocks (headline, why-us, provider-bench framing) built on younger fellowship-trained surgeons, minimally invasive techniques, and innovative technology — feeding the spine hubs, paid landing pages, and provider bios. *Evidence:* the audit says the spine page uses the same generic "fellowship-trained, coordinated care" as every other specialty; meanwhile the spine line is +89% growth with a patient base trending younger (median 60→56) and commercial-pay (42%→52%) — the exact audience this story speaks to. *Ask + owner:* spine service-line lead / a spine surgeon confirms which techniques and tech are accurate to claim and name — 30 min; content-creator drafts, marketing-director aligns brand, SEO/paid place it. *Compliance:* clinical DRAFT; every capability claim must be verifiable (no "best/most advanced" superiority language — FTC); name specific, substantiated techniques only. *Assumption flag:* the specific MIS procedures and tech platforms to name are NOT confirmed in our data — needs the clinical input above before drafting specifics. *Impact: High · Effort: Med.*

**[P5] Symptom-aware, pre-diagnosis + patient-decision/FAQ content** — Create the entry path for people who don't yet know their diagnosis: "Why does my lower back hurt?", "Numbness/tingling down your leg — what it could mean", "Neck pain: when to see a specialist", plus decision-support pieces ("Do I need surgery for a herniated disc?", "Conservative vs. surgical spine care"). All answer-first with clean FAQ blocks. *Evidence:* the site is built for patients who already know their diagnosis — there is NO symptom-aware entry path and ZERO patient FAQ/decision-support pages today, while 58% of impressions are non-branded researchers. This is also our FAQPage schema fuel (0 FAQPage today → feeds AEO/AIO). *Ask + owner:* spine physician confirms symptom-to-condition framing and the "see a doctor now vs. can wait" guidance — 30 min per batch; content-creator drafts, AEO structures for snippets/voice. *Compliance:* clinical DRAFT; symptom content must avoid self-diagnosis/fear-mongering and route to a provider; sourced and reviewer-signed. *Impact: High · Effort: Med (start with 3 symptom pages that map to stenosis/sciatica/herniated disc so they interlink with P1).*

**[P6] UGC-style 9:16 video scripts (PT-led athlete storytelling)** — Produce short-form vertical scripts for the format that's already working: PT-led, natural straight-on provider shots, athlete/recovery storytelling. Deliver 6–8 scripts (:30–:60) with hook, beats, on-screen text, and CTA, formatted 9:16 for feed. *Evidence:* the audit names PT-led UGC athlete storytelling and natural provider shots (e.g. "Dr. Kyle" in-office) as what's working; 16:9 videos underperform in feed and current videos open too clinical with dated renders and double Mendelson end cards. *Ask + owner:* PT lead / featured provider confirms clinical accuracy of any exercise or recovery claim — 15 min per script; content-creator writes, social/video produces. *Compliance:* no PHI / no unconsented patient stories (use provider-led or consented/actor framing); disclose any AI-generated media; exercise guidance carries a "check with your provider" line; drop the legacy Mendelson end card. *Impact: Med · Effort: Low.*

---

### Auto-injury / PIP content angle (high-value spine channel — note)
Auto No-Fault PIP + Workers' Comp are accepted across all carriers with no referral and no auto copay — a high-value spine channel — and we already surface for it with zero clicks: auto injury services (9.2, 1,414 impr, 0 clicks), auto injury (9.7, 677), auto injury specialist near me (9.5, 375). Recommend a dedicated, patient-first auto-injury/PIP page (what to do after a crash, how PIP covers spine care, no-referral/no-copay explainer) as a fast P2/P3 add once the P1 hubs are moving. Clinical + billing/legal review required (PIP coverage claims are legally substantive — DRAFT pending both). *Assumption flag:* treat coverage specifics as needing billing/legal confirmation before publish.

---

### Top 3 do-this-first
1. **Draft the first 2 spine hubs — stenosis + sciatica** (P1). Biggest lever on the 31.8→70 authority gap and the −71 B2C spine hole; get one spine physician to confirm each (30–45 min).
2. **Rescue neck-fracture + back-fracture** (P3) — lowest effort, highest certainty: we already rank positions 4–6 on thousands of impressions and convert ~0. Patient-first rewrite + FAQ + one physician safety check on ER/triage language.
3. **Draft the spine differentiation messaging** (P4) — unblocks paid LPs, hubs, and bios; needs 30 min of spine-surgeon input to confirm which techniques/tech we can name before I write specifics.

---

<!-- PR -->
## PR & Earned Authority — What we need to improve

**Headline:** PR/earned media is the single biggest *un-owned* growth lever we have: SHP has run **no media-relations or editorial-link program since 2012**, and holds **0 backlinks from any Michigan hospital system or medical association while competitors have 400+** (Cardinal/Semrush). That gap simultaneously starves SEO authority (referring-domain Authority Score stuck at 29) *and* the third-party corroboration that AI Overviews/GEO citations require — so earned coverage is the one input that pays off in three channels at once. Fixing it is mostly relationship and outreach work no agency owns, and it maps directly onto the Oakland County / Troy growth opening and the spine mandate.

*Ownership note: this section covers earning the mentions, links, and relationships. The SEO specialist frames the link-placement/authority value; GEO/AIO frames the citation impact — handoffs flagged inline.*

---

**[P1] Stand up a Michigan medical-authority link & relationship program (the 2012 gap)** — We have zero editorial links from MI hospital systems or medical associations; the oldest editorial link on the domain is from **2012**, referring-domain Authority Score is **29**, and topical authority is **31.8 vs a 70 benchmark**. Competitors carry **400+** of exactly the links we lack. Start with organizations SHP physicians can plausibly already belong to: **Michigan Orthopaedic Society** (~300 orthopedic surgeons; miorthosociety.org), **Oakland County Medical Society** (~1,500 physicians, based in Bingham Farms — directly on top of our Troy/Oakland target), and **Michigan State Medical Society**. These offer member directories, physician spotlights, and event/CME listings that produce durable authoritative links.
- *Ask + owner:* Marketing pulls a roster of which SHP physicians hold MOS/OCMS/MSMS membership (owner: practice leadership / credentialing, 1 spreadsheet); PR then requests directory listings + one member-spotlight per quarter.
- *SEO handoff:* SEO scores link-placement value and confirms the sameAs/entity targets. *GEO/AIO handoff:* each association mention is a corroboration source for the physician-entity graph.
- *Impact × Effort:* High × Medium. Assumption: that some SHP physicians already hold these memberships (needs confirmation — likely, given ~42 physicians).

**[P1] Build the referral-network earned-relationship engine (spine's highest-leverage channel)** — Spine runs **32% B2B — the highest referral dependency of any line** (1,360 spine NPs, Jan–Jul), and the physician-liaison engine is real but concentrated: **Kristen carries ~51% of all B2B volume at ~70 NP/100 visits** while others run 6–40 (Q2-2025: 2,208 visits → 743 NPs = 33.6/100). PR's role is the *earned-authority layer* under the liaisons' feet: co-branded clinical-education content, referring-provider newsletters, "meet the spine bench" materials, and roundtable/CME events for the feeder specialties — **PCP, PT, chiro, pain management, ER/urgent care, and the workers'-comp / auto-attorney channel**. **Auto No-Fault PIP is a confirmed high-value spine channel** (accepted all carriers, no referral, no copay) and GSC shows live demand we don't capture ("auto injury services" pos 9.2, 1,414 impr, ~0 clicks).
- *Ask + owner:* Marketing-director + Kristen convert her top-producing playbook into a repeatable referring-provider content kit (owner: PR drafts, PL team distributes); load the **currently-empty Universal Spine Target-Account list** with a tiered feeder list for PR to build materials around.
- *Impact × Effort:* High × Medium. Note: referrals are already **+14 above June budget** — this is about raising candidate *quality* and defensibility, not doubling volume (the −71 spine hole is B2C, not referral).
- *Compliance:* No PHI in any co-branded/referring material; any auto/PI-attorney outreach stays factual and non-solicitous — route through legal.

**[P1] Finish the Mendelson→Synergy migration for entity/brand consistency** — The rebrand is **incomplete behind the scenes**: legacy `payment.mendelsonortho.com`, YouTube `@mendelsonortho`, and legacy-branded LinkedIn all persist — and the site's schema `sameAs` still points to the **competitor `@mendelsonortho` YouTube**, inside the 446 open structured-data errors. Every press release, pitch, and directory listing we send amplifies whichever name we don't consolidate, splitting the entity that AI models and journalists resolve. PR can't fix schema, but PR owns the *external* name surface (bylines, boilerplate, media directories, association profiles, HARO-style responses).
- *Ask + owner:* Marketing-director drives a one-name standard; PR maintains a canonical boilerplate + spokesperson list; dev/Cardinal fix the schema sameAs (flagged, not ours). *GEO/AIO handoff:* entity consistency is a direct citation-quality input.
- *Impact × Effort:* High × Low (for the PR-surface portion). Confirmed gap.

**[P2] Thought-leadership program to build E-E-A-T around the spine bench** — The audit says spine's real story — **younger, minimally-invasive, technology-forward surgeons — "isn't messaged anywhere,"** yet the 9-physician spine bench is our differentiator and the patient base is trending younger (median 60→56) and commercial-pay (42→52%). National spine trade press is actively publishing exactly this angle right now (**Becker's Spine Review**, e.g. "What will define spine in 2026," minimally-invasive/motion-preserving coverage). Pair one national trade byline with local outlets — **Crain's Detroit Business, DBusiness, Oakland Press, and Detroit TV health desks (WXYZ/WDIV/Fox 2)** — leading local-first per brand strategy.
- *Ask + owner:* Practice leadership names 2–3 spine spokespeople and confirms credentials/fellowships (owner: clinical); PR drafts one trade byline + one local pitch per quarter. All bylines are **drafts pending clinical + legal review**.
- *SEO/GEO handoff:* bylines become authoritative author-entity signals and citable sources.
- *Impact × Effort:* Medium-High × Medium.
- *Compliance:* No superiority/"best" claims (FTC); no unsubstantiated efficacy stats — the existing "92% pain reduction" stat sits next to a disclaimer (reads as a guarantee) and is sourced to a non-peer-reviewed internal DB. Keep it out of earned materials until substantiated.

**[P2] Reputation & review-velocity program (Rater8) as an earned-trust engine** — Reviews are our most scalable third-party corroboration and directly feed local trust, GBP, and AIO. We have strong raw material — **96% recommend rate, 82/100 sentiment** — but no active velocity program in our stack yet (Cardinal's review-velocity item is open; Rater8 is the named tool, currently a vendor/API ask). Local pack already works (1,681 local-pack keywords, ~770 GBP sessions/30d) so review volume compounds an existing strength, especially for the **Troy** location we're trying to grow.
- *Ask + owner:* Santosh/ops confirm Rater8 is live and pulling a post-visit review flow per location; PR + guerilla own response templates and the Troy-first push.
- *GEO/AIO handoff:* review corpus is a primary AIO citation source; *guerilla handoff* for in-clinic activation.
- *Impact × Effort:* Medium-High × Low-Medium.
- *Compliance:* Never solicit or edit reviews for content (FTC endorsement rules); no PHI in any response; don't confirm someone is a patient in a public reply.

**[P3] Capture every PR win as a citable, linkable asset (make earned media compound)** — Today we have no system to turn a media hit into a durable link + citation. Given the 446 schema errors, 754 broken internal links, and a domain that AI training crawlers are blocked from (robots.txt blocks GPTBot/ClaudeBot/Google-Extended), an uncaptured hit evaporates. Every release, byline, award, and partnership announcement should land on a stable SHP newsroom/press URL with correct author/organization schema, then be logged for outreach follow-up.
- *Ask + owner:* PR maintains a press-hit log with URL, anchor, and date; SEO owns the newsroom URL structure + schema; dev/Cardinal own the crawler-access posture (flagged, not ours).
- *Impact × Effort:* Medium × Low. Builds the pipe the other six items flow through.

**[P3] Awards & community-partnership announcements tied to Oakland/Troy** — Low-cost earned coverage that also seeds association and local-media relationships in the exact geo where **~4,800 obtainable ortho patients/year** are going to competitors. Local business awards (Crain's, DBusiness, Corp! Magazine "Best of") and community-health partnerships generate authoritative local links and give liaisons a warm reason to engage feeder practices.
- *Ask + owner:* PR builds a rolling awards/deadlines calendar + a Troy/Oakland partnership target list; coordinate with guerilla on activations.
- *Impact × Effort:* Medium × Low-Medium.

---

### Top 3 do-this-first
1. **[P1] Michigan medical-authority link program** — confirm which SHP physicians hold MOS / Oakland County Medical Society / MSMS memberships and claim directory + spotlight placements. Attacks the 0-links-since-2012 gap head-on and lands in the Oakland/Troy target geo.
2. **[P1] Referral-network earned-authority engine** — productize Kristen's playbook into a referring-provider content kit and load the empty spine target-account list, prioritizing the PCP/PT/chiro/pain-mgmt and auto-No-Fault-PIP feeders that spine (32% B2B) leans on most.
3. **[P1] Finish the Mendelson→Synergy external name consolidation** — one canonical boilerplate/spokesperson standard across all earned surfaces so every hit builds one entity, not two.

*Compliance line for the whole section:* no PHI or unconsented patient stories (HIPAA); no superiority or unsubstantiated efficacy claims (FTC) — keep the internal-DB "92%" stat out of earned materials; reviews and endorsements must follow FTC rules (no incentivized/edited reviews); all clinical or legal-adjacent copy (bylines, referral/auto-attorney outreach, crisis statements) is a **draft pending clinical + legal/compliance sign-off** before release. Assumptions flagged inline; the biggest one to confirm is physician association membership.

---

<!-- GUERILLA -->
## Guerilla & Community — What we need to improve

**Headline:** Troy/Oakland is a ~4,800-patient/yr ortho opening where we run *zero* paid
coverage — the cheapest way to plant a flag there is boots-on-the-ground community
presence, not more ad spend. Every activation below routes to the **free, best-converting
channel (website booking, 74.7% capture, $0)** via a **unique Liine-tracked number + vanity
booking URL**, so we measure *booked patients* (~$150 value), not just handshakes — and each
one is built to throw off 9:16 PT-led clips for content/PR to amplify.

---

**[P1] "Back to Active" spine/back-pain workshop series — Troy** — Monthly evening
education sessions (a spine PT + one of the 9-physician spine bench) at a Troy venue (Troy
Community Center, a partner gym, or a library room): posture, disc/DDD basics, sciatica,
"when back pain means see a specialist," self-care. Education *only* — not a screening.
Directly targets the **B2C spine hole (−71 vs June budget)**, which is a consumer-demand
problem in exactly this geo, and the younger/commercial-pay shift (18–34 now 21%). *Capture:*
event-specific Liine vanity number on the slide/handout + QR to a Troy-spine booking page;
consented sign-in for follow-up. *Cost/effort:* low ($200–500/event, room + printed cards +
giveaway); medium coordination with clinical staff. *Owner:* Guerilla leads; clinical
presenter via practice leadership; clips → content-creator; media list → PR.

**[P1] Sports-injury / "Athletic Trainer's Table" nights with Troy-area schools & clubs** —
Pre-season and in-season injury-prevention clinics with Troy School District athletics (29
sports), the Oakland Activities Association schools, and Breen Track Club: ACL/ankle/overuse
prevention, warm-up mechanics, "what a real injury looks like." Feeds ortho/sports-med and the
younger commercial-pay base; strong, ongoing UGC. *Capture:* team/club-specific QR + a
"priority sports-injury" Liine line; hand-out cards. *Cost/effort:* low, mostly staff time +
branded warm-up/first-aid giveaways. *Owner:* Guerilla + a sports-med provider; PR pitches the
school-partnership story.

**[P1] Troy Farmers Market "Ask Our PT" booth** — Recurring presence at the Troy Farmers
Market (Stine Community Park, Fridays 11–4 / Weds 3–7 **through Sept 30**) and Family Daze
(Sept 17–20): a PT answering movement/posture questions, free tips, branded hydration/
giveaways, kid stretch demos. Frame as "ask a PT," **not** a screening (movement screens are
clinical). Cheapest repeatable foot traffic in Troy this summer. *Capture:* booth QR → Troy
booking + a market-specific Liine number; scan/sign-up count per market day. *Cost/effort:*
low ($50–150 stall fee + tent + collateral). *Owner:* Guerilla + PT volunteer; content-creator
shoots verticals on site.

**[P2] Southfield podiatry summer deepening — running-club + employer plays** — Partner with
Oakland running clubs/local 5Ks and Southfield employers for "Happy Feet" lunch-and-learns and
race-day foot/ankle tips (plantar fasciitis, running form, diabetic-foot awareness). Leans into
**Foot +114% growth** and Southfield as the confirmed near-term deepening target. *Capture:*
Southfield-podiatry QR/vanity URL + dedicated Liine number; race bib-bag insert with trackable
code. *Cost/effort:* low–medium (sponsorship + inserts). *Owner:* Guerilla + a DPM; PR for
race/employer co-promotion.

**[P2] Auto-injury & workers'-comp community education channel** — Info sessions and a
co-branded "after a crash / after a work injury — your care options" resource card with local
PI/WC attorneys, employers, and urgent-care/PT partners. Ties to the **Auto No-Fault PIP + WC
high-value spine channel** (no referral, no auto copay) and the auto-injury search queries we
rank for but never convert. *Capture:* a dedicated auto/WC intake Liine number + landing URL,
so we can attribute this feeder cleanly. *Cost/effort:* low (print + relationship time).
*Owner:* Guerilla + PR referral-network work; **flag for legal sign-off** (attorney co-branding).

**[P3] QR "point-of-pain" placements + gym/PT/running-store co-marketing (quick win)** —
Trackable, symptom-aware QR cards where pain actually shows up in Troy/Oakland: gyms, running
stores, CrossFit boxes, PT clinics, chiro, urgent care. "Back, neck, knee, or foot pain? Get
answers → book." Near-zero cost, always-on, and it seeds local links/mentions that ladder to
SEO. *Capture:* per-location QR codes → booking + Liine numbers, so we rank partner venues by
booked patients. *Cost/effort:* very low (card printing + drop-offs). *Owner:* Guerilla;
partner outreach shared with PR.

---

### Top 3 do-this-first
1. **Troy Farmers Market "Ask a PT" booth** — the market season ends Sept 30, so this is the
   only item with a hard clock; cheapest repeatable Troy foot traffic + UGC available now.
2. **"Back to Active" Troy spine workshop series** — aims straight at the B2C spine demand
   hole in the exact under-penetrated geo; recurring, and every session is content.
3. **Sports-injury nights with Troy schools / Breen Track Club** — locks in ortho/sports-med
   with the younger commercial-pay base and builds durable community relationships + links.

---

**Compliance flags:** (1) Any "screening" is a *clinical* activity — requires licensed staff,
written protocols, and sign-off; keep public activations to **education + Q&A**, not diagnosis.
(2) **No PHI**, no on-site patient stories without written consent; consent required for all
filming. (3) **No guarantees / no promising same-week access** at events — wait-time
over-promising is our top sentiment risk. (4) Public-space activations need **permits, liability/
insurance, and ADA-accessible venues**. (5) Attorney/WC co-branding needs **legal review**.

**Assumption vs. confirmed:** Confirmed from data — the ~4,800 Oakland/Troy ortho opening, no
Troy paid coverage, Southfield podiatry as near-term target, Foot +114% / spine B2C −71,
website = free best-converting channel, PT-led 9:16 UGC working, PIP/WC as spine channel, live
Troy market/school/club venues (web-verified). Assumed / to confirm — that Liine can provision
**per-campaign tracking numbers** and the site supports **location/service vanity booking
URLs** (needed for clean attribution); specific partner (schools, clubs, attorneys, employers)
willingness; clinical-staff availability for events. All partnership execution/amplification
hands to PR; clip production hands to content-creator.

---

## Notes on method & limits
- The seven sections were produced by the discipline subagents from a shared data brief
  built from today's GA4/GSC/Semrush pulls plus the Cardinal tracker. Numbers are confirmed;
  owner assignments (Paul-dev vs Cardinal vs in-house) and impact/effort are specialist
  judgment — confirm against Cardinal's active sprint before double-booking work.
- Open items that need a human/vendor unlock: the 75-query AIO baseline (from Cardinal),
  Liine per-campaign tracking numbers + vanity booking URLs (for guerilla attribution),
  Rater8 review flow status, and confirmation of which SHP physicians hold MOS/OCMS/MSMS
  memberships (for the PR link program).
