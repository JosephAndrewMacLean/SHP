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

import os
from urllib.parse import quote_plus
from xml.sax.saxutils import escape as xml_escape

_HERE = os.path.dirname(os.path.abspath(__file__))

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

# === PROVIDERS — mentions of ANY provider, by name =========================
# Data-driven from brand/provider-roster-by-service-line.md.
#   - Every PHYSICIAN (MD/DO/DPM) gets an individual news feed — they're the
#     ones with public/press/review footprints worth an individual watch.
#   - Each SERVICE LINE gets one grouped Reddit feed (name mentions on Reddit).
#   - ALLIED HEALTH (PT/OT/PA) is covered by grouped news feeds for
#     completeness (individually low-signal — prune freely).
# Each physician query is geo/brand/specialty-qualified to kill false positives;
# common names (Kevin Lee, Ben Mayo→Mayo Clinic, etc.) get extra qualifiers/excludes.

# (line_label, specialty_context_term, [(full_name, extra_qualifier, exclude_phrase)])
PROVIDER_LINES = [
    ("Spine", "spine", [
        ("Jeffrey Varghese", "surgeon", ""),
        ("Mohamed Salar", "surgeon", ""),
        ("Joseph Maslak", "surgeon", ""),
        ("Scott McCarty", "surgeon", ""),
        ("Lucia Zamorano", "neurosurgeon", ""),
    ]),
    ("Pain (interventional spine)", '"pain management"', [
        ("Anthony Oddo", "", ""),
        ("Brian Kassa", "", ""),
        ("Hanish Singh", "", ""),
        ("Kevin Lee", '"functional neurosurgery"', ""),   # very common name
    ]),
    ("Orthopedics / joint / sports", "orthopedic", [
        ("Jeffrey Mendelson", "", ""),
        ("David Mendelson", "", ""),
        ("Stephen Mendelson", "", ""),
        ("Alice Mendelson", "", ""),
        ("Preetinder Bhullar", "arthroplasty", ""),
        ("Ben Mayo", '"sports medicine"', '"Mayo Clinic"'),  # collides w/ Mayo Clinic
        ("Joseph Yacisen", '"sports medicine"', ""),
    ]),
    ("Hand & wrist", "hand", [
        ("Kyle Bohm", "surgeon", ""),
    ]),
    ("Foot & ankle (podiatry)", "podiatr", [
        ("Jeffrey Klein", "", ""),
        ("Kevin Sorensen", "", ""),
        ("Randy Leff", "", ""),
        ("Kristina Green", "", ""),
        ("Fred Leff", "", ""),
    ]),
    ("Primary care & sports chiro", "", [
        ("Tony Abood", '"family medicine"', ""),
        ("Ashley Fox", "chiropractic", ""),   # common name
        ("Francis Elwart", "chiropractic", ""),
        ("Kyle Truscott", "chiropractic", ""),
    ]),
]


def provider_news_query(name, ctx, extra, exclude):
    quals = ["Synergy", "Mendelson", "Michigan", "Detroit"]
    if ctx:
        quals.append(ctx)
    if extra:
        quals.append(extra)
    q = f'"{name}" ({" OR ".join(quals)})'
    if exclude:
        q += f" -{exclude}"
    return q


_prov_reddit = []
for _line, _ctx, _members in PROVIDER_LINES:
    Cn = f"Providers · {_line} — News/Web"
    for _name, _extra, _excl in _members:
        add(Cn, f"Google News · {_name}",
            gnews(provider_news_query(_name, _ctx, _extra, _excl)))
    _prov_reddit.append((_line, " OR ".join(f'"{n}"' for n, _e, _x in _members)))

# Grouped Reddit feeds — one per service line (kept together in one folder)
Crp = "Providers — Reddit (mentions by service line)"
for _line, _q in _prov_reddit:
    add(Crp, f"Reddit · {_line} providers", rsearch(_q))

# Allied health (PT / OT / PA-C) — grouped news feeds, completeness/low-signal
ALLIED = [
    ("Physical therapy (PT / DPT)", [
        "Cullen Lane", "Edyta Jagustin", "Beth Wilkins", "Simon Gappe",
        "Chris Kakos", "Maria Marcaida-Gorospe", "Sue Cash", "Fatema Taher",
        "Crystal Langholff", "Noah Kueber", "Amy Mazurek", "Kennie Brenner",
        "Mark Monton",
    ]),
    ("PT assistants (PTA)", [
        "Carol Arakelian", "Elaina Homer", "Ian Zaporski", "Sue Piotrowski",
        "Tiffany Hepworth", "Tony Badia", "Kathleen Blashfield", "Laura Winowiecki",
    ]),
    ("Hand / occupational therapy (OT / CHT)", [
        "Amy Hauxwell", "Loretta Assalone", "Max Castoreno", "Aaron Wienczak",
    ]),
    ("Physician assistants (PA-C) — group 1", [
        "Caitlin Rogers", "Elizabeth Zachow", "Andrew Cox", "Brittany Miller",
        "Samantha Houle", "Hayley Foster", "Evan VandenBosch", "Cassidy Ebach",
    ]),
    ("Physician assistants (PA-C) — group 2", [
        "Adelisa Zahirovic", "Pearl Dua", "Kelley Gray-Allen", "Larisa Joeright",
        "Spencer Poshadlo", "Elaine McCallister", "Mitch Misiak",
    ]),
]
Ca = "Providers · Allied health — News/Web (low-signal, prune freely)"
for _label, _names in ALLIED:
    _or = " OR ".join(f'"{n}"' for n in _names)
    add(Ca, f"Google News · {_label}",
        gnews(f"({_or}) (Synergy OR Mendelson OR Michigan)"))

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


# === OWNED / LEGACY VIDEO CHANNELS (YouTube) ===============================
# YouTube publishes a per-channel RSS feed (no auth):
#   https://www.youtube.com/feeds/videos.xml?channel_id=<UC...>
# The @handle is NOT the channel_id — you need the UC... id. How to find it:
#   1. Open the channel (e.g. https://www.youtube.com/@mendelsonortho)
#   2. View page source (Ctrl+U) and search for  "channelId"  or  "externalId"
#      -> copy the UC... value that follows.
# Then add (label, "UC...") tuples below and re-run this script.
YOUTUBE_CHANNELS = [
    ("Legacy · Mendelson Orthopedics (@mendelsonortho)", "UC5SlFVjHx7W1CiDpM0aP1hA"),
    # ("Synergy Health Partners", "UC__________________"),  # add if/when a Synergy-branded channel exists
]
if YOUTUBE_CHANNELS:
    Cy = "Owned/legacy channels — Video (YouTube)"
    for _label, _cid in YOUTUBE_CHANNELS:
        add(Cy, f"YouTube · {_label}",
            f"https://www.youtube.com/feeds/videos.xml?channel_id={_cid}")


# === EXTRA FEEDS (Google Alerts RSS + any manual adds) =====================
# Anything in extra-feeds.tsv is folded into the OPML on regeneration. This is
# where Google Alerts RSS URLs go (see monitoring/google-alerts-setup.md).
# Format, one feed per line (TAB-separated); '#' comments and blanks ignored:
#   Folder <TAB> Title <TAB> URL
_extra = os.path.join(_HERE, "extra-feeds.tsv")
if os.path.exists(_extra):
    with open(_extra, encoding="utf-8") as _fh:
        for _line in _fh:
            _line = _line.rstrip("\n")
            if not _line.strip() or _line.lstrip().startswith("#"):
                continue
            _parts = _line.split("\t")
            if len(_parts) >= 3:
                add(_parts[0].strip(), _parts[1].strip(), _parts[2].strip())


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
