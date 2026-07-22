#!/usr/bin/env python3
"""Analyze a GSC "AI features" export (impressions-only view).

Usage:  python3 analyze_gsc_ai.py data/2026-07-21-ai-features [data/2026-07-21]
Second (optional) arg = matching classic-web export folder; used to compute the
AI share of total impressions over the same date window.

Google provides impressions only for this view — no clicks/CTR/position and no
query breakdown. Data for synergyhealth.org begins 2026-05-18.
"""
import csv, sys, datetime, urllib.parse
from collections import defaultdict

D = (sys.argv[1] if len(sys.argv) > 1 else "data/2026-07-21-ai-features").rstrip("/") + "/"
WEB = (sys.argv[2].rstrip("/") + "/") if len(sys.argv) > 2 else None

def load(f, keycol):
    with open(D + f, encoding="utf-8-sig") as fh:
        return [(r[keycol], int(r["Impressions"])) for r in csv.DictReader(fh)]

pages, chart = load("Pages.csv", "Top pages"), load("Chart.csv", "Date")
total = sum(v for _, v in chart)
print(f"Window: {chart[0][0]} -> {chart[-1][0]} ({len(chart)} days) | {total} AI impressions")

weeks = defaultdict(int)
for d, v in chart:
    dt = datetime.date.fromisoformat(d)
    weeks[(dt - datetime.timedelta(days=dt.weekday())).isoformat()] += v
print("\n=== WEEKLY TREND ===")
for w in sorted(weeks): print(f"  wk {w}: {weeks[w]:6d}")

if WEB:
    webc = {}
    with open(WEB + "Chart.csv", encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh): webc[r["Date"]] = int(r["Impressions"])
    win = sum(webc.get(d, 0) for d, _ in chart)
    print(f"\nSame-window web impressions: {win} -> AI share {total/max(win,1)*100:.1f}%")

c = load("Countries.csv", "Country"); ct = sum(v for _, v in c); us = dict(c).get("United States", 0)
print(f"\nCountries: US {us/max(ct,1)*100:.1f}% | non-US {(ct-us)} impr across {len(c)-1} countries")
print("  top non-US:", [(k, v) for k, v in c if k != "United States"][:6])

SPINE = ["spine","spinal","sciatic","stenosis","herniat","disc","fusion","laminectomy","discectomy",
         "kyphoplasty","vertebr","radiculopathy","spondylo","cervical","lumbar","neck","back",
         "thoracic","decompression","esi","acdf","acdr"]
BUCKETS = [("hand", ["hand","wrist","carpal","finger","dupuytren","thumb","ganglion","quervain"]),
           ("foot", ["foot","ankle","podiat","bunion","plantar","toe","achilles","heel"]),
           ("spine", SPINE),
           ("ortho", ["knee","hip","shoulder","elbow","rotator","joint","arthroplasty","orthoped",
                      "tka","contusion","fracture","arthritis","bursitis"]),
           ("pt", ["physical-therapy","lymphedema","therapy","rehab"])]
def cls(p):
    pl = p.lower()
    for name, terms in BUCKETS:
        if any(t in pl for t in terms): return name
    if "/providers/" in pl: return "provider"
    if "/locations/" in pl or "clinic" in pl: return "location"
    return "other"

agg, paths = defaultdict(int), []
for u, v in pages:
    p = urllib.parse.urlparse(u).path
    paths.append((p, v)); agg[cls(p)] += v
ptotal = sum(v for _, v in paths)
print(f"\n=== BUCKETS ({len(paths)} pages, {ptotal} impressions) ===")
for k, v in sorted(agg.items(), key=lambda x: -x[1]):
    print(f"  {k:10} {v:6d} ({v/ptotal*100:4.1f}%)")

print("\n=== TOP 30 PAGES ===")
for p, v in paths[:30]: print(f"  {v:6d}  {p}")

print("\n=== STRUCTURE SPLIT (new vs legacy) ===")
for pre in ["/conditions/", "/treatment/", "/conditions-we-treat/", "/specialties/"]:
    s = sum(v for p, v in paths if p.startswith(pre))
    print(f"  {pre:22} {s:6d}")

print("\n=== SPINE HUB CITATIONS ===")
for hub in ["stenosis","sciatica","herniated","radiculopathy","spondylolisthesis",
            "degenerative","acdf","cervical-fusion","neck-fracture","back-fracture"]:
    hits = [(p, v) for p, v in paths if hub in p.lower()]
    print(f"  {hub:18} {hits if hits else '— absent'}")
