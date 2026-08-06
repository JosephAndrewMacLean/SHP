# FAQ library and schema

**Owner:** Randall · **Target live:** Sept 8
**Status:** questions ready · **answers require physician review**

---

## Why this matters more than it looks

Our site has **zero FAQ schema on any page** and **zero FAQ rich results** in Google. That's not a
small gap — it's an entire category of search visibility we don't participate in, and the tracking
for it is already set up and reading zero.

Two things this unlocks:

1. **Featured snippets and "People also ask."** These questions are what people actually type. A
   direct answer in the right format can win the box above the results.
2. **AI answers.** Google's AI Overviews, ChatGPT, and Perplexity all pull from clearly structured,
   plainly written, attributed answers. We now appear on 2,276 keywords where AI Overviews show — as
   exposure, not as a cited source. This is how that changes.

---

## The format rule

Every answer follows the same shape, and the shape is what makes it work:

1. **Question as an H2**, phrased the way people search it — "Does an EMG hurt?" not "EMG discomfort"
2. **A direct answer in 40–55 words, immediately below.** No preamble, no "it depends," no "at
   Synergy Health Partners we believe." Answer the question in the first sentence.
3. **Detail after** — as much as you like, once the direct answer is out of the way.

If the first sentence doesn't answer the question, it won't win a snippet and an AI won't quote it.

---

## The questions

Grouped by page. **Answers must come from Dr. Heyl or another SHP physician** — the draft text in
the linked page files is a starting point for their review, not final copy.

### Dr. Heyl's bio page
- What kind of doctor is Dr. Heyl?
- What conditions does Dr. Heyl treat?
- Where does Dr. Heyl see patients?
- Do I need a referral to see Dr. Heyl?
- What happens at a first appointment with Dr. Heyl?

### EMG page → `12-emg-page.md`
- Does an EMG hurt? *(260/month, and almost nobody answers it honestly)*
- How long does an EMG take? *(720/month)*
- What does an EMG diagnose? *(1,900/month)*
- What is an EMG test? *(4,400/month)*
- How do I prepare for an EMG?
- Can I drive myself home after an EMG?
- Who performs an EMG?
- What's the difference between an EMG and a nerve conduction study?

### Neurogenic claudication page → `11-neurogenic-claudication-page.md`
- What is neurogenic claudication? *(1,900/month)*
- What does neurogenic claudication feel like?
- Does neurogenic claudication go away? *(140/month)*
- How do you tell neurogenic from vascular claudication?
- Is neurogenic claudication the same as sciatica?
- How serious is neurogenic claudication?
- Will I need surgery for spinal stenosis?
- What kind of doctor treats neurogenic claudication?

### Surgeon vs. pain doctor article → `13-article-surgeon-vs-pain-doctor.md`
- Should I see a spine surgeon or a pain management doctor?
- Does seeing a spine surgeon mean I'll need surgery?
- Will a pain management doctor just give me an injection?
- Do I need a referral to see a spine specialist?
- What should I bring to a first appointment?

### Pain management service page → `14-pain-management-page.md`
- What does a pain management doctor do?
- What conditions does pain management treat?
- Are pain injections covered by insurance?
- How soon can I be seen?
- What's the difference between pain management and physical therapy?

### Procedure pages → `17-procedure-pages.md`
Each procedure page carries the same five, answered specifically:
- What is [procedure]?
- Does [procedure] hurt?
- How long does [procedure] take?
- How long does relief from [procedure] last?
- What are the risks of [procedure]?

---

## Schema

One `FAQPage` block per page, containing only that page's questions. Add it alongside the page's
existing schema — don't replace it.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does an EMG hurt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most people find an EMG uncomfortable rather than painful. The nerve conduction portion feels like brief static shocks. The needle portion feels like short pressure or an ache. Discomfort is brief and ends when the test does. Some people notice mild muscle soreness for a day afterward."
      }
    },
    {
      "@type": "Question",
      "name": "How long does an EMG take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most EMG and nerve conduction tests take 30 to 60 minutes, depending on how many nerves and muscles need to be examined. A focused test for one suspected problem is quicker. No sedation is needed and you can drive yourself home."
      }
    }
  ]
}
```

**Rules:**
- The `text` must match the visible answer on the page. Google checks, and mismatches get the markup
  ignored or the page flagged.
- Every question in the schema must be visibly answered on the page.
- Validate at `search.google.com/test/rich-results` before publishing.
- **No medical claims in schema that aren't approved on the page.** Schema is published content.

---

## Checking whether it worked

- **Semrush FAQ rich-result keyword count.** Currently zero. Any number above zero means it's
  registering. Check monthly.
- **Search Console → Search Appearance.** Watch for FAQ to appear as a result type. We currently show
  only one appearance type sitewide.
- **Manual check** — search the exact question and see who owns the answer box.
- **AI answer check** — part of the monthly generative-answer test in `25-baseline-snapshot.md`.

---

## Review gates

| What | Who |
|---|---|
| Every clinical answer | **Dr. Heyl or an SHP physician** — these become quotable answers in AI results, so accuracy compounds |
| Insurance and access answers | Operations + Kelly |
| Schema build and validation | Randall + Paul |
| Claims and tone | Joe |

Nothing here publishes on physician review alone if it makes a claim about outcomes, coverage, or
availability — those need Joe too.
