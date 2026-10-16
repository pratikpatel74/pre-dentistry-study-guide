"""Third batch: diagrams for topics 10–17."""
import math
from diagrams2 import _arrow_defs, _box, _fig


def _strip(title, aria, steps, cap, W=128, G=18, x0=16, y0=64, H=78, acc_last=True, foot=None, pid="st"):
    out = [_arrow_defs(pid)]
    for i, (n, ls) in enumerate(steps):
        x = x0 + i * (W + G)
        out.append(_box(x, y0, W, H, n, ls, acc=(acc_last and i == len(steps) - 1)))
        if i < len(steps) - 1:
            out.append(f'<path d="M{x+W+2} {y0+H/2}H{x+W+G-2}" class="arrow" marker-end="url(#{pid}-a)"/>')
    h = y0 + H + 24
    if foot:
        out.append(f'<text x="{x0}" y="{y0+H+30}" class="small">{foot}</text>'); h += 18
    svg = (f'<svg viewBox="0 0 760 {h}" role="img" aria-label="{aria}"><text x="16" y="30" class="title">{title}</text>'
           + "".join(out) + "</svg>")
    return _fig(svg, cap)


# ---------- Topic 10: bonding a composite ----------
def bonding():
    return _strip("A white filling sticks by micro-locking into etched enamel",
                  "Steps to bond a composite filling",
                  [("1. Isolate", ["Keep the tooth", "dry (rubber dam)"]),
                   ("2. Etch", ["~37% phosphoric", "acid, then rinse"]),
                   ("3. Bond", ["Resin flows into", "the etched pores"]),
                   ("4. Cure", ["Blue light sets", "the bond layer"]),
                   ("5. Layer", ["Composite in thin", "increments, each cured"])],
                  "Placing a composite (white) filling.", W=132, G=17, pid="bd",
                  foot="Moisture at steps 2–3 is the commonest cause of failure: composite is 'technique-sensitive'.")


# ---------- Topic 11: LA and pH ----------
def laph():
    p = "la"
    out = [_arrow_defs(p)]
    out.append('<rect x="300" y="70" width="60" height="270" rx="6" class="bone"/>')
    out.append('<text x="330" y="62" text-anchor="middle" class="small lbl">Nerve membrane</text>')
    out.append('<text x="152" y="62" text-anchor="middle" class="small lbl">Tissue (outside)</text>')
    out.append('<text x="560" y="62" text-anchor="middle" class="small lbl">Inside the nerve</text>')
    # normal tissue
    out.append('<text x="40" y="112" class="lbl">Normal tissue, pH ≈ 7.4</text>')
    out.append(_box(40, 130, 90, 40, "BH⁺", [], name_size=15))
    out.append('<text x="85" y="186" text-anchor="middle" class="sub">charged</text>')
    out.append('<text x="152" y="156" text-anchor="middle" class="lbl">⇌</text>')
    out.append(_box(175, 130, 90, 40, "B", [], acc=True, name_size=15))
    out.append('<text x="220" y="186" text-anchor="middle" class="sub">uncharged base</text>')
    out.append(f'<path d="M266 150H392" class="arrow acc-stroke" marker-end="url(#{p}-a)"/>')
    out.append(_box(396, 130, 90, 40, "B → BH⁺", [], name_size=13))
    out.append(f'<path d="M486 150H522" class="arrow" marker-end="url(#{p}-a)"/>')
    out.append(_box(526, 126, 200, 48, "Blocks Na⁺ channel", [], acc=True))
    out.append('<text x="626" y="190" text-anchor="middle" class="sub ok-text">Pain blocked</text>')
    # infected tissue
    out.append('<text x="40" y="236" class="lbl danger">Infected tissue, pH ≈ 5–6</text>')
    out.append(_box(40, 254, 90, 40, "BH⁺ BH⁺", [], name_size=13))
    out.append('<text x="85" y="310" text-anchor="middle" class="sub">most is charged</text>')
    out.append('<text x="152" y="280" text-anchor="middle" class="lbl">⇌</text>')
    out.append(_box(195, 258, 50, 32, "B", [], name_size=11))
    out.append('<text x="220" y="310" text-anchor="middle" class="sub">little base left</text>')
    out.append(f'<path d="M246 274H296" class="arrow"/>')
    out.append('<text x="300" y="280" text-anchor="middle" class="lbl danger">✕</text>')
    out.append('<text x="396" y="270" class="small">Too little crosses the membrane,</text>')
    out.append('<text x="396" y="286" class="small">so the anaesthetic works poorly.</text>')
    svg = ('<svg viewBox="0 0 760 350" role="img" aria-label="Local anaesthetic crosses nerve membranes in its uncharged form; acidic infected tissue keeps it charged">'
           '<text x="24" y="30" class="title">Only the uncharged form crosses, so acidic, infected tissue resists numbing</text>'
           + "".join(out) + "</svg>")
    return _fig(svg, "Why local anaesthetic works poorly in infection (B = base form, BH⁺ = charged form).")

# ---------- Topic 12: referral flow ----------
def referral():
    p = "rf"
    out = [_arrow_defs(p)]
    out.append(_box(270, 56, 220, 46, "Soft-tissue check", [], acc=False))
    out.append('<text x="380" y="116" text-anchor="middle" class="sub">at every dental examination</text>')
    finds = [("Ulcer > 3 weeks", "unexplained"), ("Lump", "lip or mouth"), ("Red or red-white", "patch")]
    W, G, x0 = 200, 30, 50
    out.append(f'<path d="M380 120V136H{x0+W/2}M380 136H{x0+2*(W+G)+W/2}" class="arrow"/>')
    for i, (n, l) in enumerate(finds):
        x = x0 + i * (W + G)
        out.append(f'<path d="M{x+W/2} 136V150" class="arrow" marker-end="url(#{p}-a)"/>')
        out.append(_box(x, 152, W, 62, n, [l]))
        out.append(f'<path d="M{x+W/2} 214V236" class="arrow"/>')
    out.append(f'<path d="M{x0+W/2} 236H{x0+2*(W+G)+W/2}M380 236V254" class="arrow" marker-end="url(#{p}-a)"/>')
    out.append(_box(190, 256, 380, 62, "Urgent referral: suspected cancer pathway", ["Seen within 2 weeks; biopsy confirms the diagnosis"], acc=True))
    out.append('<text x="24" y="346" class="small">Traumatic ulcer? Remove the cause and review in about 2 weeks. If it hasn\'t healed, refer urgently.</text>')
    svg = ('<svg viewBox="0 0 760 360" role="img" aria-label="Findings that need urgent referral for suspected oral cancer">'
           '<text x="24" y="30" class="title">Three findings mean an urgent referral, not a wait-and-see</text>'
           + "".join(out) + "</svg>")
    return _fig(svg, "Red flags for oral cancer (based on NICE NG12).")


# ---------- Topic 13: radiolucent vs radiopaque ----------
def radio():
    X0, X1 = 60, 700
    items = [("Air / soft tissue", 0.05), ("Pulp", 0.17), ("Decay", 0.27), ("Bone", 0.45), ("Dentine", 0.58), ("Enamel", 0.74), ("Amalgam / metal", 0.95)]
    out = ['<defs><linearGradient id="rg-grad" x1="0" x2="1"><stop offset="0" stop-color="#111"/><stop offset="1" stop-color="#f5f5f5"/></linearGradient></defs>']
    out.append(f'<rect x="{X0}" y="150" width="{X1-X0}" height="34" rx="6" fill="url(#rg-grad)" class="frame-stroke"/>')
    for i, (n, f) in enumerate(items):
        x = X0 + f * (X1 - X0)
        up = i % 2 == 0
        ty = 120 if up else 222
        out.append(f'<line x1="{x:.0f}" x2="{x:.0f}" y1="{ty+(6 if up else -16)}" y2="{150 if up else 184}" class="leader thick"/>')
        out.append(f'<circle cx="{x:.0f}" cy="{150 if up else 184}" r="3.5" class="ink-fill"/>')
        out.append(f'<text x="{x:.0f}" y="{ty}" text-anchor="middle" class="lbl">{n}</text>')
    out.append(f'<text x="{X0}" y="270" class="lbl">← Radiolucent (dark)</text>')
    out.append(f'<text x="{X0}" y="288" class="sub">X-rays pass through</text>')
    out.append(f'<text x="{X1}" y="270" text-anchor="end" class="lbl">Radiopaque (white) →</text>')
    out.append(f'<text x="{X1}" y="288" text-anchor="end" class="sub">X-rays blocked</text>')
    svg = ('<svg viewBox="0 0 760 306" role="img" aria-label="Scale from radiolucent to radiopaque: air, pulp, decay, bone, dentine, enamel, metal">'
           '<text x="24" y="30" class="title">Decay shows as a dark area because it has lost mineral</text>'
           '<text x="24" y="50" class="sub">How dark or white each tissue looks on a radiograph (schematic order)</text>'
           + "".join(out) + "</svg>")
    return _fig(svg, "Reading radiographs: radiolucent vs radiopaque.")


# ---------- Topic 14: route timeline ----------
def route():
    phases = [
        ("Year 12", "Now – Jun 2027", ["Strong grades", "Work experience", "Volunteering"]),
        ("Summer 2027", "Jul – Sep 2027", ["Sit the UCAT", "Open days", "Draft statement"]),
        ("Apply", "By mid-Oct 2027", ["UCAS: up to 4", "dental schools", "+ 1 backup"]),
        ("Interviews", "Dec – Mar", ["MMI or panel", "Offers follow", "by spring 2028"]),
        ("Year 13 exams", "May – Jun 2028", ["Meet the offer", "(usually AAA)", ""]),
        ("Start BDS", "Sep 2028", ["Results day", "in August, then", "start dental school"]),
    ]
    W, G, x0, y0, H = 112, 13, 10, 92, 112
    p = "rt"
    out = [_arrow_defs(p)]
    for i, (n, d, ls) in enumerate(phases):
        x = x0 + i * (W + G)
        acc = i == 0
        out.append(f'<rect x="{x}" y="{y0}" width="{W}" height="{H}" rx="8" class="box{" acc" if acc else ""}"/>')
        out.append(f'<text x="{x+W/2}" y="{y0+24}" text-anchor="middle" class="lbl">{n}</text>')
        out.append(f'<text x="{x+W/2}" y="{y0+42}" text-anchor="middle" class="sub acc-text">{d}</text>')
        for j, l in enumerate([l for l in ls if l]):
            out.append(f'<text x="{x+W/2}" y="{y0+64+j*16}" text-anchor="middle" class="sub">{l}</text>')
        if i < len(phases) - 1:
            out.append(f'<path d="M{x+W+1} {y0+H/2}H{x+W+G-1}" class="arrow" marker-end="url(#{p}-a)"/>')
    out.append(f'<text x="{x0+W/2}" y="{y0-12}" text-anchor="middle" class="small lbl">You are here</text>')
    gx = x0 + 3 * (W + G) - G / 2
    out.append(f'<line x1="{gx}" x2="{gx}" y1="{y0-20}" y2="{y0+H+14}" class="crit"/>')
    out.append(f'<text x="{gx}" y="{y0+H+32}" text-anchor="middle" class="small lbl danger">UCAS deadline</text>')
    svg = ('<svg viewBox="0 0 760 252" role="img" aria-label="Timeline from Year 12 to starting dental school in September 2028">'
           '<text x="10" y="30" class="title">Two years from now to the dental chair: the deadline falls in October 2027</text>'
           '<text x="10" y="50" class="sub">Dates for 2027–28 follow recent cycles; check UCAS and UCAT when they publish</text>'
           + "".join(out) + "</svg>")
    return _fig(svg, "Route to September 2028 entry.")


# ---------- Topic 15: UCAT seconds per question ----------
def ucat():
    rows = [("Verbal Reasoning", 44, 22), ("Decision Making", 35, 37), ("Quantitative Reasoning", 36, 26), ("Situational Judgement", 69, 26)]
    X0, scale = 230, 6.2  # px per second
    out = []
    for i, (n, q, m) in enumerate(rows):
        y = 80 + i * 56
        s = m * 60 / q
        w = s * scale
        cls = "bar acc-fill" if n == "Decision Making" else "bar"
        out.append(f'<text x="{X0-12}" y="{y+18}" text-anchor="end" class="lbl">{n}</text>')
        out.append(f'<text x="{X0-12}" y="{y+34}" text-anchor="end" class="sub">{q} questions · {m} min</text>')
        out.append(f'<rect x="{X0}" y="{y+4}" width="{w:.0f}" height="26" rx="5" class="{cls}"/>')
        out.append(f'<text x="{X0+w+10:.0f}" y="{y+22}" class="lbl">{s:.0f} s</text>')
    for t in (0, 20, 40, 60):
        x = X0 + t * scale
        out.append(f'<line x1="{x}" x2="{x}" y1="74" y2="306" class="gridline"/>')
        out.append(f'<text x="{x}" y="322" text-anchor="middle" class="sub">{t} s</text>')
    svg = ('<svg viewBox="0 0 760 340" role="img" aria-label="Seconds available per question in each UCAT subtest">'
           '<text x="24" y="30" class="title">Situational Judgement and Verbal Reasoning give under 30 seconds a question</text>'
           '<text x="24" y="50" class="sub">Time per question in each UCAT subtest (standard timing)</text>'
           + "".join(out) + "</svg>")
    return _fig(svg, "UCAT pacing: seconds per question.")



def _ring(cx, cy, rx, ry, nodes, W, H, pid, acc_idx=(), gap=22):
    out = [_arrow_defs(pid)]
    n = len(nodes)
    angs = [-90 + i * 360 / n for i in range(n)]
    for i, ((name, line), a) in enumerate(zip(nodes, angs)):
        x = cx + rx * math.cos(math.radians(a)); y = cy + ry * math.sin(math.radians(a))
        out.append(_box(x - W / 2, y - H / 2, W, H, name, [line], acc=(i in acc_idx)))
    for a in angs:
        t1, t2 = math.radians(a + gap), math.radians(a + 360 / n - gap)
        x1, y1 = cx + rx * math.cos(t1), cy + ry * math.sin(t1)
        x2, y2 = cx + rx * math.cos(t2), cy + ry * math.sin(t2)
        out.append(f'<path d="M{x1:.1f} {y1:.1f} A{rx} {ry} 0 0 1 {x2:.1f} {y2:.1f}" class="arrow" marker-end="url(#{pid}-a)"/>')
    return out

# ---------- Topic 16: MMI circuit ----------
def mmi():
    cx, cy = 380, 250
    st = [("Motivation", "Why dentistry?"), ("Ethics", "A dilemma"), ("Role-play", "Anxious patient"),
          ("Data", "Read a chart"), ("Dexterity", "Wire bending"), ("NHS insight", "Current issues")]
    out = _ring(cx, cy, 240, 150, st, 140, 52, "mm", gap=20)
    out.append(f'<text x="{cx}" y="{cy-8}" text-anchor="middle" class="lbl big">You rotate</text>')
    out.append(f'<text x="{cx}" y="{cy+12}" text-anchor="middle" class="sub">~5–10 min per station</text>')
    out.append(f'<text x="{cx}" y="{cy+28}" text-anchor="middle" class="sub">each scored separately</text>')
    svg = ('<svg viewBox="0 0 760 450" role="img" aria-label="A multiple mini-interview circuit with six example stations">'
           '<text x="24" y="30" class="title">An MMI is a circuit: one weak station doesn\'t sink you</text>'
           '<text x="24" y="50" class="sub">Example station types; each school chooses its own mix</text>'
           + "".join(out) + "</svg>")
    return _fig(svg, "Example MMI circuit.")


# ---------- Topic 17: Gibbs reflective cycle ----------
def gibbs():
    cx, cy = 380, 250
    st = [("Description", "What happened?"), ("Feelings", "What did you think?"), ("Evaluation", "What went well, or not?"),
          ("Analysis", "Why? What does it mean?"), ("Conclusion", "What did you learn?"), ("Action plan", "What will you do next?")]
    out = _ring(cx, cy, 240, 150, st, 156, 52, "gb", acc_idx=(3, 4), gap=22)
    out.append(f'<text x="{cx}" y="{cy-4}" text-anchor="middle" class="lbl big">Gibbs</text>')
    out.append(f'<text x="{cx}" y="{cy+14}" text-anchor="middle" class="sub">reflective cycle</text>')
    svg = ('<svg viewBox="0 0 760 450" role="img" aria-label="Gibbs reflective cycle: description, feelings, evaluation, analysis, conclusion, action plan">'
           '<text x="24" y="30" class="title">Most applicants describe; the marks are in analysis and what you learned</text>'
           '<text x="24" y="50" class="sub">Use it for your reflective diary, personal statement and interview answers</text>'
           + "".join(out) + "</svg>")
    return _fig(svg, "Gibbs' reflective cycle (1988).")


DIAGRAMS3 = {"bonding": bonding, "laph": laph, "referral": referral, "radio": radio,
             "route": route, "ucat": ucat, "mmi": mmi, "gibbs": gibbs}
