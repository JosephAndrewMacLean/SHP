#!/usr/bin/env python3
"""Core Web Vitals checker — tests Cardinal's May 1 regression status.

Usage:
    PAGESPEED_API_KEY=<key> python3 scripts/cwv-check.py [--pages N]

Queries the PageSpeed Insights API (field/CrUX data + Lighthouse lab) for the
key pages Cardinal's audit tracked, and prints each against the June 2026 audit
baseline (field LCP 3.5s, CLS 0.11, Lighthouse mobile 28/100, 0 Good URLs).

Pass thresholds (Google): LCP <= 2.5s, CLS <= 0.10, INP <= 200ms.
Results feed audits/cardinal-recommendation-tracker.md — update it after runs.
"""
import os
import sys
import time

import requests

KEY = os.environ.get("PAGESPEED_API_KEY")
if not KEY:
    sys.exit("PAGESPEED_API_KEY is not set. Add it in the Claude Code environment "
             "settings (sessions started after the change see it), or prefix the "
             "command with PAGESPEED_API_KEY=<key>.")

PAGES = [
    ("https://synergyhealth.org/", "homepage"),
    ("https://synergyhealth.org/specialty/spine-neck-back", "spine hub"),
    ("https://synergyhealth.org/conditions-we-treat/hand-upper-extremity-conditions/carpal-tunnel-syndrome/",
     "carpal tunnel"),
    ("https://synergyhealth.org/treatment/total-knee-arthroplasty-tka/", "TKA"),
    ("https://synergyhealth.org/locations/sterling-heights/", "Sterling Heights"),
]

BASELINE = "Cardinal Jun 2026 baseline: field LCP 3.5s / CLS 0.11 (FAILING), lab 28/100, 0 Good URLs since May 13"
CA = "/root/.ccr/ca-bundle.crt"
verify = CA if os.path.exists(CA) else True

def fmt_ms(name, v):
    if v is None:
        return "n/a"
    return f"{v/1000:.2f}s" if "PAINT" in name or "LCP" in name else str(v)

def check(url, label):
    r = requests.get(
        "https://www.googleapis.com/pagespeedonline/v5/runPagespeed",
        params={"url": url, "strategy": "mobile", "category": "performance",
                "key": KEY},
        timeout=120, verify=verify)
    if r.status_code != 200:
        print(f"\n== {label}: HTTP {r.status_code} — {r.text[:200]}")
        return
    j = r.json()
    print(f"\n== {label} ({url})")
    for scope_name, scope in [("page field", j.get("loadingExperience", {})),
                              ("origin field", j.get("originLoadingExperience", {}))]:
        mets = scope.get("metrics") or {}
        if not mets:
            continue
        overall = scope.get("overall_category")
        parts = []
        for mk, short in [("LARGEST_CONTENTFUL_PAINT_MS", "LCP"),
                          ("CUMULATIVE_LAYOUT_SHIFT_SCORE", "CLS"),
                          ("INTERACTION_TO_NEXT_PAINT", "INP")]:
            m = mets.get(mk)
            if not m:
                continue
            val = m.get("percentile")
            if mk == "CUMULATIVE_LAYOUT_SHIFT_SCORE":
                shown = f"{val/100:.2f}"
            elif mk == "LARGEST_CONTENTFUL_PAINT_MS":
                shown = f"{val/1000:.2f}s"
            else:
                shown = f"{val}ms"
            parts.append(f"{short} p75={shown} [{m.get('category')}]")
        print(f"   {scope_name}: {overall} | " + " · ".join(parts))
        if scope_name == "page field":
            break  # page-level exists; skip origin duplicate
    lh = j.get("lighthouseResult", {})
    perf = (lh.get("categories", {}).get("performance") or {}).get("score")
    audits = lh.get("audits", {})
    lab = " · ".join(
        f"{k.split('-')[0]} {audits.get(k, {}).get('displayValue', '?')}"
        for k in ["largest-contentful-paint", "cumulative-layout-shift",
                  "total-blocking-time"])
    print(f"   lab: {round(perf*100) if perf is not None else '?'}/100 | {lab}")


if __name__ == "__main__":
    n = len(PAGES)
    if "--pages" in sys.argv:
        n = int(sys.argv[sys.argv.index("--pages") + 1])
    print(BASELINE)
    for url, label in PAGES[:n]:
        try:
            check(url, label)
        except Exception as e:
            print(f"\n== {label}: ERROR {str(e)[:160]}")
        time.sleep(1)
    print("\nVerdict guide: 'origin field' FAST/AVERAGE/SLOW is the sitewide CrUX "
          "state. If LCP p75 is still ~3.5s+ and category SLOW, the May 1 "
          "regression is still live — escalate with Cardinal/dev. Update "
          "audits/cardinal-recommendation-tracker.md either way.")
