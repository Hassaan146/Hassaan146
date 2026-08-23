"""The workstation illustration.

Most profiles float the same stock developer GIF here, the one that turns up on
thousands of them. This is drawn instead, in the palette the rest of the page
uses, and it moves: code fills in line by line on both screens, a caret blinks,
the gear turns, the hand taps the keyboard.

Line art rather than flat colour, which means one file reads correctly on both
the light and the dark theme and there is no pair to keep in sync.
"""

import math

REDUCE = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"

AMBER = "#e8a33d"
GREY = "#8b8f98"
FAINT = "#6b7079"


def desk():
    a, g, f2 = AMBER, GREY, FAINT
    w, h = 430, 400
    css = (
        ".ln{animation:type 5.5s ease-in-out infinite}"
        "@keyframes type{0%{opacity:0}12%{opacity:1}70%{opacity:1}"
        "82%{opacity:0}100%{opacity:0}}"
        ".car{animation:blink 1.1s steps(1) infinite}"
        "@keyframes blink{0%,50%{opacity:1}51%,100%{opacity:0}}"
        ".gear{transform-box:fill-box;transform-origin:center;"
        "animation:spin 9s linear infinite}"
        "@keyframes spin{to{transform:rotate(360deg)}}"
        ".hand{transform-box:fill-box;transform-origin:center;"
        "animation:tap 1.6s ease-in-out infinite}"
        "@keyframes tap{0%,100%{transform:translateY(0)}50%{transform:translateY(1.7px)}}"
        ".glow{animation:pulse 5.5s ease-in-out infinite}"
        "@keyframes pulse{0%,100%{opacity:.05}45%{opacity:.14}}"
        + REDUCE
    )
    p = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" '
        'height="%d" role="img" aria-label="A developer at a desk with two screens, '
        'code filling in line by line, a gear turning in a thought bubble above">'
        % (w, h, w, h),
        "<style>%s</style>" % css,
    ]

    # notes pinned to the wall
    wall = [(28, 44, 88), (28, 54, 62), (28, 64, 74),
            (152, 30, 96), (152, 40, 70), (152, 50, 88), (152, 60, 54)]
    for i, (x, y, ln) in enumerate(wall):
        p.append('<rect class="ln" style="animation-delay:%ss" x="%d" y="%d" width="%d" '
                 'height="2.4" rx="1.2" fill="%s" opacity=".45"/>'
                 % (round(i * 0.22, 2), x, y, ln, f2))

    p.append('<ellipse cx="215" cy="356" rx="176" ry="15" fill="%s" opacity=".12"/>' % g)

    # desk
    p.append('<rect x="34" y="252" width="228" height="7" rx="3" fill="%s" opacity=".75"/>' % g)
    p.append('<rect x="44" y="259" width="4" height="88" fill="%s" opacity=".55"/>' % g)
    p.append('<rect x="248" y="259" width="4" height="88" fill="%s" opacity=".55"/>' % g)

    # left screen
    p.append('<rect class="glow" x="52" y="170" width="88" height="64" rx="4" fill="%s"/>' % a)
    p.append('<rect x="52" y="170" width="88" height="64" rx="4" fill="none" stroke="%s" '
             'stroke-width="2"/>' % g)
    p.append('<rect x="88" y="234" width="16" height="12" fill="%s" opacity=".6"/>' % g)
    p.append('<rect x="74" y="246" width="44" height="4" rx="2" fill="%s" opacity=".6"/>' % g)
    for i, (yy, ln) in enumerate([(182, 46), (190, 30), (198, 54), (206, 38), (214, 44)]):
        p.append('<rect class="ln" style="animation-delay:%ss" x="62" y="%d" width="%d" '
                 'height="3" rx="1.5" fill="%s" opacity=".85"/>'
                 % (round(i * 0.3, 2), yy, ln, a if i % 2 == 0 else f2))

    # right screen
    p.append('<rect class="glow" style="animation-delay:.7s" x="148" y="160" width="98" '
             'height="74" rx="4" fill="%s"/>' % a)
    p.append('<rect x="148" y="160" width="98" height="74" rx="4" fill="none" stroke="%s" '
             'stroke-width="2"/>' % g)
    p.append('<rect x="188" y="234" width="16" height="12" fill="%s" opacity=".6"/>' % g)
    p.append('<rect x="174" y="246" width="44" height="4" rx="2" fill="%s" opacity=".6"/>' % g)
    for i, (yy, ln) in enumerate([(174, 60), (182, 40), (190, 68), (198, 34),
                                  (206, 56), (214, 46)]):
        p.append('<rect class="ln" style="animation-delay:%ss" x="158" y="%d" width="%d" '
                 'height="3" rx="1.5" fill="%s" opacity=".85"/>'
                 % (round(0.4 + i * 0.3, 2), yy, ln, a if i % 3 == 0 else f2))
    p.append('<rect class="car" x="158" y="220" width="7" height="3" fill="%s"/>' % a)

    p.append('<rect x="96" y="244" width="74" height="7" rx="2.5" fill="%s" opacity=".8"/>' % g)

    # chair
    p.append('<path d="M300 206 q22 0 22 22 v58 q0 16 -18 16 h-6" fill="none" stroke="%s" '
             'stroke-width="7" stroke-linecap="round" opacity=".8"/>' % g)
    p.append('<rect x="268" y="300" width="52" height="7" rx="3.5" fill="%s" opacity=".8"/>' % g)
    p.append('<path d="M294 307 v22" stroke="%s" stroke-width="5" opacity=".7"/>' % g)
    p.append('<path d="M272 340 l22 -11 l22 11" fill="none" stroke="%s" stroke-width="4" '
             'stroke-linecap="round" opacity=".7"/>' % g)
    p.append('<circle cx="270" cy="344" r="5" fill="none" stroke="%s" stroke-width="3" '
             'opacity=".7"/>' % g)
    p.append('<circle cx="318" cy="344" r="5" fill="none" stroke="%s" stroke-width="3" '
             'opacity=".7"/>' % g)

    # the person, seated, facing the screens
    p.append('<path d="M292 232 q-10 34 -2 66" fill="none" stroke="%s" stroke-width="15" '
             'stroke-linecap="round"/>' % a)
    p.append('<path d="M286 300 q-24 6 -30 26" fill="none" stroke="%s" stroke-width="12" '
             'stroke-linecap="round"/>' % f2)
    p.append('<path d="M256 326 q-4 12 -2 20" fill="none" stroke="%s" stroke-width="11" '
             'stroke-linecap="round"/>' % f2)
    p.append('<path class="hand" d="M288 246 q-24 4 -44 12" fill="none" stroke="%s" '
             'stroke-width="10" stroke-linecap="round"/>' % a)
    p.append('<circle cx="290" cy="208" r="17" fill="none" stroke="%s" stroke-width="3.5"/>' % g)
    p.append('<path d="M274 202 q4 -18 22 -14 q10 3 10 12" fill="none" stroke="%s" '
             'stroke-width="5" stroke-linecap="round"/>' % g)

    # thought bubble, with a gear that turns
    bx, by = 322, 96
    p.append('<rect x="%d" y="%d" width="62" height="56" rx="8" fill="none" stroke="%s" '
             'stroke-width="2" opacity=".8"/>' % (bx, by, a))
    p.append('<path d="M%d %d l6 12 l10 -12" fill="none" stroke="%s" stroke-width="2" '
             'opacity=".8" stroke-linejoin="round"/>' % (bx + 12, by + 56, a))
    cx, cy = bx + 31, by + 28
    teeth = []
    for i in range(8):
        ang = i * math.pi / 4
        teeth.append("M%.1f %.1f L%.1f %.1f" % (
            cx + 13 * math.cos(ang), cy + 13 * math.sin(ang),
            cx + 18 * math.cos(ang), cy + 18 * math.sin(ang)))
    p.append('<g class="gear">'
             '<circle cx="%d" cy="%d" r="13" fill="none" stroke="%s" stroke-width="3"/>'
             '<circle cx="%d" cy="%d" r="4.5" fill="none" stroke="%s" stroke-width="2.5"/>'
             '<path d="%s" stroke="%s" stroke-width="3" stroke-linecap="round"/>'
             '</g>' % (cx, cy, a, cx, cy, a, " ".join(teeth), a))

    # bin
    p.append('<path d="M356 306 l5 40 h26 l5 -40 z" fill="none" stroke="%s" '
             'stroke-width="2.5" opacity=".6"/>' % g)
    p.append('<path d="M352 306 h48" stroke="%s" stroke-width="2.5" opacity=".6"/>' % g)
    p.append("</svg>")
    return chr(10).join(p) + chr(10)
