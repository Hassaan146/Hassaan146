"""Draws the art in the profile README.

    python assets/build.py

Style is cyberpunk: a perspective grid horizon, neon cyan and magenta on deep
violet, real gaussian glow rather than a faked one, HUD brackets on every panel,
chromatic aberration on the wordmark, and a scanline sweeping each section.

One file per asset, not a light and dark pair. The design is dark native: every
panel paints its own deep background edge to edge, so it reads the same whichever
GitHub theme the visitor uses, and there is no second palette to keep in sync.

What it emits:

  hero          wordmark, grid horizon, system rings, meta bar
  principles    three panels, how the work gets done
  sys-*         one panel per project: title, meta, pipeline, numbers, stack
  signals       stat panels plus the language mix, from live API data
  signoff       the closing bar

Animation. CSS keyframes live inside each file. GitHub serves it and the browser
paints it as an image, so the animation survives, the same mechanism the
contribution snake uses. Anyone whose system asks for reduced motion gets a
still frame.

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
REDUCE = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"

BG0, BG1 = "#0b0618", "#07040f"
CY, MG, VI = "#22e3ff", "#ff2e88", "#a06bff"
INK, DIM, FAINT = "#eaf2ff", "#9aa4c4", "#5f6684"
PANEL = "#0d0a1c"
NEON = [CY, MG, VI, "#4de3a0", "#ffd166", "#ff7b54", FAINT]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def mono_w(text, size):
    return len(text) * size * CW


DEFS = (
    '<defs>'
    '<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
    '<stop offset="0%%" stop-color="%s"/><stop offset="100%%" stop-color="%s"/>'
    '</linearGradient>'
    '<filter id="gl" x="-40%%" y="-40%%" width="180%%" height="180%%">'
    '<feGaussianBlur stdDeviation="3.2" result="b"/>'
    '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
    '<filter id="gs" x="-60%%" y="-60%%" width="220%%" height="220%%">'
    '<feGaussianBlur stdDeviation="6" result="b"/>'
    '<feMerge><feMergeNode in="b"/><feMergeNode in="b"/>'
    '<feMergeNode in="SourceGraphic"/></feMerge></filter>'
    '</defs>' % (BG0, BG1)
)

CSS_BASE = (
    ".fl{animation:fl 3.4s ease-in-out infinite}"
    "@keyframes fl{0%,100%{opacity:1}47%{opacity:.68}53%{opacity:1}}"
    ".sc{animation:sc 6s linear infinite}"
    "@keyframes sc{to{transform:translateY(760px)}}"
    ".dash{stroke-dasharray:3 6;animation:d 1.5s linear infinite}"
    "@keyframes d{to{stroke-dashoffset:-9}}"
)


def head(h, label, css=""):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" '
            'height="%d" role="img" aria-label="%s">%s<style>%s%s%s</style>'
            % (W, h, W, h, esc(label), DEFS, CSS_BASE, css, REDUCE))


def backdrop(h, grid_from=None):
    p = ['<rect width="%d" height="%d" fill="url(#sky)"/>' % (W, h)]
    if grid_from is not None:
        for i in range(16):
            y = grid_from + i * i * 1.5
            if y > h:
                break
            p.append('<line x1="0" y1="%.0f" x2="%d" y2="%.0f" stroke="%s" stroke-width="1" '
                     'stroke-opacity=".22"/>' % (y, W, y, MG))
        for i in range(-11, 12):
            p.append('<line x1="500" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1" '
                     'stroke-opacity=".16"/>' % (grid_from, 500 + i * 200, h, MG))
        p.append('<line x1="0" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2" '
                 'filter="url(#gl)"/>' % (grid_from, W, grid_from, CY))
    return p


def panel(x, y, w, h, stroke=CY, op=".72"):
    return ('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" fill-opacity="%s" '
            'stroke="%s" stroke-width="1.5" stroke-opacity=".85"/>'
            % (x, y, w, h, PANEL, op, stroke))


def corners(x, y, w, h, col=MG, n=14):
    """Bracket marks at each corner, the HUD cue that carries the style."""
    p = []
    for cx, cy, dx, dy in ((x, y, 1, 1), (x + w, y, -1, 1),
                           (x, y + h, 1, -1), (x + w, y + h, -1, -1)):
        p.append('<path d="M%d %d h%d M%d %d v%d" stroke="%s" stroke-width="2" '
                 'fill="none" stroke-opacity=".9"/>' % (cx, cy, n * dx, cx, cy, n * dy, col))
    return p


def scanline():
    return ('<rect class="sc" x="0" y="-70" width="%d" height="70" fill="%s" '
            'opacity=".045"/>' % (W, CY))


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

def hero():
    h = 420
    css = (".orb{transform-box:view-box;transform-origin:812px 168px;"
           "animation:spin linear infinite}"
           "@keyframes spin{to{transform:rotate(360deg)}}")
    p = [head(h, "Muhammad Hassaan-ul-Mustafa. AI engineer, product and backend. "
                 "I build AI agents and the backends they run on. Arbisoft, FAST-NUCES, "
                 "Islamabad, open to remote.", css)]
    p += backdrop(h, grid_from=300)
    p.append('<circle cx="500" cy="252" r="96" fill="none" stroke="%s" stroke-width="2" '
             'stroke-opacity=".42"/>' % MG)

    p.append('<text class="fl" x="60" y="86" font-family="%s" font-size="12" fill="%s" '
             'letter-spacing="4.4" filter="url(#gl)">&gt;&gt; AI ENGINEER / PRODUCT AND '
             'BACKEND _</text>' % (MONO, CY))
    # chromatic split: two offset copies behind the white one
    for dx, col, op in ((-3, MG, ".8"), (3, CY, ".8"), (0, INK, "1")):
        p.append('<text x="%d" y="164" font-family="%s" font-size="54" font-weight="800" '
                 'fill="%s" opacity="%s" letter-spacing="-2">MUHAMMAD</text>'
                 % (60 + dx, SANS, col, op))
        p.append('<text x="%d" y="220" font-family="%s" font-size="54" font-weight="800" '
                 'fill="%s" opacity="%s" letter-spacing="-2">HASSAAN</text>'
                 % (60 + dx, SANS, col, op))
    p.append('<rect x="60" y="240" width="140" height="4" fill="%s" filter="url(#gl)"/>' % MG)
    p.append('<text x="60" y="284" font-family="%s" font-size="15" fill="%s">'
             'I build AI agents and the backends they run on.</text>' % (MONO, DIM))

    for i, (r, dur) in enumerate(((28, 13), (48, 21), (68, 34))):
        p.append('<circle cx="812" cy="168" r="%d" fill="none" stroke="%s" stroke-width="1.5" '
                 'stroke-opacity=".4"/>' % (r, CY if i % 2 == 0 else VI))
        p.append('<g class="orb" style="animation-duration:%ss%s">'
                 % (dur, ";animation-direction:reverse" if i == 1 else ""))
        for k in range(i + 1):
            ang = 2 * math.pi * k / (i + 1)
            p.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" filter="url(#gl)"/>'
                     % (812 + r * math.cos(ang), 168 + r * math.sin(ang),
                        5 - i * 0.6, MG if k % 2 else CY))
        p.append("</g>")
    p.append('<circle cx="812" cy="168" r="11" fill="%s" filter="url(#gs)"/>' % CY)
    p.append('<text x="812" y="266" font-family="%s" font-size="9.6" fill="%s" '
             'letter-spacing="2" text-anchor="middle">DATA / API / AGENTS</text>' % (MONO, FAINT))

    p.append(panel(60, 336, 880, 54))
    p += corners(60, 336, 880, 54)
    p.append('<text x="82" y="369" font-family="%s" font-size="10.5" fill="%s" '
             'letter-spacing="2.4">ARBISOFT / FAST-NUCES / ISLAMABAD / OPEN TO REMOTE</text>'
             % (MONO, CY))
    p.append(scanline())
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


def principles():
    h = 186
    colw, gap = 293, 20
    lab = ". ".join("%s. %s" % (n, " ".join(b)) for _, n, b in PRINCIPLES)
    p = [head(h, lab)]
    p += backdrop(h)
    for i, (num, title, lines) in enumerate(PRINCIPLES):
        x = 40 + i * (colw + gap)
        col = (CY, MG, VI)[i]
        p.append(panel(x, 20, colw, 132, stroke=col))
        p += corners(x, 20, colw, 132, col=col, n=11)
        p.append('<text x="%d" y="58" font-family="%s" font-size="11" fill="%s" '
                 'font-weight="700" filter="url(#gl)">%s</text>' % (x + 22, MONO, col, num))
        p.append('<text x="%d" y="90" font-family="%s" font-size="15" font-weight="800" '
                 'fill="%s">%s</text>' % (x + 22, SANS, INK, title))
        for j, ln in enumerate(lines):
            p.append('<text x="%d" y="%d" font-family="%s" font-size="11" fill="%s">%s</text>'
                     % (x + 22, 114 + j * 16, MONO, DIM, esc(ln)))
    p.append(scanline())
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ---------------------------------------------------------------------------
# project panels
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


def card(spec):
    h = 328
    left = 82
    nodes = spec["nodes"]
    n = len(nodes)
    widths = [mono_w(x, FS) + PAD * 2 for x in nodes]
    lab = ("%s. %s. %s. %s. %s" % (
        spec["title"], spec["meta"], " then ".join(nodes),
        ", ".join("%s %s" % (v, k.lower()) for v, k in spec["metrics"]), spec["stack"]))
    p = [head(h, lab)]
    p += backdrop(h)
    p.append(panel(40, 20, 920, 280))
    p += corners(40, 20, 920, 280)

    p.append('<text x="%d" y="74" font-family="%s" font-size="30" font-weight="800" '
             'fill="%s" letter-spacing="-1">%s</text>' % (left, SANS, INK, esc(spec["title"])))
    p.append('<text x="%d" y="74" font-family="%s" font-size="34" font-weight="800" '
             'fill="%s" opacity=".5" text-anchor="end" filter="url(#gl)">%s</text>'
             % (W - 82, SANS, MG, spec["n"]))
    p.append('<text x="%d" y="96" font-family="%s" font-size="9.6" fill="%s" '
             'letter-spacing="1.9">%s</text>' % (left, MONO, CY, esc(spec["meta"])))
    p.append('<rect x="%d" y="110" width="44" height="3" fill="%s" filter="url(#gl)"/>'
             % (left, MG))

    y = 134
    x = float(left)
    for i, (label, bw) in enumerate(zip(nodes, widths)):
        col = CY if i % 2 == 0 else VI
        p.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s" fill-opacity=".5" '
                 'stroke="%s" stroke-width="1.4" stroke-opacity=".8"/>'
                 % (x, y, bw, BH, PANEL, col))
        p.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="%s" fill="%s" '
                 'text-anchor="middle">%s</text>'
                 % (x + bw / 2, y + BH / 2 + 4, MONO, FS, DIM, esc(label)))
        if i < n - 1:
            p.append('<path class="dash" d="M%.1f %.1f H%.1f" stroke="%s" stroke-width="1.6" '
                     'stroke-opacity=".8"/>' % (x + bw + 5, y + BH / 2, x + bw + GAP - 5, MG))
        x += bw + GAP
    p.append('<text x="%d" y="%d" font-family="%s" font-size="10.5" fill="%s">%s</text>'
             % (left, y + BH + 24, MONO, FAINT, esc(spec["note"])))

    p.append('<line x1="%d" y1="214" x2="%d" y2="214" stroke="%s" stroke-opacity=".35"/>'
             % (left, W - 82, CY))
    for i, (val, cap) in enumerate(spec["metrics"]):
        cx = left + i * 204
        p.append('<text x="%d" y="252" font-family="%s" font-size="24" font-weight="800" '
                 'fill="%s" letter-spacing="-.6" filter="url(#gl)">%s</text>'
                 % (cx, SANS, CY, esc(val)))
        p.append('<text x="%d" y="268" font-family="%s" font-size="8.6" fill="%s" '
                 'letter-spacing="1.5">%s</text>' % (cx, MONO, FAINT, esc(cap)))
    # the stack keeps its own row. Sharing a baseline with the metric labels
    # overlapped on four cards out of five when it was tried.
    p.append('<text x="%d" y="288" font-family="%s" font-size="10" fill="%s">%s</text>'
             % (left, MONO, DIM, esc(spec["stack"])))
    p.append(scanline())
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ---------------------------------------------------------------------------
# signals
# ---------------------------------------------------------------------------

def signals(s):
    h = 306
    lab = ("%d public repositories, %d stars, %d languages, last shipped %s"
           % (s["repos"], s["stars"], len(s["langs"]), s["pushed"]))
    p = [head(h, lab)]
    p += backdrop(h)
    cells = [(str(s["repos"]), "PUBLIC REPOS"), (str(s["stars"]), "STARS EARNED"),
             (str(len(s["langs"])), "LANGUAGES"), (s["pushed"], "LAST SHIPPED")]
    for i, (big, cap) in enumerate(cells):
        x = 40 + i * 235
        col = (CY, MG, VI, CY)[i]
        p.append(panel(x, 20, 215, 112, stroke=col))
        p += corners(x, 20, 215, 112, col=col, n=10)
        size = 40 if len(big) <= 4 else 24
        p.append('<text x="%d" y="88" font-family="%s" font-size="%d" font-weight="800" '
                 'fill="%s" letter-spacing="-1.4" filter="url(#gl)">%s</text>'
                 % (x + 22, SANS, size, col, esc(big)))
        p.append('<text x="%d" y="110" font-family="%s" font-size="9.4" fill="%s" '
                 'letter-spacing="1.7">%s</text>' % (x + 22, MONO, FAINT, cap))

    p.append(panel(40, 164, 920, 112))
    p += corners(40, 164, 920, 112)
    p.append('<text x="70" y="196" font-family="%s" font-size="9.6" fill="%s" '
             'letter-spacing="1.9">WHAT THE REPOSITORIES ARE WRITTEN IN</text>' % (MONO, CY))
    total = sum(c for _, c in s["langs"]) or 1
    bx, bw, by, bh = 70, 860, 210, 14
    shown = s["langs"][:6]
    other = sum(c for _, c in s["langs"][6:])
    segs = shown + ([("Other", other)] if other else [])
    x = float(bx)
    for i, (name, count) in enumerate(segs):
        seg = bw * count / total
        p.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s" '
                 'filter="url(#gl)"/>' % (x, by, max(seg - 3, 1), bh, NEON[i % len(NEON)]))
        x += seg
    lx = float(bx)
    for i, (name, count) in enumerate(segs):
        p.append('<rect x="%.1f" y="%d" width="9" height="9" fill="%s"/>'
                 % (lx, by + 26, NEON[i % len(NEON)]))
        p.append('<text x="%.1f" y="%d" font-family="%s" font-size="10.5" fill="%s">%s %d</text>'
                 % (lx + 15, by + 35, MONO, DIM, esc(name), count))
        lx += 30 + mono_w("%s %d" % (name, count), 10.5)
    p.append(scanline())
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ---------------------------------------------------------------------------
# sign off
# ---------------------------------------------------------------------------

def signoff():
    h = 110
    p = [head(h, "")]
    p += backdrop(h)
    p.append(panel(40, 20, 920, 56, stroke=MG))
    p += corners(40, 20, 920, 56, col=CY)
    p.append('<text class="fl" x="70" y="54" font-family="%s" font-size="10.5" fill="%s" '
             'letter-spacing="2.2">EVERY PANEL ON THIS PAGE IS DRAWN BY A SCRIPT IN THIS '
             'REPO</text>' % (MONO, CY))
    p.append('<text x="%d" y="54" font-family="%s" font-size="10.5" fill="%s" '
             'letter-spacing="2.2" text-anchor="end">assets/build.py</text>'
             % (W - 70, MONO, MG))
    p.append(scanline())
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


if __name__ == "__main__":
    s = stats()
    if s:
        print("  stats: %d repos, %d stars, last %s" % (s["repos"], s["stars"], s["pushed"]))
    keep = set()
    for stem, fn in (("hero", hero), ("principles", principles), ("signoff", signoff)):
        (OUT / ("%s.svg" % stem)).write_text(fn(), encoding="utf-8")
        keep.add("%s.svg" % stem)
    for key, spec in SYSTEMS.items():
        (OUT / ("sys-%s.svg" % key)).write_text(card(spec), encoding="utf-8")
        keep.add("sys-%s.svg" % key)
    f = OUT / "signals.svg"
    if s is not None:
        f.write_text(signals(s), encoding="utf-8")
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
