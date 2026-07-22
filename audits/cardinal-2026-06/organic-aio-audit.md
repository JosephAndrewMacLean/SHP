SYNERGY HEALTH
Organic Search and AI Optimization Audit
synergyhealth.org  |  Full Integrated Report
Data: Screaming Frog Full Crawl + 9 Bulk Exports  |  PageSpeed Insights  |  GSC Performance 90 Days
GSC Core Web Vitals 90-Day Trend  |  GSC Backlinks  |  June 2026  |  Power Digital Marketing | Full LLM Crawl | Cardinal Proprietary Audit Inputs | Healthcare CDM Data
# Executive Summary
The Situation
Synergy Health has a genuine competitive positioning advantage -- integrated orthopedic and spine care under one roof, same-week access, and demonstrated patient satisfaction (96% recommend rate). This advantage is largely invisible to search engines, AI systems, and the patients who do not yet know the practice name. The data makes the gap concrete: 1,186,066 organic impressions over the last 90 days generated only 13,668 clicks (1.15% CTR against a 3-5% healthcare benchmark). 80% of all clicks come from patients who already know the practice. The carpal tunnel syndrome page ranks at average position 1.37 with 15,605 impressions and generates 4 clicks. The TKA (Total Knee Arthroplasty / knee replacement) cluster accumulates 30,143 quarterly impressions across 15 competing pages and converts at 0.06% CTR. These are not close-call metrics -- they are systematic failures at the content structure, entity signal, and AIO readiness layer.
The Structural Cause
The Screaming Frog full crawl and GSC export confirm the root cause: partial schema implementation via Rank Math PRO: BreadcrumbList is deployed sitewide, location pages have MedicalClinic and MedicalOrganization schema, and condition pages have MedicalCondition schema. Critical gaps and errors remain: Physician schema present on 42 MD/DO/DPM bios but with 22–61 validation errors per page; 38 allied health bios have no Physician schema, no FAQPage schema, incorrect entity type on the homepage (Organization/Person hybrid instead of MedicalOrganization), and sameAs errors linking to a competitor’s YouTube channel (@mendelsonortho) and an incorrect LinkedIn entity (/company/mkoss/). Zero rich results in GSC Search Appearance (one entry: Translated Results, 17 clicks) is a lagging indicator consistent with recent Rank Math configuration — schema deployed after the Screaming Frog crawl date is not yet reflected. No llms.txt file exists. A Core Web Vitals regression event on approximately May 1, 2026 took the site from 238 Good URLs to zero Good URLs -- a failing CWV state that has persisted for six weeks with no confirmed fix. Simultaneously, the on-page template layer has 120 duplicate title tags, 85 missing meta descriptions (including the homepage), and 14 pages missing H1 tags. LLM-powered search systems (Google AI Overviews, ChatGPT, Perplexity, Claude) extract structured clinical information for citation -- with incomplete and partially incorrect schema, Synergy Health lacks the structured physician entity authority and FAQ extraction eligibility that fully schema-enabled competitors receive.
Three Critical Improvements to Unlock Patient Acquisition Growth
Topical authority expansion in foundational spine and core orthopedic conditions -- where patient journeys begin and where 58% of impressions are non-branded but convert at near-zero rates
Entity and schema implementation (MedicalOrganization, MedicalClinic, Physician, MedicalCondition, MedicalProcedure, FAQPage) to make Synergy's expertise machine-readable for AI Overviews, local pack enrichment, and Knowledge Panel population
Hyper-local conversion architecture combining conditions, providers, access messaging, and proof signals per location -- addressing the identified gap where "hand specialist near me" ranks position 3 with 745 impressions and generates 1 click
How This Report Is Structured
This report is organized in two parts. Part One covers the Technical SEO audit: crawlability, indexation, on-page signals, Core Web Vitals and performance, schema, local infrastructure, security, and backlinks. Part Two covers the AIO and Organic Strategy audit: topical authority, local AIO performance, competitive benchmarking, sentiment, entity signals, content alignment, and measurement. Part Three is the Integrated 90-Day Roadmap -- a single blended action plan sequencing every finding from both parts into a prioritized, owner-assigned execution timeline.
PART ONE: TECHNICAL SEO AUDIT
Pillars 1 through 13  |  Crawlability, Performance, On-Page, Schema, Security, Backlinks
# Pillar 1: Crawlability and Indexation Health
Slide Summary
The crawl structure is clean -- zero redirect chains, zero redirect loops, no internal robots.txt blocks. The primary crawl issue is the XML sitemap, which contains 10 URLs returning 404 errors and 17 URLs returning 301 redirects, directing Google to dead ends on every crawl cycle. 128 of 412 sitemap URLs (31%) are non-indexable. GSC Coverage data is the remaining gap -- pages Google crawls but refuses to index are currently unknown.
Findings
Sitemap 404 URLs -- Remove Immediately
Response time: mean 1.2s across 411 URLs. 13 pages exceed 2 seconds. Worst: /treatment/emg/ at 3.1s.
Zero redirect chains and zero redirect loops -- positive baseline signals. 17 internal 3xx source links should be updated to point to final destinations.
YMYL note: /patient-center/find-a-doctor/ is both a 404 in the sitemap and receives organic impressions. Patients following this link hit a dead end at the moment of highest appointment intent.
# Pillar 2: URL Architecture and Site Structure
Slide Summary
GSC data reveals the full scale of the legacy URL architecture problem. The site has four parallel URL structures for the same clinical content: /specialties/ (205,968 impressions), /conditions-we-treat/ (110,402 impressions), /conditions/, and /treatment/ -- coexisting with /full-service-clinics/ (30,520 impressions from 6 legacy location URLs) and /shp-* (11,793 impressions from 20 legacy physical therapy URLs). These are live, indexed URLs splitting authority across duplicate content. URL consolidation is the highest-leverage structural fix available.
Findings
The /specialties/ structure alone gets 205,968 impressions -- nearly as many as /treatment/ (179,993) combined with /providers/ (182,107). These are the main clinical pages of the site split across competing URL structures.
The full-service-clinics sterling-heights-2 page is the third highest-click page on the entire site. A 301 redirect to /locations/sterling-heights/ must be implemented carefully to preserve this traffic.
# Pillar 3: Canonicalization and Duplicate Content
Slide Summary
Canonical implementation is technically correct where present -- no conflicting canonicals, no relative canonicals, no canonicals pointing to broken URLs. The Screaming Frog content bulk export confirms zero near-duplicate and zero semantically similar page pairs, and zero spelling or grammar errors. The issues are structural: 100 pages canonicalized to a different URL (26%) with the sitemap incorrectly including 128 of those non-indexable pages.
Findings
# Pillar 4: Redirect Audit
Slide Summary
Zero redirect chains, zero redirect loops, zero JavaScript redirects, zero meta refresh redirects. The redirect profile is technically clean. The primary redirect issue is sitemap hygiene: 17 redirecting URLs are in the sitemap sending Google to stale sources instead of final destinations.
Findings
# Pillar 5: On-Page Technical Signals
Slide Summary
The bulk page exports reveal a more severe on-page picture than the crawl overview showed. Title duplicates affect 5 pages (1%) — only /locations-type/ taxonomy pages sharing one title, a minor issue resolved by Rank Math PRO custom titles. Meta descriptions are missing on 55 pages (13%) — note: the homepage has a Rank Math PRO meta description confirmed live ("Southeast Michigan's integrated orthopedic and spine destination. 70+ board-certified surgeons across 12 locations with same-week appointments.") — the crawl likely miscounted it; and 86 pages have duplicate meta descriptions generated by the same archive template pattern. H1 gaps affect 14 confirmed pages including /book-an-appointment/, /about-us/, /insurance-billing/, and the entire insurance sub-page suite. The GSC cost is concrete: the carpal tunnel page ranks #1.37 with 15,605 impressions and generates 4 clicks (0.03% CTR) -- a direct result of generic title and meta tags on a #1-ranking page.
Findings
The meta description and title duplicate patterns are identical -- both are WordPress archive template defaults. A single template change in Yoast or RankMath resolves the majority of both issues simultaneously.
GSC Search Appearance shows zero rich results beyond Translated Results (17 clicks) — a lagging indicator consistent with recent Rank Math configuration rather than zero schema. No FAQ snippets, physician cards, or sitelinks are appearing yet. Correcting the schema gaps identified in Pillar 6 — particularly Physician and FAQPage schema — will unlock these rich result types.
# Pillar 6: Schema Markup and Structured Data
Slide Summary
Rank Math PRO is deployed and generating partial schema across key page types — but the Screaming Frog crawl did not capture it (predating the current Rank Math configuration), and critical gaps and quality errors remain. Live site inspection confirms: BreadcrumbList sitewide (Rank Math default), MedicalClinic and MedicalOrganization on all 8 location pages with geo coordinates and openingHours, and MedicalCondition on condition pages. Critical gaps and errors: no Physician schema on any of 70 provider bio pages (the highest-priority remaining gap — provider pages are the top organic asset at 2.70% CTR), no FAQPage schema, wrong entity type on the homepage (Organization/Person hybrid instead of MedicalOrganization), sameAs errors sitewide pointing to a competitor’s YouTube channel (@mendelsonortho) and an incorrect LinkedIn entity (/company/mkoss/), and location schema quality issues (Hospital @type on clinic-level pages, corrupted openingHoursSpecification, Unicode separator in location name field). This is a completion and correction task, not a ground-up build. The bulk exports provide the inventory for remaining work: 70 provider bio pages, 72 treatment pages (MedicalProcedure deployed on 70 treatment pages). The cost of the gaps: 1,186,066 impressions over 3 months generating 13,668 clicks (1.15% CTR) with no rich result amplification.
Findings
Schema Implementation by Page Type
# Pillar 7: Core Web Vitals and Page Performance
Slide Summary
CRITICAL: A CWV regression event occurred on approximately May 1, 2026. The site previously passed Core Web Vitals with 184-238 Good URLs from March 16 through April 30. By May 13, Good URLs reached zero and have remained there for six weeks. LCP field data is 3.5 seconds (threshold: 2.5s), CLS is 0.11 (threshold: 0.10), and the Lighthouse mobile performance score is 28/100. The root causes are specific and fixable: a 1,032KB unoptimized logo SVG, an 11MB background video, 50+ render-blocking CSS files, Hotjar consuming 3,443ms CPU time per page load, and 203 images missing size attributes contributing to CLS. Identifying the May 1 deployment is the most urgent action in the entire audit.
CWV Regression Timeline (Mobile, GSC Field Data)
Findings
Performance remediation sequence: (1) Identify regression deployment -- may be the single fix needed. (2) Optimize logo.svg -- removes 1MB with no code change. (3) Defer Hotjar -- saves 3,443ms via GTM config only. (4) Add image size attributes -- resolves CLS in a template edit.
# Pillar 8: Mobile and Accessibility Technical Signals
Slide Summary
Lighthouse scores accessibility at 87/100. Mobile usability passes all Screaming Frog checks. PageSpeed exposed specific WCAG 2.1 AA failures: 6 consent form inputs without labels, 7 Leaflet map markers with no accessible names, the hero background video missing captions, 2 color-contrast-only links in the consent banner, and a heading sequence violation. These are ADA compliance failures on a YMYL healthcare site.
Findings
# Pillar 9: HTTPS and Security Signals
Slide Summary
HTTPS is fully implemented with zero mixed content, zero HTTP URLs, and zero insecure forms. The security header implementation has two compounding problems: four critical headers are missing on approximately 49% of all URLs, and the existing Content Security Policy is actively misconfigured -- blocking Clarity and Cloudflare Beacon on every page load while using unsafe-inline, which negates most XSS protection.
Findings
All four missing security headers can be deployed as a single Cloudflare Transform Rule. The site is confirmed behind Cloudflare. This is a dashboard configuration change resolving 394-395 flagged URLs with no development deployment.
# Pillar 10: Local SEO Technical Infrastructure
Slide Summary
Synergy Health has 8 confirmed location pages with dedicated URLs and 1,700-2,100 words of content per page. The structural foundation is in place. What is entirely absent is the schema layer and meta signal layer: zero MedicalClinic schema on any location page, 7 of 8 location pages missing meta descriptions, H1s are single city names only, and the Southfield location has 9 competing URL variants fragmenting its authority in GSC.
Confirmed Location Pages
Findings
# Pillar 11: AI Overview and Generative Engine Optimization Readiness
Slide Summary
Synergy Health has one meaningful AIO positive: all critical content is present in raw HTML -- no JavaScript-dependent content rendering -- making full text accessible to LLM crawlers. All 384 pages have substantive word counts (minimum 1,565 words on indexable pages). The three foundational AIO requirements are absent: no structured data, no llms.txt, and no E-E-A-T signals in schema form. 309 of 384 pages (80%) are rated Fairly Hard or Hard to read -- the opposite of the clear, definitive, factual prose that AI systems prefer to cite.
Findings
# Pillar 12: GSC Performance Analysis
Slide Summary
GSC data covers March 16 -- June 13, 2026 (90 days). Total: 13,668 clicks, 1,186,066 impressions, 1.15% overall CTR. The strategic story: the site has massive search visibility but converts a fraction of it into traffic. 80% of clicks are branded. 58% of impressions are non-branded but convert at near-zero rates. The highest-value pages by impression volume are all underconverting due to the on-page and schema gaps identified in earlier pillars.
Performance Overview
Critical Performance Findings
Top Opportunity Pages -- Striking Distance (Position 6-15, Over 2,000 Impressions)
# Pillar 13: Backlink Profile and E-E-A-T Authority
Slide Summary
The GSC backlink export (June 15, 2026) shows 734 linking pages from 130 unique domains -- thin for a multi-location healthcare organization. The profile is skewed by two inflating factors: 82 of 135 authoritative links are Google Play Store language-localized listings for a legacy patient app, and the staging domain (synergy.egowebdev.com) is still live and crawlable. The genuinely valuable links are 15 from Zimmer Biomet (a global orthopedic implant manufacturer) and 24 from BirdEye review pages. Zero links from Michigan hospital systems, state medical associations, or insurance provider directories.
Findings
The oldest substantive editorial link in the profile is a GlobeNewswire press release from 2012. This indicates the practice has not had an active media relations or link acquisition program during the Synergy Health brand era.
Link acquisition priority order: (1) Michigan hospital system physician affiliation pages, (2) insurance provider directories, (3) AAOS and Michigan Orthopedic Society member directories, (4) local Michigan media expert commentary, (5) Healthgrades and Doximity full profiles for all physicians.
PART TWO: AIO AND ORGANIC STRATEGY AUDIT
Sections 1 through 7  |  Topical Authority, Local, Competitive, Sentiment, Entity, Content, Measurement
# Section 1: AIO Topical Authority Benchmark
Executive Takeaways
Synergy's topical authority score in Orthopedics and Spine is 31.8, significantly behind enterprise benchmarks (Cleveland Clinic, HSS, Mayo operate at 70-85+) and below strong regional competitors (45-60 range). The GSC data confirms the authority gap structurally: /specialties/ generates 205,968 impressions across 76 URLs at 0.27% CTR. /conditions-we-treat/ generates 110,402 impressions across 85 URLs at 0.07% CTR. These are large-scale impression surfaces with near-zero conversion -- the classic signature of thin or poorly structured content that ranks by proximity but does not earn clicks.
Topical Authority by Content Area -- GSC Evidence
Strengths -- What to Protect and Compound
Gaps -- What Is Limiting AIO Growth
# Section 2: AIO Local Benchmark
Executive Takeaways
Synergy's local visibility at the GBP level is working -- 1,781 clicks from GBP UTM links at 2.75-3.5% CTR confirms the local GBP infrastructure is functional. The failure is at the organic local layer: hand specialist near me ranks position 3 with 745 impressions and generates 1 click. Hand surgeon near me ranks position 2 with 731 impressions and generates 2 clicks. These are the highest-intent patient queries in orthopedics and spine -- patients in the moment of deciding to seek care -- and the site is converting them at near-zero rates.
Local Query Performance -- GSC Evidence
Local Gaps
# Section 3: Competitive Benchmark
Executive Takeaways
National leaders (Cleveland Clinic, Mayo Clinic, Hospital for Special Surgery) dominate AI citations because they operate as clinical content libraries with systematized E-E-A-T infrastructure. Regional systems (Henry Ford, Corewell/Beaumont) dominate local packs primarily through location scale and review velocity -- but carry the same patient pain points of fragmentation, access delays, and impersonal care that Synergy's integrated model directly solves. Synergy's winning strategy is not to out-publish Mayo. It is to become the most trusted, most accessible, most coordinated orthopedic and spine destination in Southeast Michigan.
Competitive Position by Dimension
Where Synergy Can Win
# Section 4: Patient Sentiment Analysis
Executive Takeaways
Synergy's sentiment profile is a documented competitive asset: 82/100 overall sentiment score, stable-to-improving trajectory, with patient feedback strongly reinforcing the brand promise of coordination, speed, and clarity. The strategic challenge is not quality -- it is visibility of quality at the moments when patients make decisions. The 96% recommend rate is a powerful trust signal that currently exists only in internal data and is not surfaced in schema, structured content, or external review platforms where AI systems look for corroboration.
Positive Sentiment Drivers to Amplify
Risks to Manage Proactively
# Section 5: Entity Audit and E-E-A-T Signal Assessment
Executive Takeaways
E-E-A-T is constrained by incomplete and incorrect entity signals. Rank Math PRO provides partial schema coverage — BreadcrumbList sitewide, MedicalClinic on location pages, MedicalCondition on condition pages — but critical gaps remain: no Physician schema on 70 provider bios, wrong entity type on the homepage, and sameAs references pointing to a competitor’s YouTube channel (@mendelsonortho) and an incorrect LinkedIn entity (/company/mkoss/). Additionally, 734 linking pages from 130 unique domains is thin for a multi-location healthcare organization. Zero links from Michigan hospital systems, state medical associations, or insurance provider directories. In orthopedic and spine care, where trust is the primary conversion driver, completing the schema implementation simultaneously improves AIO eligibility, local pack confidence, and on-site conversion rates.
Entity Signal Assessment
# Section 6: Content AIO Alignment
Executive Takeaways
Synergy's brand voice (clear answers, faster) is inherently AIO-native -- but the site currently executes the opposite at the content structure level. 309 of 384 pages (80%) are rated Fairly Hard or Hard to read. Pages over-index on appointment CTAs and service descriptions. The fastest path to AIO citations is to publish content that AI can directly extract: definitions, FAQs, decision criteria, recovery timelines, and treatment comparisons -- each anchored to the integrated care model and each attributed to named, credentialed physicians.
Content Gap Analysis -- GSC Evidence
Findings
# Section 7: Measurement Framework
Executive Takeaways
Measurement must connect AIO visibility to appointment volume: AIO citations and rich results drive local visibility and CTR, which drives consultation requests, which drives scheduled cases. The current measurement baseline is partially established through GSC. The CWV regression event is the most urgent active measurement issue -- 6 weeks elapsed with the site in a failing CWV state with no confirmed fix.
Core KPIs -- Executive Dashboard
Recommended Tool Stack
PART THREE: INTEGRATED 90-DAY ROADMAP
Technical + Strategic + AIO  |  Every Finding Sequenced into a Single Execution Plan
# Integrated 90-Day Roadmap
How to Read This Roadmap
Every finding from Parts One and Two is sequenced here into a single, owner-assigned execution timeline. Items are ordered by two criteria: urgency (findings with compounding daily cost, like the CWV regression, come first) and leverage (items that unlock the most subsequent wins, like schema, come before items that depend on them, like AIO content). The roadmap is designed to produce measurable outcomes at each phase gate -- not just a to-do list. The Phase 1 Deliverable is an AIO-ready technical foundation. The Phase 2 Deliverable is measurable non-branded visibility growth. The Phase 3 Deliverable is expanded AIO citation presence and systematized authority growth.
A Note on Sequencing
Technical fixes and content investments are intentionally blended within each phase rather than separated. This reflects how organic search actually works: a schema deployment on a provider bio page (technical) and a physician reviewer byline on a condition page (content) both feed the same E-E-A-T signal. A CSS consolidation (technical) and a content hub launch (strategic) both feed the same page quality assessment Google and AI systems apply. The owners column reflects this -- Dev+SEO and Content+SEO appear together because neither investment is effective in isolation.
Owner Key
## Phase 1 (Days 1-30): Foundation Sprint -- Stop Active Losses and Unlock AIO Eligibility
Primary objective: address every finding with a daily compounding cost (CWV regression, analytics data loss, sitemap crawl waste, on-page template failures) and establish the minimum viable AIO infrastructure. Phase 1 is the prerequisite for everything that follows -- schema that is deployed on a page with a failing CWV state and no meta description is less effective than schema deployed on a technically sound, properly signaled page. Fix the foundation first.
What Success Looks Like at Day 30
CWV regression deployment identified and fix deployed -- Good URL count begins recovering in the 28-day rolling window
Zero 404s and zero 301s remaining in the XML sitemap -- confirmed in GSC Coverage report
Zero CSP console errors -- Clarity and Cloudflare Beacon data fully restored
logo.svg under 20KB, Hotjar deferred from critical path -- measurable LCP improvement in PageSpeed re-test
Security headers present on 100% of pages -- confirmed in Screaming Frog re-crawl
llms.txt returning 200 at synergyhealth.org/llms.txt
Homepage meta description live -- most visible page on the site now has a SERP snippet
Carpal tunnel and TKA page titles and meta descriptions rewritten -- CTR improvement visible in GSC within 2-3 weeks
Duplicate archive title and meta template fixed -- 120 duplicate titles and 86 duplicate meta descriptions resolved in single template change
MedicalOrganization schema and Physician schema live -- GSC Enhancements report active
75-query AIO tracking baseline established in ChatGPT, Perplexity, and Google AI
Phase 1 Deliverable: AIO-ready technical foundation for Google and answer engines to interpret Synergy Health as a credible medical entity with structured physician authority, functional analytics, and a clean crawl profile.
## Phase 2 (Days 31-60): Authority Build -- Expand Non-Branded Reach
Primary objective: build topical authority for the conditions and procedures patients search when they are deciding whether to seek care, and convert location pages into local clinical destinations that compete on schema, content, and proof signals. Phase 2 is where the visible organic impact begins -- the first AIO citations for spine condition queries, the first local pack improvements from MedicalClinic schema, and the first CTR lift from hyper-local service pages.
What Success Looks Like at Day 60
MedicalClinic schema live on all 8 location pages -- GSC Enhancements report shows zero schema errors for location types
MedicalCondition schema live on 61 condition pages -- AI Overview citations beginning for condition queries in Profound/manual tracking
5 foundational spine condition hubs published (stenosis, herniated disc, sciatica, DDD, spondylolisthesis) -- first non-branded impressions appearing in GSC
TKA cluster consolidated into one canonical hub -- CTR improvement measurable from existing 30,143 quarterly impressions
All 8 location pages have unique meta descriptions -- CTR improvement measurable from existing 117,771 quarterly location impressions
Southfield URL variants consolidated -- all authority signals concentrated to /locations/southfield/
GA4 conversion tracking and call tracking live -- organic consultation ROI now measurable
/full-service-clinics/ redirect complete -- legacy location traffic preserved and consolidated
Phase 2 Deliverable: Measurable lift in non-branded organic visibility and improved local conversion paths. First AIO citations expected for spine condition and location-specific queries. Organic consultation ROI now measurable via GA4 and call tracking.
## Phase 3 (Days 61-90): Conversion and Scaling -- Dominate AIO-Trigger Formats
Primary objective: build the content formats that AI Overviews most frequently extract (recovery timelines, treatment comparisons, decision-support FAQ pages), complete the schema suite, and systematize the authority-building programs (review velocity, link acquisition) that compound over months and years. Phase 3 is where the brand positioning -- integrated care, same-week access, no runaround -- becomes a content moat that national competitors cannot easily replicate.
What Success Looks Like at Day 90
Full schema suite validated across all page types -- MedicalProcedure and FAQPage live on condition and treatment pages
LCP field data trending toward 2.5s threshold in GSC 28-day rolling window -- CSS consolidation compounding with Phase 1 script deferrals
Lighthouse performance score improved from 28 to 50+ (lab score under throttled mobile conditions)
AI Overview citations appearing in Profound and manual monitoring for condition and treatment queries
Rich result types appearing in GSC Search Appearance beyond Translated Results -- FAQ rich results, breadcrumbs, physician results
Review velocity program active -- monthly growth per location tracked in BirdEye or Podium
First hospital system or medical association link acquired
Topical authority score beginning directional improvement from 31.8 baseline
Phase 3 Deliverable: Expanded AIO citations for recovery, treatment options, and decision-support queries. Measurable gains in consultation requests from organic channels. Systematized review velocity and link acquisition programs established for long-term authority compounding. Foundation for 6-12 month topical authority growth toward 55-60 score.
## Consolidated Findings Matrix -- All Findings, All Priorities
## ROI Forecast -- Tied to Patient Acquisition Outcomes
Success is evaluated in patient acquisition outcomes -- not traffic volume alone. The three primary outcomes to report quarterly to leadership:
Local pack visibility: movement toward 45-50% visibility by month 3 on priority near me + city queries (Livonia, Sterling Heights, Southfield) for orthopedic and spine specialties
Organic consultation growth: +25-35% by month 3 as schema unlocks rich results, title and meta fixes improve CTR, and conversion tracking infrastructure is in place
Topical authority: directional improvement from 31.8 toward 40-45 by months 3-6, with a 12-month target of 55-60 as spine hubs, hyper-local pages, and link acquisition compound
## Resource Requirements
APPENDIX A: Video Content Audit
Video Content Audit
YouTube Channel: @mendelsonortho  |  Channel ID: UCY-tn6Tl-_voCfjm9B4MO7w
Data: Public Channel Inspection  |  GSC Backlink Export  |  Screaming Frog Site Crawl  |  June 2026
Prepared by: Power Digital Marketing  |  Part of Integrated SEO + AIO Audit
# Executive Summary
The Core Issue
The Synergy Health YouTube channel (@mendelsonortho, Channel ID: UCY-tn6Tl-_voCfjm9B4MO7w) is branded entirely under the legacy Mendelson Orthopedics identity. The channel name, handle, description, and legacy URL all predate the Synergy Health rebrand. Every video published on this channel builds authority for a name and brand the organization no longer leads with. The channel description -- Learn more about our one-stop-medical-shop! -- is thin, keyword-absent, and does not reflect the current scope of services, locations, or brand positioning. The About section link almost certainly points to mendelsonortho.com rather than synergyhealth.org, directing patients who discover the channel to a different domain.
What We Can Confirm Without YouTube Studio Access
YouTube blocked automated access to the full video inventory list during this audit. The following findings are based on public channel data, the Screaming Frog site crawl of synergyhealth.org, the GSC backlink export, and the broader audit context. A complete video audit requires either YouTube Studio access or a manually provided video inventory. The audit prompt at the end of this document is ready to execute once channel access is granted.
What This Means for the Integrated Audit
Video content is the one scope item marked NEEDS INPUT in the Scope Coverage Tracker. The technical and strategic audit findings create specific video investment priorities that did not exist before the data was analyzed: VideoObject schema on embedded videos (no VideoObject schema deployed on any of 423 site pages), video transcripts as AIO citation sources, YouTube channel branding alignment with the Synergy Health entity, and short-form video content covering the five foundational spine conditions confirmed as complete content gaps in the GSC data.
Three Priority Actions Before Any New Video Is Produced
Rebrand the YouTube channel -- name, description, handle, and About section link -- from Mendelson Orthopedics to Synergy Health. This is a channel settings change and does not require re-uploading any video.
Audit existing videos for embed opportunities on synergyhealth.org and implement VideoObject schema on any embedded video pages. This is the fastest path from the existing video library to AIO citation eligibility.
Grant YouTube Studio access (or provide a video inventory export) to complete the full 7-dimension video content audit outlined at the end of this document.
# Dimension 1: Channel-Level SEO and Branding
Slide Summary
The channel was created under the Mendelson Orthopedics brand and has not been updated to reflect the Synergy Health rebrand. This is not a cosmetic issue -- it is an E-E-A-T and entity coherence issue. Google and LLM-based AI systems assess healthcare source authority by cross-referencing entity signals: the organization name on the website, the schema sameAs properties, the GBP listing names, and the YouTube channel name should all converge on a single recognized entity. They currently do not. The channel resolves to Synergy Health Partners | Mendelson Orthopedics in search results -- a dual-name presentation that does not match either the canonical brand (Synergy Health) or the legacy brand (Mendelson Kornblum Orthopedics and Spine Specialists) consistently.
Findings
The channel name in YouTube search results shows as Synergy Health Partners | Mendelson Orthopedics. This dual-name presentation means the channel appears under a name that is neither the canonical current brand (Synergy Health) nor the name patients in Southeast Michigan recognize from GBP (which shows Synergy Health Partners / Mendelson Kornblum Orthopedics and Spine Specialists). Standardizing to Synergy Health across all digital properties is the highest-priority channel-level action.
The channel description is the primary signal YouTube's algorithm uses to understand what a channel is about and which queries it should appear for. A 12-word description with no keywords is the channel-level equivalent of a page with no meta description -- confirmed on 85 pages in the site audit.
# Dimension 2: Video Inventory and Publishing Cadence
Slide Summary
YouTube blocked automated access to the video list during this audit. The full inventory -- titles, publish dates, view counts, descriptions, and tags -- requires YouTube Studio access or a manual export. What can be confirmed from the channel page and legacy URL structure: the channel has been active for a significant period (the legacy /user/mendelsonortho URL predates YouTube's 2022 handle system, placing channel creation before 2022 and likely before 2015). The channel appears to have published video content at some point but the current activity level and total video count cannot be confirmed without access.
Findings
The legacy channel age is actually a positive signal -- older YouTube channels with established history carry more authority than new ones. The goal is not to start over but to modernize the existing channel under the Synergy Health brand and activate it with a consistent publishing program.
Once inventory access is granted, the priority review order is: (1) videos with the highest view counts -- optimize titles, descriptions, and CTAs for these immediately, (2) videos covering TKA and carpal tunnel conditions -- these directly map to the highest-impression GSC content gaps, (3) physician introduction videos for the high-traffic providers confirmed in the site audit (Jeffrey Mendelson MD, Stephen Mendelson MD, Preetinder Bhullar MD, Scott McCarty MD, Benjamin Mayo MD).
# Dimension 3: Content Topic Coverage and Clinical Gaps
Slide Summary
Without inventory access the content categorization cannot be completed. However, the GSC audit data defines the priority content gaps precisely -- the five foundational spine conditions have zero organic presence and zero video coverage almost certainly mirrors zero written content coverage. The carpal tunnel finding (position 1.37, 15,605 impressions, 4 clicks) represents a condition where an existing ranking page is failing on on-page signals. A physician-attributed video on carpal tunnel treatment embedded on that page would simultaneously address the E-E-A-T gap, contribute VideoObject schema eligibility, and provide transcript content for AI extraction.
Confirmed Clinical Content Gaps (Cross-Referenced with GSC)
Findings
The channel keyword tags already include knee replacement, hip replacement, spine surgery, back pain, and neck pain -- these align with the high-impression GSC queries. The gap is spine condition education (stenosis, herniation, sciatica) and recovery content. The existing keyword infrastructure on the channel is the right foundation -- it needs new video content to activate it.
# Dimension 4: Individual Video Optimization
Slide Summary
Individual video optimization requires inventory access. The patterns observed from the channel-level data suggest systematic under-optimization consistent with what the Screaming Frog bulk export found across the website: generic title patterns, thin or absent descriptions, and no CTAs linking to synergyhealth.org. The same on-page template failures that produced 120 duplicate title tags and 85 missing meta descriptions on the website are likely reflected in the video library.
Findings
The UTM parameter recommendation is particularly important given the GSC data context. The site already shows 1,781 clicks from GBP UTM links with clear utm_source attribution. Adding YouTube UTM parameters to video description links will surface YouTube as a distinct traffic source in GA4 and allow direct correlation between video engagement and appointment bookings.
The first 100 characters of a YouTube video description appear in Google Video Search snippets before the See more cutoff. For a video about knee replacement, the first sentence should read: Learn what to expect from total knee replacement surgery at Synergy Health in Southeast Michigan -- not Knee Replacement at MKO or a blank description.
# Dimension 5: SEO and AI Discoverability
Slide Summary
The most actionable SEO gap for video is the complete absence of VideoObject schema on synergyhealth.org. The Screaming Frog crawl did not capture the Rank Math schema deployed across synergyhealth.org — live inspection confirms partial schema coverage (BreadcrumbList sitewide, MedicalClinic, MedicalCondition). However, VideoObject schema is absent across all 384 pages. When a YouTube video is embedded on a web page and that page has VideoObject schema, the video becomes eligible for Google Video Search rich results, Google's video carousel feature (which appears prominently for procedure and condition queries), and AI Overview citation as a multimedia source. Without VideoObject schema, embedded videos are invisible to both search engines and AI systems as structured content.
Findings
VideoObject Schema Template
The following JSON-LD template should be implemented on every page that embeds a Synergy Health YouTube video. Replace bracketed values with the specific video's data:
# Dimension 6: AIO and Generative Engine Readiness for Video
Slide Summary
AI Overviews, ChatGPT, Perplexity, and Claude extract video content for citation primarily through transcripts, not through video viewing. A YouTube video with an accurate transcript that is accessible in the video description or on the embedding page is the equivalent of a well-structured FAQ page for AI citation purposes. The Synergy Health channel's AIO readiness for video is currently zero -- no VideoObject schema, no confirmed transcript publishing, and no structured recovery or decision-support video content that matches the high-AIO-trigger formats identified in the GSC content gap analysis.
Findings
AIO Video Content Priority Order
# Dimension 7: Strategic Recommendations
Slide Summary
The video strategy for Synergy Health is an extension of the broader integrated audit strategy -- not a separate track. Every video investment should have a corresponding written content page to embed it on, VideoObject schema to make it machine-readable, and a transcript to make it AI-citable. The channel rebrand from Mendelson Orthopedics to Synergy Health is the prerequisite for everything else. Without it, video content continues building authority for the wrong brand entity.
Immediate Actions (This Week -- No Production Required)
30-Day Video Actions (Require YouTube Studio Access)
60-90 Day Video Content Production Plan

[TABLE 1]
28/100 Mobile Performance Score | FAILED Core Web Vitals (Mobile) | Partial Pages with Schema Markup | 1.15% Organic CTR vs 3-5% Benchmark | 80% Clicks from Branded Queries

[TABLE 2]
1,186,066 Organic Impressions (90 Days) | 13,668 Organic Clicks (90 Days) | 31.8 Topical Authority Score | 0 Rich Results in GSC | 130 Backlink Domains (Thin)

[TABLE 3]
Finding | Priority | Current State | Recommended Action
10 broken URLs (404) in XML sitemap | HIGH | Google processes 10 dead URLs on every crawl cycle. Includes /patient-center/find-a-doctor/, /appointments, /treatments/, /insurance-billing/insurance-information/ | Remove all 10 immediately. See URL list below. These are former live pages whose removal was not reflected in the sitemap.
17 redirecting URLs (301) in XML sitemap | HIGH | Sitemap sends Google to redirect sources instead of final destinations. Includes /providers, /locations, /treatment, /book-an-appointment | Update all 17 to their final destination URLs. Regenerate and resubmit sitemap in GSC after fixes.
128 non-indexable URLs in sitemap (31% of 412) | MEDIUM | Sitemap contains canonicalized, redirected, and error pages Google should not be processing | Configure WordPress SEO plugin to exclude non-canonical, non-indexable URLs from sitemap generation.
10 internal 4xx errors in crawl | HIGH | 10 internal URLs returning client errors -- patients clicking internal links land on broken pages | Export Internal Client Error Inlinks from Screaming Frog. Update source links. Implement 301 redirects to topically relevant live pages.
GSC Coverage report not yet exported | MEDIUM | Indexation gap unknown -- pages Google crawls but refuses to index are undetected | Export GSC Coverage report (Indexing > Pages) and cross-reference with 384 indexable pages from crawl.

[TABLE 4]
URL | Action
https://synergyhealth.org/specialty/pain-management/?post_type=treatment | 404 -- remove from sitemap
https://synergyhealth.org/patient-center/find-a-doctor/ | 404 -- CTA destinations still pointing here
https://synergyhealth.org/cdn-cgi/l/email-protection | 404 -- remove from sitemap
https://synergyhealth.org/insurance-billing/insurance-information/ | 404 -- high-intent patient page
https://synergyhealth.org/appointments | 404 -- booking intent page
https://synergyhealth.org/specialty/pcp/?post_type=specialty | 404 -- remove from sitemap
https://synergyhealth.org/specialty/orthopedics/?post_type=specialty | 404 -- remove from sitemap
https://synergyhealth.org/?page_id=20 | 404 -- remove from sitemap
https://synergyhealth.org/podcast-head-to-total/episodes/ | 404 -- remove from sitemap
https://synergyhealth.org/treatments/ | 404 -- remove from sitemap

[TABLE 5]
Finding | Priority | Current State | Recommended Action
Parallel URL hierarchies: 4 active structures for same content | HIGH | /specialties/, /conditions-we-treat/, /conditions/, /treatment/ all coexist -- carpal tunnel alone has 3 separate URLs, TKA has 4 | Map every content type to a single canonical URL structure. Consolidate all parallel paths via 301 redirects. Establish URL taxonomy governance before any new service line launches.
Legacy /full-service-clinics/ URLs: 6 pages, 30,520 impressions | HIGH | Pre-rebrand location URL structure still live. /full-service-clinics/sterling-heights-2/ is the #3 clicked page on the site at 366 clicks | 301 redirect all /full-service-clinics/ to /locations/ equivalents. The sterling-heights-2 redirect must be implemented carefully to preserve rankings and traffic.
Legacy /shp-* URLs: 20 pages, 11,793 impressions | HIGH | Legacy physical therapy sub-brand URLs still live and receiving GBP-sourced traffic | 301 redirect all /shp-* URLs to current /locations/ or service-specific equivalents. Update GBP website links to canonical URLs.
Southfield: 9 competing URL variants in GSC | HIGH | 9 Southfield URL structures confirmed in GSC -- /locations/southfield/, /locations/clinic-locations/southfield/, /location/southfield/, plus 6 parameter variants | Consolidate to /locations/southfield/. 301 redirect all variants. Update all GBP, internal, and external links.
72 internal URLs use underscores | MEDIUM | 8.92% of internal URLs use underscores instead of hyphens | Migrate to hyphenated equivalents with 301 redirects. Prioritize high-traffic condition and treatment pages.
1 URL contains a space character (/treatment/physical-therapy/%20) | MEDIUM | Confirmed in sitemap redirect list -- URL with encoded space | Correct the slug, implement 301 from the space-encoded version.

[TABLE 6]
Finding | Priority | Current State | Recommended Action
100 pages canonicalized to a different URL (26%) | HIGH | 100 of 423 HTML pages signal their content is consolidated elsewhere. Primary sources: ?treatment_type=, ?post_type=, ?specialty_id=, ?location= parameter variants | Audit all 100. Configure WordPress SEO plugin to automatically canonicalize these parameter patterns. Remove all non-canonical URLs from the sitemap.
19 pagination URLs non-indexable; 24 not in anchor tags | MEDIUM | Page 2+ likely canonicalized to page 1. Pagination URLs not linked via standard anchor tags. | Review pagination strategy. Confirm paginated pages with unique items (providers, conditions) should be individually indexed. Ensure all paginated URLs use standard a href links.
Zero near-duplicate or semantically similar pages | COMPLETE | Content bulk export confirms 0 duplicate pairs across 384 pages | No action required. Monitor as location-specific and service-line pages are added.

[TABLE 7]
Finding | Priority | Current State | Recommended Action
17 redirecting URLs in sitemap | HIGH | Sitemap sends Google through redirect hops on every crawl cycle | Replace all 17 sitemap redirect entries with final destination URLs. Resubmit sitemap in GSC after update.
17 internal 3xx redirects -- update source links | MEDIUM | 1.69% of internal crawled URLs redirect rather than resolving to final destination | Export Internal Redirection Inlinks from Screaming Frog. Update each source link href to the final URL directly.
Zero redirect chains, loops, JS redirects | COMPLETE | Clean redirect profile confirmed across full crawl | No action required. Monitor with each content deployment.

[TABLE 8]
Finding | Priority | Current State | Recommended Action
Homepage meta description confirmed present via Rank Math PRO (Screaming Frog crawl undercounted) | HIGH | synergyhealth.org/ has a meta description confirmed live via Rank Math PRO: "Southeast Michigan's integrated orthopedic and spine destination. 70+ board-certified surgeons across 12 locations with same-week appointments." Screaming Frog crawl missed it. | Meta description is confirmed present. Review and optimize if needed — current copy is strong. Confirm the crawl tool is capturing Rank Math-rendered output on re-audit.physical therapy under one roof. Same-day appointments available.
120 pages have duplicate title tags (31.3%) | HIGH | 120 of 423 pages share a title with at least one other page. Top duplicates: 36x Locations, 14x Providers, 13x Treatments, 9x Book an Appointment | Fix at the archive template level in Yoast or RankMath. Set archive titles to dynamically include archive name, location context, and specialty.
55 of 423 pages missing meta description (13%) | HIGH | All 7 named location pages (Sterling Heights, Livonia, Port Huron, Southfield, Troy, Synergy Surgery Center, Genesys Surgery Center), key provider bios (Mendelson MDs, Scott McCarty, Stephen Mendelson), and conversion pages (/book-an-appointment/, /about-us/, /insurance-billing/) confirmed missing. Homepage present. | Priority: (1) all 7 location pages — these drive local pack and local AIO queries; (2) high-traffic physician bios (Mendelson family, McCarty); (3) /book-an-appointment/ and /about-us/.
86 pages with duplicate meta descriptions | HIGH | 36x Locations Archive, 14x Providers Archive, 13x Treatments Archive -- WordPress archive plugin defaults, not written descriptions | Same template fix as title duplicates. Archive meta descriptions must be dynamically generated.
Carpal tunnel: position 1.37, 15,605 impressions, 0.03% CTR | HIGH | /conditions-we-treat/hand-upper-extremity-conditions/carpal-tunnel-syndrome/ ranks #1-2 and generates 4 clicks. Generic title tag almost certainly the cause. | Rewrite title and meta description immediately. Compelling title: Carpal Tunnel Syndrome Treatment Southeast Michigan -- Synergy Health. Could generate 300+ additional monthly patient visits from existing rankings.
14 pages missing H1 (confirmed via re-crawl 2026-06-25) | HIGH | Confirmed: /about-us/, /insurance-billing/, /book-an-appointment/, /patient-center/, /insurance-billing/medicare/, /workers-compensation/, /commercial/, /recovery-guide/, /patient-center/patient-forms/, /patient-center/pay-my-bill/, and all 7 booking parameter pages | Fix critical patient-journey pages first: /book-an-appointment/ and all insurance pages.
270 pages have non-sequential H1 (70.3%) | HIGH | H1 is not the first heading element on 70.3% of pages -- a heading precedes it in the template | One WordPress theme template edit resolves the majority. A heading in the site header or promotional banner area precedes the content H1.
74 pages have duplicate H1 text across pages | MEDIUM | Single-word H1s: Knee, Hip, Hand and Wrist, Shoulder, PT, OT each appear 3x. Location city names appear 2x each | Rewrite H1s to be unique and descriptive. Knee Pain Treatment Michigan outperforms Knee for both SEO and patient trust.
11 images missing alt text; 203 missing size attributes | MEDIUM | 11 ADA compliance failures; 203 images confirmed as CLS contributors by both crawl and PageSpeed | Add alt text to 11 images. Add width/height to 203 -- template fix resolves majority.

[TABLE 9]
Finding | Priority | Current State | Recommended Action
Schema partially deployed via Rank Math PRO — critical gaps and quality errors confirmed | HIGH | BreadcrumbList sitewide via Rank Math PRO. MedicalClinic + MedicalOrganization on location pages (with quality errors). MedicalCondition on condition pages. Missing: Physician schema on 70 provider bios, FAQPage, correct homepage entity type. sameAs errors sitewide link to competitor YouTube (@mendelsonortho) and wrong LinkedIn entity (/company/mkoss/). | Complete and correct the Rank Math schema implementation. Priority: (1) Hospital @type fix on 42 MD/DO/DPM provider bios — resolves 22–61 schema validation errors per page and unblocks rich result eligibility. Secondary: evaluate HealthcareProfessional schema for 38 allied health provider pages.; (2) Fix homepage entity type from Organization/Person hybrid to MedicalOrganization with correct medicalSpecialty properties; (3) Fix sameAs errors sitewide — YouTube sameAs currently resolves to competitor channel @mendelsonortho, LinkedIn sameAs resolves to /company/mkoss/; (4) Fix location schema quality issues — remove Hospital @type from clinic-level pages, repair corrupted openingHoursSpecification, remove Unicode separator from name field; (5) Implement FAQPage schema on condition and treatment pages with FAQ sections; (6) Implement MedicalProcedure schema on 72 treatment pages.
MedicalOrganization schema on homepage: wrong entity type | HIGH | Homepage has schema but wrong types: Organization/Person hybrid and Article schema (incorrect for a medical practice). MedicalOrganization with correct medicalSpecialty properties is absent. | Replace wrong entity types with proper MedicalOrganization: name, url, logo, description, medicalSpecialty (Orthopedics, Spine Surgery, Pain Management, Physical Therapy, Podiatry), availableService, and corrected sameAs — fix YouTube reference (currently points to competitor channel @mendelsonortho), fix LinkedIn reference (currently /company/mkoss/), add GBP, Healthgrades, Vitals, Zocdoc, Zimmer Biomet.
MedicalClinic schema on 8 location pages has confirmed quality errors | HIGH | All 8 location pages have MedicalClinic + MedicalOrganization schema via Rank Math PRO. Confirmed quality errors: Hospital @type applied to clinic-level pages (should be MedicalClinic only), corrupted openingHoursSpecification with overlapping entries, and Unicode line separator (\u2028) in location name field. | Correct the existing MedicalClinic schema in Rank Math per location: remove Hospital @type (these are ambulatory care clinics, not hospitals), repair corrupted openingHoursSpecification entries (overlapping hours for same days), remove Unicode line separator from name property. Verify geo coordinates and telephone match GBP listings.
Physician schema on 42 MD/DO/DPM pages has 22–61 validation errors per page; 38 allied health pages have no Physician schema | HIGH | 42 MD/DO/DPM pages have Physician schema via Rank Math PRO. All 42 also carry Hospital @type — driving 22–61 schema validation errors per page. Hospital is wrong type for individual physician pages (required Hospital properties like availableBed are unpopulated). 38 allied health pages (PA-C, PT, OT, PTA) have no Physician schema.o MD, Preetinder Bhullar MD, Lucia Zamorano MD, Scott McCarty MD, Tony Abood DO, Randy Leff DPM, Kyle Bohm MD, Mohamed Salar MD | Fix the Hospital @type error in Rank Math org entity definition — removing it from provider bio context will resolve ~50 validation errors per page and correct the entity type. For allied health pages, evaluate HealthcareProfessional or MedicalBusiness @type.rOf (board certifications).
BreadcrumbList deployed sitewide via Rank Math but malformed on provider bio pages | MEDIUM | BreadcrumbList is present on all pages via Rank Math PRO. Issue: provider bio page breadcrumbs are malformed — insurance acceptance pages appear as breadcrumb ancestors (e.g., Home > Policies & Insurance > Accepted Insurances > [Physician Name]), which does not reflect actual site hierarchy. | Fix malformed BreadcrumbList on all 70 provider bio pages in Rank Math. Correct ancestor chain to actual hierarchy: Home > Providers > [Physician Name]. Remove insurance acceptance pages from provider bio breadcrumb paths.
No FAQPage schema -- FAQ infrastructure confirmed present | MEDIUM | faq.css and faq.js confirmed loading site-wide in PageSpeed data -- FAQ content exists but not marked up | Implement FAQPage/Question/Answer schema on all pages with FAQ sections. Parsed by ChatGPT, Perplexity, Claude, and Google AI for citation content.

[TABLE 10]
Page Type | Schema Types to Implement
Homepage (1 page) | MedicalOrganization, BreadcrumbList
Location pages (8 pages) | MedicalClinic, LocalBusiness, GeoCoordinates, BreadcrumbList
Provider bios (70 pages) | Physician, BreadcrumbList
Condition pages (61 pages) | MedicalCondition, BreadcrumbList, FAQPage
Treatment pages (72 pages) | MedicalProcedure or MedicalTherapy, BreadcrumbList, FAQPage
Blog and article pages | Article, Author (Physician where applicable), BreadcrumbList
Patient resource and FAQ pages | FAQPage, BreadcrumbList

[TABLE 11]
Date | Status
March 16 -- April 30, 2026 | 184-238 Good URLs -- PASSING. Site in Good CWV status for 46 days.
May 1, 2026 | 104 Good, 61 Need Improvement -- REGRESSION BEGINS. First NI URLs appear.
May 3, 2026 | 33 Good, 127 Need Improvement -- RAPID COLLAPSE. Good down 80% in 3 days.
May 6, 2026 | 1 Good, 183 Need Improvement -- CRITICAL. Effectively zero Good URLs.
May 13, 2026 | 0 Good, 173 Need Improvement -- COMPLETE FAILURE.
June 13, 2026 (audit date) | 0 Good, 223 Need Improvement -- STILL FAILING. Six weeks at zero Good URLs.

[TABLE 12]
Finding | Priority | Current State | Recommended Action
CWV regression: 0 Good URLs since May 13 -- was 238 Good on April 23 | HIGH | Site went from peak passing status to complete failure in 3 weeks. 6 weeks elapsed with no fix. LCP issue Not Started in GSC validation. CLS issue Started but unresolved. | URGENT: Audit all deployments between April 25 and May 3. Compare site state in PageSpeed or staging snapshots. Likely culprits: CSS/JS change increasing render-blocking, new third-party script, logo.svg replacement at 1,032KB, Hotjar or Zocdoc configuration change.
logo.svg: 1,032KB with 4-hour cache TTL | HIGH | Site logo SVG is 1MB -- 20-50x larger than an optimized SVG. All static assets cached only 4 hours. | Optimize logo.svg to under 20KB immediately. Extend all static asset cache TTL to 1 year (max-age=31536000).
home.mp4 background video: 11,163KB | HIGH | Hero background video is 11MB -- largest single asset on the site | Compress to under 2MB using H.264 at 720p. Add poster attribute with static image for first paint.
Hotjar: 3,443ms CPU time -- worst third-party script | HIGH | Single most expensive script. Microsoft Clarity also running simultaneously -- dual session recording. | Defer Hotjar to GTM scroll trigger or remove if Clarity provides equivalent functionality. Running both doubles CPU cost.
liine.com call tracking: 343KB, 86% unused | HIGH | 341KB bootstrapped JS with 86% unused code on every page load | Move to GTM window-load trigger. Load only on contact and location pages.
50+ render-blocking CSS files -- 2,540ms est. savings | HIGH | Every page loads 50+ component-level CSS files synchronously in head before rendering begins | Consolidate all component CSS into a single minified stylesheet. Load non-critical CSS asynchronously. Highest LCP improvement available.
Adobe TypeKit: 7,387ms critical path | HIGH | Final TypeKit font file is the longest single dependency in the critical path | Add font-display: swap. Preload only 2 most-used weights. Evaluate self-hosting.
DOM: 27,528 elements (threshold 800) -- 34x recommended size | HIGH | Testimonials slider alone has 3,126 child elements -- all rendered simultaneously | Virtualize the testimonials carousel to render only visible and adjacent slides.
CSP blocking Clarity and Cloudflare Beacon | HIGH | scripts.clarity.ms and static.cloudflareinsights.com blocked by CSP -- analytics data lost on every page load | Add both domains to script-src in CSP header. 5-minute server config fix.
203 images missing size attributes (70%) -- confirmed CLS contributor | MEDIUM | 8 named SVG body-part images and 18 affiliate logos confirmed by Lighthouse as CLS sources | Add explicit width and height to all image elements. Template fix resolves majority.
13 pages exceed 2-second server response time | MEDIUM | Worst: /treatment/emg/ (3.1s), /providers/loretta-assalone-otr-l-cht/ (2.5s), /treatment/rotator-cuff-repair/ (2.4s) | Investigate top 3 pages individually for unoptimized images or synchronous third-party embeds.

[TABLE 13]
Finding | Priority | Current State | Recommended Action
6 consent modal inputs lack associated labels | HIGH | synergy-analytics plugin consent modal -- checkbox inputs and toggle labels not properly associated for screen readers | Fix in the synergy-analytics plugin. Each toggle switch needs for/id pairing or aria-labelledby. This failure appears on every page load for every screen reader user.
7 Leaflet map markers have no accessible names | HIGH | All clickable location markers in #fal-map have role=button but no accessible name -- screen readers announce as generic button | Add aria-label to each marker: Synergy Health [Location Name] -- click to view details. Single JavaScript component fix.
Hero background video missing captions track | HIGH | Hero video element has no captions track -- WCAG 1.2.2 violation | For decorative video: add role=presentation and aria-hidden=true to remove from accessibility tree.
2 consent footer links: color-only differentiation | MEDIUM | Privacy Policy links fail WCAG 1.4.1 -- color is the only visual differentiator | Add text-decoration: underline to .synergy-consent-link in consent banner CSS.
4 Find a Doctor CTAs point to a 404 URL | MEDIUM | /patient-center/find-a-doctor/ is a confirmed 404. Multiple CTAs still point to it. | Standardize all Find A Doctor CTAs to /providers/ with trailing slash. This is also a patient conversion failure.
Zero viewport, tap target, or font-size errors | COMPLETE | All 384 pages pass Screaming Frog mobile usability checks | No action required.

[TABLE 14]
Finding | Priority | Current State | Recommended Action
CSP blocks Clarity and Cloudflare Beacon -- analytics data lost | HIGH | scripts.clarity.ms and static.cloudflareinsights.com blocked by CSP. Lighthouse console errors confirmed on every page load. Active analytics tools returning zero data. | Add both domains to script-src directive immediately. 5-minute server config fix. Data loss stops instantly.
CSP uses unsafe-inline -- ineffective XSS protection | HIGH | Lighthouse explicitly flags CSP as ineffective: unsafe-inline allows execution of any inline script; host allowlists are bypassable | Medium-term: rebuild CSP to use nonces or hashes. Implement strict-dynamic to replace growing host allowlist.
Missing X-Content-Type-Options on 394 URLs (49%) | HIGH | 394 of 807 internal URLs missing nosniff header | Add X-Content-Type-Options: nosniff at Cloudflare or server level. Single configuration line.
Missing X-Frame-Options on 394 URLs (49%) | HIGH | 394 URLs missing clickjacking protection -- appointment and patient forms at risk | Add X-Frame-Options: SAMEORIGIN at CDN or server level.
Missing Referrer-Policy on 395 URLs (49%) | MEDIUM | Patient URL paths containing appointment parameters could leak to third-party servers | Implement Referrer-Policy: strict-origin-when-cross-origin at CDN or server level.
HSTS missing on 186 URLs (23%) | MEDIUM | Partial HSTS -- HTML pages have it, static assets do not | Extend Strict-Transport-Security: max-age=31536000; includeSubDomains to all response types.
100% HTTPS, zero mixed content, zero insecure forms | COMPLETE | Full HTTPS confirmed across all 807 internal URLs | No action required.

[TABLE 15]
Location URL | Status
https://synergyhealth.org/locations/sterling-heights/ | 1,980 words -- No meta description -- H1: Sterling Heights
https://synergyhealth.org/locations/southfield/ | 1,851 words -- No meta description -- 9 competing URL variants in GSC
https://synergyhealth.org/locations/troy/ | 1,794 words -- No meta description -- H1: Troy
https://synergyhealth.org/locations/livonia/ | 2,036 words -- No meta description -- H1: Livonia
https://synergyhealth.org/locations/port-huron/ | 1,786 words -- No meta description -- H1: Port Huron
https://synergyhealth.org/locations/synergy-surgery-center/ | 2,131 words -- No meta description
https://synergyhealth.org/locations/genesys-surgery-center/ | 1,717 words -- No meta description
https://synergyhealth.org/locations/ (archive) | 1,761 words -- Generic meta: Locations Archive - Synergy Health -- 212 clicks, 29,824 impressions

[TABLE 16]
Finding | Priority | Current State | Recommended Action
MedicalClinic schema on all 8 location pages has quality errors requiring correction | HIGH | All 8 location pages have MedicalClinic + MedicalOrganization schema via Rank Math PRO. Confirmed errors: Hospital @type on clinic-level pages, corrupted openingHoursSpecification entries, Unicode separator character in location name field. | Correct the existing Rank Math MedicalClinic schema: remove Hospital @type, repair corrupted openingHoursSpecification entries, remove Unicode separator from name field. Cross-reference all address, telephone, and geo values against GBP listings per location.
7 of 8 location pages missing meta description | HIGH | All location pages except the archive have no meta description | Write unique, location-specific meta descriptions. Format: Orthopedic and spine care in [City], Michigan. Board-certified surgeons, pain management, and physical therapy under one roof. Same-day appointments. Call [phone].
Southfield: 9 competing URL variants in GSC | HIGH | 9 different Southfield URL structures confirmed in GSC -- all splitting authority | Consolidate to /locations/southfield/. 301 redirect all variants. Update all GBP, internal, and external links.
Location H1s are city names only -- no specialty context | MEDIUM | H1s: Sterling Heights, Southfield, Troy -- no specialty, service, or clinical context | Expand H1s: Orthopedic and Spine Care in Sterling Heights, MI outperforms Sterling Heights for both local SEO and patient trust.
GBP-to-on-page NAP consistency unverified | HIGH | Cannot confirm phone numbers, addresses, and hours match GBP listings without GBP access | Conduct manual NAP audit per location. Any discrepancy in suite number format, phone format, or business name suppresses local pack rankings.

[TABLE 17]
Finding | Priority | Current State | Recommended Action
No llms.txt file at synergyhealth.org/llms.txt | HIGH | LLM crawlers have no site map or content prioritization guidance | Create llms.txt at domain root. Include: organization description, URL sections by content type (Spine Conditions, Orthopedic Conditions, Treatments, Provider Bios, Locations, Patient Resources). Link 50-100 highest-authority URLs. 30-minute task, zero development resources.
Partial schema via Rank Math PRO — Physician schema and FAQPage absent, limiting structured extraction | HIGH | BreadcrumbList sitewide, MedicalClinic/MedicalOrganization on location pages, MedicalCondition on condition pages. Missing: Physician schema on 70 provider bios and FAQPage on clinical content — the two schema types AI systems most rely on for healthcare citations. | Complete the Rank Math schema per Pillar 6. For AIO specifically: Physician schema exists on 42 provider bios but 22–61 validation errors per page suppress rich result eligibility — fixing the Hospital @type error is the prerequisite. FAQPage (0 pages) is the primary remaining gap for AI Q&A extraction. MedicalCondition (54 pages) and MedicalProcedure (70 pages) are deployed — verify property completeness.
309 pages (80%) rated Fairly Hard or Hard to read | HIGH | Content bulk export: 229 pages Fairly Hard, 80 Hard -- college-graduate level prose on patient-facing pages. AI systems strongly prefer clear, unambiguous language for citation. | Rewrite condition and treatment pages to 7th-8th grade reading level. Prioritize by impression volume: lymphedema management, neck fracture, TKA, PRP, cervical fusion, carpal tunnel.
AI crawler access in robots.txt unverified | MEDIUM | Robots.txt allowance for GPTBot, PerplexityBot, ClaudeBot, ChatGPT-User, Google-Extended not confirmed | Verify robots.txt allows all retrieval and agent bots. Do not block bots that serve live user queries.
Content structure is narrative, not answer-first | MEDIUM | All pages have substantive word counts (positive) but use narrative prose rather than definitive-answer-first format | Restructure condition pages to lead with a clear, direct answer. Use question-format H2 headings. FAQ schema with 8-12 questions using natural patient language.
Zero rich results in GSC Search Appearance -- confirmed | HIGH | One Search Appearance entry: Translated Results (17 clicks). Zero FAQ, review, sitelink, or other rich result types. | Schema implementation (Pillar 6) is the only mechanism to unlock rich results and AI Overview eligibility.

[TABLE 18]
13,668 Total Clicks (90 Days) | 1,186,066 Total Impressions (90 Days) | 1.15% Overall CTR vs 3-5% Benchmark | 80% Clicks from Branded Queries

[TABLE 19]
Finding | Priority | Current State | Recommended Action
Carpal tunnel: position 1.37, 0.03% CTR | HIGH | /conditions-we-treat/hand-upper-extremity-conditions/carpal-tunnel-syndrome/ ranks #1-2 for 15,605 impressions, 4 clicks. Most severe single-page CTR failure in dataset. | Rewrite title tag and meta description immediately. 20-minute task. Could generate 300+ additional monthly patient visits from existing #1 rankings.
TKA cluster: 30,143 impressions, 0.06% CTR across 15 pages | HIGH | Two competing pages: /treatment/total-knee-arthroplasty-tka/ (38,350 impressions, 9 clicks) and /specialties/.../tka-comprehensive-guide/ (26,755 impressions, 23 clicks) | Consolidate into one canonical hub. Redirect all 14 competing pages. Schema + title rewrite on consolidated page could 10x current clicks from existing rankings.
80% of clicks are branded -- non-branded organic near-zero | HIGH | 4,177 branded clicks vs 1,462 non-branded. 58% of impressions are non-branded but convert at 1.01% vs 4.88% branded CTR | Schema, content hubs, and AIO investment (Pillars 6, 11) are the mechanisms to grow non-branded reach. 6-12 month strategic investment.
GBP links outperform organic on equivalent queries | MEDIUM | GBP UTM links: 1,781 clicks at 2.75-3.5% CTR at position 3-4. Organic location pages: lower CTR at worse positions. GBP is working; organic local is not. | Schema and meta improvements to location pages should close the CTR gap between GBP-referred and organic traffic.
Zero rich results in Search Appearance | HIGH | One Search Appearance entry: Translated Results (17 clicks). Zero FAQ, review, physician, or sitelink rich results. | Schema implementation is the only mechanism to unlock rich results.

[TABLE 20]
URL | Performance
https://synergyhealth.org/ (homepage) | 124,481 impressions, pos 8.14, 1.41% CTR -- 1,750 clicks
https://synergyhealth.org/conditions/neck-fracture-broken-neck/ | 48,166 impressions, pos 7.17, 0.21% CTR -- 103 clicks
https://synergyhealth.org/treatment/total-knee-arthroplasty-tka/ | 38,350 impressions, pos 9.33, 0.02% CTR -- 9 clicks
https://synergyhealth.org/specialties/physical-therapy/lymphedema-management/ | 34,110 impressions, pos 6.21, 0.33% CTR -- 111 clicks
https://synergyhealth.org/treatment/prp-injections/ | 23,557 impressions, pos 6.17, 0.05% CTR -- 12 clicks
https://synergyhealth.org/specialties/spine-back-and-neck/cervical-fusion/ | 16,815 impressions, pos 8.94, 0.07% CTR -- 12 clicks

[TABLE 21]
Finding | Priority | Current State | Recommended Action
Staging domain synergy.egowebdev.com is live and crawlable | HIGH | 7 links from the pre-rebrand development domain are being crawled by Google. The staging site contains legacy content pages. | Password-protect or robots.txt-block the staging domain immediately. Add to GSC disavow file if needed.
No links from Michigan hospital systems or health networks | HIGH | Zero links from Henry Ford Health, Corewell/Beaumont, McLaren Health Care -- primary referring health systems | Develop a PR and partnership strategy targeting hospital system links. Physician affiliation pages and referral relationship pages are the natural acquisition vehicles.
No links from medical associations | HIGH | Zero links from AAOS, Michigan Orthopedic Society, American Podiatric Medical Association | Build relationships with state and national orthopedic organizations. Conference speaker opportunities and board membership announcements naturally generate association links.
No links from insurance company provider directories | MEDIUM | Zero links from BCBS Michigan, Blue Care Network, Priority Health | Request provider directory page inclusions from all in-network insurance companies. High-authority healthcare directory links with direct patient referral value.
Google Play app links inflate the authoritative link count | MEDIUM | 82 of 135 authoritative links are Play Store localized listings for legacy MKO patient app -- single source | These are genuine but represent a single source. Effective unique authoritative domain count is closer to 5-10 meaningful editorial sources.
Zimmer Biomet: 15 links from global orthopedic implant manufacturer | MEDIUM | 15 links from zimmerbiomet.com/find-a-doctor -- high-authority E-E-A-T signal that should be expanded | Add zimmerbiomet.com to sameAs in Physician schema for qualifying surgeons. Expand Find-a-Doctor listings for all eligible physicians.

[TABLE 22]
Content Area | URLs | Impressions | Clicks | CTR | AIO Assessment
/specialties/ content | 76 | 205,968 | 560 | 0.27% | THIN -- High reach, near-zero conversion. Content lacks AIO-ready structure.
/treatment/ content | 56 | 179,993 | 329 | 0.18% | WEAK -- Treatment pages present but no schema, poor title/meta signals.
/providers/ content | 126 | 182,107 | 4,919 | 2.70% | BEST -- Provider pages drive most organic clicks. Schema here has highest immediate ROI.
/conditions-we-treat/ content | 85 | 110,402 | 78 | 0.07% | CRITICAL GAP -- Legacy URL structure, near-zero CTR, no schema.
/conditions/ content | 39 | 110,402 | 194 | 0.18% | WEAK -- Duplicate URL structure competing with /conditions-we-treat/. Consolidation required.
/locations/ content | 25 | 117,771 | 1,654 | 1.40% | MODERATE -- Location pages underperform given impression volume. Schema and meta missing.
TKA cluster (14 queries) | 15 pages | 30,143 | 19 | 0.06% | CRITICAL -- 30K impressions, 19 clicks. 15 competing pages diluting authority.

[TABLE 23]
Finding | Priority | Current State | Recommended Action
Provider pages are the strongest organic asset | STRONG | 4,919 clicks from 182,107 impressions -- 2.70% CTR -- best-performing content type | Implement Physician schema on all 70 confirmed provider bio pages immediately. Each page with schema becomes a Knowledge Panel candidate and AIO citation source.
TKA cluster has existing page-one presence | STRONG | 14 TKA-related queries getting 30,143 impressions at average position 6-10 | The rankings exist. The problem is 15 competing pages splitting authority. Consolidation could 10x current 19 clicks from 30,143 impressions.
Brand promise maps to AIO preferred formats | STRONG | Clear answers, faster is precisely the format AI Overviews prefer -- definitions, FAQs, decision frameworks | Content execution needs to match: 50-75 word definitions, Quick Answer boxes, FAQ schema, decision criteria.
Neck fracture content has organic reach | STRONG | /conditions/neck-fracture-broken-neck/: 48,166 impressions -- highest-impression condition page | Apply AIO-ready structure (definition-first, FAQ schema, when-to-seek-care) and MedicalCondition schema to convert impressions into clicks.

[TABLE 24]
Finding | Priority | Current State | Recommended Action
Foundational spine conditions absent or thin | HIGH | Zero visibility for stenosis, herniated disc, sciatica, DDD, spondylolisthesis -- the front-door queries of spine patient journeys | Build five foundational spine condition hubs. Highest-ROI content investment for non-branded traffic growth.
TKA cluster: 15 pages competing for same queries | HIGH | The query tka alone gets 16,043 impressions at 0.04% CTR. Two main competing pages each have 20,000+ impressions | Consolidate all TKA content into one canonical hub with FAQ schema (minimum 12 FAQs), recovery milestones, and physician schema linking to relevant orthopedic surgeons.
Content structure is transactional, not educational | HIGH | Pages over-index on CTAs and under-index on answer-style content where AIO Overviews originate | Definition-first openings, Quick Answer boxes, FAQ schema, and decision criteria are the content patterns that get cited. The current structure prioritizes appointment CTAs over clinical education.
80% of clicks are branded -- non-branded capture near zero | HIGH | 4,539 branded clicks vs 1,100 non-branded clicks. 58% of impressions are non-branded. | Non-branded organic traffic requires topical authority, AIO citation eligibility, and content answering questions patients ask before they know which practice to choose.

[TABLE 25]
Query | Clicks | Impressions | CTR | Position | Assessment
hand specialist near me | 1 | 745 | 0.13% | 3.06 | Position 3 -- near-zero CTR. Title/meta failure on destination page.
hand surgeon near me | 2 | 731 | 0.27% | 2.28 | Position 2 -- 2 clicks from 731 impressions. Schema and meta fix needed.
mri near me | 36 | 686 | 5.25% | 2.82 | Best-performing local query. MRI service GBP and local signals working.
podiatrist near me | 11 | 328 | 3.35% | 4.65 | Good CTR for position 5. Schema would improve.
pain management near me | 10 | 274 | 3.65% | 3.90 | Reasonable performance. Location schema would lift this further.
physical therapy livonia | 5 | 594 | 0.84% | 4.55 | City-specific query at position 4.5 with low CTR. Location page meta fix needed.
physical therapy sterling heights | 1 | 319 | 0.31% | 17.23 | Position 17 -- content gap. Sterling Heights PT page needs local hub treatment.
spine surgeon near me | 2 | 51 | 3.92% | 2.75 | Small impression volume. Content depth and schema investment would grow this.

[TABLE 26]
Finding | Priority | Current State | Recommended Action
Location pages lack every required local schema signal | HIGH | MedicalClinic schema on all 8 location pages has quality errors requiring correction. 7 of 8 have no meta description. H1s are single city names. | Implement MedicalClinic JSON-LD on all 8 locations. Add unique meta descriptions. Expand H1s to Orthopedic and Spine Care in [City], MI.
No hyper-local condition + city pages exist | HIGH | No pages combining herniated disc livonia, knee replacement sterling heights, spine specialist southfield -- the format AI local searches extract | Build 10-15 hyper-local service pages in Days 31-60. Each page: provider module, access messaging, outcomes proof, location FAQ schema.
NAP consistency unverified across 8 locations | HIGH | GBP-to-on-page NAP consistency not confirmed. Any discrepancy suppresses local pack rankings. | Manual NAP audit per location. Citation audit via BrightLocal or Whitespark against Healthgrades, Vitals, Yelp, Bing Places, Apple Maps.
Legacy /full-service-clinics/ URLs competing with /locations/ pages | HIGH | /full-service-clinics/sterling-heights-2/ is #3 clicked page (366 clicks) -- a pre-rebrand URL receiving real patient traffic | 301 redirect all /full-service-clinics/ to /locations/ equivalents. Sterling Heights redirect must be implemented carefully.

[TABLE 27]
Dimension | National Leaders | Regional Systems | Synergy Current | Synergy Opportunity
Topical authority | 70-85+ | 45-60 | 31.8 | Reach 45-55 by 12 months with spine hub + schema investment
Schema implementation | Full suite | Partial | Zero | Partial to full in 30-60 days — correct entity types, add Physician schema, fix sameAs errors
Content depth per condition | 10-20+ pages | 3-7 pages | 1-3 thin pages | Build 5 foundational spine hubs first; replicate for ortho
AIO citation frequency | Very high | Moderate | Near zero | Schema + structure + topical depth drives citation eligibility
Local pack visibility | National brand dilution | Strong (location scale) | Moderate (GBP working) | Hyper-local schema + content creates defensible local moat
E-E-A-T signals | Institutional + physician authorship | Institutional | Provider bios exist, no schema | Physician schema + credential visibility is the fix
Review velocity | Systematized | High volume | Under-leveraged | Review program tied to care milestones builds authority fast
Patient access (same-week) | Cannot compete | Typically 2-4 weeks | Same-week -- genuine advantage | Operationalize in schema, meta, GBP, and content
Integrated care model | Fragmented (referrals) | Partially integrated | Fully integrated | Own this positioning -- AI can summarize it if structured

[TABLE 28]
Finding | Priority | Current State | Recommended Action
Coordinated care pathway as a content differentiator | STRONG | No runaround positioning directly addresses the documented pain point of fragmentation at large systems | Build pages showing the integrated care steps. Spine Care at Synergy: From First Visit to Full Recovery is a page national brands cannot credibly publish.
Same-week access as a conversion trigger | STRONG | Same-week access is a documented conversion advantage -- national brands and large systems cannot routinely offer this | Operationalize everywhere: GBP service descriptions, location page meta descriptions, FAQPage schema answers, and appointment booking CTA copy.
Hyper-local content moat against national brands | STRONG | National brands rank for generic condition queries but not for knee replacement surgeon Livonia MI or spine specialist Sterling Heights same week | 10-15 hyper-local service pages with schema, provider modules, and access messaging create a defensible Southeast Michigan moat.

[TABLE 29]
Finding | Priority | Current State | Recommended Action
Coordination and continuity of care | STRONG | Core brand differentiator and documented pain point of large system competitors | Surface in FAQPage schema. A FAQPage answer to Why choose Synergy Health? citing integrated care and same-week access is directly citeable by AI Overviews.
Access speed -- same-week appointments | STRONG | Conversion-driving claim competitors cannot routinely match | Appear as crawlable HTML text on every location page, in openingHoursSpecification schema, in GBP service descriptions, and in FAQPage schema answers.
Provider relationship strength | STRONG | Provider pages drive 2.70% CTR -- highest organic performance on the site | Physician schema transforms this performance into structured entity authority. Each physician becomes a named medical entity AI systems can cite.

[TABLE 30]
Finding | Priority | Current State | Recommended Action
Review platform diversification -- beyond GBP | HIGH | Strong GBP review presence confirmed. Healthgrades, Vitals, Doximity, and WebMD profiles likely incomplete or unclaimed -- these are the platforms AI systems cross-reference for healthcare source authority. | Claim and complete Healthgrades, Vitals.com, Doximity (per physician), WebMD physician directory profiles. Add AggregateRating schema linking to these platforms where visible review counts appear on-page.
Billing and insurance friction is a latent sentiment risk | MEDIUM | Common healthcare pain point -- if not proactively addressed in content, it surfaces in reviews | Publish billing and insurance clarity content as a trust feature. What Your Costs Depend On, How We Verify Your Insurance Before Your Visit, Who to Call with Billing Questions.
HIPAA compliance in public review responses | MEDIUM | Healthcare organizations face specific constraints in responding to patient reviews -- confirming a patient relationship violates HIPAA | Develop a standardized HIPAA-safe review response protocol. Do not confirm or deny a patient relationship. Invite private resolution for negative reviews.

[TABLE 31]
Entity Signal | Current State | Priority | Action Required
MedicalOrganization schema | CRITICAL | HIGH | Implement on homepage. Properties: name, url, logo, description, medicalSpecialty, availableService, sameAs (GBP, Healthgrades, Vitals, Zocdoc, Zimmer Biomet, LinkedIn).
MedicalClinic schema per location | CRITICAL | HIGH | Fix errors on all 8 location pages. Remove Hospital @type, repair corrupted openingHoursSpecification, remove Unicode separator from name. Verify PostalAddress, telephone, and GeoCoordinates against GBP listings.
Physician schema (70 providers) | CRITICAL | HIGH | Implement on all 70 provider bios. Properties: name, honorificSuffix, medicalSpecialty, affiliation, alumniOf, memberOf (board certifications). Validates physician entities for AI citation.
MedicalCondition schema | ABSENT | HIGH | MedicalCondition schema confirmed present on condition pages via Rank Math PRO. Verify full property coverage: associatedAnatomy, possibleTreatment, signOrSymptom, relevantSpecialty. Extend to any condition pages missing it.
MedicalProcedure schema | ABSENT | HIGH | Implement on 72 treatment pages. Properties: name, procedureType, bodyLocation, preparation, followup.
FAQPage schema | ABSENT | HIGH | Implement on all condition and treatment pages with FAQ sections. Directly parsed by ChatGPT, Perplexity, Claude, and Google AI for citation content.
Physician authorship on clinical content | ABSENT | HIGH | Add Medically reviewed by [Name], MD bylines to all clinical pages. Format: name, specialty, review date. Direct YMYL quality signal.
llms.txt file | ABSENT | HIGH | Create at domain root. Provides AI crawlers with site map and content priority guidance. 30-minute implementation.
Staging domain synergy.egowebdev.com | LIVE | HIGH | Password-protect immediately. Creates duplicate content risk and leaks link equity.
Zimmer Biomet links (15 existing) | PRESENT | MEDIUM | Add zimmerbiomet.com to sameAs in Physician schema for qualifying surgeons. Expand Find-a-Doctor listings for all eligible physicians.
Trust compliance visibility (HIPAA NPP) | LOW | LOW | Add footer links to HIPAA Notice of Privacy Practices and Privacy Policy. Add educational content disclaimer to clinical pages.

[TABLE 32]
Content Gap | Current GSC Status | Why It Matters for AIO
Spinal stenosis | Zero clicks, zero page-one presence | Front-door spine query -- patients searching this are deciding whether to seek care
Herniated disc treatment | Minimal presence | Highest-volume spine condition query category -- Synergy has no topical authority
Sciatica / radiculopathy | Minimal presence | Common presenting symptom leading to spine specialist consultation
Degenerative disc disease | Zero page-one presence | Chronic condition with high long-term patient value
Spondylolisthesis | Zero page-one presence | Specialty spine condition where Synergy surgical expertise should rank
Microdiscectomy | Zero clicks, 3,701 impressions, pos 7.87 | Strong reach, zero conversion. Page exists but needs AIO-ready structure.
PRP injections | 12 clicks from 23,557 impressions (0.05% CTR) | 23K impressions at pos 6.17 -- title/meta/schema fix would unlock this
Cervical fusion | 12 clicks from 16,815 impressions (0.07% CTR) | High reach, very low CTR -- same pattern as carpal tunnel and TKA
Knee replacement recovery | Zero specific presence | Recovery timeline queries are among highest-volume AIO trigger query types
Treatment comparisons (surgery vs PT) | Zero presence | Decision-support content format that AI Overviews frequently extract
Lymphedema management | 111 clicks from 34,110 impressions (0.33% CTR) | Highest-impression PT page. Schema and structure upgrade would amplify.

[TABLE 33]
Finding | Priority | Current State | Recommended Action
No AIO-ready page structure on any clinical page | HIGH | All condition and treatment pages lack: definition-first openings, Quick Answer boxes, FAQ schema, decision criteria sections | Standardize an AIO page framework: (1) 50-75 word plain-language definition, (2) Quick Answer box in 2-3 sentences, (3) FAQ schema with 8-12 questions, (4) When to see a specialist section, (5) Physician attribution byline, (6) Coordinated care pathway CTA.
Recovery and what-happens-next content is absent | HIGH | Zero recovery timeline pages for major procedures. Recovery queries are among the highest-volume AIO trigger query types. | Build recovery timeline content for top 5 procedures: TKA, spinal fusion, hip replacement, rotator cuff repair, lumbar discectomy. Use HowTo schema structure.
No treatment comparison content exists | HIGH | Zero comparison pages. Surgery vs PT for herniated disc, fusion vs decompression, injection options are exactly the formats AI Overviews extract for treatment decision queries. | Build 5-7 treatment comparison pages in Days 61-90. Format: decision table, patient criteria, pros and cons, Synergy integrated model CTA.
Freshness signals absent on clinical content | MEDIUM | No Last reviewed dates, no Medically reviewed by bylines on any clinical pages. YMYL quality evaluation rewards visible freshness. | Implement freshness governance: quarterly content review for top-traffic pages, Medically reviewed by [Name], MD visible on all clinical content.

[TABLE 34]
KPI | Baseline, Target, and Tracking Method
AIO citation rate by topic cluster | Baseline: near zero. Target: 10-15% by month 3. Tracked: monthly prompt testing in ChatGPT, Perplexity, and Google AI for 75 priority queries.
Core Web Vitals: Good URL count (mobile) | Baseline: 0 Good URLs (regression from 238 on April 23). Target: 100+ by Day 90. Tracked: GSC Core Web Vitals report daily.
Local pack visibility rate | Baseline: moderate. Target: 45-50% by month 3 for priority near me + city queries. Tracked: Local Falcon or BrightLocal grid tracking.
Organic CTR | Baseline: 1.15%. Target: 1.8-2.2% by month 3. Tracked: GSC Performance report.
Non-branded click share | Baseline: 20% of top-1000 query clicks. Target: 30-35% by month 6. Tracked: GSC query segmentation.
Organic consultation requests | Baseline: unknown (no conversion tracking). Target: +25-35% by month 3. Tracked: GA4 form events + call tracking.
Review velocity per location | Baseline: unknown. Target: steady monthly growth per location. Tracked: BirdEye, Podium, or ReviewTrackers.
Topical authority score | Baseline: 31.8. Target: 40-45 by months 3-6, 55-60 by month 12. Tracked: quarterly assessment.
Schema coverage | Baseline: Partial — BreadcrumbList sitewide, MedicalClinic/MedicalOrganization on location pages, MedicalCondition on condition pages. Gaps: Physician (0 of 70 provider bios), FAQPage (0 pages), MedicalProcedure (deployed on 70 treatment pages ✓). Target: Physician schema + corrected entity types by Day 60. Tracked: Screaming Frog re-crawl + GSC Enhancements report.
Rich result types in GSC Search Appearance | Baseline: 1 type (Translated Results). Target: FAQ rich results, breadcrumbs, physician results by month 2. Tracked: GSC Search Appearance report.

[TABLE 35]
Tool | Purpose
GSC + GA4 | Core performance: query data, page-level CTR, CWV field data, coverage, Search Appearance, consultation request events
Screaming Frog (monthly re-crawl) | Schema coverage, on-page signals, redirect health, sitemap quality, page speed integration
Local Falcon or BrightLocal Grid Tracker | Local pack visibility by location and query -- grid-based tracking shows Livonia vs Sterling Heights vs Southfield performance
Profound (AIO Measurement Platform) | AIO citation tracking, AI Overview visibility monitoring, competitive citation benchmarking across ChatGPT, Perplexity, and Google AI Overview
Semrush or Ahrefs | Rank tracking for 75-query AIO monitoring set, topical authority trend, competitor gap analysis, backlink monitoring
CallRail or similar call tracking | Attribution of phone calls to organic search -- essential for measuring consultation ROI from local queries
BirdEye, Podium, or ReviewTrackers | Review velocity and rating stability by location and provider

[TABLE 36]
Owner Label | Role Description
Dev Lead | Engineering or web development owner -- code deployments, server configuration, template changes
Dev/Infra | Server, CDN, or hosting configuration -- often Cloudflare settings, cache rules, security headers
Dev+SEO | Requires both developer implementation and SEO specification -- schema, redirect mapping, URL consolidation
SEO | SEO strategist -- can execute without developer dependency. Sitemap fixes, llms.txt, GSC tasks, content optimization
Content/SEO | Content writer working from SEO brief -- meta descriptions, title tags, H1 rewrites, page copy
Content+SEO | New page builds requiring both SEO keyword framework and clinical content writing
Analytics | Tag manager or analytics owner -- GTM configuration, GA4 event setup, call tracking
Marketing/PR | Marketing or communications team -- review outreach, media relations, directory submissions

[TABLE 37]
Action | Owner | Expected Outcome
URGENT: Identify May 1 CWV regression deployment | Dev Lead | Restore Good URL count. Every additional week extends damage in the 28-day rolling CWV window. Audit all deployments between April 25 and May 3.
Remove 10 broken URLs + 17 redirecting URLs from XML sitemap | SEO/Dev | Google stops processing dead ends on every crawl cycle. One-hour sitemap XML edit.
Fix CSP: add Clarity and Cloudflare domains to allowlist | Dev/Infra | Restore analytics data lost on every page load. 5-minute server config change.
Optimize logo.svg from 1,032KB to under 20KB | Dev | Remove 1MB from every page load. Re-export from source file. Immediate LCP contribution.
Defer Hotjar to GTM scroll trigger (or remove -- Clarity already running) | Analytics | Save 3,443ms CPU time per page load. GTM config change only. No code deployment.
Defer liine.com call tracking to GTM window-load trigger | Analytics | Move 343KB from critical path to post-load. 86% of script is unused on initial load.
Deploy 4 missing security headers via Cloudflare Transform Rule | Dev/Infra | Resolves 394-395 flagged URLs across X-Content-Type-Options, X-Frame-Options, Referrer-Policy, CSP coverage. Single CDN dashboard change.
Add font-display: swap to Adobe TypeKit | Dev | Remove 7,387ms TypeKit from critical path dependency. Immediate FCP improvement.
Extend cache TTL to 1 year for all static assets | Dev/Infra | All static assets currently cached for 4 hours -- repeat visitors re-download 1MB+ on every visit.
Compress home.mp4 from 11MB to under 2MB | Dev/Media | Remove largest single asset from every homepage load. H.264, 720p, CRF 28+.
Create and deploy llms.txt at synergyhealth.org/llms.txt | SEO | Establishes AI crawler priority guidance for ChatGPT, Perplexity, Claude, Google AI. 30-minute task. Zero development resources.
Verify AI crawler access in robots.txt (GPTBot, PerplexityBot, ClaudeBot, ChatGPT-User, Google-Extended) | Dev | Confirm retrieval bots are allowed. Do not block bots serving live user queries.
Fix homepage meta description | Content/SEO | Most visible page on site has no meta description. Single field in Yoast or RankMath.
Rewrite carpal tunnel page title + meta (pos 1.37, 15,605 impressions, 0.03% CTR) | Content/SEO | 300+ additional monthly visits from existing #1 ranking. 20-minute content task.
Rewrite TKA page title + meta (38,350 impressions, 0.02% CTR) | Content/SEO | Highest-impression treatment page. Title and meta rewrite unlocks clicks from existing positions.
Rewrite PRP injections page title + meta (23,557 impressions, 0.05% CTR) | Content/SEO | 23K impressions at position 6 converting at near-zero. Title and meta fix is the fastest win.
Fix duplicate title tags at archive template level | Dev/SEO | Resolves 120 pages sharing 20 title values. Single WordPress template change.
Fix duplicate meta descriptions at archive template level | Dev/SEO | Resolves 86 pages sharing archive default meta descriptions. Same template change as titles.
Fix H1 non-sequential issue at WordPress theme template level | Dev | One template edit resolves 70.3% of pages (270 instances). Heading precedes H1 in site header or promotional banner area.
Fix 14 pages missing H1 -- priority: /book-an-appointment/, /insurance-billing/, /about-us/, /recovery-guide/ | Content/Dev | Critical patient-journey pages missing H1. Includes all insurance sub-pages and booking parameter pages.
Fix 6 consent modal input labels (WCAG 2.1 AA) | Dev | ADA compliance failure on every page load for every screen reader user.
Fix 7 Leaflet map marker ARIA labels | Dev | All location map markers announce as generic button. Single JavaScript component fix.
Fix hero video -- add aria-hidden=true (decorative video) | Dev | WCAG 1.2.2 violation. Removes video from accessibility tree.
Fix /patient-center/find-a-doctor/ 404 -- update all CTAs to /providers/ | Dev | 404 in sitemap and crawl. Multiple CTAs pointing to dead end at highest appointment intent moment.
Password-protect synergy.egowebdev.com staging domain | Dev | Stops duplicate content risk and link equity leakage to non-production site.
Fix MedicalOrganization schema on homepage (wrong entity type: Organization/Person hybrid) | Dev+SEO | Corrects wrong entity type (Organization/Person hybrid → MedicalOrganization) and fixes sameAs errors. Required for all downstream schema to reference as parentOrganization with correct context.
Implement Physician schema on all 70 provider bio pages | Dev+SEO | Transforms provider pages (2.70% CTR -- best organic performer) into structured medical entities. Knowledge Panel and AI Overview citation eligibility.
Fix malformed BreadcrumbList on 70 provider bio pages | Dev | Corrects provider bio breadcrumb paths: removes insurance pages as false ancestors, establishes correct Home > Providers > [Physician Name] hierarchy.
Connect GSC Coverage report -- export and review indexation gaps | SEO | Only remaining major data gap. Identifies pages Google crawls but refuses to index.
Define 75-query AIO tracking set and run baseline audit | SEO | Establishes measurement baseline before Phase 2 content investments. Run in ChatGPT, Perplexity, and Google AI.

[TABLE 38]
Action | Owner | Expected Outcome
Consolidate TKA cluster: redirect 14 thin pages to one canonical hub | Dev+SEO | Concentrates 30,143 quarterly impressions into a single authoritative page. Target CTR improvement from 0.06% to 0.5-1.0% post-consolidation.
Publish 5 spine condition hubs: stenosis, herniated disc, sciatica, DDD, spondylolisthesis | Content+SEO | Addresses the foundational authority gap. Each hub: 50-75 word definition, Quick Answer box, FAQ schema (12+ questions), coordinated care pathway CTA, physician reviewer byline.
Fix MedicalClinic schema quality errors on all 8 location pages | Dev+SEO | Removes Hospital @type errors, repairs corrupted openingHours entries, fixes Unicode separator in location names. Strengthens local pack signals and AI Overview citation eligibility. 2-3 hour Rank Math configuration task per location.
Verify and complete MedicalCondition schema properties on 61 condition pages | Dev+SEO | MedicalCondition is deployed — confirm all pages have full property set: symptom, possibleTreatment, associatedAnatomy. Extend to any condition pages missing it. Verify no pages were missed in the Rank Math configuration.
Write meta descriptions: all 8 location pages + 15 priority provider bios | Content/SEO | 7 of 8 location pages have no meta description. 15 key physician bios missing. Immediate CTR improvement opportunity.
Build 10-15 hyper-local service pages (5-7 per location) | Content+SEO | Herniated Disc Treatment Livonia, Spine Specialist Sterling Heights, Knee Replacement Livonia, Pain Management Southfield, Podiatry Port Huron, Physical Therapy Troy. Each page: provider module, access messaging, 96% recommend rate proof, location FAQ schema.
Consolidate Southfield 9-URL variants to /locations/southfield/ | Dev/SEO | Concentrates all Southfield authority signals into a single canonical destination. Update all GBP, internal, and external links.
301 redirect /full-service-clinics/ to /locations/ equivalents | Dev | Consolidates legacy location URL traffic. /full-service-clinics/sterling-heights-2/ is #3 clicked page -- redirect must be implemented carefully to preserve 366 clicks.
301 redirect /shp-* physical therapy URLs to current equivalents | Dev | 20 legacy URLs with 11,793 quarterly impressions. Update GBP website links after redirect.
Healthcare directory citation sprint: Healthgrades, Vitals, Zocdoc, WebMD | SEO | Standardize NAP across all platforms. Complete all provider profiles. Improves local pack confidence signals and E-E-A-T.
NAP consistency audit: on-page vs GBP for all 8 locations | SEO | Any NAP discrepancy suppresses local pack rankings. Manual audit per location against GBP listing.
Implement AIO page framework on top-6 impression pages | Content+SEO | Lymphedema (34K impr), neck fracture (48K), TKA post-consolidation, PRP (23K), cervical fusion (16K), carpal tunnel (15K). These 6 pages represent 165,000+ quarterly impressions converting at under 0.2% CTR.
Add image size attributes to 203 images (template fix) | Dev | Confirmed CLS contributor. Template fix resolves majority. Specific named offenders: spine.svg, hip.svg, knee.svg, shoulder.svg, elbow.svg, foot-ankle.svg, back-neck.svg, hand-wrist.svg.
Expand location H1s to include specialty + city name | Content | Orthopedic and Spine Care in Sterling Heights, MI outperforms Sterling Heights for both local SEO and patient trust.
Add GA4 conversion tracking + call tracking attribution | Dev+Analytics | Required to measure organic consultation ROI before Month 2 reporting. GA4 form_submit on booking forms, phone_click on call-to-call numbers.
Begin CSS consolidation: reduce render-blocking from 50+ files | Dev | Primary remaining LCP fix after quick wins in Phase 1. Major development sprint -- begin scoping in Phase 1, execute in Phase 2.
Doximity profiles: submit for all physicians | Marketing | Physician professional network. Direct E-E-A-T signal for Physician schema sameAs property.
Expand Zimmer Biomet Find-a-Doctor listings for all eligible physicians | Marketing | Existing relationship. 15 links already present. Expand to all qualifying surgeons.

[TABLE 39]
Action | Owner | Expected Outcome
Implement MedicalProcedure schema on 72 treatment pages | Dev+SEO | Enables AI Overview citation for surgical and treatment procedure queries. Completes the schema suite across all major page types.
Implement FAQPage schema across all condition and procedure pages | Dev+SEO | Directly cited by ChatGPT, Perplexity, Claude, and Google AI for patient question queries. Single highest-frequency AIO citation trigger.
Launch recovery timeline content for top 5 procedures | Content | TKA, spinal fusion, hip replacement, rotator cuff repair, lumbar discectomy. HowTo schema structure. Recovery timelines are among the highest-volume AIO trigger query types in orthopedics and spine.
Build 5-7 treatment comparison pages | Content | Surgery vs PT for herniated disc, injection options for back pain, fusion vs decompression for stenosis. Decision-support format AI Overviews frequently extract. Synergy integrated model CTA on each page.
Complete CSS consolidation -- full render-blocking resolution | Dev | 50+ render-blocking CSS files to single minified stylesheet. Primary remaining LCP fix after Phase 1 script deferrals.
Rebuild CSP to nonce-based implementation (replace unsafe-inline) | Dev | Security hardening. Replaces the permissive unsafe-inline with nonces or hashes. Development sprint required.
Virtualize testimonials slider DOM (3,126 child elements) | Dev | Reduces DOM by ~3,000 elements in one component change. Direct contribution to INP and overall DOM size.
Subset Font Awesome to used icons only (save 18KB unused CSS) | Dev | 18.2KB unused CSS. Switch above-fold icons to inline SVG for fastest critical path.
Implement review velocity program with HIPAA-safe protocol | Marketing | Post-visit outreach at 3-5 days and 4-6 weeks post-procedure. Target: steady monthly growth per location. BirdEye, Podium, or similar. HIPAA-safe response SOP required before launch.
Rewrite priority condition and treatment pages to 7th grade reading level | Content | Prioritize by impression volume: lymphedema management, neck fracture, TKA post-consolidation, PRP, cervical fusion. Each rewrite also restructures to answer-first format.
Build billing and insurance clarity content section | Content | Does insurance cover spine surgery, How do I know what my visit will cost, How to use workers compensation at Synergy. High-intent queries with no current Synergy content. Reduces pre-appointment friction.
Audit 100 canonicalized pages for correctness | SEO | Confirm each of the 100 canonicalized pages is intentionally canonicalized. Remove any pages incorrectly excluded from Google's index.
Fix pagination: 24 URLs not in anchor tags | Dev | Pagination URLs in rel=next/prev but not in standard a href links. Reduces crawlability.
Complete URL underscore migration: 72 URLs with 301 redirects | Dev | 8.92% of internal URLs using underscores. Migrate to hyphenated equivalents.
Begin Michigan hospital system link outreach | Marketing/PR | Henry Ford Health, Corewell Health, McLaren. Physician affiliation pages and care pathway documents are the natural link acquisition vehicles.
Begin insurance provider directory inclusions | Marketing | BCBS Michigan, Priority Health, Blue Care Network. Direct patient decision-making touchpoint with high domain authority.
Begin AAOS and Michigan Orthopedic Society member directory submissions | Marketing | Medical association member directories. Second priority link acquisition category after hospital system links.
Re-run Screaming Frog with PSI API connected (per-page performance scores) | SEO | Fills the remaining interior page performance gap. Provides per-page LCP, CLS, and FID data for all 384 pages.
Quarterly AIO tracking report + executive review | SEO+Leadership | Connect program to patient acquisition outcomes: topical authority trend, local pack gains by location, consultation volume growth from organic channels.

[TABLE 40]
Issue | Source | Priority | Effort | Owner
Identify May 1 CWV regression deployment (URGENT) | Tech P7 | HIGH | LOW | Dev Lead
Remove 10 broken + 17 redirecting URLs from sitemap | Tech P1 | HIGH | LOW | SEO/Dev
Fix CSP: add Clarity + Cloudflare domains (5-min fix) | Tech P9 | HIGH | LOW | Dev/Infra
Optimize logo.svg from 1,032KB to under 20KB | Tech P7 | HIGH | LOW | Dev
Defer Hotjar to GTM scroll trigger (or remove) | Tech P7 | HIGH | LOW | Analytics
Defer liine.com to GTM window-load trigger | Tech P7 | HIGH | LOW | Analytics
Deploy 4 security headers via Cloudflare rule | Tech P9 | HIGH | LOW | Dev/Infra
Create and deploy llms.txt | Strat P11 | HIGH | LOW | SEO
Verify AI crawler access in robots.txt | Strat P11 | HIGH | LOW | Dev
Fix homepage meta description | Tech P5 | HIGH | LOW | Content/SEO
Rewrite carpal tunnel page title + meta (pos 1.37, 0.03% CTR) | Tech P5/P12 | HIGH | LOW | Content/SEO
Fix /patient-center/find-a-doctor/ 404 -- update all CTAs | Tech P1 | HIGH | LOW | Dev
Password-protect staging domain synergy.egowebdev.com | Tech P13 | HIGH | LOW | Dev
Implement MedicalOrganization schema (homepage) | Tech P6 | HIGH | MEDIUM | Dev+SEO
Implement Physician schema (70 provider bio pages) | Tech P6 | HIGH | MEDIUM | Dev+SEO
Fix malformed BreadcrumbList on 70 provider bio pages | Tech P6 | HIGH | MEDIUM | Dev
Fix duplicate title tags at archive template level | Tech P5 | HIGH | MEDIUM | Dev/SEO
Fix duplicate meta descriptions at archive template level | Tech P5 | HIGH | MEDIUM | Dev/SEO
Write meta descriptions: 8 location pages + homepage | Tech P5/P10 | HIGH | MEDIUM | Content/SEO
Fix 14 pages missing H1 (priority: conversion + insurance pages) | Tech P5 | HIGH | MEDIUM | Content/Dev
Fix H1 non-sequential issue at WordPress theme template | Tech P5 | HIGH | MEDIUM | Dev
Consolidate Southfield 9-URL variants | Tech P2/P10 | HIGH | MEDIUM | Dev/SEO
301 redirect /full-service-clinics/ to /locations/ equivalents | Tech P2/P10 | HIGH | MEDIUM | Dev
Schema: MedicalClinic on all 8 location pages | Tech P6/P10 | HIGH | MEDIUM | Dev+SEO
NAP audit: on-page vs GBP for all 8 locations | Tech P10 | HIGH | MEDIUM | SEO
CSS consolidation: 50+ render-blocking files | Tech P7 | HIGH | HIGH | Dev
Compress home.mp4 from 11MB to under 2MB | Tech P7 | HIGH | MEDIUM | Dev/Media
Rewrite TKA + PRP page titles and meta | Tech P5/P12 | MEDIUM | LOW | Content/SEO
Consolidate TKA cluster (14 pages to 1 canonical hub) | Strat S1 | MEDIUM | MEDIUM | Dev+SEO
Publish 5 spine condition hubs | Strat S1 | MEDIUM | HIGH | Content+SEO
Schema: MedicalCondition on 61 condition pages | Tech P6 | MEDIUM | MEDIUM | Dev+SEO
Build 10-15 hyper-local service pages | Strat S2 | MEDIUM | HIGH | Content+SEO
Write meta descriptions: 15 priority provider bios + remaining pages | Tech P5 | MEDIUM | HIGH | Content/SEO
Add image size attributes to 203 images (template fix) | Tech P5/P7 | MEDIUM | LOW | Dev
Add alt text to 11 images | Tech P5 | MEDIUM | LOW | Content
Implement AIO page framework on top-6 impression pages | Strat S6 | MEDIUM | HIGH | Content+SEO
Expand location H1s to specialty + city format | Tech P10 | MEDIUM | LOW | Content
Fix 6 consent modal input labels (WCAG AA) | Tech P8 | MEDIUM | LOW | Dev
Fix 7 Leaflet map marker ARIA labels | Tech P8 | MEDIUM | LOW | Dev
Fix hero video aria-hidden | Tech P8 | MEDIUM | LOW | Dev
Healthcare directory citation sprint (Healthgrades, Vitals, Zocdoc, WebMD) | Strat S2 | MEDIUM | MEDIUM | SEO
GA4 conversion tracking + call tracking attribution | Strat S7 | MEDIUM | MEDIUM | Dev+Analytics
Schema: MedicalProcedure on 72 treatment pages | Tech P6 | MEDIUM | MEDIUM | Dev+SEO
Schema: FAQPage on condition and treatment pages | Tech P6 | MEDIUM | MEDIUM | Dev+SEO
Rebuild CSP to nonce-based (replace unsafe-inline) | Tech P9 | MEDIUM | HIGH | Dev
Rewrite 309 difficult-readability pages (7th grade reading level) | Strat S6 | MEDIUM | HIGH | Content
301 redirect /shp-* physical therapy legacy URLs | Tech P2 | MEDIUM | MEDIUM | Dev
Audit 100 canonicalized pages for correctness | Tech P3 | MEDIUM | MEDIUM | SEO
Implement review velocity program (HIPAA-safe protocol) | Strat S4 | MEDIUM | MEDIUM | Marketing
Review platform diversification: Healthgrades, Vitals, Doximity profiles | Strat S4 | MEDIUM | MEDIUM | Marketing
Launch recovery timeline content for top 5 procedures | Strat S6 | LOW | HIGH | Content
Build 5-7 treatment comparison pages | Strat S6 | LOW | HIGH | Content
Virtualize testimonials slider DOM (3,126 elements) | Tech P7 | LOW | MEDIUM | Dev
Subset Font Awesome to used icons only | Tech P7 | LOW | MEDIUM | Dev
Fix pagination: 24 URLs not in anchor tags | Tech P3 | LOW | LOW | Dev
URL underscore migration: 72 URLs with 301 redirects | Tech P2 | LOW | HIGH | Dev
Begin Michigan hospital system link outreach | Tech P13 | LOW | HIGH | Marketing/PR
Begin insurance provider directory inclusions | Tech P13 | LOW | MEDIUM | Marketing
AAOS and Michigan Orthopedic Society member directory submissions | Tech P13 | LOW | MEDIUM | Marketing
Build billing and insurance clarity content section | Strat S4 | LOW | HIGH | Content
Add COOP header to HTML responses | Tech P9 | LOW | LOW | Dev/Infra
Re-run Screaming Frog with PSI API connected (per-page scores) | Tech P7 | LOW | LOW | SEO
Publish physician reviewer bylines on all clinical content | Strat S5 | LOW | MEDIUM | Content
Implement content freshness governance (Last reviewed dates) | Strat S6 | LOW | MEDIUM | Content

[TABLE 41]
Metric | Baseline | 30-Day Target | 90-Day Target
CWV Good URLs (mobile) | 0 (regression since May 1) | 50+ (regression fixed + image dimensions resolved) | 100+ (CSS consolidation + schema signals compounding)
Overall organic CTR | 1.15% | 1.3-1.5% (carpal tunnel + TKA title/meta fixes) | 1.8-2.2% (rich results unlocked by schema)
Branded click share | 80% | 78% (carpal tunnel + TKA fixes add non-branded) | 65-70% (spine hubs + local pages driving non-branded)
TKA cluster CTR | 0.06% (19 clicks / 30,143 impr) | 0.5-1.0% (consolidation + title fix) | 2-3% (canonical hub + schema + FAQ schema)
Local near me visibility | Moderate (GBP working, organic low) | Improved (schema + NAP consistency) | 45-50% on priority near me + city queries
Rich result types in GSC | 1 type (Translated Results only) | Breadcrumbs + early FAQ results | FAQ, physician, breadcrumb rich results across clinical pages
AIO citation rate (75 tracked queries) | Near zero (baseline not yet established) | Baseline established + first citations | 10-15% citation rate for tracked query set
Organic consultation requests | Unknown (no conversion tracking) | Attribution infrastructure live | +25-35% vs pre-program baseline
Topical authority score | 31.8 | 32-34 (schema signals improving) | 40-45 (spine hubs + local content published)

[TABLE 42]
Role | Time Commitment
SEO and AIO strategy lead | 8-12 hours per week. Governs schema implementation, content framework, tracking set, and monthly reporting.
Clinical content strategist / editor | 10-15 hours per week. Writes and edits AIO-framework condition hubs, recovery content, comparison pages. Requires healthcare content experience.
Medical reviewer (MD or DO byline) | 2-5 hours per week, scaling with publishing volume. Provides physician authorship bylines and accuracy review for YMYL quality compliance.
Web developer (schema + templates) | 20-40 hours total in Phase 1, then 5-10 hours per month. Schema, CSS consolidation, sitemap fixes, redirect management.
Local and reputation manager | 4-6 hours per week during citation sprint and review velocity ramp. Manages Healthgrades, Vitals, Zocdoc, GBP profiles, and review outreach program.

[TABLE 43]
Tool Category | Estimated Monthly Cost
Local tracking + citation tools (BrightLocal or Local Falcon) | $100-300 per month
Rank tracking and topical authority (Semrush or Ahrefs) | $200-500 per month
AIO measurement (Profound) | Pricing per agreement
Call tracking (CallRail or similar) | $100-300 per month depending on lines and locations
Reputation management platform (BirdEye or Podium) | $300-800 per month depending on location and provider count
Total estimated tool range | $700-2,200 per month (excluding Profound)

[TABLE 44]
@mendelsonortho Channel Handle (Pre-Rebrand Brand) | LEGACY Channel Branding vs Synergy Health | THIN Channel Description Quality | 0 VideoObject Schema on Site

[TABLE 45]
Finding | Priority | Current State | Recommended Action
Channel handle @mendelsonortho reflects pre-rebrand brand | HIGH | Channel handle is @mendelsonortho. YouTube channel name shows as Synergy Health Partners | Mendelson Orthopedics -- a mixed identity that confuses both patients and search engines. | Update YouTube channel name to Synergy Health and channel handle to @synergyhealth or @synergyhealth.ortho. This is a channel settings change in YouTube Studio. No videos need to be re-uploaded or re-titled.
Channel description is thin with no keywords, location, or CTA | HIGH | Current description: Learn more about our one-stop-medical-shop! No specialty mentions, no Michigan location, no physician names, no service line keywords, no appointment CTA, no website link to synergyhealth.org. | Rewrite to 200-250 words. Include: organization description, specialty list (orthopedics, spine, pain management, physical therapy, podiatry), Michigan service area, same-week access messaging, and a clear link to synergyhealth.org. Keyword-rich channel descriptions directly influence YouTube search indexing.
About section link likely points to mendelsonortho.com, not synergyhealth.org | HIGH | Based on channel creation date and legacy branding, the primary website link in the About section is almost certainly the legacy domain. GSC backlink data confirms 0 YouTube backlinks to synergyhealth.org. | Verify and update the About section website link to https://synergyhealth.org. This is a direct patient referral pathway and E-E-A-T entity link. Also update the custom URL if it still uses the legacy mendelsonortho handle.
Legacy URL youtube.com/user/mendelsonortho still active | MEDIUM | The channel predates YouTube handle system -- it still has a legacy /user/ URL in addition to the @handle. This creates a fragmented URL presence. | The handle system automatically redirects -- no action required for the legacy URL. However, all Synergy Health website embeds, GBP links, and marketing materials should use the @mendelsonortho or updated @synergyhealth handle URL rather than the legacy /user/ URL.
Channel keyword tags cover relevant territory but miss current brand | MEDIUM | Existing keywords include: orthopedic surgery, michigan, detroit, warren, livonia, back pain, spine surgery, knee replacement, hip replacement, sports medicine, pain management, physical therapy. Missing: synergy health, synergyhealth, mendelson kornblum, southeast michigan, same week appointment, sciatica, herniated disc, spinal stenosis. | Add Synergy Health, synergyhealth.org, Southeast Michigan, and the five foundational spine condition terms to channel keywords. Also add: board certified orthopedic surgeon, spine specialist michigan, total knee replacement michigan.
No YouTube channel verification or Google Knowledge Panel connection confirmed | MEDIUM | An unverified channel cannot claim a Knowledge Panel or be connected to the Google Business Profile entity. | Verify the YouTube channel via Google Search Console property verification. Connect to the Synergy Health Google Business Profiles where YouTube channel linkage is supported.

[TABLE 46]
Finding | Priority | Current State | Recommended Action
Full video inventory not accessible without YouTube Studio | NEEDS INPUT | YouTube blocked automated crawl access. Total video count, publish dates, view counts, and current activity level are unknown. | Grant YouTube Studio access or export the Videos tab as a CSV. Alternatively, provide a manual list of video titles and publish dates. This is the single input required to complete Dimensions 2-6 of this audit.
Channel predates 2022 YouTube handle system -- legacy account | MEDIUM | The /user/mendelsonortho URL structure confirms the channel was created before YouTube's 2022 migration to handles. This suggests a library of older content that may carry the legacy Mendelson Kornblum or Mendelson Orthopedics branding in titles and descriptions. | When inventory is available, audit all video titles and descriptions for legacy brand names. Titles can be updated without re-uploading video files. Update Mendelson Orthopedics references to Synergy Health in titles and descriptions for all high-performing videos.
Publishing cadence unknown -- channel may be dormant | NEEDS INPUT | No recent upload activity confirmed from public channel inspection. A dormant channel sends a negative freshness signal to YouTube's algorithm and Google Video Search. | Confirm last upload date via YouTube Studio. If channel has been dormant for 6+ months, a structured re-engagement plan (minimum 1-2 videos per month) is recommended to restore algorithmic freshness signals.
Playlist organization unknown | NEEDS INPUT | Whether videos are organized into clinical topic playlists is not visible without inventory access. | When inventory is available, create or verify playlists: Spine Conditions, Orthopedic Procedures, Provider Introductions, Patient Stories, Physical Therapy and Recovery, Practice Overview. Playlists improve watch time, session duration, and topical clustering signals for YouTube SEO.

[TABLE 47]
Topic | Gap Context and Video Priority
Spinal stenosis | Zero GSC organic presence. Zero video confirmed. Front-door spine query. Highest priority new video topic.
Herniated disc treatment | Minimal GSC presence. Highest-volume spine condition query category. Video + written content hub required together.
Sciatica and radiculopathy | Minimal GSC presence. Common presenting symptom. Patient-facing explainer video high-value.
Degenerative disc disease | Zero page-one GSC presence. Chronic condition with long patient relationship value.
Spondylolisthesis | Zero GSC page-one presence. Specialty spine condition. Physician-attributed video strengthens E-E-A-T.
Total Knee Arthroplasty (TKA / Knee Replacement) | 38,350 GSC impressions, 0.02% CTR. Almost certainly has existing video given procedure volume. Embed on canonical TKA hub with VideoObject schema.
Carpal tunnel syndrome | Position 1.37, 15,605 impressions, 4 clicks. A procedure video embedded on this page could 3x organic value. Highest urgency embed opportunity.
Recovery timelines (TKA, spinal fusion, hip replacement) | Zero recovery timeline content on site. Recovery queries are among highest-volume AIO trigger query types. Video format is the most effective delivery format for recovery guidance.
Treatment comparisons (surgery vs PT, injection options) | Zero comparison content on site. AI Overviews extract decision-support content. Video format supports this well if structured as Q&A.
Provider introductions -- key physicians | Provider pages drive 2.70% CTR -- best organic performance. Physician video on provider bio page strengthens E-E-A-T and conversion rate.

[TABLE 48]
Finding | Priority | Current State | Recommended Action
Five foundational spine conditions have no confirmed video coverage | HIGH | Spinal stenosis, herniated disc, sciatica, DDD, spondylolisthesis -- zero GSC organic presence. Video content for these conditions is likely absent because written content is absent. | Produce one 3-5 minute physician-attributed explainer video per spine condition to accompany each written condition hub (Phase 2 roadmap item). These videos become embed candidates with VideoObject schema and transcript-based AIO citation sources.
TKA content likely exists but needs embed + schema treatment | HIGH | With 15 competing written pages on TKA, video content may exist but is almost certainly not embedded on the canonical hub page or marked up with VideoObject schema. | When inventory is confirmed, identify the highest-quality TKA video on the channel. Embed it on the canonical TKA hub. Implement VideoObject schema with name, description, thumbnailUrl, uploadDate, duration, and embedUrl properties.
Recovery timeline video content is the highest AIO trigger format | HIGH | Zero recovery timeline pages confirmed on synergyhealth.org. Recovery queries (knee replacement recovery week by week, spinal fusion recovery timeline) are extremely high-volume AIO trigger query types. | Produce recovery timeline videos as HowTo-structured content. Format: week-by-week milestone guidance with physician narration. These videos, when embedded with HowTo schema and transcripts, are directly extractable by AI Overviews for patient recovery queries.
Provider introduction videos for top physicians can anchor bio pages | MEDIUM | Provider pages at 2.70% CTR are the strongest organic performance on the site. A physician introduction video on each bio page increases time-on-page, trust conversion, and VideoObject schema E-E-A-T signal. | Confirm which physicians have existing introduction or Q&A videos. Embed on bio pages with VideoObject schema including the physician's name, specialty, and affiliation in schema properties.

[TABLE 49]
Finding | Priority | Current State | Recommended Action
Video titles likely use legacy brand name or generic clinical terminology | HIGH | Channel was created and published under Mendelson Orthopedics. Older video titles almost certainly reference Mendelson Orthopedics rather than Synergy Health. | When inventory is available: audit all video titles. Update any that reference Mendelson Orthopedics or Mendelson Kornblum to Synergy Health. YouTube allows title updates without re-uploading video. Also optimize titles for patient-language search queries: Knee Replacement Surgery Michigan -- Synergy Health outperforms Total Knee Arthroplasty Procedure.
Video descriptions likely thin or absent -- same pattern as website meta descriptions | HIGH | The website has 85 pages with missing meta descriptions. YouTube video descriptions from the same organizational era are almost certainly thin or absent. | For every video: write a 200-300 word description. Include: first 100 characters as a standalone sentence summarizing the video (visible before See more cutoff), specialty and condition keywords, physician name and credentials if appearing on camera, Synergy Health name and location, and a clear CTA: Schedule your same-week appointment at synergyhealth.org or call 855-750-5757.
CTAs in video descriptions not linking to synergyhealth.org | HIGH | Zero YouTube backlinks confirmed in GSC backlink export for synergyhealth.org. Confirms that video descriptions are not driving referral traffic to the canonical domain. | Add a clickable synergyhealth.org link in the first 3 lines of every video description. For condition-specific videos, link to the relevant condition page (e.g., synergyhealth.org/conditions/carpal-tunnel-syndrome/). Use UTM parameters: utm_source=youtube&utm_medium=video&utm_campaign=organic.
End screens and cards not confirmed as active | MEDIUM | Without inventory access, whether end screens and cards are configured cannot be confirmed. A channel without end screens misses the highest-converting video format for appointment intent. | Verify end screen configuration in YouTube Studio. Every video should have: end screen with Subscribe button, link to most relevant condition or procedure page on synergyhealth.org, and link to one related video. Cards should be added at points where a viewer might search for related information.
Auto-generated captions -- accuracy on medical terminology not confirmed | MEDIUM | YouTube auto-generates captions for all videos. Medical terminology (arthroplasty, discectomy, spondylolisthesis, meniscus) has very high auto-caption error rates. | Review auto-captions on all videos. Upload corrected SRT files for any video with medical terminology errors. Accurate captions improve YouTube search indexing, AIO transcript extraction, and ADA compliance.

[TABLE 50]
Finding | Priority | Current State | Recommended Action
Zero VideoObject schema on synergyhealth.org -- confirmed by Screaming Frog | HIGH | Schema partially deployed via Rank Math PRO — critical gaps and quality errors confirmed. Any YouTube video embedded on the site has no VideoObject schema marking it up for Google Video Search or AI extraction. | Implement VideoObject JSON-LD on every page that embeds a YouTube video. Required properties: @type VideoObject, name, description (same as the written content summary), thumbnailUrl (YouTube thumbnail URL), uploadDate, duration (ISO 8601 format: PT4M30S for 4 minutes 30 seconds), embedUrl (YouTube embed URL), contentUrl (YouTube watch URL). Optional but valuable: transcript text.
No confirmed YouTube embeds on synergyhealth.org -- embed audit needed | HIGH | GSC backlink data shows zero YouTube links to synergyhealth.org. Screaming Frog crawl did not surface YouTube iframes in the content data. Videos may exist but may not be embedded on the site. | Audit the site for YouTube iframes. Search the Screaming Frog links export for youtube.com and youtu.be. Confirm which pages (if any) embed channel videos. If no embeds exist, identify the top 5 videos from the channel that should be embedded immediately: most-viewed provider introduction, most-viewed condition explainer, most-viewed procedure explainer.
Zero backlinks from youtube.com to synergyhealth.org in GSC export | HIGH | GSC backlink export (734 total linking pages, 130 domains) contains zero YouTube links. This means either video descriptions have no synergyhealth.org links or those links do not pass as crawlable anchors. | Add a clickable synergyhealth.org link in the first 3 lines of every video description. YouTube nofollow attributes mean these do not pass PageRank, but they are confirmed as referral traffic sources and entity association signals.
GBP listing not confirmed as linked to the YouTube channel | MEDIUM | Google Business Profile supports a YouTube channel link in the website/social section. If GBP and YouTube channel are not linked, the entity association between Synergy Health and the channel is weaker. | Add the YouTube channel URL to all 8 GBP location listings under the social media / website links section. This establishes a verified connection between the local business entity and the video content.
YouTube Shorts not confirmed -- Shorts receive separate AIO indexing treatment | MEDIUM | Shorts (vertical video under 60 seconds) are indexed separately by Google and are increasingly surfaced in AI Overview responses for quick health queries. Whether the channel publishes Shorts is unknown. | When inventory is reviewed, confirm if Shorts exist. If not, a Shorts program (1 per week, covering quick answers to patient questions) is low-effort and high-AIO-visibility: What is spinal stenosis? How long is knee replacement recovery? When do I need to see a spine doctor?

[TABLE 51]
<script type="application/ld+json"> {   "@context": "https://schema.org",   "@type": "VideoObject",   "name": "[Video Title -- patient-language, keyword-rich]",   "description": "[200-word description matching video description on YouTube]",   "thumbnailUrl": "https://img.youtube.com/vi/[VIDEO_ID]/maxresdefault.jpg",   "uploadDate": "[YYYY-MM-DD]",   "duration": "PT[M]M[S]S",   "embedUrl": "https://www.youtube.com/embed/[VIDEO_ID]",   "contentUrl": "https://www.youtube.com/watch?v=[VIDEO_ID]",   "author": {     "@type": "Person",     "name": "[Physician Name, MD]",     "url": "https://synergyhealth.org/providers/[physician-slug]/"   },   "publisher": {     "@type": "Organization",     "name": "Synergy Health",     "url": "https://synergyhealth.org"   } } </script>

[TABLE 52]
Finding | Priority | Current State | Recommended Action
No video transcripts accessible on synergyhealth.org -- primary AIO extraction mechanism absent | HIGH | AI systems extract video content via transcripts. Without published transcripts (either in the video description, on the embedding page, or as a dedicated transcript page), video content cannot be cited by AI Overviews. | For every video embedded on synergyhealth.org: publish the transcript on the page. Format: a collapsible Video Transcript section below the embed. This serves three functions simultaneously: AI extraction source, ADA accessibility compliance, and additional keyword content for Google to index.
No recovery timeline or decision-support video format confirmed | HIGH | The five highest-AIO-trigger video formats in healthcare are: recovery timelines, treatment comparisons, when to see a doctor decision guides, FAQ Q&A with physician, and condition explainers. None confirmed on the channel. | Produce video content in these formats and structure them for AIO extraction: open with a direct answer (What is spinal stenosis? It is a narrowing of the spinal canal...), include numbered steps or milestones for recovery content, close with a clear next step CTA. These formats are directly extractable by AI Overviews.
YouTube auto-captions on medical content are likely inaccurate -- limits AI extraction quality | MEDIUM | Auto-caption error rates for medical terminology are high. Inaccurate transcripts produce inaccurate AI extractions and worse YouTube search indexing. | Upload corrected SRT captions for all videos. The corrected transcript is the foundation for both ADA compliance and accurate AI extraction.
No FAQ-format video content confirmed -- Q&A format is highest AIO trigger | MEDIUM | FAQ-formatted content is the highest-frequency AIO citation trigger in healthcare. Video Q&A (physician answers 8-10 patient questions on camera) maps directly to FAQPage schema and is extractable by AI systems. | Produce physician Q&A videos for the top 5 condition pages. Format: 8-10 patient questions, physician answers on camera, each answer 30-60 seconds. The transcript becomes FAQPage schema content. Upload the video, embed it on the condition page, implement FAQPage schema with the Q&A content, and add VideoObject schema.

[TABLE 53]
Priority | Recommended Format and Rationale
1. Spine condition explainers (5 videos) | One per foundational spine condition: stenosis, herniated disc, sciatica, DDD, spondylolisthesis. These are the five confirmed GSC content gaps. 3-5 minutes, physician on camera, transcript published.
2. Recovery timeline videos (3-5 videos) | TKA recovery week by week, spinal fusion recovery timeline, hip replacement what to expect. HowTo schema structure. Highest-volume AIO trigger format in orthopedics.
3. Treatment comparison videos (3 videos) | Surgery vs physical therapy for herniated disc. Injection options for back pain explained. Spinal fusion vs decompression: which is right for me. Decision-support format AI Overviews extract.
4. Physician Q&A videos (5+ videos) | One per high-traffic provider: Jeffrey Mendelson MD (shoulder, general ortho), Stephen Mendelson MD (hip, knee), Preetinder Bhullar MD (knee replacement), Benjamin Mayo MD (spine), Scott McCarty MD (sports medicine). Embed on bio pages with VideoObject schema.
5. YouTube Shorts -- quick answers (ongoing) | What is spinal stenosis? (60 seconds), How long is knee replacement recovery? (60 seconds), When should I see a spine doctor? (60 seconds). Low production cost, high AIO discovery, feeds long-form video watch sessions.

[TABLE 54]
Finding | Priority | Current State | Recommended Action
Rebrand YouTube channel: name, description, handle, About section link | HIGH | Channel currently builds authority for Mendelson Orthopedics brand. Channel name shows as Synergy Health Partners | Mendelson Orthopedics in search results. | Update channel name to Synergy Health in YouTube Studio settings. Update channel description to 200-250 words with keyword coverage, service list, Michigan location, and synergyhealth.org CTA. Update About section website link to https://synergyhealth.org. Evaluate handle change from @mendelsonortho to @synergyhealth.
Audit all existing video descriptions for missing synergyhealth.org links | HIGH | Zero YouTube backlinks to synergyhealth.org confirmed in GSC export. This is confirmed evidence that existing video descriptions do not contain active links to the canonical domain. | For every existing video: add synergyhealth.org link in the first 3 lines of the description with UTM parameters (utm_source=youtube&utm_medium=video&utm_campaign=[condition-name]). Link to the most relevant condition or service page for each video.
Add YouTube channel URL to all 8 GBP listings | HIGH | GBP-to-YouTube entity linkage not confirmed. This is a direct entity association signal for Google's Knowledge Graph. | Add the YouTube channel URL in the social/website links section of all 8 GBP location listings. After channel rebrand is complete, update all GBP links to the new handle URL.

[TABLE 55]
Finding | Priority | Current State | Recommended Action
Audit full video inventory -- categorize, prioritize, and assign optimization tasks | HIGH | Full inventory unknown without YouTube Studio access. Cannot complete Dimensions 2-4 without this data. | Export video list from YouTube Studio (Content > Videos). Categorize by content type. Identify top 10 videos by view count. Assign title, description, and CTA optimization tasks to each.
Update video titles: replace legacy brand references with Synergy Health | HIGH | Older video titles almost certainly reference Mendelson Orthopedics or Mendelson Kornblum. Legacy brand names in titles build authority for the wrong entity. | For every video title containing Mendelson Orthopedics, Mendelson Kornblum, or MKO: update to Synergy Health. Also optimize title structure: [Condition/Procedure] -- [Key Benefit] -- Synergy Health Michigan.
Identify top embed candidates and embed on synergyhealth.org with VideoObject schema | HIGH | Zero confirmed embeds on synergyhealth.org. Video content is entirely disconnected from the site despite shared clinical subject matter. | Identify top 5-10 videos. Embed each on the most relevant condition, treatment, or provider bio page. Implement VideoObject schema on each embedding page immediately after embed.
Upload corrected SRT captions for top 20 videos | MEDIUM | Auto-caption error rates on medical terminology are high. Inaccurate transcripts reduce YouTube search indexing quality and AI extraction accuracy. | Export auto-captions from YouTube Studio. Correct medical terminology errors. Re-upload as SRT files. Priority: any video where a spine condition, surgical procedure, or physician credential is mentioned.

[TABLE 56]
Video Type | Format, Placement, and Schema Strategy
5 spine condition explainer videos | One per foundational condition gap (stenosis, herniated disc, sciatica, DDD, spondylolisthesis). 3-5 minutes. Physician on camera. Transcript published on corresponding condition hub page. VideoObject + FAQPage schema on embedding page.
3 recovery timeline videos | TKA, spinal fusion, hip replacement. Week-by-week milestones. HowTo schema structure. Embed on procedure pages. These are the single highest-AIO-trigger video formats in orthopedics.
3 treatment comparison videos | Surgery vs PT for herniated disc, injection options for back pain, fusion vs decompression for stenosis. Decision-support format. Embed on treatment comparison pages built in Phase 3 of the integrated roadmap.
5 physician Q&A videos | Jeffrey Mendelson MD, Stephen Mendelson MD, Preetinder Bhullar MD, Benjamin Mayo MD, Scott McCarty MD. 8-10 questions per physician, 4-6 minutes total. Embed on provider bio pages. VideoObject + Physician schema on embedding page.
YouTube Shorts program -- 4 per month ongoing | Quick answers to the most-searched patient questions. What is spinal stenosis (60s), How long is TKA recovery (60s), When do I need spine surgery (60s), What is same-week access at Synergy (60s). Low production cost, high AIO visibility.
Channel trailer -- 90-second Synergy Health overview | Post-rebrand channel introduction. Physician voiceover, facility footage, same-week access messaging. Pinned to channel homepage. Sets brand tone and entity context for all subsequent videos.