"""Original Verbal Reasoning passages. Answer ONLY from the passage (UCAT rule).
Each passage: (title, html, [(question, options, answer_index, explanation), ...])"""

TF = ["True", "False", "Can't tell"]

VR = [
("Anaesthesia's dental origins", """
<p>Before the 1840s, surgery was performed on conscious patients, and speed was the surgeon's most prized skill. The first steps towards pain-free surgery came not from a hospital but from dentistry. In 1844 Horace Wells, a dentist in Connecticut, noticed that a man injured while under the influence of nitrous oxide, then popular as an entertainment known as 'laughing gas', seemed to feel no pain. Wells had one of his own teeth removed under the gas the next day and reported feeling nothing.</p>
<p>Wells's public demonstration in Boston the following year went badly: the patient cried out, and the audience declared the method a fraud. The patient later said he had felt little, but the damage to Wells's reputation was done. In October 1846, William Morton, a former associate of Wells, used ether during an operation at Massachusetts General Hospital. This demonstration was judged a success, and news of it spread to Europe within months.</p>
<p>The question of who deserved credit led to bitter disputes. Several men, including Wells and Morton, claimed priority, and none of them profited greatly from the discovery.</p>""",
[
 ("Horace Wells tested nitrous oxide on himself before demonstrating it publicly.", TF, 0, "The passage says Wells had his own tooth removed under the gas before the Boston demonstration."),
 ("Wells's patient in Boston felt no pain at all.", TF, 1, "The patient 'later said he had felt little', not nothing, and he cried out during the procedure."),
 ("Morton's ether demonstration took place before Wells's Boston demonstration.", TF, 1, "Wells demonstrated 'the following year' after 1844, i.e. 1845; Morton's was October 1846."),
 ("Which statement is best supported by the passage?", ["Morton was trained as a dentist by Wells.", "Nitrous oxide was first used medically in a hospital.", "Several people disputed who should be credited with the discovery.", "Ether was abandoned soon after 1846."], 2, "The final paragraph describes bitter disputes over priority. The passage says Morton was a former associate, not that Wells trained him."),
]),

("Urban trees and summer heat", """
<p>Cities are often several degrees warmer than the surrounding countryside, an effect known as the urban heat island. Dark surfaces such as roads and roofs absorb sunlight during the day and release heat at night, while buildings trap warm air and reduce wind. Trees counter this in two ways: their canopies shade the ground, and water evaporating from their leaves cools the surrounding air.</p>
<p>A study of one European city found that streets with dense tree cover were up to 4°C cooler at street level on hot afternoons than nearby streets without trees. The researchers cautioned, however, that the cooling effect was much smaller at night, and that narrow streets lined with large trees could trap vehicle pollution beneath the canopy.</p>
<p>Planting trees is not always straightforward. Underground cables and pipes limit where roots can grow, and young trees need regular watering for several years. Some councils have found that a large share of newly planted street trees die within five years when maintenance budgets are cut.</p>""",
[
 ("Trees cool cities only by providing shade.", TF, 1, "The passage gives two ways: shade and evaporation from leaves."),
 ("The study found tree-lined streets were cooler at night by up to 4°C.", TF, 1, "The 4°C figure applied to hot afternoons; the night-time effect was 'much smaller'."),
 ("Most newly planted street trees in the UK die within five years.", TF, 2, "The passage mentions 'some councils' finding a large share die when budgets are cut; it gives no UK-wide figure."),
 ("Which is given as a possible drawback of large street trees?", ["They make streets warmer at night.", "They can trap traffic pollution in narrow streets.", "They damage roads by absorbing sunlight.", "They increase wind speed between buildings."], 1, "The researchers cautioned that narrow streets with large trees could trap vehicle pollution."),
]),

("The Broad Street pump", """
<p>In the summer of 1854 a severe outbreak of cholera struck the Soho district of London, killing hundreds of people within a few weeks. At the time, most doctors believed diseases like cholera spread through 'miasma', a poisonous vapour rising from rotting matter.</p>
<p>John Snow, a London physician, doubted this theory. By mapping the homes of people who had died, he showed that deaths clustered around a water pump on Broad Street. Some of his most persuasive evidence came from exceptions: workers at a nearby brewery, who drank beer supplied by their employer rather than pump water, largely escaped the disease, while a woman who lived some distance away died after having water from the Broad Street pump brought to her house because she preferred its taste.</p>
<p>Snow persuaded the local authorities to remove the pump's handle. The outbreak was already declining by then, so the removal itself may have had limited effect. Nevertheless, his investigation is often described as a founding moment of epidemiology, although the miasma theory was not abandoned for some years.</p>""",
[
 ("Snow's map showed that deaths were concentrated around the Broad Street pump.", TF, 0, "He showed that deaths clustered around the pump."),
 ("Removing the pump handle ended the outbreak.", TF, 2, "The outbreak was already declining, so the removal 'may have had limited effect'. The passage doesn't say what ended it."),
 ("The brewery workers avoided cholera because beer kills the cholera bacterium.", TF, 2, "The passage says they drank beer instead of pump water; it says nothing about beer killing bacteria."),
 ("Why was the woman who lived some distance away important evidence?", ["She had been exposed to miasma near Broad Street.", "She died despite living away from Soho, after drinking the pump's water.", "She was the first person to die in the outbreak.", "She worked at the brewery but drank pump water."], 1, "Her death far from the cluster, linked to water fetched from the pump, supported Snow's idea."),
]),

("A shorter working week", """
<p>A software company with 120 staff recently trialled a four-day week for six months, with no reduction in pay. Staff were expected to complete the same work in 32 hours instead of 40. Managers reported that output, measured by projects completed on time, stayed roughly level, while sick days fell by about a third compared with the same period the previous year.</p>
<p>Not everyone benefited equally. Customer-support staff, who had to cover the phones five days a week, worked on a rota that some felt was less predictable than before. A minority of employees said the compressed schedule made their working days more intense and stressful.</p>
<p>At the end of the trial, the company chose to keep the four-day week for most teams. Its chief executive acknowledged that the trial had not been designed as a controlled experiment and that other changes during the year, such as new project-management software, may also have affected the results.</p>""",
[
 ("Staff pay was reduced by a fifth during the trial.", TF, 1, "The trial ran 'with no reduction in pay'."),
 ("Sick days fell by about a third compared with the previous year.", TF, 0, "Stated directly in the first paragraph."),
 ("All teams moved permanently to a four-day week after the trial.", TF, 1, "The company kept it for 'most teams', not all."),
 ("Which of the following does the chief executive accept?", ["The four-day week reduced output.", "Other factors may have influenced the results.", "Customer-support staff preferred the new rota.", "The trial proved that shorter weeks reduce stress."], 1, "He acknowledged that other changes, such as new software, may have affected the results."),
]),

("A brief history of the toothbrush", """
<p>People have cleaned their teeth for thousands of years. Early methods included chewing the frayed ends of twigs from aromatic trees, a practice that continues in parts of Africa, the Middle East and South Asia today. Brushes with bristles set into a handle of bone or bamboo were in use in China by the fifteenth century, using coarse hair from pigs.</p>
<p>In England, William Addis is often credited with the first mass-produced toothbrush. According to a frequently repeated story, he came up with the idea while in prison around 1780, drilling holes in a piece of bone and threading bristles through them. Whether the prison story is true is uncertain, but the company he founded made toothbrushes for more than two centuries.</p>
<p>Animal bristles had drawbacks: they dried slowly and could harbour bacteria. Nylon bristles, introduced in the late 1930s, solved these problems and were cheaper. Even so, regular toothbrushing did not become common in many countries until the mid-twentieth century.</p>""",
[
 ("Chewing twigs to clean teeth is no longer practised anywhere.", TF, 1, "The passage says it 'continues in parts of Africa, the Middle East and South Asia today'."),
 ("William Addis definitely invented the toothbrush while in prison.", TF, 1, "The prison story is described as uncertain, and brushes existed in China centuries earlier."),
 ("Nylon bristles dried faster than animal bristles.", TF, 0, "Nylon 'solved these problems', one of which was that animal bristles dried slowly."),
 ("According to the passage, when did regular toothbrushing become common in many countries?", ["In the fifteenth century", "Around 1780", "In the late 1930s", "In the mid-twentieth century"], 3, "The final sentence says it was not common until the mid-twentieth century."),
]),

("The year without a summer", """
<p>In April 1815 Mount Tambora, a volcano in what is now Indonesia, erupted with enormous force. Tens of thousands of people on the surrounding islands died, from the eruption itself and from the famine that followed. The eruption also sent vast quantities of sulphur gas high into the atmosphere, where it formed a haze of tiny droplets that reflected sunlight back into space.</p>
<p>The following year, 1816, became known in Europe and North America as 'the year without a summer'. Snow fell in parts of New England in June, and crops failed across much of northern Europe, causing food prices to soar. Historians have linked the hardship to migration, unrest and the spread of disease.</p>
<p>At the time, no one connected the cold weather with an eruption on the other side of the world. The link was established by scientists only in the twentieth century, using records from ice cores and historical accounts.</p>""",
[
 ("The eruption caused deaths both directly and through famine.", TF, 0, "Deaths came 'from the eruption itself and from the famine that followed'."),
 ("People in 1816 blamed Tambora for the cold summer.", TF, 1, "'At the time, no one connected the cold weather' with the eruption."),
 ("Food prices rose in parts of Europe in 1816.", TF, 0, "Crops failed 'causing food prices to soar'."),
 ("How did the eruption cool the climate, according to the passage?", ["Ash blocked out the sun for the whole of 1816.", "Sulphur droplets reflected sunlight back into space.", "Lava flows cooled the oceans.", "Snow from the volcano spread to New England."], 1, "The sulphur haze 'reflected sunlight back into space'."),
]),

("Microplastics", """
<p>Microplastics are fragments of plastic smaller than five millimetres. Some are made deliberately small, such as the beads once added to face scrubs, while most come from larger items breaking down through sunlight and wear. Washing synthetic clothing releases fibres, and car tyres shed tiny particles as they wear against the road.</p>
<p>Microplastics have been found in seawater, soil, drinking water and the bodies of many animals. Researchers have also detected them in human tissue. What is far less clear is whether they cause harm at the levels people are exposed to. Laboratory studies have shown effects on cells, but often at concentrations much higher than those found in the environment.</p>
<p>Measuring exposure is itself difficult. Plastic is everywhere in laboratories, so samples are easily contaminated, and different research groups use different methods, which makes their results hard to compare.</p>""",
[
 ("Most microplastics are manufactured deliberately at a small size.", TF, 1, "Most 'come from larger items breaking down'."),
 ("Microplastics have been shown to harm human health at normal exposure levels.", TF, 1, "The passage says this is 'far less clear'; lab effects were often at much higher concentrations."),
 ("Car tyres are a larger source of microplastics than clothing.", TF, 2, "Both are named as sources; the passage doesn't compare them."),
 ("Why are results from different studies hard to compare?", ["Microplastics break down too quickly to measure.", "Groups use different methods, and contamination is common.", "Laboratories are not allowed to use plastic.", "Most studies only test seawater."], 1, "The final paragraph cites contamination and differing methods."),
]),

("Bilingual brains", """
<p>For much of the twentieth century, parents in some countries were advised not to raise children with two languages, in the belief that it would confuse them and delay their speech. Later research overturned this view: children who grow up bilingual generally reach language milestones within the normal range, though each of their vocabularies may be smaller at first than a monolingual child's.</p>
<p>More recently, some studies claimed that switching between languages strengthens 'executive function', the mental skills used to plan, focus and ignore distractions. This idea attracted widespread media coverage. However, larger and more carefully designed studies have often failed to find a clear advantage, and some researchers argue that early positive results were more likely to be published than negative ones.</p>
<p>Few researchers dispute the practical benefits of speaking more than one language, from travel and work to family connections. The debate is about whether there is an extra cognitive bonus.</p>""",
[
 ("Bilingual children usually reach language milestones within the normal range.", TF, 0, "Stated in the first paragraph."),
 ("Larger studies have consistently confirmed a bilingual advantage in executive function.", TF, 1, "They 'have often failed to find a clear advantage'."),
 ("Bilingual children always know more words in total than monolingual children.", TF, 2, "The passage says each vocabulary may be smaller at first; it doesn't compare total vocabularies."),
 ("What is the main point of disagreement described in the passage?", ["Whether bilingualism has practical benefits", "Whether bilingual children are confused", "Whether bilingualism gives an extra cognitive advantage", "Whether parents should teach two languages"], 2, "The last sentence: the debate is about 'an extra cognitive bonus'."),
]),

("Coral bleaching", """
<p>Reef-building corals live in partnership with microscopic algae that live inside their tissues. The algae provide much of the coral's energy through photosynthesis and give corals their colour. When the water becomes too warm for too long, this partnership breaks down: the coral expels the algae and turns white, a process called bleaching.</p>
<p>Bleached corals are not dead. If temperatures return to normal quickly, the algae can recolonise and the coral can recover. If heat stress continues, however, many corals starve. Repeated bleaching events, with less time to recover between them, are now one of the greatest threats to reefs.</p>
<p>Some coral species and individual colonies tolerate heat better than others, and scientists are studying whether more tolerant corals could be bred or transplanted. Most researchers say such efforts can buy time but will not save reefs on their own unless warming is limited.</p>""",
[
 ("Bleached corals are dead.", TF, 1, "'Bleached corals are not dead.'"),
 ("The algae give corals their colour.", TF, 0, "Stated in the first paragraph."),
 ("Most researchers think breeding heat-tolerant corals could save reefs on its own.", TF, 1, "Most researchers say such efforts 'will not save reefs on their own unless warming is limited'."),
 ("Which factor does the passage say makes repeated bleaching especially damaging?", ["Less time to recover between events", "Pollution from coastal towns", "Algae becoming more toxic", "Corals being too tolerant of heat"], 0, "'With less time to recover between them.'"),
]),

("The local library", """
<p>The council's plan to close the Elm Road library and replace it with a 'digital hub' in the town centre has been presented as modernisation. It is nothing of the kind. Visitor numbers have fallen, the council says, yet it has cut opening hours three times in five years. It is hardly surprising that fewer people visit a building that is rarely open.</p>
<p>The library is not just a store of books. It is the only free, warm, indoor space in the area where people can sit without buying anything. Older residents attend its reading groups; parents bring toddlers to rhyme time; students without quiet space at home study there in the evenings. A digital hub two bus rides away will not serve these people.</p>
<p>Of course the council faces real budget pressures, and nobody expects services to be immune. But cutting a well-used community space to save a sum that is small within the council's overall budget is a false economy.</p>""",
[
 ("The author believes falling visitor numbers are partly caused by reduced opening hours.", TF, 0, "'It is hardly surprising that fewer people visit a building that is rarely open.'"),
 ("The author thinks the council has no budget pressures.", TF, 1, "The author says 'the council faces real budget pressures'."),
 ("The digital hub will offer reading groups for older residents.", TF, 2, "The passage doesn't say what services the hub will offer."),
 ("Which best describes the author's view?", ["Libraries should be replaced by digital services.", "Closing the library is a false economy that would harm local people.", "The council should raise taxes to fund libraries.", "Visitor numbers prove the library is no longer needed."], 1, "The author argues the closure would harm users and calls it a false economy."),
]),

("The placebo effect", """
<p>A placebo is a treatment with no active ingredient, such as a sugar pill. Patients who receive placebos in clinical trials often report improvements, particularly in symptoms such as pain, nausea and tiredness. This is why new drugs are usually tested against a placebo rather than against no treatment at all.</p>
<p>Part of the apparent placebo effect is not caused by the placebo at all. Many conditions improve naturally over time, and symptoms that are unusually bad when someone enrols in a trial tend to be less severe later, a statistical effect called regression to the mean. However, studies have shown that expectations can genuinely change how pain is experienced, so some of the effect is real.</p>
<p>Surprisingly, some studies have found that placebos can help even when patients are told they are taking a placebo. These 'open-label' studies have mostly been small, and researchers disagree about how widely the results apply.</p>""",
[
 ("New drugs are usually compared with a placebo rather than with no treatment.", TF, 0, "Stated in the first paragraph."),
 ("The whole of the placebo effect is caused by regression to the mean.", TF, 1, "Some of the effect is real, because expectations can change pain."),
 ("Open-label placebo studies have mostly involved large numbers of patients.", TF, 1, "They 'have mostly been small'."),
 ("Which conclusion is best supported by the passage?", ["Placebos cure most illnesses.", "Some improvement seen with placebos would have happened anyway.", "Patients must never be told they are taking a placebo.", "Placebos work best for broken bones."], 1, "Natural improvement and regression to the mean explain part of the apparent effect."),
]),

("Electric cars and batteries", """
<p>Electric cars produce no exhaust emissions while driving, but building their batteries requires mining metals such as lithium, nickel and cobalt. Manufacturing an electric car therefore usually generates more greenhouse gas than building a comparable petrol car.</p>
<p>Over its lifetime, though, an electric car typically makes up for this 'carbon debt' because it emits less when in use. How quickly depends largely on how the electricity it uses is generated: in a country that relies heavily on coal, the advantage is smaller and takes longer to appear than in one with plenty of wind, solar or nuclear power.</p>
<p>Battery recycling is still developing. Recovering metals from old batteries is technically possible, but at present it is often more expensive than mining new material. Supporters argue this will change as more batteries reach the end of their lives and recycling plants grow in scale.</p>""",
[
 ("Building an electric car usually produces more greenhouse gas than building a comparable petrol car.", TF, 0, "Stated in the first paragraph."),
 ("Electric cars have a smaller lifetime advantage in countries that rely heavily on coal.", TF, 0, "'In a country that relies heavily on coal, the advantage is smaller.'"),
 ("Battery recycling is currently cheaper than mining new metals.", TF, 1, "It is 'often more expensive than mining new material'."),
 ("What determines how quickly an electric car repays its 'carbon debt', according to the passage?", ["The size of the car's battery", "How the electricity it uses is generated", "The price of lithium", "How often the battery is recycled"], 1, "'How quickly depends largely on how the electricity it uses is generated.'"),
]),

("Teenagers and sleep", """
<p>During adolescence, the body's internal clock shifts later. Many teenagers do not feel sleepy until around 11pm or later, and naturally wake later too. Yet school start times in many countries require them to be up early, which can leave them with less sleep than experts recommend.</p>
<p>Some school districts that moved their start times later reported that students slept longer, and in some cases attendance and grades improved. Critics point out that changing timetables is costly and complicated: buses must be rescheduled, and later finishes can clash with sports and part-time jobs.</p>
<p>Screen use in the evening is often blamed for poor sleep, and bright light at night can delay sleepiness. But researchers note that the shift in the body clock happens even in teenagers who use screens little, so screens are unlikely to be the whole explanation.</p>""",
[
 ("Teenagers' internal clocks shift earlier during adolescence.", TF, 1, "It 'shifts later'."),
 ("Later school start times improved grades in every district that tried them.", TF, 1, "Grades improved 'in some cases', not everywhere."),
 ("Screens are the main cause of teenagers' late sleep times.", TF, 2, "The passage says screens are 'unlikely to be the whole explanation', but it doesn't say whether they are the main cause, so you can't tell."),
 ("Which is given as an argument against later school start times?", ["Students would sleep too long.", "Rescheduling buses and activities is costly and complicated.", "Teenagers' body clocks would shift back.", "Attendance would fall."], 1, "Critics point to cost and complications such as buses, sport and jobs."),
]),

("Returning museum objects", """
<p>Many museums in Europe hold objects taken from other countries during periods of colonial rule. Some were bought, some were given, and some were seized by force. Increasingly, governments and communities in the countries of origin are asking for them back.</p>
<p>Museums that resist returns often argue that their collections allow visitors to compare cultures from across the world in one place, and that objects are well conserved. Critics reply that this argument conveniently benefits the museums themselves, and that the people with the strongest connection to an object should decide where it belongs. In recent years several museums have returned items, including some that had been on display for more than a century.</p>
<p>Returns are not always simple. Records of how an object was acquired may be incomplete, and in some cases more than one community or country claims the same item.</p>""",
[
 ("All objects taken during colonial rule were seized by force.", TF, 1, "'Some were bought, some were given, and some were seized.'"),
 ("Some museums have returned objects that had been displayed for over a hundred years.", TF, 0, "Stated in the second paragraph."),
 ("Most European museums now support returning objects.", TF, 2, "The passage says 'several' have returned items; it doesn't say what most museums think."),
 ("Which is given as a difficulty with returning objects?", ["Objects are too fragile to move.", "Records of acquisition may be incomplete.", "Countries of origin refuse to accept them.", "Visitors would stop going to museums."], 1, "Incomplete records and competing claims are named."),
]),

("Honeybees and wild pollinators", """
<p>Honeybees are the best-known pollinators, but they are far from the only ones. Wild bees, hoverflies, butterflies, moths and beetles also pollinate crops and wild plants. For some crops, wild insects do much of the work, and certain plants are pollinated far more effectively by particular wild species than by honeybees.</p>
<p>Honeybee hives are managed by beekeepers, so their numbers can be increased when colonies are lost. Wild pollinators have no such support. Many species have declined as meadows and hedgerows have disappeared and pesticide use has increased.</p>
<p>Some conservationists warn that encouraging large numbers of new hives in towns may even harm wild bees by increasing competition for limited flowers. They argue that planting more wildflowers and leaving areas unmown would do more good than adding hives.</p>""",
[
 ("Honeybees are the only important pollinators of crops.", TF, 1, "Wild bees, hoverflies and others also pollinate crops, sometimes doing much of the work."),
 ("Beekeepers can increase honeybee numbers after colonies are lost.", TF, 0, "'Their numbers can be increased when colonies are lost.'"),
 ("Pesticides are the main cause of wild pollinator decline.", TF, 2, "Pesticides and habitat loss are both named; the passage doesn't rank them."),
 ("What do some conservationists recommend instead of adding hives in towns?", ["Importing wild bees", "Banning all pesticides in towns", "Planting wildflowers and leaving areas unmown", "Keeping honeybees indoors"], 2, "Stated in the final paragraph."),
]),

("Antibiotics on farms", """
<p>Antibiotics are used in farming to treat sick animals and, in some countries, to prevent disease in healthy animals kept in crowded conditions. In the past they were also widely given in low doses to make animals grow faster, a practice that has since been banned in the European Union and the United Kingdom.</p>
<p>The concern is that using antibiotics in animals encourages bacteria to become resistant, and that resistant bacteria or the genes responsible can pass to people through food, water or direct contact. How much farm use contributes to resistant infections in humans, compared with antibiotic use in human medicine, is still debated.</p>
<p>Several countries have cut farm antibiotic use substantially by improving hygiene, vaccinating animals and reducing overcrowding, without large falls in production. Critics of further restrictions argue that farmers must still be able to treat sick animals for welfare reasons.</p>""",
[
 ("Using antibiotics to make animals grow faster is banned in the United Kingdom.", TF, 0, "Stated in the first paragraph."),
 ("Most resistant infections in humans come from farm antibiotic use.", TF, 2, "The relative contribution 'is still debated'."),
 ("Some countries have reduced farm antibiotic use without large falls in production.", TF, 0, "Stated in the final paragraph."),
 ("Why do critics oppose further restrictions?", ["Antibiotics are cheaper than vaccines.", "Farmers need to be able to treat sick animals for welfare.", "Resistance cannot pass from animals to people.", "Crowded farms do not need hygiene measures."], 1, "Critics argue farmers must still be able to treat sick animals."),
]),

("Printing and the spread of ideas", """
<p>Printing with movable metal type spread rapidly across Europe in the second half of the fifteenth century, following its development in the German city of Mainz. Within fifty years, presses were operating in hundreds of towns, and millions of books had been produced.</p>
<p>Before printing, books in Europe were copied by hand, which made them expensive and meant that copying errors multiplied as texts were reproduced. Printing made identical copies possible, so scholars in different cities could refer to the same page of the same edition.</p>
<p>The change was not immediate for most people. The majority of Europeans could not read, and early printed books were still costly. Pamphlets and single printed sheets, which were cheap and could be read aloud to others, probably did more to spread news and arguments among ordinary people than books did.</p>""",
[
 ("Printing with movable metal type was developed in Mainz.", TF, 0, "'Following its development in the German city of Mainz.'"),
 ("Most Europeans could read by 1500.", TF, 1, "'The majority of Europeans could not read.'"),
 ("Early printed books were cheaper than pamphlets.", TF, 1, "Pamphlets were described as cheap while early books 'were still costly'."),
 ("What advantage of printing for scholars does the passage describe?", ["They could print their own books at home.", "They could refer to identical copies of the same edition.", "Books no longer needed to be read aloud.", "Copying errors increased."], 1, "Identical copies let scholars in different cities refer to the same page."),
]),

("Social media and wellbeing", """
<p>Concern about the effect of social media on young people's mental health has grown alongside reports of rising anxiety and depression among teenagers in several countries. Many studies have found an association between heavy social media use and lower wellbeing.</p>
<p>Association, however, is not the same as causation. Young people who are already unhappy may use social media more, rather than social media making them unhappy. Many studies also rely on teenagers estimating their own screen time, which is often inaccurate. Researchers increasingly argue that how young people use social media, and what they see, may matter more than the total time spent.</p>
<p>Some governments have introduced or proposed age limits for social media accounts. Supporters say this protects children while research catches up; opponents question whether such limits can be enforced and whether they cut young people off from support networks.</p>""",
[
 ("Studies have proven that social media causes depression in teenagers.", TF, 1, "The passage stresses that association is not causation."),
 ("Teenagers' estimates of their own screen time are often inaccurate.", TF, 0, "Stated in the second paragraph."),
 ("Age limits for social media have been introduced in every country.", TF, 1, "'Some governments have introduced or proposed' them."),
 ("Which alternative explanation for the association does the passage give?", ["Social media improves wellbeing.", "Unhappy young people may use social media more.", "Teenagers underestimate their happiness.", "Age limits cause anxiety."], 1, "'Young people who are already unhappy may use social media more.'"),
]),
]
