"""Generates every piece of SVG art in this README.

    python assets/build_svg.py

Output:
    banner-{dark,light}.svg   the header
    about-{dark,light}.svg    the spec card, with counts pulled live from the API
    flow-*.svg                one pipeline strip per featured project

The art is animated. GitHub serves these files through its image proxy and the
browser renders them as images, so CSS keyframes inside the file survive, which
is the same trick the contribution snake uses. Anyone who has asked their OS for
less motion gets a still image instead.

Flow strips are a single file each. They carry no background of their own and
pick colours from a media query, so one file covers both GitHub themes. The
banner and the spec card are painted panels, so those ship as a pair and get
selected with <picture> in the README, which follows the GitHub theme toggle
rather than the OS setting.

Counts come from the public API and need no token. If the network is unavailable
the last known values below are used, so a build never fails and never writes a
half-empty card.
"""

import json
import pathlib
import urllib.error
import urllib.request
from datetime import datetime, timezone

OUT = pathlib.Path(__file__).parent
USER = "Hassaan146"

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

# used when the API cannot be reached
FALLBACK = {"repos": 38, "stars": 26, "pushed": "17 Aug 2026"}

REDUCE = (
    "@media (prefers-reduced-motion: reduce){*{animation:none!important}}"
)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ---------------------------------------------------------------------------
# live numbers
# ---------------------------------------------------------------------------

def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "readme-build"})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.load(r)


def stats():
    try:
        repos, stars, newest = 0, 0, None
        page = 1
        while True:
            batch = _get(f"https://api.github.com/users/{USER}/repos?per_page=100&page={page}")
            if not batch:
                break
            for r in batch:
                if r.get("fork"):
                    continue
                repos += 1
                stars += r.get("stargazers_count", 0)
                ts = r.get("pushed_at")
                if ts and (newest is None or ts > newest):
                    newest = ts
            page += 1
            if page > 5:
                break
        when = datetime.strptime(newest, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        return {"repos": repos, "stars": stars, "pushed": when.strftime("%-d %b %Y")}
    except (urllib.error.URLError, ValueError, KeyError, TypeError, OSError):
        try:
            # %-d is not portable to Windows; retry with the platform variant
            when = datetime.strptime(newest, "%Y-%m-%dT%H:%M:%SZ")
            return {"repos": repos, "stars": stars, "pushed": when.strftime("%#d %b %Y")}
        except Exception:
            return dict(FALLBACK)


# ---------------------------------------------------------------------------
# pipeline strips
# ---------------------------------------------------------------------------

FLOWS = {
    "forge": dict(
        nodes=["question", "options", "you decide", "recorded", "code runs"],
        note="the gate holds until the decision exists",
    ),
    "news": dict(
        nodes=["scrape", "store", "rank", "summarise", "email"],
        note="164 sites and 36 YouTube channels  ·  top 5 per user, daily",
    ),
    "skyelite": dict(
        nodes=["intake", "filter", "visa", "research", "scoring", "tradeoff", "final"],
        note="LangGraph StateGraph  ·  7 nodes  ·  every call has a mock fallback",
    ),
    "bitmadwall": dict(
        nodes=["your phone", "relay", "relay", "recipient"],
        note="Bluetooth LE / Wi-Fi Direct / LoRa  ·  up to 7 hops  ·  no server anywhere",
    ),
    "employeeos": dict(
        nodes=["request", "decompose", "route to agents", "validate", "trace"],
        note="dependency-aware workflow, execution trace shown back to you",
    ),
}

FS = 11.5          # node label size
CW = FS * 0.605    # monospace advance
PAD = 13
GAP = 26
H = 27

# Every colour is written out in full. No CSS custom properties, no colour media
# queries: presentation attributes cannot read var(), and keeping the stylesheet
# down to keyframes alone is the most compatible thing to hand a proxy. Themes
# are handled by shipping a pair and letting <picture> choose.
FLOW_THEME = {
    "dark": dict(edge="#58a6ff", txt="#8b949e", hot="#79c0ff"),
    "light": dict(edge="#0969da", txt="#57606a", hot="#0550ae"),
}


def flow_svg(nodes, note, c):
    widths = [len(n) * CW + PAD * 2 for n in nodes]
    w = int(sum(widths) + GAP * (len(nodes) - 1)) + 4
    h, y = 74, 20
    n = len(nodes)
    dur = max(5.0, n * 1.15)

    css = (
        f".e{{animation:d 1.4s linear infinite}}"
        f"@keyframes d{{to{{stroke-dashoffset:-8}}}}"
        f".b{{animation:s {dur}s ease-in-out infinite}}"
        "@keyframes s{0%{stroke-opacity:.42;fill-opacity:0}"
        "7%{stroke-opacity:1;fill-opacity:.14}"
        "20%{stroke-opacity:.42;fill-opacity:0}"
        "100%{stroke-opacity:.42;fill-opacity:0}}"
        f".t{{animation:tt {dur}s ease-in-out infinite}}"
        f"@keyframes tt{{0%{{fill:{c['txt']}}}7%{{fill:{c['hot']}}}"
        f"20%{{fill:{c['txt']}}}100%{{fill:{c['txt']}}}}}"
        + REDUCE
    )

    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" '
        f'height="{h}" role="img" aria-label="{esc(" then ".join(nodes))}">',
        "<style>" + css + "</style>",
        '<defs><marker id="a" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" '
        f'markerHeight="6" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="{c["edge"]}" '
        'fill-opacity=".6"/></marker></defs>',
    ]

    x = 2.0
    for i, (label, bw) in enumerate(zip(nodes, widths)):
        delay = round(i * dur / n, 2)
        p.append(
            f'<rect class="b" style="animation-delay:{delay}s" x="{x:.1f}" y="{y}" '
            f'width="{bw:.1f}" height="{H}" rx="6" fill="{c["edge"]}" fill-opacity="0" '
            f'stroke="{c["edge"]}" stroke-opacity=".42" stroke-width="1.1"/>'
        )
        p.append(
            f'<text class="t" style="animation-delay:{delay}s" x="{x + bw / 2:.1f}" '
            f'y="{y + H / 2 + 4:.1f}" font-family="{MONO}" font-size="{FS}" '
            f'fill="{c["txt"]}" text-anchor="middle">{esc(label)}</text>'
        )
        if i < n - 1:
            p.append(
                f'<path class="e" d="M{x + bw + 5:.1f} {y + H / 2:.1f} '
                f'H{x + bw + GAP - 5:.1f}" fill="none" stroke="{c["edge"]}" '
                f'stroke-opacity=".5" stroke-width="1.3" stroke-dasharray="3 5" '
                f'marker-end="url(#a)"/>'
            )
        x += bw + GAP

    p.append(
        f'<text x="3" y="{y + H + 20}" font-family="{MONO}" font-size="10.5" '
        f'fill="{c["txt"]}" fill-opacity=".85">{esc(note)}</text>'
    )
    p.append("</svg>")
    return "\n".join(p) + "\n"


# ---------------------------------------------------------------------------
# spec card
# ---------------------------------------------------------------------------

ROWS = [
    ("name", "Muhammad Hassaan-ul-Mustafa"),
    ("role", "AI engineer, product and backend"),
    ("study", "BS Computer Science, FAST-NUCES (2024 to 2028)"),
    ("now", "Arbisoft"),
    ("based", "Islamabad, Pakistan, open to remote"),
]

LAYERS = ["agent graph", "api + guardrails", "data + auth"]

THEMES = {
    "dark": dict(panel="#11161f", line="#232c38", key="#58a6ff", val="#c9d1d9",
                 dim="#6e7681", accent="#58a6ff"),
    "light": dict(panel="#f6f8fa", line="#d8dee4", key="#0969da", val="#1f2328",
                  dim="#6e7781", accent="#0969da"),
}


def about_svg(t, s):
    w, h = 880, 208
    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" '
        f'height="{h}" role="img" aria-label="About Muhammad Hassaan-ul-Mustafa">',
        "<style>"
        f'.l{{animation:g 4.5s ease-in-out infinite}}'
        "@keyframes g{0%,100%{fill-opacity:.05;stroke-opacity:.35}"
        "40%{fill-opacity:.17;stroke-opacity:.85}}"
        ".dot{animation:blink 2.6s ease-in-out infinite}"
        "@keyframes blink{0%,100%{opacity:1}50%{opacity:.35}}"
        + REDUCE +
        "</style>",
        f'<rect width="{w}" height="{h}" rx="10" fill="{t["panel"]}" stroke="{t["line"]}"/>',
        f'<rect x="0" y="0" width="3.5" height="{h}" rx="2" fill="{t["accent"]}"/>',
    ]

    y = 42
    for k, v in ROWS:
        p.append(f'<text x="30" y="{y}" font-family="{MONO}" font-size="12.5" '
                 f'fill="{t["key"]}">{k}</text>')
        p.append(f'<text x="112" y="{y}" font-family="{MONO}" font-size="12.5" '
                 f'fill="{t["val"]}">{esc(v)}</text>')
        y += 27

    bx, by = 618, 34
    p.append(f'<text x="{bx}" y="{by - 10}" font-family="{MONO}" font-size="9.5" '
             f'fill="{t["dim"]}" letter-spacing="1.3">WHAT I ACTUALLY BUILD</text>')
    for i, label in enumerate(LAYERS):
        yy = by + i * 36
        p.append(
            f'<rect class="l" style="animation-delay:{i * 0.5}s" x="{bx}" y="{yy}" '
            f'width="228" height="28" rx="6" fill="{t["accent"]}" '
            f'stroke="{t["accent"]}" stroke-width="1.2"/>'
        )
        p.append(f'<text x="{bx + 14}" y="{yy + 18.5}" font-family="{MONO}" '
                 f'font-size="11.5" fill="{t["val"]}">{esc(label)}</text>')
        if i < len(LAYERS) - 1:
            p.append(f'<path d="M{bx + 114} {yy + 28} V{yy + 36}" stroke="{t["accent"]}" '
                     f'stroke-opacity=".45" stroke-width="1.2"/>')

    p.append(f'<circle class="dot" cx="35" cy="{h - 24}" r="4" fill="#3fb950"/>')
    p.append(f'<text x="47" y="{h - 20}" font-family="{MONO}" font-size="11" '
             f'fill="{t["dim"]}">open to contract work and startup collaborations</text>')

    line = f'{s["repos"]} repos   {s["stars"]} stars   last shipped {s["pushed"]}'
    p.append(f'<text x="{w - 28}" y="{h - 20}" font-family="{MONO}" font-size="10.5" '
             f'fill="{t["dim"]}" text-anchor="end">{esc(line)}</text>')
    p.append("</svg>")
    return "\n".join(p) + "\n"


# ---------------------------------------------------------------------------
# banner
# ---------------------------------------------------------------------------

BANNER_NODES = 7
BN_GAP = 46


def banner_svg(theme):
    dark = theme == "dark"
    bg = ("#0d1117", "#0f1621", "#111d2e") if dark else ("#ffffff", "#f6f8fa", "#eaf2fb")
    acc = "#58a6ff" if dark else "#0969da"
    acc2 = "#1f6feb" if dark else "#54aeff"
    name = "#e6edf3" if dark else "#1f2328"
    sub = "#8b949e" if dark else "#57606a"
    dim = "#6e7681" if dark else "#6e7781"
    hole = "#0d1117" if dark else "#ffffff"
    w, h = 1000, 220
    dur = 7.0

    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" '
        f'height="{h}" role="img" aria-label="Muhammad Hassaan-ul-Mustafa, AI engineer">',
        "<style>"
        ".e{stroke-dasharray:4 6;animation:d 1.6s linear infinite}"
        "@keyframes d{to{stroke-dashoffset:-10}}"
        f".n{{animation:s {dur}s ease-in-out infinite}}"
        "@keyframes s{0%{r:8.5;stroke-opacity:.75}6%{r:10.5;stroke-opacity:1}"
        "18%{r:8.5;stroke-opacity:.75}100%{r:8.5;stroke-opacity:.75}}"
        + REDUCE +
        "</style>",
        "<defs>",
        f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0%" stop-color="{bg[0]}"/><stop offset="55%" stop-color="{bg[1]}"/>'
        f'<stop offset="100%" stop-color="{bg[2]}"/></linearGradient>',
        f'<linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0%" stop-color="{acc}"/>'
        f'<stop offset="100%" stop-color="{acc}" stop-opacity="0"/></linearGradient>',
        f'<pattern id="grid" width="26" height="26" patternUnits="userSpaceOnUse">'
        f'<path d="M26 0H0V26" fill="none" stroke="{acc}" stroke-opacity=".05"/></pattern>',
        f'<radialGradient id="glow"><stop offset="0%" stop-color="{acc}" stop-opacity=".26"/>'
        f'<stop offset="100%" stop-color="{acc}" stop-opacity="0"/></radialGradient>',
        "</defs>",
        f'<rect width="{w}" height="{h}" fill="url(#bg)"/>',
        f'<rect width="{w}" height="{h}" fill="url(#grid)"/>',
        f'<ellipse cx="810" cy="110" rx="230" ry="150" fill="url(#glow)"/>',
        f'<rect x="0" y="0" width="4" height="{h}" fill="{acc}"/>',
        f'<text x="56" y="86" font-family="ui-sans-serif, -apple-system, \'Segoe UI\', '
        f'Helvetica, Arial, sans-serif" font-size="40" font-weight="700" fill="{name}" '
        f'letter-spacing="-0.8">Muhammad Hassaan-ul-Mustafa</text>',
        f'<rect x="57" y="104" width="360" height="2" fill="url(#rule)"/>',
        f'<text x="56" y="139" font-family="{MONO}" font-size="16.5" font-weight="600" '
        f'fill="{acc}" letter-spacing="2.4">AI ENGINEER, PRODUCT AND BACKEND</text>',
        f'<text x="56" y="171" font-family="ui-sans-serif, -apple-system, \'Segoe UI\', '
        f'Helvetica, Arial, sans-serif" font-size="14.5" fill="{sub}">'
        f'Building AI agents that reach production.</text>',
        f'<text x="56" y="196" font-family="{MONO}" font-size="12" fill="{dim}" '
        f'letter-spacing="1.1">ARBISOFT &#183; FAST-NUCES &#183; ISLAMABAD</text>',
    ]

    p.append('<g transform="translate(648,110)">')
    span = BN_GAP * (BANNER_NODES - 1)
    for i in range(BANNER_NODES - 1):
        p.append(f'<path class="e" d="M{i * BN_GAP} 0 H{(i + 1) * BN_GAP}" '
                 f'stroke="{acc}" stroke-opacity=".6" stroke-width="1.6"/>')
    p.append(f'<path d="M{BN_GAP} 0 C {BN_GAP + 24} -42, {3 * BN_GAP - 24} -42, {3 * BN_GAP} 0" '
             f'fill="none" stroke="{acc}" stroke-opacity=".32" stroke-width="1.3" '
             f'stroke-dasharray="3 4"/>')
    p.append(f'<path d="M{3 * BN_GAP} 0 C {3 * BN_GAP + 24} 42, {5 * BN_GAP - 24} 42, '
             f'{5 * BN_GAP} 0" fill="none" stroke="{acc}" stroke-opacity=".32" '
             f'stroke-width="1.3" stroke-dasharray="3 4"/>')
    for i in range(BANNER_NODES):
        fill = acc if i == 3 else (acc2 if i in (2, 4) else hole)
        p.append(f'<circle class="n" style="animation-delay:{round(i * dur / BANNER_NODES, 2)}s" '
                 f'cx="{i * BN_GAP}" cy="0" r="8.5" fill="{fill}" stroke="{acc}" '
                 f'stroke-width="2"/>')
    p.append(f'<text x="-4" y="34" font-family="{MONO}" font-size="9.5" fill="{dim}" '
             f'letter-spacing="1.4">STATEGRAPH &#183; 7 NODES</text>')
    p.append("</g>")
    p.append("</svg>")
    _ = span
    return "\n".join(p) + "\n"


if __name__ == "__main__":
    s = stats()
    print(f"stats: {s}")
    made = set()
    for name, spec in FLOWS.items():
        for theme, c in FLOW_THEME.items():
            f = OUT / f"flow-{name}-{theme}.svg"
            f.write_text(flow_svg(spec["nodes"], spec["note"], c), encoding="utf-8")
            made.add(f.name)
    for theme, t in THEMES.items():
        (OUT / f"about-{theme}.svg").write_text(about_svg(t, s), encoding="utf-8")
        (OUT / f"banner-{theme}.svg").write_text(banner_svg(theme), encoding="utf-8")
        made |= {f"about-{theme}.svg", f"banner-{theme}.svg"}

    # anything left over from an earlier shape of this file
    for old in OUT.glob("*.svg"):
        if old.name not in made:
            old.unlink()
            print(f"removed stale {old.name}")

    print("\n".join(sorted(made)))
