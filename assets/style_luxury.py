"""Luxury typography.

A serif set far larger than a README usually allows, gold hairlines, and a lot
of air. There are almost no boxes: the structure comes from rules and from the
space between things, which is what makes it read as expensive rather than
merely dark.

Restraint is the whole point here, so the animation is limited to rules drawing
themselves in and a slow shimmer on the gold.
"""

import math

from build import (BH, FS, GAP, MONO, PAD, PRINCIPLES, REDUCE, SANS, SERIF, W,
                   esc, mono_w)

BG = "#0b0b0c"
GOLD, GOLD2 = "#c9a227", "#e6c65c"
INK, DIM, FAINT = "#f2efe9", "#c2bdb3", "#867f73"

DEFS = (
    '<defs>'
    '<linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">'
    '<stop offset="0%%" stop-color="%s" stop-opacity=".9"/>'
    '<stop offset="100%%" stop-color="%s" stop-opacity=".12"/></linearGradient>'
    '<linearGradient id="shim" x1="0" y1="0" x2="1" y2="0">'
    '<stop offset="0%%" stop-color="%s"/><stop offset="50%%" stop-color="%s"/>'
    '<stop offset="100%%" stop-color="%s"/></linearGradient>'
    '</defs>' % (GOLD, GOLD, GOLD, GOLD2, GOLD)
)

CSS = (
    ".draw{animation:draw 2.2s cubic-bezier(.2,.8,.2,1) both}"
    "@keyframes draw{from{width:0}to{width:var(--w)}}"
    ".shim{animation:shim 6s ease-in-out infinite}"
    "@keyframes shim{0%,100%{opacity:.7}50%{opacity:1}}"
    ".fade{animation:fade 1.4s ease-out both}"
    "@keyframes fade{from{opacity:0}to{opacity:1}}"
)


def head(h, label, extra=""):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" '
            'height="%d" role="img" aria-label="%s">%s<style>%s%s%s</style>'
            % (W, h, W, h, esc(label), DEFS, CSS, extra, REDUCE))


def ground(h):
    return ['<rect width="%d" height="%d" fill="%s"/>' % (W, h, BG)]


def hair(y, x0=80, x1=920, op=".3"):
    return ('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-opacity="%s"/>'
            % (x0, y, x1, y, GOLD, op))


# ------------------------------------------------------------------- hero

def hero():
    h = 440
    extra = (".orb{transform-box:view-box;transform-origin:812px 196px;"
             "animation:spin linear infinite}"
             "@keyframes spin{to{transform:rotate(360deg)}}")
    p = [head(h, "Muhammad Hassaan-ul-Mustafa. AI engineer, product and backend. "
                 "I build AI agents and the backends they run on. Arbisoft, FAST-NUCES, "
                 "Islamabad, open to remote.", extra)]
    p += ground(h)
    p.append(hair(66))
    p.append('<text x="80" y="52" font-family="%s" font-size="10.5" fill="%s" '
             'letter-spacing="5">A I &#160; E N G I N E E R</text>' % (MONO, GOLD))
    p.append('<text x="920" y="52" font-family="%s" font-size="10.5" fill="%s" '
             'letter-spacing="3" text-anchor="end">ISLAMABAD</text>' % (MONO, FAINT))

    p.append('<text class="fade" x="80" y="184" font-family="%s" font-size="62" fill="%s" '
             'letter-spacing="-1">Muhammad</text>' % (SERIF, INK))
    p.append('<text class="fade" style="animation-delay:.15s" x="80" y="252" '
             'font-family="%s" font-size="62" fill="url(#shim)" font-style="italic" '
             'letter-spacing="-1">Hassaan-ul-Mustafa</text>' % SERIF)
    p.append('<rect class="draw" style="--w:160px" x="80" y="288" width="160" height="1.6" '
             'fill="%s"/>' % GOLD)
    p.append('<text x="80" y="330" font-family="%s" font-size="19" fill="%s">'
             'I build AI agents and the backends they run on.</text>' % (SERIF, DIM))

    # a quiet ring motif, well away from the type
    for i, (r, dur) in enumerate(((26, 15), (46, 24), (66, 38))):
        p.append('<circle cx="812" cy="196" r="%d" fill="none" stroke="%s" '
                 'stroke-opacity=".22"/>' % (r, GOLD))
        p.append('<g class="orb" style="animation-duration:%ss%s">'
                 % (dur, ";animation-direction:reverse" if i == 1 else ""))
        for k in range(i + 1):
            a = 2 * math.pi * k / (i + 1)
            p.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>'
                     % (812 + r * math.cos(a), 196 + r * math.sin(a), 3.6 - i * 0.5, GOLD2))
        p.append("</g>")
    p.append('<circle class="shim" cx="812" cy="196" r="7" fill="%s"/>' % GOLD)

    p.append(hair(376))
    p.append('<text x="80" y="410" font-family="%s" font-size="10.5" fill="%s" '
             'letter-spacing="2.6">ARBISOFT &#160;&#183;&#160; FAST-NUCES &#160;&#183;&#160; '
             'OPEN TO REMOTE</text>' % (MONO, FAINT))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ------------------------------------------------------------- principles

def principles():
    h = 200
    colw, gap = 280, 40
    lab = ". ".join("%s. %s" % (n, " ".join(b)) for _, n, b in PRINCIPLES)
    p = [head(h, lab)]
    p += ground(h)
    p.append(hair(24))
    for i, (num, title, lines) in enumerate(PRINCIPLES):
        x = 80 + i * (colw + gap)
        p.append('<rect class="draw" style="--w:34px;animation-delay:%ss" x="%d" y="24" '
                 'width="34" height="2" fill="%s"/>' % (round(i * .18, 2), x, GOLD))
        p.append('<text x="%d" y="66" font-family="%s" font-size="10.5" fill="%s">%s</text>'
                 % (x, MONO, GOLD, num))
        p.append('<text x="%d" y="106" font-family="%s" font-size="21" fill="%s">%s</text>'
                 % (x, SERIF, INK, title.title()))
        for j, ln in enumerate(lines):
            p.append('<text x="%d" y="%d" font-family="%s" font-size="12.5" fill="%s">%s</text>'
                     % (x, 134 + j * 19, SERIF, DIM, esc(ln)))
    p.append(hair(184))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ------------------------------------------------------------ project card

def card(spec):
    h = 320
    left = 80
    nodes = spec["nodes"]
    n = len(nodes)
    widths = [mono_w(x, FS) + PAD * 2 for x in nodes]
    lab = ("%s. %s. %s. %s. %s" % (
        spec["title"], spec["meta"], " then ".join(nodes),
        ", ".join("%s %s" % (v, k.lower()) for v, k in spec["metrics"]), spec["stack"]))
    p = [head(h, lab)]
    p += ground(h)
    p.append(hair(24))

    p.append('<text x="%d" y="80" font-family="%s" font-size="38" fill="%s" '
             'letter-spacing="-.6">%s</text>'
             % (left, SERIF, INK, esc(spec["title"].title())))
    p.append('<text x="%d" y="80" font-family="%s" font-size="34" fill="%s" '
             'opacity=".45" text-anchor="end">%s</text>' % (W - 80, SERIF, GOLD, spec["n"]))
    p.append('<text x="%d" y="106" font-family="%s" font-size="9.6" fill="%s" '
             'letter-spacing="2.2">%s</text>' % (left, MONO, GOLD, esc(spec["meta"])))
    p.append('<rect class="draw" style="--w:44px" x="%d" y="122" width="44" height="1.6" '
             'fill="%s"/>' % (left, GOLD))

    y = 146
    x = float(left)
    for i, (label, bw) in enumerate(zip(nodes, widths)):
        p.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="none" stroke="%s" '
                 'stroke-opacity=".3"/>' % (x, y, bw, BH, GOLD))
        p.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="%s" fill="%s" '
                 'text-anchor="middle">%s</text>'
                 % (x + bw / 2, y + BH / 2 + 4, MONO, FS, DIM, esc(label)))
        if i < n - 1:
            p.append('<path d="M%.1f %.1f H%.1f" stroke="%s" stroke-opacity=".45"/>'
                     % (x + bw + 5, y + BH / 2, x + bw + GAP - 5, GOLD))
        x += bw + GAP
    p.append('<text x="%d" y="%d" font-family="%s" font-size="12.5" fill="%s" '
             'font-style="italic">%s</text>'
             % (left, y + BH + 26, SERIF, FAINT, esc(spec["note"])))

    p.append(hair(224))
    for i, (val, cap) in enumerate(spec["metrics"]):
        cx = left + i * 210
        p.append('<text x="%d" y="264" font-family="%s" font-size="30" fill="%s">%s</text>'
                 % (cx, SERIF, INK, esc(val)))
        p.append('<text x="%d" y="282" font-family="%s" font-size="8.6" fill="%s" '
                 'letter-spacing="2">%s</text>' % (cx, MONO, FAINT, esc(cap)))
    p.append('<text x="%d" y="306" font-family="%s" font-size="10" fill="%s">%s</text>'
             % (left, MONO, DIM, esc(spec["stack"])))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ---------------------------------------------------------------- signals

def signals(s):
    h = 300
    lab = ("%d public repositories, %d stars, %d languages, last shipped %s"
           % (s["repos"], s["stars"], len(s["langs"]), s["pushed"]))
    p = [head(h, lab)]
    p += ground(h)
    p.append(hair(28))
    cells = [(str(s["repos"]), "REPOSITORIES"), (str(s["stars"]), "STARS"),
             (str(len(s["langs"])), "LANGUAGES"), (s["pushed"], "LAST SHIPPED")]
    for i, (big, cap) in enumerate(cells):
        x = 80 + i * 215
        size = 46 if len(big) <= 4 else 26
        p.append('<text class="fade" style="animation-delay:%ss" x="%d" y="96" '
                 'font-family="%s" font-size="%d" fill="%s">%s</text>'
                 % (round(i * .12, 2), x, SERIF, size, INK, esc(big)))
        p.append('<text x="%d" y="120" font-family="%s" font-size="9" fill="%s" '
                 'letter-spacing="2.6">%s</text>' % (x, MONO, FAINT, cap))
    p.append(hair(152))

    p.append('<text x="80" y="182" font-family="%s" font-size="9.4" fill="%s" '
             'letter-spacing="2.4">WHAT THE REPOSITORIES ARE WRITTEN IN</text>'
             % (MONO, FAINT))
    total = sum(c for _, c in s["langs"]) or 1
    bx, bw, by, bh = 80, 840, 198, 6
    shown = s["langs"][:6]
    other = sum(c for _, c in s["langs"][6:])
    segs = shown + ([("Other", other)] if other else [])
    tone = [GOLD, GOLD2, "#a98a33", "#8f7a45", "#7a6a4f", "#6b6357", FAINT]
    x = float(bx)
    for i, (name, count) in enumerate(segs):
        seg = bw * count / total
        p.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s"/>'
                 % (x, by, max(seg - 3, 1), bh, tone[i % len(tone)]))
        x += seg
    lx = float(bx)
    for i, (name, count) in enumerate(segs):
        p.append('<rect x="%.1f" y="%d" width="7" height="7" fill="%s"/>'
                 % (lx, by + 22, tone[i % len(tone)]))
        p.append('<text x="%.1f" y="%d" font-family="%s" font-size="11" fill="%s">%s %d</text>'
                 % (lx + 13, by + 29, SERIF, DIM, esc(name), count))
        lx += 28 + mono_w("%s %d" % (name, count), 11)
    p.append(hair(258))
    p.append('<text x="80" y="286" font-family="%s" font-size="10" fill="%s" '
             'letter-spacing="2.4">3RD PLACE NATIONAL AI HACKATHON &#160;&#183;&#160; '
             'PRODUCTION ADOPTER, GRAPH CONTEXT FRAMEWORK</text>' % (MONO, FAINT))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ---------------------------------------------------------------- sign off

def signoff():
    h = 104
    p = [head(h, "")]
    p += ground(h)
    p.append('<rect class="draw" style="--w:840px" x="80" y="34" width="840" height="1" '
             'fill="url(#rule)"/>')
    p.append('<text x="80" y="70" font-family="%s" font-size="10" fill="%s" '
             'letter-spacing="2.6">EVERY MARK ON THIS PAGE IS DRAWN BY A SCRIPT IN THIS '
             'REPO</text>' % (MONO, FAINT))
    p.append('<text class="shim" x="920" y="70" font-family="%s" font-size="10" fill="%s" '
             'letter-spacing="2.6" text-anchor="end">assets/build.py</text>' % (MONO, GOLD))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)
