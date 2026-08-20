"""Draws the art in the profile README.

    python assets/build.py

To change the entire look of the page, edit STYLE below and rerun. Nothing else
moves: the filenames stay the same, so the README never needs touching, and the
scheduled job keeps working.

    STYLE = "canvas"   the cyber layout with the neon removed, drawn as
                       instrumentation: graphite grid, one ochre accent
    STYLE = "cyber"    neon grid horizon, chromatic wordmark, scanlines
    STYLE = "luxury"   serif at scale, gold hairlines, wide margins
    STYLE = "glass"    frosted panels over drifting colour, real gaussian blur

Each style lives in its own module and draws the same five things from the same
data, so switching cannot change what the page says, only how it looks.

Every asset is a single file rather than a light and dark pair. All three styles
are dark native, painting their own background edge to edge, so a page reads the
same whichever GitHub theme the visitor uses and there is no second palette to
keep in sync.

Animation. CSS keyframes live inside each file. GitHub serves it and the browser
paints it as an image, so the animation survives, the same mechanism the
contribution snake uses. Anyone whose system asks for reduced motion gets a
still frame.

Live numbers come from the public API, no token needed. If it cannot be reached
the affected card is left exactly as it was, because a card showing yesterday's
correct figures beats one confidently showing invented ones. That path has
fired for real several times, so it is not theoretical.
"""

import importlib
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

STYLE = "canvas"

OUT = pathlib.Path(__file__).parent
sys.path.insert(0, str(OUT))
USER = "Hassaan146"

W = 1000
CW = 0.601
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SANS = "Segoe UI, ui-sans-serif, -apple-system, Helvetica, Arial, sans-serif"
SERIF = "Georgia, 'Times New Roman', Times, serif"
REDUCE = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def mono_w(text, size):
    return len(text) * size * CW


# ---------------------------------------------------------------------------
# the content, shared by every style
# ---------------------------------------------------------------------------

PRINCIPLES = [
    ("01", "GUARDRAILS FIRST",
     ["Rate limiting, validation and row", "level security before features."]),
    ("02", "DEGRADE, DO NOT DIE",
     ["Every external call has a fallback.", "Clone it, it runs with zero keys."]),
    ("03", "DECIDE BEFORE CODING",
     ["The architectural choice gets made,", "and written down, first."]),
]

SYSTEMS = {
    "forge": dict(
        n="01", title="FORGE MENTOR", meta="CLAUDE CODE PLUGIN / MIT / v1.28",
        nodes=["question", "options", "you decide", "recorded", "code runs"],
        note="the gate holds until the decision exists",
        metrics=[("1,216", "TESTS"), ("100%", "COVERAGE"), ("3", "MODES"), ("MIT", "LICENCE")],
        stack="Python 3.12 / MCP / Claude / Git"),
    "news": dict(
        n="02", title="AI NEWS AGGREGATOR", meta="FULL STACK / DEPLOYED / DAILY AT 07:00",
        nodes=["scrape", "store", "rank", "summarise", "email"],
        note="two model providers, so one bad day does not kill the digest",
        metrics=[("164", "SITES"), ("36", "CHANNELS"), ("5", "PICKS A DAY"), ("LIVE", "DEPLOYED")],
        stack="React / Vite / FastAPI / PostgreSQL / Groq / Gemini / Stripe"),
    "skyelite": dict(
        n="03", title="SKYELITE AI", meta="HACKATHON BUILD / 3RD NATIONALLY / OPEN SOURCE",
        nodes=["intake", "filter", "visa", "research", "scoring", "tradeoff", "final"],
        note="ranks on safety, budget, visa difficulty and scenery, then shows its working",
        metrics=[("3rd", "NATIONAL"), ("7", "GRAPH NODES"), ("0", "KEYS TO RUN"),
                 ("GCF", "ADOPTER")],
        stack="Next.js 15 / TypeScript / Three.js / FastAPI / Pydantic v2 / LangGraph"),
    "bitmadwall": dict(
        n="04", title="BITMADWALL", meta="PRODUCT WORK / SHIPPED / bitmadwall.ai",
        nodes=["your phone", "relay", "relay", "recipient"],
        note="works where the network is gone or cannot be trusted",
        metrics=[("AES-256", "GCM"), ("7", "MESH HOPS"), ("0", "SERVERS"), ("NO SIM", "CRYPTO ID")],
        stack="Bluetooth LE / Wi-Fi Direct / LoRa / double ratchet / Bitcoin"),
    "employeeos": dict(
        n="05", title="AI EMPLOYEE OS", meta="AGENT ORCHESTRATION / IN PROGRESS",
        nodes=["request", "decompose", "route to agents", "validate", "trace"],
        note="plain English in, a dependency aware workflow out",
        metrics=[("1", "REQUEST"), ("N", "AGENTS"), ("DAG", "ORDERED"), ("FULL", "TRACE")],
        stack="Next.js / FastAPI / Pydantic / LangGraph / LangChain / Supabase / Groq"),
}

FS, PAD, GAP, BH = 11.5, 13, 22, 30


# ---------------------------------------------------------------------------
# live numbers
# ---------------------------------------------------------------------------

def _get(url, tries=4):
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "readme-build"})
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.load(r)
        except (urllib.error.URLError, OSError) as e:
            last = e
            if attempt < tries - 1:
                time.sleep(2 * (attempt + 1))
    raise last


def _dmy(dt):
    return "%d %s" % (dt.day, dt.strftime("%b %Y"))


def stats():
    try:
        repos = stars = 0
        newest = None
        langs = {}
        for page in range(1, 6):
            batch = _get("https://api.github.com/users/%s/repos?per_page=100&page=%d"
                         % (USER, page))
            if not batch:
                break
            for r in batch:
                if r.get("fork"):
                    continue
                repos += 1
                stars += r.get("stargazers_count", 0)
                if r.get("language"):
                    langs[r["language"]] = langs.get(r["language"], 0) + 1
                ts = r.get("pushed_at")
                if ts and (newest is None or ts > newest):
                    newest = ts
        if not repos or newest is None or not langs:
            return None
        when = datetime.strptime(newest, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        return {"repos": repos, "stars": stars, "pushed": _dmy(when),
                "langs": sorted(langs.items(), key=lambda kv: -kv[1])}
    except (urllib.error.URLError, ValueError, KeyError, TypeError, OSError) as e:
        print("  api unreachable (%s); cards with live numbers left untouched" % e)
        return None


# ---------------------------------------------------------------------------
# geometry check
#
# Two bugs got through before this existed. A label ran past the canvas edge,
# and the stack line shared a baseline with the metric labels and overlapped on
# four cards out of five. Neither was visible in a status code, so the build
# measures its own output now.
# ---------------------------------------------------------------------------

def audit(path):
    body = path.read_text(encoding="utf-8")
    width = int(re.search(r'viewBox="0 0 (\d+) ', body).group(1))
    rows, faults = {}, []
    for tag in re.finditer(r"<text\b([^>]*)>([^<]*)</text>", body):
        attrs, txt = tag.group(1), tag.group(2)
        mx = re.search(r'\bx="([\d.]+)"', attrs)
        my = re.search(r'\by="([\d.]+)"', attrs)
        mf = re.search(r'font-size="([\d.]+)"', attrs)
        if not (mx and my and mf):
            continue
        x, y, fs = float(mx.group(1)), float(my.group(1)), float(mf.group(1))
        anchor = re.search(r'text-anchor="(\w+)"', attrs)
        anchor = anchor.group(1) if anchor else ""
        w = len(txt) * fs * (CW if "monospace" in attrs else 0.55)
        lo = x - w if anchor == "end" else (x - w / 2 if anchor == "middle" else x)
        if lo + w > width - 4:
            faults.append("runs past the edge: %r" % txt[:30])
        rows.setdefault(round(y), []).append((lo, lo + w, txt))
    for y, items in rows.items():
        items.sort()
        for i in range(len(items) - 1):
            # identical text on one baseline is a deliberate offset copy,
            # which is how the chromatic split and the glow doubling work
            if items[i][1] > items[i + 1][0] + 2 and items[i][2] != items[i + 1][2]:
                faults.append("overlap at y=%d: %r and %r"
                              % (y, items[i][2][:22], items[i + 1][2][:22]))
    return faults


if __name__ == "__main__":
    style = importlib.import_module("style_%s" % STYLE)
    print("  style: %s" % STYLE)
    s = stats()
    if s:
        print("  stats: %d repos, %d stars, last %s" % (s["repos"], s["stars"], s["pushed"]))

    keep = set()
    if hasattr(style, "canvas"):
        # one sheet. It carries the live numbers, so a failed fetch leaves the
        # existing file alone rather than redrawing it without them.
        out = OUT / "canvas.svg"
        if s is not None or not out.exists():
            out.write_text(style.canvas(s), encoding="utf-8")
        keep.add(out.name)
    else:
        for stem, fn in (("hero", style.hero), ("principles", style.principles),
                         ("signoff", style.signoff)):
            (OUT / ("%s.svg" % stem)).write_text(fn(), encoding="utf-8")
            keep.add("%s.svg" % stem)
        for key, spec in SYSTEMS.items():
            (OUT / ("sys-%s.svg" % key)).write_text(style.card(spec), encoding="utf-8")
            keep.add("sys-%s.svg" % key)
        sig = OUT / "signals.svg"
        if s is not None:
            sig.write_text(style.signals(s), encoding="utf-8")
        keep.add(sig.name)

    for old in OUT.glob("*.svg"):
        if old.name not in keep:
            old.unlink()
            print("  removed %s" % old.name)

    bad = 0
    for n in sorted(keep):
        f = OUT / n
        if not f.exists():
            print("  MISSING  %s" % n)
            bad += 1
            continue
        faults = audit(f)
        print("  wrote    %s%s" % (n, "" if not faults else "   " + faults[0]))
        bad += len(faults)
    print("  geometry faults: %d" % bad)
    if s is None:
        print()
        print("  the API did not answer, so signals kept its previous numbers")
