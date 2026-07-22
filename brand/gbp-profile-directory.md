# Google Business Profile Directory — Synergy Health Partners

> **Canonical map of every SHP Google Business Profile (GBP / "Google My Business") listing
> managed in rater8**, with review links, Place IDs, and the share of rater8 review requests
> routed to each profile. Source: rater8 "Google Business Profile Scorecard" export supplied
> by Joe **2026-07-22** (per-listing scrape dates 2026-07-21/22) — raw export archived as
> `data/rater8/2026-07-22/gbp-scorecard.csv`.

**What this is for**

- **Review operations** — direct links to read each profile's reviews and the derived
  *write-a-review* link (`…/writereview?placeid=…`) for QR codes, follow-up emails, and
  front-desk cards.
- **Local SEO / schema** — Place IDs are the stable keys for `sameAs` / `hasMap` schema on
  physician-bio and location pages (Cardinal Pillar 6), citation building, and any future
  GBP API work (the API approval in `docs/data-sources-roadmap.md` §6).
- **Reputation measurement** — "review requests %" shows how rater8's review balancing
  currently distributes each provider's/location's review-request volume across Google
  profiles. Where a provider's Google shares sum to <100%, the remainder routes to
  non-Google sites (Healthgrades / Vitals / WebMD — confirmed by those sources appearing
  in the patient-feedback export). **Exact denominator semantics: confirm with the rater8
  rep** before using these numbers for anything load-bearing.

**Interpretation notes:** "Review Requests %" is per entity (each provider's listings sum
to ~100%; the five location profiles sum to ~100% of location-level requests). "—" = no
requests currently routed to that profile.

---

## ⚠️ Coverage gaps (found 2026-07-22 — act on these)

1. **SHP Clinic: Troy has NO Google profile linked in rater8** (no Place ID, no link) and
   receives only **0.8%** of location-level review requests. Troy is the #1 strategic
   growth market (Oakland County unlock) and fixing its Maps/GBP presence is already P1
   task **GOV-A.1** (owner Paul, due 2026-07-26) — this is hard evidence for that task.
   Only one provider, **Ben Mayo, M.D.**, has a Troy provider listing (7.3% of his requests).
2. **Rochester (and any other of the 8 locations beyond the five below) is absent from
   rater8 entirely** — no location or provider profiles. Confirm which locations have GBPs
   and enroll them.
3. **Two roster physicians have no rater8-managed GBP listing:** **Lucia Zamorano, MD**
   (neurosurgeon — spine, the growth priority; her site bio also still links legacy
   `mendelsonortho` Zocdoc) and **Fred Leff, DPM**. Confirm whether profiles exist outside
   rater8 and enroll them.
4. **Linked but receiving zero routed requests:** Kevin Lee (Sterling Heights), SHP
   Physical Therapy: Sterling Heights, Synergy Ambulatory Surgery Center, and the corporate
   "Synergy Health Partners" profile. Decide deliberately whether each should receive
   review flow (the ASC and PT profiles are patient-facing and reviewable today).
5. **Pin-location spot-check:** the "Alice Mendelson, M.D. (SHP: Livonia)" listing's Place
   ID falls in the same ID cluster as every Sterling Heights listing, unlike all other
   Livonia listings (heuristic — Place-ID prefixes correlate with map location). Click her
   [map link](https://www.google.com/maps/place/?q=place_id:ChIJRXCdkhraJIgRgvA_knxiutU)
   and confirm the profile's pin/address actually shows Livonia.

---

## Location & organization profiles

| Listing | Review requests % | Links | Place ID |
|---|---|---|---|
| SHP: Livonia | 47.4% | [reviews](https://search.google.com/local/reviews?placeid=ChIJYRydToyyJIgRSSdA8Hjp1bY) · [write a review](https://search.google.com/local/writereview?placeid=ChIJYRydToyyJIgRSSdA8Hjp1bY) · [map](https://www.google.com/maps/place/?q=place_id:ChIJYRydToyyJIgRSSdA8Hjp1bY) | `ChIJYRydToyyJIgRSSdA8Hjp1bY` |
| SHP: Sterling Heights | 37.1% | [reviews](https://search.google.com/local/reviews?placeid=ChIJ6QaEtJrZJIgR4VqEfaznNsE) · [write a review](https://search.google.com/local/writereview?placeid=ChIJ6QaEtJrZJIgR4VqEfaznNsE) · [map](https://www.google.com/maps/place/?q=place_id:ChIJ6QaEtJrZJIgR4VqEfaznNsE) | `ChIJ6QaEtJrZJIgR4VqEfaznNsE` |
| SHP Clinic: Southfield | 12.8% | [reviews](https://search.google.com/local/reviews?placeid=ChIJwTae_YS3JIgRKm3iqM8HoNE) · [write a review](https://search.google.com/local/writereview?placeid=ChIJwTae_YS3JIgRKm3iqM8HoNE) · [map](https://www.google.com/maps/place/?q=place_id:ChIJwTae_YS3JIgRKm3iqM8HoNE) | `ChIJwTae_YS3JIgRKm3iqM8HoNE` |
| SHP Clinic: Troy | 0.8% | **none — profile not linked in rater8** | — |
| SHP Clinic: Port Huron | 1.6% | [reviews](https://search.google.com/local/reviews?placeid=ChIJgbd68-mdJYgRjj5TYZ2SEIQ) · [write a review](https://search.google.com/local/writereview?placeid=ChIJgbd68-mdJYgRjj5TYZ2SEIQ) · [map](https://www.google.com/maps/place/?q=place_id:ChIJgbd68-mdJYgRjj5TYZ2SEIQ) | `ChIJgbd68-mdJYgRjj5TYZ2SEIQ` |
| SHP Physical Therapy: Sterling Heights | — | [reviews](https://search.google.com/local/reviews?placeid=ChIJiQ9CTxbaJIgRnskppXvTe0E) · [write a review](https://search.google.com/local/writereview?placeid=ChIJiQ9CTxbaJIgRnskppXvTe0E) · [map](https://www.google.com/maps/place/?q=place_id:ChIJiQ9CTxbaJIgRnskppXvTe0E) | `ChIJiQ9CTxbaJIgRnskppXvTe0E` |
| Synergy Ambulatory Surgery Center | — | [reviews](https://search.google.com/local/reviews?placeid=ChIJi8krPJraJIgRUluVg75tS_o) · [write a review](https://search.google.com/local/writereview?placeid=ChIJi8krPJraJIgRUluVg75tS_o) · [map](https://www.google.com/maps/place/?q=place_id:ChIJi8krPJraJIgRUluVg75tS_o) | `ChIJi8krPJraJIgRUluVg75tS_o` |
| Synergy Health Partners | — | [reviews](https://search.google.com/local/reviews?placeid=ChIJo2Mb2LbFJIgRtk7dzv7qjiQ) · [write a review](https://search.google.com/local/writereview?placeid=ChIJo2Mb2LbFJIgRtk7dzv7qjiQ) · [map](https://www.google.com/maps/place/?q=place_id:ChIJo2Mb2LbFJIgRtk7dzv7qjiQ) | `ChIJo2Mb2LbFJIgRtk7dzv7qjiQ` |

*Location-level review requests split: Livonia 47.4% · Sterling Heights 37.1% ·
Southfield 12.8% · Port Huron 1.6% · Troy 0.8%.*

## Provider profiles (42 listings, 22 physicians)

Grouped by location. The **Google share** table below summarizes each physician's total
share of review requests routed to Google (vs. Healthgrades/Vitals/WebMD).

### SHP: Livonia

| Provider | Review requests % | Links | Place ID |
|---|---|---|---|
| Alice Mendelson, M.D. | 100.0% | [reviews](https://search.google.com/local/reviews?placeid=ChIJRXCdkhraJIgRgvA_knxiutU) · [write a review](https://search.google.com/local/writereview?placeid=ChIJRXCdkhraJIgRgvA_knxiutU) · [map](https://www.google.com/maps/place/?q=place_id:ChIJRXCdkhraJIgRgvA_knxiutU) | `ChIJRXCdkhraJIgRgvA_knxiutU` |
| Anthony Oddo, D.O. | 44.2% | [reviews](https://search.google.com/local/reviews?placeid=ChIJ71VxhpKyJIgRodWa4XsaX9s) · [write a review](https://search.google.com/local/writereview?placeid=ChIJ71VxhpKyJIgRodWa4XsaX9s) · [map](https://www.google.com/maps/place/?q=place_id:ChIJ71VxhpKyJIgRodWa4XsaX9s) | `ChIJ71VxhpKyJIgRodWa4XsaX9s` |
| Ben Mayo, M.D. | 63.2% | [reviews](https://search.google.com/local/reviews?placeid=ChIJsza5JQazJIgR11tLvxJw9IY) · [write a review](https://search.google.com/local/writereview?placeid=ChIJsza5JQazJIgR11tLvxJw9IY) · [map](https://www.google.com/maps/place/?q=place_id:ChIJsza5JQazJIgR11tLvxJw9IY) | `ChIJsza5JQazJIgR11tLvxJw9IY` |
| David Mendelson, M.D. | 52.7% | [reviews](https://search.google.com/local/reviews?placeid=ChIJKZX9vI2yJIgR7f82nWo1gcs) · [write a review](https://search.google.com/local/writereview?placeid=ChIJKZX9vI2yJIgR7f82nWo1gcs) · [map](https://www.google.com/maps/place/?q=place_id:ChIJKZX9vI2yJIgR7f82nWo1gcs) | `ChIJKZX9vI2yJIgR7f82nWo1gcs` |
| Hanish Singh, M.D. | 86.2% | [reviews](https://search.google.com/local/reviews?placeid=ChIJv6qelHevJIgRQddw7ChaGm0) · [write a review](https://search.google.com/local/writereview?placeid=ChIJv6qelHevJIgRQddw7ChaGm0) · [map](https://www.google.com/maps/place/?q=place_id:ChIJv6qelHevJIgRQddw7ChaGm0) | `ChIJv6qelHevJIgRQddw7ChaGm0` |
| Jeffrey Klein, D.P.M. | 59.5% | [reviews](https://search.google.com/local/reviews?placeid=ChIJGRurSYyyJIgRBBu5p4kazo8) · [write a review](https://search.google.com/local/writereview?placeid=ChIJGRurSYyyJIgRBBu5p4kazo8) · [map](https://www.google.com/maps/place/?q=place_id:ChIJGRurSYyyJIgRBBu5p4kazo8) | `ChIJGRurSYyyJIgRBBu5p4kazo8` |
| Jeffrey Mendelson, M.D. | 38.0% | [reviews](https://search.google.com/local/reviews?placeid=ChIJJVZxhpKyJIgRy0txszibm08) · [write a review](https://search.google.com/local/writereview?placeid=ChIJJVZxhpKyJIgRy0txszibm08) · [map](https://www.google.com/maps/place/?q=place_id:ChIJJVZxhpKyJIgRy0txszibm08) | `ChIJJVZxhpKyJIgRy0txszibm08` |
| Jeffrey Varghese, M.D. | 34.4% | [reviews](https://search.google.com/local/reviews?placeid=ChIJ6RZ1UMizJIgRTPpjvQibjXw) · [write a review](https://search.google.com/local/writereview?placeid=ChIJ6RZ1UMizJIgRTPpjvQibjXw) · [map](https://www.google.com/maps/place/?q=place_id:ChIJ6RZ1UMizJIgRTPpjvQibjXw) | `ChIJ6RZ1UMizJIgRTPpjvQibjXw` |
| Joseph Maslak, M.D. | 53.0% | [reviews](https://search.google.com/local/reviews?placeid=ChIJSwBOkSWzJIgRbwIMzKsNCd8) · [write a review](https://search.google.com/local/writereview?placeid=ChIJSwBOkSWzJIgRbwIMzKsNCd8) · [map](https://www.google.com/maps/place/?q=place_id:ChIJSwBOkSWzJIgRbwIMzKsNCd8) | `ChIJSwBOkSWzJIgRbwIMzKsNCd8` |
| Kevin Lee, M.D. | 77.8% | [reviews](https://search.google.com/local/reviews?placeid=ChIJLXJDgjyzJIgR14gbw14b66M) · [write a review](https://search.google.com/local/writereview?placeid=ChIJLXJDgjyzJIgR14gbw14b66M) · [map](https://www.google.com/maps/place/?q=place_id:ChIJLXJDgjyzJIgR14gbw14b66M) | `ChIJLXJDgjyzJIgR14gbw14b66M` |
| Kyle Bohm, M.D. | 60.9% | [reviews](https://search.google.com/local/reviews?placeid=ChIJG7AzuYuyJIgRrTLstnw4Za8) · [write a review](https://search.google.com/local/writereview?placeid=ChIJG7AzuYuyJIgRrTLstnw4Za8) · [map](https://www.google.com/maps/place/?q=place_id:ChIJG7AzuYuyJIgRrTLstnw4Za8) | `ChIJG7AzuYuyJIgRrTLstnw4Za8` |
| Mohamed Salar, M.D. | 55.2% | [reviews](https://search.google.com/local/reviews?placeid=ChIJF_I35MWzJIgRTaOEg4SWFas) · [write a review](https://search.google.com/local/writereview?placeid=ChIJF_I35MWzJIgRTaOEg4SWFas) · [map](https://www.google.com/maps/place/?q=place_id:ChIJF_I35MWzJIgRTaOEg4SWFas) | `ChIJF_I35MWzJIgRTaOEg4SWFas` |
| Preetinder Bhullar, M.D. | 72.9% | [reviews](https://search.google.com/local/reviews?placeid=ChIJuz29SxmzJIgRqQZukK-gepw) · [write a review](https://search.google.com/local/writereview?placeid=ChIJuz29SxmzJIgRqQZukK-gepw) · [map](https://www.google.com/maps/place/?q=place_id:ChIJuz29SxmzJIgRqQZukK-gepw) | `ChIJuz29SxmzJIgRqQZukK-gepw` |
| Scott McCarty, M.D. | 68.2% | [reviews](https://search.google.com/local/reviews?placeid=ChIJkYbXZ3izJIgRXT99t0BFblc) · [write a review](https://search.google.com/local/writereview?placeid=ChIJkYbXZ3izJIgRXT99t0BFblc) · [map](https://www.google.com/maps/place/?q=place_id:ChIJkYbXZ3izJIgRXT99t0BFblc) | `ChIJkYbXZ3izJIgRXT99t0BFblc` |
| Stephen Mendelson, M.D. | 45.0% | [reviews](https://search.google.com/local/reviews?placeid=ChIJJVZxhpKyJIgRd2TcUQ2Q65E) · [write a review](https://search.google.com/local/writereview?placeid=ChIJJVZxhpKyJIgRd2TcUQ2Q65E) · [map](https://www.google.com/maps/place/?q=place_id:ChIJJVZxhpKyJIgRd2TcUQ2Q65E) | `ChIJJVZxhpKyJIgRd2TcUQ2Q65E` |
| Tony Abood, D.O. | 44.3% | [reviews](https://search.google.com/local/reviews?placeid=ChIJYbKLBSuzJIgRYoSZDqXpn0g) · [write a review](https://search.google.com/local/writereview?placeid=ChIJYbKLBSuzJIgRYoSZDqXpn0g) · [map](https://www.google.com/maps/place/?q=place_id:ChIJYbKLBSuzJIgRYoSZDqXpn0g) | `ChIJYbKLBSuzJIgRYoSZDqXpn0g` |

### SHP: Sterling Heights

| Provider | Review requests % | Links | Place ID |
|---|---|---|---|
| Andres Munk, M.D. | 71.5% | [reviews](https://search.google.com/local/reviews?placeid=ChIJJ5HHRP3bJIgRLPsNS08Eey8) · [write a review](https://search.google.com/local/writereview?placeid=ChIJJ5HHRP3bJIgRLPsNS08Eey8) · [map](https://www.google.com/maps/place/?q=place_id:ChIJJ5HHRP3bJIgRLPsNS08Eey8) | `ChIJJ5HHRP3bJIgRLPsNS08Eey8` |
| Anthony Oddo, D.O. | 52.0% | [reviews](https://search.google.com/local/reviews?placeid=ChIJRXCdkhraJIgRdcGEaPkdhAg) · [write a review](https://search.google.com/local/writereview?placeid=ChIJRXCdkhraJIgRdcGEaPkdhAg) · [map](https://www.google.com/maps/place/?q=place_id:ChIJRXCdkhraJIgRdcGEaPkdhAg) | `ChIJRXCdkhraJIgRdcGEaPkdhAg` |
| Ben Mayo, M.D. | 29.5% | [reviews](https://search.google.com/local/reviews?placeid=ChIJazHBPerbJIgR3KYkcQX_qbk) · [write a review](https://search.google.com/local/writereview?placeid=ChIJazHBPerbJIgR3KYkcQX_qbk) · [map](https://www.google.com/maps/place/?q=place_id:ChIJazHBPerbJIgR3KYkcQX_qbk) | `ChIJazHBPerbJIgR3KYkcQX_qbk` |
| Brian Kassa, D.O. | 82.5% | [reviews](https://search.google.com/local/reviews?placeid=ChIJ55u1XnDbJIgRG9Y9Jedt4Mg) · [write a review](https://search.google.com/local/writereview?placeid=ChIJ55u1XnDbJIgRG9Y9Jedt4Mg) · [map](https://www.google.com/maps/place/?q=place_id:ChIJ55u1XnDbJIgRG9Y9Jedt4Mg) | `ChIJ55u1XnDbJIgRG9Y9Jedt4Mg` |
| David Mendelson, M.D. | 47.3% | [reviews](https://search.google.com/local/reviews?placeid=ChIJRXCdkhraJIgRyj0q78GV3Zk) · [write a review](https://search.google.com/local/writereview?placeid=ChIJRXCdkhraJIgRyj0q78GV3Zk) · [map](https://www.google.com/maps/place/?q=place_id:ChIJRXCdkhraJIgRyj0q78GV3Zk) | `ChIJRXCdkhraJIgRyj0q78GV3Zk` |
| Jeffrey Klein, D.P.M. | 40.5% | [reviews](https://search.google.com/local/reviews?placeid=ChIJRXCdkhraJIgR3nwwf0zCzeM) · [write a review](https://search.google.com/local/writereview?placeid=ChIJRXCdkhraJIgR3nwwf0zCzeM) · [map](https://www.google.com/maps/place/?q=place_id:ChIJRXCdkhraJIgR3nwwf0zCzeM) | `ChIJRXCdkhraJIgR3nwwf0zCzeM` |
| Jeffrey Mendelson, M.D. | 62.0% | [reviews](https://search.google.com/local/reviews?placeid=ChIJRXCdkhraJIgRUW7iH0nxHCc) · [write a review](https://search.google.com/local/writereview?placeid=ChIJRXCdkhraJIgRUW7iH0nxHCc) · [map](https://www.google.com/maps/place/?q=place_id:ChIJRXCdkhraJIgRUW7iH0nxHCc) | `ChIJRXCdkhraJIgRUW7iH0nxHCc` |
| Jeffrey Varghese, M.D. | 65.6% | [reviews](https://search.google.com/local/reviews?placeid=ChIJPaZ9HrPbJIgR7cofjS00v4s) · [write a review](https://search.google.com/local/writereview?placeid=ChIJPaZ9HrPbJIgR7cofjS00v4s) · [map](https://www.google.com/maps/place/?q=place_id:ChIJPaZ9HrPbJIgR7cofjS00v4s) | `ChIJPaZ9HrPbJIgR7cofjS00v4s` |
| Joseph Maslak, M.D. | 47.0% | [reviews](https://search.google.com/local/reviews?placeid=ChIJ8afDlD3bJIgR61DYkyEXAZQ) · [write a review](https://search.google.com/local/writereview?placeid=ChIJ8afDlD3bJIgR61DYkyEXAZQ) · [map](https://www.google.com/maps/place/?q=place_id:ChIJ8afDlD3bJIgR61DYkyEXAZQ) | `ChIJ8afDlD3bJIgR61DYkyEXAZQ` |
| Joseph Yacisen, D.O. | 68.9% | [reviews](https://search.google.com/local/reviews?placeid=ChIJCfG0nq_bJIgRpC1fw9YFu5M) · [write a review](https://search.google.com/local/writereview?placeid=ChIJCfG0nq_bJIgRpC1fw9YFu5M) · [map](https://www.google.com/maps/place/?q=place_id:ChIJCfG0nq_bJIgRpC1fw9YFu5M) | `ChIJCfG0nq_bJIgRpC1fw9YFu5M` |
| Kevin Lee, M.D. | — | [reviews](https://search.google.com/local/reviews?placeid=ChIJi_Q0Vn7bJIgRpVLs853R8XA) · [write a review](https://search.google.com/local/writereview?placeid=ChIJi_Q0Vn7bJIgRpVLs853R8XA) · [map](https://www.google.com/maps/place/?q=place_id:ChIJi_Q0Vn7bJIgRpVLs853R8XA) | `ChIJi_Q0Vn7bJIgRpVLs853R8XA` |
| Kyle Bohm, M.D. | 39.1% | [reviews](https://search.google.com/local/reviews?placeid=ChIJQeUtbhDaJIgRzjZQXqfSnBU) · [write a review](https://search.google.com/local/writereview?placeid=ChIJQeUtbhDaJIgRzjZQXqfSnBU) · [map](https://www.google.com/maps/place/?q=place_id:ChIJQeUtbhDaJIgRzjZQXqfSnBU) | `ChIJQeUtbhDaJIgRzjZQXqfSnBU` |
| Mohamed Salar, M.D. | 44.5% | [reviews](https://search.google.com/local/reviews?placeid=ChIJ9aC3uubbJIgRc3d7s8F9pL0) · [write a review](https://search.google.com/local/writereview?placeid=ChIJ9aC3uubbJIgRc3d7s8F9pL0) · [map](https://www.google.com/maps/place/?q=place_id:ChIJ9aC3uubbJIgRc3d7s8F9pL0) | `ChIJ9aC3uubbJIgRc3d7s8F9pL0` |
| Preetinder Bhullar, M.D. | 12.9% | [reviews](https://search.google.com/local/reviews?placeid=ChIJN0EIaoPbJIgRMmhvlzoZG00) · [write a review](https://search.google.com/local/writereview?placeid=ChIJN0EIaoPbJIgRMmhvlzoZG00) · [map](https://www.google.com/maps/place/?q=place_id:ChIJN0EIaoPbJIgRMmhvlzoZG00) | `ChIJN0EIaoPbJIgRMmhvlzoZG00` |
| Scott McCarty, M.D. | 27.1% | [reviews](https://search.google.com/local/reviews?placeid=ChIJ90iLHOLbJIgRJUtYz-ynVJY) · [write a review](https://search.google.com/local/writereview?placeid=ChIJ90iLHOLbJIgRJUtYz-ynVJY) · [map](https://www.google.com/maps/place/?q=place_id:ChIJ90iLHOLbJIgRJUtYz-ynVJY) | `ChIJ90iLHOLbJIgRJUtYz-ynVJY` |
| Stephen Mendelson, M.D. | 55.0% | [reviews](https://search.google.com/local/reviews?placeid=ChIJRXCdkhraJIgRB4EVnXfB8Z4) · [write a review](https://search.google.com/local/writereview?placeid=ChIJRXCdkhraJIgRB4EVnXfB8Z4) · [map](https://www.google.com/maps/place/?q=place_id:ChIJRXCdkhraJIgRB4EVnXfB8Z4) | `ChIJRXCdkhraJIgRB4EVnXfB8Z4` |
| Tony Abood, D.O. | 49.9% | [reviews](https://search.google.com/local/reviews?placeid=ChIJB9pfI3jbJIgRCrksKOhoeBQ) · [write a review](https://search.google.com/local/writereview?placeid=ChIJB9pfI3jbJIgRCrksKOhoeBQ) · [map](https://www.google.com/maps/place/?q=place_id:ChIJB9pfI3jbJIgRCrksKOhoeBQ) | `ChIJB9pfI3jbJIgRCrksKOhoeBQ` |

### SHP Clinic: Southfield

| Provider | Review requests % | Links | Place ID |
|---|---|---|---|
| Kevin Lee, M.D. | 22.2% | [reviews](https://search.google.com/local/reviews?placeid=ChIJG_wVwLe3JIgRTflOqC8QXqM) · [write a review](https://search.google.com/local/writereview?placeid=ChIJG_wVwLe3JIgRTflOqC8QXqM) · [map](https://www.google.com/maps/place/?q=place_id:ChIJG_wVwLe3JIgRTflOqC8QXqM) | `ChIJG_wVwLe3JIgRTflOqC8QXqM` |
| Kevin Sorensen, D.P.M. | 91.2% | [reviews](https://search.google.com/local/reviews?placeid=ChIJRTfWHBG3JIgRmL6nzgYjQTY) · [write a review](https://search.google.com/local/writereview?placeid=ChIJRTfWHBG3JIgRmL6nzgYjQTY) · [map](https://www.google.com/maps/place/?q=place_id:ChIJRTfWHBG3JIgRmL6nzgYjQTY) | `ChIJRTfWHBG3JIgRmL6nzgYjQTY` |
| Kristina Green, D.P.M. | 56.5% | [reviews](https://search.google.com/local/reviews?placeid=ChIJaYeRTx23JIgRvFyS3WLl_xA) · [write a review](https://search.google.com/local/writereview?placeid=ChIJaYeRTx23JIgRvFyS3WLl_xA) · [map](https://www.google.com/maps/place/?q=place_id:ChIJaYeRTx23JIgRvFyS3WLl_xA) | `ChIJaYeRTx23JIgRvFyS3WLl_xA` |
| Preetinder Bhullar, M.D. | 14.2% | [reviews](https://search.google.com/local/reviews?placeid=ChIJUYQNsjK3JIgRoBVwOtTZ6dw) · [write a review](https://search.google.com/local/writereview?placeid=ChIJUYQNsjK3JIgRoBVwOtTZ6dw) · [map](https://www.google.com/maps/place/?q=place_id:ChIJUYQNsjK3JIgRoBVwOtTZ6dw) | `ChIJUYQNsjK3JIgRoBVwOtTZ6dw` |
| Randy Leff, D.P.M. | 99.9% | [reviews](https://search.google.com/local/reviews?placeid=ChIJM8Sf_YS3JIgRMLKjyYy1TSU) · [write a review](https://search.google.com/local/writereview?placeid=ChIJM8Sf_YS3JIgRMLKjyYy1TSU) · [map](https://www.google.com/maps/place/?q=place_id:ChIJM8Sf_YS3JIgRMLKjyYy1TSU) | `ChIJM8Sf_YS3JIgRMLKjyYy1TSU` |
| Scott McCarty, M.D. | 4.6% | [reviews](https://search.google.com/local/reviews?placeid=ChIJeZL497O3JIgRQvuqcowQU_U) · [write a review](https://search.google.com/local/writereview?placeid=ChIJeZL497O3JIgRQvuqcowQU_U) · [map](https://www.google.com/maps/place/?q=place_id:ChIJeZL497O3JIgRQvuqcowQU_U) | `ChIJeZL497O3JIgRQvuqcowQU_U` |

### SHP Clinic: Troy

| Provider | Review requests % | Links | Place ID |
|---|---|---|---|
| Ben Mayo, M.D. | 7.3% | [reviews](https://search.google.com/local/reviews?placeid=ChIJZWYp7u3DJIgR2Ns7f_x-z9s) · [write a review](https://search.google.com/local/writereview?placeid=ChIJZWYp7u3DJIgR2Ns7f_x-z9s) · [map](https://www.google.com/maps/place/?q=place_id:ChIJZWYp7u3DJIgR2Ns7f_x-z9s) | `ChIJZWYp7u3DJIgR2Ns7f_x-z9s` |

### SHP Clinic: Port Huron

| Provider | Review requests % | Links | Place ID |
|---|---|---|---|
| Andres Munk, M.D. | 23.5% | [reviews](https://search.google.com/local/reviews?placeid=ChIJNQFTJx2dJYgR5lLo67wLC6Y) · [write a review](https://search.google.com/local/writereview?placeid=ChIJNQFTJx2dJYgR5lLo67wLC6Y) · [map](https://www.google.com/maps/place/?q=place_id:ChIJNQFTJx2dJYgR5lLo67wLC6Y) | `ChIJNQFTJx2dJYgR5lLo67wLC6Y` |
| Joseph Yacisen, D.O. | 31.1% | [reviews](https://search.google.com/local/reviews?placeid=ChIJk7KZCvidJYgRGdMZvkX7Ro4) · [write a review](https://search.google.com/local/writereview?placeid=ChIJk7KZCvidJYgRGdMZvkX7Ro4) · [map](https://www.google.com/maps/place/?q=place_id:ChIJk7KZCvidJYgRGdMZvkX7Ro4) | `ChIJk7KZCvidJYgRGdMZvkX7Ro4` |

### Per-physician share of review requests routed to Google

<100% = remainder routes to non-Google review sites (Healthgrades / Vitals / WebMD).

| Physician | Locations with a GBP listing | Google share |
|---|---|---|
| Kristina Green, D.P.M. | Southfield | 57% |
| Brian Kassa, D.O. | Sterling Heights | 82% |
| Hanish Singh, M.D. | Livonia | 86% |
| Kevin Sorensen, D.P.M. | Southfield | 91% |
| Tony Abood, D.O. | Livonia, Sterling Heights | 94% |
| Andres Munk, M.D. | Port Huron, Sterling Heights | 95% |
| Anthony Oddo, D.O. | Livonia, Sterling Heights | 96% |
| Mohamed Salar, M.D. | Livonia, Sterling Heights | 100% |
| Randy Leff, D.P.M. | Southfield | 100% |
| Preetinder Bhullar, M.D. | Southfield, Livonia, Sterling Heights | 100% |
| Jeffrey Mendelson, M.D. | Livonia, Sterling Heights | 100% |
| Joseph Maslak, M.D. | Livonia, Sterling Heights | 100% |
| Jeffrey Klein, D.P.M. | Livonia, Sterling Heights | 100% |
| David Mendelson, M.D. | Livonia, Sterling Heights | 100% |
| Ben Mayo, M.D. | Troy, Livonia, Sterling Heights | 100% |
| Alice Mendelson, M.D. | Livonia | 100% |
| Scott McCarty, M.D. | Southfield, Livonia, Sterling Heights | 100% |
| Kyle Bohm, M.D. | Livonia, Sterling Heights | 100% |
| Joseph Yacisen, D.O. | Port Huron, Sterling Heights | 100% |
| Kevin Lee, M.D. | Southfield, Livonia, Sterling Heights | 100% |
| Stephen Mendelson, M.D. | Livonia, Sterling Heights | 100% |
| Jeffrey Varghese, M.D. | Livonia, Sterling Heights | 100% |

## Provenance & refresh

- Source: rater8 GBP Scorecard export (original file
  `Google_Business_Profile_Scorecard__Synergy_Health_Partners_Troy_MI.xlsx`), scraped
  2026-07-21/22, archived at `data/rater8/2026-07-22/gbp-scorecard.csv`.
- Refresh by dropping a new dated export into `data/rater8/<date>/` (convention:
  `docs/data-sources-roadmap.md` §9) and regenerating this table; long-term, the GBP API
  (roadmap §6) replaces the scrape.
- Review-velocity baseline against Cardinal's Phase-3 program:
  `audits/rater8-reputation-baseline-2026-07.md`.
