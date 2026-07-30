# Rewrite — Pain Management service page

**URL:** `https://synergyhealth.org/treatment/pain-management/` *(exists — rewrite in place)*
**Status:** DRAFT — requires physician review
**Owner:** Randall · **Target live:** Aug 28

---

## Why this page, and why it's urgent

| | 90 days ending 2026-07-28 |
|---|---|
| Times shown in Google | **9,856** |
| Clicks | **50** |
| Click rate | **0.51%** *(benchmark: 3–5%)* |
| Average position | **18.2** |
| Website visits (GA4) | 20 |
| Appointment actions | 4 |

Nearly 10,000 people saw this page in search results and 50 clicked. It's the second page of results,
so most of those impressions were never realistic — but at 0.51%, even the ones that were aren't
converting.

**And here's the thing worth knowing before you touch anything:** the best-performing pain asset on
our site isn't this page at all. It's an old blog post at
`/mendelson-orthopedics-is-a-multi-specialty-practice-that-offers-hope-and-relief-for-chronic-pain-sufferers/`
— 275 clicks, 12,705 impressions, 139 visits, and **39 appointment actions** in the same window.

Ten times the conversions of the actual service page, on a URL carrying the old brand name.
See `15-legacy-post-refresh.md` — **do not delete that post.**

---

## Title and description

**Title** (57 characters):
> Pain Management in Metro Detroit | Synergy Health Partners

**Meta description** (153 characters):
> Treatment for back, neck, joint and nerve pain across metro Detroit. Interventional pain physicians, EMG testing and same-week appointments available.

---

## Page copy — DRAFT FOR PHYSICIAN REVIEW

### H1
> Pain management

### Opening

> **Pain management means finding what's actually causing your pain and treating that specific
> problem — not just managing the symptom.**
>
> Our pain physicians use examination, imaging and nerve testing to identify the source, then treat
> it with targeted, image-guided procedures. The goal is getting you back to what the pain is
> stopping you from doing.

### Start where you are — symptom-first entry

> *(Editor's note: this block is the point of the rewrite. Our UX audit found the whole site assumes
> visitors already know their diagnosis, with no path for someone who doesn't. Each item links to the
> relevant condition or procedure page.)*
>
> **My back or neck hurts** → Back and neck pain
> **Pain travels down my leg or arm** → Sciatica and radiating nerve pain
> **My legs hurt when I walk but feel better when I sit** → Neurogenic claudication
> **I have numbness or tingling** → Nerve pain and neuropathy
> **A joint hurts — knee, hip, shoulder** → Joint pain
> **I still hurt after surgery** → Post-surgical pain
> **I don't know what's causing it** → Request an evaluation

### What we treat

> - Back and neck pain, including arthritis-related spine pain
> - Sciatica and radiating nerve pain
> - Spinal stenosis and leg pain when walking
> - Sacroiliac joint pain
> - Joint and musculoskeletal pain
> - Peripheral nerve problems and neuropathy
> - Complex regional pain syndrome
> - Pain following surgery
> - Focal headache and facial nerve pain

### What we do

> **Diagnosis**
> Physical examination, imaging review, and EMG and nerve conduction testing to identify what's
> generating your pain and how much it's affecting the nerve.
>
> **Injections and nerve blocks**
> Epidural injections, medial branch blocks, sacroiliac and joint injections, trigger-point
> injections, peripheral nerve blocks, occipital nerve blocks, and genicular nerve blocks for knee
> pain — all image-guided so the medication reaches the intended target.
>
> **Radiofrequency ablation**
> For pain confirmed to come from specific spinal joints, ablation can provide longer-lasting relief
> than injections alone.
>
> **Nerve stimulation**
> Peripheral nerve stimulation and spinal cord stimulation for nerve pain that hasn't responded to
> other treatment.
>
> **Coordinated care**
> Physical therapy, chiropractic care, imaging, and spine surgery are all part of the same practice —
> so if your treatment needs to change direction, it doesn't mean starting over somewhere new.

### When to see a pain physician instead of a surgeon

> Most people with back, neck or joint pain don't need surgery. A pain management physician diagnoses
> and treats without an operation, and can tell you whether a surgical opinion is worth getting.
>
> A surgeon is the better first call when there's progressive weakness, a structural problem that
> hasn't responded to other treatment, or a spine fracture or instability.
>
> [Read the full comparison →] *(links to `13-article-surgeon-vs-pain-doctor.md`)*

### What to expect at your first visit

> Your first appointment is an evaluation. Your physician will examine you, review your history and
> imaging, and work out the most likely source of your pain.
>
> You'll leave knowing what they think is causing it, what the next step is, and how it connects to
> what you want to be able to do again.
>
> **We won't promise a procedure before examining you.** If a procedure is the right next step,
> you'll hear why. If it isn't, you'll hear that too.

### Our pain physicians

> *(Editor's note: name all of them with photos and links. Provider pages are the strongest-performing
> content we have — our top bios earn 200–360 clicks each per quarter, while this page earns 50. Use
> that.)*
>
> **Anthony J. Oddo, DO** — Director of Pain Management
> **Kevin R. Lee, MD** — Pain management and functional neurosurgery
> **Brian Kassa, DO** — Fellowship-trained pain management
> **Hanish Singh, MD** — Pain management
> **Jonathan Heyl, DO** — Interventional pain, peripheral nerve and electrodiagnostics *(from September 2026)*
>
> *Verify this roster with Operations before publishing.*

### Where we are

> *(List locations with pain-management services and link to each location page.)*

### For referring providers

> We accept referrals for persistent spine pain, focal joint pain, suspected peripheral nerve
> problems, EMG clarification, and patients who may be candidates for an interventional option after
> conservative care.
>
> [Referral information →] [Call (855) 750-5757]

---

## Build notes

- **Grade 6–8.** The current page reads well above that, in line with about 80% of our site.
- **Fix the title and meta first** — they're the fastest lever on a page that already gets 9,856
  impressions. Ship those even if the full rewrite takes longer.
- FAQPage schema on the first-visit and surgeon-comparison sections
- Internal links out: every condition page, every procedure page, every pain physician's bio
- Internal links in: homepage services, spine hub, all location pages, the legacy post (`15-`)
- **Watch for URL confusion:** `/treatment/pain-management/` and `/specialties/pain-management/` both
  exist, along with four other pain URL patterns. This rewrite doesn't fix that — see the
  consolidation task in the checklist — but don't add a seventh pattern in the process.

## Review gates

| What | Who |
|---|---|
| Conditions and procedures lists | **Clinical** — must reflect what the whole team actually offers, not just Dr. Heyl |
| Physician roster | Operations |
| "When to see a surgeon" section | **A spine surgeon** — same reason as the article |
| First-visit description | Clinical + Kelly (the phones repeat this) |
| Claims and tone | Joe |
