# GBP Listing Estate — first full inventory view (2026-07-22)

Source: the business selector shown during the GBP API access application (pasted by
Joe). ~90 listings under the account. This is raw intel for the local-SEO/citation
workstream (Cardinal Pillar 10 / local AIO) — verify each item in the GBP dashboard
before acting.

## Composition

- **Practice/facility listings (~20):** Synergy Health Partners | Mendelson
  Orthopedics & Spine (Livonia 36622 Five Mile Rd #101, Sterling Heights 35735 Mound
  Rd, Port Huron 600 Fort St #100, Troy Clinic 5107 Rochester Rd), Pain Management
  (Mound Rd), Orthopedic Urgent Care Livonia, PT clinics (Livonia, Sterling Heights,
  Troy 5119 Rochester, Warren, Shelby Township, Port Huron), MRI (Livonia Instant
  Imaging, Sterling Heights Pure Open, Troy Instant Imaging), Synergy Spine & Ortho
  Surgery Center (Warren 12 Mile), Genesys Surgery Center, Chiropractic (×2),
  Business Office (Stephenson Hwy), Michfoot Surgeons legacy (Northwestern Hwy),
  Bone And Joint Institute Pc (2611 Electric Ave), Michigan Brain & Spine Surgery
  Center (5107 Rochester Rd).
- **Physician listings (~70):** most physicians have one listing per practice
  location (e.g., three each for Mayo, Salar, Varghese, Munk, McCarty).

## 🚩 Findings to action (local workstream)

1. **8 listings "Verification required"** — invisible/weakened in Maps until fixed:
   - **Michigan Brain & Spine Surgery Center — 5107 Rochester Rd (TROY)** ← highest
     priority: Troy is the Oakland-expansion unlock and its surgical listing is
     unverified.
   - Synergy Health Partners | Mendelson Kornblum Pain Management (Mound Rd)
   - Bone & Joint Physical Therapy (600 Fort St, Port Huron)
   - SHP Physical Therapy Port Huron (600 Fort Street) — *also a likely duplicate of
     the verified PT Port Huron footprint*
   - SHP Physical Therapy Warren (13488 East Eleven Mile Rd) — *duplicate of the
     verified Warren PT listing (13488 E Eleven Mile Rd)*
   - Troy Instant Imaging — MRI Center (5119 Rochester Rd) — *duplicate of the
     verified Troy Instant Imaging listing at the same address*
   - Brian Fiani, DO (Mound Rd) · M. Wednesday Hall, DO (Mound Rd)
2. **NAP typo on a verified listing:** Synergy MRI: Livonia — Instant Imaging shows
   address "36622 **File** Mile Rd" (should be Five Mile Rd). NAP errors suppress
   local rankings (Cardinal Pillar 10).
3. **Duplicate physician listings splitting reviews/authority:** "Kevin R. Lee, MD"
   (Five Mile + Mound) vs "Dr. Kevin Lee, MD" (Northwestern Hwy); "Preetinder
   Bhullar, MD" vs "Dr. Preetinder Bhullar, MD"; "Randy Leff DPM" vs "Fred Leff,
   DPM" at the same Northwestern Hwy address (verify whether these are two people
   — *answered 2026-07-22: they are two different podiatrists per
   `brand/provider-roster-by-service-line.md`; Randy is enrolled in rater8, Fred is
   not*); Brian Kassa duplicated with "Dr." prefix variant.
4. **Brand-name inconsistency across listings** (entity-coherence issue flagged in
   the audit): "…| Mendelson Orthopedics & Spine", "…& Spine Specialists",
   "…Mendelson Kornblum Pain Management", "(formerly Michfoot Surgeons, PC)".
   Standardize per the brand migration plan.
5. **Legacy/orphan entities to review:** Bone And Joint Institute Pc (Electric Ave),
   Michfoot listing, Business Office listing (consider whether it should be public).

## Next steps

- Once GBP API access is approved: pull all listings via `list_locations`, diff
  against this inventory **and against the 50 rater8-managed listings in
  `brand/gbp-profile-directory.md`** (which listings get review flow vs. sit idle),
  and build the NAP-consistency audit Cardinal called for
  (Pillar 10: GBP-to-on-page NAP match per location).
- Verification sprints + dedupe/merge requests through the GBP dashboard (listing
  owner action).
- Fix the "File Mile" typo immediately — one-field edit on a verified listing.
