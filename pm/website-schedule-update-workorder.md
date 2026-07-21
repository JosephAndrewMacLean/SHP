# Website Update Work Order — Clinic & ASC Schedule Redesign (7/13/2026 file)

**Source:** `ASC_and_Clinci_Redesign_7132026_002.xlsx` (sheets: Proposed · Proposed July 2026 ·
Current · Open Questions). Effective **July 1** for most changes; **Dr. Heil starts Sept 1**.
**Owner:** Joe · **Build:** Paul (templates/modules) + Randall (page edits)
**Status: DRAFT — publish-ready rows gated on Katie/Kelly confirmation (the scheduling blast +
Orthoplex update per the 7/21 meeting); VERIFY rows blocked on the sheet's own open flags.**

## 0. Publish rules (apply to every page)

1. **Publish DAYS + LOCATIONS, never hours.** Hour-level detail goes stale fastest and creates
   over-promise risk; "Mondays and Thursdays in Troy — call to confirm today's schedule" is
   durable and honest.
2. **Never publish OR/hospital days** (SYN = Synergy Surgery Center, GEN = Genesys, HOSPITAL)
   as availability — they are not patient-bookable clinic time. Surgeon pages say "surgery
   days vary; clinic days below."
3. **Collapse Week 1/Week 2 complexity.** Patients don't parse alternating weeks. If a day
   alternates, say "select [day]s — call to confirm" or omit it.
4. **Every schedule claim is sourced to this file + confirmation date** and carries a
   "last updated" note in the CMS (not necessarily on-page).
5. Anything in §4 VERIFY-FIRST does not publish until its flag clears.

## 1. The headline: Troy just became real (update the Troy page FIRST)

Weekly Troy clinic coverage in the redesign:

| Provider | Specialty | Troy days (publishable form) |
|---|---|---|
| **Dr. Zamorano** | Spine/neurosurgery | **Mondays + Thursdays** (9–5) — the Troy spine anchor |
| **Dr. Salar** | Spine | Wednesday mornings (alt. weeks → "select Wednesdays") |
| **Dr. Munk** | Spine (SI/iFuse) | **Wednesday afternoons (every week)** |
| **Dr. Mayo** | Ortho/sports | Tuesday afternoons (every week) |
| **Dr. Sorensen** | Podiatry | Wednesdays (midday/PM) |
| **Dr. Heil** (Sept 1) | Pain/sports-pain | Wednesdays (pending §4 verify) |

**Spine is now in Troy four days a week (Mon, Wed AM+PM, Thu).** This unblocks the whole
Troy program: the Troy location page gets a real spine module ("Spine specialists in Troy —
Monday through Thursday"), the semantic model's Troy location build (model §3.2) gets its
content, and the paid-analysis finding "no Troy campaign exists" now has supply to advertise.
**Do this page first.**

## 2. Provider-page updates (publishable rows)

Legend: SH = Sterling Heights · Liv = Livonia · SF = Southfield · PH = Port Huron.
"Publish as" = the days/locations line for the bio + location pages.

### Spine
| Provider | Publish as | What changed vs. current site risk |
|---|---|---|
| Dr. Zamorano | Troy — Mon + Thu | Crawl found her SHP page conflicting/absent (V5). **This is her content anchor: build/fix the page around Troy** |
| Dr. Salar | Livonia, Sterling Heights; Troy select Wed AMs | Adds Troy to his page (his bio = #1 page; add, don't disturb) |
| Dr. Munk | Sterling Heights Wed AM + Troy Wed PM; Fri SH (10–1); PH monthly (wks 2&4 Tue) | **Fixes the stale "Port Huron starting Aug 12" copy** — he's SH/Troy-primary now, PH monthly. Update his misfiled hub-child page too |
| Dr. Varghese | Livonia Tue; Sterling Heights Wed + **Fri** | **Adds Friday clinic (SH)** — new. (Sheet note: "Lost HOSPITAL (SMMH/S-choice)" — omit hospital refs) |
| Dr. Maslak | Sterling Heights Mon; Livonia Wed + **Fri AM** (+ Thu alt. wks) | **Adds Friday Livonia clinic** — new |
| Dr. McCarty | Livonia Mon + Tue (alt.); Sterling Heights Wed (added) + Thu; SF select Weds | Adds Livonia Mon + SH Wed clinics; **Fridays become surgery days — remove any Friday-clinic implication** |

**The Friday answer:** ops' open question was "want a spine physician on a Friday" — the
redesign answers it: **Maslak Fri AM (Livonia) + Varghese Fri (SH) + Munk Fri (SH)**. The
spine hub and location pages may now say spine clinics run **Monday through Friday** across
the network. (Access-promise sign-off: Katie/Kelly.)

### Ortho / Sports
| Provider | Publish as | Notes |
|---|---|---|
| Dr. David Mendelson | SH Mon + Wed; Livonia Thu | — |
| Dr. Jeffrey Mendelson | SH Tue + Thu; Livonia select Weds | — |
| Dr. Stephen Mendelson | SH Mon (+ Thu alt.); Livonia Tue/Thu (alt.) | Fri = admin, not clinic |
| Dr. Alice Mendelson | Livonia Mon + Thu | — |
| Dr. Bhullar | Livonia Tue/Fri (+ Mon alt.); SF Wed; SH select Thu | SF Wednesdays = real Southfield ortho presence |
| Dr. Mayo | Livonia Mon; Troy Tue PM; SH or Livonia Fri (alt.) | **Thu SH clinic removed (now surgery day)** — pull it wherever listed |
| Dr. Yacisen | SH Wed (alt.) + Fri; PH Wed (alt.) + Thu | **Fixes the bio's Saginaw/Midland error (V5): he's SH + Port Huron (+ Harbor Beach outreach)** |
| Dr. Yakasin ("Jerry") | PH Mon + Wed | Port Huron ortho anchor |

### Hand / Podiatry / Pain
| Provider | Publish as | Notes |
|---|---|---|
| Dr. Bohm | Livonia Mon PM + Fri AM (+ Wed AM alt.); SH Tue | Pending "talk to Kyle" flag → §4 |
| Dr. Klein | SH Mon (+ Thu PM alt.); Livonia Tue/Wed/Thu/Fri variants | Multiple "add Liv" cells + "discuss with Klein" → publish SH Mon + "Livonia most days — call" until confirmed |
| Dr. R. Leff | SF Mon–Wed + Fri; Thu AM surgery | Slightly less SF clinic than before — keep "SF five days" claim OFF |
| Dr. F. Leff | SF Tue (+ SH select Fri); home visits otherwise | "Home visits" is a differentiator — say it |
| Dr. Green | SF Wed + Fri; Livonia/SH select days | "Move to Tue/Thu" note → §4 for the select days |
| Dr. Sorensen | SF Mon + Thu; Troy Wed | — |
| Dr. Kassa | SH Mon + Tue (+ Thu alt.); PH select Thu (1st/3rd); Livonia Fri AM (EMG) | — |
| Dr. Lee | SF Mon; Livonia Wed + Fri | — |
| Dr. Oddo | SH Mon + Thu; Livonia Tue (+ Wed alt.) | — |
| Dr. Singh | Livonia Mon/Wed (+ Tue alt.); SH select Tue | Ketamine clinic mention only w/ clinical sign-off |
| Dr. Heil | — hold — | §4: three conflicting schedule versions; starts Sept 1 |
| Dr. Abood (PCP) | Livonia Mon (+ Thu most wks); SH Tue + Wed; SF select Thu; PH occasional | — |

## 3. Location-page updates (roster modules)

Per location, the "specialists here, by day" module (days only):

- **Troy:** §1 table — the new flagship module.
- **Sterling Heights:** deep bench daily; spine = Varghese (Wed/Fri), Maslak (Mon), Munk
  (Wed AM/Fri), McCarty (Wed/Thu), Salar (Tue); plus ortho/hand/pain rows above.
- **Livonia:** spine = Salar (Mon), McCarty (Mon/Tue), Maslak (Wed/Fri AM), Varghese (Tue);
  pain heavy (Oddo/Singh/Lee); note Livonia hosts the EMG + procedure days (patient-facing:
  "EMG and injection appointments in Livonia").
- **Southfield:** McCarty select Weds (spine); Bhullar Wed (ortho); Lee Mon (pain);
  podiatry-dense (R. Leff, Green, Sorensen, F. Leff). Fixes the near-empty Southfield story.
- **Port Huron:** Yakasin Mon + Wed; Yacisen Wed (alt.) + Thu; Kassa select Thu; Munk monthly;
  Abood occasional. **Replace the stale Munk-centric Port Huron copy.**
- **Hyperlocal implication:** Troy's bench strengthens the D3 case for Clawson/Rochester-area
  city pages once Joel's counts land.

## 4. VERIFY-FIRST (the sheet's own open flags — do not publish)

| Item | Flag in the file | Resolver |
|---|---|---|
| **Dr. Heil's week** | Three conflicting versions (spine sheet: Mon Troy… · pain section: Mon SH/Wed Troy · current: "ASC?/T/L?") + **name spelling "Heyl" vs meeting's "Heil"** | Katie/Kelly + credentialing before ANY publish (Sept 1 anyway) |
| Zamorano Thu | "Needs to be moved" note + Wk2 Thu SYN row | Katie — publish Mon now, Thu after confirmation |
| Zamorano 1st Monday | "1st Monday of the month block time @ hospital, Clinic on Tuesday" | Say "most Mondays" or note the exception |
| Bohm Wed/Thu | "Lets talk to Kyle" + "Should one of these be Genesys" | Katie/Kyle |
| Klein Livonia adds | "add Liv half day back on" / "Lets discuss with Klien" | Katie/Klein |
| R. Leff Thursday | "Lets discuss with Randy" | Katie |
| Green select days | "need to move to Tuesday or Thursday" | Katie |
| McCarty Wk1 layout | "flipping SAM wed/thur week 1 would resolve top 2 issues" — may still flip | Katie/Mitch — publish the stable days (Liv Mon/Tue, SH Thu), hold Wed until settled |
| Salar Wk2 Monday | "HOSPITAL/ SYN" ambiguity | Immaterial if hours aren't published (Mon = Livonia wk1 only → "select Mondays") |

## 5. Execution sequence

1. **Confirm gate:** Katie's org-wide scheduling blast + Adam's Orthoplex update = the
   go-signal per the 7/21 meeting. Send Katie this work order's §2/§3 tables for a
   line-item yes/no (15 minutes).
2. Paul builds the reusable **"providers at this location, by day" module** (one template,
   eight pages) + the bio-page "clinic days" module — both consume a single
   schedule-data source so the next redesign is a data edit, not a page edit.
3. Randall executes page edits in publish-rule form (days only) — Troy first, then Munk/PH
   staleness fixes, then the rest of §2/§3.
4. **Register/email updates:** Mitch email item 4 (clinic rosters) is now "confirm my
   extraction" not "tell me" — attach §2/§3. Register items A8 → answered-pending-confirm;
   V5 partially resolved (Yacisen geography, Munk locations, Zamorano Troy anchor).
5. Re-check within a week of the Katie blast for the §4 items that settle.

## 6. Marketing follow-ons this unlocks (not part of the page edits)

- Troy campaign supply now exists (paid finding: "no Troy campaign") — hand §1 to Cardinal.
- "Spine clinics Monday–Friday" access message (post Katie/Kelly sign-off).
- Zamorano's rebuilt page (V5) writes itself around the Troy anchor + neurosurgical spine.
- Heil launch package (Sept 1): bio + Troy/pain modules + the sports-division angle from the
  7/21 meeting — prep in August, publish on a confirmed schedule only.
