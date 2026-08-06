# Dr. Heyl Launch — Randall's Checklist

New pain-medicine physician. **Starts Sept 1.** Photo shoot Aug 10. Work top to bottom.

**The assets are written.** Drafts of the bio, pages, articles, emails, schema, referral sheets and
scripts are in **`assets/heyl-launch/`** — start at its `README.md`, which covers how to publish,
who has to review what, and the handful of things you have to create yourself.

> **Updated 2026-07-30 for the semantic model.** The Pain Management service line is gone, but its
> replacement — conditions and treatments — is already live, and **12 of his 13 procedures already
> have ranking pages.** Most of the content work is naming him on pages that exist rather than
> writing new ones. Background: `assets/heyl-launch/26-semantic-model-mapping.md`. The data:
> `27-heyl-treatment-map.csv`.

*Why each item matters, with the numbers: `heyl-launch-reference.md`. Task rows for the PM sheet:
`pm/heyl-launch-tasks.csv`.*

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
- [ ] **Ask Paul three questions.** These gate all of the September work, so ask now:
  1. Can a provider be linked to a treatment in the CMS? *(If not, that's the one thing worth
     building — it makes every future physician launch trivial.)*
  2. Do condition pages already link to their treatments?
  3. Can the dead `/specialties/pain-management/` URLs be redirected? Map is in `27-`.

## Before the shoot (by Aug 14)

- [ ] **Ask Operations, in writing:** what will actually be available on day one — nerve
  stimulation, EMG, PRP, ASC days? Only promote what they confirm.
- [ ] **Google his name.** Find every profile that already exists (Healthgrades, Vitals, Doximity,
  U-M, etc.). Claim them — don't create duplicates.
- [ ] **Claim his bio URL now: `/providers/jonathan-heyl-do/`.** Block every variant.
  ⚠️ *Oddo, Kevin Lee, and Singh each have two competing bio pages splitting their traffic. Singh's
  misspelled page outranks his real one. Free to prevent, painful to fix later.*
- [ ] **Send Paul the redirect map** from `27-heyl-treatment-map.csv` — 12 dead
  `/specialties/pain-management/` URLs pointing to their live `/treatment/` equivalents. One of them
  still ranks at position 6.0, so flag that one to redirect carefully and watch it.

## Rest of August

- [ ] **Write his bio.** Lead with the combination — rehab background *plus* pain fellowship, so he
  looks at what's limiting function, not just the pain score. 8th-grade reading level.
- [ ] Write his page title and description. Check it doesn't duplicate an existing one.
- [ ] **Spec his page's schema by hand.** Don't let it inherit the template — 446 markup errors are
  still open sitewide.
- [ ] **Check the CMS doesn't auto-link him to kyphoplasty or ketamine.** The live one is
  `/treatment/kyphoplasty-vertebroplasty/` (8,377 impressions). Check in staging before publish.
- [ ] **Reframe the old pain page** (`/treatment/pain-management/`) as a **router**, not a
  department. Keep the URL and its ~9,900 impressions; change it from "here's our department" to
  "here's what hurts → the condition → the treatment → who does it." Drop the physician roster —
  doctors attach to treatments now.
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
- [ ] **Name him on the 12 existing `/treatment/` pages.** This is the launch — those pages already
  carry 44,264 searches shown between them. It's a data task, not a writing task. List in `27-`.
- [ ] **Name him on the condition pages he treats** — sciatica, stenosis, radiculopathy, SI joint,
  and the rest. Also in `27-`. The condition pages already link to the treatments, so this is what
  makes him findable by what hurts.
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

**Only two pages genuinely don't exist. Build those, improve three weak ones, then write.**

- [ ] **Build: genicular nerve block.** 5,400 searches a month, almost no competition, and no page
  anywhere on the site.
- [ ] **Build: peripheral nerve stimulation.** His #1 priority and the thing he came here to build.
  Include the temporary 60-day system if Operations confirms it.
- [ ] **Cover neurogenic claudication where the model wants it** — a new "leg pain when walking"
  symptom page feeding the existing spinal stenosis page, *not* a third stenosis page. 14,800
  searches a month, and it fixes a duplicate on the way through. **Still the best single opportunity
  in this launch.**
- [ ] **Merge the duplicate stenosis pages** — `/conditions/lumbar-stenosis/` into
  `/conditions/spinal-stenosis/`.
- [ ] **Improve three live-but-weak pages** where his priorities and the numbers line up:
  radiofrequency ablation (ranks 27.6 against demand sitting at 51–96), occipital nerve block
  (ranks 19.4 on a 6,600/month term), and EMG.
- [ ] Article: **when to see a spine surgeon vs. a pain doctor** *(his idea, and the highest-value
  one — it also sends the right patients to the right door)*.
- [ ] Article: **what an EMG actually tells your doctor** — including whether it hurts and how long
  it takes. Lots of people ask; nobody local answers well.
- [ ] **Build three condition pages he treats that we don't have:** complex regional pain syndrome,
  focal headache / occipital neuralgia, and post-surgical pain.
- [ ] Add FAQ sections with proper markup to his pages. We have **zero** on the whole site today.
- [ ] Add him and his pages to `/llms.txt` so the AI tools can find him.
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
| What's live day one | Operations | Which treatment pages can name him, and every ad |
| Can a provider link to a treatment in the CMS? | **Paul** | **The whole September plan** — ask this week |
| Which insurance he takes | Credentialing | Phone screening |
| Is Troy happening? | Operations | A third Google listing (Troy is our biggest untapped area) |
| Boston Scientific patient-database idea | **Compliance — don't touch it yet** | — |

---

## Worth raising with Joe separately

Three things this launch turned up that are bigger than this launch:

- **The symptom layer barely exists.** One page with any traffic. It's the "I don't know what's
  wrong with me" front door the model was designed around, and it's empty.
- **Three current pain doctors have duplicate bio pages** splitting their traffic today. Small fix,
  three physicians who already rank.
- **An old Mendelson-branded blog post books more patients than any real pain page we own.** There
  are probably others like it. Worth a sweep before someone tidies them away.

---

*Everything clinical here is a draft until Dr. Heyl and clinical review sign off. Nothing on this
list is cleared to publish on its own.*
