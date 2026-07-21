# PL Visit Messages — What to Say at Every Account

**Date:** 2026-07-21 · **Owners:** Kristen (delivery) + Joe (content) · **Status: DRAFT pending
compliance review** — uses only verified claims (same-week access, integrated ortho+spine under one
roof, 96% recommend rate, deep spine bench incl. interventional front door). Fills tracker **PL-D.1**
(referrer messaging) and pairs with the one-pager.
**Per-account version:** every account's exact message + payer line + named referring providers is in
**`pm/spine-account-enrichment.csv`** (954 accounts) and inside the **Spine Routes app** (tap any stop).

---

## 1. The message architecture (every visit, 90 seconds)

**THANK → OPEN → MESSAGE → ASK**, plus the payer line when scheduling comes up.

1. **THANK** — aggregate only, never a specific patient: *"Your practice has trusted us with N spine
   patients this year — thank you."* Name the top referrer when we know them (the CSV lists each
   account's known referring providers with their individual yield).
2. **OPEN** — a service question, not a pitch: *"What could we do better — access, notes back, anything?"*
3. **MESSAGE** — the practice-type angle (§2). One sentence.
4. **ASK** — one specific behavior (§3), then leave the one-pager + named coordinator + direct line.

## 2. The angle by practice type

| Type | The one sentence |
|---|---|
| PCP | Back/neck patients seen **same week** — imaging, conservative, interventional and surgical under one roof; **we handle HMO referral paperwork with your staff**. |
| Orthopedic (non-spine) | **Co-management:** your patient stays yours — our spine team handles just the spine problem, notes back every visit. |
| Pain mgmt | **Two-way:** we send conservative-first candidates to you; you send surgical-escalation candidates to us; both seen same-week. |
| Chiropractic | Co-management for **plateaued patients** — imaging access, interventional options, surgical consult when warranted; patient returns to your care plan with notes. |
| Urgent care | **Acute back/neck pathway:** your discharge sheet books a spine evaluation same week — one number. |
| PT | Stalled-progress patients get a spine consult + imaging same week, then **straight back to your plan of care**. |
| Attorney (WC/PI) | Auto no-fault & workers' comp spine evaluations — fast scheduling, thorough documentation, clean records turnaround. **Service only, evaluated on clinical merit.** |
| Neurology | Radiculopathy/stenosis patients get imaging + interventional/surgical evaluation same week, closed-loop notes. |
| ER / hospital | Non-emergent spine discharges hold a **same-week clinic slot** instead of bouncing back to the ED. |
| Pediatrics | Adolescent spine (scoliosis, athlete spondylolysis) specialist evaluation; adult family/staff get same-week access. |

## 3. The ask by relationship (evidence band)

| Band | The ask |
|---|---|
| Repeat spine referrer (**Protect**) | *"Anything pending right now we can get seen this week?"* — and fix whatever the OPEN surfaced. |
| One spine patient (**Convert**) | *"How was that experience? Make us your default for the next back/neck patient."* |
| Ortho referrer (**Cross-sell**) | *"Send the next back/neck patient the way you already send knees and shoulders."* |
| Other-patient referrer | *"One spine referral to test the pathway."* |
| Prospect (first touch) | Intro + *"One referral to prove the pathway"* + leave-behind. |
| Lapsed producer (**Recover**) | Lead with ownership: *"We owe you a visit — that's on us."* Then THANK → OPEN. No excuses, one service commitment. |

## 4. Payer qualification — commercial/Medicare vs. Medicaid

Heuristic classification is now stamped on all 954 accounts (`Payer Class` in the CSV + a badge in
the app). **It is an assumption layer, not verification** — Kelly's intake pass verifies Tier 1
first; the gate rules stay as written in the rubric.

| Class | Accounts | Meaning for the PL |
|---|---|---|
| COMM-LIKELY | 679 | Private practice — qualified; confirm HMO share (BCN/HAP/McLaren/Priority HMO need a PCP referral — *"we handle that paperwork with your staff"*). |
| MIXED-SYSTEM | 131 | DMC / Henry Ford / Corewell / Ascension / Trinity / McLaren sites — mixed panel incl. some Medicaid; qualified **with intake screening**. |
| MIXED-WALKIN | 67 | Urgent care — mixed walk-in payers; intake screens each referral. |
| COMM-WCPI | 38 | Chiro — commercial + auto/WC liens welcome; screen Medicaid share. |
| WC-AUTO | 14 | Attorneys — auto no-fault + WC are **commercial-equivalent: no referral, no copay. Qualified by rule.** |
| PEDS | 13 | Payer irrelevant — spine fit is low. |
| **MEDICAID-LIKELY** | **12** | FQHC/community-health pattern — **do NOT promise same-week until eligibility is verified**; Medicaid is select-provider-only at SHP. Uninsured → Harmony Health Direct Pay. |

**The 12 Medicaid-likely flags** (verify before promising access): Community First Health Centers–New
Haven (**currently Tier 1 — keep visiting, it's producing, but verify payer mix this week**), Troy
Health Center, UofM Canton/Livonia/Ypsilanti/Northville Health Centers, Oakland Integrated Healthcare
Network, Henry Ford Macomb Health Center–Fraser, Corner Health Center (Medicaid), MyCare Health
Center–Mt Clemens, Advantage Family Health Center, NuVision Health Center.

## 5. Named-doctor intelligence (what we know today, and the gap)

- **384 producing accounts have named referring providers** with per-doctor 2026 spine/ortho counts,
  parsed from the deterministic referral match (e.g., Park Medical → Dr. Ozog 4 spine; DMC Sports
  Novi → Dr. Meehan; Hesselberg Chiropractic → Dr. Hesselberg 23 spine). These are in the CSV and on
  each stop card in the app — **greet the actual referrer by name.**
- **The other ~570 accounts (mostly prospects) have no named doctors yet.** Fastest fix, no research
  project: **Santosh exports "All People" from MMC (7,821 contacts, already linked to companies)**
  and we join on Company ID — full rosters land in the CSV and app in one refresh. NPI-registry
  enrichment is the fallback for accounts thin in MMC.

## 6. Compliance rails (blocking — same as always)

- **No inducements of any kind** — no payments, gifts, lunches-for-referrals; attorney channel
  especially (AKS/Stark hygiene). Value = service, access, communication.
- **No PHI, ever** — thank in aggregate counts only; never name or describe a patient or case, in
  conversation or in app notes.
- **No superiority or outcome claims** — no "best," no success rates; stick to the verified set
  (same-week access, integrated model, 96% recommend, bench depth).
- **No access promises we can't keep** — HMO plans need referrals; Medicaid-likely accounts need
  verification first; when unsure say *"intake will confirm coverage the same day."*

### Cross-references
`pm/spine-account-enrichment.csv` (per-account message + payer + providers) · Spine Routes app
(message on every stop) · `pm/spine-intake-qualification-script.md` (what intake does with the
referral) · `brand/current-state.md` §Payer reality · tracker PL-D.1.
