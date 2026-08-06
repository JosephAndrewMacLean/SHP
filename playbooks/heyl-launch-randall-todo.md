# Dr. Heyl Launch — Randall's Checklist

New pain-medicine physician. **Starts Sept 1.** Photo shoot Aug 10. Work top to bottom.

**The assets are written.** Drafts of the bio, pages, articles, emails, schema, referral sheets and
scripts are in **`assets/heyl-launch/`** — start at its `README.md`, which covers how to publish,
who has to review what, and the handful of things you have to create yourself.

*Why each item matters, with the data behind it: `heyl-launch-reference.md`. Task rows for the
PM sheet: `pm/heyl-launch-tasks.csv`.*

---

## 🚫 Three rules on everything you write

1. **"Board certified in PM&R, board eligible in Pain Medicine."** Never "board certified in Pain
   Medicine" — his exam is in September.
2. **His fellowship was in U-M's Department of Anesthesiology.** He is not an anesthesiologist.
3. **Never mention:** kyphoplasty · long-term opioid management · stem cell therapy · PRP.
   Don't call him a spinal cord stimulation specialist.

---

## This week (by Aug 5)

- [ ] **Send Dr. Heyl one email with 5 questions.** He owes answers by Aug 7 anyway:
  - What's your exact first day seeing patients?
  - Which locations/days are final, and how many new patients a week can you take?
  - Why did you go into pain medicine? *(needed for his bio — can't write it without this)*
  - How do you want to review drafts, and how fast can you turn them around?
  - What does a good first 90 days look like to you?
  - Plus: OK to mention Marine City and your Siena Heights baseball years publicly?
- [ ] **Send the photographer a shot list** for Aug 10: straight-on office portrait, a procedure
  shot, one vertical (9:16) clip, plus a square crop for directories. One shoot, all formats.
- [ ] **Ask him if he'd do one 90-second video** at the shoot. He said "ask me individually," so
  ask once. If it's a no, drop it.
- [ ] **Write the one-page rules sheet** (the three rules above, with approved wording) and send it
  to content, Kristen, Kelly, Blue Ox, and Cardinal.

## Before the shoot (by Aug 14)

- [ ] **Ask Operations, in writing:** what will actually be available on day one — nerve
  stimulation, EMG, PRP, ASC days? Only promote what they confirm.
- [ ] **Google his name.** Find every profile that already exists (Healthgrades, Vitals, Doximity,
  U-M, etc.). Claim them — don't create duplicates.
- [ ] **Claim his bio URL now: `/providers/jonathan-heyl-do/`.** Block every variant.
  ⚠️ *Oddo, Kevin Lee, and Singh each have two competing bio pages splitting their traffic. Singh's
  misspelled page outranks his real one. Free to prevent, painful to fix later.*
- [ ] **Map the pain-page URL mess** and send it to Cardinal/Paul. There are six different URL
  patterns for one service. Don't add a seventh.

## Rest of August

- [ ] **Write his bio.** Lead with the combination — rehab background *plus* pain fellowship, so he
  looks at what's limiting function, not just the pain score. 8th-grade reading level.
- [ ] Write his page title and description. Check it doesn't duplicate an existing one.
- [ ] **Spec his page's schema by hand.** Don't let it inherit the template — 446 markup errors are
  still open sitewide.
- [ ] **Make sure the CMS doesn't auto-link him to kyphoplasty or ketamine.** Both pages are live.
  Check in staging before publish.
- [ ] **Rewrite the main pain page** (`/treatment/pain-management/`). It gets ~9,900 searches shown
  and 50 clicks. Plain language, name the doctors, add "when to see a surgeon vs. a pain doctor."
- [ ] **Start rebuilding his procedure pages, 2–3 a week.** Easiest first:
  medial branch block → EMG → genicular nerve block → occipital nerve block → nerve blocks/PNS →
  RFA → SI joint → epidural injections.
- [ ] **Write the referral one-sheet** for Kristen's team — and say plainly *what not to send him*
  (widespread pain, fibromyalgia, heavy opioid cases). That's what makes referrers trust it.
- [ ] **Write the internal routing sheet** — when to send someone to Heyl vs. the surgeons vs. the
  pain doctors we already have. Otherwise he just takes their patients.
- [ ] **Give Kelly the phone rules:** evaluate first, never promise an injection, MRI, or
  medication before he's seen them.
- [ ] **Take a "before" snapshot** — current pain-page traffic, rankings, and what ChatGPT/Perplexity
  say today for "pain doctor Livonia." *Do this before Sept 1; you can't go back and get it.*

## Launch week (Sept 1)

- [ ] Bio live.
- [ ] Google Business listings live for **Livonia and Sterling Heights** (do it in the GBP screen —
  the API is still pending).
- [ ] Six directory profiles live: Healthgrades, Vitals, WebMD, Doximity, Zocdoc, NPI.
- [ ] Zero "Mendelson" references anywhere in his profiles.
- [ ] He's added to the Livonia and Sterling Heights location pages with real clinic days.
- [ ] **Test the booking path yourself, start to finish.** Website bookings are free and convert
  best — don't drive traffic to a broken path.
- [ ] Confirm his calls and bookings show up in Liine/GA4.
- [ ] **Sign him up for Rater8 reviews.** Starts at zero, compounds from day one.
- [ ] Announcement email to referring offices + press release to local media.
- [ ] Give Kristen the target list: his U-M and Ann Arbor contacts first. Jasmine can help map them.

## September–October

> **The content work shrank.** The Pain Management service line is gone, but its replacement —
> conditions and treatments — is already built, and **12 of his 13 procedures already have ranking
> pages.** Most of this is naming him on pages that exist, not writing new ones. See
> `assets/heyl-launch/26-semantic-model-mapping.md`; the data is in `27-heyl-treatment-map.csv`.

- [ ] **Add him as a performing provider on 12 existing `/treatment/` pages.** A data task, not a
  writing task. The list is in `27-heyl-treatment-map.csv`.
- [ ] **Ask Paul the three questions in `26-`** — is there a provider↔treatment link in the CMS, do
  condition pages link to treatments, and can the dead `/specialties/pain-management/` URLs be
  redirected. That's the whole dependency.
- [ ] **Build the two pages that genuinely don't exist:** genicular nerve block (5,400 searches,
  almost no competition) and peripheral nerve stimulation — his #1 priority and the thing he came
  here to build.
- [ ] **Cover neurogenic claudication where the model wants it** — a new "leg pain when walking"
  symptom page feeding the existing spinal stenosis page, rather than a third stenosis page.
  14,800 searches a month, and it fixes a duplicate on the way through. **Still the best single
  opportunity in this launch.**
- [ ] Article: **when to see a spine surgeon vs. a pain doctor** *(his idea, and it's the highest-value
  one — it also sends the right patients to the right door)*.
- [ ] Article: **what an EMG actually tells your doctor** — including whether it hurts and how long
  it takes. Lots of people ask; nobody local answers well.
- [ ] Add FAQ sections with proper markup to his pages. We have **zero** on the whole site today.
- [ ] Add him and his pages to `/llms.txt` so the AI tools can find him.
- [ ] Build a peripheral-nerve page. It's his #1 focus and we have nothing on it.
- [ ] Pitch neurology practices on migraine/occipital nerve blocks — nobody else courts them.
- [ ] Send Blue Ox a small, targeted ad brief — sized to his real capacity, with the do-not-advertise
  list attached.
- [ ] **After his September board exam:** update his bio, all six directories, schema, and every
  piece of collateral once certification is confirmed.
- [ ] **Sit down with him at 30, 60, and 90 days.** Is he seeing the patients he wanted? A full
  schedule of the wrong patients isn't a win.

---

## Waiting on other people

| Waiting for | Who | Blocks |
|---|---|---|
| 5 answers above | Dr. Heyl | His bio, the target list, the 90-day plan |
| What's live day one | Operations | Every procedure page and ad |
| Which insurance he takes | Credentialing | Phone screening |
| Is Troy happening? | Operations | A third Google listing (Troy is our biggest untapped area) |
| Boston Scientific patient-database idea | **Compliance — don't touch it yet** | — |

---

*Everything clinical here is a draft until Dr. Heyl and clinical review sign off. Nothing on this
list is cleared to publish on its own.*
