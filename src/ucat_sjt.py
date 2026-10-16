"""Original Situational Judgement scenarios.
Rating items: ("app", response, answer, explanation) using
  0 Very appropriate · 1 Appropriate, but not ideal · 2 Inappropriate, but not awful · 3 Very inappropriate
  ("imp", consideration, answer, explanation) using
  0 Very important · 1 Important · 2 Of minor importance · 3 Not important at all
MC items: ("mc", question, [options], answer, explanation)."""

SJT = [
("""<p>Aisha, a second-year dental student on clinic, notices that a classmate, Tom, has posted a photo on social media of the clinic waiting room. A patient's face is clearly visible in the background.</p>""", [
 ("app", "Aisha speaks to Tom privately and asks him to remove the photo straight away.", 0, "Quick, discreet action protects the patient's confidentiality and gives Tom the chance to fix it."),
 ("app", "Aisha comments publicly on the post saying it breaches patient confidentiality.", 2, "The concern is right, but a public comment draws more attention to the patient and humiliates Tom. Raise it privately."),
 ("app", "Aisha ignores it because it's Tom's account and not her responsibility.", 3, "Everyone has a duty to act when a patient's confidentiality is at risk."),
 ("app", "If Tom refuses to remove it, Aisha tells the clinical tutor.", 0, "Escalating is appropriate if the breach continues; patient confidentiality comes first."),
]),
("""<p>Ben is in a group of four dental students preparing a presentation due in two days. One member, Chloe, has not contributed and hasn't replied to messages for a week.</p>""", [
 ("app", "Ben messages Chloe privately, asking if she is OK and whether she can still do her part.", 0, "Checking in shows concern for her wellbeing and gives her a chance to respond."),
 ("app", "Ben and the others share Chloe's section between them so the work is finished on time.", 1, "This protects the deadline, but on its own doesn't address why Chloe is absent or make sure she is OK."),
 ("app", "Ben tells the tutor that Chloe is lazy and should fail.", 3, "Making judgements without knowing the facts is unprofessional and unfair."),
 ("app", "Ben emails the tutor about Chloe before trying to contact her himself.", 1, "Involving the tutor near a deadline is reasonable, but Ben should first try to reach Chloe directly; she may have a good reason."),
]),
("""<p>Daniel, a final-year dental student, is treating a patient under supervision. He realises that he has started preparing the wrong tooth: the upper left first premolar instead of the upper left second premolar. He has removed only a small amount of enamel.</p>""", [
 ("app", "Daniel stops and tells his supervisor immediately.", 0, "Patient safety and honesty come first. The supervisor can advise on what to do next."),
 ("app", "Daniel continues on the correct tooth and says nothing, as the damage is minor.", 3, "Concealing a mistake breaches the duty of candour and puts trust at risk."),
 ("app", "Daniel explains to the patient what has happened, with his supervisor present.", 0, "Patients must be told openly when something goes wrong (duty of candour)."),
 ("app", "Daniel records the incident in the notes but waits until the end of the session to tell his supervisor.", 2, "Recording it is right, but the supervisor needs to know now: the error affects what happens next for this patient."),
]),
("""<p>Ella, a dental student, is shadowing at a practice. Between patients she overhears the dentist making a rude joke about a patient's weight to the dental nurse. The patient has already left.</p>""", [
 ("imp", "That the patient did not hear the comment", 2, "It reduces immediate harm, but disrespectful comments about patients are unprofessional regardless."),
 ("imp", "That Ella is a guest at the practice and the dentist is senior", 1, "It's sensible to consider how to raise concerns respectfully, but it shouldn't stop her raising them."),
 ("imp", "The need to treat all patients with dignity and respect", 0, "Respect for patients is a core professional value."),
 ("imp", "Whether the dental nurse laughed at the joke", 3, "This doesn't change whether the comment was appropriate."),
]),
("""<p>Farah is a first-year dental student. During a busy exam period, a friend offers her a copy of last year's anatomy exam answers, saying lots of students have them. Farah isn't sure whether using them is allowed.</p>""", [
 ("app", "Farah doesn't open the file and plans to mention it to the module lead after the exam.", 1, "She avoids cheating, which is good, but a possible leak affects fairness for everyone and is better raised before the exam."),
 ("app", "Farah uses the answers, since others are using them too.", 3, "'Everyone is doing it' doesn't make it acceptable; it may be academic misconduct."),
 ("app", "Farah declines and revises using the official materials.", 0, "The safest and most honest choice."),
 ("app", "Farah takes the file but promises herself not to open it until after the exam.", 2, "Not cheating directly, but holding material that may be prohibited is unwise."),
]),
("""<p>George, a dental student on clinic, has an appointment with a patient who arrives 25 minutes late for a 45-minute filling appointment. The next patient is due straight after.</p>""", [
 ("app", "George explains politely that there isn't enough time and offers to rebook, after checking with his supervisor.", 0, "Honest, polite and safe; involving the supervisor follows clinic procedure."),
 ("app", "George rushes the filling to fit it into the remaining time.", 3, "Rushing clinical work risks patient safety and quality of care."),
 ("app", "George asks the supervisor whether part of the treatment can be done safely today.", 0, "This looks for the best outcome for the patient within safe limits."),
 ("app", "George tells the patient they should have been on time and refuses to see them.", 2, "Rebooking may be necessary, but a blaming tone is unprofessional; there may be a good reason for lateness."),
]),
("""<p>Hana, a dental student, notices that her clinical partner Isaac smells strongly of alcohol at the start of a morning clinic session. He says he was out late but feels fine.</p>""", [
 ("imp", "The safety of the patients Isaac is about to treat", 0, "Patient safety is the overriding priority."),
 ("imp", "Isaac's assurance that he feels fine", 2, "People affected by alcohol often underestimate it; his view shouldn't decide the matter."),
 ("imp", "Isaac's wellbeing and whether he needs support", 1, "Important, but secondary to immediate patient safety."),
 ("imp", "That reporting Isaac might damage their friendship", 3, "Friendship must not outweigh patients' safety."),
]),
("""<p>Hana (from the previous scenario) decides to act.</p>""", [
 ("mc", "Which is the MOST appropriate action for Hana to take?", ["Tell the clinical supervisor before patients are seen", "Treat Isaac's patients herself without saying anything", "Tell Isaac to drink some coffee and carry on", "Post anonymously in the year group chat about it"], 0, "The supervisor can make sure patients are safe and that Isaac is supported."),
 ("mc", "Which is the LEAST appropriate action for Hana to take?", ["Suggest Isaac speaks to the supervisor himself", "Say nothing in case she has misjudged it", "Ask Isaac how much he drank", "Offer to help Isaac seek support later"], 1, "Ignoring a potential risk to patients is the least appropriate option."),
]),
("""<p>Jack, a dental student, is taking a medical history. The patient says they don't want to tell a student about their medication and asks to see 'a proper dentist'.</p>""", [
 ("app", "Jack explains his role, that he is supervised, and why the information matters for safe care.", 0, "Clear explanation may reassure the patient and respects their choice."),
 ("app", "Jack asks his supervisor to take over without explaining to the patient why the question matters.", 1, "Getting help is sensible, but Jack misses the chance to explain, which might have reassured the patient."),
 ("app", "Jack records 'no medication' so the appointment can continue.", 3, "Falsifying records is dishonest and could put the patient at serious risk."),
 ("app", "Jack tells the patient they must answer or they cannot be treated.", 2, "Treatment may indeed depend on it, but presenting it as an ultimatum is coercive and unhelpful."),
]),
("""<p>Kemi is volunteering on a ward as part of a work-experience placement before applying to dentistry. A patient asks her for a glass of water, but she has been told some patients are 'nil by mouth' before surgery.</p>""", [
 ("app", "Kemi checks with a nurse before giving the patient anything.", 0, "She doesn't know whether the patient can drink, so checking keeps the patient safe."),
 ("app", "Kemi gives the patient a small amount, as water is harmless.", 3, "Water could be dangerous before an anaesthetic; she must not guess."),
 ("app", "Kemi tells the patient she can't help and suggests they press the call bell for a nurse.", 1, "This points the patient to the right person, but finding out for them herself would be more helpful."),
 ("app", "Kemi ignores the request because volunteers can't help with care.", 2, "She shouldn't give water herself, but ignoring the patient is unkind. She should pass the request on."),
]),
("""<p>Leo, a dental student, is behind with a reflective portfolio due tomorrow. A friend offers to send Leo her portfolio so he can 'get some ideas'.</p>""", [
 ("imp", "That reflective portfolios must reflect Leo's own experiences", 0, "Reflection must be personal and genuine; copying is misconduct."),
 ("imp", "That his friend has offered willingly", 3, "Her willingness doesn't make copying acceptable."),
 ("imp", "Whether he could ask for an extension because of genuine difficulties", 1, "A legitimate option worth considering if there are real reasons."),
 ("imp", "The risk that both students could face fitness-to-practise action", 1, "Important, but the main point is that copying is dishonest, whatever the consequences."),
]),
("""<p>Maya, a dental student, is helping on a school oral-health visit. A seven-year-old tells her quietly that she often has no breakfast and that her dad 'gets angry a lot'.</p>""", [
 ("app", "Maya listens calmly and tells the lead dentist or the school's safeguarding lead the same day.", 0, "Possible safeguarding concerns must be passed to the right person promptly."),
 ("app", "Maya promises the child she won't tell anyone.", 3, "She cannot promise confidentiality when a child may be at risk."),
 ("app", "Maya asks the child detailed questions about her home life.", 2, "Some reassurance is fine, but investigating isn't her role and could cause distress or affect any later enquiry."),
 ("app", "Maya writes down what the child said, in the child's words, and the time.", 0, "Accurate notes help those who follow up."),
]),
("""<p>Noah, a dental student, has been feeling low for several weeks. He is struggling to concentrate on clinic and has stopped seeing friends.</p>""", [
 ("app", "Noah speaks to his personal tutor or the university wellbeing service.", 0, "Seeking support early is the right thing to do."),
 ("app", "Noah decides to wait until the holidays and see his GP then if he still feels low.", 2, "Seeing a GP is right, but delaying while he's struggling on clinic risks his wellbeing and possibly patient care."),
 ("app", "Noah keeps going to clinic and hides how he feels so no one thinks less of him.", 2, "Understandable, but hiding problems can affect his health and possibly patient care."),
 ("app", "Noah stops attending clinic without telling anyone.", 3, "Unexplained absence lets down patients and colleagues and leaves him without support."),
]),
("""<p>Olivia is a dental student treating a patient who becomes angry because the appointment is running 20 minutes late. The patient raises their voice in the waiting room.</p>""", [
 ("app", "Olivia apologises for the wait and explains the reason calmly.", 0, "Acknowledging the frustration and explaining can defuse the situation."),
 ("app", "Olivia raises her own voice so the patient will listen.", 3, "Escalating makes things worse and is unprofessional."),
 ("app", "Olivia moves on to her next task and leaves the receptionist to deal with the upset patient.", 2, "The receptionist may help, but walking away without acknowledging the patient is likely to make things worse."),
 ("app", "Olivia tells the patient they can complain if they're not happy.", 1, "Patients do have a right to complain, but leading with this can sound dismissive; listening first is better."),
]),
("""<p>Priya, a dental student, sees a classmate copying answers from another student during an online class test that counts towards the final mark.</p>""", [
 ("imp", "The fairness of the assessment for other students", 0, "Cheating undermines fairness and the validity of the qualification."),
 ("imp", "That the classmate is a close friend of Priya's", 2, "Friendship may make it harder, but shouldn't decide what's right."),
 ("imp", "That dentists need to be honest and trustworthy", 0, "Honesty is central to professionalism."),
 ("imp", "Whether the test is worth only a small percentage of the module", 2, "Even small-scale dishonesty matters professionally."),
]),
("""<p>Quinn, a dental student, accidentally sends an email containing a patient's name and treatment plan to the wrong student.</p>""", [
 ("app", "Quinn tells their supervisor straight away.", 0, "Data breaches must be reported promptly so they can be managed."),
 ("app", "Quinn asks the other student to delete the email and confirm they've done so.", 1, "Sensible, but it should be done alongside reporting, not instead of it."),
 ("app", "Quinn says nothing because the other student is also a dental student.", 3, "It's still a breach of confidentiality and must be reported."),
 ("app", "Quinn follows the clinic's data breach procedure.", 0, "Following procedure ensures the right steps are taken."),
]),
("""<p>Ravi, a dental student on placement, is asked by a patient to recommend a private cosmetic treatment that the patient saw advertised online. Ravi doesn't know much about it.</p>""", [
 ("app", "Ravi says he isn't sure and offers to ask his supervisor.", 0, "Honest about the limits of his knowledge."),
 ("app", "Ravi gives his opinion based on what he's seen on social media.", 3, "Advice outside his competence, based on unreliable sources, could mislead the patient."),
 ("app", "Ravi tells the patient to look it up online.", 2, "Not harmful in itself, but unhelpful and may lead to poor information."),
 ("app", "Ravi suggests the patient discusses it with the dentist at their next appointment.", 1, "Appropriate, but involving his supervisor now would be better."),
]),
("""<p>Sofia, a dental student, has been asked by a patient she treated to connect with her on social media and to meet for coffee.</p>""", [
 ("app", "Sofia politely declines, explaining she keeps professional boundaries with patients.", 0, "Maintaining professional boundaries protects patients and clinicians."),
 ("app", "Sofia accepts the friend request but declines the coffee.", 2, "Less serious than meeting, but social media links still blur boundaries."),
 ("app", "Sofia meets the patient, since she's only a student.", 3, "Students are held to professional standards with patients."),
 ("app", "Sofia ignores the request without saying anything.", 1, "She keeps the boundary, which matters most, but a brief polite explanation would avoid confusion if she meets the patient again."),
]),
("""<p>Tariq, a Year 12 student on dental work experience, notices that the dentist doesn't wash their hands or change gloves between two patients.</p>""", [
 ("imp", "The risk of cross-infection to patients", 0, "Infection control protects patients; this is the key consideration."),
 ("imp", "That Tariq is only on work experience and may have missed something", 1, "He should check his facts and act sensibly, but shouldn't ignore a possible risk."),
 ("imp", "That the dentist was kind to Tariq during the placement", 3, "This doesn't change the risk to patients."),
 ("imp", "Knowing who he could speak to, such as the practice manager or his school contact", 1, "Important for deciding how to raise the concern appropriately."),
]),
("""<p>Uma, a dental student, realises after a patient has left that she forgot to record a medication the patient mentioned during the appointment.</p>""", [
 ("app", "Uma adds the information to the notes as soon as possible, dated and marked as a late entry.", 0, "Correct records must be completed honestly, showing when they were written."),
 ("app", "Uma backdates the entry so the record looks complete.", 3, "Altering records to hide when they were written is dishonest."),
 ("app", "Uma tells her supervisor about the omission.", 0, "Important in case the medication affects treatment."),
 ("app", "Uma decides it doesn't matter because the treatment went well.", 2, "Records must be complete for future care even if this visit was fine."),
]),
("""<p>Victor, a dental student, is asked by a nervous patient whether a procedure will hurt. Victor knows there may be some discomfort.</p>""", [
 ("app", "Victor explains honestly what the patient might feel and how it will be managed.", 0, "Honesty supports informed consent and builds trust."),
 ("app", "Victor tells the patient it definitely won't hurt, to calm them.", 2, "Well-meant, but not honest; if it does hurt, the patient's trust is damaged. Not as bad as dismissing their worry."),
 ("app", "Victor reassures the patient that most people find it less uncomfortable than they expect.", 1, "Kind and broadly true, but it doesn't answer the patient's specific question or explain how discomfort will be managed."),
 ("app", "Victor says he doesn't know and moves on quickly.", 2, "He should give what information he can or ask his supervisor."),
]),
("""<p>Willow, a dental student, finds that a group project includes several paragraphs copied from a website without referencing. The group member who wrote that section says 'no one checks'.</p>""", [
 ("app", "Willow explains that it's plagiarism and suggests rewriting and referencing it properly.", 0, "Addresses the problem directly and constructively."),
 ("app", "Willow rewrites the section herself without telling the group.", 1, "Fixes the problem but misses the chance to resolve it openly with the group."),
 ("app", "Willow submits the project as it is to avoid conflict.", 3, "Submitting plagiarised work puts the whole group at risk of misconduct."),
 ("app", "Willow tells the module lead about the copied section before raising it with the group.", 1, "Plagiarism must be dealt with, but speaking to the group first gives them the chance to fix it themselves."),
]),
("""<p>Xander, a dental student, is running late for clinic because of a train cancellation. His first patient is due in 15 minutes and he will be about 30 minutes late.</p>""", [
 ("app", "Xander phones the clinic straight away to let them know.", 0, "Early warning lets the clinic inform the patient and plan."),
 ("app", "Xander says nothing and hopes the patient is also late.", 3, "Leaving the patient and team uninformed is unprofessional."),
 ("app", "Xander texts the patient from his personal phone to say he's running late.", 2, "Well-intentioned, but students shouldn't contact patients from personal phones; the clinic should pass on the message."),
 ("app", "Xander messages a classmate to pass on the message.", 1, "Better than nothing, but contacting the clinic directly is more reliable."),
]),
("""<p>Yasmin, a dental student, is shadowing a dentist who asks her to carry out a procedure she hasn't been trained to do yet, saying 'it's easy, I'll watch'.</p>""", [
 ("imp", "Whether Yasmin has been trained and assessed as competent for the procedure", 0, "Working within competence protects patients."),
 ("imp", "Not wanting to seem unwilling to the dentist", 3, "Shouldn't influence a decision about patient safety."),
 ("imp", "Whether the patient has consented to treatment by a student", 0, "Consent must be valid, including who is treating them."),
 ("imp", "The dental school's rules about what students may do on placement", 0, "Students must follow their school's clinical governance rules."),
]),
("""<p>Zara, a dental student, notices that a patient seems confused and unsure what treatment they are agreeing to, although they have signed the consent form.</p>""", [
 ("app", "Zara stops and tells her supervisor about her concerns before treatment starts.", 0, "Valid consent requires understanding; a signature alone isn't enough."),
 ("app", "Zara goes ahead because the form is signed.", 3, "A signed form doesn't make consent valid if the patient doesn't understand."),
 ("app", "Zara explains the treatment again in simple terms and checks understanding.", 0, "Helps make consent genuinely informed."),
 ("app", "Zara asks the patient's relative in the waiting room to decide instead.", 3, "Relatives can't consent for an adult who may have capacity; capacity must be assessed properly."),
]),
("""<p>Alex, a dental student, overhears two classmates in a café discussing a patient's dental treatment by name.</p>""", [
 ("app", "Alex quietly reminds them that they could be overheard.", 0, "A tactful reminder stops the breach quickly."),
 ("app", "Alex joins in the conversation.", 3, "That would make the breach worse."),
 ("app", "Alex reports them to the dean without speaking to them first.", 2, "Raising concerns may be needed, but going straight to formal action for a first, minor lapse is disproportionate."),
 ("app", "Alex changes the subject loudly so the others stop talking about the patient.", 1, "It stops the breach in the moment, but doesn't help them realise why it was a problem."),
]),
("""<p>Ben (a dental student) has been asked by a patient to give them a 'quick tooth whitening' outside clinic hours, for cash.</p>""", [
 ("app", "Ben refuses and explains he can only treat patients in clinic under supervision.", 0, "Students mustn't treat patients outside supervised clinical settings."),
 ("app", "Ben agrees, as tooth whitening is low risk.", 3, "Unsupervised, paid treatment is unsafe and may be illegal; whitening is restricted to registered professionals."),
 ("app", "Ben tells his supervisor about the request.", 1, "Reasonable, especially if the patient persists, but declining clearly is the priority."),
 ("app", "Ben suggests the patient asks a qualified dentist about whitening.", 0, "A helpful, appropriate response."),
]),
]
