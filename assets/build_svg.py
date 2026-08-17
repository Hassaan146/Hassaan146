"""Generates the SVG art used by the profile README.

Run from the repo root:   python assets/build_svg.py

Two kinds of output:
  about-{dark,light}.svg   the spec card at the top of the About section
  flow-*.svg               one pipeline strip per featured project

The flow strips carry no background of their own and use colours that hold up
on both GitHub themes, so each one is a single file.
"""

import pathlib

OUT = pathlib.Path(__file__).parent

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SANS = "ui-sans-serif, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"

ACCENT = "#58a6ff"
NEUTRAL = "#7d8590"  # readable on #0d1117 and on #ffffff


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# --------------------------------------------------------------------------
# pipeline strips
# --------------------------------------------------------------------------

FLOWS = {
    "bitmadwall": dict(
        nodes=["your phone", "relay", "relay", "recipient"],
        mark=None,
        note="Bluetooth LE / Wi-Fi Direct / LoRa  ·  up to 7 hops  ·  no server anywhere",
    ),
    "skyelite": dict(
        nodes=["intake", "filter", "visa", "research", "scoring", "tradeoff", "final"],
        mark=4,
        note="LangGraph StateGraph  ·  7 nodes  ·  every call has a mock fallback",
    ),
    "asme": dict(
        nodes=["scrape", "store", "rank", "summarise", "email"],
        mark=3,
        note="164 sites and 36 YouTube channels  ·  top 5 per user, daily",
    ),
    "forge": dict(
        nodes=["question", "options", "you decide", "recorded", "code runs"],
        mark=2,
        note="the gate holds until the decision exists",
    ),
    "employeeos": dict(
        nodes=["request", "decompose", "route to agents", "validate", "trace"],
        mark=2,
        note="dependency-aware workflow, execution trace shown back to you",
    ),
    "fashion": dict(
        nodes=["DM", "intent + entities", "rank catalog", "order state", "reply"],
        mark=1,
        note="11 intent types  ·  drops to keyword matching with no API key",
    ),
    "paytrace": dict(
        nodes=["invoice + bank", "exact", "vendor ref", "tolerant", "partial"],
        mark=None,
        note="four matching passes, each one looser than the last",
    ),
}

FS = 11.5          # node label size
CW = FS * 0.605    # monospace advance
PAD = 13           # horizontal padding inside a node
GAP = 26           # space between nodes
H = 27             # node height


def flow_svg(nodes, note, mark):
    widths = [len(n) * CW + PAD * 2 for n in nodes]
    total = sum(widths) + GAP * (len(nodes) - 1)
    w = int(total) + 4
    h = 74
    y = 20

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" '
        f'height="{h}" role="img" aria-label="{esc(" then ".join(nodes))}">',
        '<defs><marker id="a" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" '
        'markerHeight="6" orient="auto">'
        f'<path d="M0 0 L8 4 L0 8 z" fill="{ACCENT}" fill-opacity=".75"/></marker></defs>',
    ]

    x = 2.0
    for i, (label, bw) in enumerate(zip(nodes, widths)):
        hot = i == mark
        fill = f'{ACCENT}' if hot else "none"
        fop = ".16" if hot else "0"
        sw = "1.6" if hot else "1.1"
        sop = "1" if hot else ".55"
        tcol = ACCENT if hot else NEUTRAL
        parts.append(
            f'<rect x="{x:.1f}" y="{y}" width="{bw:.1f}" height="{H}" rx="6" '
            f'fill="{fill}" fill-opacity="{fop}" stroke="{ACCENT}" '
            f'stroke-opacity="{sop}" stroke-width="{sw}"/>'
        )
        parts.append(
            f'<text x="{x + bw / 2:.1f}" y="{y + H / 2 + 4:.1f}" font-family="{MONO}" '
            f'font-size="{FS}" fill="{tcol}" text-anchor="middle">{esc(label)}</text>'
        )
        if i < len(nodes) - 1:
            x0 = x + bw + 5
            x1 = x + bw + GAP - 5
            parts.append(
                f'<path d="M{x0:.1f} {y + H / 2:.1f} H{x1:.1f}" stroke="{ACCENT}" '
                f'stroke-opacity=".55" stroke-width="1.3" marker-end="url(#a)"/>'
            )
        x += bw + GAP

    parts.append(
        f'<text x="3" y="{y + H + 20}" font-family="{MONO}" font-size="10.5" '
        f'fill="{NEUTRAL}" fill-opacity=".85">{esc(note)}</text>'
    )
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


# --------------------------------------------------------------------------
# about card
# --------------------------------------------------------------------------

ROWS = [
    ("name", "Muhammad Hassaan-ul-Mustafa"),
    ("role", "AI engineer, product and backend"),
    ("study", "BS Computer Science, FAST-NUCES (2024 to 2028)"),
    ("now", "Arbisoft"),
    ("based", "Islamabad, Pakistan, open to remote"),
]

LAYERS = [("agent graph", 0), ("api + guardrails", 1), ("data + auth", 2)]

THEMES = {
    "dark": dict(bg="#0d1117", panel="#11161f", line="#232c38", key="#58a6ff",
                 val="#c9d1d9", dim="#6e7681", accent="#58a6ff"),
    "light": dict(bg="#ffffff", panel="#f6f8fa", line="#d8dee4", key="#0969da",
                  val="#1f2328", dim="#6e7781", accent="#0969da"),
}


def about_svg(t):
    w, h = 880, 196
    p = []
    p.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" '
        f'height="{h}" role="img" aria-label="About Muhammad Hassaan-ul-Mustafa">'
    )
    p.append(f'<rect width="{w}" height="{h}" rx="10" fill="{t["panel"]}" stroke="{t["line"]}"/>')
    p.append(f'<rect x="0" y="0" width="3.5" height="{h}" rx="2" fill="{t["accent"]}"/>')

    y = 42
    for k, v in ROWS:
        p.append(
            f'<text x="30" y="{y}" font-family="{MONO}" font-size="12.5" '
            f'fill="{t["key"]}">{k}</text>'
        )
        p.append(
            f'<text x="112" y="{y}" font-family="{MONO}" font-size="12.5" '
            f'fill="{t["val"]}">{esc(v)}</text>'
        )
        y += 27

    # right side: the three layers every project of mine ends up having
    bx, by = 618, 34
    p.append(
        f'<text x="{bx}" y="{by - 10}" font-family="{MONO}" font-size="9.5" '
        f'fill="{t["dim"]}" letter-spacing="1.3">WHAT I ACTUALLY BUILD</text>'
    )
    for label, i in LAYERS:
        yy = by + i * 36
        p.append(
            f'<rect x="{bx}" y="{yy}" width="228" height="28" rx="6" fill="{t["accent"]}" '
            f'fill-opacity="{0.16 - i * 0.045:.3f}" stroke="{t["accent"]}" '
            f'stroke-opacity="{0.75 - i * 0.18:.2f}" stroke-width="1.2"/>'
        )
        p.append(
            f'<text x="{bx + 14}" y="{yy + 18.5}" font-family="{MONO}" font-size="11.5" '
            f'fill="{t["val"]}">{esc(label)}</text>'
        )
        if i < 2:
            p.append(
                f'<path d="M{bx + 114} {yy + 28} V{yy + 36}" stroke="{t["accent"]}" '
                f'stroke-opacity=".45" stroke-width="1.2"/>'
            )

    p.append(
        f'<circle cx="35" cy="{h - 22}" r="4" fill="#3fb950"/>'
    )
    p.append(
        f'<text x="47" y="{h - 18}" font-family="{MONO}" font-size="11" '
        f'fill="{t["dim"]}">open to contract work and startup collaborations</text>'
    )
    p.append("</svg>")
    return "\n".join(p) + "\n"


if __name__ == "__main__":
    written = []
    for name, spec in FLOWS.items():
        f = OUT / f"flow-{name}.svg"
        f.write_text(flow_svg(spec["nodes"], spec["note"], spec["mark"]), encoding="utf-8")
        written.append(f.name)
    for theme, t in THEMES.items():
        f = OUT / f"about-{theme}.svg"
        f.write_text(about_svg(t), encoding="utf-8")
        written.append(f.name)
    print("\n".join(sorted(written)))
