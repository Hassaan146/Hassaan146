"""Glassmorphism.

Frosted translucent panels sitting over blurred colour that drifts slowly
underneath. The blur is a real feGaussianBlur on the colour blobs, not a faked
gradient, which is what makes the panels read as glass rather than as flat
rectangles with low opacity.

Rounded corners, hairline white borders at low alpha, and a cool palette, since
warm glass tends to look like amber plastic.
"""

import math

from build import (BH, CW, FS, GAP, MONO, PAD, PRINCIPLES, REDUCE, SANS, W,
                   esc, mono_w)

BG0, BG1, BG2 = "#141826", "#1d1630", "#0e1018"
ACC, ACC2 = "#8ea2ff", "#5ee0c8"
WARM = "#ffb572"
INK, DIM, FAINT = "#f2f4fb", "#b9c0d4", "#7d849b"

DEFS = (
    '<defs>'
    '<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0%%" stop-color="%s"/><stop offset="55%%" stop-color="%s"/>'
    '<stop offset="100%%" stop-color="%s"/></linearGradient>'
    '<filter id="soft" x="-70%%" y="-70%%" width="240%%" height="240%%">'
    '<feGaussianBlur stdDeviation="46"/></filter>'
    '<linearGradient id="frost" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0%%" stop-color="#ffffff" stop-opacity=".14"/>'
    '<stop offset="100%%" stop-color="#ffffff" stop-opacity=".035"/></linearGradient>'
    '<linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0%%" stop-color="#ffffff" stop-opacity=".38"/>'
    '<stop offset="60%%" stop-color="#ffffff" stop-opacity=".1"/></linearGradient>'
    '</defs>' % (BG0, BG1, BG2)
)

CSS = (
    ".dr{animation:dr 14s ease-in-out infinite}"
    "@keyframes dr{0%,100%{transform:translate(0,0)}50%{transform:translate(26px,-18px)}}"
    ".dr2{animation:dr2 18s ease-in-out infinite}"
    "@keyframes dr2{0%,100%{transform:translate(0,0)}50%{transform:translate(-22px,16px)}}"
    ".sh{animation:sh 7s ease-in-out infinite}"
    "@keyframes sh{0%,100%{opacity:.5}50%{opacity:1}}"
    ".dash{stroke-dasharray:3 6;animation:d 1.7s linear infinite}"
    "@keyframes d{to{stroke-dashoffset:-9}}"
)


def head(h, label, extra=""):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" '
            'height="%d" role="img" aria-label="%s">%s<style>%s%s%s</style>'
            % (W, h, W, h, esc(label), DEFS, CSS, extra, REDUCE))


def backdrop(h, blobs=None):
    p = ['<rect width="%d" height="%d" fill="url(#bg)"/>' % (W, h)]
    blobs = blobs or [(230, h * 0.32, 120, ACC, ".5", "dr"),
                      (770, h * 0.62, 140, WARM, ".34", "dr2"),
                      (520, h * 0.9, 110, ACC2, ".3", "dr")]
    p.append('<g filter="url(#soft)">')
    for cx, cy, r, col, op, cls in blobs:
        p.append('<circle class="%s" cx="%.0f" cy="%.0f" r="%d" fill="%s" opacity="%s"/>'
                 % (cls, cx, cy, r, col, op))
    p.append("</g>")
    return p


def panel(x, y, w, h, r=18):
    return ('<rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="url(#frost)" '
            'stroke="url(#edge)" stroke-width="1.3"/>' % (x, y, w, h, r))


# ------------------------------------------------------------------- hero

def hero():
    h = 420
    extra = (".orb{transform-box:view-box;transform-origin:812px 150px;"
             "animation:spin linear infinite}"
             "@keyframes spin{to{transform:rotate(360deg)}}")
    p = [head(h, "Muhammad Hassaan-ul-Mustafa. AI engineer, product and backend. "
                 "I build AI agents and the backends they run on. Arbisoft, FAST-NUCES, "
                 "Islamabad, open to remote.", extra)]
    p += backdrop(h, [(220, 130, 130, ACC, ".55", "dr"),
                      (780, 250, 150, WARM, ".32", "dr2"),
                      (480, 400, 120, ACC2, ".3", "dr")])

    p.append(panel(50, 44, 600, 224, 22))
    p.append('<text x="82" y="94" font-family="%s" font-size="11" fill="%s" '
             'letter-spacing="3.2">AI ENGINEER / PRODUCT AND BACKEND</text>' % (MONO, ACC2))
    p.append('<text x="82" y="158" font-family="%s" font-size="46" font-weight="700" '
             'fill="%s" letter-spacing="-1.8">Muhammad</text>' % (SANS, INK))
    p.append('<text x="82" y="208" font-family="%s" font-size="46" font-weight="700" '
             'fill="%s" letter-spacing="-1.8">Hassaan-ul-Mustafa</text>' % (SANS, ACC))
    p.append('<rect x="82" y="230" width="120" height="4" rx="2" fill="%s"/>' % ACC2)

    p.append(panel(668, 44, 282, 224, 22))
    p.append('<text x="694" y="82" font-family="%s" font-size="9.6" fill="%s" '
             'letter-spacing="2.4">THE SHAPE OF THE WORK</text>' % (MONO, FAINT))
    for i, (r, dur) in enumerate(((30, 13), (52, 21), (74, 34))):
        p.append('<circle cx="812" cy="150" r="%d" fill="none" stroke="#ffffff" '
                 'stroke-opacity=".2"/>' % r)
        p.append('<g class="orb" style="animation-duration:%ss%s">'
                 % (dur, ";animation-direction:reverse" if i == 1 else ""))
        for k in range(i + 1):
            a = 2 * math.pi * k / (i + 1)
            p.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>'
                     % (812 + r * math.cos(a), 150 + r * math.sin(a), 5 - i * 0.6,
                        ACC if k % 2 else ACC2))
        p.append("</g>")
    p.append('<circle class="sh" cx="812" cy="150" r="12" fill="%s"/>' % ACC)
    p.append('<text x="812" y="248" font-family="%s" font-size="9.4" fill="%s" '
             'letter-spacing="1.8" text-anchor="middle">DATA / API / AGENTS</text>'
             % (MONO, FAINT))

    p.append(panel(50, 292, 900, 92, 20))
    p.append('<text x="82" y="334" font-family="%s" font-size="20" font-weight="600" '
             'fill="%s" letter-spacing="-.4">I build AI agents and the backends they '
             'run on.</text>' % (SANS, INK))
    p.append('<text x="82" y="362" font-family="%s" font-size="10.5" fill="%s" '
             'letter-spacing="2.2">ARBISOFT / FAST-NUCES / ISLAMABAD / OPEN TO REMOTE</text>'
             % (MONO, FAINT))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ------------------------------------------------------------- principles

def principles():
    h = 190
    colw, gap = 293, 20
    lab = ". ".join("%s. %s" % (n, " ".join(b)) for _, n, b in PRINCIPLES)
    p = [head(h, lab)]
    p += backdrop(h, [(180, 60, 100, ACC, ".4", "dr"),
                      (820, 140, 110, WARM, ".26", "dr2")])
    for i, (num, title, lines) in enumerate(PRINCIPLES):
        x = 40 + i * (colw + gap)
        col = (ACC, ACC2, WARM)[i]
        p.append(panel(x, 22, colw, 136, 16))
        p.append('<rect x="%d" y="22" width="46" height="4" rx="2" fill="%s"/>' % (x + 22, col))
        p.append('<text x="%d" y="62" font-family="%s" font-size="10.5" fill="%s" '
                 'font-weight="700">%s</text>' % (x + 22, MONO, col, num))
        p.append('<text x="%d" y="92" font-family="%s" font-size="15" font-weight="700" '
                 'fill="%s">%s</text>' % (x + 22, SANS, INK, title))
        for j, ln in enumerate(lines):
            p.append('<text x="%d" y="%d" font-family="%s" font-size="11.5" fill="%s">%s</text>'
                     % (x + 22, 118 + j * 17, SANS, DIM, esc(ln)))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ------------------------------------------------------------ project card

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
    p += backdrop(h, [(190, 90, 120, ACC, ".38", "dr"),
                      (800, 250, 130, WARM, ".26", "dr2")])
    p.append(panel(40, 20, 920, 280, 22))

    p.append('<text x="%d" y="76" font-family="%s" font-size="28" font-weight="700" '
             'fill="%s" letter-spacing="-.9">%s</text>' % (left, SANS, INK, esc(spec["title"])))
    p.append('<text x="%d" y="76" font-family="%s" font-size="32" font-weight="700" '
             'fill="%s" opacity=".35" text-anchor="end">%s</text>'
             % (W - 82, SANS, ACC, spec["n"]))
    p.append('<text x="%d" y="98" font-family="%s" font-size="9.6" fill="%s" '
             'letter-spacing="1.9">%s</text>' % (left, MONO, ACC2, esc(spec["meta"])))
    p.append('<rect x="%d" y="112" width="44" height="3" rx="1.5" fill="%s"/>' % (left, ACC))

    y = 136
    x = float(left)
    for i, (label, bw) in enumerate(zip(nodes, widths)):
        p.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" rx="8" fill="url(#frost)" '
                 'stroke="#ffffff" stroke-opacity=".2"/>' % (x, y, bw, BH))
        p.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="%s" fill="%s" '
                 'text-anchor="middle">%s</text>'
                 % (x + bw / 2, y + BH / 2 + 4, MONO, FS, DIM, esc(label)))
        if i < n - 1:
            p.append('<path class="dash" d="M%.1f %.1f H%.1f" stroke="%s" stroke-width="1.6" '
                     'stroke-opacity=".7"/>' % (x + bw + 5, y + BH / 2, x + bw + GAP - 5, ACC))
        x += bw + GAP
    p.append('<text x="%d" y="%d" font-family="%s" font-size="10.5" fill="%s">%s</text>'
             % (left, y + BH + 24, MONO, FAINT, esc(spec["note"])))

    p.append('<line x1="%d" y1="214" x2="%d" y2="214" stroke="#ffffff" stroke-opacity=".14"/>'
             % (left, W - 82))
    for i, (val, cap) in enumerate(spec["metrics"]):
        cx = left + i * 204
        p.append('<text x="%d" y="252" font-family="%s" font-size="24" font-weight="700" '
                 'fill="%s" letter-spacing="-.6">%s</text>' % (cx, SANS, INK, esc(val)))
        p.append('<text x="%d" y="268" font-family="%s" font-size="8.6" fill="%s" '
                 'letter-spacing="1.5">%s</text>' % (cx, MONO, FAINT, esc(cap)))
    p.append('<text x="%d" y="288" font-family="%s" font-size="10" fill="%s">%s</text>'
             % (left, MONO, DIM, esc(spec["stack"])))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ---------------------------------------------------------------- signals

TINT = [ACC, ACC2, WARM, "#c39bff", "#7fd4ff", "#ff9bb0", FAINT]


def signals(s):
    h = 306
    lab = ("%d public repositories, %d stars, %d languages, last shipped %s"
           % (s["repos"], s["stars"], len(s["langs"]), s["pushed"]))
    p = [head(h, lab)]
    p += backdrop(h, [(200, 80, 120, ACC, ".4", "dr"),
                      (790, 230, 130, ACC2, ".26", "dr2")])
    cells = [(str(s["repos"]), "PUBLIC REPOS"), (str(s["stars"]), "STARS EARNED"),
             (str(len(s["langs"])), "LANGUAGES"), (s["pushed"], "LAST SHIPPED")]
    for i, (big, cap) in enumerate(cells):
        x = 40 + i * 235
        p.append(panel(x, 20, 215, 112, 16))
        size = 38 if len(big) <= 4 else 23
        p.append('<text x="%d" y="86" font-family="%s" font-size="%d" font-weight="700" '
                 'fill="%s" letter-spacing="-1.2">%s</text>'
                 % (x + 24, SANS, size, INK, esc(big)))
        p.append('<text x="%d" y="108" font-family="%s" font-size="9.4" fill="%s" '
                 'letter-spacing="1.7">%s</text>' % (x + 24, MONO, FAINT, cap))

    p.append(panel(40, 164, 920, 112, 18))
    p.append('<text x="70" y="196" font-family="%s" font-size="9.6" fill="%s" '
             'letter-spacing="1.9">WHAT THE REPOSITORIES ARE WRITTEN IN</text>' % (MONO, FAINT))
    total = sum(c for _, c in s["langs"]) or 1
    bx, bw, by, bh = 70, 860, 210, 14
    shown = s["langs"][:6]
    other = sum(c for _, c in s["langs"][6:])
    segs = shown + ([("Other", other)] if other else [])
    x = float(bx)
    for i, (name, count) in enumerate(segs):
        seg = bw * count / total
        p.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" rx="7" fill="%s" '
                 'opacity=".9"/>' % (x, by, max(seg - 4, 1), bh, TINT[i % len(TINT)]))
        x += seg
    lx = float(bx)
    for i, (name, count) in enumerate(segs):
        p.append('<circle cx="%.1f" cy="%d" r="4.5" fill="%s"/>'
                 % (lx + 4, by + 30, TINT[i % len(TINT)]))
        p.append('<text x="%.1f" y="%d" font-family="%s" font-size="10.5" fill="%s">%s %d</text>'
                 % (lx + 16, by + 34, MONO, DIM, esc(name), count))
        lx += 32 + mono_w("%s %d" % (name, count), 10.5)
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ---------------------------------------------------------------- sign off

def signoff():
    h = 110
    p = [head(h, "")]
    p += backdrop(h, [(500, 60, 140, ACC, ".3", "dr")])
    p.append(panel(40, 20, 920, 58, 18))
    p.append('<text class="sh" x="70" y="55" font-family="%s" font-size="10.5" fill="%s" '
             'letter-spacing="2.2">EVERY PANEL ON THIS PAGE IS DRAWN BY A SCRIPT IN THIS '
             'REPO</text>' % (MONO, DIM))
    p.append('<text x="%d" y="55" font-family="%s" font-size="10.5" fill="%s" '
             'letter-spacing="2.2" text-anchor="end">assets/build.py</text>'
             % (W - 70, MONO, ACC))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)
