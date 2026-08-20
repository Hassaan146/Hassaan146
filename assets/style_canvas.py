"""One canvas.

The page used to alternate image, text block, image, text block, nine times
over, and no amount of restyling the pieces fixed the fact that it read as
pieces. This draws the whole thing as a single continuous sheet instead: one
file, one ground, one grid, hairline rules where a section ends.

Width is 900 rather than 1000, because GitHub renders a profile README in a
column around 890 wide. At 1000 everything was being scaled down by a tenth and
the small type suffered for it. At 900 it lands close to one to one.

Links cannot live in here. An SVG loaded through an img tag is not interactive
on GitHub, so anchors inside it would render but never respond. The canvas holds
the visuals and one compact row of real markdown links sits underneath it.

Palette is the instrumentation one: a neutral ground with no colour cast, bone
type, a graphite mesh, and a single desaturated ochre for the things worth
pointing at. Nothing glows.
"""

import json
import math
import pathlib

from build import (CW, MONO, PRINCIPLES, REDUCE, SANS, SYSTEMS, esc, mono_w)

CW_ = CW
BG0, BG1 = "#0d0d0e", "#08080a"
INK, DIM, FAINT = "#ece9e4", "#9a958d", "#5f5c57"
LINE = "#232329"
ACC, ACC2 = "#c08a3e", "#8d6b3a"

W = 900
M = 56                     # side margin
R = W - M                  # right edge

TOOLCHAIN = [
    ("LANGUAGES", ["Python", "TypeScript", "JavaScript", "C++", "Java", "SQL", "x86"]),
    ("AI", ["LangGraph", "LangChain", "MCP", "Anthropic", "Groq", "Gemini", "Pydantic"]),
    ("BACKEND", ["FastAPI", "Django", "DRF", "Node", "Express", "Celery"]),
    ("FRONTEND", ["React", "Next.js", "Vite", "Tailwind", "Three.js"]),
    ("DATA", ["PostgreSQL", "Supabase", "MongoDB", "Redis", "MySQL", "SQL Server"]),
    ("SHIP", ["Docker", "Git", "Linux", "Vercel", "Render", "Railway", "Stripe"]),
]

TONE = [ACC, "#a8a29a", ACC2, "#7d7871", "#5f5c57", "#4a4744", "#3a3835"]


def wrap(text, size, width):
    """Break a line to fit the sheet, measured rather than guessed."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if mono_w(trial, size) > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


def asked():
    p = pathlib.Path(__file__).parent / "asked.json"
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except ValueError:
            pass
    return []


def txt(x, y, s, size=11, fill=None, font=None, weight=None, anchor=None,
        track=None, cls=None, style=None, op=None):
    a = ['<text x="%.1f" y="%.1f" font-family="%s" font-size="%s" fill="%s"'
         % (x, y, font or MONO, size, fill or DIM)]
    if weight:
        a.append(' font-weight="%s"' % weight)
    if anchor:
        a.append(' text-anchor="%s"' % anchor)
    if track:
        a.append(' letter-spacing="%s"' % track)
    if cls:
        a.append(' class="%s"' % cls)
    if style:
        a.append(' style="%s"' % style)
    if op:
        a.append(' opacity="%s"' % op)
    a.append(">%s</text>" % esc(s))
    return "".join(a)


def rule(y, x0=M, x1=R, col=LINE, op="1"):
    return ('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-opacity="%s"/>'
            % (x0, y, x1, y, col, op))


def marker(y, label):
    """Section head: a short ochre bar, the number, and the name."""
    p = [rule(y),
         '<rect x="%d" y="%.1f" width="34" height="3" fill="%s"/>' % (M, y, ACC),
         txt(M, y + 30, label, 10.5, ACC, track="3.6")]
    return p


def scale(y, x0, x1, n=12):
    p = [rule(y, x0, x1)]
    for i in range(n + 1):
        tx = x0 + (x1 - x0) * i / n
        long = i % 4 == 0
        p.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                 'stroke-opacity="%s"/>' % (tx, y, tx, y - (6 if long else 3),
                                            ACC if long else LINE, ".65" if long else "1"))
    return p


def canvas(s):
    """s is the live stats dict, or None when the API could not be reached."""
    p = []
    y = 0.0

    # ---------------------------------------------------------------- masthead
    y = 300
    p.append(txt(M, 62, "AI ENGINEER / PRODUCT AND BACKEND", 10.5, ACC, track="4"))
    p.append(txt(R, 62, "ISLAMABAD, PK", 10.5, FAINT, track="2.4", anchor="end"))
    p.append(txt(M - 2, 148, "MUHAMMAD", 52, INK, SANS, 700, track="-2.2"))
    p.append(txt(M - 2, 202, "HASSAAN", 52, INK, SANS, 700, track="-2.2"))
    p.append('<rect x="%d" y="222" width="124" height="3" fill="%s"/>' % (M, ACC))
    p.append(txt(M, 258, "I build AI agents and the backends they run on.", 13.5, DIM))

    # the mechanism, top right of the masthead
    for i, (r, dur) in enumerate(((26, 15), (45, 24), (64, 38))):
        p.append('<circle cx="742" cy="150" r="%d" fill="none" stroke="%s"/>' % (r, LINE))
        p.append('<g class="orb" style="animation-duration:%ss%s">'
                 % (dur, ";animation-direction:reverse" if i == 1 else ""))
        for k in range(i + 1):
            a = 2 * math.pi * k / (i + 1)
            p.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>'
                     % (742 + r * math.cos(a), 150 + r * math.sin(a),
                        4 - i * 0.5, ACC if k == 0 else ACC2))
        p.append("</g>")
    p.append('<circle class="tick" cx="742" cy="150" r="7.5" fill="%s"/>' % ACC)
    p.append(txt(742, 238, "DATA / API / AGENTS", 9, FAINT, track="1.8", anchor="middle"))

    # ---------------------------------------------------------------- identity
    p += marker(y, "00 / IDENTITY")
    y += 52
    p.append(txt(M, y, "Computer Science at FAST-NUCES, currently at Arbisoft. Most AI side "
                       "projects stop at a", 12, DIM, SANS))
    y += 19
    p.append(txt(M, y, "notebook. Mine go out with the unglamorous parts attached, because "
                       "that is what a client", 12, DIM, SANS))
    y += 19
    p.append(txt(M, y, "ends up depending on.", 12, DIM, SANS))
    y += 34
    colw = (R - M - 40) / 3
    for i, (num, title, lines) in enumerate(PRINCIPLES):
        x = M + i * (colw + 20)
        p.append('<rect class="tick" style="animation-delay:%ss" x="%.1f" y="%.1f" '
                 'width="26" height="2" fill="%s"/>' % (round(i * .7, 2), x, y, ACC))
        p.append(txt(x, y + 26, title, 11.5, INK, SANS, 700))
        for j, ln in enumerate(lines):
            p.append(txt(x, y + 46 + j * 15, ln, 10.5, FAINT))
    y += 92
    p.append(txt(M, y, "3rd Place, National AI Hackathon   /   production adopter, "
                       "Graph Context Framework", 10.5, ACC))
    y += 30

    # ----------------------------------------------------------------- systems
    p += marker(y, "01 / SYSTEMS")
    y += 48
    for key, spec in SYSTEMS.items():
        p.append(txt(M, y, spec["title"], 22, INK, SANS, 700, track="-.7"))
        p.append(txt(R, y, spec["n"], 22, ACC, SANS, 700, anchor="end", op=".4"))
        y += 18
        p.append(txt(M, y, spec["meta"], 9, FAINT, track="1.7"))
        y += 26

        nodes = spec["nodes"]
        widths = [mono_w(n, 10.5) + 20 for n in nodes]
        gap = 16
        total = sum(widths) + gap * (len(nodes) - 1)
        x = float(M)
        scl = min(1.0, (R - M) / total)
        for i, (label, bw) in enumerate(zip(nodes, widths)):
            bw *= scl
            p.append('<rect x="%.1f" y="%.1f" width="%.1f" height="24" fill="none" '
                     'stroke="%s"/>' % (x, y, bw, LINE))
            p.append(txt(x + bw / 2, y + 16, label, 10.5 * scl, DIM, anchor="middle"))
            if i < len(nodes) - 1:
                p.append('<path class="dash" d="M%.1f %.1f H%.1f" stroke="%s" '
                         'stroke-opacity=".8"/>'
                         % (x + bw + 4, y + 12, x + bw + gap * scl - 4, ACC2))
            x += bw + gap * scl
        y += 38
        p.append(txt(M, y, spec["note"], 10, FAINT))
        y += 26

        for i, (val, cap) in enumerate(spec["metrics"]):
            cx = M + i * ((R - M) / 4)
            p.append(txt(cx, y, val, 19, INK, SANS, 700, track="-.5"))
            p.append(txt(cx, y + 15, cap, 8.2, FAINT, track="1.4"))
        y += 34
        p.append(txt(M, y, spec["stack"], 9.6, DIM))
        y += 26
        p.append(rule(y - 8, op=".7"))
        y += 20

    # --------------------------------------------------------------- toolchain
    y -= 12
    p += marker(y, "02 / TOOLCHAIN")
    y += 40
    for lab, items in TOOLCHAIN:
        p.append(txt(M, y + 16, lab, 9, FAINT, track="1.8"))
        x = float(M + 116)
        for j, it in enumerate(items):
            if j:
                p.append(txt(x, y + 16, "/", 11.5, LINE))
                x += mono_w("/", 11.5) + 10
            p.append(txt(x, y + 16, it, 11.5, INK))
            x += mono_w(it, 11.5) + 10
        y += 30
        p.append(rule(y - 8, op=".6"))
    y += 20

    # ----------------------------------------------------------------- signals
    p += marker(y, "03 / SIGNALS")
    y += 52
    if s is not None:
        cells = [(str(s["repos"]), "PUBLIC REPOS"), (str(s["stars"]), "STARS EARNED"),
                 (str(len(s["langs"])), "LANGUAGES"), (s["pushed"], "LAST SHIPPED")]
        for i, (big, cap) in enumerate(cells):
            cx = M + i * ((R - M) / 4)
            size = 34 if len(big) <= 4 else 20
            p.append(txt(cx, y, big, size, ACC if i == 0 else INK, SANS, 700, track="-1.2"))
            p.append(txt(cx, y + 18, cap, 8.6, FAINT, track="1.6"))
        y += 48

        total = sum(c for _, c in s["langs"]) or 1
        shown = s["langs"][:6]
        other = sum(c for _, c in s["langs"][6:])
        segs = shown + ([("Other", other)] if other else [])
        bw = R - M
        x = float(M)
        for i, (name, count) in enumerate(segs):
            seg = bw * count / total
            p.append('<rect x="%.1f" y="%.1f" width="%.1f" height="11" fill="%s"/>'
                     % (x, y, max(seg - 3, 1), TONE[i % len(TONE)]))
            x += seg
        y += 30
        lx = float(M)
        for i, (name, count) in enumerate(segs):
            p.append('<rect x="%.1f" y="%.1f" width="7" height="7" fill="%s"/>'
                     % (lx, y - 7, TONE[i % len(TONE)]))
            p.append(txt(lx + 12, y, "%s %d" % (name, count), 10, DIM))
            lx += 28 + mono_w("%s %d" % (name, count), 10)
        y += 26
    p += scale(y, M, R)
    y += 40

    # --------------------------------------------------------------------- ask
    p += marker(y, "04 / ASK IT SOMETHING")
    y += 50
    p.append(txt(M, y, "This sheet answers back. Open an issue titled agent: and your "
                       "question, and a", 12, DIM, SANS))
    y += 19
    p.append(txt(M, y, "workflow routes it, writes the reply here, then closes the issue. "
                       "Links are below.", 12, DIM, SANS))
    y += 34

    log = asked()
    if not log:
        p.append(txt(M, y, "Nobody has asked anything yet. Be the first.", 11, FAINT))
        y += 26
    for item in log[:3]:
        p.append('<rect x="%d" y="%.1f" width="3" height="%d" fill="%s"/>'
                 % (M, y - 11, 40, ACC))
        p.append(txt(M + 14, y, item.get("q", "")[:78], 11.5, INK))
        p.append(txt(R, y, "@" + str(item.get("who", ""))[:24], 9, FAINT, anchor="end"))
        y += 17
        for ln in wrap(str(item.get("a", "")), 10.5, R - M - 14)[:3]:
            p.append(txt(M + 14, y, ln, 10.5, DIM))
            y += 15
        y += 16
    y += 6

    # --------------------------------------------------------------- colophon
    p.append(txt(M, y, "EVERY MARK ON THIS SHEET IS DRAWN BY A SCRIPT IN THIS REPO",
                 9.6, FAINT, track="2.2"))
    p.append(txt(R, y, "assets/build.py", 9.6, ACC, track="2.2", anchor="end", cls="tick"))
    y += 40

    h = y
    css = ("@keyframes spin{to{transform:rotate(360deg)}}"
           ".orb{transform-box:view-box;transform-origin:742px 150px;"
           "animation:spin linear infinite}"
           ".tick{animation:tk 5s ease-in-out infinite}"
           "@keyframes tk{0%,100%{opacity:.4}18%{opacity:1}42%{opacity:.4}}"
           ".dash{stroke-dasharray:2 5;animation:d 2s linear infinite}"
           "@keyframes d{to{stroke-dashoffset:-7}}" + REDUCE)
    label = ("Muhammad Hassaan-ul-Mustafa, AI engineer, product and backend, Islamabad. "
             "I build AI agents and the backends they run on. Five systems: "
             + ", ".join(v["title"].title() for v in SYSTEMS.values())
             + ". Toolchain across languages, AI, backend, frontend, data and shipping. "
             + ("%d public repositories, %d stars, last shipped %s."
                % (s["repos"], s["stars"], s["pushed"]) if s else ""))

    front = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %.0f" width="%d" '
             'height="%.0f" role="img" aria-label="%s">' % (W, h, W, h, esc(label)),
             '<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
             '<stop offset="0%%" stop-color="%s"/><stop offset="100%%" stop-color="%s"/>'
             '</linearGradient>'
             '<pattern id="mesh" width="22" height="22" patternUnits="userSpaceOnUse">'
             '<path d="M22 0H0V22" fill="none" stroke="%s" stroke-width="1"/></pattern>'
             '</defs>' % (BG0, BG1, LINE),
             "<style>%s</style>" % css,
             '<rect width="%d" height="%.0f" fill="url(#bg)"/>' % (W, h),
             '<rect width="%d" height="%.0f" fill="url(#mesh)" opacity=".45"/>' % (W, h),
             # the sheet edge, so it reads as one drawing
             '<rect x="20" y="20" width="%d" height="%.0f" fill="none" stroke="%s"/>'
             % (W - 40, h - 40, LINE)]
    return chr(10).join(front + p + ["</svg>"]) + chr(10)
