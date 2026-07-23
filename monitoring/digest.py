#!/usr/bin/env python3
"""
SHP monitoring digest.

Reads every feed in shp-brand-monitoring.opml, collects items published in the
last LOOKBACK_HOURS, and:
  - writes a Markdown digest to the GitHub Actions job summary (always), and
  - delivers it to Slack (if SLACK_WEBHOOK_URL set) and/or email (if SMTP_* set).

Designed for GitHub Actions (open internet). Stdlib only — no pip install, so it
can't fail on a dependency. Handles RSS (Google/Bing News) and Atom (Reddit,
YouTube) alike.

Env (all optional):
  LOOKBACK_HOURS     window in hours (default 24)
  MAX_PER_FEED       cap items shown per feed (default 12)
  SEND_WHEN_EMPTY    "true" to still ping Slack/email with nothing new (default false)
  MONITOR_UA         User-Agent (Reddit wants a descriptive one)
  SLACK_WEBHOOK_URL  Slack Incoming Webhook
  SMTP_HOST/PORT/USER/PASS, EMAIL_FROM, EMAIL_TO   email delivery
"""

import os
import sys
import time
import ssl
import smtplib
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timezone, timedelta
from collections import Counter

import scoring  # local module (monitoring/ is on sys.path when run as a script)

HERE = os.path.dirname(os.path.abspath(__file__))
OPML = os.path.join(HERE, "shp-brand-monitoring.opml")

LOOKBACK_HOURS = int(os.environ.get("LOOKBACK_HOURS") or 24)
MAX_PER_FEED = int(os.environ.get("MAX_PER_FEED") or 12)
SEND_WHEN_EMPTY = (os.environ.get("SEND_WHEN_EMPTY") or "false").lower() == "true"
UA = os.environ.get("MONITOR_UA") or \
    "SHP-BrandMonitor/1.0 (+https://synergyhealth.org; internal RSS digest)"

NOW = datetime.now(timezone.utc)
CUTOFF = NOW - timedelta(hours=LOOKBACK_HOURS)


# ---- OPML ------------------------------------------------------------------
def parse_opml(path):
    """Return [(folder, [(feed_title, url), ...]), ...] preserving order."""
    root = ET.parse(path).getroot()
    body = root.find("body")
    groups = []
    for outline in body.findall("outline"):
        if outline.get("xmlUrl"):
            groups.append(("General",
                           [(outline.get("title") or outline.get("xmlUrl"),
                             outline.get("xmlUrl"))]))
            continue
        folder = outline.get("title") or outline.get("text") or "Feeds"
        feeds = [(f.get("title") or f.get("text") or f.get("xmlUrl"), f.get("xmlUrl"))
                 for f in outline.findall("outline") if f.get("xmlUrl")]
        groups.append((folder, feeds))
    return groups


# ---- fetch + parse ---------------------------------------------------------
def fetch(url, tries=3):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": UA,
                "Accept": "application/rss+xml, application/atom+xml, "
                          "application/xml;q=0.9, */*;q=0.8",
            })
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001 — best-effort; report + continue
            last = e
            time.sleep(2 * (i + 1))
    raise last


def _local(tag):
    return tag.split("}")[-1]


def _child(el, *names):
    for c in el:
        if _local(c.tag) in names:
            return c
    return None


def _text(el):
    return (el.text or "").strip() if el is not None else ""


def parse_date(s):
    s = (s or "").strip()
    if not s:
        return None
    try:
        dt = parsedate_to_datetime(s)          # RFC822 (RSS pubDate)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        pass
    try:                                       # ISO8601 (Atom updated/published)
        iso = s[:-1] + "+00:00" if s.endswith("Z") else s
        dt = datetime.fromisoformat(iso)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        return None


def parse_feed(data):
    """Return [{title, link, when}] for RSS or Atom."""
    out = []
    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return out
    tag = _local(root.tag)
    if tag == "rss":
        channel = _child(root, "channel")
        entries = [c for c in channel if _local(c.tag) == "item"] if channel is not None else []
    elif tag == "feed":
        entries = [c for c in root if _local(c.tag) == "entry"]
    else:
        entries = [c for c in root.iter() if _local(c.tag) in ("item", "entry")]

    for e in entries:
        title = _text(_child(e, "title"))
        link_el = _child(e, "link")
        link = ""
        if link_el is not None:
            link = link_el.get("href") or _text(link_el)
        if not link:
            link = _text(_child(e, "guid"))
        when = None
        for dt_tag in ("pubDate", "published", "updated", "date"):
            d = _child(e, dt_tag)
            if d is not None and _text(d):
                when = parse_date(_text(d))
                if when:
                    break
        out.append({"title": title or "(no title)", "link": link, "when": when})
    return out


def collect():
    """Fetch every feed, keep items in-window, dedup, and score each mention.
    Returns (ranked_mentions, total_feeds, failures)."""
    groups = parse_opml(OPML)
    mentions, failures, seen = [], [], set()
    total_feeds = 0
    for folder, feeds in groups:
        for ftitle, url in feeds:
            total_feeds += 1
            try:
                items = parse_feed(fetch(url))
            except Exception as e:  # noqa: BLE001
                failures.append((ftitle, str(e)[:140]))
                continue
            for it in items:
                if not (it["when"] and it["when"] >= CUTOFF):
                    continue
                key = (it["link"] or it["title"]).strip().lower()
                if key in seen:
                    continue
                seen.add(key)
                m = {"folder": folder, "feed": ftitle, "title": it["title"],
                     "link": it["link"], "when": it["when"]}
                m.update(scoring.score(folder, ftitle, it["title"]))
                mentions.append(m)
            time.sleep(0.7)  # be polite (Reddit rate-limits bursts)
    mentions.sort(key=lambda m: (m["score"], m["when"] or NOW), reverse=True)
    return mentions, total_feeds, failures


# ---- renderers (single consolidated, ranked board) -------------------------
LL = scoring._LINE_LABEL
SL = scoring._SIGNAL_LABEL


def _bands(mentions):
    return ([m for m in mentions if m["band"] == "P1"],
            [m for m in mentions if m["band"] == "P2"],
            [m for m in mentions if m["band"] == "P3"])


def _src(feed):
    for a, b in (("Google News · ", "GN "), ("Bing News · ", "BN "),
                 ("Reddit · ", "RDT "), ("YouTube · ", "YT "),
                 ("Google Alert · ", "GA ")):
        feed = feed.replace(a, b)
    return feed


def _header(mentions, total_feeds):
    p1, p2, p3 = _bands(mentions)
    mix = ""
    if mentions:
        cl = Counter(m["line"] for m in mentions)
        mix = " · ".join(f"{LL.get(k, k)} {v}" for k, v in cl.most_common())
    return p1, p2, p3, mix


def render_md(mentions, total_feeds, failures, title="SHP Mention Board",
              window_desc=None):
    window_desc = window_desc or f"in the last {LOOKBACK_HOURS}h"
    p1, p2, p3, mix = _header(mentions, total_feeds)
    out = [f"# {title} — {NOW:%Y-%m-%d %H:%M UTC}", "",
           f"**{len(mentions)} mention(s)** {window_desc} across "
           f"{total_feeds} feeds  ·  🔴 P1 **{len(p1)}**  ·  🟠 P2 **{len(p2)}**  ·  "
           f"⚪ P3 {len(p3)}", ""]
    out += [f"_Ranked by inferred patient-value (spine/ortho weighted highest; "
            f"foot/hand/pain via partnerships). Scores are heuristic — a triage aid._", ""]
    if mix:
        out += [f"_Line mix: {mix}_", ""]
    if not mentions:
        out += ["_Nothing new in the window._", ""]

    def table(title, rows, cap=None):
        if not rows:
            return []
        seg = [f"## {title}", "",
               "| Score | Line | Signal | Mention | Route |",
               "|--:|:--|:--|:--|:--|"]
        for m in (rows[:cap] if cap else rows):
            t = m["title"].replace("|", "∣")
            neg = " ⚠" if m["mods"]["negative"] else ""
            ment = f"[{t}]({m['link'] or ''})<br><sub>{_src(m['feed'])}</sub>"
            seg.append(f"| {m['score']} | {LL.get(m['line'], m['line'])} | "
                       f"{SL.get(m['signal'], m['signal'])}{neg} | {ment} | {m['route']} |")
        if cap and len(rows) > cap:
            seg.append(f"| | | | _+{len(rows) - cap} more P3 items (full board in the "
                       f"Actions run)_ | |")
        seg.append("")
        return seg

    out += table("🔴 P1 — act today", p1)
    out += table("🟠 P2 — this week", p2)
    out += table("⚪ P3 — ambient / FYI", p3, cap=20)
    if failures:
        out += ["## ⚠️ Feeds that failed this run",
                "_(transient — usually rate-limiting; they retry next run)_", ""]
        out += [f"- {ft} — `{err}`" for ft, err in failures[:25]]
    return "\n".join(out)


def render_slack(mentions, total_feeds):
    p1, p2, p3, mix = _header(mentions, total_feeds)
    hdr = (f":clipboard: *SHP Mention Board* — {NOW:%Y-%m-%d %H:%M UTC}\n"
           f"*{len(mentions)}* new · 🔴 P1 *{len(p1)}* · 🟠 P2 *{len(p2)}* · "
           f"⚪ P3 {len(p3)}  _(last {LOOKBACK_HOURS}h)_")
    if not mentions:
        return hdr + "\n_Nothing new in the window._"
    parts, used = [hdr], len(hdr)
    for title, rows in (("🔴 *P1 — act today*", p1), ("🟠 *P2 — this week*", p2)):
        if not rows:
            continue
        seg = ["\n" + title]
        for m in rows:
            t = m["title"].replace("<", "").replace(">", "")
            seg.append(f"• `{m['score']:>3}` {LL.get(m['line'], m['line'])}/"
                       f"{SL.get(m['signal'], m['signal'])} — <{m['link']}|{t}>"
                       f"  _→ {m['route']}_")
        chunk = "\n".join(seg)
        if used + len(chunk) > 38000:
            parts.append("\n_…truncated — full board in the GitHub Actions run._")
            break
        parts.append(chunk)
        used += len(chunk)
    if p3:
        parts.append(f"\n_+{len(p3)} P3 ambient item(s) in the full board._")
    return "\n".join(parts)


def render_html(mentions, total_feeds, failures, title="SHP Mention Board",
                window_desc=None):
    import html as _h
    window_desc = window_desc or f"in the last {LOOKBACK_HOURS}h"
    p1, p2, p3, mix = _header(mentions, total_feeds)
    p = [f"<h2>{_h.escape(title)} — {NOW:%Y-%m-%d %H:%M UTC}</h2>",
         f"<p><strong>{len(mentions)}</strong> {_h.escape(window_desc)} across "
         f"{total_feeds} feeds · 🔴 P1 <strong>{len(p1)}</strong> · 🟠 P2 "
         f"<strong>{len(p2)}</strong> · ⚪ P3 {len(p3)}</p>",
         "<p style='color:#555'><em>Ranked by inferred patient-value (spine/ortho "
         "highest; foot/hand/pain via partnerships). Heuristic triage aid.</em></p>"]
    if mix:
        p.append(f"<p><em>Line mix: {_h.escape(mix)}</em></p>")
    if not mentions:
        p.append("<p><em>Nothing new in the window.</em></p>")

    def table(title, rows, cap=None):
        if not rows:
            return
        p.append(f"<h3>{title}</h3>")
        p.append("<table cellpadding='6' style='border-collapse:collapse' border='1'>"
                 "<tr><th>Score</th><th>Line</th><th>Signal</th><th>Mention</th>"
                 "<th>Route</th></tr>")
        for m in (rows[:cap] if cap else rows):
            neg = " ⚠" if m["mods"]["negative"] else ""
            p.append(
                f"<tr><td align='right'><strong>{m['score']}</strong></td>"
                f"<td>{LL.get(m['line'], m['line'])}</td>"
                f"<td>{SL.get(m['signal'], m['signal'])}{neg}</td>"
                f"<td><a href=\"{_h.escape(m['link'] or '')}\">"
                f"{_h.escape(m['title'])}</a><br><small>{_h.escape(_src(m['feed']))}"
                f"</small></td><td>{_h.escape(m['route'])}</td></tr>")
        if cap and len(rows) > cap:
            p.append(f"<tr><td colspan='5'><em>+{len(rows) - cap} more P3 items</em>"
                     f"</td></tr>")
        p.append("</table>")

    table("🔴 P1 — act today", p1)
    table("🟠 P2 — this week", p2)
    table("⚪ P3 — ambient / FYI", p3, cap=20)
    return "\n".join(p)


# ---- delivery --------------------------------------------------------------
def write_summary(md):
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a", encoding="utf-8") as f:
            f.write(md + "\n")
    print(md)


def post_slack(url, text):
    import json
    body = json.dumps({"text": text}).encode("utf-8")
    req = urllib.request.Request(url, data=body,
                                 headers={"Content-Type": "application/json",
                                          "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        r.read()


def send_email(html_body, total_new):
    host = os.environ.get("SMTP_HOST")
    to = os.environ.get("EMAIL_TO")
    if not (host and to):
        return False
    port = int(os.environ.get("SMTP_PORT") or 587)
    user = os.environ.get("SMTP_USER")
    pw = os.environ.get("SMTP_PASS")
    sender = os.environ.get("EMAIL_FROM") or user or "monitor@synergyhealth.org"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"SHP monitoring — {total_new} new ({NOW:%b %d})"
    msg["From"] = sender
    msg["To"] = to
    msg.attach(MIMEText("HTML digest attached (view in an HTML-capable client).",
                        "plain"))
    msg.attach(MIMEText(html_body, "html"))

    recipients = [x.strip() for x in to.split(",") if x.strip()]
    if port == 465:
        with smtplib.SMTP_SSL(host, port, context=ssl.create_default_context(),
                              timeout=30) as s:
            if user:
                s.login(user, pw)
            s.sendmail(sender, recipients, msg.as_string())
    else:
        with smtplib.SMTP(host, port, timeout=30) as s:
            s.starttls(context=ssl.create_default_context())
            if user:
                s.login(user, pw)
            s.sendmail(sender, recipients, msg.as_string())
    return True


def main():
    mentions, total_feeds, failures = collect()
    md = render_md(mentions, total_feeds, failures)
    write_summary(md)

    if not mentions and not SEND_WHEN_EMPTY:
        print("Nothing new; skipping Slack/email (set SEND_WHEN_EMPTY=true to override).")
        return

    slack = os.environ.get("SLACK_WEBHOOK_URL")
    if slack:
        try:
            post_slack(slack, render_slack(mentions, total_feeds))
            print("Slack: sent.")
        except Exception as e:  # noqa: BLE001
            print(f"Slack: FAILED — {e}", file=sys.stderr)

    if os.environ.get("SMTP_HOST") and os.environ.get("EMAIL_TO"):
        try:
            send_email(render_html(mentions, total_feeds, failures), len(mentions))
            print("Email: sent.")
        except Exception as e:  # noqa: BLE001
            print(f"Email: FAILED — {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
