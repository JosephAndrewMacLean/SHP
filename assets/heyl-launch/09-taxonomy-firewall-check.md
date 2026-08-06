# Pre-publish compliance check — run this before the bio goes live

**Owner:** Randall · **Due:** Aug 21, and again the morning of publish · **Takes:** 20 minutes

> This is the check that stops a compliance problem, not a marketing one. Run it in staging, then
> run it again on the live page after publishing.

---

## What we're preventing

Dr. Heyl asked us never to associate him with **kyphoplasty**, **long-term opioid management**, or
**stem cell therapy**, and to hold **PRP** until the workflow is approved.

Relevant pages already live on our site:

- **`/treatment/kyphoplasty-vertebroplasty/` — 8,377 impressions in 90 days** ← the live one, check this first
- `/specialties/pain-management/kyphoplasty/` — 169 impressions *(deprecated, still indexed)*
- `/specialties/pain-management/ketamine-infusion/` — 159 impressions *(deprecated; no `/treatment/`
  equivalent found — confirm with Clinical whether the service is still offered)*

> **Corrected 2026-07-30.** The kyphoplasty page migrated to `/treatment/` and the live version is
> ~50× larger than the deprecated one. Check both, but the `/treatment/` URL is the one that matters.

If the CMS attaches him to the "Pain Management" specialty and that specialty auto-lists its
procedures, or auto-inserts a "Providers who perform this" block, **he inherits both pages without
anyone choosing to put him there.** That's a credentialing-accuracy problem and it breaks a
commitment we made to him in writing.

---

## The check

### In staging, before publish

- [ ] Open his bio. Does any auto-generated block list procedures we didn't write ourselves? If yes,
      **turn the block off** and use the hand-written list from `06-bio-page.md`.
- [ ] Open `/specialties/pain-management/kyphoplasty/`. Does Dr. Heyl appear anywhere on it — a
      provider list, a sidebar, a "book with" link, a related-providers block?
- [ ] Same check on `/specialties/pain-management/ketamine-infusion/`.
- [ ] Same check on any opioid-management or medication-management page. Search the CMS for "opioid".
- [ ] Same check on any PRP, stem cell, or regenerative-medicine page. **PRP is a hold, not a never —
      but not at launch.**
- [ ] Open the Pain Management specialty landing page. If it lists providers, confirm his entry
      doesn't inherit the full procedure taxonomy.
- [ ] Check the `availableService` list in his schema against `04-provider-record.md`. Nothing from
      the never-list. Nothing Operations hasn't confirmed.

### After publishing

- [ ] Repeat all of the above on the live page. Staging and production don't always render the same
      blocks.
- [ ] Search Google for `site:synergyhealth.org heyl kyphoplasty` — should return nothing.
- [ ] Ask Paul directly: **does adding a provider to a specialty automatically link them to every
      procedure in that specialty?** If yes, that's a systems problem affecting all 42 physicians and
      needs its own ticket.

### Ongoing

- [ ] **Re-run this whole check whenever** a new procedure page is added to Pain Management, his
      specialty assignment is edited, the provider template changes, or a bulk CMS update runs.
- [ ] Add it to the 30-day and 90-day review.

---

## If he does turn up somewhere he shouldn't

1. Remove the association immediately — don't wait for the next release.
2. Tell Joe the same day.
3. Note it in `04-provider-record.md`.
4. Work out how it happened. If it was automatic, it will happen again.

## While you're in there

The same auto-association question applies to the physicians already on the site. If the template
does this by default, some of our 42 providers may currently be listed for procedures they don't
perform. Worth flagging to Joe as a separate audit — not part of this launch, but this check is how
we'd find out.
