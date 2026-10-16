# Each question: (question, [correct, wrong, wrong, wrong], explanation)
# Correct answer is ALWAYS first here; the quiz shuffles options on screen.

T1 = dict(
    num=1, slug="landscape", short="UK Dentistry",
    title="The UK Dental Landscape",
    dark="#818cf8", light="#6366f1",
    blurb="BDS course structure, the GDC, the seven dental team roles, Dental Foundation Training and NHS charge bands.",
    icon='<path d="M3 21h18M5 21V10l7-5 7 5v11M9 21v-6h6v6"/>',
    qs=[
        ("Which body registers and regulates dentists in the UK?", ["General Dental Council (GDC)", "Care Quality Commission (CQC)", "British Dental Association (BDA)", "NHS England"], "The GDC keeps the register and sets professional standards. The BDA is the profession's association; the CQC inspects practices in England."),
        ("What does BDS stand for?", ["Bachelor of Dental Surgery", "Bachelor of Dental Science", "British Dental Standard", "Basic Dental Studies"], "BDS = Bachelor of Dental Surgery, the standard UK undergraduate dental degree."),
        ("How long is a standard UK undergraduate dental degree?", ["5 years", "3 years", "4 years", "6 years"], "Most BDS courses are 5 years. Some schools offer 4-year graduate-entry courses."),
        ("What do most new dentists complete after graduating before working independently in NHS general practice?", ["One year of Dental Foundation Training (DFT)", "A two-year foundation programme like doctors", "A master's degree", "Nothing further is needed"], "DFT is a one-year supervised training post in an NHS practice."),
        ("Which team member can place simple fillings and extract baby teeth?", ["Dental therapist", "Dental nurse", "Dental technician", "Orthodontic therapist"], "Dental therapists do hygienist work plus simple restorations and primary tooth extractions."),
        ("Who makes crowns, bridges and dentures in the laboratory?", ["Dental technician", "Dental hygienist", "Dental nurse", "Dental therapist"], "Dental technicians make appliances and restorations to a dentist's prescription."),
        ("Which of these can prescribe prescription-only medicines in a dental setting?", ["Dentist", "Dental nurse", "Dental technician", "Orthodontic therapist"], "Dentists diagnose, plan treatment and prescribe; the wider team cannot prescribe."),
        ("What is the NHS Band 1 patient charge in England from 1 April 2026?", ["£27.90", "£76.60", "£332.10", "£20.00"], "Band 1 = £27.90 (examination, diagnosis, X-rays, scale and polish)."),
        ("Which NHS band covers fillings, root canal treatment and extractions?", ["Band 2", "Band 1", "Band 3", "Urgent care"], "Band 2 (£76.60 from April 2026) covers Band 1 plus fillings, root canals and extractions."),
        ("Which NHS band covers crowns, bridges and dentures?", ["Band 3", "Band 2", "Band 1", "Urgent care"], "Band 3 (£332.10 from April 2026) covers lab-made work."),
        ("A patient needs a check-up, two fillings and a crown in one course of treatment. What do they pay?", ["One Band 3 charge", "Band 1 + Band 2 + Band 3", "Band 1 + Band 3", "Two Band 2 charges plus Band 3"], "Patients pay one charge per course of treatment: the highest band needed."),
        ("Who is automatically exempt from NHS dental charges in England?", ["A 17-year-old", "A 66-year-old, on age alone", "A 21-year-old university student", "Anyone on a waiting list"], "Under-18s are exempt. Age alone does not exempt pensioners; under-19s in full-time education and pregnant women are also exempt."),
        ("Which organisation inspects dental practices in England for quality and safety?", ["Care Quality Commission (CQC)", "General Dental Council", "British Dental Association", "NICE"], "The CQC inspects and rates health and care providers, including dental practices, in England."),
        ("What is the British Dental Association (BDA)?", ["The professional association and trade union for dentists", "The legal regulator of dentists", "An NHS department", "A dental school"], "The BDA represents dentists; it does not regulate them (that is the GDC)."),
        ("What is a 'phantom head'?", ["A mannequin head used to practise clinical skills", "A ghost image on an X-ray", "An anaesthetic technique", "A patient who misses appointments"], "Students practise drilling and fillings on phantom heads before treating patients."),
        ("Which of these is a GDC-registered profession?", ["Clinical dental technician", "Dental receptionist", "Practice manager", "Dental sales representative"], "The seven registered roles: dentist, dental nurse, hygienist, therapist, orthodontic therapist, dental technician, clinical dental technician."),
        ("How many GDC-registered dental professions are there, including dentists?", ["7", "3", "5", "10"], "Dentist, dental nurse, hygienist, therapist, orthodontic therapist, dental technician and clinical dental technician."),
        ("What does a dental hygienist mainly provide?", ["Prevention and gum (periodontal) treatment", "Crowns and bridges", "Orthodontic diagnosis", "Surgical extractions"], "Hygienists focus on prevention, scaling and periodontal care."),
        ("How much is an urgent NHS course of treatment in England from April 2026?", ["£27.90, the same as Band 1", "£76.60, the same as Band 2", "£332.10", "It is free for everyone"], "Urgent care is charged at the Band 1 rate: £27.90."),
        ("Can a dental student's behaviour outside university affect their fitness to practise?", ["Yes, professional standards apply in and out of clinic", "No, only behaviour in clinic counts", "Only after they graduate", "Only if a patient complains"], "Students are held to professional standards from day one, including online and in their private life."),
        ("What does an orthodontic therapist do?", ["Helps carry out brace treatment to an orthodontist's prescription", "Makes dentures for patients directly", "Diagnoses gum disease", "Prescribes antibiotics"], "Orthodontic therapists work under an orthodontist's prescription."),
        ("Who provides complete dentures directly to patients, without a dentist making them?", ["Clinical dental technician", "Dental nurse", "Dental hygienist", "Orthodontic therapist"], "Clinical dental technicians can provide complete dentures directly to patients."),
    ],
    notes="""
<p class="lead">UK dentistry is a regulated profession. Every dentist must be registered with the General Dental Council (GDC), and patients are treated through the NHS or privately.</p>
{{D:pathway}}
<h2>The BDS course (typical shape)</h2>
<ol>
<li><b>Years 1–2:</b> biomedical sciences (anatomy, physiology, biochemistry, oral biology), phantom-head skills, early patient contact.</li>
<li><b>Years 3–4:</b> treating patients under supervision: fillings, extractions, gum care, root canals, crowns, dentures, children's dentistry.</li>
<li><b>Year 5:</b> consolidation, outreach clinics, finals.</li>
<li><b>After graduating:</b> one year of Dental Foundation Training (DFT) in an NHS practice.</li>
</ol>
<p>Courses vary by university, so check your chosen school's handbook.</p>
<h2>The dental team (all GDC-registered)</h2>
<table><tr><th>Role</th><th>What they do</th></tr>
<tr><td>Dentist</td><td>Diagnoses, plans and carries out all treatment; prescribes; leads the team</td></tr>
<tr><td>Dental nurse</td><td>Chairside support, decontamination, records</td></tr>
<tr><td>Dental hygienist</td><td>Prevention, scaling, gum treatment</td></tr>
<tr><td>Dental therapist</td><td>Hygienist work plus simple fillings and baby-tooth extractions</td></tr>
<tr><td>Orthodontic therapist</td><td>Brace treatment to an orthodontist's prescription</td></tr>
<tr><td>Dental technician</td><td>Makes crowns, bridges, dentures, appliances</td></tr>
<tr><td>Clinical dental technician</td><td>Provides complete dentures directly to patients</td></tr></table>
<h2>NHS dental charges in England (from 1 April 2026)</h2>
<table><tr><th>Band</th><th>Covers</th><th>Charge</th></tr>
<tr><td>Band 1</td><td>Examination, diagnosis, X-rays, scale and polish</td><td>£27.90</td></tr>
<tr><td>Band 2</td><td>Band 1 + fillings, root canals, extractions</td><td>£76.60</td></tr>
<tr><td>Band 3</td><td>Band 1 and 2 + crowns, bridges, dentures</td><td>£332.10</td></tr>
<tr><td>Urgent</td><td>Urgent course of treatment</td><td>£27.90</td></tr></table>
<p>One charge per course of treatment (the highest band). Exempt: under-18s, under-19s in full-time education, pregnant women or those with a baby under 12 months, and some benefit recipients. Source: <a href="https://faq.nhsbsa.nhs.uk/knowledgebase/article/KA-02003" target="_blank" rel="noopener">NHSBSA</a>.</p>
<h2>Other bodies to know</h2>
<ul><li><b>GDC</b>: regulator. <b>BDA</b>: professional association and trade union. <b>CQC</b>: inspects practices in England.</li></ul>
""",
)

T2 = dict(
    num=2, slug="anatomy", short="Tooth Anatomy",
    title="Tooth Anatomy & Tissues",
    dark="#38bdf8", light="#0ea5e9",
    blurb="Enamel, dentine, pulp and cementum; the periodontal ligament, alveolar bone and gingiva; naming tooth surfaces.",
    icon='<path d="M7 3c-2 0-3 2-3 4 0 3 1 5 2 8l1 6h2l1-5h4l1 5h2l1-6c1-3 2-5 2-8 0-2-1-4-3-4-2 0-3 1-5 1S9 3 7 3z"/>',
    diagram="tooth",
    qs=[
        ("What is the hardest substance in the human body?", ["Enamel", "Dentine", "Cementum", "Compact bone"], "Enamel is about 96% mineral, mostly hydroxyapatite."),
        ("Which mineral makes up most of enamel?", ["Hydroxyapatite", "Calcium carbonate", "Fluorite", "Calcium sulfate"], "Hydroxyapatite: Ca₁₀(PO₄)₆(OH)₂."),
        ("Roughly what percentage of enamel (by weight) is mineral?", ["About 96%", "About 70%", "About 45%", "About 20%"], "Enamel ~96%, dentine ~70%, cementum ~45–50%."),
        ("Which part of the tooth contains nerves and blood vessels?", ["Pulp", "Enamel", "Dentine", "Cementum"], "The pulp keeps the tooth alive; decay reaching it causes toothache."),
        ("Why does exposed dentine feel sensitive?", ["It contains tubules that carry stimuli towards the pulp", "It is covered in nerve endings", "It has no mineral content", "It is thicker than enamel"], "Fluid movement in dentinal tubules triggers pulp nerves (hydrodynamic theory)."),
        ("Which cells form dentine?", ["Odontoblasts", "Ameloblasts", "Osteoclasts", "Cementoblasts"], "Odontoblasts line the pulp and keep making dentine throughout life."),
        ("Can enamel regrow once it has been lost?", ["No, it has no living cells after the tooth erupts", "Yes, ameloblasts keep making it", "Yes, but only in children", "Only with fluoride toothpaste"], "Ameloblasts are lost when the tooth erupts, so lost enamel cannot regenerate (minerals can be partly redeposited by remineralisation)."),
        ("Which tissue covers the root of the tooth?", ["Cementum", "Enamel", "Gingiva", "Pulp"], "Cementum covers the root and anchors periodontal ligament fibres."),
        ("What attaches the tooth to its socket?", ["Periodontal ligament", "Gingiva", "Pulp", "Enamel"], "Collagen fibres of the PDL run from cementum to alveolar bone."),
        ("What is the bone that forms the tooth socket called?", ["Alveolar bone", "Hyoid bone", "Mandibular condyle", "Zygomatic bone"], "Alveolar bone surrounds the roots; it shrinks after a tooth is lost."),
        ("What is the cemento-enamel junction (CEJ)?", ["The line where enamel meets cementum at the neck of the tooth", "Where enamel meets dentine", "The tip of the root", "The biting surface"], "The CEJ marks the boundary between crown and root."),
        ("Where do nerves and blood vessels enter the tooth?", ["The apical foramen at the root tip", "The CEJ", "The occlusal fissures", "The furcation"], "They pass through the apical foramen into the root canal."),
        ("Which tooth surface faces towards the midline of the dental arch?", ["Mesial", "Distal", "Buccal", "Lingual"], "Mesial = towards the midline; distal = away from it."),
        ("Which surface of a lower tooth faces the tongue?", ["Lingual", "Palatal", "Buccal", "Labial"], "Lingual for lower teeth; the equivalent on upper teeth is palatal."),
        ("What is the biting surface of a molar called?", ["Occlusal", "Incisal", "Mesial", "Cervical"], "Back teeth have occlusal surfaces; front teeth have incisal edges."),
        ("Which surface of an upper tooth faces the roof of the mouth?", ["Palatal", "Lingual", "Buccal", "Distal"], "Upper teeth: palatal. Lower teeth: lingual."),
        ("Which surface of an incisor faces the lips?", ["Labial", "Buccal", "Lingual", "Distal"], "Labial for front teeth; buccal for back teeth (towards the cheek)."),
        ("Roughly what percentage of dentine (by weight) is mineral?", ["About 70%", "About 96%", "About 45%", "About 10%"], "Dentine is ~70% mineral, plus collagen and water."),
        ("What is tertiary (reparative) dentine?", ["Dentine laid down in response to irritation such as decay", "The first enamel to form", "Another name for cementum", "Dentine in baby teeth only"], "Odontoblasts lay down tertiary dentine to protect the pulp."),
        ("What is inflammation of the pulp called?", ["Pulpitis", "Gingivitis", "Periodontitis", "Stomatitis"], "Pulpitis causes toothache and may need root canal treatment."),
        ("What is the furcation of a tooth?", ["Where the roots of a multi-rooted tooth divide", "The root tip", "The neck of the tooth", "A cusp on the crown"], "Furcations matter in gum disease because bone loss there is hard to treat."),
        ("What seals around the neck of the tooth?", ["Gingiva (gum)", "Cementum", "Dentine", "Pulp"], "The gingiva forms a cuff around the tooth just above the bone."),
    ],
    notes="""
<p class="lead">Every tooth has a crown covered in enamel and a root covered in cementum, built around dentine with living pulp at the centre.</p>
{{DIAGRAM}}
<h2>The tissues</h2>
<table><tr><th>Tissue</th><th>Made of</th><th>Key facts</th></tr>
<tr><td>Enamel</td><td>~96% mineral (hydroxyapatite)</td><td>Hardest substance in the body; no living cells, cannot regrow</td></tr>
<tr><td>Dentine</td><td>~70% mineral + collagen, water</td><td>Has tubules, so exposed dentine is sensitive; made by odontoblasts throughout life</td></tr>
<tr><td>Pulp</td><td>Soft tissue, nerves, vessels</td><td>Keeps the tooth alive; pulpitis causes pain</td></tr>
<tr><td>Cementum</td><td>~45–50% mineral</td><td>Covers the root; anchors ligament fibres</td></tr>
<tr><td>Periodontal ligament</td><td>Collagen fibres</td><td>Holds the tooth; senses biting pressure</td></tr>
<tr><td>Alveolar bone</td><td>Bone</td><td>Forms the socket; shrinks after tooth loss</td></tr>
<tr><td>Gingiva</td><td>Mucosa</td><td>Seals around the neck of the tooth</td></tr></table>
<h2>Naming surfaces</h2>
{{D:surfaces}}
<ul>
<li><b>Mesial</b> (towards the midline) and <b>distal</b> (away from it)</li>
<li><b>Buccal</b> (towards the cheek, back teeth) and <b>labial</b> (towards the lips, front teeth)</li>
<li><b>Lingual</b> (towards the tongue, lower teeth) and <b>palatal</b> (towards the palate, upper teeth)</li>
<li><b>Occlusal</b> (biting surface, back teeth) and <b>incisal</b> (biting edge, front teeth)</li>
</ul>
<h2>Landmarks</h2>
<ul><li><b>CEJ:</b> where enamel meets cementum. <b>Apical foramen:</b> where nerves and vessels enter. <b>Furcation:</b> where roots divide.</li></ul>
""",
)

T3 = dict(
    num=3, slug="notation", short="Notation",
    title="Tooth Types, Notation & Eruption",
    dark="#a78bfa", light="#7c3aed",
    blurb="Incisors to molars, FDI two-digit notation, Palmer notation, eruption ages and the mixed dentition.",
    icon='<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 3v18M3 12h18"/>',
    diagram="fdi",
    qs=[
        ("What is the FDI number of the upper right first permanent molar?", ["16", "26", "36", "46"], "Quadrant 1 (upper right), position 6 (first molar) = 16."),
        ("In FDI notation, what is quadrant 3?", ["Permanent lower left", "Permanent upper left", "Permanent lower right", "Permanent upper right"], "1 upper right, 2 upper left, 3 lower left, 4 lower right."),
        ("Which tooth is 11?", ["Upper right central incisor", "Upper left central incisor", "Lower right central incisor", "Upper right first molar"], "Quadrant 1, position 1 (nearest the midline)."),
        ("Which quadrant numbers does FDI use for primary (baby) teeth?", ["5 to 8", "1 to 4", "A to D", "9 to 12"], "5 upper right, 6 upper left, 7 lower left, 8 lower right."),
        ("What is the FDI number of the lower left primary canine?", ["73", "63", "33", "83"], "Quadrant 7 (primary lower left), position 3 (canine)."),
        ("How many teeth are in a full permanent dentition?", ["32", "28", "20", "36"], "8 per quadrant × 4 quadrants, including wisdom teeth."),
        ("How many teeth are in a full primary dentition?", ["20", "24", "32", "16"], "5 per quadrant × 4 quadrants."),
        ("Which permanent tooth has the longest root?", ["Canine", "Central incisor", "First premolar", "Third molar"], "The upper canine has the longest root in the mouth."),
        ("Teeth 18, 28, 38 and 48 are the…", ["Third molars (wisdom teeth)", "First molars", "Second premolars", "Canines"], "Position 8 = third molar."),
        ("At roughly what age do the first primary teeth erupt?", ["Around 6 months", "At birth", "Around 2 years", "Around 3 years"], "Usually the lower central incisors, at about 6 months."),
        ("At roughly what age do the first permanent teeth erupt?", ["Around 6 years", "Around 3 years", "Around 10 years", "Around 13 years"], "First permanent molars and lower incisors arrive at about 6."),
        ("Which primary tooth does the permanent first molar replace?", ["None, it erupts behind the primary teeth", "The primary second molar", "The primary canine", "The primary first molar"], "It's an extra tooth at the back, so parents often mistake it for a baby tooth."),
        ("Permanent premolars replace which primary teeth?", ["Primary molars", "Primary canines", "Primary incisors", "No primary teeth"], "There are no primary premolars; premolars erupt in place of the primary molars."),
        ("Roughly when does a child have a mixed dentition?", ["About 6 to 12 years", "Birth to 3 years", "12 to 18 years", "After 18 years"], "Both primary and permanent teeth are present."),
        ("In Palmer notation, how are primary teeth labelled?", ["Letters A to E", "Numbers 1 to 8", "Numbers 51 to 55", "Roman numerals"], "Palmer uses a grid symbol for the quadrant plus A–E for primary teeth."),
        ("How should you say tooth 16 aloud?", ["One-six", "Sixteen", "First-six", "Sixteenth"], "FDI digits are said separately to avoid confusion."),
        ("A dental chart is drawn as you face the patient. The patient's right side is on…", ["Your left", "Your right", "The top", "The bottom"], "Charts show the patient as you look at them."),
        ("Which tooth is 84?", ["Lower right primary first molar", "Lower left primary first molar", "Lower right first premolar", "Upper right primary first molar"], "Quadrant 8 (primary lower right), position 4 (primary first molar)."),
        ("When do wisdom teeth usually erupt, if they do?", ["17 to 21 years", "6 to 8 years", "10 to 12 years", "After 30 years"], "They are often impacted (blocked) because there isn't room."),
        ("By about what age is the primary dentition complete?", ["2 to 3 years", "1 year", "5 years", "6 years"], "All 20 primary teeth are usually present by 2–3 years."),
        ("Which tooth type is absent from the primary dentition?", ["Premolars", "Canines", "Incisors", "Molars"], "Primary dentition: incisors, canines and molars only."),
        ("How many premolars are in one quadrant of a permanent dentition?", ["2", "1", "3", "0"], "Per quadrant: 2 incisors, 1 canine, 2 premolars, 3 molars."),
    ],
    notes="""
<p class="lead">Adults have 32 permanent teeth and children have 20 primary teeth. UK dental schools use the two-digit FDI system to name each one.</p>
{{DIAGRAM}}
<p>First digit = quadrant (1–4 permanent, 5–8 primary). Second digit = position counted from the midline. Say digits separately: "one-six", not "sixteen".</p>
<p><b>Palmer notation</b> is still seen in UK orthodontics: a grid symbol shows the quadrant, with 1–8 for permanent teeth and A–E for primary teeth.</p>
<h2>Tooth types (per quadrant, permanent)</h2>
<table><tr><th>Type</th><th>Number</th><th>Job</th></tr>
<tr><td>Incisors</td><td>2</td><td>Cutting</td></tr>
<tr><td>Canine</td><td>1</td><td>Tearing; longest root</td></tr>
<tr><td>Premolars</td><td>2</td><td>Crushing; replace primary molars</td></tr>
<tr><td>Molars</td><td>3 (third = wisdom)</td><td>Grinding</td></tr></table>
<h2>Approximate eruption ages</h2>
<table><tr><th></th><th>Primary</th><th>Permanent</th></tr>
<tr><td>First teeth</td><td>Lower central incisors, ~6 months</td><td>First molars and lower incisors, ~6 years</td></tr>
<tr><td>Complete</td><td>All 20 by ~2–3 years</td><td>All but wisdom teeth by ~12–13 years</td></tr>
<tr><td>Wisdom teeth</td><td>—</td><td>17–21 years, often impacted</td></tr></table>
<p>Between about 6 and 12 years a child has a <b>mixed dentition</b>.</p>
""",
)

T4 = dict(
    num=4, slug="caries", short="Caries",
    title="Dental Caries & Fluoride",
    dark="#34d399", light="#059669",
    blurb="Plaque bacteria, the Stephan curve, critical pH, demineralisation and remineralisation, and how fluoride protects.",
    icon='<path d="M3 17l5-8 4 5 3-3 6 6"/><path d="M3 21h18"/>',
    diagram="stephan",
    qs=[
        ("Which bacterium is most associated with starting dental caries?", ["Streptococcus mutans", "Escherichia coli", "Staphylococcus aureus", "Candida albicans"], "S. mutans ferments sugar to acid; lactobacilli join in deeper lesions. Candida is a fungus."),
        ("Below roughly what pH does enamel start to dissolve?", ["5.5", "7.0", "4.5", "6.8"], "The critical pH for enamel (hydroxyapatite) is about 5.5."),
        ("Roughly what is the critical pH of fluorapatite?", ["4.5", "5.5", "6.5", "3.0"], "Fluorapatite resists acid down to about pH 4.5."),
        ("How does the critical pH of root dentine compare with enamel?", ["Higher, about 6.2–6.7, so roots decay more easily", "Lower, about 4", "The same, 5.5", "Root dentine has no critical pH"], "Exposed roots in older adults are vulnerable to decay."),
        ("What does the Stephan curve show?", ["Plaque pH over time after sugar is eaten", "Blood glucose after a meal", "Saliva flow during the day", "Fluoride levels in water"], "pH drops within minutes, then saliva brings it back up."),
        ("After a sugary snack, roughly how long does plaque pH take to recover?", ["30 to 60 minutes", "2 to 3 minutes", "About 6 hours", "About 24 hours"], "Saliva buffers the acid over 30–60 minutes."),
        ("Which matters most for caries risk?", ["How often sugar is eaten", "The total amount of sugar in one sitting", "The temperature of the food", "The colour of the food"], "Each intake is a new acid attack, so frequency is key."),
        ("Which four factors does caries need?", ["Tooth, bacteria, fermentable sugar, time", "Tooth, saliva, fluoride, time", "Bacteria, protein, saliva, heat", "Gum, bone, bacteria, sugar"], "Remove any one and decay stops."),
        ("What is the earliest visible sign of enamel caries?", ["A chalky white spot lesion", "A brown cavity", "A dental abscess", "Black tartar"], "Minerals are lost under an intact surface."),
        ("Can a white spot lesion be reversed?", ["Yes, with fluoride and diet changes", "No, it always needs a filling", "Only by extracting the tooth", "Only in baby teeth"], "Early lesions can remineralise."),
        ("What fluoride concentration of toothpaste is recommended for adults in the UK?", ["1,350–1,500 ppm", "About 100 ppm", "5,000 ppm for everyone", "Fluoride-free"], "5,000 ppm is prescription-only for high-risk patients."),
        ("What is the UK advice straight after brushing?", ["Spit, don't rinse", "Rinse well with water", "Rinse with mouthwash straight away", "Eat something to neutralise"], "Not rinsing leaves fluoride on the teeth."),
        ("When fluorapatite forms, which ions does fluoride replace?", ["Hydroxide ions", "Calcium ions", "Phosphate ions", "Water molecules"], "Ca₁₀(PO₄)₆(OH)₂ + 2F⁻ → Ca₁₀(PO₄)₆F₂ + 2OH⁻."),
        ("Which of these is NOT one of the ways fluoride works?", ["It kills all bacteria in plaque", "It forms fluorapatite", "It speeds up remineralisation", "It inhibits bacterial enzymes"], "Fluoride reduces acid production but does not sterilise plaque."),
        ("Which acid do plaque bacteria mainly produce from sugar?", ["Lactic acid", "Hydrochloric acid", "Citric acid", "Sulfuric acid"], "Bacteria ferment sugar to lactic acid by glycolysis."),
        ("What is the main buffer in saliva?", ["Bicarbonate", "Chloride", "Glucose", "Urea"], "Bicarbonate neutralises plaque acid."),
        ("What do fissure sealants do?", ["Seal the deep grooves of molars to keep plaque out", "Whiten teeth", "Replace lost enamel", "Numb the tooth"], "Sealants are a resin coating on biting surfaces."),
        ("Why does decay spread faster once it reaches dentine?", ["Dentine is less mineralised and has tubules", "Dentine is harder than enamel", "Dentine contains no collagen", "Saliva cannot reach enamel"], "Decay often spreads sideways under the enamel."),
        ("What is the UK's main evidence-based prevention toolkit for dental teams?", ["Delivering Better Oral Health", "Standards for the Dental Team", "The NHS Long Term Plan", "The Dental Charter"], "Published by the Office for Health Improvement and Disparities."),
        ("Which bacteria become important in deeper, established caries lesions?", ["Lactobacilli", "Streptococcus pyogenes", "Salmonella", "Clostridium"], "Lactobacilli thrive in acidic cavities."),
        ("Which fluoride treatment is applied professionally by the dental team?", ["Fluoride varnish", "Amalgam", "Composite resin", "Chlorhexidine gel"], "Varnish is painted on and slowly releases fluoride."),
        ("Which sugar is the most cariogenic?", ["Sucrose", "Xylitol", "Sorbitol", "Aspartame (a sweetener)"], "Sucrose is readily fermented and helps plaque stick to teeth."),
    ],
    notes="""
<p class="lead">Caries happens when plaque bacteria turn sugar into acid faster than saliva can repair the enamel. How often sugar is eaten matters more than how much.</p>
<h2>The four things caries needs</h2>
<ol><li><b>A tooth</b> surface</li><li><b>Plaque bacteria</b>: <i>Streptococcus mutans</i>, then lactobacilli</li><li><b>Fermentable sugar</b>, especially sucrose</li><li><b>Time</b></li></ol>
{{DIAGRAM}}
<h2>How a cavity develops</h2>
{{D:stages}}
<ol><li><b>White spot lesion</b>: chalky, still reversible</li><li><b>Enamel cavity</b>: surface breaks down</li><li><b>Dentine</b>: decay spreads faster along softer dentine</li><li><b>Pulp</b>: pulpitis, pain, infection, abscess</li></ol>
<h2>Critical pH</h2>
<table><tr><th>Tissue</th><th>Starts to dissolve below</th></tr>
<tr><td>Enamel (hydroxyapatite)</td><td>~pH 5.5</td></tr><tr><td>Fluorapatite</td><td>~pH 4.5</td></tr><tr><td>Root dentine</td><td>~pH 6.2–6.7</td></tr></table>
<h2>Fluoride works three ways</h2>
<ol><li>Forms <b>fluorapatite</b>, which resists acid</li><li><b>Speeds remineralisation</b></li><li><b>Inhibits bacterial enzymes</b> (enolase)</li></ol>
<div class="formula">Ca₁₀(PO₄)₆(OH)₂ + 2F⁻ → Ca₁₀(PO₄)₆F₂ + 2OH⁻</div>
<h2>Prevention (UK advice)</h2>
<ul><li>Adult toothpaste 1,350–1,500 ppm fluoride, twice daily; <b>spit, don't rinse</b></li><li>Keep sugar to mealtimes</li><li>Fluoride varnish and fissure sealants</li><li>Main guidance: <i>Delivering Better Oral Health</i></li></ul>
""",
)

T5 = dict(
    num=5, slug="perio", short="Gum Disease",
    title="Periodontal (Gum) Disease",
    dark="#fbbf24", light="#d97706",
    blurb="Gingivitis vs periodontitis, pockets, calculus, the BPE, risk factors and the links with diabetes and heart disease.",
    icon='<path d="M4 10c2-4 14-4 16 0"/><path d="M6 10v6a6 4 0 0 0 12 0v-6"/>',
    qs=[
        ("Which tissue does gingivitis affect?", ["The gum only", "The gum and the bone", "The periodontal ligament only", "The pulp"], "Gingivitis is inflammation of the gingiva only."),
        ("Is gingivitis reversible?", ["Yes, with good plaque control", "No, the damage is permanent", "Only with surgery", "Only with antibiotics"], "Gums return to health once plaque is removed regularly."),
        ("What does periodontitis destroy?", ["The periodontal ligament and alveolar bone", "Only the gum surface", "Only the enamel", "The pulp"], "Lost bone and ligament do not grow back; the disease can only be stabilised."),
        ("What is the normal depth of the healthy gum crevice (sulcus)?", ["1–3 mm", "5–7 mm", "0 mm", "About 10 mm"], "Deeper than this suggests a periodontal pocket."),
        ("What is calculus (tartar)?", ["Plaque that has mineralised", "Trapped food", "Tooth stain from tea", "A fluoride deposit"], "Calcium phosphate from saliva hardens the plaque."),
        ("What does BPE stand for?", ["Basic Periodontal Examination", "Bone Plaque Evaluation", "Bacterial Pocket Estimate", "Basic Plaque Exam"], "A quick gum screening used at UK check-ups."),
        ("A BPE score is recorded for each…", ["Sextant (one-sixth of the mouth)", "Quadrant", "Individual tooth", "Arch"], "The mouth is divided into six sextants."),
        ("What is the range of BPE codes?", ["0 to 4, plus *", "1 to 10", "A to E", "0 to 100"], "* marks a furcation involvement."),
        ("What is the biggest modifiable risk factor for periodontitis?", ["Smoking", "Drinking coffee", "Eating cheese", "Brushing too gently"], "Smoking greatly increases risk and slows healing."),
        ("Which condition has a two-way link with periodontitis?", ["Diabetes", "Asthma", "Migraine", "Eczema"], "Poorly controlled diabetes worsens gum disease, and gum disease worsens blood sugar control."),
        ("What is a common early sign of gingivitis?", ["Gums that bleed on brushing", "Pain on cold drinks", "A chipped tooth", "White patches on enamel"], "Red, swollen gums that bleed are the classic sign."),
        ("Which instrument measures pocket depth?", ["Periodontal probe", "Excavator", "Elevator", "Matrix band"], "A graduated probe is walked around each tooth."),
        ("Why might a smoker's gums bleed less even when disease is present?", ["Nicotine narrows blood vessels, masking the sign", "Smoking cures inflammation", "Smokers brush harder", "Tar seals the gums"], "Less bleeding can hide active disease."),
        ("Can calculus be removed by normal toothbrushing?", ["No, it needs professional scaling", "Yes, with a hard brush", "Yes, with mouthwash", "Yes, with whitening toothpaste"], "Once hardened, calculus must be scaled off."),
        ("Besides diabetes, periodontitis is associated with which condition?", ["Cardiovascular disease", "Short-sightedness", "Hay fever", "Tinnitus"], "Shared inflammation is thought to link them."),
        ("What drives gum disease?", ["Plaque bacteria and the body's inflammatory response", "Acid from sugar dissolving the gum", "Too much fluoride", "Vitamin C excess"], "Much of the damage comes from the host's own inflammation."),
        ("Which treatment cleans root surfaces below the gum line?", ["Root surface debridement (deep scaling)", "Fissure sealing", "Crown preparation", "Tooth whitening"], "It removes plaque and calculus from pockets."),
        ("Calculus forms from minerals that come mainly from…", ["Saliva", "Blood", "Toothpaste", "Food colouring"], "That's why it builds up near salivary duct openings, e.g. behind lower front teeth."),
        ("What is gum recession?", ["The gum margin moving down, exposing the root", "The gum growing over the tooth", "A cavity in the gum", "Swelling of the gum"], "Exposed roots can be sensitive and decay more easily."),
        ("Loose (mobile) teeth in an adult are a sign of…", ["Bone loss from periodontitis", "Healthy gums", "Too much fluoride", "Normal ageing only"], "Loss of supporting bone lets teeth move."),
        ("Which cleaning aid is generally best for cleaning between teeth where there are gaps?", ["Interdental brushes", "Mouthwash", "Chewing gum", "A harder toothbrush"], "Interdental brushes are the usual UK recommendation where they fit."),
        ("Which tissues together make up the periodontium?", ["Gingiva, periodontal ligament, cementum, alveolar bone", "Enamel, dentine, pulp, cementum", "Tongue, lips, cheeks, palate", "Maxilla, mandible, TMJ, hyoid"], "These are the tissues that support the tooth."),
    ],
    notes="""
<p class="lead">Gum disease is driven by plaque bacteria and the body's inflammatory response. Gingivitis is reversible; periodontitis destroys bone and is not.</p>
{{D:perio}}
<h2>The periodontium</h2>
<ul><li><b>Gingiva</b>: gum around the neck of the tooth</li><li><b>Periodontal ligament</b>: collagen fibres from cementum to bone</li><li><b>Cementum</b>: covers the root</li><li><b>Alveolar bone</b>: the socket</li></ul>
<h2>Gingivitis vs periodontitis</h2>
<table><tr><th></th><th>Gingivitis</th><th>Periodontitis</th></tr>
<tr><td>Affects</td><td>Gum only</td><td>Gum, ligament and bone</td></tr>
<tr><td>Signs</td><td>Red, swollen gums that bleed</td><td>Pockets &gt; 3 mm, recession, bone loss, loose teeth</td></tr>
<tr><td>Reversible?</td><td>Yes</td><td>No (can be stabilised)</td></tr>
<tr><td>Risk factors</td><td>Plaque</td><td>Plaque + smoking, diabetes, genetics, stress</td></tr></table>
<h2>Key terms</h2>
<ul><li><b>Pocket</b>: gap deeper than the normal 1–3 mm sulcus</li><li><b>Calculus</b>: mineralised plaque; professional removal only</li><li><b>BPE</b>: score 0–4 (plus *) per sextant at every check-up</li><li><b>Systemic links</b>: diabetes (two-way) and cardiovascular disease</li></ul>
""",
)
