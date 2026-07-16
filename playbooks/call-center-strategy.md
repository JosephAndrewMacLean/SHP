# Call Center / Patient Access Strategy

**Owner:** Kelly (call center / centralized scheduling) → reports to Joe · **Analytics:** Santosh ·
**Tracking infra:** Paul · **Sponsor:** Gautam
**Purpose:** turn the phone room from a booking desk into a **qualified-conversion engine** — the
single highest-leverage, lowest-cost lever on the spine number, because demand is already arriving
and not converting.

> Grounds in `brand/current-state.md` and `playbooks/spine-90day-plan.md`. SHP is **phone-driven**:
> ~60–80% of new patients are consumer/self-directed and a **13-person centralized call center** is
> the front door. That means the phone room, not just paid media, decides the conversion rate.

---

## Why this matters now (the data)
- **Volume is arriving but not converting.** Spine landing-page visits rose +44% and CTR climbed,
  yet new patients/day barely moved (6.8→7.2). The drop-off is happening **after the click / at the
  phone**, not upstream.
- **Patients are routing around the phones.** 166 canceled/no-show patients later **self-rescheduled
  online and kept the visit** — a direct signal of phone/access friction and lost bookings the team
  never sees.
- **Attribution is captured by hand.** "How did you hear about us?" is asked on only **60–70%** of
  calls; a liaison spends **6–8 hrs/week manually listening to calls** to identify referral sources.
- **Qualification isn't happening up front.** SHP takes **no Medicaid** and has surgical vs.
  conservative pathways — but insurance/candidacy isn't screened before booking, so mismatched
  patients consume surgeon slots and inflate no-shows/cancels.
- **Systems are fragmented** (NextGen, OrthoPlex, Accel, AutoFlow, E-Intake; clinical schedule via
  Kelly, surgical via Anna) and **Line conversion tracking is currently non-functional** (compliance fix in progress).

---

## The 6 strategy pillars

### 1. Access & speed-to-answer (stop the leak)
- Set and monitor **speed-to-answer, abandonment rate, and callback SLA** (target: answer < 30s,
  abandonment < 5%, callback < 1 business hour).
- **Recover the self-reschedulers:** build a daily worklist of canceled/no-show patients and
  proactively re-book them; treat the 166-patient signal as a standing recovery queue.
- **Protect same-week spine slots** for both consumer and referral demand (same-week access is the
  brand differentiator — the phone room must be able to deliver it).
- After-hours / overflow coverage so no qualified call goes to voicemail.

### 2. Qualification at intake (the conversion lever)
- **Insurance pre-screen on every call.** Accepted plan → book. **No Medicaid / non-covered →
  route to Harmony Health Direct Pay** (don't lose the patient; offer financing) rather than a dead end.
- **Clinical candidacy triage:** a short symptom/red-flag script that sorts spine callers into
  **conservative/interventional** vs. **surgical** intent, and books them into the right pathway.
- **Route to the right physician/location** using the roster and the routing rubric — including
  steering surgical candidates to the **higher-converting spine surgeons** (see spine plan §4A).
- **Definition of a "qualified booking":** accepted insurance (or direct-pay accepted) + correct
  service line + correct physician/pathway. Track qualified-booking rate, not just bookings.

### 3. Attribution capture (make the data clean at the source)
- Make **"How did you hear about us?" a required, scripted field** — no call closes without it.
- **Stop the referring-physician field being overwritten** by billing; add a change log; map the
  call-center source taxonomy to **Map My Customer** and **NextGen** so PLs stop "spraying and praying."
- Kill the manual 6–8 hrs/week of call-listening by capturing source at intake (+ AI assist, pillar 6).

### 4. Booking-channel optimization
- **Push appropriate demand to the free website booking path** (75% capture at $0 vs. paid Zocdoc
  ~52–57%) — but keep a human path for complex/insurance-sensitive spine cases.
- Fix the phone→booking handoffs across the fragmented scheduling tools; a single intake script
  regardless of which backend books.
- **Do not judge paid-media changes until Line tracking is fixed** — the phone room's conversions
  must be attributable before bidding moves.

### 5. Scripts, QA & coaching
- One standard **greeting → qualify → route → book → capture-source** script per service line, spine first.
- **Call scoring / QA rubric** (qualification done? routed right? source captured? same-week offered?)
  with weekly coaching. Separate **activity** (calls handled) from **outcome** (qualified bookings kept).

### 6. AI implementation (the planned upgrade)
- Deploy AI for **call summarization + automatic source detection** (removes the manual listening),
  **after-hours triage/booking**, overflow deflection, and QA scoring at scale.
- Sequence AI **after** the script/qualification/attribution foundations exist — automate a good
  process, not a broken one.

---

## Metrics dashboard (weekly)
Speed-to-answer · abandonment rate · callback SLA hit-rate · **qualified-booking rate** · booking→kept
(show) rate · no-show/cancel rate · **self-reschedule recovery count** · **source-capture % (target 100%)** ·
same-week spine fill · direct-pay conversions from Medicaid/non-covered callers.

## 30 / 60 / 90 action plan
- **Days 1–30:** ship the qualify→route→capture spine script + insurance pre-screen; make source a
  required field; stand up the self-reschedule recovery queue; set access SLAs + dashboard; unblock Line tracking.
- **Days 31–60:** QA scoring + coaching live; MMC↔NextGen source crosswalk; protected same-week spine
  slots operational; direct-pay routing for non-covered callers; measure qualified-booking rate.
- **Days 61–90:** deploy AI (summarization/source detection/after-hours); tune booking-channel mix;
  report qualified-conversion lift into the spine scorecard.

## Guardrails
No PHI beyond the minimum necessary · HIPAA-compliant call recording + consent · accurate
insurance/direct-pay/financing statements (no guarantees) · never promise same-week access the
schedule can't deliver (top sentiment risk).
