# Bio page — Dr. Jonathan Heyl, D.O.

**URL:** `https://synergyhealth.org/providers/jonathan-heyl-do/`
**Status:** DRAFT — pending Dr. Heyl's approval. One section can't be finished without him.
**Reviewed by:** ☐ Dr. Heyl (everything clinical + the personal section) ☐ Credentialing (credential
strings) ☐ Joe (mechanics)

---

## Page title and description

**Title** (58 characters):
> Jonathan Heyl, DO | Pain & Nerve Specialist | Livonia, MI

**Meta description** (152 characters):
> Dr. Jonathan Heyl treats spine, joint and nerve pain in Livonia and Sterling Heights. Rehabilitation-trained, fellowship-trained in pain medicine.

**URL slug:** `jonathan-heyl-do` — nothing else. See `08-url-lock.md`.

---

## Page copy

### H1
> Jonathan Heyl, D.O.

### Subhead
> Pain Medicine · Livonia and Sterling Heights

### Opening — the differentiator

> Dr. Jonathan Heyl treats pain by first working out what's actually causing it — and what it's
> stopping you from doing.
>
> His training is in two fields that fit together. He completed a residency in Physical Medicine and
> Rehabilitation at the University of Michigan, where he served as Chief Resident. That's the
> specialty concerned with movement and function: how the body works, where it's breaking down, and
> what it takes to get someone back to the things they care about. He then completed an
> ACGME-accredited Pain Medicine fellowship in the University of Michigan Department of
> Anesthesiology, which added advanced training in image-guided procedures that treat a specific
> source of pain directly.
>
> The combination shapes how he practices. Rather than treating a pain score, he looks for the
> specific structure — a joint, a nerve, a disc — that's generating the problem, and for what that
> pain is keeping you from doing. Then he treats that.

### ⚠️ Personal section — BLOCKED

> **Cannot be written until Dr. Heyl answers question 3 in `01-email-to-heyl.md`.**
>
> This is typically the most-read paragraph on a physician's page. Two to four sentences in his own
> words about why he chose pain medicine. **Do not write this for him and do not publish the page
> without it** — a bio with credentials and no person in it reads like a directory entry.
>
> *Placeholder, remove before publishing:*
> `[WHY PAIN MEDICINE — 2–4 sentences in Dr. Heyl's own words, from his email]`
>
> *If he grants permission (see `04-provider-record.md`), add after it:*
> `[Grew up in Marine City, Michigan. Played baseball at Siena Heights University, where he
> graduated summa cum laude — a background that shapes how he thinks about movement and mechanics.]`

### What he treats

> **Nerve pain**
> Pinched or irritated nerves, nerve pain that follows a specific path, numbness or tingling in the
> arms or legs, nerve pain after surgery or injury, and complex regional pain syndrome.
>
> **Back and neck pain**
> Ongoing low back and neck pain, sciatica, spinal stenosis and the leg pain that comes with walking,
> sacroiliac joint pain, and arthritis-related spine pain.
>
> **Joint and muscle pain**
> Knee, hip, shoulder and other joint pain, and focal muscle pain that hasn't responded to therapy.
>
> **Headache and facial nerve pain**
> Focal headaches and facial nerve pain that may respond to a targeted nerve block.
>
> **Nerve testing**
> EMG and nerve conduction studies — the tests that show whether a nerve is genuinely being pinched
> or damaged, and where.

### What he does

> Dr. Heyl uses image guidance to treat a specific structure precisely.
>
> - Epidural injections — lumbar, cervical and caudal
> - Medial branch blocks and radiofrequency ablation
> - Sacroiliac joint and other joint injections
> - Trigger-point injections
> - Peripheral nerve blocks
> - Occipital and facial nerve blocks
> - Genicular nerve blocks and ablation for knee pain
> - Peripheral nerve stimulation
> - Spinal cord stimulation
> - EMG and nerve conduction studies
>
> *Editor's note, remove before publishing: this list must match the Operations-confirmed list in
> `04-provider-record.md`. Anything unconfirmed on Aug 21 comes off.*

### What happens at your first visit

> Your first appointment is an evaluation, not a procedure.
>
> Dr. Heyl will examine you, review your history and any imaging, and work out the most likely
> source of your pain. You'll leave knowing three things: what he thinks is causing it, what the
> next step is, and how that step connects to something specific you want to be able to do again.
>
> He won't promise an injection, a medication or a scan before he's examined you. If a procedure is
> the right next step, he'll explain why and what to expect. If it isn't, he'll tell you that too.
>
> If more than one thing is causing pain, he'll usually address them one at a time — treating the
> clearest problem first tells you whether it was the right target.

### Where he practices

> **Livonia** — Monday and Tuesday
> 36622 Five Mile Road, Livonia, MI 48154
>
> **Sterling Heights** — Wednesday
> 35735 Mound Road, Sterling Heights, MI 48310
>
> *Verify against `04-provider-record.md` before publishing.*

### Training and education

> **Fellowship** — Pain Medicine, University of Michigan, Department of Anesthesiology (2025–2026)
> **Residency** — Physical Medicine and Rehabilitation, University of Michigan (2022–2025), Chief Resident
> **Medical school** — Lake Erie College of Osteopathic Medicine – Bradenton, D.O. (2021)
> **Undergraduate** — Siena Heights University, B.S. Biology, summa cum laude (2017)
>
> **Board certification** — Board certified in Physical Medicine and Rehabilitation. Board eligible
> in Pain Medicine.
>
> **Memberships** — International Pain and Spine Intervention Society · North American Spine Society ·
> American Academy of Physical Medicine and Rehabilitation

### For referring providers

> Dr. Heyl accepts referrals for persistent back or neck pain, nerve pain following a specific path,
> suspected peripheral nerve problems, patients who need EMG clarification, and patients who may be
> candidates for an interventional option after conservative care.
>
> He works within Synergy's integrated spine and orthopedic team, so patients who turn out to need
> surgical review get it without starting over somewhere else — and patients who don't need surgery
> aren't pushed toward it.
>
> [Referral information →] [Call to refer: (855) 750-5757]

### Calls to action

> Primary: **Request an appointment**
> Secondary: **Call (855) 750-5757**
> Tertiary: **Refer a patient**

---

## Build notes for Paul

- **Reading level: Grade 6–8.** Run it before publishing.
- **Images:** primary portrait 4:5, from the Aug 10 shoot. Every image needs `width` and `height`
  attributes set — missing image dimensions are the named cause of the layout-shift problem
  currently failing our page-speed scores sitewide. Don't add to it.
- **Alt text:** `Dr. Jonathan Heyl, D.O., pain medicine physician at Synergy Health Partners`
- **Schema:** hand-built. Use `07-physician-schema.json`. Do not let the bio template generate it.
- **Internal links in, minimum 8:** pain management page · spine hub · Livonia location · Sterling
  Heights location · EMG page · peripheral nerve page · neurogenic claudication page · providers index
- **Internal links out:** each procedure page he's cleared for
- **Before publish:** run `08-url-lock.md` and `09-taxonomy-firewall-check.md`

## Review gates

| Section | Who signs off | Why |
|---|---|---|
| Opening + training | Dr. Heyl **and** Credentialing | Credential accuracy is a regulatory issue |
| Personal section | Dr. Heyl | It's his words; we can't write them |
| What he treats / what he does | Dr. Heyl + Operations | Clinical accuracy; only promote what's live |
| First visit | Dr. Heyl | It's his process, and the phones will repeat it |
| Locations / hours | Operations | |
| Title, meta, schema, links | Joe | Marketing mechanics — no clinical review needed |
