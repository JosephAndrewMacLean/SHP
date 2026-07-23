# Mention scoring model — Inferred Patient-Value (IPV)

Every mention the monitor finds is scored **0–100** and dropped onto one ranked
board (the daily digest), so the team works the highest-value signals first instead
of reading 15 source folders. The model lives in **`scoring.py`** and is deliberately
simple and tunable.

> **These scores are heuristic inferences** from the feed folder + the mention's
> headline text — a triage aid, **not** ground truth. They point attention; a human
> decides. No PHI is used; scoring reads only public feed titles.

## What the scale means

The scale is anchored to SHP's **confirmed** business priority (`brand/current-state.md`:
*"new-patient growth in SPINE and ORTHO"*):

- **Top of scale = inferred value to landing new SPINE and ORTHO patients.** A
  metro-Detroit person actively looking for a spine or ortho surgeon is the most
  valuable signal there is.
- **Lower on the scale = FOOT / HAND / PAIN**, whose growth the practice pursues
  mainly through **partnerships / referrals**. Those lines carry a lower baseline but
  get a dedicated **partnership boost**, so a *referral/partnership* signal for foot,
  hand, or pain rises to the top of its band — matching how that value is actually won.
- **Brand reputation and competitor intel** are supporting axes. **Negative brand
  sentiment** is escalated regardless of line (reputation risk → PR).

## How a score is built (additive, transparent)

```
score = LINE points + SIGNAL points + modifiers        (clamped 0–100)
```

**LINE points** — strategic patient-acquisition value of the service line:

| Line | Points | | Line | Points |
|---|--:|---|---|--:|
| Spine | 45 | | Pain | 22 |
| Ortho | 36 | | Foot | 18 |
| Brand (any line) | 30 | | Hand | 18 |
| General | 20 | | Competitor | 10 |

**SIGNAL points** — what kind of mention it is:

| Signal | Points | Meaning |
|---|--:|---|
| Patient demand | 35 | someone seeking care / asking for a surgeon |
| Brand named | 28 | brand named, linked, or reviewed |
| Provider named | 26 | one of our providers named |
| Partnership | 24 | referral-source / partnership opportunity |
| Press / authority | 18 | earned media |
| Competitor intel | 12 | competitor activity |
| Ambient | 8 | background noise |

**Modifiers:**

| Modifier | Points | Trigger |
|---|--:|---|
| Metro-Detroit geo | +8 | Michigan/Detroit/Livonia/… in the text |
| Priority geo | +5 | **Troy / Oakland / Southfield** (the growth unlocks) |
| Help-seeking | +7 | "?", "recommend", "anyone", "second opinion"… |
| Negative sentiment | +12 | complaint/billing/wait/malpractice… → **PR urgent** |
| Foot/Hand/Pain × Partnership | +10 | the partnership lever for those three lines |

### Priority bands

- 🔴 **P1 — act today** (score ≥ 70)
- 🟠 **P2 — this week** (40–69)
- ⚪ **P3 — ambient / FYI** (< 40)

### Worked examples

| Score | Mention | Why |
|--:|---|---|
| **100** | "Anyone recommend a good spine surgeon in **Troy**? Herniated disc, second opinion" | Spine 45 + demand 35 + geo 8 + priority-geo 5 + help 7 |
| **79** | "Dr. Maslak performs minimally invasive spinal fusion in **Livonia**" | Spine 45 + provider 26 + geo 8 |
| **70** | "**Terrible billing** experience at Synergy Health Partners, waited months" | Brand 30 + brand-named 28 + negative 12 → PR urgent |
| **60** | "Podiatry group seeks **referral partnership** with **Detroit** workers-comp clinics" | Foot 18 + partnership 24 + FHP boost 10 + geo 8 |
| **44** | "New bunion treatment option discussed" | Foot 18 + provider 26 (no geo/partnership) |
| **35** | "Detroit Bone & Joint opens new **Troy** orthopedic office" | Competitor 10 + intel 12 + geo 8 + priority-geo 5 |

## How the line & signal are inferred

1. **Feed folder** sets the baseline — e.g. the *Spine discovery* folder ⇒
   `spine / patient_demand`; a *Providers · Foot & ankle* feed ⇒ `foot / provider_named`;
   *Competitor intel* ⇒ `competitor / competitor_intel`.
2. **Headline keywords** then refine it (word-boundary matched, so "**disc**ussed" no
   longer trips the spine keyword "disc", and "**Partner**s" in the brand name no longer
   trips "partnership"): a mention can be upgraded to a higher-priority line, reclassified
   as partnership or patient-demand, and tagged for geo / negative sentiment.

## Routing (who works it)

The board prints a **Route** per mention so it's actionable, not just ranked:

| Signal / flag | Route |
|---|---|
| Negative brand sentiment | **PR — reputation (urgent)** |
| Patient demand, spine/ortho | **SEO/AEO + Content** (answer the intent); flag Paid |
| Patient demand, other line | Content / SEO |
| Partnership | **Physician Liaison / PR** (referral) |
| Brand / provider named | PR + Content (**testimonial only with consent**) |
| Press | PR — amplify / authority |
| Competitor intel | Marketing Director — intel |

## Tuning

All weights are constants at the top of `scoring.py` — edit and re-run; no other file
changes. `python3 scoring.py` prints a ranked self-test so you can see the effect of a
change immediately. If a line's priority shifts (e.g. an ortho push quarter), bump its
`LINE_POINTS`. Keyword lexicons (geo, partnership, negative, per-line) are just below the
weights.
