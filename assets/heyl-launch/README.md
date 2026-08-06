# Dr. Heyl launch — everything, and how to use it

**Randall, start here.** 24 drafted assets. This page tells you what's finished, how to publish it,
who has to sign off, and the handful of things only you can make.

*Day-to-day checklist: `playbooks/heyl-launch-randall-todo.md`. Data behind the decisions:
`playbooks/heyl-launch-reference.md`.*

---

## What's in the folder

| # | File | What it is | State |
|---|---|---|---|
| 01 | `01-email-to-heyl.md` | Five open questions, written and ready | **Send it** |
| 02 | `02-photo-shot-list.md` | Brief for the Aug 10 shoot | **Send it** |
| 03 | `03-messaging-guardrails.md` | The rules everyone writing about him must follow | **Send it** |
| 04 | `04-provider-record.md` | Single source of truth for every fact about him | Fill the 🟡 gaps |
| 05 | `05-operations-capability-request.md` | What can we actually promote? | **Send it** |
| 06 | `06-bio-page.md` | Full bio copy, title, meta | Draft — 1 section blocked |
| 07 | `07-physician-schema.json` | Hand-built page markup | Fill the FIXMEs |
| 08 | `08-url-lock.md` | Lock one bio URL before writing anything | Do this first |
| 09 | `09-taxonomy-firewall-check.md` | Pre-publish compliance check | Run before publish |
| 10 | `10-directory-profile-pack.md` | Copy for all 6+ directories, ready to paste | Draft |
| 11 | `11-neurogenic-claudication-page.md` | New page — biggest opportunity in the launch | Draft |
| 12 | `12-emg-page.md` | Rewrite of the existing EMG page | Draft |
| 13 | `13-article-surgeon-vs-pain-doctor.md` | The decision article — his idea | Draft |
| 14 | `14-pain-management-page.md` | Rewrite of the main service page | Draft |
| 15 | `15-legacy-post-refresh.md` | ⚠️ Careful — our best-converting pain page | Needs a decision |
| 16 | `16-faq-library.md` | 40+ questions + schema pattern | Draft |
| 17 | `17-procedure-pages.md` | Template + 8 page briefs in build order | Template ready |
| 18 | `18-internal-routing-sheet.md` | Who inside SHP sends him what | Draft |
| 19 | `19-referral-one-sheet.md` | The B2B leave-behind | Draft |
| 20 | `20-call-center-rules.md` | Clinical content for Kelly's script | Draft |
| 21 | `21-press-release.md` | New physician announcement | Draft |
| 22 | `22-referral-announcement-email.md` | Three versions, three audiences | Draft |
| 23 | `23-paid-brief-blue-ox.md` | Ad brief with the compliance list | Hold until 05 is back |
| 24 | `24-post-exam-checklist.md` | Everything to change when he's certified | Set the reminder |
| 25 | `25-baseline-snapshot.md` | Fill in before Sept 1 | **Time-sensitive** |
| 26 | `26-semantic-model-mapping.md` | **How he launches without the Pain Management service line** | **Read before 11, 12, 14, 17** |
| 27 | `27-heyl-treatment-map.csv` | The mapping data — him → treatments, conditions, redirects | Ready |

> ### ⚠️ Read 26 first
> The Pain Management service line was deprecated in favour of a symptom → condition → treatment
> model, and that model is **already live** — ~60 condition pages and ~70 treatment pages.
> **12 of his 13 cleared procedures already have ranking pages** carrying 44,264 impressions between
> them. Files **11, 12, 14 and 17 were drafted against the deprecated URLs** and carry correction
> banners. The net effect is roughly a third of the original content work.

---

## How to publish, in order

The sequence matters more than the speed. Four things gate everything else.

### Step 1 — Send four things this week *(by Aug 7)*

No review needed beyond Joe's glance. These unblock the rest.

1. **`01`** to Dr. Heyl — five questions
2. **`02`** to the photographer — shot list
3. **`03`** to everyone writing about him — the rules
4. **`05`** to Operations — what can we promote

Then wait. **The bio can't be finished without answer 3 in `01`. The procedure pages can't be
finished without `05`.** Working ahead on those wastes effort.

### Step 2 — Lock the URL *(Aug 14, before any copy is written)*

Run **`08`**. Create the page at `/providers/jonathan-heyl-do/`, block the variants, set the
canonical.

This takes an hour and prevents the problem all three of our current pain physicians have — two
competing bio pages splitting their traffic. Do it before writing, not after.

### Step 3 — Build the bio *(Aug 14–25)*

1. Fill in `04` with what came back from Dr. Heyl and Operations
2. Finish `06` — drop his answer into the personal section
3. **Send `06` to Dr. Heyl for approval.** Nothing goes live until he's seen it.
4. Fill the FIXMEs in `07` and validate the schema
5. Build in staging

### Step 4 — Run the compliance check *(Aug 21)*

Run **`09`** in staging. This is the one that catches him being auto-linked to kyphoplasty or
ketamine — both pages are live on our site and both are outside his stated guardrails.

Then run it again after publishing. Staging and production don't always render the same blocks.

### Step 5 — Take the baseline *(Aug 28 — this date is not flexible)*

Fill in **`25`**. An hour's work.

Miss this and every question about whether the launch worked becomes unanswerable. It cannot be
reconstructed after Sept 1.

### Step 6 — Launch week *(Sept 1)*

- Bio live
- Directories live — work through `10`, Google Business Profiles first
- He's added to both location pages
- **Test the booking path yourself, start to finish**
- Confirm Liine is attributing his calls
- Kristen sends `22`; her team has printed copies of `19`
- Kelly's script is live, built from `20`
- `21` goes to media
- He's enrolled in the review program

### Step 7 — Content, through September and October

In this order — the sequencing is by value, not by what's easiest:

1. **`13`** — surgeon vs. pain doctor. Highest-value single piece. His idea, routes patients
   correctly, works as referral collateral.
2. **`14`** — pain management page rewrite. *Ship the title and meta immediately even if the full
   rewrite lags — it's the fastest lever on a page already getting 9,856 impressions.*
3. **`11`** — neurogenic claudication. 14,800 searches a month at difficulty 15 and we rank nowhere.
4. **`12`** — EMG rewrite
5. **`17`** — procedure pages, 2–3 a week in the listed order
6. **`16`** — FAQ schema across all of them
7. **`15`** — legacy post refresh, carefully, monitoring weekly

### Step 8 — Paid, after launch *(Sept 8)*

Send **`23`** to Blue Ox once Operations has confirmed capabilities and capacity, and once the
booking path is verified. Not before.

### Step 9 — October

Run **`24`** when Credentialing confirms his board result. Re-run `08` and `09` while you're there —
duplicates and taxonomy drift usually appear a month or two after launch.

---

## Who reviews what

Two things to get right: **route each item to the right reviewer**, and **don't send everything at
once.** A physician who gets twenty documents in one email reads none of them.

### Dr. Heyl — clinical accuracy and anything in his voice

**Must approve before publishing:**

| Item | Why |
|---|---|
| `06` bio | It's about him, and the personal section is his words |
| `11` `12` `13` | Clinical content published under our name |
| `17` procedure pages — **especially the risks sections** | He performs these |
| `16` FAQ answers | These become quoted answers in AI results |
| `18` internal routing | It's his scope; he defines it |
| `19` referral one-sheet | Referring physicians read it closely |
| `20` call-center rules | The evaluation-first rule is his |
| `21` press release + his quote | Nobody is quoted without approving their words |
| `22` version C | His personal contacts, his call |

**How to send it to him without losing him:**

Three batches, not one.
- **Batch 1, mid-August:** the bio only. It's the most important and the most personal.
- **Batch 2, late August:** referral one-sheet, routing sheet, call-center rules. All B2B and
  operational, all short.
- **Batch 3, September:** clinical content pages as they're drafted, a couple at a time.

Ask him in `01` how he wants to review and how fast he can turn things around, then schedule
backward from that. If he says tracked changes in Word, send Word — don't make him adapt to us.

### Clinical leadership / another SHP physician

| Item | Why |
|---|---|
| `18` internal routing | It routes patients. Marketing can't approve it. |
| `13` — **also to a spine surgeon** | It describes their practice too. Both-sides review is what makes it credible and keeps it internally uncontroversial. |
| `11` red-flag symptoms | Patient safety |
| `14` conditions and procedures | Reflects the whole team, not just Heyl |
| `20` urgent escalation list | Patient safety |
| `18` Heyl-vs-existing-team section — **to Dr. Oddo** | It affects his team. He should shape it, not receive it. |

### Operations

`05` capability list · `04` locations and schedule · `19` and `22` access details, fax, wait times ·
`14` physician roster · `23` capacity

### Credentialing

NPI and license · every credential string in `04` · insurance participation, **including which
Medicaid plans** — that varies by provider here · the `21` credentials paragraph · confirmation of
the board result for `24`

### Joe

Claims, tone and compliance on everything · `15` the legacy-post decision · `23` budget · `21`
distribution and media contact · consent rules for `22`

### Kelly

Owns the final call-center script. `20` is source material for her, not a script to adopt — she
knows how her team actually talks.

### Kristen

Owns the referral send and the relationships. `19` and `22` are hers to use; the send list and
approach are her call.

### Paul

URL redirects for `08` · schema deployment for `07` and `16` · the CMS taxonomy question in `09` ·
booking-path testing

---

## What only you can create

Everything above is drafted. These aren't — they need judgment, access, or a conversation.

### Blocking, do this week

1. **Chase the answers to `01`.** Nothing else on this list matters as much. The bio, the target
   account list, and the 90-day measurement plan all sit behind it.
2. **Get the capability list back from Operations (`05`).** Anything unconfirmed by Aug 21 comes out
   of the launch.
3. **Search his name across every directory** and record what already exists (`10`, step 1). Nobody
   can do this for you — it's manual, and claiming beats creating.

### Needs your judgment

4. **The legacy-post decision (`15`).** Take the recommendation to Joe with the numbers. Don't decide
   alone and don't let anyone delete it casually.
5. **The URL slug (`08`).** Confirm with Credentialing that he's "Jonathan Heyl" everywhere, then
   commit.
6. **Which procedure pages actually name him.** Depends entirely on what `05` comes back with.
7. **Whether Zocdoc is worth it for him.** A business decision, not an SEO one — take it to Joe.

### Needs your hands

8. **The baseline (`25`).** An hour, before Aug 28. Nobody else will do it and it can't be redone
   later.
9. **The generative-answer test.** Manual — run the six prompts in four tools and paste the answers.
   Monthly, same prompts.
10. **Google Business Profiles.** In the GBP interface; API access is still pending.
11. **Claiming directory profiles.** Manual verification on each, usually a phone call or a postcard.
12. **The Semrush position-tracking setup.** Add the 15 target keywords before Sept 1 so tracking
    starts before the launch, not after.

### Needs a conversation

13. **The photographer.** `02` is the brief; you still have to book and brief them.
14. **Paul, about the CMS.** Two questions worth asking properly: what created the duplicate bio
    URLs, and does adding a provider to a specialty auto-link them to every procedure in it? Both
    affect all 42 physicians, not just this launch.
15. **Kristen, about target accounts.** She needs Dr. Heyl's individual names, which we don't have
    yet. Chase both ends.
16. **Kelly, about the script.** Hand over `20` as source material and let her write it.
17. **Blue Ox.** Send `23` with `03` attached and get written acknowledgment of the compliance list.

### Not yours — hand it off

18. **The Boston Scientific patient-database idea.** It's at "Discovery" in his onboarding follow-up.
    **Don't touch it.** Patient-database outreach is a HIPAA question before it's a marketing
    question. It goes to Compliance and stays there until they rule.

---

## Three things that will go wrong if you let them

**The bio ships without his personal story.** It's the most-read paragraph on any physician page, and
a bio without one reads like a directory entry. If he hasn't answered by Aug 18, escalate to Joe
rather than writing it yourself or publishing without it.

**The baseline gets skipped because launch week is busy.** Then in October someone asks whether this
worked and the honest answer is "we don't know." One hour, Aug 28.

**The legacy post gets cleaned up by someone tidying old URLs.** It has the old brand name in it and
it books more patients than any other pain page we own. Make sure Paul and Cardinal both know it's
protected.

---

## Standing rules for everything here

- **Nothing clinical publishes without a named physician reviewer and a review date on the page.**
- **"Board eligible in Pain Medicine"** until Credentialing confirms otherwise. Never "board
  certified in Pain Medicine."
- **Never** describe him as an anesthesiologist.
- **Never** mention kyphoplasty, long-term opioid management, or stem cell therapy. **PRP is on
  hold**, not approved.
- **No patient stories, images, or details** without documented written authorization. None.
- **No outcome promises, no superlatives, no statistics we can't substantiate on request.**
- **Grade 6–8** on everything patient-facing.
- **When you're unsure, ask before publishing.** Fixing a live page is more expensive than a
  two-day delay.
