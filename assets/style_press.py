"""The broadsheet.

Every previous version of this page was a dark technical surface: panels, grids,
hairlines, monospace. This inverts all of it. Paper instead of a screen, ink
instead of glow, a serif masthead, ruled columns, and one print red.

The reason is not novelty. A profile README sits in a feed of other dark pages
built from the same handful of widget services, and the fastest way to look
unlike a generated page is to look like something that predates generation. A
broadsheet has rules a machine does not reach for: a dateline, a folio, columns
of justified measure, a letters page, small caps standfirsts.

The content is unchanged. The five systems are the stories, the counts are the
by-the-numbers box, and the agent questions strangers ask are the letters page,
which is exactly where correspondence belongs.

The date and the edition number come from live data, so the paper is genuinely
today's edition rather than a picture of one.
"""

import datetime
import json
import math
import pathlib

from build import PRINCIPLES, SYSTEMS, esc

W = 900
M = 54
R = W - M
COL = (R - M - 36) / 3.0        # three column measure with two 18pt gutters

PAPER, PAPER2 = "#f5f2ea", "#efeade"
INK = "#17150f"
SOFT = "#4a463c"
FAINT = "#8a8375"
RULE = "#c6bfae"
RED = "#a8321e"

SERIF = "Georgia, 'Times New Roman', Times, serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

REDUCE = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"

TOOLCHAIN = [
    ("LANGUAGES", "Python, TypeScript, JavaScript, C++, Java, SQL, x86 assembly"),
    ("AI", "LangGraph, LangChain, MCP, Anthropic, Groq, Gemini, Pydantic"),
    ("BACKEND", "FastAPI, Django, DRF, Node, Express, Celery"),
    ("FRONTEND", "React, Next.js, Vite, Tailwind, Three.js"),
    ("DATA", "PostgreSQL, Supabase, MongoDB, Redis, MySQL, SQL Server"),
    ("SHIP", "Docker, Git, Linux, Vercel, Render, Railway, Stripe"),
]

STORIES = {
    "forge": ("A plugin that refuses to write the code",
              "An agent will happily add two thousand lines on top of a decision "
              "nobody made. This one stops, states the architectural question, "
              "lays out the options, and waits. The answer is written into the "
              "repository so the reasoning outlives the sprint."),
    "news": ("Four hundred items in, five come out",
             "One hundred and sixty four sites and thirty six channels are read "
             "every night. What survives the ranking is summarised and posted "
             "before breakfast. Groq writes it; Gemini covers the outages."),
    "skyelite": ("It tells you what it gave up",
                 "Passport and budget rule most of the world out before the "
                 "ranking begins. What remains is scored on safety, cost, visa "
                 "difficulty and scenery, and the tradeoff is printed alongside "
                 "the answer. Third nationally, out of a hackathon weekend."),
    "bitmadwall": ("Messages that need no network",
                   "Encrypted traffic and Bitcoin move phone to phone across "
                   "Bluetooth, Wi-Fi Direct and LoRa. Up to seven hops, nothing "
                   "in the middle, and anything undeliverable waits in the pocket "
                   "until a peer walks past."),
    "employeeos": ("Every seat in the company is an agent",
                   "A sentence in plain English becomes a dependency aware plan. "
                   "Each piece goes to the agent that owns it, results are checked "
                   "before they move on, and the whole run is handed back as a "
                   "trace you can read."),
}


# --------------------------------------------------------------------------
# measuring, so nothing is guessed
# --------------------------------------------------------------------------

def wide(text, size, font):
    # these match the numbers the geometry check in build.py uses, so the
    # wrapper and the checker can never disagree about whether a line fits
    per = 0.601 if font == MONO else 0.55
    return len(text) * size * per


def flow(text, size, width, font=SERIF):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if wide(t, size, font) > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = t
    if cur:
        lines.append(cur)
    return lines


def txt(x, y, s, size=11, fill=INK, font=SERIF, weight=None, anchor=None,
        track=None, style=None, cls=None, italic=False):
    a = ['<text x="%.1f" y="%.1f" font-family="%s" font-size="%s" fill="%s"'
         % (x, y, font, size, fill)]
    if weight:
        a.append(' font-weight="%s"' % weight)
    if anchor:
        a.append(' text-anchor="%s"' % anchor)
    if track:
        a.append(' letter-spacing="%s"' % track)
    if italic:
        a.append(' font-style="italic"')
    if style:
        a.append(' style="%s"' % style)
    if cls:
        a.append(' class="%s"' % cls)
    a.append(">%s</text>" % esc(s))
    return "".join(a)


def rule(y, x0=M, x1=R, w=1, col=RULE):
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
            'stroke-width="%s"/>' % (x0, y, x1, y, col, w))


def vrule(x, y0, y1, col=RULE):
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s"/>'
            % (x, y0, x, y1, col))


def kicker(y, label):
    """A section head: rule, small caps in red, rule."""
    return [rule(y, w=1.6, col=INK),
            txt(M, y + 20, label, 10, RED, MONO, 700, track="3.4"),
            rule(y + 30)]


def asked():
    p = pathlib.Path(__file__).parent / "asked.json"
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except ValueError:
            pass
    return []


# --------------------------------------------------------------------------

def canvas(s):
    p = []
    today = datetime.datetime.now(datetime.timezone.utc)
    edition = s["repos"] if s else 38

    # ------------------------------------------------------------- masthead
    p.append(rule(34, w=3, col=INK))
    p.append(rule(40, w=1, col=INK))
    p.append(txt(W / 2, 104, "HASSAAN-UL-MUSTAFA", 50, INK, SERIF, 700,
                 anchor="middle", track="-1"))
    p.append(txt(W / 2, 126, "BUILDER OF AGENTS AND THE BACKENDS THEY RUN ON", 9.6,
                 SOFT, MONO, track="3.6", anchor="middle"))
    p.append(rule(142, w=1, col=INK))
    p.append(txt(M, 160, "ISLAMABAD, PAKISTAN", 9, FAINT, MONO, track="2"))
    p.append(txt(W / 2, 160, today.strftime("%A %d %B %Y").upper(), 9, FAINT, MONO,
                 track="2", anchor="middle"))
    p.append(txt(R, 160, "EDITION No. %d" % edition, 9, FAINT, MONO, track="2",
                 anchor="end"))
    p.append(rule(170, w=1.6, col=INK))

    y = 210

    # ----------------------------------------------------------------- lead
    lead = "The unglamorous parts are the product"
    p.append(txt(M, y, lead, 34, INK, SERIF, 700, track="-.8"))
    y += 26
    p.append(txt(M, y, "Computer Science at FAST-NUCES. Currently at Arbisoft.", 13,
                 SOFT, SERIF, italic=True))
    y += 26
    p.append(rule(y))
    y += 24

    # three columns of body text, with rules between them
    body = ("Most AI side projects stop at a notebook. These go out with rate "
            "limiting, input validation and row level security attached, because "
            "that is the part a client ends up depending on. "
            "The work worth having is the seat next to the person with the problem: "
            "find what it actually is, then build the thing that fixes it. "
            "Third place at the National AI Hackathon, and a listed production "
            "adopter of the Graph Context Framework for cross agent context.")
    lines = flow(body, 11.5, COL - 6)
    per = (len(lines) + 2) // 3
    top = y
    for c in range(3):
        cx = M + c * (COL + 18)
        chunk = lines[c * per:(c + 1) * per]
        for i, ln in enumerate(chunk):
            p.append(txt(cx, y + i * 16.5, ln, 11.5, INK))
        if c < 2:
            p.append(vrule(cx + COL + 9, top - 12, top + per * 16.5 - 4))
    y = top + per * 16.5 + 16

    # the three principles, set as a boxed standfirst
    p.append('<rect x="%d" y="%.1f" width="%.1f" height="74" fill="%s" '
             'stroke="%s"/>' % (M, y, R - M, PAPER2, RULE))
    for i, (num, title, ls) in enumerate(PRINCIPLES):
        cx = M + 16 + i * ((R - M - 32) / 3)
        p.append(txt(cx, y + 26, title.title(), 12.5, INK, SERIF, 700))
        p.append(txt(cx, y + 44, ls[0], 9.6, SOFT, SERIF))
        p.append(txt(cx, y + 58, ls[1], 9.6, SOFT, SERIF))
    y += 100

    # -------------------------------------------------------------- systems
    p += kicker(y, "THE WORK")
    y += 52
    for idx, (key, spec) in enumerate(SYSTEMS.items()):
        head, deck = STORIES[key]
        p.append(txt(M, y, head, 19, INK, SERIF, 700, track="-.4"))
        p.append(txt(R, y, spec["title"], 9, RED, MONO, track="1.8", anchor="end"))
        y += 20
        dl = flow(deck, 11, (R - M) * 0.56)
        for i, ln in enumerate(dl):
            p.append(txt(M, y + i * 15.5, ln, 11, SOFT))
        # the numbers sit in the right hand margin, like a fact box
        bx = M + (R - M) * 0.62
        p.append(vrule(bx - 14, y - 14, y + len(dl) * 15.5 - 2))
        for j, (val, cap) in enumerate(spec["metrics"][:4]):
            p.append(txt(bx, y + j * 17, val, 12.5, INK, SERIF, 700))
            p.append(txt(bx + 62, y + j * 17, cap.lower(), 8.6, FAINT, MONO))
        y += max(len(dl) * 15.5, 4 * 17) + 10
        p.append(txt(M, y, spec["stack"], 8.8, FAINT, MONO))
        y += 16
        if idx < len(SYSTEMS) - 1:
            p.append(rule(y))
            y += 22
    y += 10

    # ------------------------------------------------------ by the numbers
    p += kicker(y, "BY THE NUMBERS")
    y += 50
    if s:
        cells = [(str(s["repos"]), "public repositories"),
                 (str(s["stars"]), "stars earned"),
                 (str(len(s["langs"])), "languages"),
                 (s["pushed"], "last shipped")]
        for i, (big, cap) in enumerate(cells):
            cx = M + i * ((R - M) / 4)
            size = 34 if len(big) <= 4 else 19
            p.append(txt(cx, y, big, size, INK, SERIF, 700))
            p.append(txt(cx, y + 17, cap, 9, FAINT, MONO))
        y += 42
        total = sum(c for _, c in s["langs"]) or 1
        shown = s["langs"][:6]
        other = sum(c for _, c in s["langs"][6:])
        segs = shown + ([("Other", other)] if other else [])
        shade = ["#17150f", "#4a463c", "#6f6a5c", "#8a8375", "#a49d8c", "#bdb5a2", RED]
        x = float(M)
        for i, (name, count) in enumerate(segs):
            seg = (R - M) * count / total
            p.append('<rect x="%.1f" y="%.1f" width="%.1f" height="9" fill="%s"/>'
                     % (x, y, max(seg - 2, 1), shade[i % len(shade)]))
            x += seg
        y += 24
        lx = float(M)
        for i, (name, count) in enumerate(segs):
            p.append('<rect x="%.1f" y="%.1f" width="7" height="7" fill="%s"/>'
                     % (lx, y - 7, shade[i % len(shade)]))
            p.append(txt(lx + 12, y, "%s %d" % (name, count), 9.6, SOFT, MONO))
            lx += 26 + wide("%s %d" % (name, count), 9.6, MONO)
        y += 26

    # ---------------------------------------------------------- toolchain
    p += kicker(y, "TOOLS OF THE TRADE")
    y += 50
    for lab, items in TOOLCHAIN:
        p.append(txt(M, y, lab, 8.8, RED, MONO, track="1.8"))
        for i, ln in enumerate(flow(items, 11, R - M - 120, SERIF)):
            p.append(txt(M + 116, y + i * 15, ln, 11, INK))
        y += 24
    y += 6

    # ------------------------------------------------------------- letters
    p += kicker(y, "LETTERS TO THE EDITOR")
    y += 50
    p.append(txt(M, y, "This paper answers correspondence. Open an issue titled "
                       "agent: with your question and", 11, SOFT, SERIF, italic=True))
    y += 16
    p.append(txt(M, y, "the reply is set in the next edition, usually within a minute. "
                       "Links sit below the paper.", 11, SOFT, SERIF, italic=True))
    y += 26

    log = asked()
    if not log:
        p.append(txt(M, y, "No letters yet.", 11, FAINT, SERIF, italic=True))
        y += 22
    for item in log[:3]:
        p.append(txt(M, y, chr(8220) + str(item.get("q", ""))[:74] + chr(8221),
                     12, INK, SERIF, 700))
        p.append(txt(R, y, "@" + str(item.get("who", ""))[:22], 8.8, FAINT, MONO,
                     anchor="end"))
        y += 17
        for ln in flow(str(item.get("a", "")), 10.5, R - M - 16)[:3]:
            p.append(txt(M + 14, y, ln, 10.5, SOFT))
            y += 14
        y += 14
    y += 4

    # -------------------------------------------------------------- folio
    p.append(rule(y, w=1.6, col=INK))
    y += 20
    p.append(txt(M, y, "SET AND PRINTED BY assets/build.py", 8.8, FAINT, MONO,
                 track="1.8"))
    p.append(txt(W / 2, y, "%d" % edition, 8.8, FAINT, MONO, anchor="middle"))
    p.append(txt(R, y, "github.com/Hassaan146", 8.8, FAINT, MONO, track="1.8",
                 anchor="end"))
    y += 26

    h = y
    css = (".ink{animation:ink 1.2s ease-out both}"
           "@keyframes ink{from{opacity:0}to{opacity:1}}" + REDUCE)
    label = ("Hassaan-ul-Mustafa, builder of agents and the backends they run on, "
             "Islamabad. Edition number %d, %s. Lead: the unglamorous parts are the "
             "product. Computer Science at FAST-NUCES, currently at Arbisoft. Five "
             "systems: %s. %s"
             % (edition, today.strftime("%d %B %Y"),
                ", ".join(v["title"].title() for v in SYSTEMS.values()),
                ("%d public repositories, %d stars, last shipped %s."
                 % (s["repos"], s["stars"], s["pushed"])) if s else ""))

    front = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %.0f" width="%d" '
             'height="%.0f" role="img" aria-label="%s">' % (W, h, W, h, esc(label)),
             '<defs><linearGradient id="pg" x1="0" y1="0" x2="1" y2="1">'
             '<stop offset="0%%" stop-color="%s"/><stop offset="100%%" stop-color="%s"/>'
             '</linearGradient></defs>' % (PAPER, PAPER2),
             "<style>%s</style>" % css,
             '<rect width="%d" height="%.0f" fill="url(#pg)"/>' % (W, h)]
    return chr(10).join(front + p + ["</svg>"]) + chr(10)
