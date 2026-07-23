#!/usr/bin/env python3
"""
Generate SHP brand + spine-surgeon monitoring feeds.

Emits, from a single source of truth (the FEEDS list below):
  - shp-brand-monitoring.opml   -> import into any RSS reader (Feedly, Inoreader,
                                    NetNewsWire, Readwise Reader, NewsBlur, Miniflux...)
  - feed-list.md                -> human-readable table of every feed + clickable URL

All feeds are built from stable, no-auth RSS endpoints:
  - Google News RSS   https://news.google.com/rss/search?q=...
  - Bing News RSS     https://www.bing.com/news/search?q=...&format=rss
  - Reddit search RSS https://www.reddit.com/search.rss?q=...
  - Reddit sub RSS    https://www.reddit.com/r/<sub>/{search,new}.rss

Run:  python3 generate-feeds.py
No third-party dependencies (stdlib only).
"""

from urllib.parse import quote_plus
from xml.sax.saxutils import escape as xml_escape

# ----------------------------------------------------------------------------
# Brand + roster source terms (kept in sync with brand/ and provider roster)
# ----------------------------------------------------------------------------
# Current brand: Synergy Health Partners / synergyhealth.org
# Legacy (rebrand in progress): Mendelson Orthopaedic / Mendelson Kornblum / mendelsonortho
# Spine surgeons + interventional pain: from brand/provider-roster-by-service-line.md

GEO = '(Michigan OR Detroit OR Livonia OR Troy OR Southfield OR "Sterling Heights" OR Rochester OR Oakland)'


# ---- Feed URL builders ------------------------------------------------------
def gnews(q):
    """Google News RSS search feed (web + press mentions, most robust)."""
    return f"https://news.google.com/rss/search?q={quote_plus(q)}&hl=en-US&gl=US&ceid=US:en"


def bnews(q):
    """Bing News RSS search feed (redundancy — catches what Google misses)."""
    return f"https://www.bing.com/news/search?q={quote_plus(q)}&format=rss&setlang=en-US"


def rsearch(q):
    """Reddit sitewide search RSS, newest first."""
    return f"https://www.reddit.com/search.rss?q={quote_plus(q)}&sort=new&limit=50"


def rsub_search(sub, q):
    """Reddit search RSS scoped to a single subreddit, newest first."""
    return (f"https://www.reddit.com/r/{sub}/search.rss?"
            f"q={quote_plus(q)}&restrict_sr=1&sort=new&limit=50")


def rsub_new(sub):
    """Reddit newest-posts RSS for a whole subreddit (for small local subs)."""
    return f"https://www.reddit.com/r/{sub}/new/.rss"


# ---- The feed set -----------------------------------------------------------
# Each entry: (category, title, url)
FEEDS = []


def add(cat, title, url):
    FEEDS.append((cat, title, url))


# === TIER 1 — BRAND MENTIONS (news + web) ===================================
C = "Tier 1 · Brand mentions — News/Web"
add(C, "Google News · \"Synergy Health Partners\" (geo-qualified)",
    gnews('"Synergy Health Partners" ' + GEO))
add(C, "Google News · \"Synergy Health Partners\" (exact phrase, catch-all)",
    gnews('"Synergy Health Partners"'))
add(C, "Google News · synergyhealth.org (domain mentions)",
    gnews('synergyhealth.org'))
add(C, "Google News · Mendelson Orthopaedic / mendelsonortho (legacy brand)",
    gnews('"Mendelson Orthopaedic" OR "Mendelson Orthopedic" OR mendelsonortho'))
add(C, "Google News · \"Mendelson Kornblum\" (legacy brand)",
    gnews('"Mendelson Kornblum"'))
add(C, "Bing News · \"Synergy Health Partners\" Michigan (redundancy)",
    bnews('"Synergy Health Partners" Michigan'))
add(C, "Bing News · Mendelson Orthopaedic Michigan (redundancy)",
    bnews('"Mendelson Orthopaedic" OR mendelsonortho Michigan'))

# === TIER 1 — BRAND MENTIONS (Reddit) ======================================
C = "Tier 1 · Brand mentions — Reddit"
add(C, "Reddit · \"Synergy Health Partners\"",
    rsearch('"Synergy Health Partners"'))
add(C, "Reddit · Mendelson orthopedic / mendelsonortho",
    rsearch('Mendelson orthopedic OR mendelsonortho OR "Mendelson Kornblum"'))
add(C, "Reddit · synergyhealth.org (link/domain mentions)",
    rsearch('synergyhealth.org'))

# === TIER 1 — SPINE SURGEONS by name (news) =================================
C = "Tier 1 · Spine surgeons by name — News/Web"
add(C, "Google News · Jeffrey Varghese (spine)",
    gnews('"Jeffrey Varghese" (spine OR surgeon OR Synergy OR Michigan)'))
add(C, "Google News · Mohamed Salar (spine)",
    gnews('"Mohamed Salar" (spine OR surgeon OR Synergy OR Michigan)'))
add(C, "Google News · Joseph Maslak (spine)",
    gnews('"Joseph Maslak" (spine OR surgeon OR Synergy OR Michigan)'))
add(C, "Google News · Scott McCarty (spine)",
    gnews('"Scott McCarty" (spine OR surgeon OR Synergy OR Michigan)'))
add(C, "Google News · Lucia Zamorano (neurosurgeon/spine)",
    gnews('"Lucia Zamorano" (neurosurgeon OR spine OR Synergy OR Michigan)'))
add(C, "Google News · Interventional pain (Oddo / Kassa / Singh)",
    gnews('("Anthony Oddo" OR "Brian Kassa" OR "Hanish Singh") '
          '(pain OR spine OR Synergy OR Michigan)'))
add(C, "Google News · Kevin Lee (pain, heavily qualified — noisy name)",
    gnews('"Kevin Lee" (Synergy OR "pain management" OR "functional neurosurgery") Michigan'))

# === TIER 2 — SPINE SURGEONS by name (Reddit) ==============================
C = "Tier 2 · Spine surgeons by name — Reddit"
add(C, "Reddit · Varghese spine",  rsearch('Varghese spine'))
add(C, "Reddit · Maslak spine",    rsearch('Maslak spine'))
add(C, "Reddit · Salar spine",     rsearch('Salar spine'))
add(C, "Reddit · McCarty spine surgeon", rsearch('McCarty spine surgeon'))
add(C, "Reddit · Zamorano neurosurgeon", rsearch('Zamorano neurosurgeon OR Zamorano spine'))

# === TIER 2 — METRO DETROIT SPINE DISCOVERY (Reddit sitewide) ==============
# Where prospective patients ask "who's a good spine surgeon near Detroit?"
C = "Tier 2 · Metro Detroit spine discovery — Reddit"
add(C, "Reddit · spine surgeon Michigan",       rsearch('spine surgeon Michigan'))
add(C, "Reddit · spine surgery Detroit",        rsearch('spine surgery Detroit'))
add(C, "Reddit · back surgery Michigan",        rsearch('"back surgery" Michigan'))
add(C, "Reddit · neck / cervical fusion Michigan",
    rsearch('"neck surgery" Michigan OR "cervical fusion" Michigan'))
add(C, "Reddit · spinal fusion Michigan",       rsearch('"spinal fusion" Michigan'))
add(C, "Reddit · herniated disc / sciatica Michigan",
    rsearch('"herniated disc" Michigan OR sciatica Michigan'))
add(C, "Reddit · spinal stenosis Michigan",     rsearch('"spinal stenosis" Michigan'))
add(C, "Reddit · minimally invasive spine Michigan",
    rsearch('"minimally invasive spine" Michigan OR "minimally invasive" Detroit spine'))

# === TIER 2 — LOCAL SUBREDDITS (scoped search + small-sub new) =============
C = "Tier 2 · Local subreddits — Reddit"
add(C, "r/Detroit · spine / back surgery / surgeon recs",
    rsub_search("Detroit", 'spine OR "back surgery" OR "spine surgeon" OR "orthopedic surgeon"'))
add(C, "r/Michigan · spine surgeon / back surgery recs",
    rsub_search("Michigan", '"spine surgeon" OR "back surgery" OR "orthopedic surgeon"'))
add(C, "r/askDetroit · spine / surgeon recs",
    rsub_search("askDetroit", 'spine OR surgeon OR "back surgery"'))
add(C, "r/troymi · all new posts (small sub — watch directly)", rsub_new("troymi"))
add(C, "r/RochesterMI · all new posts (small sub — watch directly)", rsub_new("RochesterMI"))
add(C, "r/Livonia · all new posts (small sub — watch directly)", rsub_new("Livonia"))

# === TIER 2 — CONDITION SUBREDDITS (scoped to Michigan/Detroit) ============
C = "Tier 2 · Condition subreddits (Michigan/Detroit only) — Reddit"
add(C, "r/backpain · Michigan/Detroit",   rsub_search("backpain", 'Michigan OR Detroit'))
add(C, "r/Sciatica · Michigan/Detroit",   rsub_search("Sciatica", 'Michigan OR Detroit'))
add(C, "r/spinalfusion · Michigan/Detroit", rsub_search("spinalfusion", 'Michigan OR Detroit'))
add(C, "r/spine · Michigan/Detroit",      rsub_search("spine", 'Michigan OR Detroit'))
add(C, "r/Scoliosis · Michigan/Detroit",  rsub_search("Scoliosis", 'Michigan OR Detroit'))
add(C, "r/ChronicPain · Michigan/Detroit spine",
    rsub_search("ChronicPain", '(Michigan OR Detroit) spine'))

# === TIER 3 — COMPETITOR INTEL (situational awareness) =====================
C = "Tier 3 · Competitor intel"
add(C, "Google News · Michigan Orthopaedic Specialists",
    gnews('"Michigan Orthopaedic Specialists"'))
add(C, "Google News · Detroit Bone & Joint",
    gnews('"Detroit Bone & Joint" OR "Detroit Bone and Joint"'))
add(C, "Reddit · Michigan Orthopaedic Specialists",
    rsearch('"Michigan Orthopaedic Specialists"'))
add(C, "Reddit · Detroit Bone and Joint",
    rsearch('"Detroit Bone and Joint" OR "Detroit Bone & Joint"'))


# ---- Writers ----------------------------------------------------------------
def write_opml(path):
    cats = []
    for cat, title, url in FEEDS:
        if not cats or cats[-1][0] != cat:
            cats.append((cat, []))
        cats[-1][1].append((title, url))

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<opml version="2.0">',
        '  <head>',
        '    <title>SHP — Brand &amp; Metro Detroit Spine Surgeon Monitoring</title>',
        '  </head>',
        '  <body>',
    ]
    for cat, items in cats:
        c_esc = xml_escape(cat, {'"': '&quot;'})
        lines.append(f'    <outline text="{c_esc}" title="{c_esc}">')
        for title, url in items:
            t = xml_escape(title, {'"': '&quot;'})
            u = xml_escape(url, {'"': '&quot;'})
            lines.append(
                f'      <outline type="rss" text="{t}" title="{t}" '
                f'xmlUrl="{u}" htmlUrl="{u}"/>'
            )
        lines.append('    </outline>')
    lines += ['  </body>', '</opml>', '']
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return len(FEEDS), len(cats)


def write_feedlist(path):
    cats = []
    for cat, title, url in FEEDS:
        if not cats or cats[-1][0] != cat:
            cats.append((cat, []))
        cats[-1][1].append((title, url))

    out = ["# SHP monitoring — full feed list",
           "",
           "> Auto-generated by `generate-feeds.py`. Import "
           "`shp-brand-monitoring.opml` into your RSS reader to subscribe to all of "
           "these at once. This table is the human-readable index.",
           ""]
    for cat, items in cats:
        out.append(f"## {cat}")
        out.append("")
        for title, url in items:
            out.append(f"- **{title}**")
            out.append(f"  <{url}>")
        out.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))


if __name__ == "__main__":
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    n, c = write_opml(os.path.join(here, "shp-brand-monitoring.opml"))
    write_feedlist(os.path.join(here, "feed-list.md"))
    print(f"Wrote {n} feeds across {c} categories.")
    print("  -> shp-brand-monitoring.opml")
    print("  -> feed-list.md")
