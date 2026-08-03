# To-do for Randall (SEO) — MIS foot surgery quick wins (2026-08-03)

> Ready-to-send draft (email or Slack). Scope: **only items Randall can finish solo
> this week** with WP/Rank Math + GSC + Semrush access — no dev work, no content
> writing, no approvals needed. Context: Dr. Leff emailed today asking why patients
> searching MIS foot surgery can't find us (he's right — data below), Paul just
> updated the site nav, and the full plan lives in
> `playbooks/mis-foot-surgery-leff-plan.md` (skim §1, §4, §6 — 10 min).
> Every number below: GSC/GA4/Semrush, pulled 2026-08-03, window May 1–Jul 31.

**Total: 8 items, ~2.5 hours. Done = each item's "done" line.**

---

## ⭐ TL;DR — the three that matter most

1. **Eyes-on check of Paul's nav change** (you can see the site; our tooling is
   Cloudflare-walled) — screenshot + where the new links point.
2. **Paste in 4 title/meta rewrites** (copy provided) — these pages earn ~9,200
   impressions/quarter and capture almost nothing.
3. **Set 5 safe 301s** (map provided) — bunion content is split across duplicate
   URLs that are diluting each other.

---

## 1. Eyes-on: verify the nav update (10 min, any browser)

Cloudflare's bot challenge blocks all our monitoring tools from rendering the site
(Googlebot is fine — verified today). You have a normal browser, so you're the
fastest instrument we've got:

- Open synergyhealth.org → Services/specialties menu. Does **Foot & Ankle** now
  appear? Screenshot the open menu.
- List the exact URL each new foot/ankle link points to (right-click → copy link).
- Note whether any **new** page/URL was created for this, or links point at
  existing pages.

**Done =** screenshot + link list posted to Joe. (Why it matters: if the new nav
points at the weak duplicate pages, we'll want to re-point it at the canonical ones
below — that's a 2-min follow-up, not a rebuild.)

## 2. Check WordPress for orphan MIS drafts (5 min)

WP admin → Pages + Posts → search "minimally invasive". We believe **no MIS foot
page exists** (zero MIS-query impressions in GSC; nothing in Semrush top-100). Just
confirm nothing sits in drafts so the new-page URLs (coming from the content
workstream) start clean.

**Done =** yes/no to Joe.

## 3. Title/meta rewrites — paste these four (30 min, Rank Math)

These pages already earn impressions but their snippets don't sell the click.
Paste, save, then GSC → URL Inspection → **Request indexing** on each.

| Page | Today | New title | New meta description |
|---|---|---|---|
| `/specialty/foot-ankle-specialists/` | pos 24.5 · 2,471 impr · 13 clicks | Foot & Ankle Specialists in Metro Detroit \| Synergy Health Partners | Five foot & ankle doctors treating bunions, hammertoes, heel pain, and ankle injuries — including minimally invasive options. Same-week appointments, 8 locations. |
| `/treatment/bunionectomy/` | 1,805 impr · 1 click (0.06% CTR) | Bunion Surgery (Bunionectomy): Options & Recovery \| Synergy Health Partners | Compare bunion surgery options, what recovery typically looks like, and when surgery makes sense. Foot & ankle surgeons in metro Detroit, same-week appointments. |
| `/conditions/bunions/` | 1,305 impr · 1 click | Bunions: Symptoms, Causes & Treatment Options \| Synergy Health Partners | What bunions are, why they form, and treatment options from orthotics to minimally invasive surgery — explained in plain language by our foot & ankle team. |
| `/treatment/ankle-arthroscopy/` | 3,488 impr · **0 clicks** | Ankle Arthroscopy: What It Treats & What to Expect \| Synergy Health Partners | How ankle arthroscopy works, the conditions it treats, and typical recovery timelines, from the foot & ankle team at Synergy Health Partners in metro Detroit. |

(Wording is compliance-checked: no guarantees, no "best/only," recovery framed as
"typical." Tweak for length if Rank Math flags >60/160 chars, but keep those rules.)

**Done =** all four live + indexing requested.

## 4. Five safe 301s (20 min, Rank Math → Redirections)

Exact duplicates only — every target already exists and wins on data. If you don't
have the Redirections module, forward this table to Paul as-is.

| Redirect this | → To | Why |
|---|---|---|
| `/bunion-pain/` | `/conditions/bunions/` | orphan blog dupe (56 impr, pos 29) |
| `/bunion-relief/` | `/conditions/bunions/` | orphan blog dupe (17 impr) |
| `/conditions-we-treat/foot-ankle-conditions/bunions/` | `/conditions/bunions/` | legacy-structure dupe |
| `/self-pay-options/foot-ankle/` | `/insurance-billing/self-pay-foot-ankle/` | dupe; insurance-billing version has the traffic |
| `/treatment/toe-joint-replacement/` | `/treatment/toe-arthroplasty/` | same procedure, two URLs; arthroplasty holds the GSC impressions (605/quarter) |

**Done =** each old URL returns 301 to its target (check in browser or
httpstatus.io); watch GSC coverage for a week for surprises.

## 5. Internal links between the foot pages that rank (30 min, WP editor)

Today these pages barely reference each other. Add in-body contextual links:

- `/conditions/bunions/` → link "bunion surgery options" to `/treatment/bunionectomy/`,
  and "minimally invasive forefoot reconstruction with Randy Leff, DPM" to
  `/providers/randy-leff-dpm/`.
- `/treatment/bunionectomy/` → link back to `/conditions/bunions/` ("what bunions
  are") and to `/providers/randy-leff-dpm/`.
- `/specialty/foot-ankle-specialists/` → add a short "Conditions & procedures" block
  linking bunions, bunionectomy, ankle arthroscopy, and Dr. Leff's bio.
- Southfield location page (if the template allows body edits) → one line linking
  the foot & ankle specialty page.

**Done =** links live. (Dr. Leff's bio is our strongest foot page — 267 clicks,
position 5.8 — this routes its authority into the procedure pages and vice versa.)

## 6. Add the foot keyword set to Semrush position tracking (15 min)

Project **"SHP Spine 2026" (ID 30453033)** → position tracking → new tag/group
"Foot-MIS" → paste:

```
minimally invasive foot surgery
minimally invasive bunion surgery
minimally invasive bunion surgery near me
minimally invasive hammertoe surgery
keyhole bunion surgery
3d bunion correction
lapiplasty
bunion surgery
bunionectomy
bunion surgery near me
bunion doctor near me
hammer toe surgery
foot surgeon near me
podiatrist near me
podiatrist southfield
tailors bunion surgery
```

Set/keep tracking geo on metro Detroit if the campaign supports it.

**Done =** group reporting in the next weekly snapshot.

## 7. Save the monthly GSC tripwire (5 min)

GSC → Performance → Query filter (regex):
`minimally invasive|keyhole|percutaneous|mis bunion|3d bunion` — bookmark it.
**Baseline today ≈ 2 impressions/month.** That number is the whole scoreboard for
this project: it should hit ≥150/mo within a month of the MIS pages publishing.

**Done =** bookmarked; first re-check logged ~Sep 1.

## 8. Inventory the legacy foot directory (30 min, spreadsheet)

List every URL under `/conditions-we-treat/foot-ankle-conditions/` (crawl or WP
page list) and mark which have a `/conditions/` twin (merge candidates) vs. which
have **no** modern equivalent (do NOT redirect those — they need a home first).
Hand the sheet to Joe → Paul/Cardinal for the bulk-301 batch.

**Done =** sheet shared. (This is the foot version of the carpal-tunnel/TKA URL
cleanup Cardinal already recommends — we're feeding their machine, not forking it.)

---

**Explicitly NOT on your list** (so this stays a one-week win): schema (Paul +
Cardinal own the pipeline), writing the new MIS hub/pages (content team, gated on
Dr. Leff's credential session), GBP edits (listings owner), Cloudflare/WAF (Paul).
