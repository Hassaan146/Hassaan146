"""Obsidian and champagne.

The sage is gone. This is a neutral obsidian ground with no colour cast, warm
bone type, and a single muted champagne used only where something needs
pointing at. Sage was chosen to sit in the same family as GitHub's own
contribution greens, but the heatmap here is drawn from the real calendar by
this module, not fetched, so there is no external palette left to match. That
freed the accent, and a warm metal on a cold neutral reads as expensive in a
way a desaturated green does not.

Champagne rather than gold: the value is held near 60% and the saturation low,
because a dense panel layout at full-saturation gold looks like a certificate.

The panel treatment changed too. The registration brackets are gone, replaced by
a solid spine down the left edge of every block and a single rule across the
top, so a panel reads as a column entry rather than a floating card.

The contribution graph is back, and it is drawn here from the real calendar
rather than fetched from a widget. The service that used to provide it answered
HTTP 200 with an error message drawn inside the image, so nothing noticed it had
failed. A heatmap built from the actual cells cannot do that: if the data is
missing the panel says so in words.
"""

import math

from build import (BH, CW, FS, GAP, MONO, PAD, PRINCIPLES, REDUCE, SANS, W,
                   esc, mono_w)

BG0, BG1 = "#0a0a0b", "#050506"
PANEL = "#0f0f11"
INK, DIM, FAINT = "#ece7dd", "#9c968a", "#615c53"
LINE = "#1f1e1c"
ACC, ACC2 = "#c9a961", "#8a7440"

HEAT = ["#18160f", "#3a301a", "#5c4b28", "#8d7539", "#c9a961"]

DEFS = (
    '<defs>'
    '<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
    '<stop offset="0%%" stop-color="%s"/><stop offset="100%%" stop-color="%s"/>'
    '</linearGradient>'
    '<linearGradient id="spine" x1="0" y1="0" x2="0" y2="1">'
    '<stop offset="0%%" stop-color="%s"/><stop offset="100%%" stop-color="%s"/>'
    '</linearGradient>'
    '</defs>' % (BG0, BG1, ACC, ACC2)
)

CSS = (
    ".tick{animation:tk 5s ease-in-out infinite}"
    "@keyframes tk{0%,100%{opacity:.4}18%{opacity:1}42%{opacity:.4}}"
    ".dash{stroke-dasharray:2 5;animation:d 2s linear infinite}"
    "@keyframes d{to{stroke-dashoffset:-7}}"
    ".cell{animation:in .9s ease-out both}"
    "@keyframes in{from{opacity:0}to{opacity:1}}"
)


def head(h, label, extra=""):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" '
            'height="%d" role="img" aria-label="%s">%s<style>%s%s%s</style>'
            % (W, h, W, h, esc(label), DEFS, CSS, extra, REDUCE))


def ground(h):
    return ['<rect width="%d" height="%d" fill="url(#bg)"/>' % (W, h)]


def block(x, y, w, h, fill=True):
    """A spine down the left edge and a rule across the top."""
    p = []
    if fill:
        p.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" '
                 'fill-opacity=".7"/>' % (x, y, w, h, PANEL))
    p.append('<rect x="%d" y="%d" width="3" height="%d" fill="url(#spine)"/>' % (x, y, h))
    p.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s"/>'
             % (x, y, x + w, y, LINE))
    p.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s"/>'
             % (x, y + h, x + w, y + h, LINE))
    return p


def t(x, y, s, size=11, fill=DIM, font=MONO, weight=None, anchor=None, track=None,
      cls=None, style=None, op=None):
    a = ['<text x="%.1f" y="%.1f" font-family="%s" font-size="%s" fill="%s"'
         % (x, y, font, size, fill)]
    for k, v in (("font-weight", weight), ("text-anchor", anchor),
                 ("letter-spacing", track), ("class", cls), ("style", style),
                 ("opacity", op)):
        if v:
            a.append(' %s="%s"' % (k, v))
    a.append(">%s</text>" % esc(s))
    return "".join(a)


# ------------------------------------------------------------------- hero

def hero():
    h = 400
    extra = (".orb{transform-box:view-box;transform-origin:812px 152px;"
             "animation:spin linear infinite}"
             "@keyframes spin{to{transform:rotate(360deg)}}")
    p = [head(h, "Muhammad Hassaan-ul-Mustafa. AI engineer, product and backend. "
                 "I build AI agents and the backends they run on. Arbisoft, "
                 "FAST-NUCES, Islamabad, open to remote.", extra)]
    p += ground(h)
    p += block(40, 40, 920, 300)

    p.append(t(72, 84, "AI ENGINEER / PRODUCT AND BACKEND", 10.5, ACC, track="4"))
    p.append(t(928, 84, "ISLAMABAD, PK", 10.5, FAINT, track="2.4", anchor="end"))
    p.append(t(70, 168, "MUHAMMAD", 54, INK, SANS, 700, track="-2.2"))
    p.append(t(70, 224, "HASSAAN", 54, INK, SANS, 700, track="-2.2"))
    p.append('<rect x="72" y="244" width="128" height="3" fill="%s"/>' % ACC)
    p.append(t(72, 282, "I build AI agents and the backends they run on.", 14, DIM))
    p.append(t(72, 312, "ARBISOFT / FAST-NUCES / OPEN TO REMOTE", 10, FAINT, track="2.2"))

    for i, (r, dur) in enumerate(((28, 15), (48, 24), (68, 38))):
        p.append('<circle cx="812" cy="152" r="%d" fill="none" stroke="%s"/>' % (r, LINE))
        p.append('<g class="orb" style="animation-duration:%ss%s">'
                 % (dur, ";animation-direction:reverse" if i == 1 else ""))
        for k in range(i + 1):
            a = 2 * math.pi * k / (i + 1)
            p.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>'
                     % (812 + r * math.cos(a), 152 + r * math.sin(a),
                        4.2 - i * 0.5, ACC if k == 0 else ACC2))
        p.append("</g>")
    p.append('<circle class="tick" cx="812" cy="152" r="8" fill="%s"/>' % ACC)
    p.append(t(812, 246, "DATA / API / AGENTS", 9, FAINT, track="1.8", anchor="middle"))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ------------------------------------------------------------- principles

def principles():
    h = 180
    colw, gap = 293, 20
    lab = ". ".join("%s. %s" % (n, " ".join(b)) for _, n, b in PRINCIPLES)
    p = [head(h, lab)]
    p += ground(h)
    for i, (num, title, lines) in enumerate(PRINCIPLES):
        x = 40 + i * (colw + gap)
        p += block(x, 20, colw, 128)
        p.append(t(x + 24, 56, num, 10.5, ACC, weight=700))
        p.append(t(x + 24, 88, title, 15, INK, SANS, 700))
        for j, ln in enumerate(lines):
            p.append(t(x + 24, 112 + j * 16, ln, 11, DIM))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ------------------------------------------------------------ project card

def card(spec):
    h = 316
    left = 78
    nodes = spec["nodes"]
    n = len(nodes)
    widths = [mono_w(x, FS) + PAD * 2 for x in nodes]
    lab = ("%s. %s. %s. %s. %s" % (
        spec["title"], spec["meta"], " then ".join(nodes),
        ", ".join("%s %s" % (v, k.lower()) for v, k in spec["metrics"]), spec["stack"]))
    p = [head(h, lab)]
    p += ground(h)
    p += block(40, 20, 920, 272)

    p.append(t(left, 72, spec["title"], 29, INK, SANS, 700, track="-1"))
    p.append(t(922, 72, spec["n"], 30, ACC, SANS, 700, anchor="end", op=".35"))
    p.append(t(left, 94, spec["meta"], 9.6, ACC, track="1.9"))
    p.append('<rect x="%d" y="108" width="38" height="2.5" fill="%s"/>' % (left, ACC2))

    y = 132
    x = float(left)
    for i, (label, bw) in enumerate(zip(nodes, widths)):
        p.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="none" stroke="%s"/>'
                 % (x, y, bw, BH, LINE))
        p.append(t(x + bw / 2, y + BH / 2 + 4, label, FS, DIM, anchor="middle"))
        if i < n - 1:
            p.append('<path class="dash" d="M%.1f %.1f H%.1f" stroke="%s" '
                     'stroke-opacity=".8"/>' % (x + bw + 5, y + BH / 2,
                                                x + bw + GAP - 5, ACC2))
        x += bw + GAP
    p.append(t(left, y + BH + 24, spec["note"], 10.5, FAINT))

    p.append('<line x1="%d" y1="212" x2="922" y2="212" stroke="%s"/>' % (left, LINE))
    for i, (val, cap) in enumerate(spec["metrics"]):
        cx = left + i * 212
        p.append(t(cx, 250, val, 24, INK, SANS, 700, track="-.6"))
        p.append(t(cx, 266, cap, 8.6, FAINT, track="1.5"))
    p.append(t(left, 284, spec["stack"], 10, DIM))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# --------------------------------------------------- the contribution graph

def contributions(s):
    """A year of commits, drawn from the real calendar."""
    cells = s.get("cells") or []
    h = 190
    total = s.get("contrib")
    lab = ("Contribution graph. %s contributions in the last year."
           % (total if total is not None else "An unknown number of"))
    p = [head(h, lab)]
    p += ground(h)
    p += block(40, 20, 920, 150)
    p.append(t(78, 52, "A YEAR OF COMMITS", 9.6, ACC, track="1.9"))
    if total is not None:
        p.append(t(922, 54, "%s in the last year" % format(total, ","), 11, INK,
                   anchor="end"))

    if not cells:
        p.append(t(78, 100, "The calendar could not be read this build, so the graph "
                            "kept its last draw.", 11, FAINT))
        p.append("</svg>")
        return chr(10).join(p) + chr(10)

    # lay the days out in weeks, the way the calendar reads
    box, gap = 11, 3
    x0, y0 = 78, 70
    weeks = (len(cells) + 6) // 7
    span = weeks * (box + gap)
    if span > 844:                       # keep it inside the block
        box = max(6, int((844 - weeks * gap) / weeks))
    for i, (date, level) in enumerate(cells):
        wk, day = divmod(i, 7)
        p.append('<rect class="cell" style="animation-delay:%.2fs" x="%.1f" y="%.1f" '
                 'width="%d" height="%d" rx="2" fill="%s"/>'
                 % (min(wk * 0.012, 0.9), x0 + wk * (box + gap), y0 + day * (box + gap),
                    box, box, HEAT[min(level, 4)]))
    legend_y = y0 + 7 * (box + gap) + 22
    p.append(t(78, legend_y, "less", 9, FAINT))
    for i, col in enumerate(HEAT):
        p.append('<rect x="%d" y="%d" width="%d" height="%d" rx="2" fill="%s"/>'
                 % (112 + i * (box + gap), legend_y - box + 2, box, box, col))
    p.append(t(112 + 5 * (box + gap) + 6, legend_y, "more", 9, FAINT))
    p.append(t(922, legend_y, "%d days drawn from the live calendar" % len(cells),
               9, FAINT, anchor="end"))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# ---------------------------------------------------------------- signals

TONE = [ACC, "#e2cb92", ACC2, "#8a8378", "#615c53", "#47433c", "#34312c"]


def signals(s):
    h = 300
    lab = ("%d public repositories, %d stars, %d languages, last shipped %s"
           % (s["repos"], s["stars"], len(s["langs"]), s["pushed"]))
    p = [head(h, lab)]
    p += ground(h)
    cells = [(str(s["repos"]), "PUBLIC REPOS"), (str(s["stars"]), "STARS EARNED"),
             (str(len(s["langs"])), "LANGUAGES"), (s["pushed"], "LAST SHIPPED")]
    for i, (big, cap) in enumerate(cells):
        x = 40 + i * 235
        p += block(x, 20, 215, 108)
        size = 38 if len(big) <= 4 else 23
        p.append(t(x + 24, 84, big, size, ACC if i == 0 else INK, SANS, 700, track="-1.3"))
        p.append(t(x + 24, 106, cap, 9.4, FAINT, track="1.7"))

    p += block(40, 158, 920, 116)
    p.append(t(78, 190, "WHAT THE REPOSITORIES ARE WRITTEN IN", 9.6, ACC, track="1.9"))
    total = sum(c for _, c in s["langs"]) or 1
    shown = s["langs"][:6]
    other = sum(c for _, c in s["langs"][6:])
    segs = shown + ([("Other", other)] if other else [])
    bx, bw, by, bh = 78, 844, 206, 12
    x = float(bx)
    for i, (name, count) in enumerate(segs):
        seg = bw * count / total
        p.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" rx="2" fill="%s"/>'
                 % (x, by, max(seg - 3, 1), bh, TONE[i % len(TONE)]))
        x += seg
    lx = float(bx)
    for i, (name, count) in enumerate(segs):
        p.append('<rect x="%.1f" y="%d" width="8" height="8" rx="2" fill="%s"/>'
                 % (lx, by + 24, TONE[i % len(TONE)]))
        p.append(t(lx + 14, by + 32, "%s %d" % (name, count), 10.5, DIM))
        lx += 30 + mono_w("%s %d" % (name, count), 10.5)
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


# -------------------------------------------------------------- ask panel

def _flow(text, size, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        x = (cur + " " + w).strip()
        if mono_w(x, size) > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = x
    if cur:
        lines.append(cur)
    return lines


def asked_panel(log):
    log = log[:3]
    rows = sum(2 + len(_flow(str(i.get("a", "")), 10.5, 780)[:3]) for i in log) or 2
    h = 100 + rows * 16
    lab = ("Questions asked of the agent. "
           + " ".join("%s %s" % (i.get("q", ""), i.get("a", "")) for i in log)
           if log else "No questions asked yet.")
    p = [head(h, lab)]
    p += ground(h)
    p += block(40, 20, 920, h - 40)
    p.append(t(78, 52, "ASK IT SOMETHING", 9.6, ACC, track="1.9"))
    p.append(t(78, 72, "Open an issue titled agent: and your question. A workflow "
                       "answers it, writes the reply here, then closes the issue.",
               10.5, FAINT))
    y = 104
    if not log:
        p.append(t(78, y, "Nobody has asked anything yet.", 11, FAINT))
    for item in log:
        p.append('<rect x="78" y="%d" width="3" height="28" fill="%s"/>' % (y - 11, ACC))
        p.append(t(92, y, str(item.get("q", ""))[:74], 11.5, INK))
        p.append(t(922, y, "@" + str(item.get("who", ""))[:22], 9, FAINT, anchor="end"))
        y += 16
        for ln in _flow(str(item.get("a", "")), 10.5, 780)[:3]:
            p.append(t(92, y, ln, 10.5, DIM))
            y += 15
        y += 12
    p.append("</svg>")
    return chr(10).join(p) + chr(10)


def asked():
    import json
    import pathlib
    f = pathlib.Path(__file__).parent / "asked.json"
    log = []
    if f.exists():
        try:
            log = json.loads(f.read_text(encoding="utf-8"))
        except ValueError:
            pass
    return asked_panel(log)


# ---------------------------------------------------------------- sign off

def signoff():
    h = 104
    p = [head(h, "")]
    p += ground(h)
    p += block(40, 20, 920, 54)
    p.append(t(78, 54, "EVERY PANEL ON THIS PAGE IS DRAWN BY A SCRIPT IN THIS REPO",
               10.5, DIM, track="2.2"))
    p.append(t(922, 54, "assets/build.py", 10.5, ACC, track="2.2", anchor="end",
               cls="tick"))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)
