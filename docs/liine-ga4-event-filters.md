# Liine → GA4 Event Forwarding — Filter Build (Locations & Landing URLs)

Config spec for Liine's native GA4 integration wizard (**Connect to GA4 → Filter
Events → Confirm Filters → Acknowledge**). This is the integration that finally puts
**booked-patient truth into GA4** — today Liine conversions exist only in Google Ads
(see `audits/cardinal-recommendation-tracker.md` §4, the 🟠 call-tracking gate).

**Baseline verified 2026-07-22 (GA4 eventName scan, 30d):** GA4 property 370514163
receives **zero Liine events today** — only site-side events exist (`new_patient_intent`
3,981 · `book_appointment_click` 2,980 · `click_to_call` 1,328 ·
`appointment_handoff_to_zocdoc` 1,252). Whatever this wizard forwards is net-new data,
and **nothing backfills** — events before go-live are gone for GA4. Configure once,
correctly, and prefer over-collection to silent loss.

---

## Step 1 — Connect to GA4

| Setting | Value |
|---|---|
| Account | **24916876** — "Synergyhealth.org - New June 2024" |
| Property | **370514163** — "SHP - New Site - GA4" ← the only property under the account (verified via GA4 Admin API 2026-07-22); if the picker shows anything else, stop and check |
| Who connects | The Google login with GA4 **Editor+** on the property (Joe / Santosh) + a Liine admin login |

---

## Step 2 — Filter Events: recommended configuration

> **Leave BOTH filters disabled — send all events.** ("By default, all events will be
> forwarded from Liine if no filters are selected.")

This is a deliberate recommendation, not a shrug. The evidence (GA4, 90d to 2026-07-21):

1. **The GA4 property is the whole practice.** Every location's traffic, every service
   line, one property. There is no location or page family whose booked-call truth we
   want *excluded* from measurement — spine reporting, physician one-pagers, and the
   Cardinal measurement framework all need the complete picture.
2. **The landing-URL space is too fragmented to allowlist safely.** **881 distinct
   landing-URL strings** took sessions in 90 days; **165 distinct strings** produced at
   least one `click_to_call`. The same page lives under many URLs: paid `?scct=`
   params on every paid LP, `?y_source=` on every GBP listing link, `msclkid`/`fbclid`
   click IDs, plus the audit's four parallel URL structures (`/locations/`,
   `/locations/clinic-locations/`, `/location/`, `/locations-type/`) and live legacy
   paths (`/full-service-clinics/`, `/shp-*`).
3. **The homepage is the #1 call-driving landing family and cannot be allowlisted with
   a contains match.** Five live homepage variants (`/`, `/?scct=257771`,
   `/?scct=278427`, two `/?y_source=…`) drove **~687 click-to-calls in 90d** — and the
   only contains token that matches them (`/`) matches everything. An "only the pages
   we care about" allowlist silently drops the single biggest call source.
4. **Include lists rot.** A new clinic (Troy push, Oakland expansion), a renamed Liine
   location, or a new LP structure would be silently excluded from the day it launches —
   exactly the kind of quiet measurement hole the Cardinal audits exist to close.

**The only good reason to enable a filter:** the Liine account contains lines that are
*not* SHP patient-facing marketing reality — test/training lines, internal-transfer
lines, or another entity's locations. Check the pickers on this screen; if junk exists,
build the include lists below. If everything in the picker is a real SHP location,
leave filters off and move to Step 3.

### 2a. Location filter — the build (only if junk lines exist)

**Match type: `Contains` (case-insensitive). Never `Exact`.** Liine's display names
almost certainly don't match our canonical names ("Synergy Health Partners – Sterling
Heights" vs "Sterling Hts Ortho"), and any future rename silently breaks an Exact match.

Include **every** patient-facing location. Tokens chosen to survive naming drift:

| # | Contains token | Covers | Web-call evidence (90d) |
|---|---|---|---|
| 1 | `livonia` | Livonia clinic + any Livonia-named PT/MRI/ASC line | Top call driver: paid ortho LP 276 + location page 76 |
| 2 | `sterling` | Sterling Heights (survives "Sterling Hts") | Paid ortho LP 129 + location page 47 |
| 3 | `southfield` | Southfield (podiatry focus + spine/ortho pages) | Location page 34; legacy Southfield spine LP still takes paid Bing traffic |
| 4 | `troy` | Troy clinic (no paid campaign today — keep for organic/GBP calls) | Location page live, 1,794 words |
| 5 | `huron` | Port Huron (survives "Port Huron"/"Port-Huron" spacing) | Location page + paid variant 32 |
| 6 | `warren` | Synergy Surgery Center (Warren ASC) | ASC pages take sessions + calls |
| 7 | `genesys` | Genesys Surgery Center | Location page 25 click-to-calls |
| 8 | *(verify in picker)* | **Rochester** — named in `brand/brand-brief.md` as one of the 8, but has **zero site presence** (0 pageviews/365d); confirm whether a Liine location exists at all | none on the website |
| 9 | *(verify in picker)* | MRI / imaging lines (Pure Open MRI, Instant Imaging) and PT lines if tracked separately in Liine | `/locations/mri-locations/` 6,272 views/365d; `/shp-physical-therapy/*` still landing 90+ sessions/90d |

**QA rule:** after selecting, every token must match ≥1 location in the picker, and the
total matched must equal the number of real patient-facing Liine locations. A token
matching 0 = naming mismatch — fix the token, don't drop the location.

### 2b. Landing URL filter — the build (only if a filter is mandated)

**Match type: `Contains` (case-insensitive). Never `Exact`.** Unless Liine explicitly
normalizes query strings (the UI doesn't say so), Exact misses every `?scct=` /
`?y_source=` / `msclkid` variant — which is *most* paid and GBP call traffic — and even
path-only Exact misses the legacy path variants still taking real sessions.

**Safest filtered config — one token:**

| Contains token | Effect |
|---|---|
| `synergyhealth.org` | Forwards every event whose landing URL is our site, excludes any non-SHP domain in the Liine account. Functionally "all real traffic." |

**Narrow marketing allowlist — NOT recommended** (loses the ~687/90d homepage-family
calls, ~25% of top-40 call volume — see §2 point 3). If it's ever forced, it must
include ALL of these; omitting any row silently undercounts that family:

| Contains token | Page family | Click-to-calls (90d, observed) |
|---|---|---|
| `/specialty/orthopedic-services/` | Paid ortho LPs (Livonia + Sterling Heights) | 405 |
| `/specialty/spine-neck-back/` | Spine LP (both `?scct` campaign variants) | 109 |
| `/specialty/hand-wrist/` | Hand LP | 71 |
| `/specialty/foot-ankle-specialists/` | Podiatry LP | 34 |
| `/location` | One token covers all four structures: `/locations/…`, `/location/…`, `/locations-type/…`, `/locations/clinic-locations/…` | 267+ across location pages |
| `/providers/` | All ~66 provider bios | ~400 aggregate |
| `/full-service-clinics/` | Legacy pre-rebrand location URLs (audit: the Sterling Heights variant was the site's #3 clicked page) | still landing |
| `/shp-` | Legacy PT sub-brand URLs | 90+ sessions/90d |
| *(unsolvable)* | **Homepage** — no safe contains token exists; `/` matches everything | **~687** — the reason this mode is rejected |

**Do not filter out event *types* either** (if a later screen offers it): existing-patient
(EP) calls carry the access/ops signal (the "patients booking around the phone" finding
in `brand/current-state.md`), and online-booking (OB) events were 0-volume at audit —
Cardinal's roadmap wants OB go-live *visible*, and a filter would hide it.

---

## Step 3 — Confirm Filters

On the confirm screen, verify against this spec, and capture two things into the repo:

- [ ] Filters show **disabled** (or exactly the include lists above, with `Contains`
      match type on every entry — no accidental `Exact`).
- [ ] **Record the exact event names Liine says it will send** (expected to mirror the
      Liine action taxonomy from the paid-media audit: all-calls / first-time caller /
      NP lead call / NP booked / EP variants / OB online-scheduling) → add them to
      `audits/cardinal-recommendation-tracker.md` §4.
- [ ] Note any location the picker shows that this doc doesn't list (and vice versa —
      especially Rochester) → correct `brand/brand-brief.md`'s location roster.

## Step 4 — Acknowledge, then validate

Acknowledge = events start flowing from that moment. Same-day and day-7 checks:

1. **Same day:** GA4 Admin → DebugView / Realtime — Liine events arriving under the
   expected names.
2. **⚠️ PHI check (HIPAA + GA4 ToS — blocking):** inspect the event *parameters* in
   DebugView. **No caller names, phone numbers, or transcript fragments** may enter
   GA4. If any parameter carries identifying data, disable forwarding immediately and
   raise it with Liine support. (Same standard as `docs/data-sources-roadmap.md` §4:
   de-identified aggregates only.)
3. **Day 7:** Liine dashboard call count vs GA4 event count for the same window —
   investigate gaps >~5%.
4. **GA4 hygiene:** add a property annotation "Liine→GA4 events live" (go-live date
   matters for every before/after read); mark the **new-patient lead / booked / OB**
   events as key events. Do **not** key-event the all-calls action — at audit volumes
   (~740/30d in Ads) it would swamp `keyEvents` reporting.
5. **⚠️ Ads double-count guard:** Blue Ox (Shaun/Jake) already imports Liine
   conversions **directly into Google Ads**. The GA4-forwarded copies are for
   analysis only — tell Blue Ox they exist and must **not** also be imported to Ads
   as conversions, or Smart Bidding counts every call twice.

## What this unlocks (update the tracker when live)

- Landing page × **booked call** (not just intent click) — the organic booked-patient
  loop Cardinal's measurement framework requires, per page family and location.
- Channel truth: paid vs organic vs GBP share of *booked* new patients, using the same
  `?scct=` / `?y_source=` fingerprints documented above.
- Tracker §4 🟠 "GA4 conversion + call tracking live" gate → flips toward ✅ once
  events verify; `docs/data-sources-roadmap.md` Liine row gets a second, GA4-native path
  alongside the pending MCP.

**Owners:** Joe (Liine + GA4 admin, runs the wizard) · Santosh (validation, DebugView/PHI
check) · Blue Ox notified re: no Ads re-import · no website/dev change needed (Paul N/A).
