# Website Update Work Order — Clinic & ASC Schedule Redesign (7/13/2026 file)

**Source:** `ASC_and_Clinci_Redesign_7132026_002.xlsx` (Proposed · Proposed July 2026 · Current ·
Open Questions). Effective **July 1**; **Dr. Heil Sept 1**.
**Owner:** Joe · **Build:** Paul (modules) + Randall (page edits)
**Status: DRAFT — publish gated on Katie/Kelly confirmation (scheduling blast + Orthoplex update);
VERIFY rows blocked on the sheet's own open flags (§6).**

## 0. Publish rules (every page)

1. **Days + locations only — never hours** ("Mondays and Thursdays in Troy — call to confirm").
2. **Never publish OR/hospital days** (SYN/GEN/HOSPITAL are not bookable clinic time).
   Surgeon pages say "surgery days vary; clinic days below."
3. **Collapse Week 1/Week 2** → "select [day]s" or omit.
4. Every schedule claim carries a source + last-confirmed date in the CMS.
5. §6 VERIFY items do not publish until cleared.

---

## 1. PAGE-TYPE MAP — which page types carry schedule info, and what each adds

| Page type | Carries schedule? | What it shows | What's NEW because of this file |
|---|---|---|---|
| **LOCATION** | **YES — the primary home.** One reusable "specialists here, by day" module per clinic (single data source feeds all 8) | Provider × specialty × days table; walk-in/urgent note | **Troy spine module** (the headline, §2); Livonia **"EMG & injection days"** block; Port Huron **"visiting specialists" cadence module** (monthly/1st-3rd patterns); Southfield podiatry-density story; scrub removed days |
| **PROVIDER** | **YES — secondary.** "Clinic days & locations" module on every bio | Days-only line per location + "surgery days vary" | **Zamorano page CREATE** (Troy anchor — resolves half of V5); **Heil launch page** (build Aug, publish on confirmed schedule); Munk staleness fix; Yacisen geography fix; remove Mayo Thu-SH and McCarty Fri-Livonia wherever implied |
| **HUB** (spine; ortho later) | **Access messaging only — no rosters** | "Spine clinics **Monday–Friday** across metro Detroit" (new, true post-redesign); team-module cards get **location chips** (Zamorano→Troy, Varghese→SH, Maslak→Liv/SH…) | The Friday-coverage claim (ops' open question, now answered); Troy added to the hub's locations band |
| **TREATMENT** | **Selective.** Only procedure-logistics pages | "Where this is done" module: office vs. ASC; EMG/injection **days by location** (days only) | `/treatment/emg` gets real "EMG days: Livonia Fri AM, Sterling Heights Mon AM…" content; injection pages get "procedure days at Livonia/SH"; ketamine mention only with clinical sign-off |
| **CONDITION** | **NO.** Evergreen — schedules would rot here | "Who treats this" mini-team links to provider/location pages (which carry the days) | Nothing schedule-specific; add "spine care in Troy/SH/Livonia" links in the who-treats module |
| **LEARNING HUB / GUIDE** | **NO.** | Guides' what-to-expect may say "first visits often available within the week" (Katie/Kelly-approved wording only) | No direct updates |
| **GBP listings** (surface, not page) | **YES — mirror.** Each clinic's GBP mirrors its location module | Provider listings, services, hours consistency | Troy GBP gets the spine services + providers; this channel already converts (~375+ sessions) |

**Net-new content this file creates (beyond edits):**
1. Troy spine module + Troy paid-LP variant (supply for the missing Troy campaign — hand to Cardinal).
2. Zamorano provider page (CREATE — she has none/conflicting; Troy anchor is her content spine).
3. Heil launch package (bio + Troy/pain modules + sports-pain angle) — prep in August, hold for §6.
4. "EMG & nerve testing" and "injection day" logistics content (Livonia/SH) on the relevant treatment + location pages.
5. **Home-visit podiatry callout** (Dr. F. Leff) — a real differentiator nobody markets; Southfield page + his bio.
6. Port Huron "visiting specialists" module pattern (cadence-based: "Dr. Munk monthly · Dr. Kassa 1st & 3rd Thursdays").
7. The **schedule data source** itself: Paul builds location/provider modules reading one dataset so the next redesign is a data edit, not 30 page edits.

**Coverage note (corrected 7/21, per Joe):** the file schedules SH, Livonia, Southfield,
Port Huron, Troy (+ ASC/hospitals). **There is NO Rochester location — the Troy clinic is on
Rochester Road.** Any site/GBP/directory content implying a separate "Rochester" clinic is
wrong and must be corrected to Troy. The naming is an SEO asset, not a gap: "Rochester Rd,"
"Rochester Hills," and "Rochester MI" searches are served by Troy — add them as Troy-page
altLabels and hyperlocal candidates routing to Troy. If any other advertised location lacks
physician rows here, confirm whether it's PT/MRI-only before its page claims a clinic roster.

---

## 2. The headline: Troy is now real (update FIRST — location page + GBP + hub chip)

| Provider | Specialty | Troy days (publishable form) |
|---|---|---|
| **Dr. Zamorano** | Spine/neurosurgery | **Mondays + Thursdays** (Thu pending §6) |
| **Dr. Salar** | Spine | Select Wednesday mornings |
| **Dr. Munk** | Spine (SI) | **Wednesday afternoons — every week** |
| **Dr. Mayo** | Ortho/sports | Tuesday afternoons |
| **Dr. Sorensen** | Podiatry | Wednesdays |
| **Dr. Heil** (Sept 1) | Pain | Wednesdays (pending §6) |

**Spine in Troy Mon–Thu.** Troy location page, Troy GBP, hub locations band, and the Cardinal
campaign brief all update from this one table.

## 3. PROVIDER-page rows (publishable)

SH = Sterling Heights · Liv = Livonia · SF = Southfield · PH = Port Huron.

**Spine:** Zamorano — Troy Mon (+Thu pending) · Salar — Liv, SH; Troy select Wed AM · Munk —
SH Wed AM + Fri, **Troy Wed PM**, PH monthly · Varghese — Liv Tue; SH Wed + **Fri (new)** ·
Maslak — SH Mon; Liv Wed + **Fri AM (new)** (+ Thu alt.) · McCarty — Liv Mon/Tue; SH Wed
(added)/Thu; SF select Wed; **no Friday clinic (now surgery day — scrub any implication)**.

**Ortho:** D. Mendelson — SH Mon/Wed; Liv Thu · J. Mendelson — SH Tue/Thu; Liv select Wed ·
S. Mendelson — SH Mon (+Thu alt.); Liv Tue/Thu alt.; Fri admin · A. Mendelson — Liv Mon/Thu ·
Bhullar — Liv Tue/Fri (+Mon alt.); SF Wed; SH select Thu · Mayo — Liv Mon; **Troy Tue PM**;
SH/Liv Fri alt.; **Thu SH clinic removed** · Yacisen — SH Wed (alt.) + Fri; PH Wed (alt.) +
Thu (**fixes the Saginaw/Midland bio error**) · Yakasin — PH Mon/Wed.

**Hand/Pod:** Bohm — Liv Mon PM + Fri AM (+Wed AM alt.); SH Tue (§6 flag) · Klein — SH Mon;
"Livonia most days — call" until §6 clears · R. Leff — SF Mon–Wed + Fri · F. Leff — SF Tue;
**home visits** (+ SH select Fri) · Green — SF Wed/Fri (+ select days §6) · Sorensen — SF
Mon/Thu; **Troy Wed**.

**Pain:** Kassa — SH Mon/Tue (+Thu alt.); PH 1st & 3rd Thu; Liv Fri AM EMG · Lee — SF Mon;
Liv Wed/Fri · Oddo — SH Mon/Thu; Liv Tue (+Wed alt.) · Singh — Liv Mon/Wed (+Tue alt.); SH
select Tue · Heil — **hold (§6)** · Abood (PCP) — Liv Mon (+Thu most); SH Tue/Wed; SF select
Thu; PH occasional.

**The Friday answer:** Maslak Fri AM (Liv) + Varghese Fri (SH) + Munk Fri (SH) → spine runs
**Monday–Friday** networkwide. Hub + location access messaging may say so after Katie/Kelly
sign-off (ops' own open question: "Want a spine physician on a Friday").

## 4. LOCATION-page modules (days-only rosters)

- **Troy:** §2 table — flagship.
- **Sterling Heights:** spine daily (Varghese Wed/Fri · Maslak Mon · Munk Wed AM/Fri ·
  McCarty Wed/Thu · Salar Tue) + ortho/hand/pain rows.
- **Livonia:** spine Salar Mon · McCarty Mon/Tue · Maslak Wed/Fri AM · Varghese Tue; pain-heavy
  (Oddo/Singh/Lee); **"EMG & injection appointments" block** (EMG: Kassa Fri AM, Belen select
  days; procedure days Singh/Heil).
- **Southfield:** McCarty select Wed (spine) · Bhullar Wed (ortho) · Lee Mon (pain) ·
  podiatry-dense (R. Leff, Green, Sorensen, F. Leff) + home-visits callout.
- **Port Huron:** Yakasin Mon/Wed · Yacisen Wed alt./Thu · Kassa 1st & 3rd Thu · Munk monthly ·
  Abood occasional — **visiting-specialists module; replace stale Munk-centric copy.**
- No separate Rochester page/listing exists or should exist — Troy (on Rochester Road) serves
  that geography; add Rochester/Rochester Hills language to the Troy page + GBP (see §1 note).

## 5. Execution sequence

1. Katie line-item confirm of §2–§4 (15 min) — go-signal = her blast + Orthoplex update.
2. Paul: the single-source schedule modules (location + provider variants).
3. Randall: Troy → Munk/PH staleness → Yacisen fix → the rest; GBP mirrors last.
4. Mitch email item 4 = confirm-extraction (already updated); register A8 answered-pending-
   confirm; V5 partially resolved (Yacisen, Munk, Zamorano-Troy).
5. Re-check §6 items within a week of the blast.

## 6. VERIFY-FIRST (the sheet's own open flags — no publish)

| Item | Flag | Resolver |
|---|---|---|
| **Heil's week** | 3 conflicting versions + "Heyl vs. Heil" spelling | Katie/Kelly + credentialing (Sept 1 anyway) |
| Zamorano Thu | "Needs to be moved" + Wk2 Thu SYN row | Katie — publish Mon now |
| Zamorano Mondays | "1st Monday of month = hospital block, clinic Tuesday" | "Most Mondays" wording |
| Bohm Wed/Thu | "Lets talk to Kyle" / "Should one of these be Genesys" | Katie/Kyle |
| Klein Livonia adds | "add Liv half day back on" / "discuss with Klein" | Katie/Klein |
| R. Leff Thursday | "Lets discuss with Randy" | Katie |
| Green select days | "need to move to Tuesday or Thursday" | Katie |
| McCarty Wk1 Wed/Thu | "flipping SAM wed/thur would resolve top 2 issues" — may flip | Katie/Mitch — hold Wed, publish Liv Mon/Tue + SH Thu |

## 7. Marketing follow-ons unlocked

Troy campaign supply → Cardinal · "Spine Monday–Friday" access message (post sign-off) ·
Zamorano page build (V5) · Heil Sept-1 launch package (sports-division angle) · home-visit
podiatry story · EMG/injection logistics content feeding the interventional front door.
