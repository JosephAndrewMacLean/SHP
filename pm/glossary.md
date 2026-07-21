# Glossary — Every Term and Acronym in the Spine Referral Workstream

**Date:** 2026-07-21 · Plain-language definitions for everything used in the reports, plan docs,
app, and decks. Where a term rests on an assumption or an export we could be reading wrong, it
says so — **corrections welcome; flag anything that doesn't match how the team actually works.**

## People & roles
| Term | Meaning |
|---|---|
| **PL** | Physician Liaison — the field reps who visit referring practices (Kristen, Jasmine, Coty, Sean). |
| **KJ / JJ / CO / SS / KG** | Initials used in the source report: Kristen Jones, Jasmine Jones, Coty, Sean Sweeney, Kessia (departed). |

## Patients & channels
| Term | Meaning |
|---|---|
| **NP** | New Patient — a first appointment at SHP. |
| **B2B** | New patients that came through a referring practice/professional (the PL channel). |
| **B2C** | New patients that came directly (web, ads, word of mouth). In our data B2C is *inferred* = total minus B2B — not source-confirmed yet (Analytics validation pending). |
| **PER Number** | The patient identifier in the practice's referral export. "Distinct PER numbers" = unique patients. |
| **Attributed patient** | A referral-export patient matched to a specific practice in our CRM. **Attributed ≠ confirmed kept visit** — the export has no kept/cancelled field. |
| **Match rate (82.5%)** | Share of referral rows we could tie to exactly one CRM company using deterministic rules (exact provider name, unique first+last, exact company, reviewed alias). Ambiguous rows were *excluded, not guessed*; ~17.5% still unmatched. |

## Accounts & the book
| Term | Meaning |
|---|---|
| **MMC** | Map My Customers — the field CRM the PLs log visits in. |
| **The book / universe** | The 848 target accounts (808 core + Sean's 40 routed priorities). |
| **Evidence band** | What an account has actually sent us in 2026: **Repeat Spine Referrer** (2+ spine patients) · **One Spine Patient** · **Ortho Referrer** (ortho but no spine) · **Other Patient Referrer** (pain/hand/foot only) · **Visit / Prospect** (no attributed patients). |
| **Tier 1 / 2 / 3 / Prospect** | Tier 1 = sent ≥1 spine patient (146 accounts) · Tier 2 = ortho referrers (156) · Tier 3 = other-service referrers (37) · Prospect = spine-adjacent, nothing attributed yet (469). |
| **Wave 1** | The first-priority 90 accounts (all proven spine senders) — never more than 2 weeks between visits. |
| **Target Score (0–100)** | Ranking number: up to 88 points from actual referral production, up to 12 from context (specialty fit, recent visits, reachability, data confidence). Prioritization only — not a revenue measure. |
| **Operating lane / Next Action** | The account's job in the plan: Protect · Reactivation · Convert · Cross-sell · Expansion/Test. |
| **DNC** | "Do Not Call" label in MMC — excluded from the book. |

## Field activity & the funnel
| Term | Meaning |
|---|---|
| **Visit-day (practice visit-day)** | One PL at one practice on one date, logged as a completed Visit in MMC. The core activity unit. |
| **People touches** | Individual provider/staff contacts logged within visits (one stop can touch several people). |
| **Wedding cake** | The funnel visual: provider touches → practice visit-days → new patients. |
| **NP per 100 visit-days** | Productivity ratio (2026 YTD: Kristen 67 · Jasmine 30 · Coty 18 · Sean 14). Directional — referrals lag visits. |
| **Lag (visit→first appointment)** | Days between the last completed visit to a practice and an attributed patient's first appointment. **Median 31 days; 83% within 60.** Timing context, not proof the visit caused the patient. |
| **Route day (D05, K-D03, FP/rev/swp)** | A pre-built geographic day of ≤10 stops. FP = first pass (all stops) · rev = producer revisit (proven stops only) · swp = sweep of tail producers. |
| **Protect Radar / Money List** | App screens: every proven referrer ranked by yield + days since visit; and the week's highest-value visits. |

## ⚠️ Configured Frequency — read this one carefully
**What it is:** Map My Customers lets you set a **visit frequency** (e.g., "every 30 days") —
attached to a **Group** (a label like "Urgent Cares") or account — and MMC then flags accounts
**Past Due / Up to Date / Upcoming** against it. The export columns `Configured Frequency` and
`Frequency Status` read this setting back.

**What the Jul 16 export shows:** almost nothing is set — statuses read "No frequency"/"Unknown"
on nearly every account; the per-PL rollup counts only **64 of 2,349 owned accounts** with any
frequency configured (Kristen 5 · Jasmine 15 · Coty 30 · Sean 14), most of those past due.
Kristen herself noted (Jul 17) that **old past-due entries can't easily be cleared and are being
ignored** — i.e., the feature exists but isn't trusted or used today.

**What we might have wrong (say so if it is):** this reading is only as good as the export. If
frequencies live somewhere the export doesn't capture (per-person settings, routes, a newer MMC
feature), the "64 of 2,349" understates reality — tell Joe and we re-pull before repeating it.

**Don't confuse it with Planned Cadence:** the **14 / 21 / 30 / 45-day cadences** in the plan and
app are **our target rhythm** (Tier 1 = 14d, Tier 2 = 21d, Tier 3 = 30d, Prospect = 45d) — they
are *not* in MMC yet. The MMC sync (`pm/mmc-import/`) proposes setting them **once per spine
group** in MMC so the Past-Due engine finally works for us instead of being ignored.

## Payers & compliance
| Term | Meaning |
|---|---|
| **WC / PI** | Workers' Compensation / Personal Injury. **Auto no-fault** = Michigan auto-injury coverage. All accepted, no referral needed, no copay — commercial-equivalent for spine. |
| **HMO referral-required** | BCN, HAP, McLaren, Priority Health HMO plans need a PCP referral before the visit. PPO/Medicare/self-pay/auto/WC don't. |
| **Medicaid (select providers)** | Accepted at *some* SHP providers only — verify per provider; never a blanket yes or no. Uninsured → **Harmony Health Direct Pay**. |
| **FQHC** | Federally Qualified Health Center — community clinics, typically Medicaid-heavy panels (our "Medicaid-likely — VERIFY" flag). |
| **Payer Class (heuristic)** | Our pattern-based guess at an account's payer mix (7 classes). **Assumption, not verification** — Kelly's intake pass confirms Tier 1 first. |
| **AKS / Stark** | Federal anti-kickback and physician self-referral laws. Practical rule: relationships are earned on service and clinical merit — **no payments, gifts, or inducements for referrals, ever.** |
| **PHI** | Protected Health Information. Never in notes, messages, or conversation — thank practices in aggregate counts only. |

## Plan & measurement
| Term | Meaning |
|---|---|
| **W1…W11** | Plan weeks, Mondays Jul 20 → Sep 28 (W1 = Jul 22–25 short week). |
| **Protect sweep / blitz** | W1–W2 recovery visits to every lapsed proven referrer (all 36 by Jul 31). |
| **95–115 vs 150** | Committed range vs stretch for monthly B2B spine by October; stretch requires capacity ≥200 team visit-days/wk, Sean active, 30+ one-spine conversions. |
| **Measurement contract** | Weeks 1–2 judged on activity (lapses→0, visit-days), patients read from mid-Aug, verdict in September. August will look soft — the June–July activity dip is already baked in via the 31-day lag. |
| **Scorecard** | The weekly spine tracker (11 weeks to Sep 28) — B2B spine NPs, active accounts, visit-days/PL, protect lapses, NP/100, match-rate. |
| **Validation sprint** | Joel's Jul 23–31 project: PLs disposition all 848 accounts (Keep/Remove/Reassign) in the review workbook; universe locked + routes regenerated Jul 31. |
