# Year-1 science topics 10–13. Same format as content_a/b: correct answer FIRST.

T10 = dict(
    num=10, slug="materials", short="Materials",
    title="Dental Materials",
    dark="#fb923c", light="#ea580c",
    blurb="Amalgam, composite and glass ionomer; how white fillings bond; impression materials; crowns; the amalgam phase-down.",
    icon='<path d="M4 20h16M6 20V9l6-5 6 5v11"/><path d="M10 20v-5h4v5"/>',
    qs=[
        ("What is dental amalgam?", ["An alloy of mercury with silver, tin and copper", "A tooth-coloured resin with glass filler", "A cement made from glass and polyacrylic acid", "A ceramic fired in a laboratory furnace"], "Amalgam is a mercury alloy; it's strong and long-lasting but not tooth-coloured."),
        ("Since 2018, who should not normally receive amalgam fillings in Great Britain?", ["Under-15s and pregnant or breastfeeding women", "Anyone over 65 or with a heart condition", "Patients who have had a previous amalgam", "Anyone being treated on the NHS"], "Use in these groups is restricted unless the dentist judges it strictly necessary."),
        ("What did countries agree at the 2025 Minamata Convention meeting about amalgam?", ["To end its manufacture, import and export by 2034", "To ban it immediately for all patients worldwide", "To remove all existing amalgam fillings by 2030", "To make it the only NHS filling for back teeth"], "The phase-out keeps a clinical-necessity exemption; existing fillings don't need removing."),
        ("What are the main parts of a composite filling material?", ["Resin matrix, glass filler and a coupling agent", "Mercury, silver, tin and copper powder", "Glass powder and polyacrylic acid liquid", "Zinc oxide powder and eugenol (clove oil)"], "The silane coupling agent bonds the filler particles to the resin."),
        ("How is a composite filling usually set?", ["With a blue curing light (light-activated)", "By drying it with warm air for a minute", "By a slow reaction with saliva overnight", "By heating it to body temperature"], "Blue light (around 470 nm) activates the photo-initiator, usually camphorquinone."),
        ("Why is composite placed and cured in small layers?", ["To reduce stress from polymerisation shrinkage", "Because thick layers are too heavy to stay put", "To make the filling a darker, matching colour", "So saliva can reach and harden each layer"], "Composite shrinks as it sets; thin increments cure fully and pull less on the tooth."),
        ("What is used to etch enamel before bonding composite?", ["About 37% phosphoric acid", "Dilute hydrochloric acid", "Sodium hypochlorite solution", "Hydrogen peroxide gel"], "Etching creates a microscopically rough surface the bonding resin can lock into."),
        ("How does etching help a white filling stay in?", ["It creates micro-pores the resin locks into", "It removes all the dentine under the enamel", "It makes the enamel softer so it can bend", "It releases fluoride into the cavity walls"], "This 'micromechanical' retention is why composites don't need undercut cavities."),
        ("Which material bonds chemically to tooth and releases fluoride?", ["Glass ionomer cement (GIC)", "Dental amalgam", "Light-cured composite", "Zirconia ceramic"], "GIC sets by an acid–base reaction and releases fluoride, useful in children and root caries."),
        ("How does glass ionomer cement set?", ["An acid–base reaction between glass and polyacid", "Light-activated free-radical polymerisation", "Mercury dissolving silver–tin particles", "Crystallisation as it cools from a melt"], "Calcium and aluminium ions from the glass cross-link the polyacrylic acid chains."),
        ("What is a main drawback of glass ionomer compared with composite?", ["It is weaker and wears faster", "It contains mercury", "It needs a curing light", "It cannot be tooth-coloured"], "That's why it's often used where strength matters less, or as a base or temporary filling."),
        ("Alginate is an example of which kind of impression material?", ["Irreversible hydrocolloid", "Elastomeric silicone", "Thermoplastic compound", "Zinc oxide–eugenol paste"], "Alginate is cheap and quick, used for study models; it tears and distorts if not cast promptly."),
        ("Why are silicone (elastomer) impressions used for crowns?", ["They are accurate and dimensionally stable", "They are the cheapest material available", "They set without being mixed at all", "They dissolve in water after use"], "Crowns need a precise fit, so accuracy and stability matter more than cost."),
        ("What are dental models (casts) usually poured in?", ["Gypsum (dental stone or plaster)", "Glass ionomer cement", "Composite resin", "Alginate"], "Gypsum products are calcium sulfate hemihydrate that sets back to the dihydrate."),
        ("What is zirconia used for in dentistry?", ["Strong, tooth-coloured crowns and bridges", "Temporary fillings in baby teeth", "Taking impressions of the teeth", "Etching enamel before bonding"], "Zirconia is a very strong ceramic, useful for back teeth and bridges."),
        ("What does PFM stand for in crown and bridge work?", ["Porcelain fused to metal", "Polymer filled with minerals", "Pre-formed metal", "Polished fibre matrix"], "A metal substructure with porcelain baked on for appearance."),
        ("Why do many dentists still use amalgam for some back-tooth fillings?", ["It is durable and less technique-sensitive", "It is tooth-coloured and bonds to enamel", "It releases large amounts of fluoride", "It is the only material allowed on the NHS"], "Amalgam tolerates moisture better than composite, which needs a dry field to bond."),
        ("What does 'technique-sensitive' mean for composite?", ["Results depend on careful handling, e.g. keeping it dry", "It only works on teeth with no previous fillings", "Only a specialist is allowed to place it", "It reacts badly to the patient's saliva type"], "Moisture contamination during bonding is a common cause of failure."),
        ("What is a 'base' or 'lining' placed under a filling for?", ["To protect the pulp in a deep cavity", "To make the filling a whiter colour", "To glue the filling to the gum", "To speed up the curing light"], "Calcium hydroxide or GIC linings protect the pulp and can encourage dentine repair."),
        ("Which property describes a material that conducts heat poorly?", ["Low thermal conductivity", "High compressive strength", "High elastic modulus", "Low water solubility"], "Metal fillings conduct heat well, which is why deep amalgams can feel sensitive to cold."),
        ("What is 'microleakage' at a filling margin?", ["Fluid and bacteria seeping into a tiny gap", "Saliva dripping out of the patient's mouth", "Mercury vapour escaping from the filling", "The filling slowly dissolving in water"], "It can cause staining, sensitivity and decay under the filling (secondary caries)."),
        ("Which crown material looks most natural but is less strong than zirconia?", ["Feldspathic porcelain", "Cast gold alloy", "Stainless steel", "Cobalt–chromium"], "Gold is strong but not tooth-coloured; stainless steel crowns are used in children's back teeth."),
    ],
    notes="""
<p class="lead">You'll handle these materials from your first phantom-head sessions. Know what each is made of, how it sets and when it's chosen.</p>
<h2>The three main filling materials</h2>
<table><tr><th></th><th>Amalgam</th><th>Composite</th><th>Glass ionomer (GIC)</th></tr>
<tr><td>Made of</td><td>Mercury alloyed with silver, tin, copper</td><td>Resin matrix + glass filler + silane coupling agent</td><td>Fluoro-alumino-silicate glass + polyacrylic acid</td></tr>
<tr><td>Sets by</td><td>Amalgamation (metallic reaction)</td><td>Blue-light polymerisation</td><td>Acid–base reaction</td></tr>
<tr><td>Sticks by</td><td>Shape of the cavity (undercuts)</td><td>Etch and bond (micromechanical)</td><td>Chemical bond to tooth</td></tr>
<tr><td>Strengths</td><td>Durable, tolerates moisture</td><td>Tooth-coloured, conserves tooth</td><td>Releases fluoride</td></tr>
<tr><td>Weaknesses</td><td>Not tooth-coloured; mercury phase-down</td><td>Shrinks on setting; technique-sensitive</td><td>Weaker, wears faster</td></tr></table>
{{D:bonding}}
<h2>Amalgam: the rules now</h2>
<ul><li><b>Great Britain:</b> since 2018 not normally used for baby teeth, under-15s, or pregnant or breastfeeding women, unless strictly necessary. Not banned.</li>
<li><b>EU:</b> banned for most uses from 1 January 2025. <b>Northern Ireland</b> has a derogation to 2034.</li>
<li><b>Worldwide:</b> in November 2025 the Minamata Convention agreed to end manufacture, import and export by 2034.</li></ul>
<h2>Impressions and models</h2>
<ul><li><b>Alginate</b> (irreversible hydrocolloid): quick and cheap, for study models; pour promptly.</li><li><b>Silicones / elastomers</b>: accurate and stable, for crowns and bridges.</li><li><b>Gypsum</b> (plaster, dental stone): poured into impressions to make models.</li></ul>
<h2>Crowns</h2>
<ul><li><b>Zirconia</b>: very strong, tooth-coloured. <b>Porcelain / glass ceramics</b>: most natural-looking. <b>PFM</b>: porcelain fused to metal. <b>Gold</b>: strong, kind to opposing teeth. <b>Stainless steel</b>: preformed crowns for children's back teeth.</li></ul>
""",
)

T11 = dict(
    num=11, slug="anaesthesia", short="Local Anaesthesia",
    title="Local Anaesthesia & Pharmacology",
    dark="#c084fc", light="#9333ea",
    blurb="How local anaesthetics work and why they fail in infection; common agents; antibiotics, painkillers and medicines that change dental care.",
    icon='<path d="M18 2l4 4M17 7l3-3M5 19l-3 3M14 4l6 6-9 9-6-6z"/><path d="M8 13l3 3"/>',
    qs=[
        ("How do local anaesthetics stop pain signals?", ["They block voltage-gated sodium channels in nerves", "They block pain receptors in the brain", "They destroy the nerve endings in the tooth", "They stop blood flowing to the nerve"], "No sodium influx means no action potential, so no signal reaches the brain."),
        ("Which form of a local anaesthetic crosses the nerve membrane?", ["The uncharged (unionised) base form", "The positively charged (ionised) form", "Only the form bound to adrenaline", "Both forms cross equally well"], "Lipid-soluble base crosses; once inside, the ionised form blocks the channel."),
        ("Why do local anaesthetics work poorly in infected, inflamed tissue?", ["Low pH there keeps more drug ionised, so less crosses", "Infection breaks the drug down within seconds", "Pus blocks the needle from going in", "Bacteria produce their own anaesthetic"], "Acidic tissue shifts the equilibrium toward the charged form."),
        ("Which local anaesthetic is the UK's standard dental choice, with adrenaline?", ["Lidocaine 2% with 1:80,000 adrenaline", "Benzocaine 20% gel with adrenaline", "Procaine 1% with felypressin", "Bupivacaine 5% with no additive"], "Lidocaine with adrenaline is the classic UK dental cartridge."),
        ("Articaine is commonly supplied at what strength?", ["4% with adrenaline", "2% with felypressin", "20% as a gel", "0.5% plain"], "Articaine 4% with 1:100,000 or 1:200,000 adrenaline is widely used."),
        ("Which vasoconstrictor is used with prilocaine?", ["Felypressin", "Adrenaline", "Noradrenaline", "Atropine"], "Felypressin is an alternative where adrenaline is best avoided."),
        ("Lidocaine, articaine and prilocaine all belong to which group?", ["Amides", "Esters", "Opioids", "Steroids"], "Amides are metabolised mainly in the liver; most dental injectables are amides."),
        ("Benzocaine, used as topical gel before injections, is an…", ["Ester local anaesthetic", "Amide local anaesthetic", "Opioid painkiller", "Antibiotic"], "Esters are broken down by plasma esterases and are more likely to cause allergy."),
        ("Why do you aspirate before injecting local anaesthetic?", ["To check the needle tip is not in a blood vessel", "To remove saliva from the injection site", "To check the anaesthetic has not expired", "To make the injection less painful"], "Intravascular injection raises the risk of toxicity and adrenaline effects."),
        ("Which painkiller combination is often recommended for dental pain?", ["Ibuprofen and paracetamol together", "Aspirin and codeine together", "Paracetamol and morphine together", "Antibiotics and ibuprofen together"], "Taken correctly, ibuprofen plus paracetamol is effective for most dental pain."),
        ("Do antibiotics cure most toothache?", ["No; dental treatment removes the cause", "Yes; most toothache is a bacterial infection", "Yes, if taken for at least a fortnight", "Only if given by injection, not by mouth"], "Antibiotics are for spreading infection or systemic signs, alongside treatment."),
        ("Which antibiotic is first-line for many dental infections in the UK?", ["Amoxicillin (or phenoxymethylpenicillin)", "Vancomycin", "Ciprofloxacin", "Gentamicin"], "Metronidazole is an alternative; clarithromycin may be used in penicillin allergy."),
        ("A patient on warfarin needs an extraction. What should be checked first?", ["Their INR (blood clotting test)", "Their blood glucose level", "Their blood pressure only", "Their cholesterol level"], "Warfarin raises bleeding risk; the INR shows how anticoagulated they are."),
        ("Which drug group can cause medication-related osteonecrosis of the jaw (MRONJ)?", ["Bisphosphonates and similar bone drugs", "Statins for cholesterol", "Antihistamines for hay fever", "Inhaled steroids for asthma"], "Extractions in these patients need careful planning."),
        ("Which antibiotic interacts with alcohol, so patients must avoid drinking?", ["Metronidazole", "Amoxicillin", "Phenoxymethylpenicillin", "Clindamycin"], "It can cause flushing, nausea and vomiting with alcohol."),
        ("Which group should avoid ibuprofen or use it only with advice?", ["People with some asthma, ulcers or kidney disease", "Everyone under the age of 30", "People who are allergic to latex", "People with good kidney function"], "NSAIDs can worsen these conditions."),
        ("What is 'antibiotic stewardship'?", ["Prescribing only when needed, to limit resistance", "Always prescribing the strongest antibiotic first", "Giving antibiotics before every dental extraction", "Storing antibiotics in a locked cupboard"], "Dentistry is a significant source of antibiotic prescriptions in primary care."),
        ("Which block numbs most lower teeth on one side?", ["Inferior alveolar nerve block", "Infraorbital nerve block", "Greater palatine block", "Posterior superior alveolar block"], "The lingual nerve is usually caught too, numbing the tongue on that side."),
        ("Why is adrenaline added to local anaesthetic?", ["It narrows vessels, so the effect lasts longer", "It raises blood pressure to stop fainting", "It neutralises the acidic anaesthetic", "It kills bacteria around the injection site"], "Vasoconstriction slows removal of the drug and reduces bleeding."),
        ("What should be done before giving any medicine to a patient?", ["Take a full, up-to-date medical history", "Check their dental charting first", "Ask whether they have dental insurance", "Confirm their next recall date"], "Medical history picks up allergies, interactions and conditions that change care."),
        ("A patient has a severe penicillin allergy. Which is a suitable alternative for a dental infection?", ["Clarithromycin or metronidazole", "Amoxicillin at a lower dose", "Co-amoxiclav", "Phenoxymethylpenicillin"], "Amoxicillin, co-amoxiclav and phenoxymethylpenicillin are all penicillins."),
        ("What is the maximum safe dose of local anaesthetic based on?", ["The patient's body weight", "The patient's height", "The number of teeth treated", "The length of the appointment"], "Doses are calculated in mg per kg, so children need particular care."),
    ],
    notes="""
<p class="lead">Local anaesthetics block sodium channels in nerves. Almost every dental procedure you learn depends on giving them safely, so understand both the chemistry and the cautions.</p>
<h2>How local anaesthetics work</h2>
<ol><li>The drug is a weak base. Its uncharged form crosses the lipid nerve membrane.</li><li>Inside, it picks up H⁺ and the charged form blocks voltage-gated Na⁺ channels.</li><li>No action potential, so no pain signal.</li></ol>
{{D:laph}}
<h2>Common dental agents</h2>
<table><tr><th>Drug</th><th>Group</th><th>Usual form</th></tr>
<tr><td>Lidocaine</td><td>Amide</td><td>2% with 1:80,000 adrenaline</td></tr>
<tr><td>Articaine</td><td>Amide (with an ester side group)</td><td>4% with adrenaline</td></tr>
<tr><td>Prilocaine</td><td>Amide</td><td>3% with felypressin</td></tr>
<tr><td>Mepivacaine</td><td>Amide</td><td>3% plain</td></tr>
<tr><td>Benzocaine</td><td>Ester</td><td>Topical gel before injections</td></tr></table>
<ul><li><b>Vasoconstrictors</b> (adrenaline, felypressin) make the anaesthetic last longer and reduce bleeding.</li><li><b>Aspirate</b> before injecting to avoid a blood vessel.</li><li><b>Maximum doses</b> are per kg of body weight. Learn the official figures on your course.</li></ul>
<h2>Other medicines you'll meet</h2>
<ul><li><b>Painkillers:</b> ibuprofen plus paracetamol is effective for most dental pain. Take care with NSAIDs in some asthma, stomach ulcers and kidney disease.</li>
<li><b>Antibiotics:</b> only for spreading infection or systemic signs, always with treatment of the cause. Amoxicillin or penicillin V first-line; metronidazole (no alcohol); clarithromycin in penicillin allergy.</li>
<li><b>Anticoagulants:</b> warfarin (check INR) and newer DOACs raise bleeding risk after extractions.</li>
<li><b>Bisphosphonates</b> and similar bone drugs: risk of medication-related osteonecrosis of the jaw (MRONJ) after extractions.</li></ul>
<p>Always take an up-to-date medical history before treatment.</p>
""",
)

T12 = dict(
    num=12, slug="pathology", short="Oral Pathology",
    title="Oral Pathology & Oral Cancer",
    dark="#f87171", light="#b91c1c",
    blurb="Ulcers, infections and white and red patches; oral cancer risk factors and warning signs; when a dentist must refer urgently.",
    icon='<circle cx="12" cy="12" r="9"/><path d="M12 7v6M12 16v.5"/>',
    qs=[
        ("What is the most common type of oral cancer?", ["Squamous cell carcinoma", "Basal cell carcinoma", "Malignant melanoma", "Lymphoma"], "Around 9 in 10 oral cancers are squamous cell carcinomas."),
        ("Which two risk factors multiply each other's effect on oral cancer?", ["Tobacco and alcohol", "Sugar and fizzy drinks", "Coffee and tea", "Fluoride and mouthwash"], "The combination raises risk far more than either alone."),
        ("Which chewing habit, common in some South Asian communities, raises oral cancer risk?", ["Betel quid or paan with areca nut", "Chewing sugar-free gum daily", "Chewing fennel seeds after meals", "Chewing mint leaves"], "Areca nut is a carcinogen, with or without tobacco."),
        ("Which virus is linked to cancers at the back of the mouth and throat (oropharynx)?", ["Human papillomavirus (HPV)", "Herpes simplex virus", "Varicella zoster virus", "Epstein–Barr virus only"], "HPV-related oropharyngeal cancers have been rising; HPV vaccination helps."),
        ("Which sites in the mouth are most common for oral cancer?", ["Side of the tongue and floor of the mouth", "The hard palate and the gums", "The inside of the upper lip", "The tip of the tongue"], "These sites must be checked at every examination."),
        ("A mouth ulcer has not healed after how long before it should raise concern?", ["More than 3 weeks", "More than 3 days", "More than 1 week", "More than 3 months"], "Unexplained ulceration over 3 weeks needs urgent assessment for possible cancer."),
        ("Which patch carries the higher risk of becoming cancer?", ["A red patch (erythroplakia)", "A white patch (leukoplakia)", "A brown freckle on the lip", "A yellow spot on the cheek"], "Erythroplakia is less common than leukoplakia but more often dysplastic or malignant."),
        ("What is leukoplakia?", ["A white patch that can't be wiped off or explained", "A white coating that wipes off easily", "A normal white line along the cheek", "A white ulcer caused by a sharp tooth"], "It's a potentially malignant disorder that needs monitoring or biopsy."),
        ("A white coating that wipes off, leaving a red surface, is most likely…", ["Candida (thrush)", "Leukoplakia", "Lichen planus", "Squamous cell carcinoma"], "Common in denture wearers, after antibiotics, with inhaled steroids or when immunity is low."),
        ("Inflammation under a denture, often due to Candida, is called…", ["Denture stomatitis", "Denture gingivitis", "Denture periodontitis", "Denture pulpitis"], "Good denture hygiene and leaving dentures out at night help."),
        ("What causes cold sores?", ["Herpes simplex virus", "Candida albicans", "Streptococcus mutans", "Human papillomavirus"], "The virus lies dormant in the trigeminal ganglion and can reactivate."),
        ("What is primary herpetic gingivostomatitis?", ["A first herpes infection with sore gums and ulcers", "A gum disease caused by poor brushing", "A reaction to a new toothpaste", "A fungal infection under dentures"], "Usually in young children, with fever and widespread painful ulcers."),
        ("What are recurrent aphthous ulcers?", ["Common recurring mouth ulcers with no single cause", "Ulcers caused only by the herpes virus", "Cancerous ulcers that keep coming back", "Ulcers that only occur under dentures"], "Minor aphthae heal in 1–2 weeks; triggers include stress, trauma and deficiencies."),
        ("Lacy white lines on the inside of both cheeks suggest…", ["Oral lichen planus", "Candida (thrush)", "Leukoplakia", "Herpes simplex"], "An immune-mediated condition; some forms need monitoring."),
        ("Who should check the whole mouth for signs of cancer at check-ups?", ["The dentist, at every examination", "Only a hospital specialist", "Only the patient's GP", "Only the dental hygienist"], "A soft-tissue check is part of every routine dental examination."),
        ("If a dentist suspects oral cancer, how should they refer?", ["Urgently, on the suspected cancer pathway", "Routinely, at the next six-month check-up", "By asking the patient to see their GP someday", "Only if the patient asks for a referral"], "Patients should be seen within 2 weeks."),
        ("Which is a warning sign for oral cancer?", ["An unexplained lump in the mouth or neck", "Gums that bleed slightly when flossing", "A chipped front tooth", "Sensitivity to cold drinks"], "Others include persistent ulcers, red or red-white patches and numbness."),
        ("What is a biopsy?", ["Removing a small piece of tissue to examine", "Taking an X-ray of a suspicious area", "Swabbing the mouth to grow bacteria", "Photographing a lesion for the notes"], "Histology confirms the diagnosis."),
        ("What does 'potentially malignant disorder' mean?", ["A condition with an increased risk of cancer", "A cancer that has already spread", "A harmless condition with no cancer risk", "An infection that can be cured with antibiotics"], "Examples include leukoplakia, erythroplakia and some lichen planus."),
        ("A traumatic ulcer next to a sharp broken tooth should…", ["Heal within about 2 weeks once the cause is fixed", "Never heal, even after the tooth is smoothed", "Be treated with antibiotics straight away", "Always be referred on the cancer pathway"], "If it doesn't heal once the cause is removed, it needs urgent review."),
        ("Which advice reduces oral cancer risk?", ["Stop smoking and keep alcohol within guidelines", "Use whitening toothpaste twice a day", "Have more frequent scale and polishes", "Avoid fluoride toothpaste"], "Dental teams give smoking cessation and alcohol advice."),
        ("Why does early detection of oral cancer matter?", ["Survival is much better when it is caught early", "Early cancers can always be cured with mouthwash", "Late cancers are easier to remove surgically", "It only matters for patients over 80"], "Many oral cancers are found late, when treatment is harder."),
    ],
    notes="""
<p class="lead">Dentists see the mouth more often than any other clinician, so they're often first to spot oral cancer. Know the common harmless conditions and the red flags.</p>
<h2>Common conditions</h2>
<table><tr><th>Condition</th><th>Cause</th><th>Key features</th></tr>
<tr><td>Aphthous ulcers</td><td>Unknown; triggers include stress, trauma, deficiencies</td><td>Recurrent, painful; minor ones heal in 1–2 weeks</td></tr>
<tr><td>Cold sores / herpetic gingivostomatitis</td><td>Herpes simplex virus</td><td>Lip blisters; first infection in children causes fever and widespread ulcers</td></tr>
<tr><td>Candida (thrush), denture stomatitis</td><td>Candida albicans (fungus)</td><td>White coating that wipes off; redness under dentures</td></tr>
<tr><td>Lichen planus</td><td>Immune-mediated</td><td>Lacy white lines, often both cheeks</td></tr>
<tr><td>Traumatic ulcer</td><td>Sharp tooth, denture, bite</td><td>Heals in about 2 weeks once the cause is removed</td></tr></table>
<h2>Oral cancer</h2>
<ul><li>About 9 in 10 are <b>squamous cell carcinomas</b>.</li>
<li><b>Risk factors:</b> tobacco and alcohol (worse together), betel quid / paan / areca nut, HPV (oropharynx), age, poor diet.</li>
<li><b>Common sites:</b> side of the tongue, floor of the mouth.</li>
<li><b>Potentially malignant disorders:</b> leukoplakia (white patch), erythroplakia (red patch, higher risk), some lichen planus.</li></ul>
{{D:referral}}
<p>Referral criteria follow <a href="https://gpnotebook.com/en-GB/pages/ear-nose-and-throat/urgent-referral-for-suspected-oral-cancer" target="_blank" rel="noopener">NICE NG12</a> (suspected cancer recognition and referral).</p>
""",
)

T13 = dict(
    num=13, slug="radiography", short="Radiography",
    title="Dental Radiography",
    dark="#94a3b8", light="#475569",
    blurb="Bitewings, periapicals, OPGs and CBCT; reading radiolucent vs radiopaque; IR(ME)R roles, justification and keeping doses low.",
    icon='<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M7 15l3-4 3 3 2-2 3 3"/>',
    qs=[
        ("Which radiograph is best for spotting decay between back teeth?", ["Bitewing", "Periapical", "Occlusal", "Lateral cephalogram"], "Bitewings show the crowns of upper and lower back teeth together, plus bone levels."),
        ("Which radiograph shows a whole tooth including the root tip?", ["Periapical", "Bitewing", "Lateral cephalogram", "Hand–wrist film"], "Used for abscesses, root canal treatment and root problems."),
        ("What does an OPG (or DPT) show?", ["Both jaws and all the teeth in one panoramic image", "A single tooth in very fine detail", "A 3D image of the jaw in slices", "Only the front teeth from above"], "Useful for wisdom teeth, jaw fractures and an overview of the dentition."),
        ("What is CBCT?", ["Cone-beam CT, a 3D scan of the teeth and jaws", "A coloured bitewing used in children", "A camera that photographs the cheek", "A computer that checks bitewings for decay"], "Higher dose than plain films, so used only when 3D information is needed."),
        ("On a radiograph, what does 'radiolucent' mean?", ["Dark: X-rays pass through easily", "White: X-rays are blocked", "Coloured: the area is infected", "Blurred: the patient moved"], "Decay, the pulp and air spaces look dark."),
        ("Which appears most radiopaque (white) on a radiograph?", ["An amalgam filling", "The pulp chamber", "A cavity in dentine", "The soft gum tissue"], "Metals block X-rays almost completely."),
        ("How does tooth decay usually look on a bitewing?", ["A dark (radiolucent) area in the tooth", "A bright white spot on the enamel", "A thin white line around the root", "It cannot be seen on X-rays at all"], "Mineral loss lets more X-rays through."),
        ("Which regulations govern patient X-ray exposures in the UK?", ["IR(ME)R", "COSHH", "RIDDOR", "HTM 01-05"], "The Ionising Radiation (Medical Exposure) Regulations."),
        ("Under IR(ME)R, who justifies each X-ray exposure?", ["The practitioner", "The receptionist", "The patient", "The equipment supplier"], "Roles include referrer, practitioner (justifies) and operator (carries it out)."),
        ("What does 'justification' mean for an X-ray?", ["The benefit to the patient outweighs the risk", "The X-ray machine has been serviced", "The patient has paid for the X-ray", "The image has been saved to the notes"], "No exposure without a clinical reason."),
        ("What does 'optimisation' mean in radiation protection?", ["Keeping each dose as low as reasonably practicable", "Taking more X-rays to get the best one", "Using the highest setting for the clearest image", "Repeating X-rays every six months"], "This is the ALARP principle."),
        ("If you double the distance from an X-ray source, the dose falls to…", ["A quarter", "A half", "A third", "An eighth"], "The inverse square law: dose ∝ 1/distance²."),
        ("Why do many dental X-ray machines use rectangular collimation?", ["It reduces the area exposed and so the dose", "It makes the image larger and sharper", "It lets the X-rays pass through metal", "It means the patient doesn't need to keep still"], "The beam is shaped to the size of the sensor."),
        ("Can a pregnant patient have a dental X-ray?", ["Yes, if justified; the beam isn't aimed at the abdomen", "No, never during pregnancy", "Only in the last three months", "Only if she wears two lead aprons"], "The dose from a dental film to the abdomen is negligible."),
        ("Roughly how does the dose of a bitewing compare with natural background radiation?", ["About the same as a day or so of background", "About the same as a year of background", "About the same as a chest CT scan", "Ten times more than a chest CT scan"], "Dental films are very low dose, but every exposure still needs justifying."),
        ("What is the 'controlled area' around a dental X-ray set?", ["The zone where staff must not be during exposure", "The waiting room for patients having X-rays", "The cupboard where films are stored", "The area where images are reported"], "Staff stand outside it, usually at least 1.5–2 m away and out of the beam."),
        ("Which radiograph helps plan orthodontic treatment by showing the skull from the side?", ["Lateral cephalogram", "Bitewing", "Periapical", "Occlusal"], "Used to measure jaw and tooth relationships."),
        ("What should happen to every X-ray image taken?", ["It should be reported and recorded in the notes", "It should be deleted after the appointment", "It should be given to the patient to keep", "It should be sent to the GDC"], "A clinical evaluation (report) is a legal requirement under IR(ME)R."),
        ("Why are digital sensors popular in dental radiography?", ["Lower dose and instant images", "They show colour images of decay", "They don't need a power supply", "They work without any X-rays"], "Digital imaging also avoids chemical processing."),
        ("What does a dark area at the tip of a root on a periapical often suggest?", ["Infection that has spread from a dead pulp", "A healthy, normal tooth", "A brand-new filling", "Extra-strong bone"], "A periapical radiolucency is a sign of apical periodontitis."),
        ("On a bitewing, what can be seen besides decay?", ["Bone levels around the teeth", "The patient's sinuses in 3D", "The whole of both jaws", "The nerve in the tongue"], "Useful for monitoring periodontal bone loss."),
        ("Who is the 'referrer' under IR(ME)R?", ["The clinician who requests the X-ray", "The person who presses the exposure button", "The patient who agrees to the X-ray", "The engineer who services the machine"], "In a dental practice, one dentist may act as referrer, practitioner and operator."),
    ],
    notes="""
<p class="lead">X-rays let you see decay between teeth, root problems and bone loss. Every exposure is ionising radiation, so it must be justified and kept as low as reasonably practicable.</p>
<h2>Types of dental radiograph</h2>
<table><tr><th>View</th><th>Shows</th><th>Used for</th></tr>
<tr><td>Bitewing</td><td>Crowns of upper and lower back teeth; bone levels</td><td>Decay between teeth; gum disease monitoring</td></tr>
<tr><td>Periapical</td><td>Whole tooth to the root tip</td><td>Abscesses, root canal treatment, trauma</td></tr>
<tr><td>Occlusal</td><td>A section of the arch from above or below</td><td>Unerupted teeth, salivary stones</td></tr>
<tr><td>OPG / DPT (panoramic)</td><td>Both jaws, all teeth</td><td>Wisdom teeth, fractures, overview</td></tr>
<tr><td>Lateral cephalogram</td><td>Skull from the side</td><td>Orthodontic planning</td></tr>
<tr><td>CBCT</td><td>3D slices of teeth and jaws</td><td>Implants, complex roots (higher dose)</td></tr></table>
{{D:radio}}
<h2>Radiation protection</h2>
<ul><li><b>IR(ME)R</b> roles: <b>referrer</b> requests, <b>practitioner</b> justifies, <b>operator</b> takes the image. One dentist can be all three.</li>
<li><b>Justification:</b> benefit must outweigh risk. <b>Optimisation:</b> keep dose as low as reasonably practicable (ALARP).</li>
<li><b>Inverse square law:</b> double the distance, quarter the dose.</li>
<li>Rectangular collimation and digital sensors reduce dose.</li>
<li>Pregnancy isn't a bar to a justified dental X-ray.</li>
<li>Every image must be <b>reported</b> (clinically evaluated) and recorded.</li></ul>
""",
)
