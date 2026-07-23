# SHP Brand, Provider & Metro Detroit Spine-Surgeon Monitoring (RSS)

A robust, no-cost, no-login listening net for **Synergy Health Partners** — every
brand mention (current + legacy names), **a mention watch on every provider on the
roster by name**, and the Reddit conversations where metro Detroit patients ask
*"who's a good spine surgeon near me?"*

Everything here is built on **free, stable, auth-free RSS endpoints** (Google News,
Bing News, Reddit). No API keys, no paid social-listening tool, no scraping. Import
one file and you're listening. **71 feeds across 14 folders.**

---

## TL;DR — get listening in 2 minutes

1. Open your RSS reader (Feedly, Inoreader, Readwise Reader, NetNewsWire, NewsBlur,
   Miniflux, Feedbin — any of them). No reader yet? See **Setup walkthrough** below.
2. Import **`shp-brand-monitoring.opml`** (every reader has *Import OPML* — usually
   under Settings → Import, or "Add content → Import OPML").
3. You now have **71 feeds in 14 folders**. Skim the Tier 1 / Provider folders daily,
   Tier 2 a few times a week, Tier 3 weekly.

That's it. Full clickable list of every feed is in **`feed-list.md`**.

---

## What's being monitored (the 14 folders)

| Group | Folder | What it catches |
|---|---|---|
| **Brand** | Brand mentions — News/Web | "Synergy Health Partners", synergyhealth.org, and legacy **Mendelson Orthopaedic / Kornblum / mendelsonortho** across news + indexed web (Google + Bing) |
| **Brand** | Brand mentions — Reddit | Any Reddit thread naming the brand (current or legacy) or linking the site |
| **Providers** | Spine — News/Web | Individual feed per surgeon: Varghese, Salar, Maslak, McCarty, Zamorano |
| **Providers** | Pain (interventional spine) — News/Web | Oddo, Kassa, Singh, Lee (heavily qualified — common name) |
| **Providers** | Orthopedics / joint / sports — News/Web | The four Mendelsons, Bhullar, Mayo (excl. "Mayo Clinic"), Yacisen |
| **Providers** | Hand & wrist — News/Web | Kyle Bohm |
| **Providers** | Foot & ankle (podiatry) — News/Web | Klein, Sorensen, R. Leff, Green, F. Leff |
| **Providers** | Primary care & sports chiro — News/Web | Abood + chiros (Fox, Elwart, Truscott) |
| **Providers** | Reddit (mentions by service line) | One grouped Reddit feed per line — every provider name OR'd |
| **Providers** | Allied health — News/Web | PT / PTA / OT / PA-C, grouped (completeness; low-signal, prune freely) |
| **Discovery** | Metro Detroit spine discovery — Reddit | "spine surgeon Michigan", "back surgery Michigan", fusion / sciatica / stenosis + Michigan — **the demand-signal folder** |
| **Local** | Local subreddits — Reddit | r/Detroit, r/Michigan, r/askDetroit scoped to surgeon/spine recs, plus new posts in r/troymi, r/RochesterMI, r/Livonia |
| **Condition** | Condition subreddits (MI/Detroit only) — Reddit | r/backpain, r/Sciatica, r/spinalfusion, r/spine, r/Scoliosis, r/ChronicPain — filtered to **Michigan/Detroit only** |
| **Competitor** | Competitor intel | Michigan Orthopaedic Specialists, Detroit Bone & Joint (news + Reddit) |

**Provider coverage = the whole roster.** Every physician (MD/DO/DPM) gets an
individual news feed — they're the ones with press/review/profile footprints worth
watching one-by-one. Each service line gets one grouped Reddit feed (name mentions
like *"saw Dr. Maslak, great spine surgeon"*). Allied health (PT/OT/PA-C) is included
in grouped news feeds for completeness, but is individually low-signal — prune those
if they don't earn their keep.

Why three sources instead of one: Google News and Bing News index different corners
of the web, and Reddit isn't in either news index — so brand/provider coverage is
deliberately redundant. If one source misses a mention, another usually catches it.

---

## Setup walkthrough (Inoreader — recommended; Feedly similar)

You need an RSS reader account once; then it polls all 71 feeds forever. **Inoreader**
is the best fit here (free tier works; supports OPML folders, keyword *rules*, and
email/Slack/Telegram alerts on new matches). Feedly works the same way for import.

1. **Create an account** at inoreader.com (or feedly.com). Free tier is fine to start.
2. **Import the OPML:** Inoreader → *Preferences → Import/Export → Choose file →*
   upload `shp-brand-monitoring.opml → Import*. (Feedly: *Organize/Settings → Import
   OPML*.) All 14 folders appear in the sidebar.
3. **Set refresh + first fill:** feeds populate on the reader's schedule (Inoreader
   free ≈ hourly). A brand-new search feed that shows nothing just means *no mention
   yet* — that's the point.
4. **(Optional) push alerts instead of skimming:** Inoreader → select the *Brand
   mentions* and *Provider* folders → *Rules* → "when new article matches, send
   email / mobile push / Slack." Now a fresh brand or provider mention pings you
   without opening the reader.
5. **(Optional) share the load:** in Inoreader, folders can be shared to teammates so
   PR watches the brand/competitor folders and content watches the discovery folder.

Prefer to run it as an automated digest into email/Slack instead of a reader? That's
a small scheduled job (a GitHub Action on a cron) — ask and I'll wire it up; it needs
to run somewhere with open internet, since this workspace's network policy can't reach
these hosts (see *Known limits*).

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

- **Daily (5 min):** both brand folders + the six provider **News/Web** folders and the
  provider **Reddit** folder. These are your "did anyone say our name — or a provider's
  name" alerts. (Best done as push-alert rules per the setup walkthrough, so you only
  look when something lands.)
- **2–3×/week:** "Metro Detroit spine discovery" and "Local subreddits" — this is where
  **prospective spine patients** are literally asking for a surgeon recommendation. Feeds
  directly into the spine-growth priority (see `playbooks/spine-90day-plan.md`). Capture
  recurring questions as **content-creator** FAQ/hub fodder; note competitor names that
  get recommended; a thread naming *our* surgeon well is PR/testimonial-lead material
  (with consent).
- **Weekly:** competitor intel + condition subreddits + the low-signal allied-health
  folder.

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
- **Reviews (Google/Healthgrades/Yelp)** don't offer RSS; those are covered via the
  Google Business Profile connection (`list_reviews`) and Semrush, not this file.

---

## Automated daily digest (GitHub Actions — no reader required)

If you'd rather have mentions **pushed to you** than skim a reader, the repo ships a
workflow that emails / Slacks a daily roundup. It runs on GitHub's runners (open
internet), so it works despite this workspace's network policy.

- **Workflow:** `.github/workflows/brand-monitor-digest.yml` — runs **daily at 13:00 UTC
  (~9am ET)**, plus a manual *Run workflow* button. It executes `monitoring/digest.py`,
  which fetches all 72 feeds, keeps items from the last 24h, and renders a foldered digest.
- **Delivery is opt-in via repo secrets** (*Settings → Secrets and variables → Actions*):
  - **Slack:** add `SLACK_WEBHOOK_URL` (a Slack Incoming Webhook).
  - **Email:** add `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`, `EMAIL_FROM`,
    `EMAIL_TO` (any SMTP provider — Gmail app password, SendGrid, SES, etc.).
  - **No secrets?** The digest still renders to the Actions **run summary** — open the
    run to read it. Good for a no-setup trial.
- By default it stays quiet when there's nothing new (set `SEND_WHEN_EMPTY=true` to
  always ping). Failed feeds (usually transient Reddit rate-limiting) are listed at the
  bottom and simply retry next run.
- **Try it now:** Actions tab → *Brand & Provider Monitoring Digest* → *Run workflow*.

The digest reads the same OPML, so it stays in sync automatically — regenerate the OPML
and the digest picks up the changes on its next run.

---

## Add-on layers (optional)

- **Google Alerts (RSS):** a second, independent listening layer that catches editorial
  web pages the news feeds miss. One-time ~10-min setup in **`google-alerts-setup.md`** —
  create the alerts, paste their RSS URLs into **`extra-feeds.tsv`**, rerun the generator,
  and they fold into both the reader and the digest.
- **YouTube:** the legacy **Mendelson Orthopedics** channel (`@mendelsonortho`,
  `channel_id UC5SlFVjHx7W1CiDpM0aP1hA`) is already wired in as a video feed. Add a
  Synergy-branded channel by dropping its `UC…` id into `YOUTUBE_CHANNELS` in
  `generate-feeds.py` and rerunning.
- **Reviews:** Google/Healthgrades/Yelp have no RSS — use the Google Business Profile
  connection (`list_reviews`) + Semrush for those.

---

## Files in this folder

| File | Purpose |
|---|---|
| `shp-brand-monitoring.opml` | **Import this** into your RSS reader — all 72 feeds, foldered |
| `feed-list.md` | Human-readable index of every feed with clickable URLs |
| `generate-feeds.py` | Source of truth — edit + rerun to change/extend the feed set |
| `extra-feeds.tsv` | Paste Google Alerts (or any) RSS URLs here; merged into the OPML on regen |
| `digest.py` | The daily-digest engine (run by the GitHub Action; stdlib only) |
| `google-alerts-setup.md` | How to create Google Alerts as RSS and fold them in |
| `README.md` | This guide |

The digest workflow itself lives at `.github/workflows/brand-monitor-digest.yml`.
