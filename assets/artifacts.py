"""One bespoke artifact per project.

The idea. A README that describes five projects in five paragraphs reads like
every other README, because a paragraph looks the same whatever it is about.
So each project here draws the thing it actually produces: the plugin shows a
decision gate holding, the aggregator shows the digest that lands in your inbox,
the travel engine shows a ranked answer with its tradeoff written out, the mesh
shows a message walking between phones, the agent org shows its dependency graph.

Existing tools in this space record a real terminal (asciinema, term-to-svg).
These are drawn, because four of the five produce something that is not a
terminal at all, and because a drawing can be sized to the page and themed to
match the rest of it.

Everything is representative of real behaviour and labelled as a sample, so
nobody mistakes it for a screenshot of live data.

Glyphs are drawn as paths, never as characters, so a missing font can never
turn a tick into a box.
"""

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SANS = "Segoe UI, ui-sans-serif, -apple-system, Helvetica, Arial, sans-serif"
CW = 0.601

PAD_L = 64
PANEL_W = 872


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def mw(text, size):
    return len(text) * size * CW


# --- small drawn marks -----------------------------------------------------

def tick(x, y, col, s=1.0):
    return (f'<path d="M{x} {y} l{3.4 * s} {3.6 * s} l{6.6 * s} {-7.4 * s}" fill="none" '
            f'stroke="{col}" stroke-width="{1.9 * s}" stroke-linecap="round" '
            f'stroke-linejoin="round"/>')


def chevron(x, y, col, s=1.0):
    return (f'<path d="M{x} {y - 3.4 * s} l{3.8 * s} {3.4 * s} l{-3.8 * s} {3.4 * s}" '
            f'fill="none" stroke="{col}" stroke-width="{1.6 * s}" stroke-linecap="round" '
            f'stroke-linejoin="round"/>')


def dot(x, y, col, r=3.2):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}"/>'


def phone(x, y, col, w=17, h=28):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="none" '
            f'stroke="{col}" stroke-width="1.3"/>'
            f'<line x1="{x + 5}" y1="{y + h - 4}" x2="{x + w - 5}" y2="{y + h - 4}" '
            f'stroke="{col}" stroke-width="1.1"/>')


def chrome(t, y, h, label, right=""):
    """Panel with a hairline border and a small caps label above it."""
    p = [f'<text x="{PAD_L}" y="{y - 9}" font-family="{MONO}" font-size="8.8" '
         f'fill="{t["faint"]}" letter-spacing="1.9">{esc(label)}</text>']
    if right:
        p.append(f'<text x="{PAD_L + PANEL_W}" y="{y - 9}" font-family="{MONO}" '
                 f'font-size="8.8" fill="{t["faint"]}" letter-spacing="1.4" '
                 f'text-anchor="end">{esc(right)}</text>')
    p.append(f'<rect x="{PAD_L}" y="{y}" width="{PANEL_W}" height="{h}" rx="5" '
             f'fill="{t["accent"]}" fill-opacity=".025" stroke="{t["rule"]}"/>')
    return p


def line(t, x, y, text, col=None, size=11.5, weight=None):
    w = f' font-weight="{weight}"' if weight else ""
    return (f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="{size}" '
            f'fill="{col or t["dim"]}"{w}>{esc(text)}</text>')


# --- 01 Forge Mentor, a decision gate holding ------------------------------

def forge(t):
    top, h = 22, 214
    x = PAD_L + 22
    p = chrome(t, top, h, "WHAT IT LOOKS LIKE WHEN THE GATE HOLDS", "sample session")
    y = top + 30
    p.append(line(t, x, y, "$ claude", t["faint"]))
    y += 24
    p.append(dot(x + 4, y - 4, t["accent"], 3.4))
    p.append(line(t, x + 16, y, "forge  one decision before the store layer", t["accent"], 11.5, 600))
    y += 26
    p.append(line(t, x, y, "Q   how should sessions persist?", t["ink"], 11.5, 600))
    y += 22
    for k, v in (("A", "signed cookie      stateless, 4 KB cap, no revocation"),
                 ("B", "redis session id   revocable, needs a Redis you run"),
                 ("C", "database session   revocable, one more query per request")):
        p.append(line(t, x, y, f"{k}   {v}", t["dim"], 11))
        y += 19
    y += 4
    p.append(line(t, x, y, "recommend B if Redis already runs, otherwise C", t["accent2"], 10.8))
    y += 26
    p.append(chevron(x + 1, y - 4, t["ink"]))
    p.append(line(t, x + 16, y, "your call: C", t["ink"], 11.5, 600))
    y += 22
    p.append(tick(x, y - 5, t["good"]))
    p.append(line(t, x + 16, y, "recorded   .claude/forge/0007-sessions.md", t["dim"], 11))
    y += 19
    p.append(tick(x, y - 5, t["good"]))
    p.append(line(t, x + 16, y, "gate open, writing code", t["dim"], 11))
    return p, top + h


# --- 02 AI News Aggregator, the digest that lands --------------------------

DIGEST = [
    ("model release", "lab blog"),
    ("policy update", "regulator"),
    ("benchmark result", "research paper"),
    ("funding round", "newsletter"),
    ("tooling launch", "product blog"),
]


def news(t):
    top, h = 22, 214
    x = PAD_L + 22
    p = chrome(t, top, h, "WHAT LANDS IN YOUR INBOX", "sample digest")
    y = top + 32
    p.append(f'<text x="{x}" y="{y}" font-family="{SANS}" font-size="15" font-weight="700" '
             f'fill="{t["ink"]}">Your AI digest</text>')
    p.append(f'<text x="{PAD_L + PANEL_W - 22}" y="{y}" font-family="{MONO}" font-size="10" '
             f'fill="{t["faint"]}" text-anchor="end">07:00 daily</text>')
    y += 16
    p.append(f'<line x1="{x}" y1="{y}" x2="{PAD_L + PANEL_W - 22}" y2="{y}" '
             f'stroke="{t["rule"]}"/>')
    y += 26
    for i, (kind, src) in enumerate(DIGEST):
        p.append(f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="11" '
                 f'fill="{t["accent"]}">{i + 1}</text>')
        p.append(line(t, x + 22, y, kind, t["ink"], 11.5))
        p.append(f'<text x="{x + 250}" y="{y}" font-family="{MONO}" font-size="10" '
                 f'fill="{t["faint"]}">{esc(src)}</text>')
        # the summary, drawn as measured rules so no headline is invented
        for j, wdt in enumerate((300, 214)):
            p.append(f'<rect x="{x + 400}" y="{y - 8 + j * 7}" width="{wdt}" height="2.4" '
                     f'rx="1.2" fill="{t["dim"]}" opacity="{0.34 - j * 0.12}"/>')
        y += 27
    y += 2
    p.append(f'<line x1="{x}" y1="{y - 14}" x2="{PAD_L + PANEL_W - 22}" y2="{y - 14}" '
             f'stroke="{t["rule"]}"/>')
    p.append(line(t, x, y + 4, "5 kept from 412 collected  ·  Groq wrote them  ·  Gemini on standby",
                  t["faint"], 10))
    return p, top + h


# --- 03 SkyElite AI, a ranked answer with its tradeoff ---------------------

RANK = [
    ("LISBON", "PT", 84, [("safety", .82), ("budget", .91), ("visa", .95), ("scenery", .70)],
     "cheaper than Zurich, and wetter through November", "0.78", "6"),
    ("TBILISI", "GE", 79, None, None, None, None),
    ("MEDELLIN", "CO", 74, None, None, None, None),
]


def skyelite(t):
    top, h = 22, 214
    x = PAD_L + 22
    p = chrome(t, top, h, "WHAT IT HANDS BACK", "sample ranking")
    name, cc, score, bars, trade, conf, srcs = RANK[0]
    y = top + 36
    p.append(f'<text x="{x}" y="{y}" font-family="{SANS}" font-size="20" font-weight="700" '
             f'fill="{t["ink"]}" letter-spacing="-.5">{name}</text>')
    p.append(f'<text x="{x + mw(name, 20) * 0.92 + 12}" y="{y}" font-family="{MONO}" '
             f'font-size="11" fill="{t["faint"]}">{cc}</text>')
    p.append(f'<text x="{PAD_L + PANEL_W - 22}" y="{y}" font-family="{SANS}" font-size="22" '
             f'font-weight="700" fill="{t["accent"]}" text-anchor="end">{score}</text>')
    p.append(f'<text x="{PAD_L + PANEL_W - 22}" y="{y + 14}" font-family="{MONO}" '
             f'font-size="8.6" fill="{t["faint"]}" letter-spacing="1.4" '
             f'text-anchor="end">SCORE</text>')
    y += 22
    for i, (lab, frac) in enumerate(bars):
        bx = x + i * 196
        p.append(f'<text x="{bx}" y="{y + 12}" font-family="{MONO}" font-size="9.4" '
                 f'fill="{t["faint"]}" letter-spacing="1.2">{lab.upper()}</text>')
        p.append(f'<rect x="{bx}" y="{y + 20}" width="150" height="4" rx="2" '
                 f'fill="{t["rule"]}"/>')
        p.append(f'<rect x="{bx}" y="{y + 20}" width="{150 * frac:.0f}" height="4" rx="2" '
                 f'fill="{t["accent"]}"/>')
    y += 48
    p.append(f'<line x1="{x}" y1="{y}" x2="{PAD_L + PANEL_W - 22}" y2="{y}" '
             f'stroke="{t["rule"]}"/>')
    y += 22
    p.append(line(t, x, y, "tradeoff", t["faint"], 9.6))
    p.append(line(t, x + 76, y, trade, t["dim"], 11))
    y += 20
    p.append(line(t, x, y, "confidence", t["faint"], 9.6))
    p.append(line(t, x + 76, y, f"{conf}   from {srcs} sources", t["dim"], 11))
    y += 26
    for nm, c2, sc, *_ in RANK[1:]:
        p.append(line(t, x, y, f"{nm}", t["faint"], 11))
        p.append(f'<text x="{x + 110}" y="{y}" font-family="{MONO}" font-size="10" '
                 f'fill="{t["faint"]}">{c2}</text>')
        p.append(f'<text x="{x + 150}" y="{y}" font-family="{MONO}" font-size="11" '
                 f'fill="{t["faint"]}">{sc}</text>')
        y += 17
    return p, top + h


# --- 04 BitMadWall, a message walking across the mesh ----------------------

def bitmadwall(t):
    top, h = 22, 214
    x = PAD_L + 22
    p = chrome(t, top, h, "HOW A MESSAGE TRAVELS WITH NO NETWORK", "sample relay")
    y = top + 46
    labels = ["you", "relay", "relay", "amina"]
    hops = ["Bluetooth LE", "Wi-Fi Direct", "LoRa 2 km"]
    step = 206
    for i, lab in enumerate(labels):
        px = x + i * step
        p.append(phone(px, y, t["accent"]))
        p.append(f'<text x="{px + 8.5}" y="{y + 44}" font-family="{MONO}" font-size="10" '
                 f'fill="{t["dim"]}" text-anchor="middle">{lab}</text>')
        if i < 3:
            p.append(f'<path class="e" d="M{px + 26} {y + 14} H{px + step - 10}" '
                     f'stroke="{t["accent"]}" stroke-opacity=".55" stroke-width="1" '
                     f'stroke-dasharray="2.5 4.5"/>')
            p.append(chevron(px + step - 12, y + 14, t["accent"]))
            p.append(f'<text x="{px + 26 + (step - 36) / 2}" y="{y + 6}" font-family="{MONO}" '
                     f'font-size="8.8" fill="{t["faint"]}" text-anchor="middle" '
                     f'letter-spacing="1">{hops[i]}</text>')
    y += 78
    p.append(f'<rect x="{x}" y="{y}" width="286" height="34" rx="5" fill="{t["accent"]}" '
             f'fill-opacity=".1" stroke="{t["accent"]}" stroke-opacity=".4"/>')
    p.append(line(t, x + 14, y + 21, "convoy is at the bridge", t["ink"], 11.5))
    p.append(tick(x + 306, y + 16, t["good"]))
    p.append(line(t, x + 324, y + 21, "delivered  ·  3 hops  ·  0 servers", t["dim"], 11))
    y += 48
    p.append(f'<rect x="{x}" y="{y}" width="286" height="30" rx="5" fill="none" '
             f'stroke="{t["rule"]}" stroke-dasharray="3 4"/>')
    p.append(line(t, x + 14, y + 19, "supplies, grid 44B", t["faint"], 11))
    p.append(line(t, x + 324, y + 19, "queued 42 min, no peer in range yet", t["faint"], 10.5))
    return p, top + h


# --- 05 AI Employee OS, the graph it builds from a sentence ---------------

def employeeos(t):
    top, h = 22, 214
    x = PAD_L + 22
    p = chrome(t, top, h, "ONE SENTENCE IN, A DEPENDENCY GRAPH OUT", "sample run")
    y = top + 30
    p.append(f'<rect x="{x}" y="{y}" width="{PANEL_W - 44}" height="30" rx="5" '
             f'fill="{t["accent"]}" fill-opacity=".08" stroke="{t["accent"]}" '
             f'stroke-opacity=".35"/>')
    p.append(line(t, x + 14, y + 20,
                  '"find three suppliers, check their prices, draft the outreach"',
                  t["ink"], 11.5))
    y += 56
    agents = [("research agent", "finds the three"),
              ("ops agent", "prices each one"),
              ("writer agent", "drafts the email")]
    colw = 250
    for i, (nm, what) in enumerate(agents):
        ax = x + i * (colw + 20)
        p.append(f'<rect x="{ax}" y="{y}" width="{colw}" height="46" rx="4" fill="none" '
                 f'stroke="{t["accent"]}" stroke-opacity=".38"/>')
        p.append(f'<rect x="{ax}" y="{y}" width="3" height="46" fill="{t["accent"]}" '
                 f'opacity=".65"/>')
        p.append(line(t, ax + 14, y + 20, nm, t["ink"], 11.5, 600))
        p.append(line(t, ax + 14, y + 36, what, t["faint"], 10))
        p.append(f'<path d="M{ax + colw / 2} {y - 14} V{y - 2}" stroke="{t["accent"]}" '
                 f'stroke-opacity=".4" stroke-width="1"/>')
        if i:
            p.append(f'<path d="M{x + colw / 2} {y - 14} H{ax + colw / 2}" '
                     f'stroke="{t["accent"]}" stroke-opacity=".4" stroke-width="1"/>')
    p.append(f'<text x="{x + colw + 20 + colw + 20 + colw + 8}" y="{y + 26}" '
             f'font-family="{MONO}" font-size="9" fill="{t["faint"]}"></text>')
    y += 76
    p.append(f'<path d="M{x + colw / 2} {y - 22} V{y - 10} H{x + PANEL_W - 66} V{y - 4}" '
             f'fill="none" stroke="{t["accent"]}" stroke-opacity=".3" stroke-width="1"/>')
    p.append(tick(x, y + 4, t["good"]))
    p.append(line(t, x + 18, y + 9, "ops agent waited for research, then ran", t["dim"], 11))
    y += 20
    p.append(tick(x, y + 4, t["good"]))
    p.append(line(t, x + 18, y + 9,
                  "every step timed, logged and replayable from the trace", t["dim"], 11))
    return p, top + h


ARTIFACTS = {
    "forge": forge,
    "news": news,
    "skyelite": skyelite,
    "bitmadwall": bitmadwall,
    "employeeos": employeeos,
}
