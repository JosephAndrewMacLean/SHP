# MRI Scheduling Talking Points — v2 DRAFT (edits by marketing, 7/22)

**Status: DRAFT — four [VERIFY] items must be answered by ops/compliance before rollout.**
**Owners:** call center (Kelly) + MRI front desk · ancillary (Mitch).
**Program alignment:** the patient-facing lines below use Mitch's approved imaging wording
(7/22) — the same words going on the website (templates §2). Same words, every channel.
**Edits from v1:** added the outside-specialist branch (referral relations) · made
"schedule the MRI" an explicit step · book-both-same-call · auth + order intake ·
standardized callback promise · direct-scheduling default · capture + call tags ·
added Situation #0 (current patients) · [VERIFY] flags.

---

## Situation #0 — Current patient calls to schedule an ordered MRI

Most common call. Schedule it (or warm-assist per the Call Center notes), confirm their
follow-up appointment exists ≥3 days after the MRI [VERIFY read SLA below], and confirm
insurance authorization status. Done.

---

## Situation #1 — NOT a current patient, has an MRI order from an outside provider

### Step 1 — Find out who's managing the problem
Ask: **"Which provider ordered your MRI — and are they planning to treat this, or did they
say you'd need a specialist?"**
(Orders come from PCPs, urgent care, the ED, chiropractors, neurologists, pain clinics —
the fork is *who manages next*, not just "ortho vs PCP.")

### Branch A — Ordered by a specialist who is managing the care (outside ortho / spine / neuro / pain)
1. **Schedule the MRI.** We're glad to do their imaging.
2. Confirm the order is in hand (fax/portal/photo — see intake note below) and that
   **results route to the ordering provider**.
3. **Do NOT offer a follow-up with our specialists.** Their provider is managing the case —
   and outside orderers are referral relationships we protect.
4. If the patient *asks* whether our doctors can see them: yes — that's the second-opinion
   path. "Bring your MRI — our specialists review outside imaging."

### Branch B — Ordered by a PCP / urgent care / ED (no specialist managing yet)
1. **Schedule the MRI.**
2. **In the same call**, offer the follow-up with the right Orthopedic or Spine provider to
   review results — booked **at least 3 days after the MRI** [VERIFY: radiologist read
   turnaround actually beats 3 days — if not, adjust the gap]. Book both before hanging up.
3. Suggested line: *"Let's get both on the calendar — the MRI, and a visit where a
   specialist walks you through exactly what it shows and what to do next. Your PCP gets
   the results too."*
4. If they decline the follow-up: *"No problem — if your results show anything that needs a
   specialist, call us and we'll get you in quickly."* **Record the decline** (see capture).

### Both branches — order + authorization intake
- Collect the order (fax, portal, or photo) before the appointment.
- Ask: **"Has your doctor's office obtained insurance authorization, or should we check on
  that?"** [VERIFY: who owns prior auth for outside orders — us or the ordering office?
  Script the answer once ops confirms.]

---

## Situation #2 — Wants an MRI, has NO order, not a current patient

### Step 1 — Determine the need
Ask: What body part? Is it an orthopedic or spine problem?
[VERIFY: our MRI scope — if a caller needs non-musculoskeletal imaging (brain, abdomen),
what do we say? Script the referral-out line once confirmed.]

### Step 2 — Who sent them
Ask: **"Who told you that you needed an MRI?"** — and **record the answer** (ED, urgent
care, PCP name). These sources referred them to our *specialists* to evaluate and order the
right study — not to book imaging directly. (The names feed the physician-liaison team.)

### The why-script (this is the booking-maker — Mitch's approved wording, 7/22)
*"Not everyone actually needs an MRI — and an order has to come from a provider anyway.
The fastest path is to see our specialist first and make sure you need one. If you do, we
can order it, perform it, and review it with you — we're with you every step of the way."*
→ **Schedule the evaluation with the appropriate Orthopedic or Spine specialist.**

### If the patient declines an appointment
Suggested line (say the next step, don't recite the rule): *"I wish I could book it
directly, but an MRI needs a provider's order. The visit is the quickest way to get one —
often within the week."* ⏳ACCESS — only promise speed scheduling can deliver.
- **Self-pay exception:** [VERIFY with compliance/imaging leadership BEFORE using: can we
  perform a self-pay MRI with no provider order at all, or does policy still require an
  order (e.g., via our medical director)? Script this branch only after the answer.]
  If permitted: schedule the self-pay MRI (quote from the current self-pay price sheet) and
  offer the results-review visit with one of our specialists.

---

## Notes for the Call Center

1. **Default = schedule it yourself.** If you're trained on MRI scheduling, book it directly
   — do not transfer. Transfer is the exception, not the norm. (Unsure? Ask your Lead for
   the training — that's the goal state for everyone.)
2. If you must transfer: set the expectation honestly — *"You may reach the MRI team's
   voicemail; leave your name and number and they'll call you back by the next business
   day."*
3. **Capture, every MRI call:** referral source (who sent/told them) · outcome tag —
   `MRI scheduled` / `eval booked` / `declined` / `transferred` — so this funnel is
   measurable in Liine. [Paul adds the tags.]

## Notes for MRI Locations

1. Voicemail greeting clearly identifies the MRI Department.
2. Ask callers for name and number; **promise: callback by the next business day** — one
   promise, same as the call center's line. (Replaces "within 24 hours" — a Friday call
   can't be returned in 24.)
3. Log callbacks with the same outcome tags.

---

## Why the wording matches the website (for reviewers)

The website's imaging module (approved by Mitch 7/22) says: have an MRI → *"we'll review it
with you and decide next steps together"* · no MRI → *"see us first and make sure you need
one… if you do, we can order it, perform it, and review it with you."* The scripts above are
the spoken version of the same two branches. One vocabulary across website, call center, and
triage — that's the routing-intelligence rule.

**Open verifies before rollout:** ① self-pay-without-order policy · ② prior-auth ownership
for outside orders · ③ read-turnaround vs the 3-day gap · ④ MRI scope for non-MSK requests.
