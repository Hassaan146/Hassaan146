"""Instrumentation.

The cyberpunk layout with the neon taken out. Same grid, same HUD brackets, same
dense annotated panels, but rendered as a technical drawing rather than a
synthwave poster.

What was removed and why. Saturated cyan and magenta on violet, gaussian glow,
chromatic aberration on the wordmark, and a sweeping scanline are the four most
recognisable cliches in AI generated imagery, and a page wearing all four reads
as generated no matter how carefully it was built. They are gone.

What replaced them. A neutral near black ground with no colour cast, bone white
type, a graphite grid, and a single desaturated ochre used only where something
needs pointing at. Every rule is hairline. Nothing glows.

The result keeps the density that made the layout work and loses the costume.
"""

import json
import math
import pathlib

from build import (BH, CW, FS, GAP, MONO, PAD, PRINCIPLES, REDUCE, SANS, W,
                   esc, mono_w)

BG0, BG1 = "#0d0d0e", "#08080a"
PANEL = "#111113"
INK, DIM, FAINT = "#ece9e4", "#9a958d", "#5f5c57"
LINE = "#24242a"
ACC = "#c08a3e"          # the only colour on the page
ACC2 = "#8d6b3a"

DEFS = (
    '<defs>'
    '<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
    '<stop offset="0%%" stop-color="%s"/><stop offset="100%%" stop-color="%s"/>'
    '</linearGradient>'
    '<pattern id="mesh" width="22" height="22" patternUnits="userSpaceOnUse">'
    '<path d="M22 0H0V22" fill="none" stroke="%s" stroke-width="1"/></pattern>'
    '</defs>' % (BG0, BG1, LINE)
)

CSS = (
    ".tick{animation:tk 5s ease-in-out infinite}"
    "@keyframes tk{0%,100%{opacity:.35}18%{opacity:1}40%{opacity:.35}}"
    ".dash{stroke-dasharray:2 5;animation:d 2s linear infinite}"
    "@keyframes d{to{stroke-dashoffset:-7}}"
    ".sweep{animation:sw 9s ease-in-out infinite}"
    "@keyframes sw{0%,100%{opacity:.18}50%{opacity:.5}}"
)


def head(h, label, extra=""):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" '
            'height="%d" role="img" aria-label="%s">%s<style>%s%s%s</style>'
            % (W, h, W, h, esc(label), DEFS, CSS, extra, REDUCE))


def ground(h, mesh=True):
    p = ['<rect width="%d" height="%d" fill="url(#bg)"/>' % (W, h)]
    if mesh:
        p.append('<rect width="%d" height="%d" fill="url(#mesh)" opacity=".5"/>' % (W, h))
    return p


def panel(x, y, w, h):
    return ('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" fill-opacity=".82" '
            'stroke="%s" stroke-width="1"/>' % (x, y, w, h, PANEL, LINE))


def corners(x, y, w, h, col=ACC, n=13):
    """Registration marks. A drafting cue, not a HUD glow."""
    p = []
    for cx, cy, dx, dy in ((x, y, 1, 1), (x + w, y, -1, 1),
                           (x, y + h, 1, -1), (x + w, y + h, -1, -1)):
        p.append('<path d="M%d %d h%d M%d %d v%d" stroke="%s" stroke-width="1.4" '
                 'fill="none" stroke-opacity=".8"/>' % (cx, cy, n * dx, cx, cy, n * dy, col))
    return p


def scale_bar(x, y, w, n=10):
    """A measuring rule along an edge, the way a drawing is dimensioned."""
    p = ['<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s"/>' % (x, y, x + w, y, LINE)]
    for i in range(n + 1):
        tx = x + w * i / n
        long = i % 5 == 0
        p.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" '
                 'stroke-opacity="%s"/>' % (tx, y, tx, y - (7 if long else 4),
                                            ACC if long else LINE, ".7" if long else "1"))
    return p


# ------------------------------------------------------------------- hero

def hero():
    h = 420
    extra = (".orb{transform-box:view-box;transform-origin:816px 158px;"
             "animation:spin linear infinite}"
             "@keyframes spin{to{transform:rotate(360deg)}}")
    p = [head(h, "Muhammad Hassaan-ul-Mustafa. AI engineer, product and backend. "
                 "I build AI agents and the backends they run on. Arbisoft, FAST-NUCES, "
                 "Islamabad, open to remote.", extra)]
    p += ground(h)

    # horizon, one hairline instead of a perspective sunset
    p.append('<line class="sweep" x1="0" y1="300" x2="%d" y2="300" stroke="%s"/>' % (W, ACC))
    p += scale_bar(60, 300, 880, 22)

    p.append('<text x="60" y="82" font-family="%s" font-size="10.5" fill="%s" '
             'letter-spacing="4">AI ENGINEER / PRODUCT AND BACKEND</text>' % (MONO, ACC))
    p.append('<text x="%d" y="82" font-family="%s" font-size="10.5" fill="%s" '
             'letter-spacing="2.4" text-anchor="end">ISLAMABAD, PK</text>' % (W - 60, MONO, FAINT))

    p.append('<text x="58" y="164" font-family="%s" font-size="54" font-weight="700" '
             'fill="%s" letter-spacing="-2.2">MUHAMMAD</text>' % (SANS, INK))
    p.append('<text x="58" y="220" font-family="%s" font-size="54" font-weight="700" '
             'fill="%s" letter-spacing="-2.2">HASSAAN</text>' % (SANS, INK))
    p.append('<rect x="60" y="240" width="132" height="3" fill="%s"/>' % ACC)
    p.append('<text x="60" y="278" font-family="%s" font-size="14" fill="%s">'
             'I build AI agents and the backends they run on.</text>' % (MONO, DIM))

    # the system, drawn as a mechanism
    for i, (r, dur) in enumerate(((28, 15), (48, 24), (68, 38))):
        p.append('<circle cx="816" cy="158" r="%d" fill="none" stroke="%s" '
                 'stroke-opacity=".9"/>' % (r, LINE))
        p.append('<g class="orb" style="animation-duration:%ss%s">'
                 % (dur, ";animation-direction:reverse" if i == 1 else ""))
        for k in range(i + 1):
            a = 2 * math.pi * k / (i + 1)
            p.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>'
                     % (816 + r * math.cos(a), 158 + r * math.sin(a),
                        4.2 - i * 0.5, ACC if k == 0 else ACC2))
        p.append("</g>")
    p.append('<circle class="tick" cx="816" cy="158" r="8" fill="%s"/>' % ACC)
    p.append('<text x="816" y="252" font-family="%s" font-size="9.2" fill="%s" '
             'letter-spacing="1.8" text-anchor="middle">DATA / API / AGENTS</text>'
             % (MONO, FAINT))

    p.append(panel(60, 334, 880, 54))
    p += corners(60, 334, 880, 54)
    p.append('<text x="82" y="367" font-family="%s" font-size="10.5" fill="%s" '
             'letter-spacing="2.4">ARBISOFT / FAST-NUCES / ISLAMABAD / OPEN TO REMOTE</text>'
             % (MONO, DIM))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ------------------------------------------------------------- principles

def principles():
    h = 186
    colw, gap = 293, 20
    lab = ". ".join("%s. %s" % (n, " ".join(b)) for _, n, b in PRINCIPLES)
    p = [head(h, lab)]
    p += ground(h)
    for i, (num, title, lines) in enumerate(PRINCIPLES):
        x = 40 + i * (colw + gap)
        p.append(panel(x, 20, colw, 132))
        p += corners(x, 20, colw, 132, n=10)
        p.append('<rect class="tick" style="animation-delay:%ss" x="%d" y="20" width="%d" '
                 'height="3" fill="%s"/>' % (round(i * .7, 2), x, colw, ACC))
        p.append('<text x="%d" y="60" font-family="%s" font-size="10.5" fill="%s" '
                 'font-weight="700">%s</text>' % (x + 22, MONO, ACC, num))
        p.append('<text x="%d" y="92" font-family="%s" font-size="15" font-weight="700" '
                 'fill="%s">%s</text>' % (x + 22, SANS, INK, title))
        for j, ln in enumerate(lines):
            p.append('<text x="%d" y="%d" font-family="%s" font-size="11" fill="%s">%s</text>'
                     % (x + 22, 116 + j * 16, MONO, DIM, esc(ln)))
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
    p += ground(h)
    p.append(panel(40, 20, 920, 280))
    p += corners(40, 20, 920, 280)

    p.append('<text x="%d" y="74" font-family="%s" font-size="29" font-weight="700" '
             'fill="%s" letter-spacing="-1">%s</text>' % (left, SANS, INK, esc(spec["title"])))
    p.append('<text x="%d" y="74" font-family="%s" font-size="30" font-weight="700" '
             'fill="%s" opacity=".4" text-anchor="end">%s</text>'
             % (W - 82, SANS, ACC, spec["n"]))
    p.append('<text x="%d" y="96" font-family="%s" font-size="9.6" fill="%s" '
             'letter-spacing="1.9">%s</text>' % (left, MONO, ACC, esc(spec["meta"])))
    p.append('<rect x="%d" y="110" width="40" height="2.5" fill="%s"/>' % (left, ACC))

    y = 134
    x = float(left)
    for i, (label, bw) in enumerate(zip(nodes, widths)):
        p.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="none" stroke="%s"/>'
                 % (x, y, bw, BH, LINE))
        p.append('<text x="%.1f" y="%.1f" font-family="%s" font-size="%s" fill="%s" '
                 'text-anchor="middle">%s</text>'
                 % (x + bw / 2, y + BH / 2 + 4, MONO, FS, DIM, esc(label)))
        if i < n - 1:
            p.append('<path class="dash" d="M%.1f %.1f H%.1f" stroke="%s" '
                     'stroke-opacity=".85"/>' % (x + bw + 5, y + BH / 2,
                                                 x + bw + GAP - 5, ACC2))
        x += bw + GAP
    p.append('<text x="%d" y="%d" font-family="%s" font-size="10.5" fill="%s">%s</text>'
             % (left, y + BH + 24, MONO, FAINT, esc(spec["note"])))

    p += scale_bar(left, 214, W - 82 - left, 16)
    for i, (val, cap) in enumerate(spec["metrics"]):
        cx = left + i * 204
        p.append('<text x="%d" y="254" font-family="%s" font-size="24" font-weight="700" '
                 'fill="%s" letter-spacing="-.6">%s</text>' % (cx, SANS, INK, esc(val)))
        p.append('<text x="%d" y="270" font-family="%s" font-size="8.6" fill="%s" '
                 'letter-spacing="1.5">%s</text>' % (cx, MONO, FAINT, esc(cap)))
    p.append('<text x="%d" y="290" font-family="%s" font-size="10" fill="%s">%s</text>'
             % (left, MONO, DIM, esc(spec["stack"])))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ---------------------------------------------------------------- signals

TONE = [ACC, "#a8a29a", ACC2, "#7d7871", "#5f5c57", "#4a4744", "#3a3835"]


def signals(s):
    h = 306
    lab = ("%d public repositories, %d stars, %d languages, last shipped %s"
           % (s["repos"], s["stars"], len(s["langs"]), s["pushed"]))
    p = [head(h, lab)]
    p += ground(h)
    cells = [(str(s["repos"]), "PUBLIC REPOS"), (str(s["stars"]), "STARS EARNED"),
             (str(len(s["langs"])), "LANGUAGES"), (s["pushed"], "LAST SHIPPED")]
    for i, (big, cap) in enumerate(cells):
        x = 40 + i * 235
        p.append(panel(x, 20, 215, 112))
        p += corners(x, 20, 215, 112, n=9)
        size = 40 if len(big) <= 4 else 24
        p.append('<text x="%d" y="88" font-family="%s" font-size="%d" font-weight="700" '
                 'fill="%s" letter-spacing="-1.4">%s</text>'
                 % (x + 22, SANS, size, INK if i else ACC, esc(big)))
        p.append('<text x="%d" y="110" font-family="%s" font-size="9.4" fill="%s" '
                 'letter-spacing="1.7">%s</text>' % (x + 22, MONO, FAINT, cap))

    p.append(panel(40, 164, 920, 112))
    p += corners(40, 164, 920, 112)
    p.append('<text x="70" y="196" font-family="%s" font-size="9.6" fill="%s" '
             'letter-spacing="1.9">WHAT THE REPOSITORIES ARE WRITTEN IN</text>' % (MONO, FAINT))
    total = sum(c for _, c in s["langs"]) or 1
    bx, bw, by, bh = 70, 860, 210, 12
    shown = s["langs"][:6]
    other = sum(c for _, c in s["langs"][6:])
    segs = shown + ([("Other", other)] if other else [])
    x = float(bx)
    for i, (name, count) in enumerate(segs):
        seg = bw * count / total
        p.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s"/>'
                 % (x, by, max(seg - 3, 1), bh, TONE[i % len(TONE)]))
        x += seg
    lx = float(bx)
    for i, (name, count) in enumerate(segs):
        p.append('<rect x="%.1f" y="%d" width="8" height="8" fill="%s"/>'
                 % (lx, by + 24, TONE[i % len(TONE)]))
        p.append('<text x="%.1f" y="%d" font-family="%s" font-size="10.5" fill="%s">%s %d</text>'
                 % (lx + 14, by + 32, MONO, DIM, esc(name), count))
        lx += 30 + mono_w("%s %d" % (name, count), 10.5)
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ---------------------------------------------------------------- sign off

def signoff():
    h = 110
    p = [head(h, "")]
    p += ground(h)
    p.append(panel(40, 20, 920, 56))
    p += corners(40, 20, 920, 56)
    p.append('<text x="70" y="54" font-family="%s" font-size="10.5" fill="%s" '
             'letter-spacing="2.2">EVERY PANEL ON THIS PAGE IS DRAWN BY A SCRIPT IN THIS '
             'REPO</text>' % (MONO, DIM))
    p.append('<text class="tick" x="%d" y="54" font-family="%s" font-size="10.5" fill="%s" '
             'letter-spacing="2.2" text-anchor="end">assets/build.py</text>'
             % (W - 70, MONO, ACC))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


def _asked():
    p = pathlib.Path(__file__).parent / "asked.json"
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except ValueError:
            pass
    return []


def _flow(text, size, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if mono_w(t, size) > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = t
    if cur:
        lines.append(cur)
    return lines


def asked():
    """The questions strangers have put to the agent, and what it said back."""
    log = _asked()[:3]
    rows = sum(2 + len(_flow(str(i.get("a", "")), 10.5, 800)[:3]) for i in log) or 2
    h = 96 + rows * 16
    lab = "Questions asked of the agent" + (
        ". " + " ".join("%s. %s" % (i.get("q", ""), i.get("a", "")) for i in log) if log else
        ". None yet.")
    p = [head(h, lab)]
    p += ground(h)
    p.append(panel(40, 20, 920, h - 40))
    p += corners(40, 20, 920, h - 40)
    p.append('<text x="70" y="52" font-family="%s" font-size="9.6" fill="%s" '
             'letter-spacing="1.9">ASK IT SOMETHING</text>' % (MONO, ACC))
    p.append('<text x="70" y="72" font-family="%s" font-size="11" fill="%s">'
             'Open an issue titled agent: and your question. A workflow answers it, '
             'writes the reply here, then closes the issue.</text>' % (MONO, FAINT))
    y = 104
    if not log:
        p.append('<text x="70" y="%d" font-family="%s" font-size="11" fill="%s">'
                 'Nobody has asked anything yet.</text>' % (y, MONO, FAINT))
    for item in log:
        p.append('<rect x="70" y="%d" width="3" height="30" fill="%s"/>' % (y - 11, ACC))
        p.append('<text x="84" y="%d" font-family="%s" font-size="11.5" fill="%s">%s</text>'
                 % (y, MONO, INK, esc(str(item.get("q", ""))[:76])))
        p.append('<text x="930" y="%d" font-family="%s" font-size="9" fill="%s" '
                 'text-anchor="end">@%s</text>'
                 % (y, MONO, FAINT, esc(str(item.get("who", ""))[:22])))
        y += 16
        for ln in _flow(str(item.get("a", "")), 10.5, 800)[:3]:
            p.append('<text x="84" y="%d" font-family="%s" font-size="10.5" fill="%s">%s</text>'
                     % (y, MONO, DIM, esc(ln)))
            y += 15
        y += 12
    p.append("</svg>")
    return chr(10).join(p) + chr(10)
