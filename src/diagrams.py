"""Inline SVG diagrams. Colours come from CSS variables defined on notes pages."""

def tooth():
    lead = lambda px, py, ly: (f'<circle cx="{px}" cy="{py}" r="2.5" class="ink-fill"/>'
                               f'<path d="M{px} {py}L556 {ly-4}H560" class="leader"/>')
    labels = [("Enamel", 497, 130, 96), ("Pulp chamber", 420, 175, 136), ("Dentine", 470, 258, 176),
              ("Gingiva (gum)", 512, 222, 216), ("Periodontal ligament", 495, 275, 256),
              ("Alveolar bone", 512, 305, 296), ("Cementum", 487, 340, 336), ("Root canal", 454, 340, 376)]
    leads = "".join(lead(px, py, ly) for _, px, py, ly in labels)
    texts = "".join(f'<text x="564" y="{ly}" class="lbl">{t}</text>' for t, _, _, ly in labels)
    outline = ("M172 200 C160 150, 165 100, 200 85 Q225 75, 240 90 Q260 70, 280 90 Q295 75, 320 85 "
               "C355 100, 360 150, 348 200 L345 260 C340 330, 330 380, 315 400 Q305 410, 295 400 "
               "C290 360, 285 300, 270 270 Q260 255, 250 270 C235 300, 230 360, 225 400 Q215 410, 205 400 "
               "C190 380, 180 330, 175 260 Z")
    return f'''<figure class="diagram"><svg viewBox="0 0 760 450" role="img" aria-label="Cross-section of a molar showing enamel, dentine, pulp and supporting tissues">
<text x="24" y="30" class="title">A molar: three layers inside, held in the jaw by four tissues</text>
<g transform="translate(150,0)">
<rect x="145" y="238" width="230" height="192" rx="8" class="bone"/>
<path d="M348 238 L345 260 C340 330, 330 380, 315 400 Q305 410, 295 400 C290 360, 285 300, 270 270 Q260 255, 250 270 C235 300, 230 360, 225 400 Q215 410, 205 400 C190 380, 180 330, 175 260 L173 238" class="pdl"/>
<path d="{outline}" class="dentine"/>
<path d="M172 200 C160 150, 165 100, 200 85 Q225 75, 240 90 Q260 70, 280 90 Q295 75, 320 85 C355 100, 360 150, 348 200 L334 200 C342 155, 338 118, 315 105 Q295 97, 280 108 Q260 92, 240 108 Q225 97, 205 105 C182 118, 178 155, 186 200 Z" class="enamel"/>
<path d="M225 150 Q240 135, 260 145 Q280 135, 295 150 L298 210 C300 250, 305 320, 308 392 L302 394 C295 320, 285 260, 270 235 Q260 225, 250 235 C235 260, 225 320, 218 394 L212 392 C215 320, 220 250, 222 210 Z" class="pulp"/>
<path d="M145 240 L145 215 Q158 197, 172 192 C174 210, 175 225, 176 240 Z" class="gum"/>
<path d="M375 240 L375 215 Q362 197, 348 192 C346 210, 345 225, 344 240 Z" class="gum"/>
</g>
<path d="M286 80 H278 V196 H286" class="leader thick"/><path d="M286 204 H278 V408 H286" class="leader thick"/>
<text x="270" y="142" text-anchor="end" class="lbl">Crown</text><text x="270" y="158" text-anchor="end" class="sub">visible in the mouth</text>
<text x="270" y="300" text-anchor="end" class="lbl">Root</text><text x="270" y="316" text-anchor="end" class="sub">hidden in bone</text>
{leads}{texts}<text x="564" y="392" class="sub">nerves, vessels enter at apex</text>
</svg><figcaption>Cross-section of a lower molar: tooth tissues and supporting tissues.</figcaption></figure>'''


def fdi():
    def typ(d):
        return "inc" if d <= 2 else "can" if d == 3 else "pm" if d <= 5 else "mol"
    out = []
    def row(nums, x0, y, primary=False):
        for i, n in enumerate(nums):
            d = n % 10
            t = "mol" if primary and d >= 4 else typ(d)
            x = x0 + i * 40
            extra = ' hl' if n == 16 else ''
            out.append(f'<rect x="{x}" y="{y}" width="36" height="36" rx="6" class="tt {t}{extra}"/>'
                       f'<text x="{x+18}" y="{y+23}" text-anchor="middle" class="num{extra}">{n}</text>')
    row([18,17,16,15,14,13,12,11], 52, 100); row([21,22,23,24,25,26,27,28], 392, 100)
    row([48,47,46,45,44,43,42,41], 52, 156); row([31,32,33,34,35,36,37,38], 392, 156)
    row([55,54,53,52,51], 172, 286, True); row([61,62,63,64,65], 392, 286, True)
    row([85,84,83,82,81], 172, 342, True); row([71,72,73,74,75], 392, 342, True)
    key = "".join(f'<rect x="{x}" y="424" width="16" height="16" rx="4" class="tt {c}"/><text x="{x+24}" y="437" class="small">{t}</text>'
                  for x, c, t in [(52,"inc","Incisors (1, 2)"),(192,"can","Canine (3)"),(322,"pm","Premolars (4, 5)"),(472,"mol","Molars (6–8; primary 4–5)")])
    return f'''<figure class="diagram"><svg viewBox="0 0 760 456" role="img" aria-label="FDI tooth numbering chart for permanent and primary teeth">
<text x="24" y="30" class="title">FDI notation: quadrant first, then position counted from the midline</text>
<text x="24" y="50" class="sub">Drawn as you face the patient, so their right is on your left. Upper right first molar = 16.</text>
<line x1="40" x2="720" y1="146" y2="146" class="axis"/><line x1="380" x2="380" y1="84" y2="202" class="axis"/>
<text x="210" y="90" text-anchor="middle" class="lbl">Quadrant 1 · upper right</text><text x="550" y="90" text-anchor="middle" class="lbl">Quadrant 2 · upper left</text>
<text x="210" y="214" text-anchor="middle" class="lbl">Quadrant 4 · lower right</text><text x="550" y="214" text-anchor="middle" class="lbl">Quadrant 3 · lower left</text>
<text x="24" y="250" class="lbl big">Primary (baby) teeth use quadrants 5 to 8, five teeth each</text>
<line x1="160" x2="600" y1="332" y2="332" class="axis"/><line x1="380" x2="380" y1="270" y2="388" class="axis"/>
<text x="270" y="276" text-anchor="middle" class="lbl">5 · upper right</text><text x="490" y="276" text-anchor="middle" class="lbl">6 · upper left</text>
<text x="270" y="400" text-anchor="middle" class="lbl">8 · lower right</text><text x="490" y="400" text-anchor="middle" class="lbl">7 · lower left</text>
{"".join(out)}{key}
</svg><figcaption>FDI two-digit notation for the permanent and primary dentitions.</figcaption></figure>'''


def stephan():
    return '''<figure class="diagram"><svg viewBox="0 0 760 330" role="img" aria-label="Stephan curve: plaque pH drops below the critical pH after sugar, then recovers">
<defs><marker id="st-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="axis-fill"/></marker></defs>
<text x="24" y="30" class="title">Each sugar hit drops plaque pH below the critical point for up to an hour</text>
<text x="24" y="50" class="sub">The Stephan curve (schematic, not to scale)</text>
<rect x="90" y="180" width="610" height="104" class="danger-zone"/>
<path d="M90 284 V76" class="axis" marker-end="url(#st-arrow)"/><path d="M90 284 H712" class="axis" marker-end="url(#st-arrow)"/>
<line x1="90" x2="700" y1="180" y2="180" class="crit"/>
<path d="M90 110 H150 C165 110, 175 240, 205 240 C260 240, 330 160, 420 130 C480 112, 540 110, 700 110" class="curve"/>
<path d="M150 72 V100" class="axis" marker-end="url(#st-arrow)"/>
<text x="60" y="180" text-anchor="middle" class="sub" transform="rotate(-90 60 180)">Plaque pH</text>
<text x="700" y="306" text-anchor="end" class="sub">Time after a sugary snack or drink</text>
<text x="160" y="80" class="lbl">Sugar eaten</text>
<text x="250" y="96" class="lbl">Above the line: enamel repairs</text>
<text x="560" y="100" class="small">Resting pH, about 6.5–7</text>
<text x="560" y="172" class="lbl">Critical pH ≈ 5.5 (enamel)</text>
<text x="214" y="262" class="small">Bacteria make acid within minutes</text>
<text x="330" y="206" class="small">Saliva buffers it back over 30–60 min</text>
<text x="470" y="250" class="lbl danger">Below the line: enamel dissolves</text>
<text x="470" y="266" class="sub">(demineralisation)</text>
</svg><figcaption>Stephan curve: plaque pH after one sugar intake.</figcaption></figure>'''


DIAGRAMS = {"tooth": tooth, "fdi": fdi, "stephan": stephan}
