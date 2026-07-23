#!/usr/bin/env python3
"""
One-time backfill: pull everything CURRENTLY INDEXED across all feeds (no time
window), score + rank it, and write a starting snapshot to monitoring/history/:

    backfill-<date>.csv    durable archive (open in Excel/Sheets, or grep)
    backfill-<date>.md     the ranked board (same format as the daily digest)
    backfill-<date>.html   the board as a standalone page

It also prints the board to the GitHub Actions job summary.

WHERE TO RUN IT (it needs to reach news.google.com / reddit.com):
  - GitHub Actions: .github/workflows/backfill.yml runs it for you (open internet).
  - Locally on any machine with open internet:  python3 monitoring/backfill.py
NOTE: it CANNOT run inside the Claude workspace — that network policy blocks the
feed hosts (same reason synergyhealth.org is blocked there).

LIMITS: RSS is forward-looking. Each feed only exposes its most recent items
(~up to 100; we keep up to BACKFILL_MAX_PER_FEED per feed), so this recovers what
is indexed *right now*, not deep historical mentions. Ongoing history accrues from
the daily digest going forward.

Stdlib only. Reuses digest.py (fetch/parse/render) and scoring.py.
"""

import os
import csv
import time

import digest
import scoring

MAX_PER_FEED = int(os.environ.get("BACKFILL_MAX_PER_FEED") or 25)
OUTDIR = os.environ.get("BACKFILL_OUTDIR") or os.path.join(digest.HERE, "history")
TITLE = "SHP Mention Board — Backfill snapshot"
WINDOW = "currently indexed across all feeds (one-time backfill)"


def collect_all():
    """Every item each feed currently exposes — no CUTOFF window — scored+ranked."""
    groups = digest.parse_opml(digest.OPML)
    mentions, failures, seen = [], [], set()
    total_feeds = 0
    for folder, feeds in groups:
        for ftitle, url in feeds:
            total_feeds += 1
            try:
                items = digest.parse_feed(digest.fetch(url))
            except Exception as e:  # noqa: BLE001
                failures.append((ftitle, str(e)[:140]))
                continue
            kept = 0
            for it in items:
                if kept >= MAX_PER_FEED:
                    break
                key = (it["link"] or it["title"]).strip().lower()
                if not key or key in seen:
                    continue
                seen.add(key)
                kept += 1
                m = {"folder": folder, "feed": ftitle, "title": it["title"],
                     "link": it["link"], "when": it["when"]}
                m.update(scoring.score(folder, ftitle, it["title"]))
                mentions.append(m)
            time.sleep(0.7)  # polite (Reddit rate-limits bursts)
    # rank: score desc, then most-recent first (undated sort last)
    mentions.sort(
        key=lambda m: (m["score"], m["when"].timestamp() if m["when"] else 0),
        reverse=True)
    return mentions, total_feeds, failures


def write_csv(path, mentions):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["score", "band", "line", "signal", "geo", "priority_geo",
                    "negative", "partnership", "route", "when_utc", "title",
                    "link", "feed", "folder"])
        for m in mentions:
            mods = m["mods"]
            w.writerow([
                m["score"], m["band"], m["line"], m["signal"],
                int(mods["geo"]), int(mods["geo_priority"]),
                int(mods["negative"]), int(mods["partnership"]), m["route"],
                m["when"].strftime("%Y-%m-%d %H:%M") if m["when"] else "",
                m["title"], m["link"], m["feed"], m["folder"],
            ])


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    mentions, total_feeds, failures = collect_all()
    stamp = digest.NOW.strftime("%Y-%m-%d")
    base = os.path.join(OUTDIR, f"backfill-{stamp}")

    write_csv(base + ".csv", mentions)
    md = digest.render_md(mentions, total_feeds, failures, title=TITLE, window_desc=WINDOW)
    with open(base + ".md", "w", encoding="utf-8") as f:
        f.write(md)
    html = digest.render_html(mentions, total_feeds, failures, title=TITLE, window_desc=WINDOW)
    with open(base + ".html", "w", encoding="utf-8") as f:
        f.write("<!doctype html><html><head><meta charset='utf-8'>"
                "<title>SHP Mention Backfill</title></head><body>" + html +
                "</body></html>")

    digest.write_summary(md)  # -> GitHub Actions job summary
    print(f"Backfill: {len(mentions)} mention(s) across {total_feeds} feeds")
    print(f"  wrote {base}.csv / .md / .html")
    if failures:
        print(f"  {len(failures)} feed(s) failed this run (transient — rerun to retry)")


if __name__ == "__main__":
    main()
