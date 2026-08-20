"""Draws the art in the profile README.

    python assets/build.py

Style is bento grid with a neo-brutalist finish: tiles of deliberately different
sizes, thick borders, a hard offset shadow under every one, and type set far
larger than a README usually dares.

The reason is structural. An earlier version made every section an identical
full-width band, ten of them stacked, so there was no hierarchy and nothing for
the eye to land on. Restyling the bands never fixed it because the shape never
changed. Different tile sizes create the hierarchy that was missing.

What it emits:

  hero-{dark,light}        name tile, system tile, strapline tile
  principles-{dark,light}  three tiles, how the work gets done
  sys-*-{dark,light}       one tile per project: title, meta, pipeline, numbers
  signals-{dark,light}     stat tiles plus the language mix, from live API data
  signoff-{dark,light}     the closing strip

Palette. Almost every profile on GitHub uses #58a6ff on #0d1117, because that is
what the badge and card services default to. This one is warm: amber on
near-black, ink on bone, so it reads as chosen rather than inherited.

Animation. CSS keyframes live inside each file. GitHub serves it and the browser
paints it as an image, so the animation survives, the same mechanism the
contribution snake uses. Anyone whose system asks for reduced motion gets a
still frame.

Themes ship as a pair and <picture> picks one, which follows the GitHub theme
toggle rather than the operating system setting.

Live numbers come from the public API, no token needed. If it cannot be reached
the affected card is left exactly as it was, because a card showing yesterday's
correct figures beats one confidently showing invented ones. That path has
fired for real several times, so it is not theoretical.
"""

import json
import math
import pathlib
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

OUT = pathlib.Path(__file__).parent
USER = "Hassaan146"

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SANS = "Segoe UI, ui-sans-serif, -apple-system, Helvetica, Arial, sans-serif"

CW = 0.601
W = 1000
SH = 7          # how far the hard shadow sits below and right of a tile
BW = 3          # border weight

REDUCE = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"

THEME = {
    "dark": dict(
        page="#0a0b0d", tile="#14161a", shadow="#000000", ink="#f4f1ec",
        dim="#9b968e", faint="#6e6a63", accent="#e8a33d", accent2="#f6cd85",
        onAccent="#0a0b0d",
    ),
    "light": dict(
        page="#fbfaf8", tile="#ffffff", shadow="#15171b", ink="#15171b",
        dim="#5f5a52", faint="#8b857a", accent="#c07f10", accent2="#8a5709",
        onAccent="#fffdf8",
    ),
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def mono_w(text, size):
    return len(text) * size * CW


def head(w, h, label, style=""):
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" '
        'height="%d" role="img" aria-label="%s">' % (w, h, w, h, esc(label))
        + ("<style>%s%s</style>" % (style, REDUCE) if style else "")
    )


def tile(t, x, y, w, h, fill=None, stroke=None, sw=BW):
    """A panel with a hard shadow. The shadow is a solid offset copy, not a
    blur, which is the whole point of the neo-brutalist look."""
    fill = fill or t["tile"]
    stroke = stroke or t["accent"]
    return ('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" opacity=".9"/>'
            '<rect x="%d" y="%d" width="%d" height="%d" fill="%s" stroke="%s" '
            'stroke-width="%d"/>'
            % (x + SH, y + SH, w, h, t["shadow"], x, y, w, h, fill, stroke, sw))


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
# hero
# ---------------------------------------------------------------------------

def _orbit(t, cx, cy, col):
    """The system motif that used to be a separate file. It lives inside the
    hero tile now, which is what a bento layout is for."""
    p = []
    for i, (r, dur, rev) in enumerate(((30, 13, ""), (52, 21, ";animation-direction:reverse"),
                                       (74, 34, ""))):
        p.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="2" '
                 'stroke-opacity=".45"/>' % (cx, cy, r, col))
        p.append('<g class="orb" style="animation-duration:%ss%s">' % (dur, rev))
        for k in range(i + 1):
            ang = 2 * math.pi * k / (i + 1)
            p.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>'
                     % (cx + r * math.cos(ang), cy + r * math.sin(ang), 5.5 - i * 0.7, col))
        p.append("</g>")
    p.append('<circle class="pulse" cx="%d" cy="%d" r="13" fill="%s"/>' % (cx, cy, col))
    return p


def hero(t):
    h = 420
    css = ('.orb{transform-box:view-box;transform-origin:812px 145px;'
           'animation-name:spin;animation-timing-function:linear;'
           'animation-iteration-count:infinite}'
           '@keyframes spin{to{transform:rotate(360deg)}}'
           '.pulse{transform-box:view-box;transform-origin:812px 145px;'
           'animation:beat 4s ease-in-out infinite}'
           '@keyframes beat{0%,100%{transform:scale(1)}50%{transform:scale(1.15)}}'
           '.rule{animation:grow 1.4s cubic-bezier(.2,.8,.2,1) both}'
           '@keyframes grow{from{width:0}to{width:130px}}')
    p = [head(W, h, "Muhammad Hassaan-ul-Mustafa. AI engineer, product and backend. "
                    "I build AI agents and the backends they run on. Arbisoft, "
                    "FAST-NUCES, Islamabad, open to remote.", css)]
    p.append('<rect width="%d" height="%d" fill="%s"/>' % (W, h, t["page"]))

    # name tile
    p.append(tile(t, 40, 40, 600, 216))
    p.append('<text x="70" y="86" font-family="%s" font-size="11" fill="%s" '
             'letter-spacing="3.2">AI ENGINEER / PRODUCT AND BACKEND</text>'
             % (MONO, t["accent"]))
    p.append('<text x="70" y="150" font-family="%s" font-size="52" font-weight="800" '
             'fill="%s" letter-spacing="-2.4">MUHAMMAD</text>' % (SANS, t["ink"]))
    p.append('<text x="70" y="204" font-family="%s" font-size="52" font-weight="800" '
             'fill="%s" letter-spacing="-2.4">HASSAAN</text>' % (SANS, t["accent"]))
    p.append('<rect class="rule" x="70" y="222" width="130" height="6" fill="%s"/>' % t["accent"])

    # system tile, filled amber so it reads as the loud one
    p.append(tile(t, 664, 40, 296, 216, fill=t["accent"], stroke=t["ink"]))
    p.append('<text x="690" y="76" font-family="%s" font-size="10.5" fill="%s" '
             'letter-spacing="2.6" opacity=".75">THE SHAPE OF THE WORK</text>'
             % (MONO, t["onAccent"]))
    p += _orbit(t, 812, 145, t["onAccent"])
    p.append('<text x="812" y="242" font-family="%s" font-size="9.6" fill="%s" '
             'letter-spacing="1.8" text-anchor="middle" opacity=".75">'
             'DATA / API / AGENTS</text>' % (MONO, t["onAccent"]))

    # strapline tile
    p.append(tile(t, 40, 288, 920, 92))
    p.append('<text x="70" y="330" font-family="%s" font-size="21" font-weight="600" '
             'fill="%s" letter-spacing="-.5">I build AI agents and the backends they '
             'run on.</text>' % (SANS, t["ink"]))
    p.append('<text x="70" y="358" font-family="%s" font-size="10.5" fill="%s" '
             'letter-spacing="2.2">ARBISOFT / FAST-NUCES / ISLAMABAD / OPEN TO REMOTE</text>'
             % (MONO, t["faint"]))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ---------------------------------------------------------------------------
# principles
# ---------------------------------------------------------------------------

PRINCIPLES = [
    ("01", "GUARDRAILS FIRST",
     ["Rate limiting, validation and row", "level security before features."]),
    ("02", "DEGRADE, DO NOT DIE",
     ["Every external call has a fallback.", "Clone it, it runs with zero keys."]),
    ("03", "DECIDE BEFORE CODING",
     ["The architectural choice gets made,", "and written down, first."]),
]


def principles(t):
    h = 186
    colw, gap = 293, 20
    css = ('.pt{animation:lift 6s ease-in-out infinite}'
           '@keyframes lift{0%,100%{opacity:.55}14%{opacity:1}32%{opacity:.55}}')
    lab = ". ".join("%s. %s" % (n, " ".join(b)) for _, n, b in PRINCIPLES)
    p = [head(W, h, lab, css)]
    p.append('<rect width="%d" height="%d" fill="%s"/>' % (W, h, t["page"]))
    for i, (num, title, lines) in enumerate(PRINCIPLES):
        x = 40 + i * (colw + gap)
        p.append(tile(t, x, 20, colw, 132))
        p.append('<rect class="pt" style="animation-delay:%ss" x="%d" y="20" width="%d" '
                 'height="7" fill="%s"/>' % (round(i * 0.8, 2), x, colw, t["accent"]))
        p.append('<text x="%d" y="66" font-family="%s" font-size="11" fill="%s" '
                 'font-weight="700">%s</text>' % (x + 24, MONO, t["accent"], num))
        p.append('<text x="%d" y="96" font-family="%s" font-size="15" font-weight="800" '
                 'fill="%s" letter-spacing="-.2">%s</text>' % (x + 24, SANS, t["ink"], title))
        for j, ln in enumerate(lines):
            p.append('<text x="%d" y="%d" font-family="%s" font-size="11.5" fill="%s">%s</text>'
                     % (x + 24, 120 + j * 17, SANS, t["dim"], esc(ln)))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ---------------------------------------------------------------------------
# project tiles
# ---------------------------------------------------------------------------

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


def card(spec, t):
    h = 328
    left = 70
    nodes, n = spec["nodes"], len(spec["nodes"])
    widths = [mono_w(x, FS) + PAD * 2 for x in nodes]
    dur = max(5.0, n * 1.15)
    css = ('.e{stroke-dasharray:2.5 4.5;animation:d 1.6s linear infinite}'
           '@keyframes d{to{stroke-dashoffset:-7}}'
           '.b{animation:s %ss ease-in-out infinite}'
           '@keyframes s{0%%{stroke-opacity:.45;fill-opacity:0}'
           '7%%{stroke-opacity:1;fill-opacity:.18}22%%{stroke-opacity:.45;fill-opacity:0}'
           '100%%{stroke-opacity:.45;fill-opacity:0}}' % dur)
    lab = ("%s. %s. %s. %s. %s" % (
        spec["title"], spec["meta"], " then ".join(nodes),
        ", ".join("%s %s" % (v, k.lower()) for v, k in spec["metrics"]), spec["stack"]))
    p = [head(W, h, lab, css)]
    p.append('<rect width="%d" height="%d" fill="%s"/>' % (W, h, t["page"]))
    p.append(tile(t, 40, 20, 920, 280))

    p.append('<text x="%d" y="72" font-family="%s" font-size="30" font-weight="800" '
             'fill="%s" letter-spacing="-1.1">%s</text>'
             % (left, SANS, t["ink"], esc(spec["title"])))
    p.append('<text x="%d" y="72" font-family="%s" font-size="34" font-weight="800" '
             'fill="%s" opacity=".28" text-anchor="end">%s</text>'
             % (W - 70, SANS, t["accent"], spec["n"]))
    p.append('<text x="%d" y="94" font-family="%s" font-size="9.6" fill="%s" '
             'letter-spacing="1.9">%s</text>' % (left, MONO, t["faint"], esc(spec["meta"])))
    p.append('<rect x="%d" y="108" width="40" height="4" fill="%s"/>' % (left, t["accent"]))

    y = 132
    x = float(left)
    for i, (label, bw) in enumerate(zip(nodes, widths)):
        d = round(i * dur / n, 2)
        p.append('<rect class="b" style="animation-delay:%ss" x="%.1f" y="%d" width="%.1f" '
                 'height="%d" fill="%s" fill-opacity="0" stroke="%s" stroke-opacity=".45" '
                 'stroke-width="2"/>' % (d, x, y, bw, BH, t["accent"], t["accent"]))
        p.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="%s" fill="%s" '
                 'text-anchor="middle">%s</text>'
                 % (x + bw / 2, y + BH / 2 + 4, MONO, FS, t["dim"], esc(label)))
        if i < n - 1:
            p.append('<path class="e" d="M%.1f %.1f H%.1f" stroke="%s" stroke-opacity=".6" '
                     'stroke-width="2"/>' % (x + bw + 5, y + BH / 2, x + bw + GAP - 5, t["accent"]))
        x += bw + GAP
    p.append('<text x="%d" y="%d" font-family="%s" font-size="10.5" fill="%s">%s</text>'
             % (left, y + BH + 24, MONO, t["faint"], esc(spec["note"])))

    p.append('<line x1="%d" y1="212" x2="%d" y2="212" stroke="%s" stroke-opacity=".25"/>'
             % (left, W - 70, t["accent"]))
    for i, (val, cap) in enumerate(spec["metrics"]):
        cx = left + i * 208
        p.append('<text x="%d" y="250" font-family="%s" font-size="24" font-weight="800" '
                 'fill="%s" letter-spacing="-.8">%s</text>' % (cx, SANS, t["ink"], esc(val)))
        p.append('<text x="%d" y="266" font-family="%s" font-size="8.6" fill="%s" '
                 'letter-spacing="1.5">%s</text>' % (cx, MONO, t["faint"], esc(cap)))
    # the stack gets its own row. An earlier version right-anchored it on the
    # same baseline as the metric labels and it collided on four cards out of five.
    p.append('<text x="%d" y="288" font-family="%s" font-size="10" fill="%s">%s</text>'
             % (left, MONO, t["dim"], esc(spec["stack"])))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ---------------------------------------------------------------------------
# signals
# ---------------------------------------------------------------------------

LANG_COLOUR = {
    "Python": "#e8a33d", "HTML": "#c1613b", "C++": "#9c6bb0", "JavaScript": "#d9c04a",
    "TypeScript": "#4a89c4", "Java": "#b0764a", "Assembly": "#7a6a4f", "PHP": "#6b6fa8",
    "TeX": "#5d8a5a", "CSS": "#8d6bb0", "Shell": "#7fb069", "Jupyter Notebook": "#d07b3b",
}


def signals(t, s):
    h = 306
    css = ('.sg{animation:in .9s ease-out both}@keyframes in{from{opacity:0}to{opacity:1}}')
    lab = ("%d public repositories, %d stars, %d languages, last shipped %s"
           % (s["repos"], s["stars"], len(s["langs"]), s["pushed"]))
    p = [head(W, h, lab, css)]
    p.append('<rect width="%d" height="%d" fill="%s"/>' % (W, h, t["page"]))

    cells = [(str(s["repos"]), "PUBLIC REPOS"), (str(s["stars"]), "STARS EARNED"),
             (str(len(s["langs"])), "LANGUAGES"), (s["pushed"], "LAST SHIPPED")]
    for i, (big, cap) in enumerate(cells):
        x = 40 + i * 235
        filled = i == 0
        p.append(tile(t, x, 20, 215, 112,
                      fill=t["accent"] if filled else t["tile"],
                      stroke=t["ink"] if filled else t["accent"]))
        col = t["onAccent"] if filled else t["accent"]
        cap_col = t["onAccent"] if filled else t["faint"]
        size = 40 if len(big) <= 4 else 24
        p.append('<g class="sg" style="animation-delay:%ss">' % round(i * 0.1, 2))
        p.append('<text x="%d" y="86" font-family="%s" font-size="%d" font-weight="800" '
                 'fill="%s" letter-spacing="-1.5">%s</text>' % (x + 24, SANS, size, col, esc(big)))
        p.append('<text x="%d" y="108" font-family="%s" font-size="9.4" fill="%s" '
                 'letter-spacing="1.7" opacity="%s">%s</text>'
                 % (x + 24, MONO, cap_col, ".8" if filled else "1", cap))
        p.append("</g>")

    p.append(tile(t, 40, 164, 920, 112))
    p.append('<text x="70" y="196" font-family="%s" font-size="9.6" fill="%s" '
             'letter-spacing="1.9">WHAT THE REPOSITORIES ARE WRITTEN IN</text>'
             % (MONO, t["faint"]))
    total = sum(c for _, c in s["langs"]) or 1
    bx, bw, by, bh = 70, 860, 210, 14
    shown = s["langs"][:6]
    other = sum(c for _, c in s["langs"][6:])
    segs = shown + ([("Other", other)] if other else [])
    x = float(bx)
    for i, (name, count) in enumerate(segs):
        seg = bw * count / total
        p.append('<rect class="sg" style="animation-delay:%ss" x="%.1f" y="%d" width="%.1f" '
                 'height="%d" fill="%s"/>'
                 % (round(0.4 + i * 0.07, 2), x, by, max(seg - 3, 1), bh,
                    LANG_COLOUR.get(name, t["faint"])))
        x += seg
    lx = float(bx)
    for name, count in segs:
        p.append('<rect x="%.1f" y="%d" width="9" height="9" fill="%s"/>'
                 % (lx, by + 26, LANG_COLOUR.get(name, t["faint"])))
        p.append('<text x="%.1f" y="%d" font-family="%s" font-size="10.5" fill="%s">%s %d</text>'
                 % (lx + 15, by + 35, MONO, t["dim"], esc(name), count))
        lx += 30 + mono_w("%s %d" % (name, count), 10.5)
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ---------------------------------------------------------------------------
# sign off
# ---------------------------------------------------------------------------

def signoff(t):
    h = 110
    css = ('.dash{stroke-dasharray:3 7;animation:g 3s linear infinite}'
           '@keyframes g{to{stroke-dashoffset:-10}}')
    p = [head(W, h, "", css)]
    p.append('<rect width="%d" height="%d" fill="%s"/>' % (W, h, t["page"]))
    p.append(tile(t, 40, 20, 920, 56, fill=t["accent"], stroke=t["ink"]))
    p.append('<text x="70" y="55" font-family="%s" font-size="10.5" fill="%s" '
             'letter-spacing="2.2" opacity=".85">EVERY TILE ON THIS PAGE IS DRAWN BY A '
             'SCRIPT IN THIS REPO</text>' % (MONO, t["onAccent"]))
    p.append('<text x="%d" y="55" font-family="%s" font-size="10.5" fill="%s" '
             'letter-spacing="2.2" text-anchor="end">assets/build.py</text>'
             % (W - 70, MONO, t["onAccent"]))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


if __name__ == "__main__":
    s = stats()
    if s:
        print("  stats: %d repos, %d stars, last %s" % (s["repos"], s["stars"], s["pushed"]))
    keep = set()
    for name, t in THEME.items():
        for stem, fn in (("hero", hero), ("principles", principles), ("signoff", signoff)):
            (OUT / ("%s-%s.svg" % (stem, name))).write_text(fn(t), encoding="utf-8")
            keep.add("%s-%s.svg" % (stem, name))
        for key, spec in SYSTEMS.items():
            (OUT / ("sys-%s-%s.svg" % (key, name))).write_text(card(spec, t), encoding="utf-8")
            keep.add("sys-%s-%s.svg" % (key, name))
        f = OUT / ("signals-%s.svg" % name)
        if s is not None:
            f.write_text(signals(t, s), encoding="utf-8")
        keep.add(f.name)

    for old in OUT.glob("*.svg"):
        if old.name not in keep:
            old.unlink()
            print("  removed %s" % old.name)
    for n in sorted(keep):
        print(("  wrote    " if (OUT / n).exists() else "  MISSING  ") + n)
    if s is None:
        print()
        print("  the API did not answer, so signals kept its previous numbers")
