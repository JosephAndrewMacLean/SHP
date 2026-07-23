# Working-Session Outcomes — Spine · MRI · Pain × Call Center

**Session held:** 2026-07-22 · **In the room:** Joe, Kelley, Mitch · **Recap email:** sent by
Joe (text preserved in §6) · **Status:** decisions recorded; follow-ups in flight.
**Supersedes:** the proposal sections of `spine-imaging-pain-call-center-scheduling-meeting.md`
(the straw man served its purpose — what's below is what was actually decided).

---

## 1. The three decisions

**Decision 1 — Spine-first routing for neck/back symptoms.**
For callers with neck- or back-related symptoms — numbness, tingling, pain traveling down an
arm or leg, back pain, or requests for back injections — the default is to **think Spine
first** and get the patient in front of a Spine provider whenever appropriate, rather than
losing them to wherever they initially thought they needed to go.
*Resolves:* the routing-door question the call data raised (C5, C13); supports the
service-line tagging intent (D7 — spine-adjacent bookings should count as Spine on the
scorecard; Santosh still to wire).

**Decision 2 — No-order MRI callers: Spine consult first, cash-pay MRI as the fallback.**
When a caller wants an MRI but has no order: the call center **first offers an appointment
with a Spine provider** (the visit that generates the order and keeps the patient in-system).
If the caller isn't interested, offer the **cash-pay MRI route and transfer to MRI**, telling
them plainly that they may need to leave a voicemail and will get a callback.
*Resolves:* D3 (route-don't-refuse — adopted in a Spine-first form; the C6/C11/C19/C28-type
caller now has a real path). Affirms the cash-pay route as a legitimate offer (D19's price
card is still needed so the quote is consistent).

**Decision 3 — MRI scheduling stays with the MRI team.**
The call center will **not** take on MRI scheduling. Keeping the process with the MRI team
keeps it cleaner and easier to support. The seam improves via Mitch's voicemail follow-ups
(below) and honest expectation-setting at transfer.
*Resolves:* the imaging-scheduling structure question — decided as "keep separate, strengthen
the seam." The shared pending-imaging queue proposed in the meeting package was **not adopted
at this time**; the meeting doc's guarantee stands and is now simply fact: imaging scheduling,
safety screening, protocols, and capacity remain entirely with Mitch's team.

## 2. Follow-ups by owner

| Owner | Item | Notes |
|---|---|---|
| **Kelley** | Roll Spine-first routing + the MRI conversation into call-center training | Training-ready language in §3; ties to CC-A.5 (train once) |
| **Kelley** | Use the reviewed example call as a coaching opportunity | The agent's instinct (get the patient to Spine) was right; adjust how the referral conversation is handled so patients aren't lost |
| **Mitch** | Review the MRI voicemail process — messages checked consistently, callbacks timely | See §4 watch items for the specific failure modes the data flagged |
| **Mitch** | Update the MRI voicemail greeting so patients know exactly what to expect | Welcome + what happens next + when they'll hear back |
| **Joe** | Investigate how a call ended up in **Medical Records** instead of the call center; close the loop | IVR routing item — fold into the D15 phone-tree review |

## 3. Training-ready language for the two decided flows (DRAFT — Kelley owns final wording)

**Spine-first routing (Decision 1).** Trigger symptoms/requests: neck pain · back pain ·
numbness or tingling · pain traveling down an arm or leg · back-injection requests.
> "It sounds like our Spine team is the right place to start — they handle exactly this, and
> they can see you [soonest real availability]. Let me get you set up with one of our Spine
> providers."
Guardrails unchanged: reps route, they don't diagnose; the red-flag screen still cannot run
until the escalation path is named (D1 — with Katie); soonest **real** slot only.

**No-order MRI conversation (Decision 2).**
> "The fastest way to get the right scan is to start with one of our Spine providers — they
> can evaluate you, order exactly the right MRI, and it all happens here under one roof. Can I
> set that up for you?"
If declined:
> "No problem — we also offer a self-pay MRI option. I'll transfer you to our MRI team to go
> over pricing and scheduling. A heads-up: you may reach their voicemail — leave your name and
> number and they'll call you back."
(Consistent cash pricing for that conversation still needs the D19 price card — Mitch + Greg.)

## 4. Watch items — making the decided flows succeed (from the call data, not re-litigation)

- **The voicemail leg is the fragile link in Decision 2.** The data showed one MRI-path
  mailbox that was **never activated** (C28) and a cash shopper who hit two voicemails in two
  calls (C28/C29). Suggest Mitch's review include: confirm every MRI transfer target's
  mailbox is live, set a stated callback window in the new greeting (and beat it), and a
  daily check cadence.
- **Capture before transfer.** If the rep logs name + number *before* transferring a
  no-order caller, nobody is lost even if the voicemail leg hiccups — one sentence of
  training that protects the whole flow (and feeds the source question when it ships).
- **Tagging keeps score.** Spine-first routing only shows up in the spine number if the
  booking is tagged Spine — the D7 wiring with Santosh becomes more valuable, not less.

## 5. Still open — routed onward per the meeting package (§8B), unaffected by this session

Red-flag escalation path (**Katie** — blocking the screen) · pain-access policy questions
(**Dr. Oddo + Katie** — Joe carries, with the 1:1 first) · source-capture standard + tag set
(**Kelley + Santosh**) · fax/pending-order handling and capacity truth for imaging (**Mitch**,
at his pace, per Decision 3) · facility payer + cash price cards (**Greg + Mitch + Kelley**) ·
on-hold audio claims substantiation + IVR review, now including the Medical Records misroute
(**Joe + compliance + vendor**).

## 6. Joe's recap email (the record)

> Hi Kelley and Mitch,
> Thanks again for taking the time to meet yesterday. I thought we had a productive discussion
> and landed on a few changes that should help us capture more Spine patients while making
> things simpler for both our patients and the call center.
> A few takeaways I wanted to recap:
> - For neck and back-related symptoms, our default should be to think Spine first. That
>   includes patients calling about numbness, tingling, pain traveling down an arm or leg,
>   back pain, or back injections. The goal is to get them in front of a Spine provider
>   whenever appropriate rather than losing them because of where they initially think they
>   need to go.
> - For patients requesting an MRI without an order, we'd like the call center to first offer
>   an appointment with one of our Spine providers. If the patient isn't interested in that
>   option, we can then offer the cash-pay MRI route and transfer them to MRI, while letting
>   them know they may need to leave a voicemail for a callback.
> - We also agreed that the call center shouldn't take on MRI scheduling itself. Keeping that
>   process with the MRI team keeps things much cleaner and easier to support.
>
> A few follow-up items:
> Kelley
> - Roll the Spine-first routing approach and MRI conversation into call center training.
> - Use the example call we reviewed as a coaching opportunity. The agent had the right
>   instinct by trying to get the patient to Spine—we just want to adjust how we handle the
>   referral conversation so we don't lose patients unnecessarily.
> Mitch
> - Review the MRI voicemail process with the team to make sure messages are being checked
>   consistently and patients are receiving timely callbacks.
> - Update the MRI voicemail greeting so patients know exactly what to expect when they reach
>   the department.
>
> Lastly, let's also look into how one of the calls ended up in Medical Records instead of the
> call center so we can close that loop.
> I appreciate everyone's willingness to work through these scenarios together. I think these
> are relatively small changes that can make a meaningful difference in both the patient
> experience and our ability to keep Spine patients within our system.
> Thanks,
> Joe

## 7. Document impacts

- `pm/spine-intake-qualification-script.md` → needs a **v1.1** pass: add the Spine-first
  symptom triggers (Decision 1) and the no-order MRI conversation (Decision 2) as scripted
  branches; keep all v1.0 guardrails (no clinical triage, red-flag screen pending D1,
  accurate money statements).
- `pm/spine-imaging-pain-call-center-scheduling-meeting.md` → marked **session held**; §7's
  queue design recorded as not adopted at this time (Decision 3).
- `pm/spine-imaging-pain-call-review-pack.md` → remains the evidence base; Kelley + Mitch
  corrections/co-sign still welcome for v1.1 of the pack.
- `pm/email-kelley-mitch-meeting-prep.md` → superseded (meeting held; recap sent).
