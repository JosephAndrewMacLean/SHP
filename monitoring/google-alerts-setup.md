# Google Alerts → RSS (optional, high-value add-on)

Google Alerts is a second, independent listening layer. It often catches editorial
web pages, blogs, and directory updates that the Google/Bing **News** feeds miss, and
Google de-dupes it for you. Each alert can be delivered **as an RSS feed**, so it drops
straight into the same reader — and into the daily digest — as everything else.

You can't create these programmatically (Google requires a signed-in Google account),
so this is a one-time ~10-minute manual setup. Do it once and it runs forever.

## Create the alerts

1. Sign in to the **marketing Google account** and go to **<https://www.google.com/alerts>**.
2. Type a query (see the recommended list below) into the box at the top.
3. Click **Show options** and set:
   - **How often:** *At most once a day* (or *As-it-happens* for the brand alerts)
   - **Sources:** *Automatic*
   - **Language:** English · **Region:** United States
   - **How many:** *All results*
   - **Deliver to:** **RSS feed**  ← this is the important one
4. Click **Create Alert**.
5. Back on the alerts page, each alert now shows an **RSS icon (orange)**. Right-click
   it → **Copy link address**. That URL looks like:
   `https://www.google.com/alerts/feeds/1234567890/9876543210`

## Recommended alerts (mirror the feed tiers)

**Brand (set these to *As-it-happens*):**
- `"Synergy Health Partners"`
- `synergyhealth.org OR mendelsonortho.com`
- `"Mendelson Orthopaedic" OR "Mendelson Kornblum"`

**Providers (once a day):**
- `"Jeffrey Varghese" spine`
- `"Scott McCarty" spine`
- `"Joseph Maslak" spine`
- `"Mohamed Salar" spine`
- `"Lucia Zamorano"`
- `"Kyle Bohm"`  (hand — "Michigan's only" percutaneous carpal tunnel; PR-worthy)
- `"Jeffrey Mendelson" OR "David Mendelson" OR "Stephen Mendelson" OR "Alice Mendelson"`

**Discovery / competitor (once a day, optional):**
- `"spine surgeon" Michigan`
- `"Michigan Orthopaedic Specialists"`
- `"Detroit Bone & Joint"`

## Fold them into the reader + digest

Paste each alert's RSS URL into **`extra-feeds.tsv`** (TAB-separated), e.g.:

```
Tier 1 · Brand mentions — Google Alerts	Google Alert · "Synergy Health Partners"	https://www.google.com/alerts/feeds/1234567890/9876543210
Providers · Google Alerts	Google Alert · Jeffrey Varghese	https://www.google.com/alerts/feeds/1234567890/1111111111
```

Then regenerate and re-import:

```bash
cd monitoring
python3 generate-feeds.py     # extra-feeds.tsv is merged into the OPML automatically
```

The new alert feeds now appear in `shp-brand-monitoring.opml` (re-import to your reader)
and are picked up by the daily GitHub Actions digest with no further changes.
