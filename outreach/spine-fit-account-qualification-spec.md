# Spine-Fit Account Qualification — Field Spec for Physician Liaisons + MapMyCustomers Config

**Owner:** Kristen (PL lead) · **Contributors:** Cody, Jasmine · **Data/config:** Joe + Santosh
**Purpose:** Give every liaison one consistent, in-the-field way to judge whether a referring
practice is a good candidate to send **spine** referrals to SHP — and to tag that judgment in
MapMyCustomers (MMC) so we can prioritize, route, and report the book of business by spine fit.
**Status:** ready for team use and for handoff to the MMC vendor to configure.

> **Why this exists.** The Universal Spine Target-Account list is currently **empty (0 accounts
> loaded)**, and today PLs "spray and pray." This spec turns a fuzzy gut call ("good practice") into
> a repeatable tag two different PLs would land on the same way. It supports the realistic mandate:
> a **qualified** spine lift (recover Sean's ~2–3 NP/week, then push ~79 → ~95–110/month), not raw
> volume. See `playbooks/b2b-physician-liaison-strategy.md` and `playbooks/spine-90day-plan.md`.

> **Grounding note.** Feeder types, geography (Livonia, Sterling Heights, Southfield, Troy,
> Rochester, Port Huron), payer taxonomy (Commercial/Medicare accepted; Auto No-Fault PIP + Workers'
> Comp are high-value no-referral spine channels; Medicaid varies by provider; HMO needs a referral),
> and surgeon routing are all **confirmed SHP facts** from `brand/current-state.md` and
> `brand/provider-roster-by-service-line.md`. The **point thresholds and the exact picklist wording**
> below are this team's **proposed operating convention** (assumption) — adopt/tune them in the first
> weekly review, then freeze so tagging stays consistent.

---

## 1. Spine-fit qualification criteria — the vital few

Six signals. Each is observable by a PL on a visit or from a quick pre-call lookup. Nothing here
requires PHI — it's all practice-level.

| # | Signal | What it means | How a PL observes it (no PHI) |
|---|---|---|---|
| **1** | **Spine-generating specialty (feeder type)** | Does this practice actually see back/neck patients it can't keep? | Practice type on the door/website: ortho (non-spine), pain mgmt, chiro, PM&R, PCP, urgent care, PT, ER, WC/PI attorney. Ask "who do you send your back and neck patients to?" |
| **2** | **Spine referral volume potential** | Roughly how many spine patients/month they could realistically send us | Ask patient volume + share with spine complaints; count providers in the practice; watch waiting-room throughput. Estimate a monthly band, don't guess a decimal. |
| **3** | **Relationship strength / where they send today** | Do they know us, trust us, and is their spine referral "up for grabs"? | Are they already sending? To whom? Any SHP champion inside? Do they even know we have a spine bench? |
| **4** | **Distance to nearest SHP spine site** | Referrals track with convenience; too far and the patient won't travel | Drive distance from the practice to the closest spine-capable site (Livonia, Sterling Heights, Southfield, Troy, Rochester, Port Huron). |
| **5** | **Payer fit** | Will the patients they'd send actually be covered / high-value? | Ask their dominant payer mix. **Best:** commercial, Medicare, **Auto No-Fault PIP, Workers' Comp** (no referral, high-value spine). **Watch:** HMO (needs referral), heavy Medicaid (accepted only at select providers — verify). |
| **6** | **Competitive lock-in** | Is their spine referral already captured or structurally unavailable? | Are they employed by / owned by a system (Corewell/Beaumont, Henry Ford)? In-house spine? Exclusive tie to a competitor spine group? |

**Two hard disqualifiers (automatic "Not a Fit," regardless of points):**
- **No spine to send** — the practice does not generate back/neck patients it refers out (e.g., a
  pure hand/foot/derm/cosmetic practice, or a specialty that keeps its own spine).
- **Structurally locked** — system-employed or has an in-house/exclusive spine service, so the
  referral is not winnable on service merit (anti-kickback/Stark: we compete on clinical merit and
  service, never inducements — if it can't be won on merit, it's Not a Fit).

---

## 2. "Spine Fit" custom fields for MapMyCustomers

Create these on the **Account/Company** object (not Contact). One headline field, one conditional
reason field, and five short input fields that make the headline reproducible and bulk-importable.

### 2.1 Headline field (required on every spine account)

**Field name:** `Spine Fit`
**Type:** Single-select picklist

| Value | One-line definition |
|---|---|
| **A – Priority** | Strong spine feeder, winnable, close, good payer mix. Work on a tight cadence now. |
| **B – Develop** | Real spine potential but needs relationship-building, is farther out, or has a payer/volume caveat. |
| **C – Maintain** | Low but non-zero spine yield; keep warm with light-touch cadence. |
| **Not a Fit** | Won't produce qualified spine referrals (no spine to send, locked to a competitor, or wrong payer). Do not spend spine field time here. |
| **Not Yet Assessed** | Default for imported/new accounts before a PL has scored it. Working backlog to qualify. |

*Values are mutually exclusive and ranked, so two PLs land on the same tag.*

### 2.2 Conditional reason field (required only when Spine Fit = Not a Fit)

**Field name:** `Spine Not-a-Fit Reason`
**Type:** Single-select picklist

| Value | Definition |
|---|---|
| **No spine referrals generated** | Practice doesn't see/refer out back/neck patients. |
| **Competitor-owned / employed** | Owned or employed by Corewell/Beaumont, Henry Ford, or another system that captures the referral. |
| **In-house / exclusive spine** | Has its own spine provider or an exclusive tie elsewhere. |
| **Payer mismatch** | Dominant payer mix SHP largely can't serve (verify per provider before finalizing). |
| **Out of area** | Too far from any SHP spine site for patients to travel. |
| **Closed / defunct / bad data** | Practice closed, duplicate, or record is unusable. |

### 2.3 Supporting input fields (drive the score; also power reporting)

Keep these short — they are the observable inputs from Section 1 and let us **bulk-set and audit**
the headline tag.

| Field name | Type | Values / format |
|---|---|---|
| `Spine Feeder Type` | Multi-select | Ortho (non-spine) · Pain Management · Chiropractic · PM&R · PCP / Family Med · Urgent Care · Physical Therapy · ER / Hospital · WC-PI Attorney · Other |
| `Spine Volume Potential (NP/mo)` | Single-select (band) | 0 · 1–2 · 3–5 · 6–10 · 10+ *(estimated qualified spine NPs/month)* |
| `Relationship Strength` | Single-select | None (cold) · Aware · Sending occasionally · Active referrer · Champion inside |
| `Nearest Spine Site` | Single-select | Livonia · Sterling Heights · Southfield · Troy · Rochester · Port Huron |
| `Miles to Nearest Spine Site` | Number | Whole miles (drive distance) |
| `Payer Fit` | Single-select | Strong (commercial/Medicare/Auto/WC) · Mixed · Weak (heavy HMO/Medicaid — verify) |

> **Attribution guardrail.** Do **not** repurpose MMC's free-text/notes for the spine tag — that
> field gets messy and can't be reported on. Use these structured fields only. This also keeps the
> spine flag independent of the referring-physician data that billing overwrites in NextGen.

---

## 3. Scoring rubric — how the six criteria set the `Spine Fit` value

Score the five scorable signals 0–2 each (the sixth, competitive lock-in, is a gate). Max **10 points**.

| Signal | 2 points | 1 point | 0 points |
|---|---|---|---|
| **1. Feeder type** | Ortho / pain mgmt / PM&R / spine-heavy chiro | PCP / urgent care / PT / chiro (general) / ER | No spine referrals generated → **STOP: Not a Fit** |
| **2. Volume potential** | 6+ NP/mo | 3–5 NP/mo | 1–2 NP/mo (0 → **STOP: Not a Fit**) |
| **3. Relationship** | Active referrer / champion | Aware or sending occasionally | Cold / unknown |
| **4. Distance** | ≤ 10 mi to a spine site | 11–25 mi | > 25 mi |
| **5. Payer fit** | Strong (commercial/Medicare/Auto/WC) | Mixed | Weak (heavy HMO/Medicaid) |

**Gate first (Signal 6 + hard disqualifiers):** if the account is competitor-owned/employed, has
in-house/exclusive spine, generates no spine, or is out of area/defunct → tag **Not a Fit** and set
the reason. Do not score further.

**Then map the total:**

| Total points | `Spine Fit` |
|---|---|
| **8–10** | **A – Priority** |
| **5–7** | **B – Develop** |
| **2–4** | **C – Maintain** |
| **0–1** (and not already gated out) | **Not a Fit** (reason: usually low volume or out of area) |

### Quick decision tree (for the field / mobile app)

1. **Do they refer out back/neck patients?** No → **Not a Fit** (No spine referrals generated).
2. **Is the referral winnable?** (Not competitor-owned, no in-house/exclusive spine) No → **Not a Fit**.
3. **Within ~25 miles of a spine site?** No → **Not a Fit** (Out of area) *(use judgment for a big
   feeder just past the line — tag C and note it).*
4. **Score signals 1–5, add up, map to A / B / C.**

> **"Qualified" is the whole point.** A big practice that sends Medicaid-heavy or HMO-without-referral
> volume is a **B or C**, not an A — because those aren't qualified spine NPs. Payer fit and volume
> are weighted deliberately so PLs chase yield, not activity (Kristen ≈ 70 NP/100 visits; team 6–40 —
> this tag is how we point everyone at her kind of accounts).

---

## 4. Rollout notes

### 4.1 Setting it in the field (PLs, day to day)
- On a visit or pre-call, fill the six supporting fields in the MMC mobile app, let the rubric drive
  the `Spine Fit` value, and set it. Takes under a minute once the fields exist.
- **Re-tag on change, not on a calendar.** Bump B→A when a champion emerges; drop to Not a Fit if
  they get acquired by a system. Note the trigger in account notes.
- New/unworked accounts stay **Not Yet Assessed** — that's the qualification backlog to burn down.

### 4.2 Bulk-setting on import (accounts already assessed)
- Build the import spreadsheet with a column per field in Section 2 (`Spine Fit`, `Spine Not-a-Fit
  Reason`, `Spine Feeder Type`, `Spine Volume Potential (NP/mo)`, `Relationship Strength`,
  `Nearest Spine Site`, `Miles to Nearest Spine Site`, `Payer Fit`). **Column headers and cell
  values must match the picklist values in Section 2 exactly** or MMC will reject or blank them.
- For any account Kristen/team have already assessed, pre-fill `Spine Fit` directly; leave the rest
  **Not Yet Assessed** and let PLs score them.
- **Match on import to avoid duplicates** — de-dupe on practice name + address (confirm the exact
  match key with the MMC support contact; see `outreach/mapmycustomers-api-support-email.md` §2–3).
- Ask the vendor to create the picklists **before** the first import so values map cleanly, and to
  set `Not Yet Assessed` as the **default** for `Spine Fit` on all existing/new accounts.

### 4.3 Reporting on it (segment the book of business)
Once tagged, filter/segment the book by spine fit:
- **A/B/C/Not-a-Fit count and mix** — the tiered target-account universe the plan asks for; A = the
  active spine target list, tracked against the "double active spine accounts" goal.
- **Coverage/overlap** by `Nearest Spine Site` (weight Sterling Heights defense + Southfield/Troy ramp).
- **Not-a-Fit reason breakdown** — tells us if we're losing feeders to competitor lock-in vs. payer.
- **Yield check (the real KPI):** cross qualified spine NPs (from the NextGen↔MMC crosswalk, once
  clean) against `Spine Fit` to confirm A accounts actually out-produce B/C — then re-tune the
  thresholds. This closes the loop from tag → qualified NP per 100 visits.

### 4.4 What to hand the vendor
Section 2 (exact field names, types, and picklist values) plus 4.2. That's a complete, unambiguous
config request. Pair it with the open items already drafted in
`outreach/mapmycustomers-api-support-email.md` (custom-field create/read-write, bulk import with
duplicate matching, reporting/filtering on custom fields).

---

## 5. Compliance guardrails (apply to every tag and comm)
- **No PHI** in the tag, notes, or import files — practice-level signals only, never patient detail.
- **Anti-kickback / Stark:** "fit" and "not a fit" are judged on clinical merit, service, and
  logistics — never on payments or inducements. That's why competitor lock-in = Not a Fit rather
  than something to "buy."
- **Payer accuracy:** Medicaid is accepted only at select SHP providers and HMO needs a referral —
  **verify per spine provider** before telling a practice we can serve their patients; don't over-promise.
- **Surgical routing stays clinical:** this tag qualifies the *practice*, not the patient. Routing a
  referred surgical candidate to a higher-converting spine surgeon (spine plan §4A) is a
  clinical/ops decision (Katie + physicians), not a PL field tag.
</content>
</invoke>
