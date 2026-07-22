# Per-URL Internal-Link Checklists — generated from the D2 contract (model §D2)

**Generated 7/22 (agent-executed — no human input needed to produce; humans only paste).**
Rules baked in: anchors = patient words (altLabels) in sentence context · links point at
canons only · treatment links in ladder order (PT → injection → surgery pages; copy opens
with activity mods/meds) · every arrow two-way · a missing link is a launch blocker.
Check off in the workbench T10. Where a target page doesn't exist yet (guide, OptiLIF),
the link ships WITH that page — listed here so nothing is forgotten.

---

## Hub — `/specialty/spine-neck-back` (T1)
**OUT:** condition grid → all 6 canons (sciatica · spinal-stenosis · herniated-disc · DDD ·
spondylolisthesis · radiculopathy/pinched-nerve) · pathway band → PT canon, `/treatment/caudal-esi/`,
endoscopic page (when live) · differentiation band → endoscopic · OptiLIF · ACDR · MILD pages ·
team module → 5 surgeon bios + pain-management page · locations band → 5 clinic pages ·
guide rail → "Do I need spine surgery?" (when live) · symptom router → conditions + `/orthopedic-urgent-care/`
**IN:** breadcrumb on every spine page · homepage dual-entry strip · location pages' services line

## Sciatica — `/conditions/sciatica` (T4)
**OUT (13):** hub (breadcrumb) · herniated-disc (cause — anchor e.g. *"often caused by a
herniated disc"*) · PT canon → caudal-ESI (*"an epidural steroid injection often calms the
nerve"*) → endoscopic page (treatment order) · 1 pain bio + Maslak bio (who treats) ·
sciatica guide (rail, when live) · 5 location chips
**IN (11+):** hub grid + symptom router · herniated-disc related block · caudal-ESI
indications · endoscopic indications (when live) · sciatica guide (when live) · future
cluster articles

## Spinal stenosis — `/conditions/spinal-stenosis/` (T4)
**OUT:** hub · DDD (related cause) · PT canon → lumbar-ESI/caudal → laminectomy + **MILD
page** (it already ranks — capture its momentum) · McCarty bio + 1 pain bio · guide rail ·
5 location chips
**IN:** hub grid + router · MILD page (indications — *"for lumbar spinal stenosis"*) ·
laminectomy page · DDD related block · its guide

## Herniated disc — `/conditions/herniated-disc/` (T4)
**OUT:** hub · sciatica (symptom it causes) · pinched-nerve entry (when live) · PT canon →
caudal-ESI → microdiscectomy + endoscopic (when live) · Maslak bio + 1 pain bio · guide
rail · 5 location chips · show "bulging disc / disc herniation" as visible synonyms
**IN:** hub grid + router · sciatica cause link · microdiscectomy + endoscopic indications ·
its guide · L5-S1 cluster article (when live)

## Degenerative disc disease — `/conditions/degenerative-disc-disease/` (T4)
**OUT:** hub · herniated-disc (related) · PT canon → injection canon → ACDR/fusion pages
(honest indications) · Varghese bio + 1 pain bio · guide rail · 5 location chips · imaging
module (A10)
**IN:** hub grid + router · herniated-disc related · fusion/ACDR indications · its guide

## Spondylolisthesis — `/conditions/spondylolisthesis/` (T4)
**OUT:** hub · stenosis (related) · PT canon → injection → fusion/OptiLIF (when live, honest
indication) · McCarty bio + 1 pain bio · guide rail · 5 location chips
**IN:** hub grid + router · stenosis related · fusion + OptiLIF indications (when live)

## Pinched nerve — NEW `/conditions/pinched-nerve/` (T4, ships ≥3 inbound FIRST)
**OUT:** hub · cervical-radiculopathy page + lumbar mapping (links both, duplicates neither)
· PT canon → injection → ACDR/decompression · Salar bio + 1 pain bio · guide rail
**IN (pre-ship requirement):** hub grid + symptom router · herniated-disc related block ·
cervical-radiculopathy related block — all three live BEFORE the page publishes

## Caudal ESI — `/treatment/caudal-esi/` (T3)
**OUT:** hub (breadcrumb) · conditions it treats: sciatica + stenosis + herniated-disc
(indications) · conservative-alternatives: PT canon (+ activity-mods/meds copy, no link
needed) · who-performs: pain-management page/bios · guide rail ("injection vs surgery"
guide when live)
**IN:** sciatica + stenosis + herniated-disc + DDD treatment-in-order sections · hub pathway
band · MRI-facts article (T2 adds it) · Livonia page injection block

## MRI-facts article — `/mri-facts-that-you-may-have-not-known/` (T2)
**OUT:** EMG page · hub (*"our spine specialists"* in sentence context) · caudal-ESI
(*"image-guided injections"*)
**IN:** Livonia page imaging line · DDD page imaging module · learning-hub shelf

## OptiLIF — NEW `/treatment/optilif/` (T7, ships ≥3 inbound FIRST)
**OUT:** hub (breadcrumb via treatment spectrum) · conditions treated: DDD + spondylolisthesis
(honest indications) · conservative-alternatives: PT + injection first · McCarty bio ·
comparison rail: fusion page · guide rail
**IN (pre-ship):** hub differentiation band · DDD + spondylolisthesis treatment sections ·
McCarty bio "procedures I perform" — all live BEFORE publish

## SI fusion canon (T8)
**OUT:** hub · si-joint-pain condition (indication) · conservative-alternatives: PT + SI
injection page · Varghese bio (performing surgeon) · guide rail
**IN (pre-ship):** hub differentiation band · si-joint-pain treatment section · SI-injection
page ("when injections stop lasting") · Varghese bio procedures module

## Guide #1 — NEW `/guides/do-i-need-spine-surgery/` (T9, ships ≥3 inbound FIRST)
**OUT:** conditions it serves: sciatica + stenosis + herniated-disc · treatments it weighs:
caudal-ESI + endoscopic/fusion · team module (I3 bridge) · booking
**IN (pre-ship):** hub guide rail · all six condition guide rails · caudal-ESI guide rail —
the rails go live on the canons FIRST, then the guide publishes into them

## Provider bios (T5) — each of the six
**OUT:** "procedures I perform" → their treatment pages (McCarty adds OptiLIF when live;
Varghese adds SI; Maslak adds endoscopic when live) · "conditions I treat" chips → 2–4
canons · location chips → their clinic pages · "meet the full team" → hub team module
**IN:** hub team module · every treatment page they perform (surgeon modules) · location
rosters (Paul's modules) · guide bylines ("medically reviewed by") once guides ship
