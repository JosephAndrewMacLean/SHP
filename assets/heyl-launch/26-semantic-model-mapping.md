# Launching Heyl without the Pain Management service line

**The short answer: don't rebuild the service line, and don't map treatments to him as a workaround.
Mapping him to treatments *is* the model working correctly.**

You already have three of the four layers built. The only thing missing is the join between
providers and treatments — and Dr. Heyl's questionnaire already collected the data for it, in
exactly the right shape.

---

## What's actually on the site right now

I pulled every page under `/symptom/`, `/conditions/` and `/treatment/` (GSC + GA4, 90 days ending
2026-07-28). The semantic model isn't a plan — it's live and mostly complete:

| Layer | Pages | Search performance | State |
|---|---|---|---|
| `/symptom/{symptom}` | ~1 with any traffic | `/symptom/knee-pain/` — 2 sessions | 🔴 **Barely built** |
| `/conditions/{condition}` | ~60 live | e.g. neck fracture 69,533 impressions, Dupuytren's 18,761 | ✅ Built |
| `/treatment/{treatment}` | ~70 live | e.g. PRP 26,122 impressions at position 6.9 | ✅ Built |
| `/treatment/?treatment_type=` | surgical / non-surgical facet | 18 sessions | ✅ Exists |
| `/providers/{name}` | ~66 live | Top bios 200–360 clicks each | ✅ Strongest asset we have |

So the chain the model intends is **symptom → condition → treatment → provider.** Conditions and
treatments are done. Providers are done. **The symptom layer and the provider↔treatment join are
the two gaps** — and only the second one blocks this launch.

---

## Your instinct is right, and it's not a compromise

You wrote: *"specialties to Heyl are treatments."*

That's exactly it. When he described his practice in onboarding, he didn't give us a department — he
gave us **a list of conditions and a list of procedures.** Two checkbox lists.

Those two lists map one-to-one onto `/conditions/` and `/treatment/`.

The old service line was the thing that didn't match how he thinks. The semantic model matches it
precisely. **You're not working around the missing service line — you're using the model as designed,
and he happens to describe himself in its native vocabulary.**

This holds for every physician, not just him. "What do you treat" and "what do you do" are the two
questions any physician can answer instantly. "Which department bucket are you" is the one that
requires a taxonomy meeting.

---

## 🚨 Correction: my earlier procedure-page work targeted the deprecated URLs

This is the part that changes the launch, and it's good news.

I built `12-emg-page.md` and `17-procedure-pages.md` against `/specialties/pain-management/*`. Those
are the **old** URLs. The migrated `/treatment/*` pages already exist and are dramatically stronger:

| Procedure | Old `/specialties/pain-management/` | New `/treatment/` | Difference |
|---|---|---|---|
| Peripheral nerve injection | **1 impression** | **7,754** at position 8.9 | 7,754× |
| Trigger point injection | 2 | **8,422** at position 11.4 | 4,211× |
| Radiofrequency ablation | 1 | **3,515** at position 27.6 | 3,515× |
| Caudal ESI | 1 | **9,314** at position 8.5 | 9,314× |
| EMG | 132 at position 7.9 | **1,034** at position 9.2 | 8× |
| Spinal cord stimulator | 29 | **2,997** at position 18.7 | 103× |

The migration worked. The `/specialties/pain-management/` pages are dead remnants still in the index.

**What this means for the launch: 12 of Dr. Heyl's 13 cleared procedures already have live, ranking
pages.** We don't need to build a procedure library. We need to put his name on pages that already
exist.

**Those 12 pages carry 44,264 impressions per 90 days between them.** The deprecated
`/treatment/pain-management/` service-line page carries 9,856. The treatment layer is already doing
**4.5× the work** of the page we were about to rebuild.

---

## The solution: one join table

Everything below is a data operation. No new taxonomy, no new service line, and — for the launch —
almost no new pages.

### 1. Map him to treatments *(the whole launch, essentially)*

Add him as a performing provider on the 12 existing treatment pages. Data in
`27-heyl-treatment-map.csv`.

Each treatment page gets a **"Physicians who perform this"** block. Each provider page gets a
**"Treatments I perform"** block. That's the join — a many-to-many relationship between two content
types that already exist.

### 2. Map him to conditions

Same operation on the condition pages. Most already exist; a few of his don't (below).

### 3. Let the conditions do the routing

This is the part that answers *"how do we organize pain specialists into what hurts?"*

**You don't.** You organize **treatments** into what hurts — which is already done, because every
condition page links to its treatments. Physicians attach to treatments. A patient searching
"sciatica" lands on the condition, sees the treatments, and sees who performs them.

Nobody maintains a specialty bucket. Nobody decides which department a physician belongs to. The next
hire is a row in a spreadsheet, not a taxonomy discussion.

### 4. Replace the service line with a pathway page, not a department

One real problem remains: **"pain management doctor near me" gets 2,400 searches a month**, and
`/treatment/pain-management/` still pulls 9,856 impressions. People do search the category.

But that's a **care-pathway question**, not a department. Recommendation: keep the URL, change what
the page is.

| Was | Becomes |
|---|---|
| Pain Management service line — a department listing | **Non-surgical pain treatment** — a router |
| "Here is our department and its staff" | "Here's what hurts → here's the condition → here's the treatment → here's who does it" |
| A bucket physicians belong to | An entry point that sends people into the model |

It keeps the 9,856 impressions and serves the query without resurrecting the department. It becomes
the human-readable front door to `?treatment_type=non-surgical`, which is a terrible landing page but
the right underlying idea.

---

## Where Heyl actually has gaps

Only two treatments and three conditions. That's the entire net-new content requirement.

**Missing treatment pages — build these:**

| Missing | Searches/mo | Difficulty | Note |
|---|---|---|---|
| **Genicular nerve block / ablation** | 5,400 | 19 | No page anywhere. His priority #4. |
| **Peripheral nerve stimulation** | 1,000 | 32 | No page. His **priority #2** — what he came here to build. |

**Missing condition pages:**

- Complex regional pain syndrome
- Focal headache / occipital neuralgia *(pairs with the occipital nerve block page)*
- Post-surgical / persistent post-operative pain

**Everything else already exists.** That's 2 treatment pages and 3 condition pages instead of the
8-page procedure library I originally scoped.

---

## I was wrong about the neurogenic claudication page — the model has a better home for it

I proposed a standalone `/conditions/neurogenic-claudication/`. That fights the taxonomy, and there's
already a duplicate problem there: **`/conditions/spinal-stenosis/`** (550 impressions, position 18.3)
and **`/conditions/lumbar-stenosis/`** (105 impressions, position 23.2) are two pages for one
condition. A third would make it worse.

The model wants it split by layer:

- **Symptom:** `/symptom/leg-pain-when-walking/` — the "what hurts" entry, currently missing
- **Condition:** `/conditions/spinal-stenosis/` — exists; consolidate the lumbar-stenosis duplicate
  into it, and cover neurogenic claudication *within* it as the mechanism
- **Treatment:** epidural injection, medial branch block — all exist

That captures the 14,800 monthly searches, doesn't add a competing stenosis page, and fixes an
existing duplicate on the way through. Same opportunity, less content, better structure.

**And it seeds the symptom layer** — which is the one part of the model that was designed and never
built. A pain physician's launch is the natural reason to build it, because "what hurts" is exactly
how his patients arrive.

---

## What this does to the launch plan

| Was | Now |
|---|---|
| Rebuild 8 procedure pages | **Name him on 12 existing pages** + build 2 |
| Rewrite the Pain Management service page | **Reframe it as a pathway router** |
| New neurogenic claudication page | **Consolidate stenosis duplicates**, add a symptom page |
| Figure out where pain specialists live | **They live on treatments. Conditions route to them.** |
| Taxonomy work for every future hire | **A spreadsheet row** |

Roughly a third of the original content work, and the pages he lands on are already ranking rather
than starting from zero.

---

## What has to be true for this to work

Three questions for Paul, and they're the whole dependency:

1. **Is there a provider↔treatment relationship in the CMS?** If treatments and providers are both
   custom post types, this is a relationship field and a template block — a small job. If it doesn't
   exist, it's the one thing worth building, because it's what makes every future physician launch
   trivial.
2. **Do condition pages already link to their treatments?** If yes, routing is free. If not, that
   link is the other half of the model.
3. **What happens to `/specialties/pain-management/*`?** Those old pages are still indexed and still
   competing. They should 301 to their `/treatment/` equivalents — see the redirect map in
   `27-heyl-treatment-map.csv`.

**If the relationship field doesn't exist and can't be built before Sept 1**, the fallback is manual:
hand-add a "Physicians who perform this" block to the 12 treatment pages and a treatment list to his
bio. Same result, no automation, and it still beats rebuilding a service line.

---

## Worth raising beyond this launch

- **`/treatment/prp-injections/` has 26,122 impressions at position 6.9** — the strongest treatment
  page on the site. PRP is on Dr. Heyl's hold list, so **don't attach him**, but it's proof the
  treatment layer works when a page is good.
- **`/treatment/injections-esi-facet-nerve-blocks/`** (2,098 impressions) looks like an umbrella page
  overlapping the specific injection pages. Probable cannibalization — worth a look.
- **`/treatment/kyphoplasty-vertebroplasty/`** (8,377 impressions) is the live URL for the page
  Dr. Heyl must never be linked to. `09-taxonomy-firewall-check.md` has been updated to check this
  URL rather than the deprecated one.
- **The symptom layer is the unbuilt half of the model.** One page with traffic. If the site is meant
  to serve people who don't know their diagnosis — which is what the Creative Audit said was
  missing — this is where that happens, and it's currently empty.

---

## The one-line version, for anyone who asks

> We don't need the Pain Management service line back. Patients search for what hurts, so conditions
> are the front door; conditions link to treatments; physicians attach to treatments. Dr. Heyl
> described his practice as a list of conditions and a list of procedures, which is exactly the two
> lists the model needs — so he plugs in without a department, and so does everyone we hire after him.
