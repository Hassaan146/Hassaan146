"""The orbit.

The first attempt at this slot was a developer at a desk, which was the same
idea as the stock GIF everyone floats here, just redrawn. Being a better copy is
still a copy, so this is a different object entirely.

Three rings turning at different speeds around a core that beats: data on the
inside, the API around it, agents on the outside. It is the shape of the systems
in section 01, so the illustration says something true rather than decorating.

Line art in one file, so it reads on both themes with no pair to keep in sync.
"""

import math

REDUCE = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"

AMBER = "#e8a33d"
WARM = "#f6cd85"
GREY = "#8b8f98"
FAINT = "#6b7079"

CX, CY = 200, 196

RINGS = [
    dict(r=58, dur=13, dir="normal", nodes=1, label="DATA", size=4.6),
    dict(r=102, dur=21, dir="reverse", nodes=2, label="API", size=4.2),
    dict(r=148, dur=34, dir="normal", nodes=3, label="AGENTS", size=3.8),
]


def orbit():
    a, wm, g, f = AMBER, WARM, GREY, FAINT
    w, h = 400, 418
    css = [
        ".o{transform-box:view-box;transform-origin:%dpx %dpx}" % (CX, CY),
        "@keyframes spin{to{transform:rotate(360deg)}}",
        ".core{transform-box:view-box;transform-origin:%dpx %dpx;"
        "animation:beat 4.5s ease-in-out infinite}" % (CX, CY),
        "@keyframes beat{0%,100%{transform:scale(1);opacity:.9}"
        "50%{transform:scale(1.08);opacity:1}}",
        ".halo{transform-box:view-box;transform-origin:%dpx %dpx;"
        "animation:ripple 4.5s ease-out infinite}" % (CX, CY),
        "@keyframes ripple{0%{transform:scale(.6);opacity:.5}"
        "100%{transform:scale(2.1);opacity:0}}",
        ".dash{animation:drift 26s linear infinite}",
        "@keyframes drift{to{stroke-dashoffset:-200}}",
        ".lg{animation:fade 5s ease-in-out infinite}",
        "@keyframes fade{0%,100%{opacity:.55}50%{opacity:1}}",
    ]
    for i, ring in enumerate(RINGS):
        css.append(".r%d{animation:spin %ss linear infinite;animation-direction:%s}"
                   % (i, ring["dur"], ring["dir"]))
    css.append(REDUCE)

    p = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" '
         'height="%d" role="img" aria-label="Three rings turning around a core: '
         'data inside, the API around it, agents on the outside">' % (w, h, w, h),
         "<style>%s</style>" % "".join(css)]

    # faint outer boundary, slowly drifting
    p.append('<circle class="dash" cx="%d" cy="%d" r="180" fill="none" stroke="%s" '
             'stroke-width="1" stroke-opacity=".3" stroke-dasharray="2 8"/>'
             % (CX, CY, a))

    # tick marks on the boundary, every 30 degrees
    for i in range(12):
        ang = i * math.pi / 6
        x1, y1 = CX + 172 * math.cos(ang), CY + 172 * math.sin(ang)
        x2, y2 = CX + 180 * math.cos(ang), CY + 180 * math.sin(ang)
        op = ".5" if i % 3 == 0 else ".22"
        p.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                 'stroke-width="1.4" stroke-opacity="%s"/>' % (x1, y1, x2, y2, a, op))

    # the rings, each with its own speed and direction
    for i, ring in enumerate(RINGS):
        r, n, sz = ring["r"], ring["nodes"], ring["size"]
        p.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" '
                 'stroke-width="1" stroke-opacity=".28"/>' % (CX, CY, r, g))
        p.append('<g class="o r%d">' % i)
        for k in range(n):
            ang = 2 * math.pi * k / n
            nx, ny = CX + r * math.cos(ang), CY + r * math.sin(ang)
            # a short arc trailing each node, so the direction of travel reads
            a0, a1 = ang - 0.34, ang
            p.append('<path d="M%.1f %.1f A%d %d 0 0 1 %.1f %.1f" fill="none" '
                     'stroke="%s" stroke-width="2" stroke-opacity=".45" '
                     'stroke-linecap="round"/>'
                     % (CX + r * math.cos(a0), CY + r * math.sin(a0), r, r, nx, ny, a))
            p.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>'
                     % (nx, ny, sz, a if k == 0 else wm))
        p.append("</g>")

    # the core
    p.append('<circle class="halo" cx="%d" cy="%d" r="20" fill="none" stroke="%s" '
             'stroke-width="1.5"/>' % (CX, CY, a))
    p.append('<g class="core">')
    p.append('<circle cx="%d" cy="%d" r="19" fill="%s" fill-opacity=".1" stroke="%s" '
             'stroke-width="2"/>' % (CX, CY, a, a))
    p.append('<circle cx="%d" cy="%d" r="6.5" fill="%s"/>' % (CX, CY, a))
    p.append("</g>")

    # legend, so the rings mean something
    ly = 372
    for i, ring in enumerate(RINGS):
        lx = 26 + i * 122
        p.append('<circle class="lg" style="animation-delay:%ss" cx="%d" cy="%d" r="4" '
                 'fill="%s"/>' % (round(i * 0.6, 2), lx, ly - 4, a))
        p.append('<text x="%d" y="%d" font-family="ui-monospace, SFMono-Regular, Menlo, '
                 'Consolas, monospace" font-size="10" fill="%s" letter-spacing="1.6">%s</text>'
                 % (lx + 12, ly, f, ring["label"]))
        p.append('<text x="%d" y="%d" font-family="ui-monospace, SFMono-Regular, Menlo, '
                 'Consolas, monospace" font-size="8.4" fill="%s" letter-spacing="1.1" '
                 'opacity=".7">%ss ORBIT</text>' % (lx + 12, ly + 13, f, ring["dur"]))
    p.append("</svg>")
    return chr(10).join(p) + chr(10)
