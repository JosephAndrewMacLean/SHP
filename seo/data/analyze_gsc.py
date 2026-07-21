#!/usr/bin/env python3
"""Analyze a synergyhealth.org GSC performance export (the monthly loop).

Usage:  python3 analyze_gsc.py data/2026-07-21
Expects the standard GSC "Performance on Search" export CSVs in that folder:
Queries.csv, Pages.csv, Chart.csv, Devices.csv (Filters.csv documents the scope).

Outputs the standard cuts used by seo/gsc-analysis-*.md:
intent split, service-line split, spine deep-dive, striking distance, page quick
wins vs. CTR benchmark, cannibalization sets, city demand, revision-gap check,
monthly trend. Compare month over month; log conclusions in a dated analysis file.
"""
import csv, sys, urllib.parse
from collections import defaultdict

D = (sys.argv[1] if len(sys.argv) > 1 else "data/2026-07-21").rstrip("/") + "/"

def pct(s): return float(s.replace("%", "")) / 100.0

def load(f, keycol):
    with open(D + f, encoding="utf-8-sig") as fh:
        return [{"key": r[keycol], "clicks": int(r["Clicks"]), "impr": int(r["Impressions"]),
                 "ctr": pct(r["CTR"]), "pos": float(r["Position"])} for r in csv.DictReader(fh)]

queries, pages = load("Queries.csv", "Top queries"), load("Pages.csv", "Top pages")

BRAND = ["synergy", "mendelson", "kornblum", "shp "]
PROVIDERS = ["bhullar", "mccarty", "maslak", "varghese", "salar", "munk", "zamorano", "oddo",
             "kassa", "singh", "kyle", "trotter", "krebs", "buse", "sherman", "silverman",
             "fram", "verner", "faraj", "haidar", "khalil", "shammas", "knesek", "guettler",
             "milia", "mehling", "sikorski", "bohm", "abood", "kevin lee", "dr lee", "dr. lee"]
SPINE = ["spine", "spinal", "back pain", "neck pain", "sciatic", "stenosis", "herniat",
         "bulging disc", "slipped disc", "disc ", " disc", "disk ", "fusion", "laminectomy",
         "discectomy", "kyphoplasty", "vertebr", "radiculopathy", "spondylo", "scoliosis",
         "cervical", "lumbar", "thoracic", "pinched nerve", "myelopathy", "foramin",
         "decompression", "si joint", "sacroiliac", "coccyx", "tailbone", "whiplash",
         "low back", "lower back", "neck ", " neck", "back surgery", "back doctor",
         "back specialist", "acdf", "acdr"]
HAND = ["hand ", " hand", "wrist", "carpal", "trigger finger", "dupuytren", "cubital",
        "finger", "thumb", "ganglion"]
FOOT = ["foot", "ankle", "podiat", "bunion", "plantar", "hammertoe", "achilles", "heel",
        "toe ", " toe", "toenail", "neuroma", "flat feet"]
ORTHO = ["knee", "hip", "shoulder", "elbow", "rotator", "meniscus", "acl", "mcl", "labrum",
         "labral", "joint replacement", "arthroplasty", "orthoped", "orthopaed", "sports med",
         "fracture", "arthritis", "bursitis", "tendonitis", "tendinitis", "frozen shoulder",
         "dislocat", "cartilage", "osteo", "tka"]
PAIN = ["pain management", "pain clinic", "pain doctor", "pain specialist", "injection",
        "nerve block", "epidural", "radiofrequency", "ablation", "pain center", "esi"]
PT = ["physical therapy", "physical therapist", "physiotherap", "rehab", "lymphedema", "lymphatic"]
IMG = ["mri", "x-ray", "xray", "imaging", "ct scan", "radiolog"]
CITIES = ["livonia", "sterling heights", "southfield", "troy", "rochester", "clawson", "warren",
          "madison heights", "royal oak", "novi", "farmington", "westland", "canton", "dearborn",
          "detroit", "shelby", "macomb", "utica", "clinton township", "roseville", "ferndale",
          "oak park", "redford", "garden city", "plymouth", "northville", "waterford", "pontiac",
          "auburn hills", "west bloomfield", "port huron", "michigan", "near me"]
REVISION = ["failed back", "revision", "second opinion", "adjacent segment", "hardware",
            "reherniat", "recurrent", "post laminectomy", "fbss", "failed fusion", "scar tissue"]

def has(t, terms): return any(x in t for x in terms)
def intent(q):
    return "branded" if has(q, BRAND) else "provider" if has(q, PROVIDERS) else "nonbranded"
def line(q):
    for name, terms in (("hand", HAND), ("foot", FOOT), ("spine", SPINE), ("pain", PAIN),
                        ("pt", PT), ("imaging", IMG), ("ortho", ORTHO)):
        if has(q, terms): return name
    return "other"
def bench(pos):
    for p, c in ((1,.28),(2,.15),(3,.10),(4,.07),(5,.055),(6,.045),(7,.035),(8,.03),(9,.025),(10,.022)):
        if pos <= p + 0.5: return c
    return .015 if pos <= 15 else .010 if pos <= 20 else .005

def show(rows, n=25, label=""):
    if label: print(f"\n=== {label} ===")
    for q in rows[:n]:
        print(f"  {q['key'][:60]:60} | {q['clicks']:5d} c | {q['impr']:7d} i | "
              f"CTR {q['ctr']*100:5.2f}% | pos {q['pos']:5.1f}")

def table(agg, tc, ti):
    for k, a in sorted(agg.items(), key=lambda x: -x[1]["impr"]):
        print(f"  {k:>10}: {a['n']:4d} q | {a['clicks']:6d} c ({a['clicks']/tc*100:4.1f}%) | "
              f"{a['impr']:8d} i ({a['impr']/ti*100:4.1f}%) | CTR {a['clicks']/max(a['impr'],1)*100:5.2f}% | "
              f"pos {a['posw']/max(a['impr'],1):5.1f}")

def aggregate(rows, keyfn):
    agg = defaultdict(lambda: {"clicks":0,"impr":0,"n":0,"posw":0.0})
    for q in rows:
        a = agg[keyfn(q["key"])]
        a["clicks"] += q["clicks"]; a["impr"] += q["impr"]; a["n"] += 1; a["posw"] += q["pos"]*q["impr"]
    return agg

print("=== INTENT SPLIT ===")
table(aggregate(queries, intent), sum(q["clicks"] for q in queries), sum(q["impr"] for q in queries))

nb = [q for q in queries if intent(q["key"]) == "nonbranded"]
print("\n=== SERVICE LINE (non-branded) ===")
table(aggregate(nb, line), max(sum(q["clicks"] for q in nb),1), max(sum(q["impr"] for q in nb),1))

spine = sorted([q for q in nb if line(q["key"]) == "spine"], key=lambda x: -x["impr"])
show(spine, 40, "SPINE NON-BRANDED, TOP 40 BY IMPRESSIONS")
show(sorted([q for q in spine if 8 <= q["pos"] <= 20 and q["impr"] >= 100],
            key=lambda x: -x["impr"]), 25, "SPINE STRIKING DISTANCE (pos 8-20, impr>=100)")

rev = [q for q in queries if has(q["key"], REVISION)]
print(f"\n=== REVISION/FAILED-BACK/SECOND-OPINION QUERIES: {len(rev)} ===")
show(sorted(rev, key=lambda x: -x["impr"]))

locq = sorted([q for q in nb if has(q["key"], CITIES)], key=lambda x: -x["impr"])
show(locq, 25, f"LOCATION-MODIFIED NON-BRANDED ({len(locq)} queries)")
city = defaultdict(lambda: [0,0])
for q in locq:
    for c in CITIES:
        if c in q["key"]: city[c][0] += q["impr"]; city[c][1] += q["clicks"]
print("\n=== CITY DEMAND ===")
for c,(i,cl) in sorted(city.items(), key=lambda x: -x[1][0])[:20]:
    print(f"  {c:18} | {cl:5d} c | {i:7d} i")

pagg = defaultdict(lambda: {"clicks":0,"impr":0,"posw":0.0})
for p in pages:
    a = pagg[urllib.parse.urlparse(p["key"]).path]
    a["clicks"] += p["clicks"]; a["impr"] += p["impr"]; a["posw"] += p["pos"]*p["impr"]

print(f"\n=== PAGE QUICK WINS (impr>=20k, CTR below benchmark) — {len(pages)} URLs, {len(pagg)} paths ===")
qw = []
for path, a in pagg.items():
    pos, ctr = a["posw"]/max(a["impr"],1), a["clicks"]/max(a["impr"],1)
    if a["impr"] >= 20000 and ctr < bench(pos):
        qw.append((path, a["clicks"], a["impr"], ctr, pos, a["impr"]*(bench(pos)-ctr)))
for path, c, i, ctr, pos, g in sorted(qw, key=lambda x: -x[5])[:25]:
    print(f"  {path[:60]:60} | {c:5d} c | {i:7d} i | CTR {ctr*100:4.2f}% | pos {pos:5.1f} | gap +{g:.0f}")

SPINE_PATH = ["spine", "spinal", "sciatic", "stenosis", "herniat", "disc", "fusion",
              "laminectomy", "discectomy", "kyphoplasty", "vertebr", "radiculopathy",
              "spondylo", "cervical", "lumbar", "neck-fracture", "back-fracture", "decompression"]
sp = sorted([(p, a) for p, a in pagg.items() if has(p.lower(), SPINE_PATH)], key=lambda x: -x[1]["impr"])
print(f"\n=== SPINE PAGES ({len(sp)} paths) ===")
for p, a in sp[:30]:
    print(f"  {p[:64]:64} | {a['clicks']:5d} c | {a['impr']:7d} i | pos {a['posw']/max(a['impr'],1):5.1f}")

print("\n=== MONTHLY TREND ===")
months = defaultdict(lambda: [0,0])
with open(D + "Chart.csv", encoding="utf-8-sig") as fh:
    for r in csv.DictReader(fh):
        months[r["Date"][:7]][0] += int(r["Clicks"]); months[r["Date"][:7]][1] += int(r["Impressions"])
for m in sorted(months):
    c, i = months[m]
    print(f"  {m}: {c:5d} c | {i:8d} i | CTR {c/max(i,1)*100:4.2f}%")
