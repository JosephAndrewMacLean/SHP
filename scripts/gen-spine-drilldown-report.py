#!/usr/bin/env python3
"""Generate the spine drill-down report HTML from report_data.json."""
import json, html

D = json.load(open("report_data.json"))

# Scope: Providers = spine SURGEONS only (roster: Varghese, Salar, Maslak, McCarty,
# Zamorano, Munk; legacy surgeon URLs Kornblum/Fiani/Phillips kept for history).
SURGEONS = ("varghese", "salar", "maslak", "mccarty", "zamorano", "munk",
            "kornblum", "fiani", "phillips")
_prov = D["types"]["Providers"]
_excluded = [p for p in _prov["pages"] if not any(n in p["path"] for n in SURGEONS)]
EXC_C4 = sum(p["c4"] for p in _excluded); EXC_I4 = sum(p["i4"] for p in _excluded)
EXC_N = len(_excluded)
_prov["pages"] = [p for p in _prov["pages"] if any(n in p["path"] for n in SURGEONS)]
for k in ("c4", "i4", "cp", "ip", "c26", "i26"):
    _prov[k] = sum(p[k[0] == "c" and k or k] if False else p[k] for p in _prov["pages"])
_prov["weekly"] = [[sum(p["spark_c"][w] for p in _prov["pages"]),
                   sum(p["spark"][w] for p in _prov["pages"])] for w in range(26)]

WEEKS = D["weeks"]                      # 26 labels, "Feb 9" .. "Aug 3"
TYPES = ["Providers", "Conditions", "Treatments", "Specialty", "Other"]
TYPE_LABEL = {
    "Providers": "Spine surgeon pages", "Conditions": "Condition pages",
    "Treatments": "Treatment pages", "Specialty": "Specialty pages",
    "Other": "Other spine URLs",
}
TYPE_SUB = {
    "Providers": "Profile pages for the spine surgical team — Varghese, Salar, Maslak, McCarty, Zamorano (neurosurgery), Munk. Pain, chiro, PT & directory pages excluded.",
    "Conditions": "Spine, neck & back conditions — /conditions/ and legacy /conditions-we-treat/",
    "Treatments": "Spine procedures & injections — /treatment/ (launched in search Apr 22)",
    "Specialty": "Spine service-line landings & procedure library — /specialty/ and /specialties/",
    "Other": "Legacy blog & pre-rebrand URLs that match spine topics",
}
SERIES_VAR = {"Providers": "--s-prov", "Conditions": "--s-cond", "Treatments": "--s-trt",
              "Specialty": "--s-spec", "Other": "--s-oth"}

def esc(s): return html.escape(str(s), quote=True)
def fmtn(n):
    if n >= 100000: return f"{n/1000:.0f}K"
    if n >= 10000: return f"{n/1000:.1f}K"
    return f"{n:,}"
def ctr(c, i): return f"{c/i*100:.2f}%" if i else "—"
def delta_pct(cur, prev):
    if prev == 0: return ("new", "+") if cur > 0 else ("—", "")
    d = (cur - prev) / prev * 100
    if abs(d) < 0.5: return ("±0%", "")
    return (f"{abs(d):.0f}%", "+" if d > 0 else "−")

# ---------- totals ----------
tot = {k: sum(D["types"][g][k] for g in TYPES) for k in ("c4", "i4", "cp", "ip")}
live_pages = sum(1 for g in TYPES for p in D["types"][g]["pages"] if p.get("crawl") == "200")
cons_pages = sum(1 for g in TYPES for p in D["types"][g]["pages"] if p.get("crawl") in ("301","302","308"))
dead_pages = sum(1 for g in TYPES for p in D["types"][g]["pages"] if p.get("crawl") == "404")
ctr4 = tot["c4"] / tot["i4"] * 100
ctrp = tot["cp"] / tot["ip"] * 100

# ---------- main chart ----------
CW, CH, PL, PR, PT, PB = 960, 320, 46, 136, 18, 30
ymax_raw = max(D["types"][g]["weekly"][w][1] for g in TYPES for w in range(26))
ymax = (int(ymax_raw / 3000) + 1) * 3000
def X(w): return PL + w * (CW - PL - PR) / 25
def Y(v): return PT + (CH - PT - PB) * (1 - v / ymax)

chart_paths, endpoints = [], []
for g in TYPES:
    pts = [(X(w), Y(D["types"][g]["weekly"][w][1])) for w in range(26)]
    dpath = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    chart_paths.append(
        f'<path class="ln" style="stroke:var({SERIES_VAR[g]})" d="{dpath}"/>'
        f'<circle class="end" style="fill:var({SERIES_VAR[g]})" cx="{pts[-1][0]:.1f}" cy="{pts[-1][1]:.1f}" r="3.5"/>')
    endpoints.append([pts[-1][1], g, D["types"][g]["weekly"][25][1]])
# nudge end labels apart (14px min gap)
endpoints.sort()
for i in range(1, len(endpoints)):
    if endpoints[i][0] - endpoints[i-1][0] < 15: endpoints[i][0] = endpoints[i-1][0] + 15
def kfmt(n): return f"{n/1000:.1f}K" if n >= 1000 else f"{n:,}"
true_y = {g: Y(D["types"][g]["weekly"][25][1]) for g in TYPES}
end_labels = "".join(
    (f'<path class="leader" style="stroke:var({SERIES_VAR[g]})" d="M{X(25)+5:.1f},{true_y[g]:.1f} L{CW-PR+6:.1f},{y:.1f}"/>'
     if abs(y - true_y[g]) > 6 else "") +
    f'<text class="endlbl" x="{CW-PR+10}" y="{y+4:.1f}"><tspan style="fill:var({SERIES_VAR[g]})">\u2014</tspan> {g} <tspan class="mut2">{kfmt(v)}</tspan></text>'
    for y, g, v in endpoints)
gridlines = "".join(
    f'<line class="grid" x1="{PL}" y1="{Y(v):.1f}" x2="{CW-PR}" y2="{Y(v):.1f}"/>'
    f'<text class="tick" x="{PL-8}" y="{Y(v)+4:.1f}">{(str(v) if v == 0 else f"{v//1000}K")}</text>'
    for v in range(0, ymax + 1, 3000))
xticks = "".join(
    f'<text class="tick tx" x="{X(w):.1f}" y="{CH-8}">{WEEKS[w]}</text>' for w in range(0, 26, 4))
mig_x = X(10.3)
annotation = (f'<line class="anno" x1="{mig_x:.1f}" y1="{PT}" x2="{mig_x:.1f}" y2="{CH-PB}"/>'
              f'<text class="annot" x="{mig_x+6:.1f}" y="{PT+12}">Apr 22 — /treatment/ URLs first appear in search</text>')

chart_data_js = json.dumps({
    "weeks": WEEKS, "ymax": ymax,
    "series": {g: [D["types"][g]["weekly"][w][1] for w in range(26)] for g in TYPES},
    "clicks": {g: [D["types"][g]["weekly"][w][0] for w in range(26)] for g in TYPES},
    "geom": {"cw": CW, "pl": PL, "pr": PR},
})

# weekly table (a11y / relief rule)
wk_rows = "".join(
    "<tr><th scope=\"row\">" + esc(WEEKS[w]) + "</th>" +
    "".join(f"<td>{D['types'][g]['weekly'][w][1]:,}<span class='mut2'> / {D['types'][g]['weekly'][w][0]}</span></td>" for g in TYPES) +
    "</tr>" for w in range(26))

# ---------- sparkline ----------
def spark(vals, var):
    mx = max(vals) or 1
    w, h = 120, 26
    pts = [(i * w / 25, h - 3 - (h - 6) * v / mx) for i, v in enumerate(vals)]
    line = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    area = line + f" L{w},{h} L0,{h} Z"
    peak_i = vals.index(max(vals))
    tip = f"Weekly impressions, Feb 9 – Aug 9. Peak {max(vals):,} (wk of {WEEKS[peak_i]})"
    return (f'<svg class="spark" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(tip)}">'
            f'<title>{esc(tip)}</title>'
            f'<path class="sp-a" style="fill:var({var})" d="{area}"/>'
            f'<path class="sp-l" style="stroke:var({var})" d="{line}"/>'
            f'<circle style="fill:var({var})" cx="{pts[-1][0]:.1f}" cy="{pts[-1][1]:.1f}" r="2.2"/></svg>')

# ---------- page rows ----------
def page_row(p, var):
    name, path = esc(p["name"]), esc(p["path"])
    status_chip = ""
    if p.get("crawl") == "404":
        status_chip = '<span class="chip chip-404">✕ 404</span>'
    redirect_note = ""
    if p.get("pending_301"):
        redirect_note = f'<div class="rnote">301 pending → <code>{esc(p["pending_301"])}</code></div>'
    dval, dsign = delta_pct(p["i4"], p["ip"])
    if dsign == "+": dcls, arrow = "up", "▲"
    elif dsign == "−": dcls, arrow = "dn", "▼"
    else: dcls, arrow = "", ""
    return f"""<tr>
<td class="c-page"><div class="pname">{name} {status_chip}</div><code class="ppath">{path}</code>{redirect_note}</td>
<td class="c-spark">{spark(p["spark"], var)}</td>
<td class="num">{p["c4"]:,}</td>
<td class="num">{p["i4"]:,}</td>
<td class="num">{ctr(p["c4"], p["i4"])}</td>
<td class="num c-delta"><span class="d {dcls}">{arrow} {dval}</span></td>
</tr>"""

def section(g, open_=False):
    n = D["types"][g]
    has_act = lambda p: p["i26"] > 0 or p["c26"] > 0
    active = [p for p in n["pages"] if has_act(p) and p.get("crawl") in ("200", "404")]
    consolidated = [p for p in n["pages"] if p.get("crawl") in ("301", "302", "308")]
    silent = [p for p in n["pages"] if not has_act(p) and p.get("crawl") == "200"]
    dval, dsign = delta_pct(n["i4"], n["ip"])
    darrow = "▲" if dsign == "+" else ("▼" if dsign == "−" else "")
    rows = "".join(page_row(p, SERIES_VAR[g]) for p in active)
    exc_html = ""
    if g == "Providers" and EXC_N:
        exc_html = (f'<p class="consnote">Scope note: {EXC_N} other spine-bench provider pages (interventional pain, '
                    f'chiropractic, PT and directory pages) are excluded from this report at the requested surgeon-only scope — '
                    f'they earned {EXC_C4:,} clicks / {EXC_I4:,} impressions in the last 4 weeks.</p>')
    cons_html = ""
    if consolidated:
        ci = sum(p["i26"] for p in consolidated); ccl = sum(p["c26"] for p in consolidated)
        cons_html = (f'<p class="consnote">{len(consolidated)} legacy URLs in this group have been consolidated via 301 redirect '
                     f'(verified by crawl, Aug 11) and are no longer listed. Their historical activity '
                     f'({ccl:,} clicks / {ci:,} impressions over 26 wk) remains in the totals above and in the chart.</p>')
    silent_html = ""
    if silent:
        names = " · ".join(esc(p["name"]) for p in sorted(silent, key=lambda x: x["name"]))
        silent_html = (f'<details class="silent"><summary>{len(silent)} live spine pages with zero Google '
                       f'impressions in all 26 weeks</summary><p class="silentlist">{names}</p></details>')
    return f"""<details class="sec" {"open" if open_ else ""}>
<summary>
  <span class="dot" style="background:var({SERIES_VAR[g]})"></span>
  <span class="sec-name">{TYPE_LABEL[g]}<span class="sec-sub">{esc(TYPE_SUB[g])}</span></span>
  <span class="sec-stats">
    <span class="ss"><b>{n["c4"]:,}</b> clicks</span>
    <span class="ss"><b>{fmtn(n["i4"])}</b> impressions</span>
    <span class="ss"><b>{ctr(n["c4"], n["i4"])}</b> CTR</span>
    <span class="ss mut">{darrow} {dval} impr. vs prior 4 wk</span>
    <span class="ss mut">{len(active) + len(silent)} pages</span>
  </span>
  <span class="tw">▸</span>
</summary>
<div class="secbody">
<div class="tscroll"><table class="pt">
<thead><tr><th>Page</th><th>26-week trend</th><th class="num">Clicks</th><th class="num">Impressions</th><th class="num">CTR</th><th class="num">Δ impr.</th></tr></thead>
<tbody>{rows}</tbody>
</table></div>
{exc_html}
{cons_html}
{silent_html}
</div>
</details>"""

sections = "".join(section(g, open_=(g == "Providers")) for g in TYPES)

dvalT, dsignT = delta_pct(tot["c4"], tot["cp"])
dvalI, dsignI = delta_pct(tot["i4"], tot["ip"])
def tile_delta(val, sign):
    if sign == "+": return f'<span class="d up">▲ {val}</span>'
    if sign == "−": return f'<span class="d dn">▼ {val}</span>'
    return f'<span class="d">{val}</span>'

page = f"""<title>Spine Pages — Organic Search Drill-Down</title>
<style>
:root {{
  color-scheme: light;
  --page:#f4f7f8; --surface:#fcfdfd; --surface2:#eef2f4; --ink:#101a20; --ink2:#46545d;
  --muted:#64747e; --grid:#e2e8eb; --hair:#d5dde1; --accent:#2a78d6;
  --s-prov:#2a78d6; --s-cond:#eb6834; --s-trt:#1baf7a; --s-spec:#eda100; --s-oth:#e87ba4;
  --crit:#d03b3b; --good:#006300; --chip404:#fbeaea; --tipbg:#101a20; --tipink:#f2f6f8;
  --k-prov:#3987e5; --k-cond:#d95926; --k-trt:#199e70; --k-spec:#c98500; --k-oth:#d55181;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    color-scheme: dark;
    --page:#0c1114; --surface:#161c20; --surface2:#1d2530; --ink:#edf3f5; --ink2:#b4c1c8;
    --muted:#7f8d95; --grid:#242e34; --hair:#303c43; --accent:#3987e5;
    --s-prov:#3987e5; --s-cond:#d95926; --s-trt:#199e70; --s-spec:#c98500; --s-oth:#d55181;
    --crit:#e66767; --good:#0ca30c; --chip404:#3a2020; --tipbg:#edf3f5; --tipink:#101a20;
    --k-prov:#2a78d6; --k-cond:#eb6834; --k-trt:#1baf7a; --k-spec:#eda100; --k-oth:#e87ba4;
  }}
}}
:root[data-theme="dark"] {{
  color-scheme: dark;
  --page:#0c1114; --surface:#161c20; --surface2:#1d2530; --ink:#edf3f5; --ink2:#b4c1c8;
  --muted:#7f8d95; --grid:#242e34; --hair:#303c43; --accent:#3987e5;
  --s-prov:#3987e5; --s-cond:#d95926; --s-trt:#199e70; --s-spec:#c98500; --s-oth:#d55181;
  --crit:#e66767; --good:#0ca30c; --chip404:#3a2020; --tipbg:#edf3f5; --tipink:#101a20;
  --k-prov:#2a78d6; --k-cond:#eb6834; --k-trt:#1baf7a; --k-spec:#eda100; --k-oth:#e87ba4;
}}
* {{ box-sizing:border-box; }}
body {{ background:var(--page); color:var(--ink); margin:0;
  font:15px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif; }}
.wrap {{ max-width:1060px; margin:0 auto; padding:34px 26px 64px; }}
code {{ font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-size:.86em; }}
a {{ color:var(--accent); }}

.eyebrow {{ font-size:11.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); font-weight:600; }}
h1 {{ font-size:29px; line-height:1.2; margin:6px 0 4px; letter-spacing:-.015em; text-wrap:balance; }}
.meta {{ color:var(--ink2); font-size:13.5px; margin:0 0 26px; }}
.meta b {{ color:var(--ink); font-weight:600; }}

.tiles {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:12px; margin-bottom:14px; }}
.tile {{ background:var(--surface); border:1px solid var(--hair); border-radius:8px; padding:14px 16px 12px; }}
.tile .lab {{ font-size:11.5px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); font-weight:600; }}
.tile .val {{ font-size:27px; font-weight:650; letter-spacing:-.01em; margin:2px 0 0; }}
.tile .sub {{ font-size:12.5px; color:var(--ink2); }}
.d {{ font-variant-numeric:tabular-nums; font-size:12.5px; font-weight:600; color:var(--ink2); }}
.d.up {{ color:var(--good); }} .d.dn {{ color:var(--crit); }}

.callout {{ background:var(--surface2); border-left:3px solid var(--accent); border-radius:0 8px 8px 0;
  padding:11px 16px; font-size:13.8px; color:var(--ink2); margin:0 0 26px; }}
.callout b {{ color:var(--ink); }}

.card {{ background:var(--surface); border:1px solid var(--hair); border-radius:10px; padding:20px 22px 14px; margin-bottom:26px; }}
.card h2 {{ font-size:16px; margin:0 0 2px; }}
.card .sub {{ color:var(--muted); font-size:13px; margin:0 0 12px; }}
.chartbox {{ position:relative; }}
.chartbox svg {{ width:100%; height:auto; display:block; }}
.ln {{ fill:none; stroke-width:2; }}
.grid {{ stroke:var(--grid); stroke-width:1; }}
.anno {{ stroke:var(--muted); stroke-width:1; stroke-dasharray:4 4; }}
.leader {{ stroke-width:1; opacity:.55; fill:none; }}
.annot {{ font-size:11px; fill:var(--muted); }}
.tick {{ font-size:11px; fill:var(--muted); text-anchor:end; font-variant-numeric:tabular-nums; }}
.tick.tx {{ text-anchor:middle; }}
.endlbl {{ font-size:11.5px; fill:var(--ink2); font-weight:600; }}
.endlbl .mut2 {{ font-weight:500; }}
.mut2 {{ fill:var(--muted); color:var(--muted); }}
.cross {{ stroke:var(--muted); stroke-width:1; stroke-dasharray:2 3; opacity:0; }}
.tip {{ position:absolute; pointer-events:none; background:var(--tipbg); color:var(--tipink);
  border-radius:7px; padding:8px 11px; font-size:12px; line-height:1.5; opacity:0; transition:opacity .12s;
  box-shadow:0 4px 14px rgba(0,0,0,.18); min-width:180px; z-index:5; }}
.tip .tw-lab {{ font-weight:650; margin-bottom:2px; }}
.tip .row {{ display:flex; justify-content:space-between; gap:14px; align-items:center; }}
.tip .key {{ display:inline-block; width:12px; height:3px; border-radius:2px; margin-right:6px; vertical-align:2px; }}
.tip .row .val {{ font-weight:650; font-variant-numeric:tabular-nums; }}
.tip .row .nm {{ opacity:.8; }}
@media (prefers-reduced-motion: reduce) {{ .tip {{ transition:none; }} }}

details.tblv {{ margin-top:8px; border-top:1px solid var(--grid); padding-top:8px; }}
details.tblv summary, details.silent summary {{ cursor:pointer; color:var(--ink2); font-size:13px; }}
details.tblv table {{ border-collapse:collapse; font-size:12.5px; margin-top:8px; font-variant-numeric:tabular-nums; }}
details.tblv th, details.tblv td {{ padding:3px 10px; text-align:right; border-bottom:1px solid var(--grid); }}
details.tblv th[scope=row] {{ text-align:left; font-weight:500; color:var(--ink2); }}

.sec {{ background:var(--surface); border:1px solid var(--hair); border-radius:10px; margin-bottom:14px; }}
.sec summary {{ list-style:none; display:flex; align-items:center; gap:12px; padding:15px 18px; cursor:pointer; flex-wrap:wrap; }}
.sec summary::-webkit-details-marker {{ display:none; }}
.sec summary:focus-visible {{ outline:2px solid var(--accent); outline-offset:2px; border-radius:10px; }}
.dot {{ width:11px; height:11px; border-radius:3px; flex:none; }}
.sec-name {{ font-weight:650; font-size:15.5px; display:flex; flex-direction:column; min-width:210px; }}
.sec-sub {{ font-weight:400; font-size:12px; color:var(--muted); max-width:420px; }}
.sec-stats {{ display:flex; gap:18px; margin-left:auto; align-items:baseline; flex-wrap:wrap; }}
.ss {{ font-size:13px; color:var(--ink2); white-space:nowrap; }}
.ss b {{ font-size:15px; color:var(--ink); font-variant-numeric:tabular-nums; }}
.ss.mut {{ color:var(--muted); font-size:12.5px; }}
.tw {{ color:var(--muted); transition:transform .15s; }}
.sec[open] .tw {{ transform:rotate(90deg); }}
@media (prefers-reduced-motion: reduce) {{ .tw {{ transition:none; }} }}
.secbody {{ padding:0 18px 14px; }}
.tscroll {{ overflow-x:auto; }}
table.pt {{ width:100%; border-collapse:collapse; font-size:13.5px; min-width:680px; }}
table.pt th {{ text-align:left; font-size:11px; letter-spacing:.07em; text-transform:uppercase;
  color:var(--muted); font-weight:600; padding:8px 10px; border-bottom:1px solid var(--hair); }}
table.pt td {{ padding:9px 10px; border-bottom:1px solid var(--grid); vertical-align:middle; }}
table.pt tbody tr:last-child td {{ border-bottom:none; }}
th.num, td.num {{ text-align:right; font-variant-numeric:tabular-nums; }}
.pname {{ font-weight:600; }}
.ppath {{ color:var(--muted); font-size:11.5px; word-break:break-all; }}
.rnote {{ font-size:11.5px; color:var(--ink2); margin-top:2px; }}
.rnote code {{ color:var(--ink2); }}
.chip {{ display:inline-block; font-size:10.5px; font-weight:650; letter-spacing:.03em; border-radius:99px;
  padding:1px 8px; vertical-align:1px; }}
.chip-404 {{ background:var(--chip404); color:var(--crit); }}
.spark {{ width:120px; height:26px; display:block; }}
.sp-a {{ opacity:.14; stroke:none; }}
.sp-l {{ fill:none; stroke-width:1.4; }}
.c-spark {{ width:130px; }}
details.silent {{ margin:10px 2px 4px; }}
.silentlist {{ font-size:12.5px; color:var(--ink2); line-height:1.8; }}
.consnote {{ font-size:12.5px; color:var(--muted); margin:10px 2px 4px; border-top:1px dashed var(--grid); padding-top:8px; }}

.foot {{ color:var(--ink2); font-size:13px; border-top:1px solid var(--hair); margin-top:34px; padding-top:18px; }}
.foot h3 {{ font-size:12px; letter-spacing:.09em; text-transform:uppercase; color:var(--muted); margin:16px 0 6px; }}
.foot dl {{ margin:0; }} .foot dt {{ font-weight:600; color:var(--ink); }} .foot dd {{ margin:0 0 8px; }}
</style>

<div class="wrap">
<p class="eyebrow">Synergy Health Partners · Organic Search</p>
<h1>Spine pages — drill-down by page type</h1>
<p class="meta">Google Search Console, property <code>synergyhealth.org</code> · 26 weeks: <b>Feb 9 – Aug 9, 2026</b> ·
headline tiles &amp; page tables show the <b>last 4 complete weeks (Jul 13 – Aug 9)</b> vs the prior 4 ·
URL statuses verified by Screaming Frog crawl · provider scope: spine surgeons only · prepared Aug 11, 2026</p>

<div class="tiles">
  <div class="tile"><div class="lab">Clicks · last 4 wk</div><div class="val">{tot["c4"]:,}</div>
    <div class="sub">{tile_delta(dvalT, dsignT)} vs prior 4 wk ({tot["cp"]:,})</div></div>
  <div class="tile"><div class="lab">Impressions · last 4 wk</div><div class="val">{fmtn(tot["i4"])}</div>
    <div class="sub">{tile_delta(dvalI, dsignI)} vs prior 4 wk ({fmtn(tot["ip"])})</div></div>
  <div class="tile"><div class="lab">CTR · last 4 wk</div><div class="val">{ctr4:.2f}%</div>
    <div class="sub">prior 4 wk: {ctrp:.2f}%</div></div>
  <div class="tile"><div class="lab">Spine URLs tracked</div><div class="val">{live_pages + cons_pages + dead_pages}</div>
    <div class="sub">{live_pages} live · {cons_pages} consolidated (301) · {dead_pages} dead (404)</div></div>
</div>

<div class="callout"><b>Read this first:</b> the six spine surgeons&rsquo; profile pages earn {D["types"]["Providers"]["c4"]:,} of
{tot["c4"]:,} spine clicks ({D["types"]["Providers"]["c4"]/tot["c4"]*100:.0f}%) at
{ctr(D["types"]["Providers"]["c4"], D["types"]["Providers"]["i4"])} CTR — steady, branded demand. The condition &amp; treatment pages
hold most of the impressions but convert at ~0.2–0.4%. A URL migration on <b>Apr 22</b> moved the clinical library from
<code>/specialties/…</code> to <code>/treatment/…</code> and <code>/conditions/…</code> — visible in the chart. Per the Aug 11 crawl
that consolidation is largely implemented: redirected URLs are no longer listed, though their history stays in the totals.
Provider scope: <b>spine surgeons only</b>; the wider bench (pain, chiro, PT) is footnoted in the surgeon section.</div>

<div class="card">
<h2>Weekly Google impressions by page type</h2>
<p class="sub">26 weeks, Mon–Sun. Hover for weekly values (impressions, with clicks in parentheses).</p>
<div class="chartbox" id="chartbox">
<svg viewBox="0 0 {CW} {CH}" role="img" aria-label="Line chart of weekly Google impressions for five spine page types, Feb 9 to Aug 9 2026. The specialty pages line collapses in late April while treatments and conditions rise — the April 22 URL migration.">
{gridlines}
{annotation}
{chart_paths and "".join(chart_paths)}
{end_labels}
{xticks}
<line id="cross" class="cross" x1="0" x2="0" y1="{PT}" y2="{CH-PB}"/>
<rect id="hover" x="{PL}" y="{PT}" width="{CW-PL-PR}" height="{CH-PT-PB}" fill="transparent"/>
</svg>
<div class="tip" id="tip"></div>
</div>
<details class="tblv"><summary>Weekly data table (impressions / clicks)</summary>
<div class="tscroll"><table>
<thead><tr><th>Week of</th>{"".join(f"<th>{g}</th>" for g in TYPES)}</tr></thead>
<tbody>{wk_rows}</tbody></table></div></details>
</div>

{sections}

<div class="foot">
<h3>How to read this</h3>
<dl>
<dt>Impressions</dt><dd>How many times a page appeared anywhere in Google results — reach, not visits.</dd>
<dt>Clicks</dt><dd>People who actually clicked through to the page from Google.</dd>
<dt>CTR (click-through rate)</dt><dd>Clicks ÷ impressions. Spine provider pages run ~3–5%; condition/treatment pages currently ~0.2–0.3%, which is the main fixable gap (title &amp; description rewrites).</dd>
<dt>Δ impr.</dt><dd>Change in impressions, last 4 weeks (Jul 13 – Aug 9) vs the prior 4 (Jun 15 – Jul 12).</dd>
<dt>Consolidated (301)</dt><dd>URL now permanently redirects to its canonical page (verified by the Aug 11 Screaming Frog crawl). These rows are removed from the tables; each section notes how many it absorbed.</dd>
<dt>✕ 404</dt><dd>URL currently returns “page not found” but still appeared in search this window — each has a redirect queued in the implementation file.</dd>
<dt>“301 pending”</dt><dd>Page is still live but scheduled to consolidate into the canonical URL shown (remaining rows in <code>data/redirects-to-implement-v2-2026-08-11.csv</code>).</dd>

</dl>
<h3>Method &amp; caveats</h3>
<p>Source: Google Search Console page-level data (aggregation: by page), spine pages identified by a validated URL pattern
(topic keywords + the spine provider roster). Google search only — Bing not included. GSC data is finalized through Aug 9;
weeks run Monday–Sunday. HTTP statuses (200 / 301 / 404) verified by a Screaming Frog list-mode crawl on Aug 11, 2026.
Live pages with zero impressions all window are listed inside each section. Full inventory &amp; redirect map: <code>data/</code> folder in the
SHP marketing workspace repo.</p>
</div>
</div>

<script>
const CD = {chart_data_js};
const box = document.getElementById('chartbox'), tip = document.getElementById('tip'),
      cross = document.getElementById('cross'), hover = document.getElementById('hover'),
      svg = box.querySelector('svg');
const ORDER = {json.dumps(TYPES)};
const KVAR = {json.dumps({"Providers":"--k-prov","Conditions":"--k-cond","Treatments":"--k-trt","Specialty":"--k-spec","Other":"--k-oth"})};
function showWeek(w, clientY) {{
  w = Math.max(0, Math.min(25, w));
  const r = svg.getBoundingClientRect();
  const sx = CD.geom.cw / r.width;
  const cx = CD.geom.pl + w * (CD.geom.cw - CD.geom.pl - CD.geom.pr) / 25;
  cross.setAttribute('x1', cx); cross.setAttribute('x2', cx); cross.style.opacity = 1;
  const kvar = KVAR;
  let rows = ORDER.map(g =>
    `<div class="row"><span class="nm"><span class="key" style="background:var(${{kvar[g]}})"></span>${{g}}</span>` +
    `<span class="val">${{CD.series[g][w].toLocaleString()}} <span style="opacity:.6;font-weight:400">(${{CD.clicks[g][w]}})</span></span></div>`).join('');
  tip.innerHTML = `<div class="tw-lab">Week of ${{CD.weeks[w]}}</div>` + rows;
  tip.style.opacity = 1;
  const bx = box.getBoundingClientRect();
  let lx = (cx / sx) + 14; if (lx + 210 > bx.width) lx = (cx / sx) - 224;
  tip.style.left = lx + 'px';
  tip.style.top = Math.max(0, ((clientY ?? (bx.top + 120)) - bx.top) - 40) + 'px';
  return w;
}}
let kw = 12;
svg.setAttribute('tabindex', '0');
svg.setAttribute('aria-label', svg.getAttribute('aria-label') + ' Focus the chart and use left and right arrow keys to step through weeks; values also appear in the weekly data table below.');
svg.addEventListener('keydown', e => {{
  if (e.key === 'ArrowRight') {{ kw = showWeek(kw + 1); e.preventDefault(); }}
  else if (e.key === 'ArrowLeft') {{ kw = showWeek(kw - 1); e.preventDefault(); }}
  else if (e.key === 'Escape') {{ tip.style.opacity = 0; cross.style.opacity = 0; }}
}});
svg.addEventListener('blur', () => {{ tip.style.opacity = 0; cross.style.opacity = 0; }});
hover.addEventListener('pointermove', e => {{
  const r = svg.getBoundingClientRect();
  const px = (e.clientX - r.left) * (CD.geom.cw / r.width);
  kw = showWeek(Math.round((px - CD.geom.pl) / ((CD.geom.cw - CD.geom.pl - CD.geom.pr) / 25)), e.clientY);
}});
hover.addEventListener('mouseleave', () => {{ tip.style.opacity = 0; cross.style.opacity = 0; }});
</script>
"""
open("spine-drilldown-report.html", "w").write(page)
print("written:", len(page), "chars")
