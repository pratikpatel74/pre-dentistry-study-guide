"""Second batch of original diagrams. Classes are styled in build.py's NOTES_CSS."""
import math

def _arrow_defs(pid):
    return (f'<defs><marker id="{pid}-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" '
            f'orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="axis-fill"/></marker></defs>')

def _box(x, y, w, h, name, lines=(), acc=False, name_size=None):
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" class="box{" acc" if acc else ""}"/>']
    cx = x + w / 2
    ns = f' style="font-size:{name_size}px"' if name_size else ''
    out.append(f'<text x="{cx}" y="{y+24}" text-anchor="middle" class="lbl"{ns}>{name}</text>')
    for i, l in enumerate(lines):
        out.append(f'<text x="{cx}" y="{y+42+i*16}" text-anchor="middle" class="sub">{l}</text>')
    return "".join(out)

def _fig(svg, cap):
    return f'<figure class="diagram">{svg}<figcaption>{cap}</figcaption></figure>'


# ---------- Topic 1: pathway ----------
def pathway():
    W, G, x0, y0, H = 110, 16, 10, 76, 100
    steps = [
        ("Before BDS", ["A-levels", "UCAT, interview", "Health checks"], False),
        ("Years 1–2", ["Biomedical", "sciences", "Phantom head"], True),
        ("Years 3–4", ["Treating", "patients under", "supervision"], False),
        ("Year 5", ["Outreach", "clinics", "Finals"], False),
        ("DFT · 1 year", ["Supervised", "NHS practice", ""], False),
        ("Practice", ["NHS or private", "Specialise", "later if wanted"], False),
    ]
    p = "pw"
    out = [_arrow_defs(p)]
    for i, (n, ls, acc) in enumerate(steps):
        x = x0 + i * (W + G)
        out.append(_box(x, y0, W, H, n, [l for l in ls if l], acc))
        if i < len(steps) - 1:
            out.append(f'<path d="M{x+W+2} {y0+H/2}H{x+W+G-2}" class="arrow" marker-end="url(#{p}-a)"/>')
    gx = x0 + 4 * (W + G) - G / 2
    out.append(f'<line x1="{gx}" x2="{gx}" y1="66" y2="{y0+H+10}" class="crit"/>')
    out.append(f'<text x="{gx}" y="60" text-anchor="middle" class="small lbl">Graduate + register with the GDC</text>')
    bx1, bx2 = x0 + (W + G), x0 + 3 * (W + G) + W
    out.append(f'<path d="M{bx1} {y0+H+16}V{y0+H+24}H{bx2}V{y0+H+16}" class="leader thick"/>')
    out.append(f'<text x="{(bx1+bx2)/2}" y="{y0+H+42}" text-anchor="middle" class="lbl">BDS degree · 5 years</text>')
    svg = (f'<svg viewBox="0 0 760 240" role="img" aria-label="Route from A-levels through a five-year BDS and foundation training to practice">'
           f'<text x="10" y="28" class="title">Five years of BDS, then a year of foundation training</text>'
           + "".join(out) + "</svg>")
    return _fig(svg, "Typical route into UK dentistry. Course structure varies by dental school.")


# ---------- Topic 2: tooth surfaces ----------
def surfaces():
    cx, top, rx, ry = 200, 96, 130, 190
    centre = (cx, top + ry)
    n = 16
    thetas = [math.radians(12 + i * (156 / (n - 1))) for i in range(n)]
    out = []
    out.append(f'<line x1="{cx}" x2="{cx}" y1="70" y2="300" class="crit"/>')
    out.append(f'<text x="{cx}" y="64" text-anchor="middle" class="sub">midline</text>')
    k = 4  # highlighted tooth (premolar, right of picture)
    for i, t in enumerate(thetas):
        x = cx + rx * math.cos(t); y = top + ry - ry * math.sin(t)
        side = min(i, n - 1 - i)  # 0 = back molar, 7 = central incisor
        r = 15 if side <= 2 else 12 if side <= 4 else 10
        cls = "tt mol" if side <= 2 else "tt pm" if side <= 4 else "tt can" if side == 5 else "tt inc"
        hl = " hl" if i == k else ""
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" class="{cls}{hl}"/>')
    t = thetas[k]
    x = cx + rx * math.cos(t); y = top + ry - ry * math.sin(t)
    d = (-rx * math.sin(t), -ry * math.cos(t)); L = math.hypot(*d); d = (d[0] / L, d[1] / L)  # towards front
    # normal pointing away from arch centre
    nx, ny = -d[1], d[0]
    if (x + nx - centre[0]) ** 2 + (y + ny - centre[1]) ** 2 < (x - centre[0]) ** 2 + (y - centre[1]) ** 2:
        nx, ny = -nx, -ny
    p = "sf"
    out.insert(0, _arrow_defs(p))
    def arr(vx, vy, label, anchor, dx=0, dy=0):
        sx, sy = x + vx * 18, y + vy * 18
        ex, ey = x + vx * 62, y + vy * 62
        return (f'<path d="M{sx:.1f} {sy:.1f}L{ex:.1f} {ey:.1f}" class="arrow acc-stroke" marker-end="url(#{p}-a)"/>'
                f'<text x="{ex+dx:.1f}" y="{ey+dy:.1f}" text-anchor="{anchor}" class="lbl">{label}</text>')
    out.append(arr(d[0], d[1], "Mesial", "end", -6, 0))
    out.append(arr(-d[0], -d[1], "Distal", "start", 20, 6))
    out.append(arr(nx, ny, "Buccal", "start", 6, 4))
    out.append(arr(-nx, -ny, "Lingual", "end", -6, 4))
    out.append(f'<text x="40" y="318" class="sub">Lower arch seen from above, front teeth at the top</text>')
    # enlarged tooth
    X0, Y0, S, I = 500, 110, 130, 34
    X1, Y1 = X0 + S, Y0 + S
    out.append(f'<rect x="{X0}" y="{Y0}" width="{S}" height="{S}" rx="14" class="tt pm"/>')
    out.append(f'<rect x="{X0+I}" y="{Y0+I}" width="{S-2*I}" height="{S-2*I}" rx="6" class="box acc"/>')
    for (a, b, c, e) in [(X0, Y0, X0+I, Y0+I), (X1, Y0, X1-I, Y0+I), (X0, Y1, X0+I, Y1-I), (X1, Y1, X1-I, Y1-I)]:
        out.append(f'<line x1="{a}" y1="{b}" x2="{c}" y2="{e}" class="leader"/>')
    mx, my = X0 + S / 2, Y0 + S / 2
    out.append(f'<text x="{mx}" y="{my+4}" text-anchor="middle" class="small lbl">Occlusal</text>')
    out.append(f'<text x="{mx}" y="{Y0-10}" text-anchor="middle" class="lbl">Buccal <tspan class="sub">(cheek)</tspan></text>')
    out.append(f'<text x="{mx}" y="{Y1+22}" text-anchor="middle" class="lbl">Lingual <tspan class="sub">(tongue)</tspan></text>')
    out.append(f'<text x="{X0-10}" y="{my}" text-anchor="end" class="lbl">Mesial</text>')
    out.append(f'<text x="{X0-10}" y="{my+16}" text-anchor="end" class="sub">to midline</text>')
    out.append(f'<text x="{X1+10}" y="{my}" class="lbl">Distal</text>')
    out.append(f'<text x="{X1+10}" y="{my+16}" class="sub">away</text>')
    out.append(f'<text x="440" y="290" class="sub">Upper teeth: palatal instead of lingual.</text>')
    out.append(f'<text x="440" y="306" class="sub">Front teeth: labial instead of buccal,</text>')
    out.append(f'<text x="440" y="322" class="sub">incisal edge instead of occlusal.</text>')
    svg = (f'<svg viewBox="0 0 760 340" role="img" aria-label="Tooth surfaces named by direction: mesial, distal, buccal, lingual and occlusal">'
           f'<text x="24" y="30" class="title">Surfaces are named by direction: midline, cheek, tongue or biting</text>'
           + "".join(out) + "</svg>")
    return _fig(svg, "Naming tooth surfaces. The highlighted premolar's arrows show each direction.")


# ---------- Topic 4: caries stages ----------
_OUTLINE = ("M172 200 C160 150, 165 100, 200 85 Q225 75, 240 90 Q260 70, 280 90 Q295 75, 320 85 "
            "C355 100, 360 150, 348 200 L345 260 C340 330, 330 380, 315 400 Q305 410, 295 400 "
            "C290 360, 285 300, 270 270 Q260 255, 250 270 C235 300, 230 360, 225 400 Q215 410, 205 400 "
            "C190 380, 180 330, 175 260 Z")
_ENAMEL = ("M172 200 C160 150, 165 100, 200 85 Q225 75, 240 90 Q260 70, 280 90 Q295 75, 320 85 C355 100, 360 150, 348 200 "
           "L334 200 C342 155, 338 118, 315 105 Q295 97, 280 108 Q260 92, 240 108 Q225 97, 205 105 C182 118, 178 155, 186 200 Z")
_PULP = ("M225 150 Q240 135, 260 145 Q280 135, 295 150 L298 210 C300 250, 305 320, 308 392 L302 394 C295 320, 285 260, "
         "270 235 Q260 225, 250 235 C235 260, 225 320, 218 394 L212 392 C215 320, 220 250, 222 210 Z")

def stages():
    s, ytop = 0.56, 96
    centres = [100, 287, 474, 661]
    lesions = [
        '<ellipse cx="280" cy="97" rx="10" ry="6" class="whitespot"/>',
        '<path d="M282 89 C275 92, 272 100, 280 106 C288 100, 290 93, 284 89 Z" class="lesion"/><path d="M276 90 L281 101 L287 90 Z" class="hole"/>',
        '<path d="M266 108 C252 128, 260 150, 281 152 C302 150, 308 128, 294 108 Z" class="lesion"/><path d="M270 90 L274 106 L287 108 L292 90 Z" class="lesion"/><path d="M272 89 L280 108 L290 89 Z" class="hole"/>',
        '<path d="M258 104 C240 135, 255 170, 282 172 C308 170, 318 135, 302 104 Z" class="lesion"/><path d="M262 88 L272 110 L292 110 L300 88 Z" class="hole"/>',
    ]
    labels = [("1. White spot", "Chalky patch under an", "intact surface"),
              ("2. Enamel cavity", "Surface breaks down;", "bacteria move in"),
              ("3. Into dentine", "Spreads fast along", "softer dentine"),
              ("4. Reaches the pulp", "Pulpitis, pain,", "possible abscess")]
    p = "cs"
    out = [_arrow_defs(p)]
    for i, (c, les) in enumerate(zip(centres, lesions)):
        pulp_cls = "pulp inflamed" if i == 3 else "pulp"
        tx, ty = c - 260 * s, ytop - 75 * s
        out.append(f'<g transform="translate({tx:.1f},{ty:.1f}) scale({s})">'
                   f'<path d="{_OUTLINE}" class="dentine"/><path d="{_ENAMEL}" class="enamel"/>'
                   f'<path d="{_PULP}" class="{pulp_cls}"/>{les}</g>')
        n, a, b = labels[i]
        out.append(f'<text x="{c}" y="306" text-anchor="middle" class="lbl">{n}</text>')
        out.append(f'<text x="{c}" y="324" text-anchor="middle" class="sub">{a}</text>')
        out.append(f'<text x="{c}" y="340" text-anchor="middle" class="sub">{b}</text>')
        if i < 3:
            out.append(f'<path d="M{c+70} 190H{centres[i+1]-70}" class="arrow" marker-end="url(#{p}-a)"/>')
    out.append(f'<path d="M40 84V76H160V84" class="leader thick"/><text x="100" y="68" text-anchor="middle" class="small lbl ok">Can remineralise</text>')
    out.append(f'<path d="M227 84V76H721V84" class="leader thick"/><text x="474" y="68" text-anchor="middle" class="small lbl danger">Lost tissue cannot regrow: needs treatment</text>')
    svg = (f'<svg viewBox="0 0 760 356" role="img" aria-label="Four stages of tooth decay from white spot to pulp">'
           f'<text x="24" y="30" class="title">Decay is reversible only while the enamel surface is intact</text>'
           + "".join(out) + "</svg>")
    return _fig(svg, "Caries progression in a molar fissure (schematic).")


# ---------- Topic 5: healthy vs gingivitis vs periodontitis ----------
def perio():
    def er(y):  # right root edge (local coords)
        return 145 - (y - 120) * 10 / 160
    def el(y):
        return 75 + (y - 120) * 10 / 160
    tooth = "M75 120 C72 80, 80 45, 110 40 C140 45, 148 80, 145 120 L135 280 Q110 310 85 280 Z"
    enamel = "M75 120 C72 80, 80 45, 110 40 C140 45, 148 80, 145 120 L139 120 C140 86, 132 56, 110 52 C88 56, 80 86, 81 120 Z"
    panels = [
        dict(name="Healthy", a="Pocket 1–3 mm", b="Bone just below the neck", m=112, bt=140, base=128, bulge=24, cls="gum", calc=False),
        dict(name="Gingivitis", a="Red, swollen, bleeds", b="Bone unaffected · reversible", m=100, bt=140, base=132, bulge=40, cls="gum sore", calc=False),
        dict(name="Periodontitis", a="Deep pocket, calculus", b="Bone lost · permanent", m=128, bt=212, base=204, bulge=26, cls="gum sore", calc=True),
    ]
    out = []
    for i, P in enumerate(panels):
        ox = 20 + i * 245
        m, bt, base, bu = P["m"], P["bt"], P["base"], P["bulge"]
        g = [f'<g transform="translate({ox},56)">']
        g.append(f'<rect x="10" y="{bt}" width="200" height="{330-bt}" rx="6" class="bone"/>')
        g.append(f'<path d="{tooth}" class="dentine"/><path d="{enamel}" class="enamel"/>')
        # gums, both sides
        R = (f'M{er(m)+1:.1f} {m} C{er(m)+bu*0.6:.1f} {m-6}, {er(m)+bu:.1f} {m+8}, 210 {m+26} '
             f'L210 {bt+12} L{er(bt)+1:.1f} {bt+12} L{er(base)+1:.1f} {base} Z')
        Lp = (f'M{el(m)-1:.1f} {m} C{el(m)-bu*0.6:.1f} {m-6}, {el(m)-bu:.1f} {m+8}, 10 {m+26} '
              f'L10 {bt+12} L{el(bt)-1:.1f} {bt+12} L{el(base)-1:.1f} {base} Z')
        g.append(f'<path d="{R}" class="{P["cls"]}"/><path d="{Lp}" class="{P["cls"]}"/>')
        if P["calc"]:
            for cy in (150, 172, 192):
                g.append(f'<ellipse cx="{er(cy)+1:.1f}" cy="{cy}" rx="4" ry="7" class="calculus"/>')
        # probe on right side
        px = er(m) + 4
        g.append(f'<line x1="{px:.1f}" y1="{m-44}" x2="{er(base)+3:.1f}" y2="{base}" class="probe"/>')
        g.append(f'<line x1="{er(base)+8:.1f}" y1="{m}" x2="{er(base)+8:.1f}" y2="{base}" class="depth"/>')
        g.append('</g>')
        out.append("".join(g))
        cxp = ox + 110
        out.append(f'<text x="{cxp}" y="420" text-anchor="middle" class="lbl">{P["name"]}</text>')
        out.append(f'<text x="{cxp}" y="438" text-anchor="middle" class="sub">{P["a"]}</text>')
        out.append(f'<text x="{cxp}" y="454" text-anchor="middle" class="sub">{P["b"]}</text>')
    key = [("gum", "Gum"), ("gum sore", "Inflamed gum"), ("bone", "Alveolar bone"), ("calculus", "Calculus")]
    kx = 40
    for c, t in key:
        out.append(f'<rect x="{kx}" y="476" width="16" height="16" rx="4" class="{c}"/><text x="{kx+24}" y="489" class="small">{t}</text>')
        kx += 150
    out.append(f'<line x1="{kx}" y1="484" x2="{kx+18}" y2="484" class="probe"/><text x="{kx+26}" y="489" class="small">Probe</text>')
    svg = (f'<svg viewBox="0 0 760 506" role="img" aria-label="Healthy gums, gingivitis and periodontitis compared">'
           f'<text x="24" y="30" class="title">Gingivitis stays in the gum; periodontitis takes the bone</text>'
           + "".join(out) + "</svg>")
    return _fig(svg, "Gum and bone levels in health, gingivitis and periodontitis (schematic).")


# ---------- Topic 6: trigeminal territories ----------
def trigeminal():
    cx, cy, rx, ry = 190, 230, 118, 158
    eye, mouth = 196, 296
    p = "tg"
    clip = f'<clipPath id="{p}-face"><ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}"/></clipPath>'
    zones = (f'<g clip-path="url(#{p}-face)">'
             f'<rect x="0" y="0" width="400" height="{eye}" class="z1"/>'
             f'<rect x="0" y="{eye}" width="400" height="{mouth-eye}" class="z2"/>'
             f'<rect x="{cx-10}" y="{eye}" width="20" height="{266-eye}" class="z1"/>'
             f'<rect x="0" y="{mouth}" width="400" height="200" class="z3"/>'
             f'<circle cx="{cx-95}" cy="335" r="36" class="zc"/><circle cx="{cx+95}" cy="335" r="36" class="zc"/>'
             f'</g>')
    face = (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" class="face"/>'
            f'<ellipse cx="{cx-44}" cy="{eye}" rx="18" ry="8" class="feature"/><ellipse cx="{cx+44}" cy="{eye}" rx="18" ry="8" class="feature"/>'
            f'<path d="M{cx-10} {eye+6} L{cx-16} 262 Q{cx} 272 {cx+16} 262 L{cx+10} {eye+6}" class="feature-line"/>'
            f'<path d="M{cx-32} {mouth} Q{cx} {mouth+14} {cx+32} {mouth}" class="feature-line"/>')
    out = [clip.join(['<defs>', '</defs>']), zones, face]
    out.append(f'<text x="{cx}" y="128" text-anchor="middle" class="lbl">V1</text>')
    out.append(f'<text x="{cx-70}" y="250" text-anchor="middle" class="lbl">V2</text>')
    out.append(f'<text x="{cx}" y="350" text-anchor="middle" class="lbl">V3</text>')
    out.append(f'<text x="{cx-82}" y="340" text-anchor="middle" class="small lbl">C2/3</text>')
    rows = [
        ("z1", "V1 · Ophthalmic", "Forehead, upper eyelid, bridge and tip of nose", ""),
        ("z2", "V2 · Maxillary", "Cheek, lower eyelid, side of nose, upper lip", "Inside: upper teeth, palate, upper gums"),
        ("z3", "V3 · Mandibular", "Lower lip, chin, lower jaw, temple in front of ear", "Inside: lower teeth, tongue (sensation); moves chewing muscles"),
        ("zc", "Angle of the jaw", "Not trigeminal: cervical nerves C2/C3", "A classic exam trap"),
    ]
    y = 96
    for c, n, a, b in rows:
        out.append(f'<rect x="352" y="{y-14}" width="18" height="18" rx="4" class="{c}"/>')
        out.append(f'<text x="380" y="{y}" class="lbl">{n}</text>')
        out.append(f'<text x="380" y="{y+18}" class="small">{a}</text>')
        if b:
            out.append(f'<text x="380" y="{y+34}" class="sub">{b}</text>')
        y += 76
    svg = (f'<svg viewBox="0 0 760 410" role="img" aria-label="Areas of the face supplied by the three trigeminal branches">'
           f'<text x="24" y="30" class="title">Three trigeminal branches share the face, but not the angle of the jaw</text>'
           f'<text x="24" y="50" class="sub">Skin sensation, front view (schematic; real boundaries overlap)</text>'
           + "".join(out) + "</svg>")
    return _fig(svg, "Sensory territories of the trigeminal nerve (CN V).")


# ---------- Topic 7: decontamination cycle + sharps ----------
def decon():
    cx, cy, r = 380, 262, 172
    W, H = 136, 58
    nodes = [("Use", "On one patient"), ("Clean", "Washer-disinfector"), ("Inspect", "Check it's clean"),
             ("Sterilise", "Steam autoclave"), ("Store", "Wrapped and dated")]
    angs = [-90 + i * 72 for i in range(5)]
    p = "dc"
    out = [_arrow_defs(p)]
    for (n, l), a in zip(nodes, angs):
        x = cx + r * math.cos(math.radians(a)); y = cy + r * math.sin(math.radians(a))
        out.append(_box(x - W / 2, y - H / 2, W, H, n, [l], acc=(n == "Sterilise")))
    for i, a in enumerate(angs):
        a1, a2 = math.radians(a + 25), math.radians(a + 72 - 25)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
        out.append(f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 0 1 {x2:.1f} {y2:.1f}" class="arrow" marker-end="url(#{p}-a)"/>')
    out.append(f'<text x="{cx}" y="{cy-6}" text-anchor="middle" class="lbl big">HTM 01-05</text>')
    out.append(f'<text x="{cx}" y="{cy+14}" text-anchor="middle" class="sub">decontamination cycle</text>')
    out.append(f'<text x="{cx}" y="{cy+30}" text-anchor="middle" class="sub">(England)</text>')
    svg = (f'<svg viewBox="0 0 760 480" role="img" aria-label="Instrument decontamination cycle: use, clean, inspect, sterilise, store">'
           f'<text x="24" y="30" class="title">Instruments must be clean before they can be sterilised</text>'
           + "".join(out) + "</svg>")
    return _fig(svg, "Reusable instrument cycle (single-use items are never reprocessed).")


def sharps():
    W, G, x0, y0, H = 160, 24, 24, 62, 70
    steps = [("1. Bleed it", "Encourage bleeding"), ("2. Wash it", "Soap and running water"),
             ("3. Cover it", "Waterproof dressing"), ("4. Report it", "Follow clinic protocol")]
    p = "sh"
    out = [_arrow_defs(p)]
    for i, (n, l) in enumerate(steps):
        x = x0 + i * (W + G)
        out.append(_box(x, y0, W, H, n, [l], acc=(i == 3)))
        if i < 3:
            out.append(f'<path d="M{x+W+2} {y0+H/2}H{x+W+G-2}" class="arrow" marker-end="url(#{p}-a)"/>')
    out.append(f'<text x="24" y="{y0+H+28}" class="small lbl danger">Never suck the wound or scrub it. Report the same day.</text>')
    svg = (f'<svg viewBox="0 0 760 170" role="img" aria-label="Four steps after a sharps injury">'
           f'<text x="24" y="30" class="title">After a sharps injury: four steps, in order, straight away</text>'
           + "".join(out) + "</svg>")
    return _fig(svg, "Sharps injury first aid.")


# ---------- Topic 8: capacity test ----------
def capacity():
    p = "cp"
    out = [_arrow_defs(p)]
    out.append(_box(255, 58, 250, 46, "Start by assuming capacity", []))
    tests = [("Understand", "the information given"), ("Retain", "it long enough"),
             ("Weigh up", "the options and risks"), ("Communicate", "their decision")]
    W, G, x0, y0 = 166, 16, 24, 150
    out.append(f'<path d="M380 104V122" class="arrow"/><path d="M{x0+W/2} 122H{x0+3*(W+G)+W/2}" class="arrow"/>')
    for i, (n, l) in enumerate(tests):
        x = x0 + i * (W + G)
        out.append(f'<path d="M{x+W/2} 122V{y0-2}" class="arrow" marker-end="url(#{p}-a)"/>')
        out.append(_box(x, y0, W, 64, n, [l]))
        out.append(f'<path d="M{x+W/2} {y0+64}V236" class="arrow"/>')
    out.append(f'<path d="M{x0+W/2} 236H{x0+3*(W+G)+W/2}" class="arrow"/>')
    out.append(f'<path d="M210 236V284" class="arrow" marker-end="url(#{p}-a)"/><path d="M550 236V284" class="arrow" marker-end="url(#{p}-a)"/>')
    out.append(f'<text x="218" y="266" class="small lbl ok">All four: yes</text>')
    out.append(f'<text x="558" y="266" class="small lbl danger">Any one: no</text>')
    out.append(_box(60, 286, 300, 80, "Has capacity", ["Can consent or refuse, even if", "you think the choice is unwise"], acc=True))
    out.append(_box(400, 286, 300, 80, "Lacks capacity for this decision", ["Act in their best interests and", "involve others (MCA 2005)"]))
    svg = (f'<svg viewBox="0 0 760 384" role="img" aria-label="Mental capacity test: understand, retain, weigh up, communicate">'
           f'<text x="24" y="30" class="title">Capacity test: the patient must manage all four, for this decision</text>'
           + "".join(out) + "</svg>")
    return _fig(svg, "Assessing capacity under the Mental Capacity Act 2005 (England and Wales).")


# ---------- Topic 9: pH scale ----------
def phscale():
    X = lambda ph: 80 + (ph - 3) * 120
    out = []
    out.append(f'<rect x="{X(3)}" y="150" width="{X(5.5)-X(3)}" height="30" class="danger-zone" style="fill-opacity:.25"/>')
    out.append(f'<rect x="{X(5.5)}" y="150" width="{X(8)-X(5.5)}" height="30" class="safe-zone"/>')
    out.append(f'<rect x="{X(3)}" y="150" width="{X(8)-X(3)}" height="30" class="frame"/>')
    sups = {3: "⁻³", 4: "⁻⁴", 5: "⁻⁵", 6: "⁻⁶", 7: "⁻⁷", 8: "⁻⁸"}
    for ph in range(3, 9):
        x = X(ph)
        out.append(f'<line x1="{x}" x2="{x}" y1="222" y2="232" class="leader"/>')
        out.append(f'<text x="{x}" y="248" text-anchor="middle" class="lbl">pH {ph}</text>')
        out.append(f'<text x="{x}" y="266" text-anchor="middle" class="sub">[H⁺] = 10{sups[ph]}</text>')
    # markers
    def mark(ph, row_y, label, anchor="middle"):
        x = X(ph)
        return (f'<line x1="{x}" x2="{x}" y1="{row_y+6}" y2="150" class="leader thick"/>'
                f'<circle cx="{x}" cy="150" r="4" class="ink-fill"/>'
                f'<text x="{x}" y="{row_y}" text-anchor="{anchor}" class="lbl">{label}</text>')
    out.append(mark(4.5, 96, "Fluorapatite dissolves · 4.5"))
    out.append(mark(5.5, 126, "Enamel critical pH · 5.5"))
    out.append(mark(6.75, 96, "Resting plaque ≈ 6.5–7"))
    out.append(f'<rect x="{X(6.2)}" y="186" width="{X(6.7)-X(6.2)}" height="8" rx="3" class="z3"/>')
    out.append(f'<text x="{(X(6.2)+X(6.7))/2}" y="212" text-anchor="middle" class="small">Root dentine 6.2–6.7</text>')
    out.append(f'<text x="{X(3)+8}" y="170" class="small lbl danger">Enamel dissolves</text>')
    out.append(f'<text x="{X(8)-8}" y="170" text-anchor="end" class="small lbl">Enamel stable</text>')
    out.append(f'<text x="24" y="300" class="small">Each pH unit is a ten-fold change in [H⁺]: pH 4.5 has ten times the [H⁺] of pH 5.5.</text>')
    svg = (f'<svg viewBox="0 0 760 316" role="img" aria-label="pH scale with the critical pH of enamel, fluorapatite and root dentine">'
           f'<text x="24" y="30" class="title">One pH unit separates enamel from fluorapatite: a ten-fold change in acid</text>'
           f'<text x="24" y="50" class="sub">pH = −log₁₀[H⁺], [H⁺] in mol dm⁻³</text>'
           + "".join(out) + "</svg>")
    return _fig(svg, "Critical pH values on the pH scale.")


DIAGRAMS2 = {"pathway": pathway, "surfaces": surfaces, "stages": stages, "perio": perio,
             "trigeminal": trigeminal, "decon": decon, "sharps": sharps, "capacity": capacity, "phscale": phscale}
