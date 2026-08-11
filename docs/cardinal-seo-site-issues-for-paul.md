# Cardinal SEO Audit — Site Issues for Implementation (Paul)

**Source:** Cardinal Digital Marketing, *Organic Search and AI Optimization Audit* (June 2026) —
full text in `audits/cardinal-2026-06/organic-aio-audit.md` (cited below by Pillar/Table and
line number). Status columns come from `audits/cardinal-recommendation-tracker.md` (verified
2026-07-22/27 via GSC, Semrush, PSI) and the **2026-08-11 Screaming Frog crawl**
(`data/screamingfrog-crawl-2026-08-11.csv`).

**How to read this:** items are grouped in Cardinal's priority order (their Phase-1 "stop active
losses" items first). ✅ = verified done, don't redo · 🟠 = partially done, finish noted ·
❌ = open · ❓ = can't verify from our side, needs your confirmation.

---

## 0. Already done — verified, don't redo

| Item | Cardinal ref | Verified |
|---|---|---|
| Staging domain `synergy.egowebdev.com` password-protected | Pillar 13 (line 84: "still live and crawlable") | ✅ HTTP 401, 2026-07-22 |
| `llms.txt` created at domain root | Table 17 (line 379: "30-minute task") | ✅ live & valid; AI-crawler access end-to-end verified 2026-07-27 (ClaudeBot/GPTBot UA → 200; `Content-Signal` header present) |
| Robots.txt AI-crawler allowance (line 382: "Do not block bots that serve live user queries") | Table 17 | ✅ verified 2026-07-27, incl. GSC URL Inspection (`robotsTxtState: ALLOWED`) |
| Missing meta descriptions — 55 pages incl. 7 location pages (Table 8 line 289; Table 15) | Pillars 5/10 | ✅ Semrush 2026-07-21: **0 flagged** |
| LCP regression (part of the May 1 CWV event, Table 11/12) | Pillar 7 | ✅ field p75 now 1.36–1.57s (was 3.5s) — **but see §1: CLS still failing** |
| Parallel URL structures / duplicate clinical content (Table 5 line 266: "4 active structures… carpal tunnel alone has 3 separate URLs, TKA has 4") | Pillar 2 | 🟠 **~⅔ implemented** per Aug 11 crawl: 267 of 585 audited URLs now 301 (cwt→/conditions/, /specialties/→/specialty/ migration). Remainder in §3. |
| Sitemap 404s/301s (Tables 3–4: 10 dead + 17 redirecting URLs listed at lines 253–262) | Pillar 1 | 🟠 GSC now reports 0 errors / 0 warnings, 343 URLs (was 412 with 128 non-indexable); Semrush still flags 2 wrong entries — final pass in §3 |

---

## 1. P0 — Finish the Core Web Vitals recovery (CLS is the last failing metric)

Cardinal's most urgent finding (Pillar 7, line 54): *"A CWV regression event occurred on
approximately May 1, 2026… By May 13, Good URLs reached zero… LCP field data is 3.5 seconds,
CLS is 0.11, and the Lighthouse mobile performance score is 28/100."* Regression timeline:
Table 11 (lines 317–323). LCP is fixed; **CLS p75 still reads 0.10–0.12 (pass line = 0.10)** —
these are the CLS/perf items still open, all from Table 12 (lines 327–337):

| # | Issue (Cardinal's numbers) | Cardinal's fix | Ref | Status |
|---|---|---|---|---|
| 1.1 | **203 images missing width/height — "confirmed CLS contributor"**; named offenders: `spine.svg, hip.svg, knee.svg, shoulder.svg, elbow.svg, foot-ankle.svg, back-neck.svg, hand-wrist.svg` + 18 affiliate logos | "Add explicit width and height to all image elements. Template fix resolves majority." | Table 12 line 336; Table 8 line 295; roadmap line 603 | ❌ **the named remaining CLS cause** |
| 1.2 | **DOM 27,528 elements (threshold 800); testimonials slider alone = 3,126 children** | "Virtualize the testimonials carousel to render only visible and adjacent slides." | Table 12 line 334 | ❌ |
| 1.3 | logo.svg 1,032KB, 4-hour cache TTL | "Optimize to <20KB; extend static asset TTL to 1 year (`max-age=31536000`)." | Table 12 line 328 | ❓ verify (lab scores improved — confirm the logo itself) |
| 1.4 | home.mp4 hero video 11,163KB | "Compress to <2MB (H.264 720p); add `poster` attribute." | Table 12 line 329 | ❓ |
| 1.5 | 50+ render-blocking CSS files (est. 2,540ms) | "Consolidate into a single minified stylesheet; load non-critical CSS async." | Table 12 line 332 | ❓ |
| 1.6 | Hotjar 3,443ms CPU/page — running **alongside** MS Clarity (dual session recording) | "Defer to GTM scroll trigger or remove if Clarity suffices." | Table 12 line 330 | ❓ |
| 1.7 | liine.com JS 343KB, 86% unused, every page | "GTM window-load trigger; load only on contact/location pages." | Table 12 line 331 | ❓ |
| 1.8 | Adobe TypeKit 7,387ms critical path | "`font-display: swap`; preload 2 weights; evaluate self-hosting." | Table 12 line 333 | ❓ |
| 1.9 | 13 pages >2s server response — worst `/treatment/emg/` 3.1s, `/providers/loretta-assalone-otr-l-cht/` 2.5s, `/treatment/rotator-cuff-repair/` 2.4s | "Investigate top 3 individually." | Table 12 line 337; Pillar 1 line 24 | ❌ |

**Verify with:** PSI field data (`scripts/cwv-check.py`, `PAGESPEED_API_KEY` env) — CLS p75 ≤ 0.10
on spine hub, homepage, condition/treatment/location templates.

## 2. P0 — Schema corrections in Rank Math (446 errors outstanding)

Cardinal, Pillar 6 (line 49): *"This is a completion and correction task, not a ground-up
build."* Semrush still counts **446 structured-data errors** (Jul 21); GSC shows **0 rich
results** beyond Translated Results (line 384). All items Table 9 (lines 299–304) unless noted:

| # | Issue (Cardinal's numbers) | Cardinal's fix | Ref | Status |
|---|---|---|---|---|
| 2.1 | **Hospital `@type` on 42 MD/DO/DPM bios → 22–61 validation errors per page** (unpopulated Hospital properties like `availableBed`) | "Fix the Hospital @type error in Rank Math org entity definition — removing it from provider bio context will resolve ~50 validation errors per page." | Table 9 line 302 | ❌ **highest-leverage single fix** |
| 2.2 | Homepage entity = Organization/Person hybrid + Article schema | "Replace with `MedicalOrganization`: name, url, logo, description, `medicalSpecialty` (Orthopedics, Spine Surgery, Pain Management, Physical Therapy, Podiatry), `availableService`, corrected `sameAs`." | Table 9 line 300 | ❌ |
| 2.3 | **`sameAs` errors sitewide → competitor YouTube `@mendelsonortho` and wrong LinkedIn `/company/mkoss/`** | Fix both; add GBP, Healthgrades, Vitals, Zocdoc, Zimmer Biomet | Table 9 lines 299–300 | ❌ (tracker: YouTube error persists) |
| 2.4 | Location schema on all 8 pages: Hospital `@type` on clinic pages, **corrupted `openingHoursSpecification`** (overlapping entries), **Unicode line separator (U+2028) in name field** | Correct per location; cross-check NAP vs GBP | Table 9 line 301; Table 16 line 371 | ❌ |
| 2.5 | Provider-bio BreadcrumbList malformed — insurance pages appear as ancestors (`Home > Policies & Insurance > Accepted Insurances > [Physician]`) | Correct chain to `Home > Providers > [Physician]` on all 70 bios | Table 9 line 303 | ❌ (Breadcrumbs rich result did PASS on spine hub 2026-07-27 — sitewide fix still open) |
| 2.6 | **FAQPage schema: 0 pages** — `faq.css`/`faq.js` already load sitewide, content exists unmarked | FAQPage/Question/Answer on all pages with FAQ sections | Table 9 line 304; Table 17 line 380 | ❌ (Semrush FAQ rich-result keywords: 0) |
| 2.7 | 38 allied-health bios (PA-C/PT/OT/PTA) have no schema | Evaluate `HealthcareProfessional` / `MedicalBusiness` | Table 9 line 302 | ❌ |
| 2.8 | Target state by page type (70 provider bios = `Physician`; 61 condition = `MedicalCondition`+`FAQPage`; 72 treatment = `MedicalProcedure`+`FAQPage`; blog = `Article` w/ physician author) | — | Table 10 lines 307–314 | reference |

**Verify with:** Semrush Site Audit issue 45 (446 → falling), GSC Enhancements/Search
Appearance (FAQ + Breadcrumb types appearing), Rich Results Test on one page per type.

## 3. P1 — Redirects, sitemap, canonicalization (final pass)

Cardinal: Pillars 1–4 (Tables 3–7). Much of this landed since June — the Aug 11 crawl is the
ground truth. Remaining:

| # | Issue | Action | Ref | Status |
|---|---|---|---|---|
| 3.1 | Dead URLs still 404 (departed providers, removed cwt hubs, legacy paths) | **Import `data/redirects-to-implement-v2-2026-08-11.csv` — 60 rows, source→target, all targets crawl-verified 200, no chains** (WP Redirection plugin format). 17 further rows need a judgment call first — see `data/redirect-verification-2026-08-11.csv`. | extends Table 5 line 266 | ❌ ready to ship |
| 3.2 | Sitemap final hygiene: Cardinal's 10 dead + 17 redirecting entries (URL list lines 253–262) | Mostly landed (GSC 0 errors, 343 URLs). Clear Semrush's 2 remaining wrong entries; **regenerate + resubmit after 3.1 ships** | Tables 3–4, line 247 | 🟠 |
| 3.3 | 100 pages (26%) canonicalized to another URL yet included in sitemap — sources: `?treatment_type=`, `?post_type=`, `?specialty_id=`, `?location=` | Configure Rank Math to auto-canonicalize those parameter patterns and exclude non-canonical URLs from sitemap generation | Table 6 line 275 | ❓ |
| 3.4 | Internal links pointing at redirects/404s — Cardinal: 17 internal 3xx + 10 internal 4xx (lines 25, 248); Semrush now flags **754 broken internal links** (post-migration growth) | Export inlinks (Screaming Frog / Semrush), update hrefs to final URLs — especially nav/GBP links to `/our-providers/` (15.9K visits/yr still flow through it) | Pillar 1/4; tracker §1 | ❌ |
| 3.5 | Legacy structures outside our crawl scope: `/full-service-clinics/` (6 pages, 30,520 impr; sterling-heights-2 = #3 clicked page — "implement carefully"), `/shp-*` (20 pages), Southfield ×9 variants, 72 underscore URLs, `/treatment/physical-therapy/%20` space URL | Cardinal's listed 301 mappings | Table 5 lines 267–271 | ❓ crawl these before acting (same list-mode method) |
| 3.6 | `/patient-center/find-a-doctor/` 404 + **4 CTAs still pointing at it** | "Standardize all Find A Doctor CTAs to `/providers/` with trailing slash." | line 26 ("YMYL note… dead end at the moment of highest appointment intent"); Table 13 line 345 | ❓ |

## 4. P1 — Security headers & CSP (analytics data loss)

Pillar 9 (lines 64–66, Table 14 lines 350–356). Cardinal: *"All four missing security headers
can be deployed as a single Cloudflare Transform Rule… resolving 394–395 flagged URLs with no
development deployment."*

| # | Issue | Fix | Status |
|---|---|---|---|
| 4.1 | **CSP blocks `scripts.clarity.ms` + `static.cloudflareinsights.com` — "active analytics tools returning zero data"** | Add both to `script-src`. Cardinal: "5-minute server config fix. Data loss stops instantly." | ❓ confirm Clarity data is flowing |
| 4.2 | Missing `X-Content-Type-Options` (394 URLs) & `X-Frame-Options` (394 URLs — "appointment and patient forms at risk") | One Cloudflare Transform Rule: `nosniff` + `SAMEORIGIN` | ❓ |
| 4.3 | Missing `Referrer-Policy` (395 URLs — "patient URL paths containing appointment parameters could leak") / HSTS absent on 186 static-asset URLs | `strict-origin-when-cross-origin`; extend HSTS to all response types | ❓ |
| 4.4 | CSP `unsafe-inline` — "negates most XSS protection" | Medium-term: nonces/hashes + `strict-dynamic` | ❌ |
| 4.5 | *(New, ours)* Cloudflare has firewall-blocked our monitoring egress `160.79.106.0/24` (Ray `a21bf49b0c648b8e`) | WAF Skip rule for that range restores our automated verification; keep the existing `/robots.txt` + `/llms.txt` challenge exemptions | request |

## 5. P2 — On-page template fixes (one archive-template change resolves most)

Pillar 5 (line 43–45, Table 8). Cardinal: *"The meta description and title duplicate patterns
are identical — both are WordPress archive template defaults. A single template change…
resolves the majority of both issues simultaneously."*

| # | Issue | Ref | Status |
|---|---|---|---|
| 5.1 | 120 duplicate titles (36× Locations, 14× Providers, 13× Treatments, 9× Book an Appointment) + 86 duplicate metas — archive templates | Table 8 lines 288, 290 | 🟠 dup metas 86→7; 5 titles remain (`/locations-type/` taxonomy) |
| 5.2 | 14 pages missing H1 — `/book-an-appointment/`, `/about-us/`, `/insurance-billing/` + entire insurance suite, `/patient-center/…` | Table 8 line 292 | ❌ (Semrush: 21 flagged) |
| 5.3 | **270 pages (70.3%): H1 is not the first heading** — a template header/banner heading precedes it; "one WordPress theme template edit resolves the majority" | Table 8 line 293 | ❌ |
| 5.4 | 74 duplicate H1s — single words (`Knee`, `Hip`, `PT`…); location H1s = bare city names | Table 8 line 294; Table 16 line 374 ("Orthopedic and Spine Care in Sterling Heights, MI outperforms Sterling Heights") | ❌ |
| 5.5 | 11 images missing alt text | Table 8 line 295 | ❌ |
| 5.6 | Title/meta rewrites on the CTR-failure pages — carpal tunnel (Cardinal's example title: "Carpal Tunnel Syndrome Treatment Southeast Michigan — Synergy Health"), TKA, cervical fusion, neck fracture, kyphoplasty | Table 8 line 291; roadmap line 602 | ❌ content+SEO task; note carpal tunnel URL is now `/conditions/carpal-tunnel-syndrome/` (old cwt URL 301s per Aug 11 crawl) |

## 6. P2 — Accessibility (WCAG 2.1 AA on a YMYL site)

Pillar 8 (line 60, Table 13 lines 341–345): *"These are ADA compliance failures on a YMYL
healthcare site."* All ❓ pending your check:

- 6 consent-modal inputs without labels (`synergy-analytics` plugin — `for/id` or `aria-labelledby`)
- 7 Leaflet map markers with no accessible name (`aria-label="Synergy Health [Location] — click to view details"`)
- Hero video: no captions track → for decorative use add `role="presentation"` + `aria-hidden="true"`
- 2 consent-banner links color-only → underline `.synergy-consent-link`

## 7. P3 — Housekeeping

- Pagination: 19 URLs non-indexable, 24 not in `<a href>` anchor tags (Table 6 line 276)
- GSC Coverage (Indexing > Pages) export never pulled — indexation gap unknown (Table 3 line 249)
- Cache TTL for all static assets → 1 year (with 1.3)

---

**Sequencing (Cardinal's Phase-1 gates, lines 136–145):** CLS finish (§1.1–1.2) and the
Rank Math corrections (§2.1–2.4) are the two "stop active losses" tracks; §3.1's import and
§4.1's CSP line are same-day wins. After each deploy: PSI re-test, Semrush re-crawl, and the
tracker (`audits/cardinal-recommendation-tracker.md`) gets a dated status update — that file
is the running ledger of what's verified done.

*Prepared 2026-08-11 from Cardinal's June 2026 audit + our July–August verification data.
Statuses are evidence-based; ❓ items need Paul's confirmation because our monitoring range
is currently WAF-blocked (§4.5).*
