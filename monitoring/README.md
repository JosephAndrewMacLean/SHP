# SHP Brand & Metro Detroit Spine-Surgeon Monitoring (RSS)

A robust, no-cost, no-login listening net for **Synergy Health Partners** — every
brand mention (current + legacy names), every spine-surgeon name mention, and the
Reddit conversations where metro Detroit patients ask *"who's a good spine surgeon
near me?"*

Everything here is built on **free, stable, auth-free RSS endpoints** (Google News,
Bing News, Reddit). No API keys, no paid social-listening tool, no scraping. Import
one file and you're listening.

---

## TL;DR — get listening in 2 minutes

1. Open your RSS reader (Feedly, Inoreader, Readwise Reader, NetNewsWire, NewsBlur,
   Miniflux, Feedbin — any of them).
2. Import **`shp-brand-monitoring.opml`** (every reader has *Import OPML* — usually
   under Settings → Import, or "Add content → Import OPML").
3. You now have **46 feeds in 8 folders**. Skim the Tier 1 folders daily, Tier 2
   a few times a week, Tier 3 weekly.

That's it. Full clickable list of every feed is in **`feed-list.md`**.

---

## What's being monitored (the 8 folders)

| Tier | Folder | What it catches |
|---|---|---|
| **1** | Brand mentions — News/Web | "Synergy Health Partners", synergyhealth.org, and legacy **Mendelson Orthopaedic / Kornblum / mendelsonortho** across news + indexed web (Google + Bing) |
| **1** | Brand mentions — Reddit | Any Reddit thread naming the brand (current or legacy) or linking the site |
| **1** | Spine surgeons by name — News/Web | Varghese, Salar, Maslak, McCarty, Zamorano + the interventional-pain bench (Oddo, Kassa, Singh, Lee) |
| **2** | Spine surgeons by name — Reddit | Same surgeons, last-name + "spine" on Reddit |
| **2** | Metro Detroit spine discovery — Reddit | "spine surgeon Michigan", "back surgery Michigan", spinal fusion / sciatica / stenosis + Michigan — **the demand-signal folder** |
| **2** | Local subreddits — Reddit | r/Detroit, r/Michigan, r/askDetroit scoped to surgeon/spine recs, plus new posts in r/troymi, r/RochesterMI, r/Livonia |
| **2** | Condition subreddits — Reddit | r/backpain, r/Sciatica, r/spinalfusion, r/spine, r/Scoliosis, r/ChronicPain — filtered to **Michigan/Detroit only** so you don't drown in global posts |
| **3** | Competitor intel | Michigan Orthopaedic Specialists, Detroit Bone & Joint (news + Reddit) |

Why three sources instead of one: Google News and Bing News index different corners
of the web, and Reddit isn't in either news index — so brand/surgeon coverage is
deliberately redundant. If one source misses a mention, another usually catches it.

---

## How the feeds are built (and how to change them)

Everything is generated from one script — **`generate-feeds.py`** — which is the
single source of truth. The search terms live near the top (brand names, GEO
qualifier, surgeon roster). To add a surgeon, tune a query, or drop a competitor:

```bash
cd monitoring
# edit generate-feeds.py (the FEEDS section)
python3 generate-feeds.py     # regenerates the .opml AND feed-list.md
```

Re-import the OPML (most readers de-dupe on re-import, or import into a fresh folder).

**Feed URL formats** (all documented, stable, no auth):
- Google News: `https://news.google.com/rss/search?q=<query>&hl=en-US&gl=US&ceid=US:en`
- Bing News: `https://www.bing.com/news/search?q=<query>&format=rss`
- Reddit sitewide: `https://www.reddit.com/search.rss?q=<query>&sort=new`
- Reddit subreddit: `https://www.reddit.com/r/<sub>/search.rss?q=<query>&restrict_sr=1&sort=new`

Query operators that make these *robust* (used throughout): `"exact phrase"`, `OR`,
parenthesised `(A OR B)` geo-qualifiers to kill false positives. Google News also
supports `when:7d` / `when:30d` if you ever want to force a recency window.

---

## ⚠️ Healthcare compliance — read before you engage

These feeds are for **listening**, not public patient interaction. Per
`CLAUDE.md` / `brand/brand-brief.md`:

- **Never respond to a patient's health situation on a public thread.** No PHI, no
  "we can help with your herniated disc," no confirming anyone is a patient (HIPAA).
  If someone is clearly seeking care, the only safe public move is a neutral pointer
  to book/contact through official channels — and even that is a **judgment call for a
  human**, not an automated reply.
- **Reddit especially:** most subreddits ban brand/vendor self-promotion. Astroturfing
  ("I love Synergy!") is both against Reddit rules and an **FTC disclosure violation**.
  Any genuine staff participation must be disclosed as such.
- **Route, don't freelance.** Negative reviews, safety complaints, or a possible crisis
  → hand to `pr-specialist` (reputation/crisis) and practice leadership. Wait-time
  complaints are the flagged top sentiment risk — log them, don't argue them.
- **Reputation ≠ diagnosis.** Use mentions to inform content, PR, and referral
  messaging — not to give medical advice.

---

## Suggested triage cadence

- **Daily (5 min):** both Tier 1 brand folders + Tier 1 surgeon news. These are your
  "did anyone say our name" alerts.
- **2–3×/week:** Tier 2 "Metro Detroit spine discovery" and "Local subreddits" — this
  is where **prospective spine patients** are literally asking for a surgeon
  recommendation. Feeds directly into the spine-growth priority (see
  `playbooks/spine-90day-plan.md`). Capture recurring questions as **content-creator**
  FAQ/hub fodder and note competitor names that get recommended.
- **Weekly:** Tier 3 competitor intel + condition subreddits.

Tag anything actionable to the right owner: PR → reputation/press; content-creator →
recurring patient questions; SEO/AEO → question phrasings to target; marketing-director
→ anything cross-cutting.

---

## Known limits & optional upgrades

- **This container can't preview the feeds.** The session's network policy blocks
  `news.google.com` and `reddit.com` (same reason it blocks `synergyhealth.org`), so
  the feeds were built from their documented URL formats and the OPML is validated as
  well-formed XML — but they must be subscribed from your own reader on an open network.
  If any feed looks empty on day one, that's normal: an empty search feed just means
  no mention *yet* (that's the point of monitoring).
- **"Kevin Lee" is a very common name** — that feed is heavily geo/context-qualified and
  will still be the noisiest. Prune if it's not earning its keep.
- **Reddit rate-limits** aggressive polling. Let your reader poll on its default
  schedule (usually hourly); don't set it to sub-minute refresh.
- **Add-ons that need a login (not in the OPML):**
  - **Google Alerts** — create alerts for the same brand/surgeon terms and choose
    "Deliver to: RSS feed" to get an alert-grade feed you can drop into the same reader.
  - **YouTube** — the legacy `@mendelsonortho` channel can be watched via
    `https://www.youtube.com/feeds/videos.xml?channel_id=<ID>` once you grab its
    channel ID.
  - **Reviews (Google/Healthgrades/Yelp)** don't offer RSS; those are covered via the
    Google Business Profile MCP (`list_reviews`) and Semrush, not this file.

---

## Files in this folder

| File | Purpose |
|---|---|
| `shp-brand-monitoring.opml` | **Import this** into your RSS reader — all 46 feeds, foldered |
| `feed-list.md` | Human-readable index of every feed with clickable URLs |
| `generate-feeds.py` | Source of truth — edit + rerun to change/extend the feed set |
| `README.md` | This guide |
