"""Builds ucat/ practice pages: 4 untimed drills, 4 timed subtest sets and a full-length mock.
Called from build.py: build_ucat(OUT, LANDING, THEME_HEAD, FONT, NOTES_CSS_BASE)."""
import json, os, random

from ucat_vr import VR
from ucat_sjt import SJT
from ucat_dm import DM_ARG
import ucat_gen as gen

HERE = os.path.dirname(os.path.abspath(__file__))
OFFICIAL = "https://www.ucat.ac.uk/prepare/practice-tests/"

INTRO = {
    "vr": "<p>Read each passage and answer using <b>only the information in the passage</b>, not your own knowledge.</p><p><b>True</b>: the passage says or clearly implies it. <b>False</b>: the passage contradicts it. <b>Can't tell</b>: the passage doesn't give enough information.</p><p>Real pace: about 30 seconds per question, including reading.</p>",
    "dm": "<p>Logic puzzles, syllogisms, Venn diagrams, probability, interpreting data and choosing the strongest argument.</p><p>For <b>Yes/No</b> questions, decide for each of the five statements. You score 2 marks if all five are right, or 1 mark with one mistake.</p><p>Real pace: about 1 minute per question.</p>",
    "qr": "<p>Use the tables and charts to answer. An on-screen <b>calculator</b> is available (top bar), as in the real test.</p><p>Real pace: about 43 seconds per question, so skip and flag long calculations.</p>",
    "sjt": "<p>Rate each response or consideration as a dental student or professional should. Think about patient safety, honesty, confidentiality, teamwork and working within your competence.</p><p>Exact answers score 1 mark; answers one step away score ½.</p><p>Real pace: about 23 seconds per question.</p>",
}
NAMES = {"vr": "Verbal Reasoning", "dm": "Decision Making", "qr": "Quantitative Reasoning", "sjt": "Situational Judgement"}
TF = ["True", "False", "Can't tell"]


def vr_items(passages, limits=None):
    out = []
    for k, (title, html, qs) in enumerate(passages):
        n = limits[k] if limits else len(qs)
        stem = f"<p><b>{title}</b></p>{html}"
        for q, opts, ans, exp in qs[:n]:
            if opts == TF:
                qh = f"<p>{q}</p><p class='muted' style='font-weight:500;font-size:0.88rem'>True, False or Can't tell?</p>"
            else:
                qh = f"<p>{q}</p>"
            out.append({"type": "mc", "stem": stem, "q": qh, "opts": opts, "ans": ans, "exp": exp})
    return out


def sjt_items(scenarios, total):
    out = []
    for scen, items in scenarios:
        for it in items:
            if len(out) >= total: return out
            if it[0] == "mc":
                _, q, opts, ans, exp = it
                out.append({"type": "mc", "stem": scen, "q": f"<p>{q}</p>", "opts": opts, "ans": ans, "exp": exp})
            else:
                kind, text, ans, exp = it
                lead = "How appropriate is this response?" if kind == "app" else "How important is this to take into account?"
                out.append({"type": "rate", "scale": kind, "stem": scen, "q": f"<p><b>{lead}</b></p><p>{text}</p>", "ans": ans, "exp": exp})
    return out


def dm_items(counts, args, seed):
    rng = random.Random(seed)
    items = gen.dm_generated({k: v for k, v in counts.items() if k != "arg"}, seed)
    for q, opts, ans, exp in args:
        items.append({"type": "mc", "stem": None, "q": f"<p>{q}</p><p class='muted' style='font-weight:500;font-size:0.88rem'>Select the strongest argument.</p>", "opts": opts, "ans": ans, "exp": exp})
    rng.shuffle(items)
    return items


def sections_for(keys, mode):
    return keys


def build_sets():
    # split hand-written banks so no question appears in two sets
    vr_mock, vr_timed, vr_drill = VR[:11], VR[11:15], VR[15:18]
    # SJT: scenario lists in order; count items to split
    sj = SJT[:]
    def take(n):
        out, cnt = [], 0
        while cnt < n:
            s = sj.pop(0); out.append(s); cnt += len(s[1])
        return out
    sjt_mock = take(69); sjt_timed = take(24); sjt_drill = sj
    arg_mock, arg_timed, arg_drill = DM_ARG[:6], DM_ARG[6:8], DM_ARG[8:9]

    S = {}
    S["drill-vr"] = [("vr", vr_items(vr_drill, [4, 3, 3]), 0)]
    S["drill-dm"] = [("dm", dm_items({"syll": 2, "order": 2, "venn": 2, "prob": 2, "interp": 1}, arg_drill, 303), 0)]
    S["drill-qr"] = [("qr", gen.qr_set(10, 303), 0)]
    S["drill-sjt"] = [("sjt", sjt_items(sjt_drill, 10), 0)]
    S["timed-vr"] = [("vr", vr_items(vr_timed), 8)]
    S["timed-dm"] = [("dm", dm_items({"syll": 2, "order": 2, "venn": 2, "prob": 2, "interp": 2}, arg_timed, 202), 13)]
    S["timed-qr"] = [("qr", gen.qr_set(12, 202), 9)]
    S["timed-sjt"] = [("sjt", sjt_items(sjt_timed, 24), 9)]
    S["mock"] = [("vr", vr_items(vr_mock), 22),
                 ("dm", dm_items({"syll": 6, "order": 6, "venn": 6, "prob": 5, "interp": 6}, arg_mock, 101), 37),
                 ("qr", gen.qr_set(36, 101), 26),
                 ("sjt", sjt_items(sjt_mock, 69), 26)]
    return S


META = {
    "drill-vr": ("Verbal Reasoning drill", "Untimed drill", "10 questions on 3 passages, with feedback after each answer."),
    "drill-dm": ("Decision Making drill", "Untimed drill", "10 mixed questions with feedback after each answer."),
    "drill-qr": ("Quantitative Reasoning drill", "Untimed drill", "10 data questions with worked answers."),
    "drill-sjt": ("Situational Judgement drill", "Untimed drill", "10 items with the reasoning behind each rating."),
    "timed-vr": ("Verbal Reasoning: timed set", "Timed set · real pace", "16 questions in 8 minutes."),
    "timed-dm": ("Decision Making: timed set", "Timed set · real pace", "12 questions in 13 minutes."),
    "timed-qr": ("Quantitative Reasoning: timed set", "Timed set · real pace", "12 questions in 9 minutes."),
    "timed-sjt": ("Situational Judgement: timed set", "Timed set · real pace", "24 questions in 9 minutes."),
    "mock": ("Full UCAT mock", "Full-length mock", "All four subtests in order with real timings: 184 questions in 111 minutes, then a full review."),
}


def build_ucat(OUT, THEME_HEAD, FONT, notes_css):
    os.makedirs(f"{OUT}/ucat", exist_ok=True)
    tpl = open(os.path.join(HERE, "ucat_engine.html"), encoding="utf-8").read()
    sets = build_sets()
    counts = {}
    for sid, secs in sets.items():
        title, kind, blurb = META[sid]
        data = {"id": sid, "title": title, "kind": kind, "blurb": blurb,
                "mode": "drill" if sid.startswith("drill") else "test",
                "sections": [{"key": k, "name": NAMES[k], "minutes": m, "intro": INTRO[k], "items": items} for k, items, m in secs]}
        for s in data["sections"]:
            for it in s["items"]:
                if it["type"] == "mc":
                    assert 0 <= it["ans"] < len(it["opts"]) and len(set(it["opts"])) == len(it["opts"]), (sid, it["q"][:80])
                elif it["type"] == "yn":
                    assert len(it["statements"]) == 5 and len(it["answers"]) == 5
                else:
                    assert it["type"] == "rate" and 0 <= it["ans"] <= 3
        counts[sid] = [len(s["items"]) for s in data["sections"]]
        page = tpl.replace("__TITLE__", title).replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
        open(f"{OUT}/ucat/{sid}.html", "w", encoding="utf-8").write(page)
    assert counts["mock"] == [44, 35, 36, 69], counts["mock"]
    assert counts["drill-vr"] == [10] and counts["drill-sjt"] == [10], counts
    assert counts["timed-sjt"] == [24] and counts["timed-vr"] == [16], counts

    def row(sid):
        title, kind, blurb = META[sid]
        return (f'<a class="set" href="{sid}.html"><div><div class="k">{kind}</div><div class="t">{title}</div>'
                f'<div class="b">{blurb}</div></div><div class="last" id="last-{sid}"></div></a>')
    total = sum(sum(v) for v in counts.values())
    page = f"""<!doctype html>
{THEME_HEAD}
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>UCAT practice – Pre-Dentistry Study Hub</title>
{FONT}
<style>{notes_css}
:root{{--accent:#38bdf8;--accent-bg:rgba(56,189,248,0.10)}}
[data-theme="light"]{{--accent:#0284c7;--accent-bg:rgba(2,132,199,0.08)}}
.set{{display:flex;justify-content:space-between;align-items:center;gap:14px;background:var(--card);border:1px solid var(--border);border-radius:12px;padding:16px 18px;margin-bottom:10px;text-decoration:none;color:var(--text)}}
.set:hover{{border-color:var(--accent)}}
.set .k{{font-size:0.66rem;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:var(--accent)}}
.set .t{{font-weight:700;margin:2px 0}}
.set .b{{font-size:0.85rem;color:var(--muted)}}
.set .last{{font-size:0.78rem;color:var(--muted);text-align:right;white-space:nowrap}}
.official{{background:var(--accent-bg);border:1px solid var(--accent);border-radius:12px;padding:16px 18px;margin:18px 0}}
</style>
</head>
<body>
<div class="topbar">
  <div class="topbar-brand"><span>Step 2</span>UCAT practice</div>
  <div style="display:flex;align-items:center;gap:12px">
    <a class="back-link" href="../notes/topic15.html">UCAT notes</a>
    <a class="back-link" href="../index.html">← Hub</a>
    <button class="theme-btn" onclick="toggleTheme()" aria-label="Toggle theme">☀️</button>
  </div>
</div>
<div class="container">
  <div class="eyebrow">Getting in · Step 2 · Practice</div>
  <h1>UCAT practice</h1>
  <p class="lead">{total} original UCAT-style questions in the real formats: untimed drills to learn each question type, timed sets at real pace, and a full-length mock.</p>
  <div class="official"><b>Use the official tests too.</b> UCAT doesn't publish past papers. Its free <a href="{OFFICIAL}" target="_blank" rel="noopener">practice tests and question banks</a> (Sets A–D, standard, extra-time and untimed versions) use the real test interface, so do them after these drills and before test day.</div>
  <h2>1. Untimed drills</h2>
  {''.join(row(s) for s in ['drill-vr','drill-dm','drill-qr','drill-sjt'])}
  <h2>2. Timed sets (real pace)</h2>
  {''.join(row(s) for s in ['timed-vr','timed-dm','timed-qr','timed-sjt'])}
  <h2>3. Full mock</h2>
  {row('mock')}
  <p class="muted" style="font-size:0.85rem;margin-top:18px">These are original practice questions written for this site, not official UCAT content. Scores shown are raw marks; the real UCAT reports scaled scores (300–900 per cognitive subtest) and SJT bands, which can't be reproduced exactly.</p>
  <div class="cta"><a class="btn btn-hub" href="../notes/topic15.html">UCAT notes</a><a class="btn btn-quiz" href="../quizzes/topic15.html">UCAT facts quiz →</a></div>
</div>
<script>
function toggleTheme(){{const c=document.documentElement.getAttribute('data-theme')||'dark';const n=c==='dark'?'light':'dark';document.documentElement.setAttribute('data-theme',n);document.querySelector('.theme-btn').textContent=n==='dark'?'☀️':'🌙';try{{localStorage.setItem('theme',n);}}catch(e){{}}}}
try{{if(document.documentElement.getAttribute('data-theme')==='light')document.querySelector('.theme-btn').textContent='🌙';}}catch(e){{}}
{json.dumps(list(sets.keys()))}.forEach(function(id){{try{{var d=JSON.parse(localStorage.getItem('ucat_'+id+'_last')||'null');var el=document.getElementById('last-'+id);
if(d&&el){{var g=0,m=0;d.sections.forEach(function(s){{g+=s.got;m+=s.max;}});el.innerHTML='Last: <b>'+Math.round(100*g/m)+'%</b><br>'+new Date(d.date).toLocaleDateString('en-GB');}}}}catch(e){{}}}});
</script>
</body>
</html>"""
    open(f"{OUT}/ucat/index.html", "w", encoding="utf-8").write(page)
    return counts
