"""Cyberpunk.

A perspective grid horizon, neon cyan and magenta on deep violet, real gaussian
glow through feGaussianBlur rather than a faked one, HUD brackets on every
panel, chromatic aberration on the wordmark, and a scanline sweeping each
section.

The chromatic split draws the wordmark three times, offset by a few pixels in
magenta and cyan behind white. The geometry check in build.py knows to ignore
identical text on one baseline, which is why that reads as clean.
"""

from build import (BH, CW, FS, GAP, MONO, PAD, PRINCIPLES, REDUCE, SANS, W,
                   esc, mono_w)

import math

BG0, BG1 = "#0b0618", "#07040f"
CY, MG, VI = "#22e3ff", "#ff2e88", "#a06bff"
INK, DIM, FAINT = "#eaf2ff", "#9aa4c4", "#5f6684"
PANEL = "#0d0a1c"
NEON = [CY, MG, VI, "#4de3a0", "#ffd166", "#ff7b54", FAINT]




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
