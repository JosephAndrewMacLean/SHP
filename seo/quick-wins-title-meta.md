# Title/Meta Quick Wins — Wave 1 (drafted Jul 21, 2026)

**What this is:** implementation-ready title tag + meta description rewrites for the pages the
16-month GSC data says are wasting rankings (`gsc-analysis-2026-07.md`). This is Paul's point in
the Jul 21 meeting made concrete: *"it doesn't even need to be that crazy — change the title,
change the meta description."*

**Status: DRAFT PENDING HUMAN REVIEW.** Copy touching clinical claims, service availability,
provider counts, or on-site amenities must be verified before entering Rank Math (marked
⚠️ verify). Nothing here is cleared to publish as-is.

## Rules for this wave (so the measurement is clean)

1. **Titles/metas ONLY. No content, H1, or URL changes in this wave** — isolate the variable.
2. Titles ≤ ~60 characters (truncation); metas ~140–155. Front-load the term the page ranks for.
3. One location signal where intent is local; none where it's national/informational.
4. No "best/#1/top-rated," no outcome promises, nothing that reads as a guarantee (FTC).
5. Implement in one batch, log the date in `seo/change-log.md`, annotate in GSC, read CTR at
   2 and 4 weeks against the same pages in the next export.
6. Google rewrites titles it dislikes. If SERP shows a different title after 2 weeks, iterate —
   don't stack more changes on top.
7. Expectation tags: **[Local]** commercial-local (CTR should move most) · **[Decision]**
   treatment-research (should move) · **[Info]** informational (AI Overviews absorb clicks —
   partial recovery only) · **[Brand-bridge]** rebrand navigation.

> **Jul 21 PM addendum (AI-features data):** Wave 1 stands as written — titles are per-URL,
> cheap, and reversible. But consolidation targets changed (cluster map **§4a**: primaries flip
> to `/conditions/` + `/treatment/`), so do **not** extend this wave to a duplicate URL of any
> row here — one optimized URL per topic until its consolidation ships. Row 22 was retargeted
> to the new-structure Dupuytren's URL accordingly.

---

## A. Spine (priority per the 80%-to-spine mandate)

**1. `/specialties/spine-back-and-neck/anterior-cervical-discectomy-fusion/`** — 14.6K impr,
pos 7.2, 0.36% CTR; query "acdf" 21K impr @ **pos 3.0, 0.02% CTR**. [Decision]
- Title: `ACDF Surgery: Procedure, Recovery & Risks | Synergy Health`
- Meta: `What ACDF (anterior cervical discectomy and fusion) treats, how the surgery works, and week-by-week recovery — reviewed by Metro Detroit spine surgeons.` ⚠️ verify a named reviewer is actually on the page before claiming "reviewed."

**2. `/specialties/spine-back-and-neck/cervical-fusion/`** — 80.4K impr, pos 9.0, 0.18% CTR. [Decision]
- Title: `Cervical Fusion Surgery: What to Expect | Synergy Health`
- Meta: `How neck (cervical) fusion works, who it helps, the recovery timeline, and questions to ask your surgeon. Spine care across Metro Detroit.`

**3. `/specialties/spine-back-and-neck/lumbar-laminectomy/`** — 87.5K impr, pos 28.6, 0.39% CTR
(also the consolidation primary — cluster map §4). [Decision]
- Title: `Lumbar Laminectomy: Procedure & Recovery | Synergy Health`
- Meta: `What a lumbar laminectomy involves, how long surgery takes, incision size, and realistic recovery week by week — from Metro Detroit spine specialists.`

**4. `/treatment/microdiscectomy/`** — 3.9K impr, **pos 8.3, 0.00% CTR**. Interim fix; page
merges into the cluster primary later. [Decision]
- Title: `Microdiscectomy: Herniated Disc Surgery & Recovery | Synergy`
- Meta: `How microdiscectomy relieves herniated disc pain, what recovery looks like, and when it's recommended. Minimally invasive spine care in Metro Detroit.`

**5. `/conditions/neck-fracture-broken-neck/`** — 69.3K impr, pos 7.0, 0.26% CTR. [Info — trauma;
page must keep a clear "call 911 / ER now" banner]
- Title: `Broken Neck: Symptoms, Types & Treatment | Synergy Health`
- Meta: `How to recognize a possible neck fracture, when to call 911, and how spine specialists treat and monitor healing. Reviewed by our spine team.` ⚠️ reviewer

**6. `/conditions/back-fracture-break/`** — 17.2K impr, pos 8.7, 0.14% CTR. [Info — trauma banner]
- Title: `Back (Vertebral) Fracture: Symptoms & Treatment | Synergy`
- Meta: `Signs of a spinal compression fracture, when it's an emergency, and treatment options from bracing to kyphoplasty. Metro Detroit spine care.`

**7. `/conditions-we-treat/spine-neck-back-conditions/spondylolisthesis/`** — 2.3K impr,
**pos 6.0, 0.09% CTR** — cheapest spine win on the list. [Decision]
- Title: `Spondylolisthesis: Symptoms, Grades & Treatment | Synergy`
- Meta: `What spondylolisthesis is, how grades differ, symptoms to watch for, and treatment from physical therapy to surgery — Metro Detroit spine specialists.`

**8. `/specialties/spine-back-and-neck/`** (pillar — full rebuild is Wk 2–4; title now) — 66.5K
impr, pos 24.7, 0.19% CTR. [Local]
- Title: `Spine, Back & Neck Care in Metro Detroit | Synergy Health`
- Meta: `Complete spine care under one roof — spine surgeons plus interventional pain physicians, PT, and imaging. Same-week appointments at Metro Detroit locations.` ⚠️ verify same-week promise holds for spine scheduling before publish (top sentiment risk).

**9. `/specialties/spine-back-and-neck/thoracic-lumbar-decompression/`** — 11.6K impr, pos 18.2,
0.33% CTR; query "thoracic decompression" 2.1K impr pos 11.1. [Decision]
- Title: `Thoracic & Lumbar Decompression Surgery | Synergy Health`
- Meta: `When spinal decompression surgery is recommended, how it relieves nerve pressure, and what recovery involves. Metro Detroit spine surgeons.`

**10. `/locations/clinic-locations/southfield/spine-neck/`** — 8.1K impr, pos 15.4, 1.33% CTR —
the template for future spine-at-location pages. [Local]
- Title: `Spine & Neck Care in Southfield, MI | Synergy Health`
- Meta: `See a spine specialist in Southfield — surgeons and pain physicians with on-site imaging and PT. Same-week appointments; serving Oakland County.` ⚠️ verify on-site services at Southfield.

## B. Site-wide biggest modeled gaps

**11. `/contact-us/`** — 128.9K impr, pos 6.2, 0.30% CTR (largest modeled gap; much of it is
branded-sitelink noise, so expect partial recovery). [Local]
- Title: `Contact Synergy Health Partners | Schedule an Appointment`
- Meta: `Book online or call to schedule orthopedic, spine, physical therapy, or MRI care at 8 Metro Detroit locations. Same-week appointments available.` ⚠️ same-week wording

**12. `/about-us/company-history/`** — 86.4K impr, pos 5.3, 3.06% CTR — ranks for "mendelson
kornblum" queries; make it the rebrand bridge. [Brand-bridge]
- Title: `Mendelson Kornblum Is Now Synergy Health Partners`
- Meta: `The practice you've known as Mendelson Kornblum Orthopedics continues as Synergy Health Partners — same physicians, same locations, one integrated team.`

**13. `/mendelson-kornblum-orthopedics-is-a-multi-specialty-practice…/`** (legacy post) — 106.5K
impr, pos 5.9, 1.61% CTR. Interim title below; flag to Cardinal as an eventual 301 →
company-history once that page holds the Mendelson rankings. [Brand-bridge]
- Title: `Mendelson Kornblum Orthopedics | Now Synergy Health Partners`
- Meta: `Mendelson Kornblum's orthopedic, spine, and pain teams now practice as Synergy Health Partners. Find your physician and book at the same locations.`

**14. `/flying-with-joint-replacement/`** — 123K impr, pos 6.4, 0.55% CTR. [Info]
- Title: `Flying After a Joint Replacement: What to Expect at TSA`
- Meta: `Will your knee or hip implant set off airport security? What to know before you fly — screening, implant cards, and travel tips after joint replacement.`

**15. `/specialties/physical-therapy/lymphedema-management/`** — 222.6K impr (2nd-largest pool
on the site), pos 8.7, 0.26% CTR. [Info + Local hybrid]
- Title: `Lymphedema Treatment & Certified Therapy | Synergy Health`
- Meta: `How certified lymphedema therapists reduce swelling with manual drainage, compression, and exercise — treatment at Metro Detroit locations.` ⚠️ verify certification claim

**16. `/specialties/hand-upper-extremity/finger-amputation/`** — 60.2K impr, pos 4.6, 0.44% CTR. [Decision — sensitive tone]
- Title: `Finger Amputation: Surgery, Recovery & Rehab | Synergy`
- Meta: `What to expect before and after finger amputation surgery — healing timeline, hand therapy, and returning to daily activities. Metro Detroit hand surgeons.`

**17. `/our-providers/`** — 125.2K impr, pos 10.0, 0.34% CTR. [Local]
- Title: `Find an Orthopedic or Spine Doctor | Synergy Health`
- Meta: `Search Synergy's orthopedic, spine, hand, foot & ankle, and pain physicians across Metro Detroit. Filter by specialty and location; book online.` ⚠️ audit flagged broken find-a-doctor filters — fix or drop "filter" wording.

**18. `/locations/clinic-locations/`** — 118K impr, pos 9.2, 0.91% CTR (apply same pattern to
`/locations/`, 153K impr). [Local]
- Title: `Orthopedic & Spine Clinic Locations — Metro Detroit | Synergy`
- Meta: `Find your nearest Synergy Health Partners clinic — Livonia, Sterling Heights, Southfield, Troy, Rochester, and more. Hours, directions, and booking.`

**19. `/treatment/total-knee-arthroplasty-tka/`** — 56.4K impr, **pos 9.3, 0.02% CTR**; queries
"tka" 43.8K + "tka medical abbreviation" 26K. [Info — definitional; AI-overview headwind]
- Title: `TKA (Total Knee Arthroplasty): A Patient's Guide | Synergy`
- Meta: `What TKA means, how total knee replacement works, and what recovery really looks like — explained simply by Metro Detroit orthopedic surgeons.`

**20. `/full-service-clinics/sterling-heights-2/`** — 94K impr, pos 10.9, 2.73% CTR — strongest
location asset; do NOT change its URL (cluster map §4). [Local]
- Title: `Synergy Health Sterling Heights — Orthopedics, Spine & PT`
- Meta: `Full-service orthopedic and spine care on Mound Rd in Sterling Heights — same-week appointments with on-site MRI and physical therapy.` ⚠️ verify on-site amenities

**21. `/full-service-clinics/port-huron/`** — 40.8K impr, pos 9.6 — real "orthopedic port huron"
demand at pos ~6. [Local] ⚠️ verify clinic's current status/services first.
- Title: `Synergy Health Port Huron — Orthopedic Care & PT`
- Meta: `Orthopedic specialists in Port Huron — joint, spine, hand, and foot care with on-site physical therapy. Book online or call to schedule.`

**22. `/conditions/dupuytrens-contracture/`** — 18.9K impr, pos 14.1, plus **1,013 AI-feature
impressions** (vs ~0 for the legacy 81K-impr `/conditions-we-treat/...dupuytrens-disease/`
version, which consolidates into this one per cluster map §4a — leave the legacy URL alone). [Decision]
- Title: `Dupuytren's Contracture: Signs & Treatment | Synergy`
- Meta: `Why fingers curl inward with Dupuytren's disease, when to see a hand specialist, and treatment options from injections to surgery. Metro Detroit.`

**23. `/specialties/occupational-therapy/hand-therapy/`** — 65.9K impr, pos 16.8, 0.06% CTR;
query "hand therapy" 39.6K impr pos 13.6. [Local]
- Title: `Certified Hand Therapy | Synergy Health`
- Meta: `Work with certified hand therapists on injury recovery, custom splinting, and post-surgical rehab at Metro Detroit locations.` ⚠️ verify CHT credential

**24. `/treatment/prp-injections/`** — 25.7K impr, pos 6.7, 0.07% CTR. [Decision — strict
medical review: evidence for PRP is mixed; keep expectations conservative]
- Title: `PRP Injections: How They Work & What They Treat | Synergy`
- Meta: `How platelet-rich plasma injections are used for joint and tendon problems, who may be a candidate, and what realistic expectations look like.`

**25. `/mri/`** — 83.7K impr, pos 4.8, 4.28% CTR — already the best performer; light polish only. [Local]
- Title: `Open MRI & Imaging in Metro Detroit | Synergy Health`
- Meta: `High-field open MRI with fast scheduling and quick results — multiple Metro Detroit locations. Most insurance accepted; schedule your scan today.` ⚠️ "fast/quick" only if scheduling truly supports it.

---

## Modeled upside (honesty attached)

Full-benchmark recovery across the top-25 gap list ≈ 2,900 clicks/mo; **planning target = ⅓ ≈
+950/mo (+~20% on the ~4,300/mo baseline)**, because several pools are informational queries
losing clicks to AI Overviews no matter the title. The spine rows matter beyond their click
counts — they're decision-stage patients, not abbreviation lookups.

## QA checklist before entering Rank Math

- [ ] Human review of every line (this file is AI-drafted from data; voice + accuracy pass)
- [ ] ⚠️-flagged claims verified (reviewers named, amenities, credentials, same-week, filters)
- [ ] Medical reviewer sign-off on clinical phrasing (ACDF, PRP, fractures, amputation)
- [ ] Titles deduped against the site's existing 120 duplicate-title problem — no new collisions
- [ ] Change date logged in `seo/change-log.md` + GSC annotation added
- [ ] Nothing else edited on these pages in the same batch
