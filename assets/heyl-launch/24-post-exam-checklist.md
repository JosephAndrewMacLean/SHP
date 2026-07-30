# After the September board exam — update everything

**Trigger:** written confirmation from Credentialing that Dr. Heyl has passed the Pain Medicine
board examination
**Owner:** Randall · **Set the reminder now for Oct 1**

---

## Why this needs a checklist

Right now, every asset says **"board eligible in Pain Medicine."** That's correct today and will be
wrong the moment he's certified.

**Nothing updates itself.** Not the schema, not the directory profiles, not the printed one-sheets,
not the ad copy. If this isn't worked through deliberately, we'll be understating a physician's
credentials on twenty properties for years — which is its own kind of inaccuracy, and it's the kind
physicians notice.

**Don't start until Credentialing confirms in writing.** Not when he says he thinks it went well,
not when results are expected. Written confirmation.

---

## The list

### Website
- [ ] Bio page — credentials section
- [ ] Bio page — meta description, if it mentions certification
- [ ] `07-physician-schema.json` — update the `hasCredential` block; add the Pain Medicine board
      certification with the certifying body
- [ ] Re-validate schema at `search.google.com/test/rich-results`
- [ ] Pain management service page, if it lists his credentials
- [ ] Any procedure page naming him
- [ ] Both location pages
- [ ] Articles with an author or reviewer credit — check every one published since September

### Directory profiles *(each has its own certification field)*
- [ ] Google Business Profile — Livonia
- [ ] Google Business Profile — Sterling Heights
- [ ] Healthgrades
- [ ] Vitals
- [ ] WebMD
- [ ] Doximity
- [ ] Zocdoc, if in use
- [ ] NPI registry — check whether the taxonomy code changes
- [ ] IPSIS, NASS, AAPM&R listings
- [ ] Any profile found and claimed during the `10-` audit

### Print and collateral
- [ ] Referral one-sheet — **needs reprinting.** Check how many are in circulation and get them
      swapped; an outdated one-sheet in a referring office outlives the file on our server
- [ ] Any leave-behind Kristen's team is carrying
- [ ] Presentation or event materials

### Paid
- [ ] Ad copy — tell Blue Ox. "Board certified in pain medicine" becomes available and is worth
      testing as a headline
- [ ] Any landing page copy

### Internal
- [ ] `04-provider-record.md` — update and bump the version
- [ ] `03-messaging-guardrails.md` — Rule 1 changes; redistribute
- [ ] Call-center script — what the phones say about his credentials
- [ ] Internal routing sheet
- [ ] `20-call-center-rules.md`

### Announce it
- [ ] Note it in the referral newsletter or the next liaison round — it's a legitimate, small piece
      of good news for referring offices
- [ ] LinkedIn / owned social
- [ ] Not worth a press release on its own

---

## Verify when done

- [ ] Search his name and check the top ten results for stale "board eligible" wording
- [ ] Check every directory profile visually — some have more than one certification field
- [ ] Confirm the schema validates and shows the new credential
- [ ] Ask Credentialing to confirm the certifying body's exact name for the schema entry

---

## If he doesn't pass, or defers

It happens, and it isn't unusual. Change nothing, say nothing publicly, and keep "board eligible" —
which remains accurate. Reset the reminder for the next exam window and tell no one outside the
people who need to know. Handle it quietly and without commentary.

---

## While you're doing this

This is a good moment to re-run two checks:

- **`08-url-lock.md`** — has a duplicate bio URL appeared? They usually show up after launch, when
  someone edits the page or adds a specialty.
- **`09-taxonomy-firewall-check.md`** — has he been auto-associated with kyphoplasty, ketamine, or
  anything else outside his scope since publish?

Both take ten minutes and both catch the kind of drift nobody notices until it's been live for
months.
