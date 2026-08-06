# URL lock — do this before anyone writes the bio

**Owner:** Randall, with Paul · **Due:** Aug 14 · **Takes:** about an hour

---

## The one rule

Dr. Heyl gets **exactly one** bio URL, forever:

```
https://synergyhealth.org/providers/jonathan-heyl-do/
```

## Why this is worth an hour

All three of our current interventional pain physicians have **two competing bio pages each**, and
Google splits their traffic between them:

| Physician | URL A | URL B |
|---|---|---|
| Anthony Oddo, DO | `/providers/anthony-oddo-do/` — 141 clicks, position 6.8 | `/providers/anthony-j-oddo-do/` — 112 clicks, position 5.2 |
| Kevin Lee, MD | `/providers/kevin-lee-md/` — 197 clicks, position 6.4 | `/providers/kevin-r-lee-md/` — 61 clicks, position 5.0 |
| Hanish Singh, MD | `/providers/hanish-singh-md/` — 79 clicks, position 7.5 | `/providers/hainish-singh-md/` — 52 clicks, **position 4.5** |

*(Google Search Console, 90 days ending 2026-07-28.)*

Look at the last row. **Dr. Singh's better-performing page is the one with his name misspelled.**
Every link, every mention, and every bit of authority those pages have earned is split in half.

There's a third pattern in circulation too — `/providers/pain-management/jason-mulawa-md/` — for a
physician who isn't on the current roster.

Preventing this costs an hour now. Fixing it later means redirects, lost rankings, and a
consolidation project.

---

## Checklist

- [ ] **Confirm the exact slug with Credentialing.** Is he "Jonathan Heyl" in every system? Any
      middle initial in use anywhere? Decide once. `jonathan-heyl-do` is the recommendation — it
      matches the majority pattern (`scott-mccarty-md`, `kyle-bohm-md`, `randy-leff-dpm`).
- [ ] **Create the page at the correct URL first**, before any copy goes in. Draft status is fine.
- [ ] **Check nothing already exists** at any variant. Search the CMS for "Heyl" and check for
      auto-created stubs.
- [ ] **Ask Paul to 301 these variants** to the canonical URL, and to keep the rule in place:
  - `/providers/jonathan-r-heyl-do/`
  - `/providers/jonathan-heyl-md/` *(wrong degree — he's a D.O.)*
  - `/providers/jon-heyl-do/`
  - `/providers/johnathan-heyl-do/` and `/providers/jonathon-heyl-do/` *(the two most likely
    misspellings — this is exactly how the Singh duplicate happened)*
  - `/providers/heyl-jonathan-do/`
  - `/providers/pain-management/jonathan-heyl-do/` *(the third pattern)*
- [ ] **Set the self-referencing canonical tag** on the page.
- [ ] **Ask Paul one systems question:** what created the existing duplicates? If the CMS spawns a
      second page when a provider's name or specialty is edited, this will happen again to the next
      hire regardless of what we do here. Get the cause fixed, not just this instance.
- [ ] **Give the canonical URL to everyone** before they need it: content, Kristen, Kelly,
      Blue Ox, the press-release draft, and every directory profile. A single wrong URL in a
      directory listing creates the exact split we're preventing.

## Verify after publishing

- [ ] Search Google for `site:synergyhealth.org heyl` — exactly one result.
- [ ] Every variant above returns a 301 to the canonical URL, not a 404 and not a live page.
- [ ] Search Console shows one URL accumulating impressions, not two.
- [ ] **Re-check at 30 and 90 days.** Duplicates usually appear after launch, when someone edits the
      page or adds him to a new specialty.

---

## Worth raising separately with Joe

The Oddo, Lee, and Singh duplicates are live right now and costing traffic today. Consolidating them
is a small job — pick the better-performing URL, 301 the other, update internal links — and it would
lift three physicians who are already ranking. It sits outside this launch, but this is the moment
we have the evidence in hand. Suggest it as a follow-on task.
