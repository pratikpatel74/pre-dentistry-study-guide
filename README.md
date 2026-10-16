# Pre-Dentistry Study Hub

Revision hub for a student starting a UK dentistry (BDS) degree: 9 topics, 198 quiz questions, notes and diagrams.
Same design and quiz engine as the A-level finance hub. Static site, no build step: Netlify serves the repo root.

## Structure
- `index.html` – hub homepage (topic cards, last-score badges)
- `quizzes/topicN.html` – quiz: 10 of 22 questions per session, options shuffled, 60s timer toggle, retry missed, keyboard 1–4 / Enter
- `notes/topicN.html` – summary notes with diagrams; printable to PDF

## Topics
1. The UK Dental Landscape
2. Tooth Anatomy & Tissues
3. Tooth Types, Notation & Eruption
4. Dental Caries & Fluoride
5. Periodontal (Gum) Disease
6. Head & Neck Anatomy Essentials
7. Infection Control & Occupational Health
8. Professionalism & Ethics
9. Bridging from A-level

## Editing questions
Question data lives in each `quizzes/topicN.html` (`const POOL=[...]`). The correct answer is the first option (`"ans": 0`);
the page shuffles options each session.

## Deploy
```bash
cd ~/Documents/Projects/pre-dentistry-study-guide
git add -A
git commit -m "Update hub"
git push
```
Netlify redeploys automatically on push to `main`.
