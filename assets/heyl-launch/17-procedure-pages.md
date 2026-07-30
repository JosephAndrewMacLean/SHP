# Procedure pages — template and build order

**Owner:** Randall · **Pace:** 2–3 per week from Aug 25 · **Status:** template ready, briefs ready
**Every page requires physician review before publishing.**

---

## Build order

Ordered by search demand against ranking difficulty, weighted toward Dr. Heyl's stated priorities.
Do them in this sequence — the early ones are the cheapest wins.

| # | Page | Searches/mo | Difficulty | Status today |
|---|---|---|---|---|
| 1 | **Medial branch block** | 8,100 | **14** | Page exists, ranks 6.0, 525 impressions — *easiest win on the list* |
| 2 | **EMG / nerve conduction** | 1,900 + 6,600 | **14 / 37** | Exists, ranks 7.9 — full rewrite in `12-emg-page.md` |
| 3 | **Genicular nerve block** | 5,400 | **19** | **No page exists** — pure gap |
| 4 | **Occipital nerve block** | 6,600 | **27** | No dedicated page |
| 5 | **Peripheral nerve block + stimulation** | 1,000 | **32** | Page exists with **1 impression in 90 days** |
| 6 | **Radiofrequency ablation** | 30 exact, but see below | — | Exists with **1 impression** |
| 7 | **SI joint injection** | 1,000 | 33 | Condition page ranks 23.4 |
| 8 | **Epidural steroid injection** | 18,100 | 61 | Hardest, biggest — do last |

**On radiofrequency ablation:** the exact phrase has low volume, but Search Console shows dozens of
variants — "ablation for back pain," "back nerve ablation," "ablation for facet joint pain" — where
we appear at **position 51–96.** There's real demand; we're just invisible for it. Treat this as a
higher priority than the exact-match number suggests.

**Before writing any of these:** check the procedure against the Operations-confirmed list in
`04-provider-record.md`. If Operations hasn't confirmed it, the page can still exist — it just can't
name Dr. Heyl as performing it.

---

## Template

Every procedure page uses this structure. Consistency helps readers, helps search engines, and makes
these fast to produce.

```
H1: [Procedure name]

DIRECT ANSWER — 40-55 words, immediately under the H1, no preamble.
What it is, what it treats, and roughly how long it takes.
This is the snippet-eligible paragraph. Don't put anything above it.

H2: What it treats
Specific conditions. Link to each condition page.

H2: How it works
Plain language. What the procedure targets and why that helps.
Grade 6-8. If a physician wouldn't say it out loud to a patient, rewrite it.

H2: What happens during the procedure
Step by step, in order. Include:
- How long it takes
- Whether you're sedated
- What guidance is used (X-ray, ultrasound)
- What you'll feel

H2: What to expect afterward
- Recovery time
- Restrictions
- When relief typically begins
- Whether you can drive yourself home

H2: How long relief lasts
Honest ranges, no promises. "Varies from person to person" is fine
when it's true — it's more credible than a number we can't stand behind.

H2: Risks and side effects
Real ones, plainly stated. This section builds trust rather than
costing conversions. Requires physician review, no exceptions.

H2: Is this right for me?
Who it tends to help. Who it doesn't. What usually comes first.

H2: Common questions
The five standard FAQs, answered for this procedure. FAQPage schema.

H2: [Procedure] at Synergy
Named physicians. Locations. Booking CTA. Referral link.
```

**Rules for every page:**
- Grade 6–8
- No outcome promises. "Reduces pain for many people" — not "eliminates pain."
- Name the physicians who perform it
- FAQPage schema
- "Medically reviewed by [name], [credentials], [date]"
- Link to the relevant condition pages and to Dr. Heyl's bio
- Every image needs `width` and `height` attributes set

---

## Briefs

### 1. Medial branch block — *start here*
**Target:** medial branch block (8,100/KD 14), cervical medial branch block, facet joint injection
**Covers:** diagnosing whether pain is coming from the facet joints in the spine
**Angle:** this is both a treatment and a **diagnostic test** — if a block relieves the pain, it
confirms the target, and that often makes someone a candidate for longer-lasting radiofrequency
ablation. Most pages don't explain this two-step logic, and patients find it genuinely clarifying.
**Existing pages:** `/specialties/pain-management/lumbar-medial-branch-block/` (525 impressions,
position 6.0) and `/cervical-medial-branch-block/` (144 impressions, position 6.7). Improve these
rather than creating new ones.

### 2. EMG and nerve conduction
Full draft already written — see `12-emg-page.md`.

### 3. Genicular nerve block and ablation — *biggest pure gap*
**Target:** genicular nerve block (5,400/KD 19), knee nerve block, knee ablation
**Covers:** chronic knee pain, arthritis knee pain, pain after knee replacement
**Angle:** for people with knee arthritis who aren't candidates for replacement, don't want one yet,
or still hurt after having one. That last group is underserved and actively searching.
**No page exists.** 5,400 searches a month at difficulty 19 with nothing on our site.
**Cross-link:** the orthopedic knee pages — this is a genuine hand-off between service lines.

### 4. Occipital and facial nerve blocks
**Target:** occipital nerve block (6,600/KD 27), occipital neuralgia treatment
**Covers:** occipital neuralgia, focal headache, facial nerve pain
**Angle:** headaches that start at the base of the skull and radiate up, especially when they haven't
responded to headache medication.
**Also:** this page is the backbone of the neurology referral push in the checklist. Write it so a
neurologist could read it and know exactly who to send.

### 5. Peripheral nerve blocks and peripheral nerve stimulation — *his #1 priority*
**Target:** peripheral nerve stimulation (1,000/KD 32), peripheral nerve block, nerve pain treatment
**Covers:** focal nerve pain, mononeuropathy, post-surgical nerve pain, CRPS
**Angle:** this is what Dr. Heyl came to build, and no competitor in metro Detroit has a real page on
it. Explain the difference between a diagnostic block, a therapeutic block, and stimulation — and
cover the **temporary 60-day stimulator system** if Operations confirms it, because it's unusual
enough to be worth explaining properly.
**Existing page** `/specialties/pain-management/peripheral-nerve-injection/` has **one impression in
90 days.** Rebuild it entirely.

### 6. Radiofrequency ablation
**Target:** the whole "ablation for back pain" family, where we currently sit at position 51–96
**Covers:** facet joint pain, SI joint pain, knee pain, confirmed sources of chronic pain
**Angle:** follows on from the medial branch block page — the block confirms the target, the ablation
treats it for longer. Be honest that nerves regenerate and the procedure may need repeating; that
honesty is what distinguishes a credible page from a sales page.

### 7. Sacroiliac joint injection
**Target:** si joint pain treatment (1,000/KD 33), si joint injection
**Covers:** SI joint dysfunction, low back pain that doesn't radiate below the knee
**Angle:** SI joint pain is commonly mistaken for lumbar spine pain. The injection both treats and
confirms.
**Existing:** `/conditions/si-joint-pain/` ranks 23.4 with 296 impressions — link the two.

### 8. Epidural steroid injection — *do last*
**Target:** epidural steroid injection (18,100/KD 61), lumbar ESI, cervical ESI
**Covers:** sciatica, radicular pain, spinal stenosis
**Angle:** the highest-volume term here and the hardest. Every health system in the country has this
page. Win on specifics — the actual experience, honest duration ranges, and how it fits into a plan
rather than being the plan.
**Existing pages** for caudal, cervical and lumbar ESI have 1–2 impressions each. Consolidate into
one strong page with sections, rather than three weak ones competing with each other.

---

## Review gates — same for every page

| What | Who |
|---|---|
| Procedure description, risks, recovery | **Dr. Heyl** — no exceptions, and the risks section especially |
| Whether he performs it at all | Operations |
| Which conditions it treats | Clinical |
| Claims, promises, tone | Joe |
| Schema and technical build | Randall + Paul |
