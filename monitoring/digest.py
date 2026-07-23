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
    groups = parse_opml(OPML)
    sections, failures = [], []
    total_new = total_feeds = 0
    for folder, feeds in groups:
        hits = []
        for ftitle, url in feeds:
            total_feeds += 1
            try:
                items = parse_feed(fetch(url))
            except Exception as e:  # noqa: BLE001
                failures.append((ftitle, str(e)[:140]))
                continue
            fresh = [it for it in items if it["when"] and it["when"] >= CUTOFF]
            fresh.sort(key=lambda x: x["when"], reverse=True)
            if fresh:
                hits.append((ftitle, fresh[:MAX_PER_FEED]))
                total_new += len(fresh)
            time.sleep(0.7)  # be polite (Reddit rate-limits bursts)
        if hits:
            sections.append((folder, hits))
    return sections, total_new, total_feeds, failures


# ---- renderers -------------------------------------------------------------
def _stamp(it):
    return it["when"].strftime("%b %d %H:%M UTC") if it["when"] else ""


def render_md(sections, total_new, total_feeds, failures):
    lines = [f"# SHP brand & provider monitoring — {NOW:%Y-%m-%d %H:%M UTC}",
             "",
             f"**{total_new} new item(s)** in the last {LOOKBACK_HOURS}h "
             f"across {total_feeds} feeds."]
    if not total_new:
        lines += ["", "_Nothing new in the window._"]
    for folder, hits in sections:
        lines += ["", f"## {folder}"]
        for ftitle, items in hits:
            lines.append(f"- **{ftitle}**")
            for it in items:
                stamp = f" — _{_stamp(it)}_" if it["when"] else ""
                link = it["link"] or ""
                lines.append(f"  - [{it['title']}]({link}){stamp}")
    if failures:
        lines += ["", "## ⚠️ Feeds that failed this run",
                  "_(transient — usually rate-limiting; they retry next run)_"]
        for ftitle, err in failures[:25]:
            lines.append(f"- {ftitle} — `{err}`")
    return "\n".join(lines)


def render_slack(sections, total_new, total_feeds, failures):
    # Slack mrkdwn: <url|text>, *bold*
    hdr = (f":mag: *SHP brand & provider monitoring* — {NOW:%Y-%m-%d %H:%M UTC}\n"
           f"*{total_new}* new item(s) in the last {LOOKBACK_HOURS}h "
           f"across {total_feeds} feeds.")
    if not total_new:
        return hdr + "\n_Nothing new in the window._"
    parts, budget = [hdr], 38000  # keep well under Slack's ~40k limit
    used = len(hdr)
    for folder, hits in sections:
        block = [f"\n*{folder}*"]
        for ftitle, items in hits:
            block.append(f"• _{ftitle}_")
            for it in items:
                t = it["title"].replace("<", "").replace(">", "")
                stamp = f"  ({_stamp(it)})" if it["when"] else ""
                block.append(f"   ◦ <{it['link']}|{t}>{stamp}")
        chunk = "\n".join(block)
        if used + len(chunk) > budget:
            parts.append("\n_…truncated — see the full digest in the GitHub Actions run._")
            break
        parts.append(chunk)
        used += len(chunk)
    return "\n".join(parts)


def render_html(sections, total_new, total_feeds, failures):
    import html as _h
    p = [f"<h2>SHP brand &amp; provider monitoring — {NOW:%Y-%m-%d %H:%M UTC}</h2>",
         f"<p><strong>{total_new}</strong> new item(s) in the last {LOOKBACK_HOURS}h "
         f"across {total_feeds} feeds.</p>"]
    if not total_new:
        p.append("<p><em>Nothing new in the window.</em></p>")
    for folder, hits in sections:
        p.append(f"<h3>{_h.escape(folder)}</h3><ul>")
        for ftitle, items in hits:
            p.append(f"<li><strong>{_h.escape(ftitle)}</strong><ul>")
            for it in items:
                stamp = f" — <em>{_stamp(it)}</em>" if it["when"] else ""
                p.append(f'<li><a href="{_h.escape(it["link"])}">'
                         f'{_h.escape(it["title"])}</a>{stamp}</li>')
            p.append("</ul></li>")
        p.append("</ul>")
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
    sections, total_new, total_feeds, failures = collect()
    md = render_md(sections, total_new, total_feeds, failures)
    write_summary(md)

    if total_new == 0 and not SEND_WHEN_EMPTY:
        print("Nothing new; skipping Slack/email (set SEND_WHEN_EMPTY=true to override).")
        return

    slack = os.environ.get("SLACK_WEBHOOK_URL")
    if slack:
        try:
            post_slack(slack, render_slack(sections, total_new, total_feeds, failures))
            print("Slack: sent.")
        except Exception as e:  # noqa: BLE001
            print(f"Slack: FAILED — {e}", file=sys.stderr)

    if os.environ.get("SMTP_HOST") and os.environ.get("EMAIL_TO"):
        try:
            send_email(render_html(sections, total_new, total_feeds, failures), total_new)
            print("Email: sent.")
        except Exception as e:  # noqa: BLE001
            print(f"Email: FAILED — {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
