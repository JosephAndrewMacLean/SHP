# Content Update Workflow — how site changes happen from now on

**Why this exists (Jul 20–21 meetings):** updating pages one at a time through a chat window,
with no sitewide context, was measurably hurting the site — pages optimized in isolation drift
onto each other's queries and trade rankings instead of rising (evidence:
`gsc-analysis-2026-07.md`, cannibalization section). Paul's summary stands: a GPT fed one page
"doesn't know all the other pages." This workflow replaces that method.

## 1. The rules

1. **No single-page, no-context edits. Ever.** Every content change is drafted inside this
   workspace, where the cluster map, brand guardrails, and current GSC data are loaded — or
   through Paul's backend content system, which carries the sitewide config. Never a bare chat
   window with one page pasted in. (Claude subscription/account for the backend plugin: being
   moved to Joe's account — decided Jul 21.)
2. **Changes ship in weekly batches, not dribbles.** One batch = one theme (e.g., "title/meta
   wave 1," "stenosis hub rebuild"), logged in `seo/change-log.md` with date + URLs + what
   changed, and annotated in GSC the same day. If everything changes at once, nothing can be
   attributed.
3. **Every page belongs to the cluster map** (`spine-content-cluster-map.md`). If a proposed
   page/edit isn't on the map, the map gets updated first — that's where cannibalization is
   caught (one primary URL per topic; siblings link, never duplicate).
4. **Decisions run on GSC data, not SEMrush** (meeting decision). Monthly export → analyze →
   compare → choose the next batch. Paul's plugin gap-analysis view is a prompt source;
   the dated export in `seo/data/` is the record.
5. **Change → wait → measure → then touch again.** Titles/metas: read at 2 and 4 weeks.
   Content/structure: 4–8 weeks. Consolidations/redirects: sequenced after title waves so
   effects are separable. Resist the urge to re-edit inside the waiting window.
6. **Compliance gates are blocking** (brand brief): clinical claims need a named physician
   reviewer + date; no PHI; no guarantees/superiority claims; accessibility; anything clinical
   or legal is a draft until a human clears it. AI-drafted copy is always labeled as draft.
7. **Stay out of the agencies' lanes, hand them ammo:** Power Digital/Cardinal own technical
   SEO (schema, CWV, redirects/canonicals, llms.txt). We hand them the primary-URL list
   (cluster map §4) and the mobile bug (§6) — we don't ship competing technical fixes.

## 2. Who does what

| Person | Role in this loop |
|---|---|
| **Randall** | Runs the loop: monthly export, batch drafting in this workspace, Rank Math implementation, change log, 80% of effort on spine |
| **Joe** | Owns strategy + this repo; approves batches; owns the CEO expectations conversation; account holder for the backend Claude config |
| **Paul** | Backend content system + GSC dashboard/gap analysis; mobile-render bug (§6); technical sanity check on consolidations |
| **Cardinal/PD** | Technical execution (redirects, schema, CWV) fed by our lists |
| **Medical reviewers** | Named physician per clinical page — blocking gate before publish |

## 3. The monthly loop (repeatable)

1. GSC → Performance → Export (same scope: Web, 16 months) → drop CSVs into
   `seo/data/YYYY-MM-DD/` → run `seo/data/analyze_gsc.py` (paths at top of script).
2. Compare vs. prior month: spine non-branded (queries/impr/CTR/pos) · ortho tripwire
   (>15% non-branded click drop ×2 months = pause and diagnose) · CTR deltas on changed pages ·
   new-page indexing/positions.
3. Pick next batch from the cluster-map roadmap (§9) + fresh striking-distance list.
4. Draft in workspace → human/medical review → implement → log + annotate.

## 4. Change log discipline

Every batch appends to `seo/change-log.md`: date · batch name · URLs touched · what changed ·
expected effect · review-by date. GSC annotations mirror it. This is what makes "did it work?"
answerable in the CEO conversation — and what proves marketing's contribution against Liine
booked-call data once its tracking is validated.

## 5. What we do NOT do (each one burned us or will)

- ❌ One-page GPT edits with no cluster context (the original sin this replaces)
- ❌ New URLs for topics that already have a primary (check map §4 first)
- ❌ Doorway pages for suburbs without clinics; canonicals pointing city pages at other cities
- ❌ Bulk AI-publish without named medical review (E-E-A-T/YMYL + brand risk)
- ❌ SEMrush-driven decisions; ❌ redirecting the legacy Sterling Heights / Port Huron URLs
  before replacements demonstrably hold their rankings
- ❌ Touching ortho architecture, provider pages' structure, or the high-earning legacy blogs
  (title/meta polish only)
- ❌ Promising speed ("same-week") anywhere scheduling can't deliver it — top sentiment risk

## 6. Open technical ticket — desktop/mobile content mismatch (the original issue)

Symptom: updated content appeared on desktop but not mobile. This is a **rendering/caching bug,
not an SEO-strategy issue** — most likely a stale mobile cache variant (page cache/CDN serving
device-split HTML) or a mobile-specific template/element not receiving the update. Why it still
matters for SEO: **Google indexes mobile-first** — if mobile HTML is stale, Google ranks the
stale version; and mobile is where SHP's local intent lives (mobile pos 12.8 vs desktop 28.7).

Triage for Paul (in order): purge page cache/CDN and re-check on a real phone (not just
responsive dev-tools) → confirm whether the cache layer stores separate mobile/desktop variants →
check the page builder/plugin for device-conditional sections → verify with GSC URL Inspection
("view crawled page" rendered HTML) that Google sees the updated mobile content. Log the root
cause here when found; until fixed, every content batch gets a mobile spot-check before being
marked shipped.

## 7. Expectations line (for leadership, verbatim-usable)

Titles/metas move clicks in 2–4 weeks. New cluster content takes 3–6 months to rank on a
31.8-authority domain. Site-level movement is a 6–9 month arc. Clicks are a proxy — the real
KPI is Liine-qualified spine calls/bookings, which also depends on the phone/booking fixes in
`playbooks/spine-90day-plan.md`. SEO fills the funnel; it doesn't answer the phone.
