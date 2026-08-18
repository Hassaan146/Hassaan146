"""Draws every piece of art in the profile README.

    python assets/build.py

Design notes, so whoever edits this next knows the rules.

Palette. Almost every profile on GitHub uses #58a6ff on #0d1117, because that is
what the badge and card services default to. This one is warm: amber on
near-black, ink on bone. It reads as chosen rather than inherited.

Weight. The first draft put a designed hero on top of plain markdown, and the
page fell off a cliff the moment the hero ended. Every project now gets a
full-width card carrying its pipeline, four hard numbers and its stack, so the
body holds the same weight as the top.

No badge services. The toolchain used to be 42 separate requests to
img.shields.io, a wall of brand colours that says very little and is the
clearest tell of a template profile. It is one typographic block now.

Animation. CSS keyframes live inside each SVG. GitHub serves the file and the
browser paints it as an image, so the animation survives, the same mechanism the
contribution snake uses. Reduced-motion systems get a still frame.

Themes ship as pairs and <picture> chooses, which follows the GitHub theme
toggle rather than the operating system setting.

Live numbers come from the public API. If it cannot be reached, the affected
card is left exactly as it was, because a card showing yesterday's correct
figures beats one confidently showing invented ones.
"""

import json
import pathlib
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

OUT = pathlib.Path(__file__).parent
sys.path.insert(0, str(OUT))
from artifacts import ARTIFACTS  # noqa: E402

USER = "Hassaan146"

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SANS = "Segoe UI, ui-sans-serif, -apple-system, Helvetica, Arial, sans-serif"

CW = 0.601
REDUCE = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"

THEME = {
    "dark": dict(
        bg="#0a0b0d", rule="#20242b", ink="#eae7e2", dim="#8b867e",
        faint="#5c584f", accent="#e8a33d", accent2="#f6cd85", good="#7fb069",
    ),
    "light": dict(
        bg="#fbfaf8", rule="#e2ddd4", ink="#15171b", dim="#5f5a52",
        faint="#8b857a", accent="#a96a08", accent2="#7d4e05", good="#3f6b2c",
    ),
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def mono_w(text, size):
    return len(text) * size * CW


def head(w, h, label, style=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" '
        f'height="{h}" role="img" aria-label="{esc(label)}">'
        + (f"<style>{style}{REDUCE}</style>" if style else "")
    )


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
    return f"{dt.day} {dt.strftime('%b %Y')}"


def stats():
    try:
        repos = stars = 0
        newest = None
        langs = {}
        for page in range(1, 6):
            batch = _get(f"https://api.github.com/users/{USER}/repos?per_page=100&page={page}")
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
        return {
            "repos": repos, "stars": stars, "pushed": _dmy(when),
            "langs": sorted(langs.items(), key=lambda kv: -kv[1]),
        }
    except (urllib.error.URLError, ValueError, KeyError, TypeError, OSError) as e:
        print(f"  api unreachable ({e}); cards with live numbers left untouched")
        return None


# ---------------------------------------------------------------------------
# hero
# ---------------------------------------------------------------------------

NODES = [(0, 40), (54, 8), (54, 74), (112, 40), (112, 108), (170, 8), (170, 74),
         (226, 40), (226, 108)]
EDGES = [(0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (3, 5), (3, 6), (4, 6),
         (5, 7), (6, 7), (6, 8)]


def hero(t):
    w, h = 1000, 340
    css = (
        ".ln{stroke-dasharray:3 5;animation:flow 2.2s linear infinite}"
        "@keyframes flow{to{stroke-dashoffset:-8}}"
        ".nd{animation:beat 6s ease-in-out infinite}"
        "@keyframes beat{0%,100%{opacity:.42}9%{opacity:1}24%{opacity:.42}}"
    )
    p = [head(w, h, "Muhammad Hassaan-ul-Mustafa, AI engineer, product and backend", css)]
    p.append(f'<rect width="{w}" height="{h}" fill="{t["bg"]}"/>')
    p.append(f'<rect x="30" y="26" width="{w - 60}" height="{h - 52}" fill="none" '
             f'stroke="{t["rule"]}" stroke-width="1"/>')
    p.append(f'<text x="64" y="74" font-family="{MONO}" font-size="10.5" fill="{t["accent"]}" '
             f'letter-spacing="3.4">AI ENGINEER &#183; PRODUCT AND BACKEND</text>')
    p.append(f'<text x="{w - 64}" y="74" font-family="{MONO}" font-size="10.5" '
             f'fill="{t["faint"]}" letter-spacing="2.2" text-anchor="end">ISLAMABAD, PK</text>')
    p.append(f'<text x="60" y="158" font-family="{SANS}" font-size="58" font-weight="700" '
             f'fill="{t["ink"]}" letter-spacing="-2.2">MUHAMMAD</text>')
    p.append(f'<text x="60" y="216" font-family="{SANS}" font-size="58" font-weight="700" '
             f'fill="{t["ink"]}" letter-spacing="-2.2">HASSAAN-UL-MUSTAFA</text>')
    p.append(f'<rect x="64" y="240" width="132" height="3" fill="{t["accent"]}"/>')
    p.append(f'<text x="64" y="278" font-family="{SANS}" font-size="16" fill="{t["dim"]}">'
             f'I build AI agents and the backends they run on.</text>')
    p.append(f'<text x="64" y="308" font-family="{MONO}" font-size="10.5" fill="{t["faint"]}" '
             f'letter-spacing="2">ARBISOFT &#183; FAST-NUCES &#183; OPEN TO REMOTE</text>')
    p.append('<g transform="translate(706,58)">')
    for a, b in EDGES:
        x1, y1 = NODES[a]
        x2, y2 = NODES[b]
        p.append(f'<line class="ln" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                 f'stroke="{t["accent"]}" stroke-opacity=".38" stroke-width="1"/>')
    for i, (x, y) in enumerate(NODES):
        big = i in (3, 6)
        col = t["accent"] if big else t["accent2"]
        p.append(f'<circle class="nd" style="animation-delay:{round(i * 0.62, 2)}s" cx="{x}" '
                 f'cy="{y}" r="{4.6 if big else 3.1}" fill="{col}"/>')
    p.append("</g></svg>")
    return "\n".join(p) + "\n"


# ---------------------------------------------------------------------------
# how I work, three columns under section 00
# ---------------------------------------------------------------------------

PRINCIPLES = [
    ("Guardrails first",
     ["Rate limiting, input validation and row",
      "level security land before the features do."]),
    ("Degrade, do not die",
     ["Every external call has a fallback. Clone",
      "the repo and it runs with zero API keys."]),
    ("Decide before coding",
     ["The architectural choice gets made, and",
      "written down, ahead of the first line."]),
]


def principles(t):
    w, h = 1000, 152
    colw, x0 = 300, 64
    css = (".pc{animation:rise .8s ease-out both}"
           "@keyframes rise{from{opacity:0}to{opacity:1}}")
    lab = " ".join(f"{a}. {' '.join(b)}" for a, b in PRINCIPLES)
    p = [head(w, h, lab, css)]
    p.append(f'<rect width="{w}" height="{h}" fill="{t["bg"]}"/>')
    p.append(f'<line x1="{x0}" y1="18" x2="{w - 64}" y2="18" stroke="{t["rule"]}"/>')
    for i, (title, lines) in enumerate(PRINCIPLES):
        x = x0 + i * (colw + 18)
        p.append(f'<g class="pc" style="animation-delay:{round(i * .12, 2)}s">')
        p.append(f'<rect x="{x}" y="18" width="46" height="2" fill="{t["accent"]}"/>')
        p.append(f'<text x="{x}" y="56" font-family="{MONO}" font-size="13" '
                 f'font-weight="600" fill="{t["ink"]}">{esc(title)}</text>')
        for j, ln in enumerate(lines):
            p.append(f'<text x="{x}" y="{82 + j * 19}" font-family="{SANS}" font-size="12.5" '
                     f'fill="{t["dim"]}">{esc(ln)}</text>')
        p.append("</g>")
    p.append("</svg>")
    return "\n".join(p) + "\n"


# ---------------------------------------------------------------------------
# project cards
# ---------------------------------------------------------------------------

SYSTEMS = {
    "forge": dict(
        headline="A decision gate holding until the architectural choice is made and recorded",
        n="01",
        metrics=[("1,216", "TESTS"), ("100%", "COVERAGE"), ("v1.28", "RELEASE"), ("MIT", "LICENCE")],
        stack="Python 3.12 / MCP / Claude / Git",
    ),
    "news": dict(
        headline="A five item digest assembled from 412 collected items and delivered each morning",
        n="02",
        metrics=[("164", "SITES"), ("36", "CHANNELS"), ("5", "PICKS A DAY"), ("LIVE", "DEPLOYED")],
        stack="React / Vite / FastAPI / PostgreSQL / Groq / Gemini / Stripe",
    ),
    "skyelite": dict(
        headline="A ranked destination with its component scores, its tradeoff and its confidence",
        n="03",
        metrics=[("3rd", "NATIONAL HACKATHON"), ("7", "GRAPH NODES"),
                 ("0", "KEYS TO RUN IT"), ("GCF", "PRODUCTION ADOPTER")],
        stack="Next.js 15 / TypeScript / Three.js / FastAPI / Pydantic v2 / LangGraph / Supabase",
    ),
    "bitmadwall": dict(
        headline="A message relayed phone to phone across a mesh with no network in the path",
        n="04",
        metrics=[("AES-256", "GCM ENCRYPTION"), ("7", "MESH HOPS"),
                 ("0", "SERVERS IN PATH"), ("NO SIM", "CRYPTOGRAPHIC ID")],
        stack="Bluetooth LE / Wi-Fi Direct / LoRa / Signal double ratchet / Bitcoin",
    ),
    "employeeos": dict(
        headline="One plain English request decomposed into a dependency graph of agents",
        n="05",
        metrics=[("1", "MESSY REQUEST"), ("N", "SPECIALIST AGENTS"),
                 ("DAG", "DEPENDENCY AWARE"), ("FULL", "EXECUTION TRACE")],
        stack="Next.js / FastAPI / Pydantic / LangGraph / LangChain / Supabase / Groq",
    ),
}

FS, PAD, GAP, BH = 11.5, 14, 28, 28


def card(key, spec, t):
    """A project block: the thing it produces, then its numbers, then its stack."""
    w = 1000
    css = (
        ".e{stroke-dasharray:2.5 4.5;animation:d 1.6s linear infinite}"
        "@keyframes d{to{stroke-dashoffset:-7}}"
        ".sg{animation:in .9s ease-out both}@keyframes in{from{opacity:0}to{opacity:1}}"
    )
    parts, art_bottom = ARTIFACTS[key](t)

    y = art_bottom + 30
    h = y + 76
    lab = (spec["headline"] + ". "
           + ", ".join(f"{v} {k.lower()}" for v, k in spec["metrics"])
           + ". " + spec["stack"])
    p = [head(w, h, lab, css)]
    p.append(f'<rect width="{w}" height="{h}" fill="{t["bg"]}"/>')
    p.append(f'<line x1="64" y1="1" x2="{w - 64}" y2="1" stroke="{t["rule"]}"/>')
    p.append(f'<text x="{w - 64}" y="16" font-family="{SANS}" font-size="26" '
             f'font-weight="700" fill="{t["accent"]}" opacity=".32" text-anchor="end" '
             f'letter-spacing="-1">{spec["n"]}</text>')
    p += parts

    p.append(f'<line x1="64" y1="{y - 14}" x2="{w - 64}" y2="{y - 14}" stroke="{t["rule"]}"/>')
    for i, (val, lab2) in enumerate(spec["metrics"]):
        cx = 64 + i * 218
        p.append(f'<text x="{cx}" y="{y + 20}" font-family="{SANS}" font-size="21" '
                 f'font-weight="700" fill="{t["ink"]}" letter-spacing="-.6">{esc(val)}</text>')
        p.append(f'<text x="{cx}" y="{y + 37}" font-family="{MONO}" font-size="8.6" '
                 f'fill="{t["faint"]}" letter-spacing="1.5">{esc(lab2)}</text>')
    p.append(f'<text x="64" y="{y + 64}" font-family="{MONO}" font-size="10.5" '
             f'fill="{t["dim"]}">{esc(spec["stack"])}</text>')
    p.append("</svg>")
    return '\n'.join(p) + '\n'


# ---------------------------------------------------------------------------
# toolchain
# ---------------------------------------------------------------------------

TOOLCHAIN = [
    ("LANGUAGES", ["Python", "TypeScript", "JavaScript", "C++", "Java", "SQL", "x86"]),
    ("AI", ["LangGraph", "LangChain", "MCP", "Anthropic", "Groq", "Gemini", "Pydantic"]),
    ("BACKEND", ["FastAPI", "Django", "DRF", "Node", "Express", "Celery"]),
    ("FRONTEND", ["React", "Next.js", "Vite", "Tailwind", "Three.js"]),
    ("DATA", ["PostgreSQL", "Supabase", "MongoDB", "Redis", "MySQL", "SQL Server"]),
    ("SHIP", ["Docker", "Git", "Linux", "Vercel", "Render", "Railway", "Stripe"]),
]


def toolchain(t):
    rowh, top, labx, itemx = 46, 24, 64, 216
    w = 1000
    h = top + rowh * len(TOOLCHAIN) + 26
    lab = "Toolchain. " + " ".join(f"{k}: {', '.join(v)}." for k, v in TOOLCHAIN)
    css = ".r{animation:fade .9s ease-out both}@keyframes fade{from{opacity:0}to{opacity:1}}"
    p = [head(w, h, lab, css)]
    p.append(f'<rect width="{w}" height="{h}" fill="{t["bg"]}"/>')
    for i, (lb, items) in enumerate(TOOLCHAIN):
        y = top + i * rowh
        p.append(f'<line x1="{labx}" y1="{y}" x2="{w - 64}" y2="{y}" stroke="{t["rule"]}"/>')
        p.append(f'<g class="r" style="animation-delay:{round(i * 0.09, 2)}s">')
        p.append(f'<text x="{labx}" y="{y + 29}" font-family="{MONO}" font-size="10" '
                 f'fill="{t["faint"]}" letter-spacing="1.9">{lb}</text>')
        x = float(itemx)
        for j, it in enumerate(items):
            if j:
                p.append(f'<text x="{x:.1f}" y="{y + 29}" font-family="{MONO}" font-size="13" '
                         f'fill="{t["rule"]}">/</text>')
                x += mono_w("/", 13) + 12
            p.append(f'<text x="{x:.1f}" y="{y + 29}" font-family="{MONO}" font-size="13" '
                     f'fill="{t["ink"]}">{esc(it)}</text>')
            x += mono_w(it, 13) + 12
        p.append("</g>")
    yy = top + rowh * len(TOOLCHAIN)
    p.append(f'<line x1="{labx}" y1="{yy}" x2="{w - 64}" y2="{yy}" stroke="{t["rule"]}"/>')
    p.append("</svg>")
    return "\n".join(p) + "\n"


# ---------------------------------------------------------------------------
# signals
# ---------------------------------------------------------------------------

LANG_COLOUR = {
    "Python": "#e8a33d", "HTML": "#c1613b", "C++": "#9c6bb0", "JavaScript": "#d9c04a",
    "TypeScript": "#4a89c4", "Java": "#b0764a", "Assembly": "#7a6a4f", "PHP": "#6b6fa8",
    "TeX": "#5d8a5a", "CSS": "#8d6bb0", "Shell": "#7fb069", "Jupyter Notebook": "#d07b3b",
}

CREDS = [
    ("3rd Place", "National AI Hackathon"),
    ("Production adopter", "Graph Context Framework"),
    ("1,216 tests", "100% coverage, Forge Mentor"),
    ("4 certifications", "Anthropic, Harvard, DeepLearning"),
]


def signals(t, s):
    w, h = 1000, 236
    labx = 64
    css = (".sg{animation:in .8s ease-out both}@keyframes in{from{opacity:0}to{opacity:1}}"
           ".pl{animation:pulse 5s ease-in-out infinite}"
           "@keyframes pulse{0%,100%{opacity:.5}50%{opacity:1}}")
    lab = (f'{s["repos"]} public repositories, {s["stars"]} stars, '
           f'{len(s["langs"])} languages, last shipped {s["pushed"]}')
    p = [head(w, h, lab, css)]
    p.append(f'<rect width="{w}" height="{h}" fill="{t["bg"]}"/>')
    p.append(f'<line x1="{labx}" y1="26" x2="{w - 64}" y2="26" stroke="{t["rule"]}"/>')

    cells = [(str(s["repos"]), "PUBLIC REPOS"), (str(s["stars"]), "STARS EARNED"),
             (str(len(s["langs"])), "LANGUAGES"), (s["pushed"], "LAST SHIPPED")]
    for i, (big, cap) in enumerate(cells):
        cx = labx + i * 234
        size = 34 if len(big) <= 4 else 21
        p.append(f'<g class="sg" style="animation-delay:{round(i * 0.1, 2)}s">')
        p.append(f'<text x="{cx}" y="80" font-family="{SANS}" font-size="{size}" '
                 f'font-weight="700" fill="{t["ink"]}" letter-spacing="-1">{esc(big)}</text>')
        p.append(f'<text x="{cx}" y="100" font-family="{MONO}" font-size="9.4" '
                 f'fill="{t["faint"]}" letter-spacing="1.7">{cap}</text>')
        p.append("</g>")

    total = sum(c for _, c in s["langs"]) or 1
    bx, bw, by, bh = labx, w - 128, 128, 8
    shown = s["langs"][:6]
    other = sum(c for _, c in s["langs"][6:])
    segs = shown + ([("Other", other)] if other else [])
    x = float(bx)
    for i, (name, count) in enumerate(segs):
        seg = bw * count / total
        col = LANG_COLOUR.get(name, t["faint"])
        p.append(f'<rect class="sg" style="animation-delay:{round(0.4 + i * 0.07, 2)}s" '
                 f'x="{x:.1f}" y="{by}" width="{max(seg - 2, 1):.1f}" height="{bh}" '
                 f'fill="{col}"/>')
        x += seg
    lx = float(bx)
    for name, count in segs:
        col = LANG_COLOUR.get(name, t["faint"])
        p.append(f'<rect x="{lx:.1f}" y="{by + 24}" width="7" height="7" fill="{col}"/>')
        p.append(f'<text x="{lx + 13:.1f}" y="{by + 31}" font-family="{MONO}" font-size="10.5" '
                 f'fill="{t["dim"]}">{esc(name)} {count}</text>')
        lx += 26 + mono_w(f"{name} {count}", 10.5)

    p.append(f'<line x1="{labx}" y1="182" x2="{w - 64}" y2="182" stroke="{t["rule"]}"/>')
    for i, (big, small) in enumerate(CREDS):
        cx = labx + i * 234
        p.append(f'<circle class="pl" style="animation-delay:{round(i * 0.8, 2)}s" '
                 f'cx="{cx + 3}" cy="205" r="3" fill="{t["accent"]}"/>')
        p.append(f'<text x="{cx + 14}" y="208" font-family="{MONO}" font-size="11" '
                 f'font-weight="600" fill="{t["ink"]}">{esc(big)}</text>')
        p.append(f'<text x="{cx + 14}" y="222" font-family="{MONO}" font-size="9.2" '
                 f'fill="{t["faint"]}">{esc(small)}</text>')
    p.append("</svg>")
    return "\n".join(p) + "\n"


# ---------------------------------------------------------------------------
# sign off
# ---------------------------------------------------------------------------

def signoff(t):
    w, h = 1000, 96
    css = (".dash{stroke-dasharray:2 6;animation:g 3s linear infinite}"
           "@keyframes g{to{stroke-dashoffset:-8}}")
    p = [head(w, h, "", css)]
    p.append(f'<rect width="{w}" height="{h}" fill="{t["bg"]}"/>')
    p.append(f'<line class="dash" x1="64" y1="34" x2="{w - 64}" y2="34" '
             f'stroke="{t["accent"]}" stroke-opacity=".5"/>')
    p.append(f'<text x="64" y="66" font-family="{MONO}" font-size="10.5" fill="{t["faint"]}" '
             f'letter-spacing="2.2">EVERY MARK ON THIS PAGE WAS DRAWN BY A SCRIPT IN THIS REPO</text>')
    p.append(f'<text x="{w - 64}" y="66" font-family="{MONO}" font-size="10.5" '
             f'fill="{t["accent"]}" letter-spacing="2.2" text-anchor="end">assets/build.py</text>')
    p.append("</svg>")
    return "\n".join(p) + "\n"


if __name__ == "__main__":
    s = stats()
    if s:
        print(f"  stats: {s['repos']} repos, {s['stars']} stars, last {s['pushed']}")
    keep = set()
    for name, t in THEME.items():
        for stem, fn in (("hero", hero), ("principles", principles),
                         ("toolchain", toolchain), ("signoff", signoff)):
            (OUT / f"{stem}-{name}.svg").write_text(fn(t), encoding="utf-8")
            keep.add(f"{stem}-{name}.svg")
        for key, spec in SYSTEMS.items():
            (OUT / f"sys-{key}-{name}.svg").write_text(card(key, spec, t), encoding="utf-8")
            keep.add(f"sys-{key}-{name}.svg")
        f = OUT / f"signals-{name}.svg"
        if s is not None:
            f.write_text(signals(t, s), encoding="utf-8")
        keep.add(f.name)

    for old in OUT.glob("*.svg"):
        if old.name not in keep:
            old.unlink()
            print(f"  removed {old.name}")

    # width guard: nothing may run past the 1000 unit canvas
    import re as _re
    for n in sorted(keep):
        f = OUT / n
        if not f.exists():
            print("  MISSING  " + n)
            continue
        body = f.read_text(encoding="utf-8")
        over = [float(m) for m in _re.findall(r'x="(\d+\.?\d*)"', body) if float(m) > 1000]
        print(f"  wrote    {n}" + (f"   OVERFLOW at x={max(over)}" if over else ""))
    if s is None:
        print("\n  the API did not answer, so signals kept its previous numbers")
