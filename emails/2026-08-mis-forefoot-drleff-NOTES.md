# MIS Forefoot Surgery Email — Dr. Leff (July/August 2026) — Build & Send Notes

**File:** `emails/2026-08-mis-forefoot-drleff.html`
**Status: DRAFT — pending Dr. Leff's clinical review and marketing sign-off. Not cleared to send.**

## What this is

Last year's print newsletter (`MIS_surgery_newsletter.docx`, July/August 2025, Michfoot
Surgeons branding) rebuilt as a bulletproof HTML email in the established Dr. Leff
summer-note template (Synergy branding, 620px hybrid layout). Copy is Dr. Leff's original
newsletter text, lightly edited for first-person email voice and claim hygiene (see
Compliance). ESP merge tags are Mailchimp (`*|UNSUB|*`, `*|UPDATE_PROFILE|*`, `*|EMAIL|*`,
`*|ABOUT_LIST|*`, `*|LIST:ADDRESSLINE|*`).

## The advertisement (cross-promo block), per Joe's request

"More Care, Same Roof — Southfield" card now carries spine, ortho, **and Dr. Abood**:

| Provider | Label shown | Rating shown | Booking URL (Zocdoc white-label) |
|---|---|---|---|
| Dr. Scott McCarty, MD | Spine Surgeon · Back & Neck | 4.81★ (53 reviews) | `zocdoc.com/wl/mendelsonortho/doctor/scott-mccarty-md-614176?...` |
| Dr. Preetinder Bhullar, MD | Orthopedic Surgeon · Hip & Knee | 4.99★ (137 reviews) | `zocdoc.com/wl/mendelsonortho/doctor/preetinder-bhullar-md-431825?...` |
| Dr. Tony Abood, DO | Family Physician · Primary Care | 4.91★ (67 reviews) | `zocdoc.com/wl/mendelsonortho/doctor/tony-abood-do-575326?...` |

- Abood is labeled **Family Physician / Primary Care** (his actual credential — he is not
  spine/ortho; do not relabel him as such).
- Ratings are Zocdoc averages as pulled August 2026; a disclosure line under the block says
  so (FTC). Refresh numbers if the send slips a month+.
- The summer template's podiatry alternates (Dr. Sorensen, Dr. Green) were **replaced** by
  this block. If you want them too, copy a row and reuse their booking URLs from the
  summer email.

## Compliance / claims — what changed from the source doc and why

1. **"REAL PATIENT RESULTS" before/after photo omitted.** The docx image is a patient
   photo with "Minimal incision / NO hardware / No Scars" overlaid. Not included because
   (a) marketing use of patient photos needs signed media consent verified on file, and
   (b) email images must be hosted. A commented `OPTIONAL BEFORE/AFTER PHOTO SLOT` marks
   the insertion point in the HTML if consent + a hosted URL are confirmed.
2. **Absolute outcome claims hedged** (FTC/substantiation): "NO hardware / No Scars"
   dropped; replaced with the "At a Glance" strip using the doc's own hedged register
   ("poke-hole incisions · typically less pain and swelling · often walking the same
   day"). "Permanent solution" → "lasting solution."
3. Everything else is the doctor's own copy — Dr. Leff should still confirm clinical
   accuracy (conditions list, weight-bearing/recovery statements, candidacy language).
4. Trust bar reuses the summer email's verified figures (4.9 / 408 Google reviews).

## Open decisions before send

- **Phone number:** email uses **(855) 750-5757** everywhere (matches the summer template
  and Liine-tracked main line). The docx/print piece used the Michfoot Southfield direct
  line **248-355-4000**, and `michfoot@me.com` was dropped (legacy brand). Confirm which
  number patient-access wants on this campaign.
- **Dr. Leff's CTA links** go to his Zocdoc marketplace profile
  (`zocdoc.com/doctor/randy-leff-dpm-579782`), carried over from the summer template. The
  three cross-promo doctors use free white-label booking links (`/wl/mendelsonortho/...`).
  Per the Zocdoc+NextGen analysis, booking-link/website paths capture ~74% at $0 vs ~57%
  via paid marketplace — if a white-label link exists for Dr. Leff, swap it into the hero
  and primary CTAs.
- **Subject line & preview text:** recommendations below (own section).

## Subject line & preview text

**Recommended send (or A in an A/B):**

- **Subject:** `Not your grandmother's bunion surgery` (37 chars)
- **Preview:** `Smaller incisions, less downtime — and why summer is the smart window to plan a consultation. A note from Dr. Randy Leff.` (121 chars, payload in first 40)
- **From name:** `Dr. Randy Leff | Synergy Health Partners` — front-load the doctor; the
  personal-letter format earns the personal sender. Same sending domain/auth as usual, so
  no deliverability change. Reply-to: a monitored inbox.

The subject is the email's own pull quote — distinctive, on-voice, zero outcome claims,
and short enough to display in full on virtually every mobile client.

**B test / alternates (subject → paired preview):**

| # | Subject (chars) | Paired preview | Angle / note |
|---|---|---|---|
| B | Pain-free feet by fall? Now's the time to plan (46) | Dr. Leff on minimally invasive bunion & hammertoe surgery — tiny incisions, less downtime, no pressure. | Timing/outcome. Mirrors the print piece's own H1; keep the "?" so it stays aspirational, not a promise. |
| C | Back in regular shoes before the holidays? (42) | Most MIS patients are — Dr. Leff on why July and August are the smart window for forefoot surgery. | Subject asks, preview answers with the body's hedged "most patients" language. Keep the "?". |
| D | "I just can't take the time off" — sound familiar? (50) | Modern forefoot surgery has changed the math on downtime. Dr. Leff explains what's different now. | Objection/empathy; strongest fit for the letter format. |
| E | A summer note from Dr. Leff: bunion surgery has changed (55) | What minimally invasive forefoot surgery treats, what recovery looks like, and how to find out if you're a candidate. | Safest/plainest; use if compliance wants maximum caution. |

Personalization variant (only if FNAME coverage in the audience is clean, with a default
value set): `*|FNAME|*, dreading another season of foot pain?` — reuses the checklist's
own line.

**Mechanics:**

- Sentence case, no emoji (YMYL trust + older segment), no "free"/all-caps/"!!" — all
  options above are CAN-SPAM-truthful to the content.
- Char budgets: subject ≤ ~46 shows in full on iPhone portrait and the Gmail app; preview
  front-loaded in the first ~40 chars, useful to ~90.
- Mailchimp: put the preview string in the **Preview Text** field; the same string is also
  baked into the HTML preheader as a fallback, so keep them aligned if edited.
- A/B: 25/25/50, pick the winner on **clicks, not opens** (Apple Mail Privacy Protection
  inflates opens), wait ≥4 hours before the winner sends.
- Optional: resend to non-openers after 3–4 days under subject D (exclude clickers).
  MPP-inflated "openers" are excluded automatically — that errs conservative, which is
  fine for a patient list.
- B and C echo aspirational phrases from the doctor-approved 2025 print piece; final
  wording still rides along with the clinical review of the email itself.

## Client-compatibility engineering (what makes it "bulletproof")

- 620px hybrid layout: fluid `max-width` + ghost-table lock for Outlook/IE; single-column
  stack under 620px; all layout in nested tables, `role="presentation"`.
- Outlook desktop (Word engine): VML roundrect buttons for the three filled CTAs;
  outline buttons are border+padding on the `<td>` (renders without VML); MSO font
  fallback stylesheet; `mso-line-height-rule:exactly`; `mso-hide` on preheader.
- CSS-stripped fallback: `bgcolor` attributes on every colored section, so white-on-teal
  text can never sit on a white background.
- Dark mode: `prefers-color-scheme` + `[data-ogsc]` (Outlook Android) overrides. Dark
  cards get light text; tinted content cards intentionally stay light with dark text so
  nothing can render unreadable (fixes a latent issue in the summer template where
  `.dm-text` targeted paragraphs on backgrounds that stayed white). Gmail's forced
  auto-invert is left to do its own thing (standard practice).
- Apple Mail: `x-apple-disable-message-reformatting`, data-detector color suppression,
  `format-detection` meta (explicit `tel:` links still work).
- Gmail/webmail quirks: `u + #body` link reset, `#MessageViewBody` reset, `.ExternalClass`
  (legacy Outlook.com), 100%-width wrappers, `-webkit-text-size-adjust`.
- HTML entities throughout (numeric for ★ →), UTF-8 declared; all `&` in URLs escaped.
- Accessibility: alt text on images, semantic h1–h3, ~AA contrast in both modes,
  decorative tables `aria-hidden`.
- Verified in this repo via Chromium renders at 375px/700px, light + dark: no horizontal
  overflow, correct stacking. **Still run a real matrix test (Litmus/Email on Acid or
  Mailchimp Inbox Preview) before send** — priority: Outlook 2016+ Win, Gmail app
  (Android/iOS), Apple Mail + dark mode, Outlook.com, Yahoo, Samsung Mail.

## Tracking

All links carry `utm_source=newsletter&utm_medium=email&utm_campaign=mis_forefoot_drleff_2026`
with per-placement `utm_content` (`hero_cta`, `primary_cta_book`, `ad_mccarty_spine`,
`ad_bhullar_ortho`, `ad_abood_primarycare`, `trust_bar_*`, `header_logo`,
`signature_reviews`, `footer_southfield`). Zocdoc `lnsg` tokens on the three white-label
URLs were preserved exactly as provided.
