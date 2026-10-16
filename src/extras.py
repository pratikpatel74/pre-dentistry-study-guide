"""Progress page (progress.html) and Year 12 study plan (plan.html).
Both read/write browser localStorage only; nothing leaves the device.
Storage keys:
  topicN_hist   – list of {score,total,pct,date,retry} (quiz engine, last 50)
  topicN_last / topicN_missed – existing quiz keys (used as fallbacks)
  ucat_<id>_hist – list of {date,set,sections:[{name,key,got,max}]} (UCAT engine, last 50)
  ucat_<id>_last – existing key (fallback)
  plan_done     – list of ticked week numbers on the study plan
"""
import datetime as dt
import html
import json

PAGE_CSS = """
.strip{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:18px 0 8px}
.cell{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:14px 16px}
.cell .n{font-size:1.6rem;font-weight:800;line-height:1.1}
.cell .l{font-size:0.72rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--dim);margin-top:4px}
.muted{color:var(--muted)}
.focus{display:flex;align-items:center;justify-content:space-between;gap:12px;background:var(--card);border:1px solid var(--border);border-left:4px solid var(--danger);border-radius:10px;padding:12px 14px;margin-bottom:8px}
.focus .t{font-weight:700}
.focus .s{font-size:0.82rem;color:var(--muted)}
.focus .acts{display:flex;gap:6px;flex-shrink:0}
.mini{display:inline-block;padding:6px 12px;border-radius:8px;font-size:0.78rem;font-weight:700;text-decoration:none;border:1px solid var(--border);background:var(--surface);color:var(--text)}
.mini.pri{background:var(--accent);border-color:var(--accent);color:#000}
[data-theme="light"] .mini.pri{color:#fff}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0 10px}
.chip{font-size:0.78rem;padding:4px 10px;border-radius:999px;border:1px solid var(--border);background:var(--surface);color:var(--muted);text-decoration:none}
.sbar{display:flex;align-items:center;gap:12px;margin:8px 0}
.sbar .nm{width:200px;font-size:0.88rem;font-weight:600}
.sbar .tr{flex:1;height:10px;background:var(--surface);border:1px solid var(--border);border-radius:6px;overflow:hidden}
.sbar .tr i{display:block;height:100%;background:var(--accent)}
.sbar .v{width:80px;text-align:right;font-size:0.85rem}
.weak{color:var(--danger);font-weight:700;font-size:0.72rem;letter-spacing:0.08em;text-transform:uppercase;margin-left:6px}
td.num,th.num{text-align:right;white-space:nowrap}
.spark rect.hi{fill:var(--ok)}
.spark rect.lo{fill:var(--danger)}
.spark rect.mid{fill:var(--gold)}
.tablewrap{overflow-x:auto}
.toolsrow{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}
button.mini{cursor:pointer;font-family:inherit}
@media (max-width:540px){.sbar .nm{width:110px;font-size:0.8rem}.focus{flex-direction:column;align-items:flex-start}.hide-sm{display:none}}
"""

TOPBAR = """<div class="topbar">
  <div class="topbar-brand"><span>{tag}</span>{name}</div>
  <div style="display:flex;align-items:center;gap:12px">
    <a class="back-link" href="index.html">← Hub</a>
    <button class="theme-btn" onclick="toggleTheme()" aria-label="Toggle theme">☀️</button>
  </div>
</div>"""


def _page(THEME_HEAD, FONT, NOTES_CSS, THEME_JS, title, accent, body, script, extra_css=""):
    return f"""<!doctype html>
{THEME_HEAD}
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} – Pre-Dentistry Study Hub</title>
{FONT}
<style>{NOTES_CSS}
:root{{--accent:{accent[0]};--accent-bg:{accent[1]}}}
[data-theme="light"]{{--accent:{accent[2]};--accent-bg:{accent[3]}}}
{PAGE_CSS}{extra_css}
</style>
</head>
<body>
{body}
<script>{THEME_JS}
{script}
</script>
</body>
</html>
"""


# ======================================================================= progress
def build_progress(OUT, THEME_HEAD, FONT, NOTES_CSS, THEME_JS, TOPICS, UCAT_META):
    topics = [{"n": t["num"], "label": t["label"], "short": t["short"], "section": t["section"]} for t in TOPICS]
    order = ["mock", "timed-vr", "timed-dm", "timed-qr", "timed-sjt", "drill-vr", "drill-dm", "drill-qr", "drill-sjt"]
    sets = [{"id": k, "title": UCAT_META[k][0], "kind": UCAT_META[k][1]} for k in order]
    body = TOPBAR.format(tag="Tracker", name="My progress") + """
<div class="container">
  <div class="eyebrow">Pre-Dentistry Study Hub · Progress</div>
  <h1>My progress</h1>
  <p class="lead">Every quiz and UCAT practice session you finish on this device is recorded here, so you can see what's improving and what to revise next.</p>
  <div class="strip" id="strip"></div>

  <h2>Revise next</h2>
  <p class="muted" style="font-size:0.88rem">Topics where your recent quiz average (last 3 sessions) is below 80%, weakest first.</p>
  <div id="focus"></div>
  <div id="unstarted"></div>

  <h2>UCAT by subtest</h2>
  <p class="muted" style="font-size:0.88rem">Average of your last 5 sessions in each subtest, across drills, timed sets and mocks. Raw marks, not scaled scores.</p>
  <div id="subtests"></div>

  <h2>Quiz history by topic</h2>
  <div class="tablewrap"><table id="ttable"></table></div>

  <h2>UCAT practice history</h2>
  <div class="tablewrap"><table id="utable"></table></div>

  <h2>Your data</h2>
  <p class="muted" style="font-size:0.88rem">Scores are saved in this browser only. Export a backup to move them to another device or browser, then import it there.</p>
  <div class="toolsrow">
    <button class="mini" onclick="exportData()">Export backup</button>
    <label class="mini" style="cursor:pointer">Import backup<input type="file" accept="application/json" style="display:none" onchange="importData(this)"></label>
    <button class="mini" id="reset-btn" onclick="resetData(this)">Reset all scores</button>
  </div>
  <p class="muted" id="data-msg" style="font-size:0.85rem;margin-top:8px"></p>

  <div class="cta"><a class="btn btn-quiz" href="plan.html">Study plan →</a><a class="btn btn-hub" href="ucat/index.html">UCAT practice</a><a class="btn btn-hub" href="index.html">← Hub</a></div>
</div>"""
    script = """
const TOPICS = %s;
const SETS = %s;
const SUB = {vr:'Verbal Reasoning',dm:'Decision Making',qr:'Quantitative Reasoning',sjt:'Situational Judgement'};
function J(k,d){try{const v=localStorage.getItem(k);return v?JSON.parse(v):d;}catch(e){return d;}}
function qhist(n){let h=J('topic'+n+'_hist',null);if(!h){const l=J('topic'+n+'_last',null);h=l?[l]:[];}return h;}
function uhist(id){let h=J('ucat_'+id+'_hist',null);if(!h){const l=J('ucat_'+id+'_last',null);h=l?[l]:[];}return h;}
function upct(r){let g=0,m=0;r.sections.forEach(s=>{g+=s.got;m+=s.max;});return m?Math.round(100*g/m):0;}
function avg(a){return a.length?Math.round(a.reduce((x,y)=>x+y,0)/a.length):null;}
function d(s){try{return new Date(s).toLocaleDateString('en-GB',{day:'numeric',month:'short'});}catch(e){return '';}}
function spark(vals){const v=vals.slice(-10);if(!v.length)return '';const w=8,g=3,H=24;
  return '<svg class="spark" width="'+(v.length*(w+g))+'" height="'+H+'" viewBox="0 0 '+(v.length*(w+g))+' '+H+'" role="img" aria-label="last '+v.length+' scores">'+
  v.map((p,i)=>{const h=Math.max(2,Math.round(H*p/100));return '<rect class="'+(p>=80?'hi':p>=60?'mid':'lo')+'" x="'+(i*(w+g))+'" y="'+(H-h)+'" width="'+w+'" height="'+h+'" rx="1.5"><title>'+p+'%%</title></rect>';}).join('')+'</svg>';}
function render(){
  const T = TOPICS.map(t=>{const h=qhist(t.n);const main=h.filter(r=>!r.retry);const p=h.map(r=>r.pct);
    const recent=avg((main.length?main:h).slice(-3).map(r=>r.pct));
    return Object.assign({},t,{h,p,recent,latest:p.length?p[p.length-1]:null,best:p.length?Math.max(...p):null,missed:(J('topic'+t.n+'_missed',[])||[]).length});});
  const U = SETS.map(s=>{const h=uhist(s.id);const p=h.map(upct);return Object.assign({},s,{h,p,latest:p.length?p[p.length-1]:null,best:p.length?Math.max(...p):null});});
  const tried=T.filter(t=>t.h.length), quizzes=T.reduce((a,t)=>a+t.h.length,0), usess=U.reduce((a,s)=>a+s.h.length,0);
  const avgLatest=avg(tried.map(t=>t.latest));
  document.getElementById('strip').innerHTML=[
    [tried.length+'<span class="muted" style="font-size:1rem">/'+T.length+'</span>','Topics tried'],
    [avgLatest===null?'–':avgLatest+'%%','Average latest quiz'],
    [quizzes,'Quizzes taken'],[usess,'UCAT sessions']].map(c=>'<div class="cell"><div class="n">'+c[0]+'</div><div class="l">'+c[1]+'</div></div>').join('');
  const weak=tried.filter(t=>t.recent<80).sort((a,b)=>a.recent-b.recent).slice(0,6);
  document.getElementById('focus').innerHTML = !tried.length ? '<p class="muted">No quizzes yet. Take any topic quiz from the hub and your scores will appear here.</p>' :
    !weak.length ? '<div class="callout">All the topics you have tried are averaging 80%% or more. Try a topic you haven\\'t started, or move on to timed UCAT sets.</div>' :
    weak.map(t=>'<div class="focus"><div><div class="t">'+t.label+' · '+t.short+'</div><div class="s">Recent average '+t.recent+'%% over '+Math.min(3,t.h.length)+' session'+(t.h.length>1?'s':'')+(t.missed?' · '+t.missed+' missed question'+(t.missed>1?'s':'')+' to retry':'')+'</div></div>'+
      '<div class="acts"><a class="mini" href="notes/topic'+t.n+'.html">Notes</a>'+(t.missed?'<a class="mini" href="quizzes/topic'+t.n+'.html?retry=missed">Retry missed</a>':'')+'<a class="mini pri" href="quizzes/topic'+t.n+'.html">Quiz</a></div></div>').join('');
  const un=T.filter(t=>!t.h.length);
  document.getElementById('unstarted').innerHTML = un.length && tried.length ? '<p class="muted" style="font-size:0.85rem;margin-top:14px">Not started yet:</p><div class="chips">'+un.map(t=>'<a class="chip" href="quizzes/topic'+t.n+'.html">'+t.label+' · '+t.short+'</a>').join('')+'</div>' : '';
  // subtests
  const per={vr:[],dm:[],qr:[],sjt:[]};
  U.forEach(s=>s.h.forEach(r=>r.sections.forEach(x=>{if(per[x.key]&&x.max)per[x.key].push({date:r.date,p:Math.round(100*x.got/x.max)});})));
  const sv=Object.keys(per).map(k=>{const a=per[k].sort((x,y)=>x.date<y.date?-1:1).slice(-5).map(x=>x.p);return {k,v:avg(a),n:per[k].length};});
  const have=sv.filter(x=>x.v!==null); const low=have.length>1?have.reduce((a,b)=>b.v<a.v?b:a):null;
  document.getElementById('subtests').innerHTML = !have.length ? '<p class="muted">No UCAT practice yet. Start with the <a href="ucat/index.html">untimed drills</a>.</p>' :
    sv.map(x=>'<div class="sbar"><div class="nm">'+SUB[x.k]+(low&&low.k===x.k?'<span class="weak">Weakest</span>':'')+'</div><div class="tr"><i style="width:'+(x.v||0)+'%%"></i></div><div class="v">'+(x.v===null?'<span class="muted">–</span>':'<b>'+x.v+'%%</b> <span class="muted" style="font-size:0.75rem">('+x.n+')</span>')+'</div></div>').join('');
  // tables
  document.getElementById('ttable').innerHTML='<tr><th>Topic</th><th class="num">Tries</th><th class="num">Latest</th><th class="num hide-sm">Best</th><th>Last 10</th><th class="hide-sm">Last</th></tr>'+
    T.map(t=>'<tr><td><a href="quizzes/topic'+t.n+'.html">'+t.label+'</a> · '+t.short+'</td><td class="num">'+t.h.length+'</td><td class="num">'+(t.latest===null?'–':'<b>'+t.latest+'%%</b>')+'</td><td class="num hide-sm">'+(t.best===null?'–':t.best+'%%')+'</td><td>'+spark(t.p)+'</td><td class="hide-sm muted">'+(t.h.length?d(t.h[t.h.length-1].date):'')+'</td></tr>').join('');
  document.getElementById('utable').innerHTML='<tr><th>Practice set</th><th class="num">Tries</th><th class="num">Latest</th><th class="num hide-sm">Best</th><th>Last 10</th><th class="hide-sm">Last</th></tr>'+
    U.map(s=>'<tr><td><a href="ucat/'+s.id+'.html">'+s.title+'</a></td><td class="num">'+s.h.length+'</td><td class="num">'+(s.latest===null?'–':'<b>'+s.latest+'%%</b>')+'</td><td class="num hide-sm">'+(s.best===null?'–':s.best+'%%')+'</td><td>'+spark(s.p)+'</td><td class="hide-sm muted">'+(s.h.length?d(s.h[s.h.length-1].date):'')+'</td></tr>').join('');
}
function ourKeys(){const k=[];try{for(let i=0;i<localStorage.length;i++){const x=localStorage.key(i);if(/^(topic\\d+_|ucat_|plan_)/.test(x))k.push(x);}}catch(e){}return k;}
function msg(t){document.getElementById('data-msg').textContent=t;}
function exportData(){const o={};ourKeys().forEach(k=>{o[k]=localStorage.getItem(k);});
  const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([JSON.stringify({hub:'pre-dentistry',saved:new Date().toISOString(),data:o},null,1)],{type:'application/json'}));
  a.download='pre-dentistry-progress-'+new Date().toISOString().slice(0,10)+'.json';document.body.appendChild(a);a.click();a.remove();msg('Backup downloaded.');}
function importData(inp){const f=inp.files[0];if(!f)return;const r=new FileReader();r.onload=()=>{try{const o=JSON.parse(r.result);if(o.hub!=='pre-dentistry')throw 0;
  let n=0;Object.entries(o.data).forEach(([k,v])=>{if(/^(topic\\d+_|ucat_|plan_)/.test(k)){localStorage.setItem(k,v);n++;}});msg('Imported '+n+' saved items.');render();}catch(e){msg('That file isn\\'t a Pre-Dentistry Hub backup.');}};r.readAsText(f);}
function resetData(b){if(!b.dataset.armed){b.dataset.armed='1';b.textContent='Click again to delete all scores';setTimeout(()=>{delete b.dataset.armed;b.textContent='Reset all scores';},4000);return;}
  ourKeys().filter(k=>!/_timer$/.test(k)).forEach(k=>{try{localStorage.removeItem(k);}catch(e){}});delete b.dataset.armed;b.textContent='Reset all scores';msg('All scores cleared.');render();}
render();
""" % (json.dumps(topics, ensure_ascii=False), json.dumps(sets, ensure_ascii=False))
    page = _page(THEME_HEAD, FONT, NOTES_CSS, THEME_JS, "My progress",
                 ("#e8b84b", "rgba(232,184,75,0.10)", "#b8861a", "rgba(184,134,26,0.08)"), body, script)
    open(f"{OUT}/progress.html", "w", encoding="utf-8").write(page)


# ======================================================================= study plan
START = dt.date(2026, 10, 19)      # first Monday after the plan was written
END = dt.date(2027, 10, 11)        # week containing the UCAS deadline (15 Oct in recent years)

# (first Monday, name, colour key, summary, weekly routine)
PHASES = [
    (dt.date(2026, 10, 19), "Groundwork", "p1",
     "Year 12 grades come first: they drive your predicted grades. Learn what the UCAT is, line up work experience and start a regular volunteering role.",
     "A-levels as normal · UCAT: one 20–30 minute untimed drill a week · one application task a week"),
    (dt.date(2026, 12, 21), "Christmas break", "hol",
     "Rest, catch up on A-level work and keep UCAT ticking over.",
     "One drill and one reading task a week"),
    (dt.date(2027, 1, 4), "Build the skills", "p2",
     "Learn every UCAT question type properly with untimed drills, using New set for fresh Decision Making and Quantitative Reasoning questions.",
     "UCAT: two 30-minute sessions a week · quick mental maths and fast reading on other days"),
    (dt.date(2027, 3, 29), "Easter", "hol",
     "Ideal time for dental work experience. Check the UCAT 2027 dates and register when it opens.",
     "Work experience if booked · first timed sets"),
    (dt.date(2027, 4, 12), "Timed practice", "p3",
     "Move to timed sets at real pace. Review every mistake: the review is where the marks come from.",
     "UCAT: three timed sets a week, plus a review of mistakes"),
    (dt.date(2027, 5, 24), "Exam season", "p4",
     "Year 12 exams matter for your predictions, so UCAT drops to maintenance. Book your test date if you haven't already.",
     "UCAT: one or two timed sets a week · revise for exams"),
    (dt.date(2027, 7, 5), "UCAT intensive", "p5",
     "Four to five weeks of daily practice: full mocks and the official UCAT practice tests. Sit the test in late July or early August so September is free for your application.",
     "UCAT: 45–90 minutes a day, 5–6 days a week · one full mock a week"),
    (dt.date(2027, 8, 9), "Application", "p6",
     "Use your UCAT result to choose four dental schools, finish the personal statement and submit before the deadline. Start interview practice.",
     "Personal statement drafts · school research · interview practice from September"),
]

ROT = ["Verbal Reasoning", "Decision Making", "Quantitative Reasoning", "Situational Judgement"]
SLUG = {"Verbal Reasoning": "vr", "Decision Making": "dm", "Quantitative Reasoning": "qr", "Situational Judgement": "sjt"}

def _u(kind, sub):
    s = SLUG[sub]
    return f'<a href="ucat/{kind}-{s}.html">{sub} {"drill" if kind == "drill" else "timed set"}</a>'

# Week-specific tasks, keyed by Monday. Each value: (ucat task or None for the phase default, other task)
SPECIFIC = {
    "2026-10-19": (None, 'Read <a href="notes/topic14.html">Step 1: Route to 2028</a> and take its quiz'),
    "2026-10-26": (None, 'Read <a href="notes/topic15.html">Step 2: UCAT</a> notes; look at the official UCAT site'),
    "2026-11-02": (None, 'Read <a href="notes/topic17.html">Step 4: Experience &amp; statement</a>; list 10 local dental practices'),
    "2026-11-09": (None, "Email or write to practices asking for Easter or summer work experience"),
    "2026-11-16": (None, "Find a weekly volunteering or caring role (care home, charity, St John Ambulance, school mentoring)"),
    "2026-11-23": (None, "Start a reflective diary: one entry per placement or volunteering session"),
    "2026-11-30": (None, "Follow up practices that haven't replied; try a hospital or community dental service"),
    "2026-12-07": (None, 'Read <a href="notes/topic1.html">Topic 1: UK dental landscape</a> and take its quiz'),
    "2026-12-14": (None, "Review your term: grades, any work experience booked, diary started?"),
    "2026-12-21": (_u("drill", "Situational Judgement"), 'Read <a href="notes/topic8.html">Topic 8: Professionalism &amp; ethics</a>'),
    "2026-12-28": (_u("drill", "Verbal Reasoning"), "Read one long article (news or science) and summarise it in 3 lines"),
    "2027-01-04": (None, 'Read <a href="notes/topic16.html">Step 3: Interviews</a> to see what schools look for'),
    "2027-01-11": (None, "List dental schools and their entry requirements (A-levels, GCSEs, UCAT use)"),
    "2027-01-18": (None, 'Read <a href="notes/topic4.html">Topic 4: Caries</a>; good material for interview questions'),
    "2027-01-25": (None, "Diary: write up anything you've done since Christmas"),
    "2027-02-01": (None, "Check open-day dates for spring and summer 2027; book the ones you can reach"),
    "2027-02-08": (None, 'Read <a href="notes/topic2.html">Topic 2: Tooth anatomy</a> and take its quiz'),
    "2027-02-15": ("Half term: try one timed set in each subtest (Untimed mode is fine)", "Practise manual dexterity: a hobby you can talk about (model-making, an instrument, sewing)"),
    "2027-02-22": (None, "Read a recent news story about NHS dentistry; note two points for interviews"),
    "2027-03-01": (None, 'Read <a href="notes/topic7.html">Topic 7: Infection control</a>'),
    "2027-03-08": (None, "Confirm Easter work experience details: dates, dress code, contact name"),
    "2027-03-15": (None, "Check your progress page: which topics and subtests are weakest?"),
    "2027-03-22": (None, "Prepare questions to ask the dental team during work experience"),
    "2027-03-29": (_u("timed", "Verbal Reasoning") + " and " + _u("timed", "Quantitative Reasoning"), "Work experience; diary entry every day"),
    "2027-04-05": (_u("timed", "Decision Making") + " and " + _u("timed", "Situational Judgement"), "Check UCAT 2027 test dates and registration; register when it opens"),
    "2027-04-12": (None, "Book your UCAT slot as soon as booking opens (aim for late July or early August)"),
    "2027-04-19": (None, "Diary: reflect on Easter work experience: what you saw, learned, and how it confirmed dentistry"),
    "2027-04-26": (None, 'Read <a href="notes/topic12.html">Topic 12: Oral pathology</a>'),
    "2027-05-03": (None, "Shortlist 6–8 dental schools; note which use UCAT heavily"),
    "2027-05-10": (None, "Keep volunteering going: consistency over months counts"),
    "2027-05-17": ("Full UCAT mock, then review your two weakest subtests", "Plan exam revision for the next six weeks"),
    "2027-05-24": (None, "Exam revision"),
    "2027-05-31": (None, "Exam revision (half term)"),
    "2027-06-07": (None, "Exams"),
    "2027-06-14": (None, "Exams"),
    "2027-06-21": (None, "Open days: go to at least two if you can"),
    "2027-06-28": (None, "Write a rough first draft of each personal statement answer (no editing yet)"),
    "2027-07-05": ('<a href="ucat/mock.html">Full mock</a> + review; daily timed sets in your weakest subtest', "Summer work experience or volunteering if booked"),
    "2027-07-12": ('<a href="https://www.ucat.ac.uk/prepare/practice-tests/" target="_blank" rel="noopener">Official practice test A</a> + review; daily drills on weak question types', "Keep the diary going"),
    "2027-07-19": ('<a href="ucat/mock.html">Full mock</a> (New set) + official practice test B', "Re-read your personal statement draft once; note gaps"),
    "2027-07-26": ("Official practice tests C and D; light timed sets", "Prepare for test day: ID, route, timings"),
    "2027-08-02": ("Test week: short warm-ups only, sleep well, sit the UCAT", "Rest after the test"),
    "2027-08-09": ("UCAT done", "Compare your score with each school's past cut-offs; pick 4 dental schools and a 5th choice"),
    "2027-08-16": ("UCAT done", "Personal statement draft 2; ask a teacher to read it"),
    "2027-08-23": ("UCAT done", "Register on UCAS Hub; fill in the non-statement sections"),
    "2027-08-30": ("UCAT done", "Year 13 starts: confirm your referee and when they need your draft"),
    "2027-09-06": ("UCAT done", 'Personal statement final edits (4,000 characters, 3 answers); start <a href="notes/topic16.html">interview practice</a>'),
    "2027-09-13": ("UCAT done", "Final checks with your school; aim to submit by the end of September"),
    "2027-09-20": ("UCAT done", "Submit to UCAS if ready; practise one MMI station a week"),
    "2027-09-27": ("UCAT done", "Interview practice: ethics scenarios and 'Why dentistry?'"),
    "2027-10-04": ("UCAT done", "Interview practice; keep up volunteering and A-level work"),
    "2027-10-11": ("UCAT done", "UCAS deadline week (15 October in recent years, 6pm). Don't leave it to the last day"),
}


def _phase(d):
    cur = PHASES[0]
    for p in PHASES:
        if d >= p[0]:
            cur = p
    return cur


def _default_ucat(i, ph):
    sub = ROT[i % 4]
    key = ph[2]
    if key == "p1":
        return _u("drill", sub)
    if key == "p2":
        return _u("drill", sub) + " ×2 (use New set)" if sub in ("Decision Making", "Quantitative Reasoning") else _u("drill", sub) + " + revisit any drill you scored under 70%"
    if key == "p3":
        return _u("timed", sub) + " ×2 + one timed set in another subtest; review mistakes"
    if key == "p4":
        return _u("timed", sub) + " (maintenance)"
    return _u("timed", sub)


def build_plan(OUT, THEME_HEAD, FONT, NOTES_CSS, THEME_JS):
    weeks = []
    d, i = START, 0
    while d <= END:
        ph = _phase(d)
        spec = SPECIFIC.get(d.isoformat())
        assert spec, f"no plan for week of {d}"
        ucat = spec[0] or _default_ucat(i, ph)
        weeks.append((i + 1, d, ph, ucat, spec[1]))
        d += dt.timedelta(days=7); i += 1
    assert set(SPECIFIC) == {w[1].isoformat() for w in weeks}, "SPECIFIC has dates outside the plan"

    phase_cards = []
    for k, p in enumerate(PHASES):
        nxt = PHASES[k + 1][0] - dt.timedelta(days=1) if k + 1 < len(PHASES) else END + dt.timedelta(days=6)
        phase_cards.append(f'<div class="ph {p[2]}"><div class="pd">{p[0].strftime("%-d %b %Y")} – {nxt.strftime("%-d %b %Y")}</div>'
                           f'<div class="pn">{p[1]}</div><p>{p[3]}</p><div class="pr"><b>Each week:</b> {p[4]}</div></div>')

    rows, last_ph = [], None
    for n, d, ph, ucat, other in weeks:
        if ph is not last_ph:
            rows.append(f'<div class="phhead {ph[2]}">{ph[1]}</div>')
            last_ph = ph
        rows.append(f'<div class="wk" id="w{n}" data-mon="{d.isoformat()}"><label class="tick"><input type="checkbox" data-w="{n}" aria-label="Week {n} done"></label>'
                    f'<div class="wd"><b>Week {n}</b><span>{d.strftime("%-d %b %Y")}</span></div>'
                    f'<div class="wt"><div><span class="tg">UCAT</span>{ucat}</div><div><span class="tg o">Also</span>{other}</div></div></div>')

    body = TOPBAR.format(tag="Plan", name="Year 12 study plan") + f"""
<div class="container wide">
  <div class="eyebrow">Getting in · Year 12 to 2028 entry · Study plan</div>
  <h1>Year 12 study plan</h1>
  <p class="lead">Week by week from October 2026 to the UCAS deadline in October 2027: untimed drills, then timed sets, then full mocks and the official UCAT practice tests, around A-level work and your application.</p>
  <div class="callout"><b>Keep it realistic.</b> A-level grades matter more than anything else this year, so UCAT stays small until the summer. Swap weeks around to fit your school's holidays and exams; the order matters more than the dates. Dates for UCAT 2027 and UCAS 2028 entry are published in spring 2027, so check them then.</div>
  <div class="now" id="now"></div>

  <h2>The phases</h2>
  <div class="phases">{''.join(phase_cards)}</div>

  <h2>Week by week</h2>
  <p class="muted" style="font-size:0.88rem">Tick each week when it's done; ticks are saved in this browser. <span id="donecount"></span></p>
  <div class="weeks">{''.join(rows)}</div>

  <div class="cta"><a class="btn btn-quiz" href="ucat/index.html">UCAT practice →</a><a class="btn btn-hub" href="progress.html">My progress</a><a class="btn btn-print" onclick="window.print()" href="#">Print</a><a class="btn btn-hub" href="index.html">← Hub</a></div>
</div>"""
    css = """
.container.wide{max-width:860px}
.now{margin:16px 0 0}
.now a{font-weight:700}
.phases{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:10px}
.ph{background:var(--card);border:1px solid var(--border);border-top:4px solid var(--pc);border-radius:10px;padding:12px 14px}
.ph .pd{font-size:0.72rem;color:var(--dim);letter-spacing:0.06em;text-transform:uppercase}
.ph .pn{font-weight:800;margin:2px 0 6px;color:var(--pc)}
.ph p{font-size:0.85rem;margin:0 0 8px}
.ph .pr{font-size:0.8rem;color:var(--muted)}
.p1{--pc:#60a5fa}.p2{--pc:#34d399}.p3{--pc:#e8b84b}.p4{--pc:#a78bfa}.p5{--pc:#f87171}.p6{--pc:#38bdf8}.hol{--pc:#8b8aab}
[data-theme="light"] .p1{--pc:#2563eb}[data-theme="light"] .p2{--pc:#059669}[data-theme="light"] .p3{--pc:#b8861a}[data-theme="light"] .p4{--pc:#7c3aed}[data-theme="light"] .p5{--pc:#dc2626}[data-theme="light"] .p6{--pc:#0284c7}[data-theme="light"] .hol{--pc:#706c60}
.phhead{margin:22px 0 8px;font-size:0.72rem;font-weight:800;letter-spacing:0.14em;text-transform:uppercase;color:var(--pc)}
.wk{display:flex;gap:12px;align-items:flex-start;background:var(--card);border:1px solid var(--border);border-radius:10px;padding:10px 12px;margin-bottom:6px;scroll-margin-top:80px}
.wk.done{opacity:0.55}
.wk.cur{border-color:var(--accent);box-shadow:0 0 0 2px var(--accent-bg)}
.tick input{width:18px;height:18px;margin-top:3px;accent-color:var(--accent);cursor:pointer}
.wd{width:96px;flex-shrink:0;display:flex;flex-direction:column;font-size:0.85rem}
.wd span{font-size:0.75rem;color:var(--muted)}
.wt{flex:1;font-size:0.86rem;display:flex;flex-direction:column;gap:4px}
.tg{display:inline-block;min-width:44px;font-size:0.62rem;font-weight:800;letter-spacing:0.1em;text-transform:uppercase;color:var(--accent);margin-right:6px}
.tg.o{color:var(--muted)}
.btn-print{background:var(--surface);color:var(--muted);border:1px solid var(--border)}
@media (max-width:540px){.wk{flex-wrap:wrap}.wd{width:auto;flex-direction:row;gap:8px;align-items:baseline}.wt{flex-basis:100%}}
@media print{.tick,.now{display:none}.wk{break-inside:avoid}}
"""
    script = """
function J(k,d){try{const v=localStorage.getItem(k);return v?JSON.parse(v):d;}catch(e){return d;}}
let done=new Set(J('plan_done',[]));
function paint(){document.querySelectorAll('.wk').forEach(w=>{const n=+w.id.slice(1);w.classList.toggle('done',done.has(n));w.querySelector('input').checked=done.has(n);});
  document.getElementById('donecount').textContent=done.size?done.size+' of '+document.querySelectorAll('.wk').length+' weeks ticked.':'';}
document.querySelectorAll('.wk input').forEach(i=>i.addEventListener('change',()=>{const n=+i.dataset.w;if(i.checked)done.add(n);else done.delete(n);
  try{localStorage.setItem('plan_done',JSON.stringify([...done].sort((a,b)=>a-b)));}catch(e){}paint();}));
(function(){const today=new Date();today.setHours(0,0,0,0);const ws=[...document.querySelectorAll('.wk')];let cur=null;
  ws.forEach(w=>{const m=new Date(w.dataset.mon+'T00:00:00');const e=new Date(m);e.setDate(e.getDate()+7);if(today>=m&&today<e)cur=w;});
  const el=document.getElementById('now');
  if(cur){cur.classList.add('cur');el.innerHTML='This week is <a href="#'+cur.id+'">'+cur.querySelector('.wd b').textContent+'</a>.';}
  else if(ws.length&&today<new Date(ws[0].dataset.mon)){el.innerHTML='The plan starts on <a href="#w1">'+ws[0].querySelector('.wd span').textContent+'</a>.';}
  else el.innerHTML='The plan has finished. Good luck with interviews!';})();
paint();
"""
    page = _page(THEME_HEAD, FONT, NOTES_CSS, THEME_JS, "Year 12 study plan",
                 ("#38bdf8", "rgba(56,189,248,0.10)", "#0284c7", "rgba(2,132,199,0.08)"), body, script, css)
    open(f"{OUT}/plan.html", "w", encoding="utf-8").write(page)
    return len(weeks)
