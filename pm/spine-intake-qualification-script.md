# Spine Intake — Qualification + Routing Script (Call Center)

**Owner:** Kelly (call center) · **Advisor:** Patient Access Mgr · **Sponsor:** Joe / Gautam
**Feeds:** Spine 90-day plan §4A (Qualification & Routing) · Call Center Strategy Pillars 2, 3, 5
**Version:** v1.0 · 2026-07-17 · **Status: DRAFT — clinical triage + routing PENDING Katie / clinical sign-off**

> **Read before using.** This is a *triage-and-route* script, not clinical advice. Reps do not
> diagnose, do not interpret symptoms, and do not tell a caller whether they need surgery. Reps
> ask scripted questions and route to the right door. Anything that sounds like clinical judgment
> is a red-flag → escalate/route, never advise.
>
> **Three hard guardrails, every call:**
> 1. **HIPAA minimum-necessary** — collect only what's needed to qualify + route. No detailed
>    medical history over the phone.
> 2. **Never promise same-week access the schedule can't deliver.** Offer the *soonest real* slot
>    the system shows. "Same-week when available" — never a blanket guarantee.
> 3. **Accurate money statements only** — insurance, direct-pay, and financing described as they
>    truly are. No coverage promises, no "it'll be covered," no quoted out-of-pocket the rep can't verify.

---

## SECTION 1 — THE CALL FLOW (read this)

### Step 0 · Recording consent + greeting
> "Thank you for calling Synergy Health Partners, this is **[Name]**. This call may be recorded
> for quality. How can I help you today?"

- If the caller objects to recording, follow the standard no-record transfer/handling process.
- Do **not** collect clinical detail before you know why they're calling.

### Step 1 · Reason for call (identify spine, capture the basics)
> "I can help with that. So I get you to the right specialist — are you calling about **neck or
> back pain, or another area**?"

If neck/back/spine-related, continue this script. Capture minimum-necessary:
- First/last name, DOB, callback number, ZIP (for location routing), reason in the caller's words.

> "And is this something **new** you'd like to be seen for, or **follow-up** on care you've already
> had here?"

New patient → continue. Established → route to their existing provider's scheduling.

### Step 2 · INSURANCE PRE-SCREEN (do this before booking — it's the conversion lever)
> "Before I find you the soonest appointment, let me make sure we're **in-network** so there are no
> surprises. **What insurance will you be using?**"

Capture: carrier + plan type (e.g., "Blue Cross PPO," "BCN HMO," "Medicare"). Then branch.

> **✅ Real accepted-plans list (from the Feb 2026 insurance taxonomy — 29 carriers / 2,333
> provider-location-plan rows; source of truth is the WordPress `insurance_carrier` taxonomy).**

**Branch A — Accepted COMMERCIAL (PPO/HMO) → PROCEED, but check referral (2b).**
Aetna · **Blue Cross Blue Shield of Michigan (PPO + BCN HMO)** · Cigna · Cofinity/PPOM ·
Coventry/First Health · HAP · Humana · McLaren · Molina · MultiPlan/PHCS · Priority Health · United Healthcare.
> "Great — we're in-network with that. Let me get you booked."

**Branch A2 — Accepted MEDICARE → PROCEED (no referral).**
Traditional Medicare (A&B) · Medicare Advantage: Aetna, BCN Advantage*, HAP, Humana, Meridian,
Molina, Priority Health, UHC/AARP. (*BCN Advantage = HMO → needs referral, see 2b.)

**Branch A3 — AUTO ACCIDENT / WORKERS' COMP → PROCEED (no referral, and no copay for auto).**
Michigan No-Fault PIP (all carriers) and Workers' Comp (all carriers) are accepted — this is a
**high-value spine channel**. Capture the claim basics: carrier, **claim #**, **adjuster name/phone**,
date of injury (auto: + police report if available; WC: + employer name).
> "Because this is an auto/work injury, it's covered under your [PIP / workers'-comp] claim — I just
> need a few claim details and I'll get you scheduled."

**2b · REFERRAL CHECK — HMO plans need a PCP referral BEFORE the visit. Flag it, don't lose them.**
Referral required: **BCN HMO · HAP HMO · McLaren HMO · Priority Health HMO · BCN Advantage.**
(PPO, Traditional Medicare, Self-Pay, Auto, WC = **no referral**.)
> "That plan needs a **referral from your primary-care doctor** before we can see you. I can still
> hold you the soonest spine slot — reach out to your PCP for the referral and we'll confirm it. Want
> me to hold that time?" → book as **referral-pending**; note it so the visit isn't denied.

**Branch B — MEDICAID → VERIFY, don't reflexively decline. Acceptance VARIES BY PROVIDER.**
Medicaid plans in the taxonomy: Blue Cross Complete · HAP Empowered · Meridian Medicaid · Molina
Medicaid · Priority Health Medicaid · McLaren Medicaid — but **accepted only at select providers,
not universally** (and not necessarily by every spine physician).
> "Let me check which of our spine providers is in-network with your Medicaid plan — I don't want to
> book you somewhere it isn't covered. Let me confirm and I'll lock in your time."
- If a spine provider accepts it → book to **that** provider. If none does → offer **Harmony Health
  Direct Pay + financing** (Branch C). **Never quote a flat "we don't take Medicaid" — verify first.**

**Branch C — Uninsured / self-pay / truly out-of-network → DO NOT DEAD-END.**
> "We don't want that to stop you from getting care. We have a **Direct Pay program through Harmony
> Health** with transparent up-front pricing and **financing** to spread the cost. Want me to go over
> it and get you scheduled that way?"
- **Yes** → book as **Direct-Pay** (tag per Section 3). **Unsure** → hand to the direct-pay coordinator
  + **log the lead, don't let it fall off.** Out-of-network callers: note many plans still reimburse
  partially and billing can provide an estimate — don't turn them away.
- **Accuracy guardrail:** describe Direct Pay/financing only as they truly work; **no** unverified price
  or rate; never imply Direct Pay is "insurance."

> **Verification note:** in-network status varies by plan sub-type, physician, and facility (surgery
> centers/imaging differ). If unsure, say "let me confirm we're in-network and I'll lock in your time"
> — treat as **needs-verification**, never a guess or a hard no. Prior auth (MRI/injections/surgery)
> is handled by SHP after the consult (3–7 business days) — reassure, don't over-explain.

### Step 3 · RED-FLAG + CANDIDACY TRIAGE (short symptom screen — sort the door, don't diagnose)
> "A couple quick questions so I get you to the **right kind of spine specialist**."

**3a · RED-FLAG SCREEN — ask first, every spine caller. Any YES = urgent path, stop normal booking.**
> "Are you **right now** experiencing any of the following?"
> - New **loss of control of your bladder or bowels**
> - New **numbness in the groin/inner-thigh (saddle) area**
> - **Sudden, severe weakness** in a leg or arm — or trouble walking that came on fast
> - Spine pain **with fever, or after a recent serious fall or accident**
> - Unrelenting pain that is **severe and getting rapidly worse**

**If ANY red flag = YES → do NOT book a routine slot.**
> "Those symptoms can need to be looked at **urgently**. **If this is a medical emergency, please
> hang up and call 911 or go to the nearest emergency room now.** If you're safe to stay on, let me
> get a clinical staff member to speak with you right away."
- Warm-transfer / escalate per the **urgent spine escalation path** (clinical triage line / nurse).
  Never send a red-flag caller into a routine future-dated appointment. **Escalation contact:
  [Kelly/clinical to confirm — PENDING].**

**3b · CANDIDACY / INTENT SCREEN — only if no red flags. Sorts conservative/interventional vs. surgical *intent* (not a diagnosis).**
> "Have you already had **imaging** — an MRI or CT — for this?" (Y/N + when/where if easy)
> "How long has this been going on — **weeks, or months and ongoing**?"
> "Have you already tried treatment like **physical therapy, injections, or seen a spine doctor** for it?"
> "Has any doctor **already talked to you about spine surgery**, or are you mainly looking for relief
> and to find out what's going on?"

Use answers to pick the **door** (see routing rubric, Section 2). Default posture: **when unsure,
route to the conservative/interventional front door** — it keeps the patient in-system and lets a
physician determine surgical candidacy. Reps never decide "you need surgery."

### Step 4 · ROUTE TO THE RIGHT PHYSICIAN / PATHWAY
Apply Section 2 rubric. Match to service line = **Spine**, then door (conservative/interventional
vs. surgical), then a specific physician + location near the caller's ZIP.
> "Based on that, the right fit is our **[interventional pain / spine surgery] team** — I'd get you
> in with **Dr. [Name]** at our **[location]** office."

### Step 5 · OFFER THE SOONEST SAME-WEEK SPINE SLOT (real availability only)
> "Let me find you the **soonest opening**… I have **[day/time]** — does that work?"

- Offer the earliest genuinely-available spine slot the system shows. Same-week is the SHP
  differentiator — **use protected same-week spine slots when available**, but **only offer what the
  schedule actually holds.** No "we can always get you in this week" if it isn't true.
- If nothing same-week fits the caller, offer the next real opening + the **online self-schedule**
  option (patients who book around the phone are keeping visits — make the online path easy, not a
  fallback for our friction).

### Step 6 · CAPTURE "HOW DID YOU HEAR ABOUT US?" (REQUIRED — no call closes without it)
> "One last thing so we can keep improving — **how did you hear about us?**"

- **Required field. 100% capture target.** Do not skip, do not guess.
- Log to the standard source taxonomy (see Section 3). If a **referring physician/practice**, capture
  the **practice name** — this feeds the referral engine and must not be left blank or overwritten.

### Step 7 · CONFIRM + SET EXPECTATIONS
> "You're all set: **Dr. [Name]**, **[day/time]**, at **[location]**. You'll get a confirmation by
> [text/email]. Please **bring your insurance card / photo ID**, arrive **15 minutes early** to
> complete intake, and **bring any prior MRI/CT images or reports** if you have them. Anything else
> I can help with?"

- Set honest expectations: what to bring, arrival time, and that the first visit is an **evaluation**
  (not a promise of a specific treatment or surgery). No outcome guarantees.

---

## SECTION 2 — ROUTING RUBRIC (real roster)

> **DRAFT — clinical routing PENDING Katie / clinical approval. Reps follow the approved table; they
> do not exercise clinical discretion beyond it.**

### Door 1 — Conservative / Interventional (the front door; keeps patients in-system)
Use when: no red flags, seeking relief/diagnosis, **no surgeon has recommended surgery**, or unsure.
Also the default when intent is unclear.

| Physician | Role |
|---|---|
| **Anthony J. Oddo, DO** | Director of Pain Management — spine pain, injections |
| **Kevin R. Lee, MD** | Pain mgmt + functional neurosurgery — minimally invasive |
| **Brian Kassa, DO** | Fellowship-trained pain mgmt — spine & joint interventions |
| **Hanish Singh, MD** | Pain mgmt — spine diagnostics, injections |

### Door 2 — Surgical
Use when: a physician has **already recommended/discussed spine surgery**, imaging shows a surgical
problem *and* the caller is seeking surgical consult, or a clinician escalates them here.

| Physician | Role |
|---|---|
| **Scott McCarty, MD** | Spine surgeon — integrated spine team |
| **Joseph Maslak, MD** | Board-certified, fellowship-trained (Cleveland Clinic) |
| **Jeffrey Varghese, MD** | Spine surgeon — deformity + minimally invasive (HSS background) |

### Surgical routing guidance — **higher-converting surgeons** (PENDING CLINICAL SIGN-OFF)
The spine plan directs surgical candidates to the **higher-converting** surgeons —
**McCarty / Maslak / Varghese** — to reduce wasted top-of-funnel. This is a **clinical/ops decision,
not rep discretion.**

- **Dr. Salar's surgical candidates:** the plan flags redirecting **Dr. Mohamed Salar's** *surgical*
  candidates to McCarty/Maslak/Varghese (Salar absorbs ~21% of spine NPs but converts very few to
  surgery). **This is FLAGGED for Katie / clinical approval — reps do NOT redirect on their own.**
  Until signed off, follow the currently-approved assignment. If a caller specifically requests Dr.
  Salar, honor it (see Section 5).
- Other spine physicians in the roster (**Zamorano — neurosurgeon; Munk**) exist; **route to them only
  per the clinically-approved rubric**, not rep guess.

### Location routing
Match to the caller's ZIP / nearest office (Livonia, Sterling Heights, Southfield, Troy, Rochester,
+ others). Balance "soonest same-week slot" against a reasonable drive. Troy/Southfield are growth
offices — book there when it's the right fit and gets the patient in sooner.

---

## SECTION 3 — DEFINITION OF A "QUALIFIED BOOKING" + how to tag it

A booking counts as **qualified** only if **all three** are true:

1. **Money is sorted** — accepted insurance verified/plausibly in-network **OR** enrolled in
   **Harmony Health Direct Pay** (Medicaid/non-covered/uninsured routed, not lost).
2. **Correct service line** — booked as **Spine** (not mis-slotted into general ortho/pain).
3. **Correct physician / pathway** — right door (conservative-interventional vs. surgical) per the
   approved rubric, at a workable location.

**Plus (required for a clean record, not part of the 3-part definition):** "how did you hear about
us" captured.

**How the rep tags it (in the intake tool / NextGen booking):**
- `Service line = Spine`
- `Door = Conservative-Interventional | Surgical`
- `Payer path = Commercial/Medicare (accepted) | Direct-Pay (Harmony) | Needs-verification`
- `Source = [taxonomy value]` (Website · Google · Referral: [practice] · Zocdoc · Word-of-mouth ·
  Returning · Event · Other)
- `Qualified booking = Y/N` (Y only if the 3 conditions above are met)
- Red-flag escalations are tagged `Urgent-escalation` and are **not** counted as a routine qualified booking.

> Report the **qualified-booking rate**, not raw call/booking volume. That's the number that maps to
> the spine plan's "qualified volume, not raw volume" thesis.

---

## SECTION 4 — QA SCORING RUBRIC (0–100)

Score a sample of recorded calls weekly; coach to the gaps. Five equally-weighted dimensions, 20 pts each.

| # | Dimension | What earns full 20 | Points |
|---|---|---|---|
| 1 | **Insurance qualified?** | Asked payer up front; correctly identified accepted vs. Medicaid/non-covered; routed non-covered to Harmony Direct Pay instead of dead-ending | /20 |
| 2 | **Candidacy triaged?** | Ran the **red-flag screen** on a spine caller; ran the intent/candidacy questions; escalated any red flag correctly (911/clinical, no routine booking) | /20 |
| 3 | **Routed right?** | Correct service line = Spine + correct door (conservative-interventional vs. surgical) + sensible physician/location per the approved rubric | /20 |
| 4 | **Same-week / soonest slot offered?** | Offered the soonest genuine slot; used protected same-week spine slot when available; **no over-promise** of speed the schedule can't hold | /20 |
| 5 | **Source captured?** | "How did you hear about us" asked and logged to taxonomy; referring practice name captured if applicable | /20 |
| | **TOTAL** | | **/100** |

**Auto-fail overrides (score the call ≤ 40 regardless of points):**
- Missed a stated **red flag** (booked a routine slot for a saddle-anesthesia / bladder-bowel / acute-weakness caller).
- **Promised coverage or a specific out-of-pocket** the rep couldn't verify, or promised same-week that didn't exist.
- Dead-ended a **Medicaid/non-covered** caller with no Harmony Direct Pay offer.
- Collected excessive clinical history (HIPAA minimum-necessary breach) or gave clinical advice beyond triage.

**Coaching cadence:** weekly per Call Center Strategy Pillar 5 — separate **activity** (calls handled)
from **outcome** (qualified bookings kept).

---

## SECTION 5 — OBJECTION / EDGE-CASE HANDLING

**"I have Medicaid" / "I don't have insurance" / plan not accepted**
> "We're not in-network with that plan for this, but we have a **Direct Pay program through Harmony
> Health** with up-front pricing and **financing** so cost doesn't stop your care. Want me to walk
> you through it and get you scheduled?"
Route to Harmony Direct Pay; log the lead; never dead-end. Don't quote unverified prices.

**"I want to see a specific doctor" (incl. Dr. Salar)**
> "Absolutely — I can book you with **Dr. [Name]**."
Honor caller-requested physicians, including Dr. Salar. Do **not** redirect a requested surgeon on
your own — the Salar-redirect guidance is a clinical decision pending Katie's sign-off, and it does
not override a patient's explicit request. If their requested doctor's soonest slot is far out, offer
the earliest alternative *as an option*, not a switch: "Dr. X's next opening is [date]; I also have
[earlier] with Dr. Y if getting in sooner matters — your choice."

**"I'm not sure if I need surgery"**
> "That's exactly what the visit is for — you don't have to know. Let me start you with our **[pain
> management / spine]** team who'll evaluate you and map out options."
Default to the **conservative/interventional front door** unless a surgeon has already recommended
surgery. Reps never tell a caller they do or don't need surgery.

**Red-flag caller who resists urgency**
> "I understand — I still don't want to schedule you weeks out with those symptoms. **If it's an
> emergency, please call 911 or go to the ER.** Otherwise let me connect you to clinical staff now."
Do not book a routine future slot over a stated red flag. Escalate.

**Out of area / far from all locations**
Offer the **nearest** office + telehealth/online options if available; if truly out of service area,
provide honest guidance rather than booking a visit the patient won't keep. Capture the lead + source.

**Caller booking around the phone / already tried online**
Make the **website self-schedule** easy — 166 canceled/no-show patients self-rescheduled online and
kept. Don't treat online as our fallback for phone friction; offer it as a convenience and ensure the
booking is still tagged and source-captured.

**Not sure if their plan is accepted**
Treat as **needs-verification**, not a no. "Let me confirm we're in-network and lock in your time."
Never guess in-network status.

---

## SECTION 6 — DEPENDENCIES & OPEN ITEMS (not owned by the call center)

- **Clinical sign-off (Katie / clinical):** the red-flag list, the triage questions, the surgical
  routing, and the Salar-redirect guidance are **DRAFT pending clinical approval** before go-live.
- **Urgent escalation contact/path:** clinical triage line / nurse target — **Kelly + clinical to confirm.**
- **Accepted-plan list:** now wired from the real Feb 2026 taxonomy (29 carriers; see Step 2 and
  `brand/current-state.md` Payer reality). **Medicaid = accepted at select providers, VARIES — verify
  per spine provider; not a flat "no."** Confirm the current provider-level Medicaid + facility
  participation with billing/RCM and post the accepted-plan card at every rep desk.
- **Harmony Health Direct Pay:** pricing sheet, financing terms, and coordinator handoff — **confirm
  current details** so reps state them accurately.
- **Line conversion tracking:** currently non-functional (compliance fix in progress) — Paul/Santosh.
  Qualified-booking tagging above should be built to reconcile with Line once it's live.
- **Source taxonomy ↔ NextGen / Map My Customer crosswalk:** Santosh — so referral sources stop being
  overwritten by billing.
- **AI assist (source auto-detection, call summarization):** sequence **after** this script is live and
  stable (Call Center Strategy Pillar 6).
