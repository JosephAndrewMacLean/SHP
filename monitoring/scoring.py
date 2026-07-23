#!/usr/bin/env python3
"""
Inferred Patient-Value (IPV) scoring for monitored mentions.

Ranks each mention 0–100 by its *inferred* value to landing new patients, weighted
to SHP's confirmed priority (see brand/current-state.md):

  - SPINE and ORTHO patient acquisition = most valuable.
  - FOOT / HAND / PAIN value is realized mainly through PARTNERSHIPS / referrals,
    so those lines score lower at baseline but get a dedicated partnership boost.
  - Brand reputation and competitor intel are supporting axes; NEGATIVE brand
    sentiment escalates to PR regardless of line.

These scores are heuristic inferences from feed folder + mention text — a triage
aid, not ground truth. Tune the weights below; the model is intentionally simple
and transparent. Stdlib only.
"""

# --- weights (edit here to re-tune) -----------------------------------------
LINE_POINTS = {          # strategic patient-acquisition value of the service line
    "spine": 45,
    "ortho": 36,
    "brand": 30,         # brand-level: could convert any line
    "pain": 22,
    "foot": 18,
    "hand": 18,
    "general": 20,
    "competitor": 10,
}
SIGNAL_POINTS = {        # what KIND of mention it is
    "patient_demand": 35,     # someone seeking care / asking for a surgeon
    "provider_mention": 26,   # one of our providers named
    "brand_mention": 28,      # brand named / linked / reviewed
    "partnership": 24,        # referral-source / partnership opportunity
    "press": 18,              # earned media / authority
    "competitor_intel": 12,
    "ambient": 8,
}
GEO_BONUS = 8            # metro-Detroit / SE-Michigan geo present
GEO_PRIORITY_BONUS = 5  # Troy / Oakland / Southfield (the growth unlocks)
HELP_BONUS = 7          # explicit help-seeking ("?", "recommend", "anyone")
NEGATIVE_BONUS = 12     # negative brand sentiment -> urgency (PR)
FHP_PARTNERSHIP_BONUS = 10  # foot/hand/pain get their value from partnerships

P1, P2 = 70, 40         # priority band cutoffs

# --- keyword lexicons (word-boundary matched to avoid substring false hits) -
import re


def _rx(terms):
    return re.compile(r"\b(?:" + "|".join(re.escape(t) for t in terms) + r")\b", re.I)


_LINE_KW = [  # order = priority; first match wins on text inference
    ("spine", _rx(("spine", "spinal", "back surgery", "herniated", "disc", "discs",
                   "sciatica", "stenosis", "fusion", "scoliosis", "spondylosis",
                   "spondylolisthesis", "cervical", "neck surgery", "laminectomy",
                   "microdiscectomy", "radiculopathy", "pinched nerve", "myelopathy"))),
    ("ortho", _rx(("knee", "hip", "shoulder", "joint replacement", "arthroplasty",
                   "acl", "rotator", "meniscus", "sports medicine", "fracture",
                   "orthopedic", "orthopaedic", "total knee", "total hip", "labrum"))),
    ("foot", _rx(("foot", "ankle", "podiatry", "podiatrist", "podiatric", "bunion",
                  "heel", "plantar", "achilles", "toe", "hammertoe", "flatfoot"))),
    ("hand", _rx(("hand surgery", "wrist", "carpal", "thumb", "finger",
                  "trigger finger", "tendon release", "dupuytren"))),
    ("pain", _rx(("pain management", "epidural", "injection", "nerve block",
                  "radiofrequency", "rfa", "spinal cord stimulator"))),
]
_LINE_RANK = {"spine": 5, "ortho": 4, "pain": 3, "foot": 2, "hand": 2,
              "brand": 1, "general": 0, "competitor": 0}

# Note: bare "partner" is deliberately excluded — the brand is literally
# "Synergy Health Partners", so it would false-trigger on every brand mention.
_PARTNERSHIP_RX = _rx(("refer", "refers", "referral", "referrals", "referring",
                       "referred", "partnership", "partner with", "physical therapy",
                       "chiropractor", "chiropractic", "primary care", "pcp",
                       "urgent care", "workers comp", "workers' comp", "workman",
                       "attorney", "auto accident", "car accident", "no-fault",
                       "employer", "sponsor", "collaboration", "provider network"))
_HELP_RX = _rx(("recommend", "recommendation", "recommendations", "anyone",
                "looking for", "who is a good", "who's a good", "need a",
                "suggestion", "suggestions", "any good", "advice", "second opinion",
                "best spine", "best ortho", "best surgeon", "where should"))
_GEO_RX = _rx(("michigan", "detroit", "livonia", "troy", "sterling heights",
               "southfield", "rochester", "oakland", "novi", "farmington", "warren",
               "royal oak", "birmingham", "metro detroit", "macomb", "wayne county"))
_GEO_PRIORITY_RX = _rx(("troy", "oakland", "southfield"))
_NEG_RX = _rx(("worst", "terrible", "avoid", "rude", "waited", "long wait", "cancel",
               "canceled", "cancelled", "malpractice", "sue", "sued", "lawsuit",
               "complaint", "billing", "horrible", "bad experience", "never again",
               "unprofessional", "dismissive", "misdiagnosed", "misdiagnosis",
               "botched"))


def _line_from_text(t):
    for line, rx in _LINE_KW:
        if rx.search(t):
            return line
    return None


def classify(folder, feed_title):
    """Map (folder, feed_title) to a baseline (line, signal)."""
    f = (folder or "").lower()
    ft = (feed_title or "").lower()
    if "competitor" in f:
        return "competitor", "competitor_intel"
    if "brand mentions" in f or "google alerts" in f or "youtube" in f or "video" in f:
        return "brand", "brand_mention"
    if "spine discovery" in f:
        return "spine", "patient_demand"
    if "local subreddits" in f:
        return "ortho", "patient_demand"          # local recs skew ortho/spine
    if "condition subreddits" in f:
        return ("pain" if "chronicpain" in ft or "chronic pain" in ft else "spine"), "patient_demand"
    if "allied health" in f:
        return "general", "ambient"
    if "providers" in f and "reddit" in f:
        return (_line_from_text(ft) or "general"), "provider_mention"
    if "providers" in f:                          # provider news; line in folder name
        if "spine" in f:
            line = "spine"
        elif "pain" in f:
            line = "pain"
        elif "orthopedic" in f or "orthopaedic" in f or "sports" in f or "primary" in f:
            line = "ortho"
        elif "hand" in f:
            line = "hand"
        elif "foot" in f or "podiatry" in f:
            line = "foot"
        else:
            line = "general"
        return line, "provider_mention"
    return "general", "ambient"


def _refine(line, signal, title):
    t = (title or "").lower()
    mods = {"geo": False, "geo_priority": False, "help": False,
            "negative": False, "partnership": False}
    if signal != "competitor_intel":
        tl = _line_from_text(t)
        if tl and _LINE_RANK.get(tl, 0) > _LINE_RANK.get(line, 0):
            line = tl                              # upgrade toward priority lines
    mods["geo"] = bool(_GEO_RX.search(t))
    mods["geo_priority"] = bool(_GEO_PRIORITY_RX.search(t))
    mods["negative"] = bool(_NEG_RX.search(t))
    mods["partnership"] = bool(_PARTNERSHIP_RX.search(t))
    mods["help"] = ("?" in (title or "")) or bool(_HELP_RX.search(t))
    # reclassify signal: partnership first, then help-seeking wins (direct demand)
    if signal not in ("competitor_intel", "patient_demand") and mods["partnership"]:
        signal = "partnership"
    if signal in ("ambient", "brand_mention", "provider_mention") and mods["help"]:
        signal = "patient_demand"
    return line, signal, mods


_LINE_LABEL = {"spine": "Spine", "ortho": "Ortho", "pain": "Pain", "foot": "Foot",
               "hand": "Hand", "brand": "Brand", "general": "General",
               "competitor": "Competitor"}
_SIGNAL_LABEL = {"patient_demand": "patient demand", "provider_mention": "provider named",
                 "brand_mention": "brand named", "partnership": "partnership",
                 "press": "press/authority", "competitor_intel": "competitor intel",
                 "ambient": "ambient"}


def _route(line, signal, mods):
    if mods["negative"]:
        return "PR — reputation (urgent)"
    if signal == "patient_demand":
        return ("SEO/AEO + Content (answer intent); flag Paid"
                if line in ("spine", "ortho") else "Content / SEO")
    if signal == "partnership":
        return "Physician Liaison / PR (referral)"
    if signal in ("brand_mention", "provider_mention"):
        return "PR + Content (testimonial w/ consent)"
    if signal == "press":
        return "PR — amplify / authority"
    if signal == "competitor_intel":
        return "Marketing Director — intel"
    return "Monitor"


def score(folder, feed_title, title):
    """Return a dict: score, band, line, signal, route, why, mods."""
    line, signal = classify(folder, feed_title)
    line, signal, mods = _refine(line, signal, title)
    pts = LINE_POINTS.get(line, 20) + SIGNAL_POINTS.get(signal, 8)
    if mods["geo"]:
        pts += GEO_BONUS
    if mods["geo_priority"]:
        pts += GEO_PRIORITY_BONUS
    if mods["help"]:
        pts += HELP_BONUS
    if mods["negative"]:
        pts += NEGATIVE_BONUS
    if line in ("foot", "hand", "pain") and mods["partnership"]:
        pts += FHP_PARTNERSHIP_BONUS
    pts = max(0, min(100, pts))
    band = "P1" if pts >= P1 else ("P2" if pts >= P2 else "P3")
    tags = [_LINE_LABEL.get(line, line), _SIGNAL_LABEL.get(signal, signal)]
    if mods["geo_priority"]:
        tags.append("priority-geo")
    elif mods["geo"]:
        tags.append("metro-Detroit")
    if mods["negative"]:
        tags.append("⚠ negative")
    return {
        "score": pts, "band": band, "line": line, "signal": signal,
        "route": _route(line, signal, mods), "why": " · ".join(tags), "mods": mods,
    }


# --- self-test --------------------------------------------------------------
if __name__ == "__main__":
    cases = [
        ("Tier 2 · Metro Detroit spine discovery — Reddit", "Reddit · spine surgeon Michigan",
         "Anyone recommend a good spine surgeon in Troy or Oakland County?"),
        ("Providers · Spine — News/Web", "Google News · Joseph Maslak",
         "Dr. Maslak performs minimally invasive spinal fusion at Livonia clinic"),
        ("Tier 1 · Brand mentions — Reddit", "Reddit · Synergy Health Partners",
         "Terrible billing experience at Synergy Health Partners, waited months"),
        ("Providers · Foot & ankle (podiatry) — News/Web", "Google News · Jeffrey Klein",
         "Podiatry group seeks referral partnership with Detroit workers' comp clinics"),
        ("Providers · Foot & ankle (podiatry) — News/Web", "Google News · Kevin Sorensen",
         "New bunion treatment option discussed"),
        ("Tier 3 · Competitor intel", "Google News · Detroit Bone & Joint",
         "Detroit Bone & Joint opens new Troy orthopedic office"),
        ("Providers · Hand & wrist — News/Web", "Google News · Kyle Bohm",
         "Michigan's only percutaneous carpal tunnel release now offered"),
    ]
    for folder, ft, title in sorted(cases, key=lambda c: -score(*c)["score"]):
        r = score(folder, ft, title)
        print(f"{r['score']:3d} [{r['band']}] {r['why']:38s} | {r['route']:38s} | {title[:60]}")
