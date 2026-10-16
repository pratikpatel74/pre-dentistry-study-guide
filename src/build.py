"""Build the Pre-Dentistry study hub from the finance hub's templates.

Usage (from the repo root):  python3 src/build.py
Templates come from src/templates (copied from the finance hub); output goes to the repo root.
"""
import html, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content_a import T1, T2, T3, T4, T5
from content_b import T6, T7, T8, T9
from diagrams import DIAGRAMS
from diagrams2 import DIAGRAMS2
DIAGRAMS.update(DIAGRAMS2)
import bridge

TOPICS = [T1, T2, T3, T4, T5, T6, T7, T8, T9]
T9['notes'] = bridge.notes()
T9['blurb'] = 'The A-level topics that come straight back in dentistry (%d of them), each linked to your AQA Biology, Chemistry and Maths hubs.' % bridge.count()
HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(HERE, "templates")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(HERE)
LANDING = "https://alevel-study-hubs.netlify.app/"
THEME_HEAD = '<html lang="en" data-theme="dark"><script>try{var _t=localStorage.getItem("theme");if(_t)document.documentElement.setAttribute("data-theme",_t);}catch(e){}</script>'
FONT = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">'

def rgba(hexc, a):
    h = hexc.lstrip("#")
    r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
    return f"rgba({r},{g},{b},{a})"

def esc(s):
    return html.escape(s, quote=False)

# ---------- validate content ----------
for t in TOPICS:
    assert len(t["qs"]) == 22, (t["num"], len(t["qs"]))
    for q, opts, exp in t["qs"]:
        assert len(opts) == 4 and len(set(opts)) == 4, (t["num"], q)

os.makedirs(f"{OUT}/quizzes", exist_ok=True)
os.makedirs(f"{OUT}/notes", exist_ok=True)

# ---------- quizzes (finance hub topic9.html engine) ----------
tpl = open(os.path.join(TPL, "quiz-template.html"), encoding="utf-8").read()
for t in TOPICS:
    n, title = t["num"], t["title"]
    s = tpl
    s = re.sub(r"<title>.*?</title>", f"<title>Topic {n} Quiz – {esc(title)}</title>", s)
    s = re.sub(r"(:root\{[^}]*?)--accent:#[0-9a-f]+;--accent-bg:rgba\([^)]*\);",
               lambda m: m.group(1) + f"--accent:{t['dark']};--accent-bg:{rgba(t['dark'],0.12)};", s, count=1)
    s = re.sub(r'(\[data-theme="light"\]\{[^}]*?)--accent:#[0-9a-f]+;--accent-bg:rgba\([^)]*\);',
               lambda m: m.group(1) + f"--accent:{t['light']};--accent-bg:{rgba(t['light'],0.10)};", s, count=1)
    s = re.sub(r'<div class="topbar-brand"><span>.*?</span>.*?</div>',
               f'<div class="topbar-brand"><span>Topic {n}</span>{esc(t["short"])}</div>', s, count=1)
    s = re.sub(r'<div class="quiz-eyebrow">.*?</div>', '<div class="quiz-eyebrow">Pre-Dentistry · Topic %d</div>' % n, s, count=1)
    s = re.sub(r'<h1 class="quiz-title">.*?</h1>', f'<h1 class="quiz-title">{esc(title)}</h1>', s, count=1)
    s = s.replace("const TOPIC_ID='topic9'", f"const TOPIC_ID='topic{n}'")
    pool = ",\n".join(json.dumps({"q": esc(q), "opts": [esc(o) for o in opts], "ans": 0, "exp": esc(exp)}, ensure_ascii=False)
                      for q, opts, exp in t["qs"])
    s = re.sub(r"const POOL=\[\n.*?\n\];", lambda m: "const POOL=[\n" + pool + "\n];", s, count=1, flags=re.S)
    # Shuffle answer options each session (the correct answer is stored first).
    s = s.replace("sessionQ=pool.slice(0,Math.min(DRAW,pool.length));",
                  "sessionQ=pool.slice(0,Math.min(DRAW,pool.length)).map(q=>{const o=[0,1,2,3];"
                  "for(let i=3;i>0;i--){const j=Math.floor(Math.random()*(i+1));[o[i],o[j]]=[o[j],o[i]];}"
                  "return Object.assign({},q,{opts:o.map(k=>q.opts[k]),ans:o.indexOf(q.ans)});});")
    if n in (5, 9):  # light accents need dark text in the dark theme
        s = s.replace("</style>", ".btn-next,.btn-quiz{color:#000}[data-theme=\"light\"] .btn-next{color:#fff}</style>", 1)
    s = s.replace("initSession();\n</script>", "try{if(document.documentElement.getAttribute('data-theme')==='light')document.querySelector('.theme-btn').textContent='🌙';}catch(e){}\ninitSession();\n</script>", 1)
    assert "textContent='🌙'" in s
    assert "const TOPIC_ID='topic%d'" % n in s and "o.indexOf(q.ans)" in s and "Bank Accounts" not in s
    open(f"{OUT}/quizzes/topic{n}.html", "w", encoding="utf-8").write(s)

# ---------- notes pages ----------
NOTES_CSS = """
:root{--bg:#09090f;--surface:#111118;--card:#16161e;--border:#2a2a38;--border-hi:#3d3d52;--text:#f0efff;--muted:#8b8aab;--dim:#55546e;--gold:#e8b84b;--gold-bg:rgba(232,184,75,0.10);--danger:#f87171;
--d-enamel:#a5b4fc;--d-dentine:#fcd9b8;--d-pulp:#f9a8a8;--d-gum:#f0abfc;--d-bone:#2a2a38;--d-pdl:#fb7185;
--d-inc:#60a5fa;--d-can:#fb923c;--d-pm:#34d399;--d-mol:#94a3b8;--d-gum-sore:#f87171;--ok:#34d399}
[data-theme="light"]{--bg:#f5f4f0;--surface:#eeede8;--card:#fff;--border:#dddbd4;--border-hi:#c8c5bc;--text:#1a1814;--muted:#706c60;--dim:#a09c90;--gold:#b8861a;--gold-bg:rgba(184,134,26,0.08);--danger:#dc2626;
--d-enamel:#c7d2fe;--d-dentine:#fde7d2;--d-pulp:#fca5a5;--d-gum:#f5c2f9;--d-bone:#e7e5e0;--d-pdl:#e11d48;
--d-inc:#93c5fd;--d-can:#fdba74;--d-pm:#6ee7b7;--d-mol:#cbd5e1;--d-gum-sore:#fca5a5;--ok:#059669}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Inter',system-ui,sans-serif;background:var(--bg);color:var(--text);min-height:100vh;line-height:1.6}
.topbar{position:sticky;top:0;z-index:50;background:rgba(9,9,15,0.85);backdrop-filter:blur(16px);border-bottom:1px solid var(--border);padding:0 24px;display:flex;align-items:center;justify-content:space-between;height:52px}
[data-theme="light"] .topbar{background:rgba(245,244,240,0.88)}
.topbar-brand{font-size:0.9rem;font-weight:700;display:flex;align-items:center;gap:10px}
.topbar-brand span{font-size:0.68rem;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;background:var(--gold-bg);color:var(--gold);border:1px solid var(--gold);border-radius:4px;padding:2px 8px}
.back-link{font-size:0.78rem;font-weight:600;color:var(--muted);text-decoration:none}
.back-link:hover{color:var(--text)}
.theme-btn{background:var(--surface);border:1px solid var(--border);border-radius:8px;width:34px;height:34px;cursor:pointer;font-size:15px;display:flex;align-items:center;justify-content:center;color:var(--muted)}
.container{max-width:760px;margin:0 auto;padding:48px 20px 80px}
.eyebrow{font-size:0.68rem;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:var(--accent);margin-bottom:10px}
h1{font-size:2rem;font-weight:800;letter-spacing:-0.03em;margin-bottom:20px;line-height:1.15}
h2{font-size:1.1rem;font-weight:700;margin:32px 0 12px;padding-top:8px;border-top:1px solid var(--border)}
p,li{font-size:0.95rem;color:var(--text)}
p{margin-bottom:12px}
.lead{font-size:1.05rem;color:var(--muted);margin-bottom:24px}
ul,ol{padding-left:22px;margin-bottom:12px}li{margin-bottom:6px}
a{color:var(--accent)}
table{width:100%;border-collapse:collapse;margin:8px 0 16px;font-size:0.88rem;background:var(--card);border:1px solid var(--border);border-radius:10px;overflow:hidden}
th,td{text-align:left;padding:9px 12px;border-bottom:1px solid var(--border);vertical-align:top}
th{font-size:0.7rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--dim);background:var(--surface)}
tr:last-child td{border-bottom:none}
.formula{font-family:ui-monospace,Menlo,monospace;background:var(--card);border:1px solid var(--border);border-left:3px solid var(--accent);border-radius:8px;padding:10px 14px;margin:10px 0;font-size:0.9rem;overflow-x:auto}
.callout{background:var(--accent-bg);border:1px solid var(--accent);border-radius:10px;padding:12px 16px}
.diagram{margin:20px 0 24px;background:var(--card);border:1px solid var(--border);border-radius:14px;padding:12px}
.diagram svg{width:100%;height:auto;display:block}
.diagram figcaption{font-size:0.78rem;color:var(--dim);text-align:center;margin-top:6px}
.diagram text{font-family:'Inter',system-ui,sans-serif;fill:var(--text);font-size:13px}
.diagram .title{font-size:15px;font-weight:600}
.diagram .lbl{font-weight:600}.diagram .big{font-size:14px}
.diagram .sub{font-size:11.5px;fill:var(--muted)}.diagram .small{font-size:12px}
.diagram .num{font-size:12.5px}.diagram .num.hl{font-weight:800}
.diagram .ink-fill{fill:var(--text)}
.diagram .leader{fill:none;stroke:var(--dim);stroke-width:1}.diagram .leader.thick{stroke-width:1.25}
.diagram .axis{fill:none;stroke:var(--dim);stroke-width:1.25}.diagram .axis-fill{fill:var(--dim)}
.diagram .bone{fill:var(--d-bone)}
.diagram .pdl{fill:none;stroke:var(--d-pdl);stroke-width:6;opacity:.75}
.diagram .dentine{fill:var(--d-dentine);stroke:var(--dim);stroke-width:1.25}
.diagram .enamel{fill:var(--d-enamel);stroke:var(--dim);stroke-width:1}
.diagram .pulp{fill:var(--d-pulp);stroke:var(--dim);stroke-width:1}
.diagram .gum{fill:var(--d-gum);stroke:var(--dim);stroke-width:1}
.diagram .tt{stroke:var(--dim);stroke-width:1;fill-opacity:.35}
.diagram .tt.inc{fill:var(--d-inc)}.diagram .tt.can{fill:var(--d-can)}.diagram .tt.pm{fill:var(--d-pm)}.diagram .tt.mol{fill:var(--d-mol)}
.diagram .tt.hl{stroke:var(--text);stroke-width:2.5}
.diagram .danger-zone{fill:var(--danger);fill-opacity:.08}
.diagram .crit{stroke:var(--danger);stroke-width:1.25;stroke-dasharray:5 4}
.diagram .curve{fill:none;stroke:var(--accent);stroke-width:2.5}
.diagram .danger{fill:var(--danger)}.diagram .ok{fill:var(--ok)}
.diagram .box{fill:var(--surface);stroke:var(--dim);stroke-width:1.25}
.diagram .box.acc{fill:var(--accent-bg);stroke:var(--accent);stroke-width:2}
.diagram .arrow{fill:none;stroke:var(--dim);stroke-width:1.25}.diagram .acc-stroke{stroke:var(--accent);stroke-width:2}
.diagram .whitespot{fill:#fff;stroke:var(--dim);stroke-width:1}
.diagram .lesion{fill:#8a5a2b;fill-opacity:.85}.diagram .hole{fill:var(--card)}
.diagram .pulp.inflamed{fill:var(--danger);fill-opacity:.8}
.diagram .gum.sore{fill:var(--d-gum-sore)}
.diagram .calculus{fill:#b8a36a;stroke:var(--dim);stroke-width:.75}
.diagram .probe{stroke:var(--text);stroke-width:2.5;stroke-linecap:round}
.diagram .depth{stroke:var(--accent);stroke-width:2}
.diagram .face{fill:none;stroke:var(--dim);stroke-width:1.5}
.diagram .feature{fill:none;stroke:var(--dim);stroke-width:1.25}.diagram .feature-line{fill:none;stroke:var(--dim);stroke-width:1.25}
.diagram .z1{fill:var(--d-inc);fill-opacity:.45}.diagram .z2{fill:var(--d-pm);fill-opacity:.45}.diagram .z3{fill:var(--d-can);fill-opacity:.45}.diagram .zc{fill:var(--dim);fill-opacity:.45}
.diagram .safe-zone{fill:var(--ok);fill-opacity:.15}.diagram .frame{fill:none;stroke:var(--dim);stroke-width:1.25}
.ref{font-size:0.7rem;color:var(--dim);margin-top:2px}
.bridge td{font-size:0.86rem}.bridge .pd{font-size:0.8rem;white-space:nowrap}
.bridge td a{font-weight:600;text-decoration:none}.bridge td a:hover{text-decoration:underline}
.hub-links{font-weight:600;font-size:0.9rem}
@media (max-width:540px){.bridge .pd{white-space:normal}}
.cta{display:flex;gap:10px;flex-wrap:wrap;margin-top:36px}
.btn{display:inline-flex;align-items:center;gap:6px;padding:11px 22px;border-radius:10px;font-size:0.88rem;font-weight:700;text-decoration:none}
.btn-quiz{background:var(--accent);color:#fff}
.btn-hub{background:var(--surface);color:var(--muted);border:1px solid var(--border)}
.btn-print{background:var(--surface);color:var(--muted);border:1px solid var(--border);cursor:pointer;font-family:inherit}
@media print{.topbar,.cta{display:none}body{background:#fff;color:#000}}
@media (max-width:540px){.topbar{padding:0 16px}h1{font-size:1.6rem}table{display:block;overflow-x:auto}}
"""
THEME_JS = "function toggleTheme(){const c=document.documentElement.getAttribute('data-theme')||'dark';const n=c==='dark'?'light':'dark';document.documentElement.setAttribute('data-theme',n);document.querySelector('.theme-btn').textContent=n==='dark'?'☀️':'🌙';try{localStorage.setItem('theme',n);}catch(e){}}\ntry{if(document.documentElement.getAttribute('data-theme')==='light')document.querySelector('.theme-btn').textContent='🌙';}catch(e){}"

for t in TOPICS:
    n = t["num"]
    body = t["notes"]
    if "diagram" in t:
        body = body.replace("{{DIAGRAM}}", DIAGRAMS[t["diagram"]]())
    body = re.sub(r"\{\{D:(\w+)\}\}", lambda m: DIAGRAMS[m.group(1)](), body)
    assert "{{" not in body, n
    t["ndiag"] = body.count('<figure class="diagram">')
    page = f"""<!doctype html>
{THEME_HEAD}
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Topic {n} Notes – {esc(t['title'])}</title>
{FONT}
<style>{NOTES_CSS}
:root{{--accent:{t['dark']};--accent-bg:{rgba(t['dark'],0.10)}}}
[data-theme="light"]{{--accent:{t['light']};--accent-bg:{rgba(t['light'],0.08)}}}
</style>
</head>
<body>
<div class="topbar">
  <div class="topbar-brand"><span>Topic {n}</span>{esc(t['short'])}</div>
  <div style="display:flex;align-items:center;gap:12px">
    <a class="back-link" href="../index.html">← Hub</a>
    <button class="theme-btn" onclick="toggleTheme()" aria-label="Toggle theme">☀️</button>
  </div>
</div>
<div class="container">
  <div class="eyebrow">Pre-Dentistry · Topic {n} · Summary notes</div>
  <h1>{esc(t['title'])}</h1>
  {body}
  <div class="cta">
    <a class="btn btn-quiz" href="../quizzes/topic{n}.html">Take the quiz →</a>
    <button class="btn btn-print" onclick="window.print()">Print / save as PDF</button>
    <a class="btn btn-hub" href="../index.html">← Hub</a>
  </div>
</div>
<script>{THEME_JS}</script>
</body>
</html>
"""
    open(f"{OUT}/notes/topic{n}.html", "w", encoding="utf-8").write(page)

# ---------- index ----------
fi = open(os.path.join(TPL, "index-template.html"), encoding="utf-8").read()
css = fi[fi.index("* { box-sizing"):fi.index("</style>")]
# drop the finance hub's per-topic rules; regenerate them for our topics
css = "\n".join(l for l in css.split("\n") if not re.match(r"\s*\.t\d+[ :]", l))
css = re.sub(r"\.btn-src \{.*?\}\n\.btn-src:hover \{.*?\}\n", "", css, flags=re.S)
dark_vars = "\n".join(f"  --t{t['num']}: {t['dark']}; --t{t['num']}-bg: {rgba(t['dark'],0.10)}; --t{t['num']}-glow: {rgba(t['dark'],0.20)};" for t in TOPICS)
light_vars = "\n".join(f"  --t{t['num']}: {t['light']}; --t{t['num']}-bg: {rgba(t['light'],0.08)}; --t{t['num']}-glow: {rgba(t['light'],0.15)};" for t in TOPICS)
root_dark = fi[fi.index(":root {"):fi.index("--t1:")] + dark_vars + "\n}\n"
_ls = fi.index(':root[data-theme="light"] {')
root_light = fi[_ls:fi.index("--t1-bg:", _ls)] + light_vars + "\n}\n"
per_topic = "\n".join(
    f".t{t['num']}:hover {{ box-shadow: 0 8px 32px var(--t{t['num']}-glow); }}\n"
    f".t{t['num']} .card-accent {{ background: var(--t{t['num']}); }}\n"
    f".t{t['num']} .topic-icon {{ background: var(--t{t['num']}-bg); color: var(--t{t['num']}); }}\n"
    f".t{t['num']} .btn-quiz {{ background: var(--t{t['num']}); }}" for t in TOPICS)
light_btn_text = ".t5 .btn-quiz, .t9 .btn-quiz { color: #000; }\n:root[data-theme=\"light\"] .t5 .btn-quiz, :root[data-theme=\"light\"] .t9 .btn-quiz { color: #fff; }"

QUIZ_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>'
DOC_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>'
cards = "\n".join(f"""
    <div class="topic-card t{t['num']}">
      <div class="card-accent"></div>
      <div class="card-body">
        <div class="card-header">
          <div class="topic-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">{t['icon']}</svg></div>
          <div class="card-meta">
            <div class="card-num">Topic {t['num']}{(' · %d diagram%s' % (t['ndiag'], '' if t['ndiag']==1 else 's')) if t['ndiag'] else ''}</div>
            <div class="card-title">{esc(t['title'])}</div>
          </div>
          <span class="score-badge" id="score-t{t['num']}"></span>
        </div>
        <div class="card-divider"></div>
        <p class="card-desc">{esc(t['blurb'])}</p>
        <div class="card-actions">
          <a class="btn btn-quiz" href="quizzes/topic{t['num']}.html">{QUIZ_ICON}Quiz</a>
          <a class="btn btn-doc" href="notes/topic{t['num']}.html">{DOC_ICON}Notes</a>
        </div>
      </div>
    </div>""" for t in TOPICS)
nq = sum(len(t["qs"]) for t in TOPICS)
ids = ",".join(f"'{t['num']}'" for t in TOPICS)

index = f"""<!doctype html>
{THEME_HEAD}
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pre-Dentistry Study Hub</title>
<meta name="description" content="Revision hub for students starting a UK dentistry (BDS) degree: notes, diagrams and quizzes.">
<link rel="preconnect" href="https://fonts.googleapis.com">
{FONT}
<style>
{root_dark}{root_light}{css}
{per_topic}
{light_btn_text}
</style>
</head>
<body>

<div class="topbar">
  <div class="topbar-brand"><span>BDS · Year 0</span>Pre-Dentistry Study Hub</div>
  <div class="topbar-right">
    <a class="home-link" href="{LANDING}">← All subjects</a>
    <button class="theme-btn" onclick="toggleTheme()" aria-label="Toggle theme">☀️</button>
  </div>
</div>

<div class="hero">
  <div class="hero-eyebrow">Before you start Dentistry · UK</div>
  <h1>Pre-Dentistry<br><em>Study Hub</em></h1>
  <p class="hero-sub">{len(TOPICS)} topics · 10 questions drawn from a pool of 22 · Notes and diagrams for every topic.</p>
  <div class="stats-strip">
    <div class="stat-cell"><div class="stat-num">{len(TOPICS)}</div><div class="stat-label">Topics</div></div>
    <div class="stat-cell"><div class="stat-num">{nq}</div><div class="stat-label">Questions</div></div>
    <div class="stat-cell"><div class="stat-num">{sum(t['ndiag'] for t in TOPICS)}</div><div class="stat-label">Diagrams</div></div>
  </div>
</div>

<div class="main">
  <div class="section-head"><div class="section-head-label">Suggested order</div><div class="section-head-line"></div></div>
  <div class="grid">{cards}
  </div>
</div>

<div class="footer">
  <strong>Pre-Dentistry Study Hub</strong> &nbsp;·&nbsp; For students starting a UK BDS &nbsp;·&nbsp; Facts checked October 2026; always follow your dental school's guidance
</div>

<script>
function toggleTheme() {{
  const cur = document.documentElement.getAttribute('data-theme') || 'dark';
  const next = cur === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  try {{ localStorage.setItem('theme', next); }} catch (e) {{}}
  document.querySelector('.theme-btn').textContent = next === 'dark' ? '☀️' : '🌙';
}}
try {{ if (document.documentElement.getAttribute('data-theme') === 'light') document.querySelector('.theme-btn').textContent = '🌙'; }} catch (e) {{}}
function loadScores(){{
  [{ids}].forEach(function(t){{
    try{{
      var d=JSON.parse(localStorage.getItem('topic'+t+'_last')||'null');
      var el=document.getElementById('score-t'+t);
      if(d&&el){{el.textContent=d.score+'/'+d.total;el.className='score-badge '+(d.pct>=60?'pass':'fail');el.style.display='inline-block';}}
    }}catch(e){{}}
  }});
}}
loadScores();
</script>
</body>
</html>
"""
open(f"{OUT}/index.html", "w", encoding="utf-8").write(index)

readme = f"""# Pre-Dentistry Study Hub

Revision hub for a student starting a UK dentistry (BDS) degree: {len(TOPICS)} topics, {nq} quiz questions, notes and diagrams.
Same design and quiz engine as the A-level finance hub. Netlify serves the repo root; the HTML is generated by `src/build.py`.

**Claude sessions: read `HANDOVER.md` first.**

## Structure
- `index.html` – hub homepage (topic cards, last-score badges)
- `quizzes/topicN.html` – quiz: 10 of 22 questions per session, options shuffled, 60s timer toggle, retry missed, keyboard 1–4 / Enter
- `notes/topicN.html` – summary notes with diagrams; printable to PDF
- `src/` – content, diagrams and the build script (edit here, never the generated HTML)

## Topics
""" + "\n".join(f"{t['num']}. {t['title']}" for t in TOPICS) + """

## Rebuild after editing src/
```bash
cd ~/Documents/Projects/pre-dentistry-study-guide
python3 src/build.py
```

## Deploy
```bash
cd ~/Documents/Projects/pre-dentistry-study-guide
git add -A
git commit -m "Update hub"
git push
```
Netlify redeploys automatically on push to `main`.
"""
open(f"{OUT}/README.md", "w", encoding="utf-8").write(readme)
print("built", len(TOPICS), "topics,", nq, "questions ->", OUT)
