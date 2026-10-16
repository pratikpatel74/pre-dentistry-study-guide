"""Topic 9 notes: A-level -> dentistry bridge, linking to Pratik's AQA hubs."""

HUBS = {
    "Biology": ("https://aqa-alevel-biology.netlify.app/", "AQA Biology hub"),
    "Chemistry": ("https://aqa-alevel-chemistry.netlify.app/", "AQA Chemistry hub"),
    "Maths": ("https://aqa-alevel-maths.netlify.app/", "AQA Maths hub"),
}
PD = {1: "UK dentistry", 2: "Tooth anatomy", 3: "Notation", 4: "Caries", 5: "Gum disease",
      6: "Head &amp; neck", 7: "Infection control", 8: "Professionalism", 9: "This page"}

ROWS = {
    "Biology": [
        ("3.1a", "Monomers, carbohydrates and lipids", "Why sucrose is the most cariogenic sugar; starch vs sugar; sweeteners like xylitol", [4]),
        ("3.1b", "Proteins and enzymes", "Collagen in dentine and the periodontal ligament; salivary amylase; fluoride inhibits bacterial enolase", [2, 4]),
        ("3.1c", "Nucleic acids, ATP, water and ions", "Calcium and phosphate ions in saliva drive remineralisation", [4]),
        ("3.2a", "Cell structure and studying cells", "Odontoblasts and ameloblasts; plaque bacteria are prokaryotic cells", [2, 4]),
        ("3.2c", "Transport across cell membranes", "Local anaesthetic must cross the nerve membrane (lipid-soluble form) to work", [9]),
        ("3.2d", "Cell recognition and the immune system", "Hepatitis B vaccine and antibody check; inflammation in gum disease", [5, 7]),
        ("3.3b", "Digestion and absorption", "Digestion starts in the mouth: saliva and amylase", [6]),
        ("3.3c", "Mass transport in animals", "Heart and blood pressure: fainting, adrenaline narrowing vessels in anaesthetics", [7, 9]),
        ("3.5b", "Respiration", "Plaque bacteria ferment sugar to lactic acid (anaerobic respiration)", [4]),
        ("3.6b", "Nerve impulses and synaptic transmission", "Local anaesthetics block voltage-gated Na⁺ channels; trigeminal nerve", [6, 9]),
        ("3.6c", "Skeletal muscle", "Muscles of mastication; jaw opening and closing", [6]),
        ("3.6d", "Homeostasis and blood glucose", "Diabetes and gum disease (two-way link); hypoglycaemia in the dental chair", [5, 7]),
        ("3.7c", "Evolution and speciation", "Antibiotic resistance is natural selection: why stewardship matters", [9]),
        ("3.8b", "Gene expression, epigenetics and cancer", "Dentists screen the mouth for oral cancer at every check-up", [1]),
    ],
    "Chemistry": [
        ("3.1.2", "Amount of substance", "Concentrations, % solutions, mg per mL: drug dose calculations", [9]),
        ("3.1.3", "Bonding", "Hydroxyapatite is an ionic lattice; hydrogen bonds in collagen", [2]),
        ("3.1.6", "Chemical equilibria and Kc", "Demineralisation ⇌ remineralisation; Le Chatelier and acid attack", [4]),
        ("3.1.7", "Oxidation, reduction and redox equations", "Corrosion of metal fillings and instruments", [9]),
        ("3.1.11", "Electrode potentials and cells", "Two different metals in the mouth can form a cell: 'galvanic' tooth pain", [9]),
        ("3.1.12", "Acids and bases", "pH, critical pH of enamel, saliva's bicarbonate buffer", [4, 9]),
        ("3.2.2", "Group 2, the alkaline earth metals", "Calcium chemistry; calcium hydroxide used as a lining under fillings", [2]),
        ("3.2.3", "Group 7, the halogens", "Fluoride in toothpaste; sodium hypochlorite (bleach) cleans root canals", [4, 7]),
        ("3.3.9", "Carboxylic acids and derivatives", "Lactic acid from plaque bacteria", [4]),
        ("3.3.12", "Polymers", "Composite fillings set by light-activated polymerisation; acrylic dentures", [9]),
        ("3.3.13", "Amino acids, proteins and DNA", "Collagen structure in dentine, cementum and gums", [2, 5]),
    ],
    "Maths": [
        ("p1", "Proof, indices and surds", "Standard form and indices: [H⁺] = 10⁻⁵ mol dm⁻³", [9]),
        ("p7", "Exponentials and logarithms", "pH is a log scale; bacterial growth is exponential", [4, 9]),
        ("s1", "Sampling and data presentation", "Reading clinical studies: sample size, bias, charts", [9]),
        ("s2", "Probability", "Risk, and how often a test gives a false result", [9]),
        ("s6", "The normal distribution", "Normal ranges, e.g. blood glucose; spread of results in trials", [7, 9]),
        ("s7", "Correlation and hypothesis testing", "p-values; gum disease is linked to heart disease, but correlation is not causation", [5, 9]),
        ("m6", "Moments", "Forceps and elevators are levers; the jaw works as a lever", [6]),
    ],
}

def _row(subj, hid, title, back, pds):
    url = HUBS[subj][0] + "#s-" + hid
    pd = ", ".join(f'<a href="topic{n}.html">{n} · {PD[n]}</a>' if n != 9 else "This page" for n in pds)
    return (f'<tr><td><a href="{url}" target="_blank" rel="noopener">{title}</a>'
            f'<div class="ref">AQA {hid}</div></td><td>{back}</td><td class="pd">{pd}</td></tr>')

def notes():
    parts = ['<p class="lead">Much of year 1 is A-level Biology and Chemistry applied to the mouth. '
             'Each A-level topic below links to its summary and quiz in your AQA revision hubs.</p>',
             '<p class="hub-links">' + " · ".join(f'<a href="{u}" target="_blank" rel="noopener">{n} →</a>' for u, n in HUBS.values()) + '</p>']
    for subj, rows in ROWS.items():
        parts.append(f'<h2>{subj}</h2>')
        parts.append('<table class="bridge"><tr><th>A-level topic</th><th>Comes back in dentistry as</th><th>Pre-Dentistry topic</th></tr>'
                     + "".join(_row(subj, *r) for r in rows) + '</table>')
    parts.append("""<h2>Chemistry to know cold</h2>
<div class="formula">Ca₁₀(PO₄)₆(OH)₂ + 8H⁺ ⇌ 10Ca²⁺ + 6HPO₄²⁻ + 2H₂O</div>
<div class="formula">Ca₁₀(PO₄)₆(OH)₂ + 2F⁻ → Ca₁₀(PO₄)₆F₂ + 2OH⁻</div>
<div class="formula">HCO₃⁻ + H⁺ → H₂CO₃ → H₂O + CO₂</div>
{{D:phscale}}
<h2>Worked maths: local anaesthetic</h2>
<p>2% = 2 g per 100 mL = 20 mg/mL. A 2.2 mL cartridge holds 2.2 × 20 = 44 mg. Maximum doses are per kg of body weight, so practise mg/kg sums. Learn the official maximum doses from your course.</p>
<ol><li>Patient weighs 70 kg; the given limit is 4.4 mg/kg.</li><li>Maximum = 70 × 4.4 = 308 mg.</li><li>Cartridges = 308 ÷ 44 = 7.</li></ol>""")
    return "\n".join(parts)

def count():
    return sum(len(r) for r in ROWS.values())
