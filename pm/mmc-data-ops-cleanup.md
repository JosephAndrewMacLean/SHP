# MMC / referral data — cleanup list for Data Ops

**Date:** Aug 14, 2026 · **From:** Joe MacLean · **For:** Santosh / data-ops team
Every item below was hit while matching the Aug 14 new-patient report to CRM field-visit
activity. Ranked by leverage: the top items change what we can measure; the bottom items
reduce friction. No patient identifiers appear in this document.

## High leverage — changes what we can measure

**1. Capture referring-provider NPI at intake.** Referrer names arrive as free text
("SEIFELDIN MD, RAOUF", "Parachuri MD, Radha / Trivedi MD", "Dr. Michaels - not specified"),
so visit→referral matching is name-based and probabilistic (68/75 matched this week; 7
unmatchable). An NPI on the registration referral field makes the join deterministic and
makes conversion tracking automatic. Single highest-leverage fix on this list.

**2. Add a Tier field in MMC.** Tiers (T1/T2/T3/Prospect) exist only in our routing book —
MMC itself can't report visits by tier, and the team can't see tier on the pin. Add a custom
field (or controlled group tags), populated by the Friday import. Also the prerequisite for
Kristen's "one place to enter tier/visit data."

**3. Merge duplicate company records.** Same practice, multiple company records (seen:
Forum Medical Clinic, MDWell, Beaumont UC Wellstreet, AMC Primary Care — two records, one
real location; plus location-variant records like Plymouth Physical Therapy). Check-ins land
on one record while the book holds the other, so visit history splits and cadence/attribution
undercount. One record per physical location; merge histories, don't delete.

**4. One check-in per stop.** MMC logs a Visit activity **per person greeted** — the week of
Aug 3 is 482 activity rows for 103 actual stops (~4.7×). Any native MMC report overcounts
accordingly, and every downstream consumer has to know to dedupe. Either log one check-in per
stop (people recorded as linked contacts, not separate visit activities) or publish an
official deduped reporting view.

## Medium leverage — reliability & hygiene

**5. Person name fields carry credentials and punctuation.** Last-name fields like
"Summers MD,", "Trivedi MD,", first names with trailing commas. Broke referrer matching until
we normalized both sides. Move credentials to a suffix field; enforce clean First/Last.

**6. Groups taxonomy sprawl.** 75+ group values mixing four different concepts: specialty
("Internal Medicine/PCP" vs "PCP" vs "Erik PCP" vs "Bdex PCP"; "Podaitry" [typo] /
"Podiatrist" / "Podiatry Targets"; "Urgent care" / "Urgent Cares"; "Pain" / "Pain
Management"), ownership ("Coty", "Kristen Strategic Account"), lifecycle ("DO NOT CALL",
"CLOSED", "Passed Away", "T4- 6 MONTH FU"), and campaigns (senior housing, high schools).
Split into: one specialty field (controlled list), one status field, owner from the native
owner field, campaign tags only in Groups.

**7. Patient-identifying text in CRM notes.** Thank-you notes frequently name referred
patients, occasionally with insurance detail. MMC is a third-party CRM and notes travel in
every export. Going-forward convention is already agreed ("TY for recent referral", no
identifiers); data-ops piece = scrub the historical pattern (already flagged with Santosh).

**8. Corrupted custom Company-ID field.** At least one record (Michigan Neurology
Associates) carries junk text in the Company-ID custom field. Audit that field for
non-conforming values; it's the import/update key, so corruption breaks round-tripping.

## Lower leverage — friction reducers

**9. Activity Note field unused.** Visit intel is written on the company record (pattern
since 2025), so notes aren't timestamped per visit and the activity Note field is dead
weight. Log per-visit notes on the activity; keep the company record for durable facts.

**10. People→Company links incomplete.** Some person records have no linked company
(matched the physician, couldn't reach a visitable account). Backfill links for referring
providers; new-provider intake should require one.

**11. Address hygiene.** Three accounts added without street addresses; street-string
variants ("W" vs "West") defeat text-based building grouping (we group by rounded
coordinates as a workaround); coordinates stored as "(lng, lat)" — nonstandard order, worth
documenting wherever consumed.

**12. Blank owners on historical activities.** Pre-2025 visits often have no owner —
harmless for current reporting (they fall outside the program window) but worth knowing
before anyone trends multi-year.

## Suggested sequencing

NPI capture (#1) and the Tier field (#2) unlock the most measurement per unit of work.
Dupes (#3) and check-in convention (#4) fix the visit denominator. The rest can ride along
with normal CRM housekeeping. Items #3, #5, #6, #8 are one-time scrubs plus a validation
rule; #1, #2, #4, #9 are process changes that need a 15-minute walkthrough with the PL team.
