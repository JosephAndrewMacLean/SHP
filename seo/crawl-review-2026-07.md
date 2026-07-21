# Crawl Review — internal_html.csv (Screaming Frog, crawled Jul 15, 2026)

**What was reviewed:** 420 HTML URLs from a crawl of the live site (392×200, 20×301, 8×404).
**Asked:** "review this and make sure to remove the 301 redirects."
**Answer in one line:** **no redirect *rules* should be removed — every 301 in this crawl is
doing a correct job. What gets removed is the ~3,900 internal-link hops *through* them:
six template link fixes eliminate nearly all of it.** Details and the bigger findings below.

---

## 1. The context this crawl reveals (changes how we read everything else)

**The site has already migrated to the new URL structure.** The crawl contains only
`/conditions/ · /treatment/ · /specialty/ · /providers/ · /locations/` — the legacy
`/specialties/`, `/conditions-we-treat/`, `/full-service-clinics/`, `/our-providers/`,
`/contact-us/`, `/mri/` structures are no longer linked anywhere on the site. The GSC
16-month data blends pre- and post-migration history, which is why our Wave-1 list included
legacy URLs. The AI-features data (which showed Google citing the new structure 315:1)
now makes complete sense: **the new structure isn't a preference — it's the live site.**

**⚠️ Warning signal:** July clicks are pacing ~110/day vs ~148/day in June (**−26%**), and
AI-feature impressions dipped after mid-June. That pattern is consistent with a migration
cutover where some legacy URLs lost their redirect coverage. Verification is Priority 0 (§5).

## 2. The 20 × 301s — triage (what "remove" correctly means)

**KEEP the redirect rules — all four kinds are correct:**
| Kind | Examples | Verdict |
|---|---|---|
| Filter-URL → clean URL | `/locations/?location_type=imaging-mri` → `/locations-type/imaging-mri/` | Correct behavior |
| Slash/typo normalization | `/providers`→`/providers/` · `/treatment/physical-therapy/%20` (trailing space) → clean | Correct; fix the links |
| Old slug → new slug | `/specialty/spine/`→`/specialty/spine-neck-back/` · `/what-hurts/*`→`/specialty/*` · `/specialty/foot-ankle/`→`…-specialists/` | Correct; preserves equity |
| Legacy blog → money page | `/how-do-i-know-if-i-need-knee-replacement-surgery/` and `/hip-knee-replacement/` → `/treatment/total-knee-arthroplasty-tka/` | Correct; TKA consolidation already done — keep |

**REMOVE the hops — fix these internal links (one template edit each, sitewide effect):**
| Link currently pointing at | Should point at | Hops removed |
|---|---|---|
| `/locations/?location_type=imaging-mri` (nav) | `/locations-type/imaging-mri/` | 784 |
| `/what-hurts/hand-wrist/` (nav) | `/specialty/hand-wrist/` | 784 |
| `/specialty/foot-ankle/` (nav) | `/specialty/foot-ankle-specialists/` | 410 |
| `/what-hurts/shoulder-elbow/` (nav) | `/specialty/shoulder-elbow/` | 392 |
| `/services/` (template) | `/treatment/` | 392 |
| `/treatment/physical-therapy/ ` (trailing space in href) | `/treatment/physical-therapy/` | 392 |
| `/specialty/spine/…` (content links, 3 variants) | `/specialty/spine-neck-back/` | 32 |
| Legacy TKA blog links (content) | `/treatment/total-knee-arthroplasty-tka/` | 30 |

One oddity to hand Paul: `/specialty/orthopedics/` redirects to
`/specialty/orthopedic-services/?post_type=specialty` — a redirect **target** carrying a query
string. Point it at the clean `/specialty/orthopedic-services/` instead.

## 3. The 404s the crawl caught (these DO need fixing)

| URL | Inlinks | What it is |
|---|---|---|
| `/?page_id=20` | **392 — sitewide template link to a deleted page.** Find the nav/footer element and fix or remove. | Priority |
| `/specialty/pain-management/?post_type=treatment` | 4 | **Pain management specialty page missing/404** — a whole service line unreachable from nav |
| `/insurance-billing/insurance-information/` | 6 | Broken link → point at `/insurance-billing/insurance-accepted/` |
| `/patient-center/pay-my-bill/` | 1 | Bill-pay 404 — ties to the unfinished `payment.mendelsonortho.com` rebrand item |
| `/appointments` | 1 | Point at `/book-an-appointment/` |
| `/cdn-cgi/l/email-protection` | 395 | Cloudflare email-cloak pseudo-URL — ignore, normal |

## 4. Title/meta reality on the LIVE site (this reshapes Wave 1)

The migration already shipped **good titles/metas on the new spine pages** (e.g.
`/conditions/spinal-stenosis/` "Spinal Stenosis Treatment Michigan | Synergy Health Partners",
`/specialty/spine-neck-back/` "Spine, Neck & Back Specialists Michigan…", `/providers/`
"Find an Orthopedic or Spine Doctor Near You" — essentially our approved drafts, already live).
The real, current title/meta problems are template bugs:

- **38 pages titled "… | Page Synergy Health"** — the Rank Math title template for the "Page"
  post type is printing the literal post-type name. One template fix cures all 38 (contact,
  booking ×9, insurance pages, HIPAA, first-visit, patient forms, disclaimer…).
- **11 pages with page-builder debris as meta descriptions** ("hero gradient breadcrumb…"):
  contact-us, your-first-visit, insurance-accepted, learning-hub, self-pay, why-synergy-health,
  patient-testimonials, HIPAA, medical-records, privacy ×2. Template pulls raw builder text —
  fix the template, then handwrite metas for the money pages (contact, insurance, learning hub, self-pay).
- **4 `/locations-type/` pages share the locations-index title** ("12 Orthopedic & Spine Clinic
  Locations…"): imaging-mri, auto-accident-care, surgical-centers, full-service-clinics. Each
  is self-canonical and indexable → each needs its own title (e.g. "Open MRI & Imaging
  Locations — Metro Detroit | Synergy"). These map directly to GSC demand (open MRI queries
  are the site's best non-branded performers; auto-accident is the high-value PIP channel).
- `/locations/genesys-surgery-center/` shows the same bug pattern: "… | **Location** Synergy Health".
- The 32 `/locations/?provider_id=…` variants all canonical to `/locations/` — **fine, no action**.
- `/locations/synergy-surgery-center/` is titled "**Warren Orthopedic Clinic**" — the ASC
  wearing the clinic label. Warren demand exists (2.7K impr) but this is mislabeling, not a
  clinic page. Needs a naming decision (see §6).

## 5. PRIORITY 0 — verify legacy redirect coverage (Paul + Randall, 15 minutes)

I could not test live URLs from this environment (network policy blocks the domain), so this
is the first manual check. For each high-equity legacy URL, load it and record: **301 to the
right new page / 301 to wrong page / 404.** Any 404 or wrong target = report to Paul same day;
July's −26% click pace makes this urgent. *(These are migration-hygiene redirects owned by
Paul — distinct from the gated consolidation work; nobody on our side ships redirects.)*

| Legacy URL (16-mo GSC equity) | Expected live target |
|---|---|
| `/specialties/spine-back-and-neck/lumbar-laminectomy/` (87K impr) | `/treatment/lumbar-laminectomy/` |
| `/specialties/spine-back-and-neck/cervical-fusion/` (80K impr) | `/treatment/lumbar-cervical-fusion/` (no dedicated page yet) |
| `/specialties/spine-back-and-neck/anterior-cervical-discectomy-fusion/` (14.6K + "acdf" pos 3) | nearest: `/treatment/lumbar-cervical-fusion/` — ACDF page still needs building |
| `/specialties/spine-back-and-neck/` (66.5K) | `/specialty/spine-neck-back/` |
| `/conditions-we-treat/spine-neck-back-conditions/*` (5 hubs) | `/conditions/<condition>/` |
| `/contact-us/` (129K) | `/get-involved/contact-us/` |
| `/our-providers/` (125K) | `/providers/` |
| `/locations/clinic-locations/` (118K) + `/locations/` legacy children | `/locations/` + city pages |
| `/full-service-clinics/sterling-heights-2/` (94K) | `/locations/sterling-heights/` |
| `/full-service-clinics/port-huron/` (41K) | `/locations/port-huron/` |
| `/mri/` (84K, best CTR on the site) | `/locations-type/imaging-mri/` |
| `/specialties/physical-therapy/lymphedema-management/` (222K impr) | **no equivalent exists — content gap, see §6** |
| `/specialties/hand-upper-extremity/finger-amputation/` (60K) | `/treatment/finger-amputation-surgery/` |
| `/specialties/occupational-therapy/hand-therapy/` (66K) | `/treatment/hand-therapy/` |
| Blog posts: `/flying-with-joint-replacement/` (123K) · `/6-tests…shoulder…/` (145K, still linked) · `/5-common-causes-of-hip-pain/` | live but likely **orphaned** — confirm + add learning-hub links |

## 6. Gaps the crawl exposed (add to the build queue)

1. **No ACDF page** on the new site — 21K impressions of "acdf" demand rank on a legacy URL. The Week-2 ACDF build now targets a NEW `/treatment/` URL (per plan).
2. **No lymphedema page** — the site's 2nd-largest impression topic (222K) has no home. Decide: rebuild under `/treatment/` or let it go deliberately (it's PT-line, non-priority — but 222K impressions shouldn't die by accident).
3. **Rochester is missing entirely** from `/locations/` (6 cities + 2 ASCs live; brand docs say 8 locations). Confirm clinic status; restore the page if open.
4. **Warren**: real demand, no clinic page — only the mislabeled ASC. Decide the story (ASC page titled honestly + Warren served-area on Sterling Heights, or a true Warren page if there's a clinic).
5. **Duplicate history pages**: `/about-us/our-history/` AND `/about-us/company-history/` both live — pick one (company-history holds the Mendelson rankings; 86K impr), canonical/redirect the other (Paul's list, gated as usual).
6. `/treatment/disc-replacement-surgery/` already exists — Week-3 ACDR work lands there (rename/scope check first).
7. Spine-at-location pages don't exist yet (matches plan — Troy first).

## 7. What this does to Wave 1 (revised priorities, same discipline)

The approved-draft copy still applies, but the target list changes — several drafts are
already live on new URLs, and the template bugs are bigger wins than re-titling pages that
migrated well. **Wave 1R, in order:**
1. **Template fixes (Paul/Randall, biggest single win):** the "| Page" title template bug
   (38 pages) + the debris-meta template bug (11 pages). Two template edits + handwritten
   metas for contact / insurance-accepted / learning-hub / self-pay.
2. **4 `/locations-type/` titles** + Genesys title (5 unique titles, high local value).
3. **Internal-link fixes** (§2 table) + **404 fixes** (§3) — kills every crawlable 301 hop and broken link.
4. **Priority-0 legacy verification** (§5) — same day, before anything else ships.
5. Original Wave-1 rows that survive on live URLs (contact via `/get-involved/contact-us/`,
   location pages, back/neck fracture reviewer+banner work) — per the Studio, after the URL check.

Everything still ships as one logged batch → change-log → GSC annotation → 14-day freeze.
