"""Generated UCAT-style items whose answers are computed, not hand-keyed.

QR: table/chart scenarios with 5 options (A–E), answers calculated.
DM: syllogisms (model-checked yes/no), ordering puzzles (brute-force unique), Venn counts,
    probability (exact fractions), interpreting a table (yes/no, computed).
Everything is seeded, so builds are reproducible.
"""
import itertools, math, random
from fractions import Fraction

# ---------------------------------------------------------------- helpers
def _fmt_money(x):
    return f"£{x:,.2f}"

def _opts5(correct, cands, fmt, rng, spread=(0.8, 0.9, 1.1, 1.2, 1.25, 0.75)):
    """Return (options list of 5 formatted strings sorted ascending, index of correct)."""
    vals = [correct]
    seen = {fmt(correct)}
    for c in cands:
        if c is None or c <= 0: continue
        f = fmt(c)
        if f not in seen and len(vals) < 5:
            vals.append(c); seen.add(f)
    tries = 0
    while len(vals) < 5:
        tries += 1
        assert tries < 500 and correct > 0, ("cannot build options", correct)
        c = correct * rng.choice(spread) * (1 + rng.uniform(-0.03, 0.03))
        f = fmt(c)
        if f not in seen and c > 0:
            vals.append(c); seen.add(f)
    vals.sort()
    opts = [fmt(v) for v in vals]
    return opts, opts.index(fmt(correct))

def _table(headers, rows, caption=""):
    h = "".join(f"<th>{x}</th>" for x in headers)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    cap = f"<p><b>{caption}</b></p>" if caption else ""
    return f"{cap}<table><tr>{h}</tr>{b}</table>"

def _mc(stem, q, opts, ans, exp, calc=True):
    return {"type": "mc", "stem": stem, "q": q, "opts": opts, "ans": ans, "exp": exp}

def _r(x, n=2):
    return round(x + 1e-12, n)

# ---------------------------------------------------------------- QR scenarios
def qr_shop(rng):
    items = rng.sample([("Electric toothbrush", 42, 89), ("Interdental brushes (pack)", 3, 7), ("Floss (50 m)", 2, 5),
                        ("Mouthwash (500 ml)", 3, 7), ("Toothpaste (75 ml)", 2, 5), ("Replacement heads (4)", 12, 25),
                        ("Water flosser", 35, 70), ("Whitening strips", 15, 30)], 5)
    rows = []
    for name, lo, hi in items:
        price = rng.randint(lo * 4, hi * 4) / 4 - 0.01
        disc = rng.choice([0, 0, 10, 15, 20, 25])
        rows.append((name, price, disc))
    stem = _table(["Item", "Price", "Offer"],
                  [(n, _fmt_money(p), f"{d}% off" if d else "–") for n, p, d in rows],
                  "Pharmacy price list (prices include VAT at 20%)")
    out = []
    # Q1 basket total with discounts
    pick = rng.sample(range(5), 3); qty = [rng.randint(1, 3) for _ in pick]
    total = sum(rows[i][1] * (1 - rows[i][2] / 100) * q for i, q in zip(pick, qty))
    nodisc = sum(rows[i][1] * q for i, q in zip(pick, qty))
    once = sum(rows[i][1] * (1 - rows[i][2] / 100) for i in pick)
    desc = ", ".join(f"{q} × {rows[i][0].lower()}" for i, q in zip(pick, qty))
    o, a = _opts5(_r(total), [_r(nodisc), _r(once), _r(total * 1.2), _r(total - min(rows[i][1] for i in pick) * 0.1)], _fmt_money, rng)
    out.append(_mc(stem, f"A customer buys {desc}. How much do they pay, after offers?", o, a,
                   f"Apply each item's offer, multiply by quantity, then add: {_fmt_money(_r(total))}. Forgetting the offers gives {_fmt_money(_r(nodisc))}."))
    # Q2 price excluding VAT
    i = rng.randrange(5); p = rows[i][1]
    exv = p / 1.2
    o, a = _opts5(_r(exv), [_r(p * 0.8), _r(p - 20), _r(p / 1.02), _r(p * 0.83)], _fmt_money, rng)
    out.append(_mc(stem, f"Prices include VAT at 20%. What is the price of the {rows[i][0].lower()} before VAT (ignore offers)?", o, a,
                   f"Price before VAT = price ÷ 1.2 = {_fmt_money(p)} ÷ 1.2 = {_fmt_money(_r(exv))}. Taking 20% off (× 0.8) is the common mistake: it gives {_fmt_money(_r(p*0.8))}."))
    # Q3 saving
    disc_items = [r for r in rows if r[2]] or [rows[0]]
    name, p, d = max(disc_items, key=lambda r: r[1] * r[2])
    if d == 0: d = 10
    n = rng.randint(2, 4)
    save = p * d / 100 * n
    o, a = _opts5(_r(save), [_r(p * d / 100), _r(p * n * (1 - d / 100)), _r(save * 1.2), _r(save / 1.2)], _fmt_money, rng)
    out.append(_mc(stem, f"How much does a customer save by buying {n} × {name.lower()} on offer rather than at full price?", o, a,
                   f"Saving per item = {d}% of {_fmt_money(p)} = {_fmt_money(_r(p*d/100))}; × {n} = {_fmt_money(_r(save))}."))
    # Q4 percentage difference between two items
    pairs = [(i, j) for i in range(5) for j in range(5) if rows[i][1] > rows[j][1] * 1.08]
    i, j = rng.choice(pairs)
    pct = (rows[i][1] - rows[j][1]) / rows[j][1] * 100
    wrong = (rows[i][1] - rows[j][1]) / rows[i][1] * 100
    fmtp = lambda x: f"{x:.0f}%"
    o, a = _opts5(round(pct), [round(wrong), round(pct / 2), round(pct * 1.1 + 3), round(rows[i][1] / rows[j][1] * 100)], fmtp, rng)
    out.append(_mc(stem, f"By what percentage is the full price of the {rows[i][0].lower()} higher than the full price of the {rows[j][0].lower()}? (nearest whole %)", o, a,
                   f"(higher − lower) ÷ lower × 100 = ({_fmt_money(rows[i][1])} − {_fmt_money(rows[j][1])}) ÷ {_fmt_money(rows[j][1])} × 100 ≈ {round(pct)}%. Dividing by the higher price instead gives {round(wrong)}%."))
    return out


def qr_clinic(rng):
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    kinds = ["Check-ups", "Fillings", "Extractions", "Hygienist"]
    data = [[rng.randint(14, 40), rng.randint(6, 22), rng.randint(1, 8), rng.randint(8, 20)] for _ in days]
    stem = _table(["Day"] + kinds, [[d] + row for d, row in zip(days, data)], "Appointments at a dental practice in one week")
    out = []
    tot = [sum(r) for r in data]
    # Q1 mean per day of check-ups
    ck = [r[0] for r in data]; mean = sum(ck) / 5
    f1 = lambda x: f"{x:.1f}"
    o, a = _opts5(round(mean, 1), [round(sum(ck) / 4, 1), round(sorted(ck)[2], 1), round(sum(tot) / 5, 1), round(mean * 1.1, 1)], f1, rng)
    out.append(_mc(stem, "What was the mean number of check-ups per day?", o, a, f"Total check-ups = {sum(ck)}; ÷ 5 days = {mean:.1f}."))
    # Q2 % of week's appointments that were fillings
    fil = sum(r[1] for r in data); allx = sum(tot)
    pct = fil / allx * 100
    fp = lambda x: f"{x:.1f}%"
    o, a = _opts5(round(pct, 1), [round(fil / sum(ck) * 100, 1), round(100 / 4, 1), round(pct * 1.15, 1), round(pct * 0.85, 1)], fp, rng)
    out.append(_mc(stem, "What percentage of all appointments that week were fillings? (1 decimal place)", o, a, f"Fillings {fil} ÷ all appointments {allx} × 100 = {pct:.1f}%."))
    # Q3 busiest day vs quietest day ratio of total
    hi, lo = max(tot), min(tot)
    fr = lambda x: f"{x:.2f}"
    o, a = _opts5(round(hi / lo, 2), [round(lo / hi, 2), round((hi - lo) / lo, 2), round(hi / (sum(tot) / 5), 2), round(hi / lo + 0.25, 2)], fr, rng)
    out.append(_mc(stem, "How many times as many appointments were there on the busiest day as on the quietest day? (2 decimal places)", o, a,
                   f"Daily totals: {', '.join(f'{d} {t}' for d, t in zip(days, tot))}. Busiest {hi} ÷ quietest {lo} = {hi/lo:.2f}."))
    # Q4 income
    fee = {"Check-ups": 27.90, "Fillings": 76.60, "Extractions": 76.60}
    d = rng.randrange(5)
    inc = data[d][0] * 27.90 + (data[d][1] + data[d][2]) * 76.60
    o, a = _opts5(_r(inc), [_r((data[d][0] + data[d][1] + data[d][2]) * 76.60), _r(data[d][0] * 27.90 + data[d][1] * 76.60), _r(inc * 1.2), _r(tot[d] * 27.90)], _fmt_money, rng)
    out.append(_mc(stem, f"Each check-up is charged £27.90 and each filling or extraction £76.60. Hygienist visits are charged separately. How much was charged for check-ups, fillings and extractions on {days[d]}?", o, a,
                   f"{data[d][0]} × £27.90 + ({data[d][1]} + {data[d][2]}) × £76.60 = {_fmt_money(_r(inc))}."))
    return out


def qr_travel(rng):
    towns = ["Leicester", "Nottingham", "Derby", "Birmingham", "Coventry", "Sheffield"]
    a, b = rng.sample(towns, 2)
    dist = rng.choice([28, 34, 42, 48, 55, 64, 72])
    deps = sorted(rng.sample(range(6 * 60 + 5, 9 * 60, 5), 4))
    dur = [rng.choice([38, 42, 47, 51, 55, 58, 63]) for _ in deps]
    hm = lambda m: f"{m//60:02d}:{m%60:02d}"
    rows = [(hm(d), f"{u} min", hm(d + u)) for d, u in zip(deps, dur)]
    stem = _table(["Departs " + a, "Journey time", "Arrives " + b], rows,
                  f"Morning trains from {a} to {b} ({dist} miles by rail). Anytime return £{rng.choice([18.40, 22.70, 26.90, 31.50]):.2f}; railcard saves one third.")
    fare = float(stem.split("return £")[1].split(";")[0])
    out = []
    # Q1 average speed fastest train
    k = min(range(4), key=lambda i: dur[i]); spd = dist / (dur[k] / 60)
    f0 = lambda x: f"{x:.0f} mph"
    o, a2 = _opts5(round(spd), [round(dist / dur[k] * 100), round(dist / (max(dur) / 60)), round(spd * 0.9), round(dist / (dur[k] / 100))], f0, rng)
    out.append(_mc(stem, "What is the average speed of the fastest train? (nearest mph)", o, a2,
                   f"Fastest journey {dur[k]} min = {dur[k]/60:.3f} h. Speed = {dist} ÷ {dur[k]/60:.3f} ≈ {spd:.0f} mph."))
    # Q2 railcard fare for 3 people
    n = rng.randint(2, 4); rc = fare * 2 / 3 * n
    o, a2 = _opts5(_r(rc), [_r(fare / 3 * n), _r(fare * n), _r(fare * 2 / 3), _r(rc * 1.1)], _fmt_money, rng)
    out.append(_mc(stem, f"{n} people, each with a railcard, buy anytime returns. What is the total cost?", o, a2,
                   f"Railcard fare = £{fare:.2f} × ⅔ = £{fare*2/3:.2f}; × {n} = {_fmt_money(_r(rc))}. A third OFF means paying two thirds."))
    # Q3 latest train to arrive by time
    target = deps[2] + dur[2] + rng.choice([2, 4, 6])
    ok = [i for i in range(4) if deps[i] + dur[i] <= target]
    best = max(ok, key=lambda i: deps[i])
    opts = [hm(d) for d in deps] + ["None of these trains"]
    ans = best
    out.append(_mc(stem, f"A student must arrive in {b} by {hm(target)}. What is the latest train they can catch?",
                   opts, ans, f"Arrival times: {', '.join(r[2] for r in rows)}. The latest departure arriving by {hm(target)} is {hm(deps[best])}."))
    # Q4 cost per mile
    cpm = fare / (2 * dist) * 100
    fp = lambda x: f"{x:.1f}p"
    o, a2 = _opts5(round(cpm, 1), [round(fare / dist * 100, 1), round(cpm / 2, 1), round(cpm * 1.2, 1), round(fare / (2 * dist), 1)], fp, rng)
    out.append(_mc(stem, "Without a railcard, what is the cost per mile of an anytime return? (pence, 1 decimal place)", o, a2,
                   f"A return covers 2 × {dist} = {2*dist} miles. £{fare:.2f} ÷ {2*dist} = {cpm:.1f}p per mile. Forgetting the return leg doubles it."))
    return out


def qr_dilution(rng):
    conc = rng.choice([0.2, 0.12, 0.05, 2.0, 1.5])  # %
    stock = rng.choice([10, 20, 25])  # % stock solution
    vol = rng.choice([250, 500, 750, 1000])
    stem = (f"<p>A clinic makes up a rinse at <b>{conc}%</b> from a <b>{stock}%</b> stock solution, "
            f"diluted with water. It uses <b>{vol} ml</b> of rinse a day. Stock costs <b>£{rng.choice([6.40, 8.80, 12.50])}</b> per 100 ml. "
            f"The clinic opens 5 days a week.</p><p>% means grams of active ingredient per 100 ml.</p>")
    price = float(stem.split("costs <b>£")[1].split("</b>")[0])
    out = []
    stock_ml = vol * conc / stock
    f1 = lambda x: f"{x:.1f} ml"
    o, a = _opts5(round(stock_ml, 1), [round(vol * stock / conc / 100, 1), round(vol * conc / 100, 1), round(stock_ml * 10, 1), round(vol - stock_ml, 1)], f1, rng)
    out.append(_mc(stem, "How much stock solution is needed for one day's rinse?", o, a,
                   f"C₁V₁ = C₂V₂: stock volume = {vol} × {conc} ÷ {stock} = {stock_ml:.1f} ml."))
    g = vol * conc / 100
    fg = lambda x: f"{x:.2f} g"
    o, a = _opts5(round(g, 2), [round(g * 10, 2), round(g / 10, 2), round(vol * stock / 100, 2), round(g * 5, 2)], fg, rng)
    out.append(_mc(stem, "How many grams of active ingredient are in one day's rinse?", o, a, f"{conc}% = {conc} g per 100 ml, so {vol} ml contains {vol} × {conc} ÷ 100 = {g:.2f} g."))
    wk = stock_ml * 5 / 100 * price
    o, a = _opts5(_r(wk), [_r(stock_ml / 100 * price), _r(wk * 7 / 5), _r(vol * 5 / 100 * price), _r(wk * 10)], _fmt_money, rng)
    out.append(_mc(stem, "What is the weekly cost of the stock solution used?", o, a,
                   f"Weekly stock = {stock_ml:.1f} × 5 = {stock_ml*5:.1f} ml; cost = {stock_ml*5:.1f} ÷ 100 × £{price:.2f} = {_fmt_money(_r(wk))}."))
    water = vol - stock_ml
    o, a = _opts5(round(water, 1), [round(vol, 1), round(stock_ml, 1), round(water * 1.1, 1), round(vol + stock_ml, 1)], f1, rng)
    out.append(_mc(stem, "How much water is added to make one day's rinse?", o, a, f"Water = total − stock = {vol} − {stock_ml:.1f} = {water:.1f} ml."))
    return out


def qr_exchange(rng):
    cur = [("Euro", "€", round(rng.uniform(1.12, 1.19), 3)), ("US dollar", "$", round(rng.uniform(1.24, 1.36), 3)),
           ("Swiss franc", "CHF ", round(rng.uniform(1.05, 1.15), 3)), ("Japanese yen", "¥", round(rng.uniform(185, 205), 1))]
    comm = rng.choice([1.5, 2, 2.5, 3])
    stem = _table(["Currency", "£1 buys"], [(n, f"{s}{r}") for n, s, r in cur], f"Bureau de change rates. Commission of {comm}% is charged on the pounds exchanged, deducted before conversion.")
    out = []
    n, s, r = cur[0]; gbp = rng.choice([300, 450, 600, 750])
    got = gbp * (1 - comm / 100) * r
    fe = lambda x: f"€{x:,.2f}"
    o, a = _opts5(_r(got), [_r(gbp * r), _r(gbp * r - comm), _r(gbp / r), _r(gbp * (1 - comm / 100) / r)], fe, rng)
    out.append(_mc(stem, f"How many euros does a traveller receive for £{gbp}?", o, a, f"After {comm}% commission: £{gbp} × {1-comm/100} = £{gbp*(1-comm/100):.2f}; × {r} = €{got:,.2f}."))
    n, s, r = cur[1]; usd = rng.choice([200, 350, 500])
    need = usd / r / (1 - comm / 100)
    o, a = _opts5(_r(need), [_r(usd / r), _r(usd * r), _r(usd / r * (1 + comm / 100)), _r(usd / r * (1 - comm / 100))], _fmt_money, rng)
    out.append(_mc(stem, f"How many pounds must be exchanged to receive exactly ${usd}?", o, a,
                   f"Pounds after commission needed = {usd} ÷ {r} = £{usd/r:.2f}. That's {100-comm}% of what's handed over, so £{usd/r:.2f} ÷ {1-comm/100} = {_fmt_money(_r(need))}."))
    n, s, r = cur[3]; yen = rng.choice([12000, 20000, 35000])
    back = yen / r
    o, a = _opts5(_r(back), [_r(yen * r / 1000), _r(back * (1 - comm / 100)), _r(back * 1.1), _r(yen / 100)], _fmt_money, rng)
    out.append(_mc(stem, f"Ignoring commission, what is ¥{yen:,} worth in pounds?", o, a, f"¥{yen:,} ÷ {r} = {_fmt_money(_r(back))}."))
    e, d = cur[0][2], cur[1][2]
    ed = d / e
    f3 = lambda x: f"${x:.3f}"
    o, a = _opts5(round(ed, 3), [round(e / d, 3), round(d - e + 1, 3), round(e * d, 3), round(ed * 1.05, 3)], f3, rng)
    out.append(_mc(stem, "Using these rates, how many US dollars is €1 worth? (3 decimal places)", o, a, f"€1 = £1 ÷ {e}; × {d} = ${ed:.3f}."))
    return out


def qr_bar(rng):
    q = ["Q1", "Q2", "Q3", "Q4"]
    yrs = ["2025", "2026"]
    vals = {y: [rng.randint(120, 380) for _ in q] for y in yrs}
    W, H, x0, y0, top = 520, 260, 50, 220, 400
    bars = []
    for i, qq in enumerate(q):
        for j, y in enumerate(yrs):
            v = vals[y][i]; h = v / top * 190
            x = x0 + 20 + i * 115 + j * 36
            fill = "#94a3b8" if j == 0 else "#38bdf8"
            bars.append(f'<rect x="{x}" y="{y0-h:.0f}" width="32" height="{h:.0f}" fill="{fill}"/>'
                        f'<text x="{x+16}" y="{y0-h-4:.0f}" font-size="11" text-anchor="middle">{v}</text>')
        bars.append(f'<text x="{x0+56+i*115}" y="{y0+18}" font-size="12" text-anchor="middle">{qq}</text>')
    grid = "".join(f'<line x1="{x0}" x2="{W-10}" y1="{y0-v/top*190:.0f}" y2="{y0-v/top*190:.0f}" stroke="#888" stroke-opacity="0.25"/><text x="{x0-6}" y="{y0-v/top*190+4:.0f}" font-size="11" text-anchor="end">{v}</text>' for v in (0, 100, 200, 300, 400))
    legend = '<rect x="330" y="10" width="12" height="12" fill="#94a3b8"/><text x="346" y="21" font-size="12">2025</text><rect x="400" y="10" width="12" height="12" fill="#38bdf8"/><text x="416" y="21" font-size="12">2026</text>'
    stem = (f'<p><b>New patients registering at a dental practice, by quarter</b></p>'
            f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Bar chart of new patients by quarter in 2025 and 2026">{grid}{"".join(bars)}{legend}</svg>')
    out = []
    t25, t26 = sum(vals["2025"]), sum(vals["2026"])
    ch = (t26 - t25) / t25 * 100
    fp = lambda x: f"{x:+.1f}%"
    out.append(None)
    cands = [round(ch, 1), round((t26 - t25) / t26 * 100, 1), round(ch + 4.5, 1), round(ch - 4.5, 1), round(ch * 1.8 + (1 if ch >= 0 else -1), 1)]
    uniq = []
    for c in cands:
        if fp(c) not in [fp(u) for u in uniq]: uniq.append(c)
    while len(uniq) < 5: uniq.append(round(ch + rng.choice([-9, -7, 7, 9]), 1))
    while len({fp(u) for u in uniq}) < 5:
        uniq.append(round(ch + rng.choice([-12, -10, 10, 12, 15]), 1))
    dedup = {}
    for u in uniq: dedup.setdefault(fp(u), u)
    keep = [dedup[fp(round(ch, 1))]] + [v for k, v in dedup.items() if k != fp(round(ch, 1))][:4]
    opts = [fp(u) for u in sorted(keep)]
    out[-1] = _mc(stem, "What was the percentage change in total new patients from 2025 to 2026? (1 decimal place)", opts, opts.index(fp(round(ch, 1))),
                  f"2025 total = {t25}; 2026 total = {t26}. Change = ({t26} − {t25}) ÷ {t25} × 100 = {ch:+.1f}%.")
    m26 = t26 / 4
    f1 = lambda x: f"{x:.2f}"
    o, a = _opts5(round(m26, 2), [round(t25 / 4, 2), round((t25 + t26) / 8, 2), round(max(vals['2026']) / 2, 2), round(m26 * 1.1, 2)], f1, rng)
    out.append(_mc(stem, "What was the mean number of new patients per quarter in 2026?", o, a, f"{' + '.join(map(str, vals['2026']))} = {t26}; ÷ 4 = {m26:.2f}."))
    i = rng.randrange(4)
    share = vals["2026"][i] / t26 * 100
    fp2 = lambda x: f"{x:.1f}%"
    o, a = _opts5(round(share, 1), [round(vals['2025'][i] / t25 * 100, 1), round(vals['2026'][i] / (t25 + t26) * 100, 1), 25.0, round(share * 1.15, 1)], fp2, rng)
    out.append(_mc(stem, f"What percentage of 2026's new patients registered in {q[i]}? (1 decimal place)", o, a, f"{vals['2026'][i]} ÷ {t26} × 100 = {share:.1f}%."))
    target = round(t26 * 1.15)
    need_q4 = target - sum(vals["2026"][:3])
    fi = lambda x: f"{x:.0f}"
    o, a = _opts5(need_q4, [round(vals['2026'][3] * 1.15), target - sum(vals['2025'][:3]), round(t25 * 1.15) - sum(vals['2026'][:3]), need_q4 + 37], fi, rng)
    out.append(_mc(stem, f"The practice wanted 2026's total to be 15% higher than it actually was ({target} patients, rounded). How many new patients would Q4 2026 have needed, with Q1–Q3 unchanged?", o, a,
                   f"Target {target} − (Q1–Q3 2026 = {sum(vals['2026'][:3])}) = {need_q4}."))
    return out


def qr_tariff(rng):
    plans = [("Basic", rng.choice([8, 10, 12]), rng.choice([5, 6, 8]), rng.choice([3, 4])),
             ("Plus", rng.choice([18, 20, 22]), rng.choice([15, 20, 25]), rng.choice([1, 2])),
             ("Max", rng.choice([30, 32, 35]), 100, 0)]
    stem = _table(["Plan", "Monthly fee", "Data included", "Extra data (per GB)"],
                  [(n, f"£{f}", f"{d} GB" if d < 100 else "Unlimited", f"£{e}" if e else "–") for n, f, d, e in plans],
                  "Mobile phone plans (12-month contract)")
    out = []
    use = rng.choice([9, 11, 12, 14])
    cost = lambda p, u: p[1] + max(0, u - p[2]) * p[3]
    c0 = cost(plans[0], use)
    o, a = _opts5(c0, [plans[0][1] + use * plans[0][3], plans[0][1], c0 + plans[0][3], c0 * 12], lambda x: f"£{x:.2f}", rng)
    out.append(_mc(stem, f"A student uses {use} GB in a month on the Basic plan. What is their bill?", o, a,
                   f"£{plans[0][1]} + ({use} − {plans[0][2]}) GB × £{plans[0][3]} = £{c0:.2f}."))
    # break-even basic vs plus
    be = None
    for u in range(0, 300):
        if cost(plans[0], u) > cost(plans[1], u):
            be = u; break
    vals = {be, be - 1, be + 1, be + 2}
    extra = be + 3
    while len(vals) < 5:
        vals.add(extra); extra += 1
    opts = [f"{x} GB" for x in sorted(vals)]
    out.append(_mc(stem, "What is the smallest whole number of GB a month at which Basic costs more than Plus?", opts, opts.index(f"{be} GB"),
                   f"Basic at u GB = £{plans[0][1]} + (u − {plans[0][2]}) × £{plans[0][3]}; Plus = £{plans[1][1]} up to {plans[1][2]} GB. Basic first exceeds Plus at {be} GB (£{cost(plans[0],be)} vs £{cost(plans[1],be)})."))
    yr = plans[2][1] * 12
    o, a = _opts5(yr, [plans[2][1] * 10, plans[2][1] * 12 * 1.2, plans[1][1] * 12, yr + 12], lambda x: f"£{x:,.0f}", rng)
    out.append(_mc(stem, "What is the total cost of the Max plan over the 12-month contract?", o, a, f"£{plans[2][1]} × 12 = £{yr}."))
    diff = (plans[2][1] - plans[1][1]) / plans[1][1] * 100
    o, a = _opts5(round(diff), [round((plans[2][1] - plans[1][1]) / plans[2][1] * 100), plans[2][1] - plans[1][1], round(diff / 2), round(diff + 10)], lambda x: f"{x:.0f}%", rng)
    out.append(_mc(stem, "By what percentage is the Max monthly fee higher than the Plus monthly fee? (nearest whole %)", o, a,
                   f"(£{plans[2][1]} − £{plans[1][1]}) ÷ £{plans[1][1]} × 100 ≈ {round(diff)}%."))
    return out


def qr_room(rng):
    L, W_, Hh = rng.choice([4.2, 4.8, 5.4, 6.0]), rng.choice([3.0, 3.6, 4.2]), rng.choice([2.4, 2.5, 2.7])
    door, window = 1.8, rng.choice([1.5, 2.0, 2.4])
    cov = rng.choice([10, 12, 13])
    tin = rng.choice([2.5, 5])
    price = rng.choice([24.99, 29.99, 34.50])
    stem = (f"<p>A dental surgery measuring <b>{L} m × {W_} m</b> with walls <b>{Hh} m</b> high is being repainted.</p>"
            f"<ul><li>One door ({door} m²) and one window ({window} m²) are not painted.</li>"
            f"<li>Paint covers <b>{cov} m² per litre</b> per coat; two coats are needed.</li>"
            f"<li>Paint is sold in <b>{tin}-litre tins</b> at <b>£{price}</b> each. The ceiling is not painted.</li></ul>")
    walls = 2 * (L + W_) * Hh - door - window
    out = []
    fa = lambda x: f"{x:.2f} m²"
    o, a = _opts5(round(walls, 2), [round(2 * (L + W_) * Hh, 2), round(L * W_, 2), round((L + W_) * Hh - door - window, 2), round(walls + L * W_, 2)], fa, rng)
    out.append(_mc(stem, "What is the total wall area to be painted?", o, a, f"Perimeter {2*(L+W_):.1f} m × height {Hh} m = {2*(L+W_)*Hh:.2f} m²; minus door and window = {walls:.2f} m²."))
    litres = walls * 2 / cov
    fl = lambda x: f"{x:.2f} litres"
    o, a = _opts5(round(litres, 2), [round(walls / cov, 2), round(walls * 2 * cov / 100, 2), round(litres * 1.2, 2), round((walls + door + window) * 2 / cov, 2)], fl, rng)
    out.append(_mc(stem, "How much paint is needed for two coats?", o, a, f"{walls:.2f} m² × 2 coats ÷ {cov} m²/L = {litres:.2f} L."))
    tins = math.ceil(litres / tin)
    cost = tins * price
    o, a = _opts5(_r(cost), [_r(litres / tin * price), _r((tins - 1) * price if tins > 1 else price * 2), _r((tins + 1) * price), _r(litres * price)], _fmt_money, rng)
    out.append(_mc(stem, "Tins can't be split. What is the cost of the paint?", o, a, f"{litres:.2f} L ÷ {tin} L = {litres/tin:.2f} → round up to {tins} tins × £{price} = {_fmt_money(_r(cost))}."))
    left = tins * tin - litres
    o, a = _opts5(round(left, 2), [round(tins * tin, 2), round(litres - tin, 2) if litres > tin else round(left + 1, 2), round(left * 2, 2), round(left + tin, 2)], fl, rng)
    out.append(_mc(stem, "How much paint will be left over?", o, a, f"Bought {tins} × {tin} = {tins*tin} L; used {litres:.2f} L; left {left:.2f} L."))
    return out


def qr_marks(rng):
    comps = [("Coursework", rng.choice([20, 25, 30])), ("Practical", rng.choice([15, 20])), ]
    comps.append(("Final exam", 100 - comps[0][1] - comps[1][1]))
    students = ["Asha", "Ben", "Chen", "Dev", "Ella"]
    sc = [[rng.randint(48, 92) for _ in comps] for _ in students]
    stem = _table(["Student"] + [f"{c} ({w}%)" for c, w in comps], [[s] + r for s, r in zip(students, sc)],
                  "Module marks (%) and the weight of each component")
    wavg = lambda r: sum(m * w for m, (_, w) in zip(r, comps)) / 100
    out = []
    i = rng.randrange(5)
    v = wavg(sc[i])
    f1 = lambda x: f"{x:.1f}%"
    o, a = _opts5(round(v, 1), [round(sum(sc[i]) / 3, 1), round(v + 2.5, 1), round(sc[i][2], 1), round(v - 3.1, 1)], f1, rng)
    out.append(_mc(stem, f"What is {students[i]}'s overall module mark? (1 decimal place)", o, a,
                   f"Weighted mean = " + " + ".join(f"{m} × {w}%" for m, (_, w) in zip(sc[i], comps)) + f" = {v:.1f}%. A simple average gives {sum(sc[i])/3:.1f}%."))
    best = max(range(5), key=lambda k: wavg(sc[k]))
    out.append(_mc(stem, "Which student has the highest overall module mark?", students[:], best,
                   "Overall marks: " + ", ".join(f"{s} {wavg(r):.1f}%" for s, r in zip(students, sc)) + "."))
    j = rng.randrange(5)
    needed = (70 * 100 - sc[j][0] * comps[0][1] - sc[j][1] * comps[1][1]) / comps[2][1]
    fi = lambda x: f"{x:.1f}%"
    cands = [round(needed, 1), round(70 * 3 - sc[j][0] - sc[j][1], 1), 70.0, round(needed + 4, 1), round(needed - 4, 1)]
    o, a = _opts5(round(needed, 1), cands[1:], fi, rng)
    out.append(_mc(stem, f"If {students[j]} resat only the final exam, what exam mark would give an overall mark of exactly 70%? (1 decimal place)", o, a,
                   f"70 = ({sc[j][0]} × {comps[0][1]} + {sc[j][1]} × {comps[1][1]} + x × {comps[2][1]}) ÷ 100 → x = {needed:.1f}%."))
    ex = [r[2] for r in sc]
    med = sorted(ex)[2]
    o, a = _opts5(med, [round(sum(ex) / 5, 1), max(ex) - min(ex), sorted(ex)[1], sorted(ex)[3]], lambda x: f"{x:.1f}%", rng)
    out.append(_mc(stem, "What is the median final exam mark?", o, a, f"In order: {', '.join(map(str, sorted(ex)))}. The middle value is {med}."))
    return out


QR_MAKERS = [qr_shop, qr_clinic, qr_travel, qr_dilution, qr_exchange, qr_bar, qr_tariff, qr_room, qr_marks]


def qr_set(n_items, seed):
    rng = random.Random(seed)
    items = []
    makers = QR_MAKERS[:]
    rng.shuffle(makers)
    k = 0
    while len(items) < n_items:
        block = makers[k % len(makers)](rng)
        k += 1
        take = min(len(block), n_items - len(items))
        items.extend(block[:take])
    for it in items:
        assert len(it["opts"]) == 5 and len(set(it["opts"])) == 5, it["q"]
    return items


# ---------------------------------------------------------------- DM: syllogisms
REGIONS = list(itertools.product([0, 1], repeat=3))  # membership in (A, B, C)

def _holds(stmt, world):
    kind, x, y = stmt
    ex = lambda f: any(f(r) for r in world)
    if kind == "all": return not ex(lambda r: r[x] and not r[y])
    if kind == "no": return not ex(lambda r: r[x] and r[y])
    if kind == "some": return ex(lambda r: r[x] and r[y])
    if kind == "somenot": return ex(lambda r: r[x] and not r[y])

def _worlds(premises):
    out = []
    for mask in range(1, 2 ** 8):
        w = [REGIONS[i] for i in range(8) if mask >> i & 1]
        if not all(any(r[c] for r in w) for c in range(3)):  # every category non-empty
            continue
        if all(_holds(p, w) for p in premises):
            out.append(w)
    return out

def _say(stmt, names, plural=True):
    k, x, y = stmt
    X, Y = names[x], names[y]
    return {"all": f"All {X} are {Y}.", "no": f"No {X} are {Y}.", "some": f"Some {X} are {Y}.", "somenot": f"Some {X} are not {Y}."}[k]

def _why_not(stmt, names):
    k, x, y = stmt
    X, Y = names[x], names[y]
    return {"all": f"there could be {X} who are not {Y}", "no": f"some {X} could also be {Y}",
            "some": f"it's possible that no {X} are {Y}", "somenot": f"it's possible that all {X} are {Y}"}[k]

SYLL_THEMES = [
    ("dental students", "rowers", "musicians"), ("dentists", "runners", "cyclists"), ("patients", "smokers", "coffee drinkers"),
    ("nurses", "swimmers", "chess players"), ("hygienists", "volunteers", "first-aiders"), ("students", "early risers", "vegetarians"),
    ("surgeons", "pianists", "linguists"), ("applicants", "athletes", "debaters"), ("receptionists", "gardeners", "bakers"),
    ("therapists", "climbers", "readers"), ("lecturers", "drivers", "golfers"), ("technicians", "painters", "walkers"),
]

def dm_syllogism(rng):
    kinds = ["all", "no", "some", "somenot"]
    for _ in range(4000):
        names = rng.choice(SYLL_THEMES)
        names = list(names); rng.shuffle(names)
        n = rng.choice([2, 2, 3])
        prem = []
        pairs = [(0, 1), (1, 2), (0, 2), (1, 0), (2, 1), (2, 0)]
        for _p in range(n):
            x, y = rng.choice(pairs)
            prem.append((rng.choice(kinds), x, y))
        ws = _worlds(prem)
        if not ws or len(set(prem)) < n: continue
        cands = [(k, x, y) for k in kinds for x, y in pairs if (k, x, y) not in prem]
        rng.shuffle(cands)
        concl = []
        yes = [c for c in cands if all(_holds(c, w) for w in ws)]
        no = [c for c in cands if not all(_holds(c, w) for w in ws)]
        ny = rng.choice([2, 2, 3])
        if len(yes) < ny or len(no) < 5 - ny: continue
        concl = yes[:ny] + no[:5 - ny]
        rng.shuffle(concl)
        answers = [all(_holds(c, w) for w in ws) for c in concl]
        stem = None
        q = "<p>" + " ".join(_say(p, names) for p in prem) + "</p><p>Place 'Yes' if the conclusion follows from the statements, or 'No' if it does not.</p>"
        exp = "<br>".join(("<b>Yes</b>: " if a else "<b>No</b>: ") + _say(c, names)[:-1] +
                          ("; this is true in every situation the statements allow." if a else f"; {_why_not(c, names)}.")
                          for c, a in zip(concl, answers))
        return {"type": "yn", "stem": stem, "q": q, "statements": [_say(c, names) for c in concl], "answers": answers,
                "exp": "Remember: 'some' means at least one, and possibly all.<br>" + exp}
    raise RuntimeError("syllogism generation failed")


# ---------------------------------------------------------------- DM: ordering puzzles
ORDER_THEMES = [
    ("Five patients arrive at a dental practice one after another.", "arrived {}", ["first", "second", "third", "fourth", "fifth"]),
    ("Five students finish a 5 km run, with no ties.", "finished {}", ["first", "second", "third", "fourth", "fifth"]),
    ("Five dental chairs in a row are numbered 1 to 5 from left to right; each of five students sits at a different chair.", "sat at chair {}", ["1", "2", "3", "4", "5"]),
]
NAMES = ["Amir", "Bea", "Cal", "Dina", "Eli", "Femi", "Gus", "Hana", "Isla", "Jai"]

def dm_order(rng):
    for _ in range(2000):
        theme, verb, posw = rng.choice(ORDER_THEMES)
        ppl = rng.sample(NAMES, 5)
        sol = ppl[:]; rng.shuffle(sol)
        pos = {p: i for i, p in enumerate(sol)}
        clues = []
        for a, b in itertools.permutations(ppl, 2):
            if pos[a] < pos[b]: clues.append(("before", a, b))
            if pos[b] - pos[a] == 1: clues.append(("imm", a, b))
            d = abs(pos[a] - pos[b]) - 1
            if a < b: clues.append(("between", a, b, d))
        for a in ppl:
            if pos[a] not in (0, 4): clues.append(("notend", a))
            clues.append(("not", a, rng.choice([k for k in range(5) if k != pos[a]])))
        rng.shuffle(clues)
        def ok(perm, c):
            P = {p: i for i, p in enumerate(perm)}
            t = c[0]
            if t == "before": return P[c[1]] < P[c[2]]
            if t == "imm": return P[c[2]] - P[c[1]] == 1
            if t == "between": return abs(P[c[1]] - P[c[2]]) - 1 == c[3]
            if t == "notend": return P[c[1]] not in (0, 4)
            if t == "not": return P[c[1]] != c[2]
        chosen = []
        perms = list(itertools.permutations(ppl))
        for c in clues:
            alive = [p for p in perms if all(ok(p, x) for x in chosen + [c])]
            if len(alive) < len([p for p in perms if all(ok(p, x) for x in chosen)]):
                chosen.append(c)
            if len(alive) == 1: break
        alive = [p for p in perms if all(ok(p, x) for x in chosen)]
        if len(alive) != 1 or not (4 <= len(chosen) <= 6): continue
        k = rng.randrange(5)
        if theme.startswith("Five dental chairs"):
            say = {"before": lambda c: f"{c[1]} sits somewhere to the left of {c[2]}.", "imm": lambda c: f"{c[1]} sits immediately to the left of {c[2]}.",
                   "between": lambda c: (f"{c[1]} and {c[2]} sit next to each other." if c[3]==0 else f"There {'is' if c[3]==1 else 'are'} exactly {c[3]} {'student' if c[3]==1 else 'students'} between {c[1]} and {c[2]}."),
                   "notend": lambda c: f"{c[1]} is not at either end.", "not": lambda c: f"{c[1]} is not at chair {c[2]+1}."}
            q2 = f"Who sat at chair {k+1}?"
        else:
            vv = verb.split()[0]
            say = {"before": lambda c: f"{c[1]} {vv} before {c[2]}.", "imm": lambda c: f"{c[1]} {vv} immediately before {c[2]}.",
                   "between": lambda c: (f"{c[1]} and {c[2]} {vv} one straight after the other, in some order." if c[3]==0 else f"Exactly {c[3]} {'person' if c[3]==1 else 'people'} {vv} between {c[1]} and {c[2]}."),
                   "notend": lambda c: f"{c[1]} {vv} neither first nor last.", "not": lambda c: f"{c[1]} did not {('arrive' if vv=='arrived' else 'finish')} {posw[c[2]]}."}
            q2 = f"Who {verb.format(posw[k])}?"
        q = f"<p>{theme}</p><ul>" + "".join(f"<li>{say[c[0]](c)}</li>" for c in chosen) + f"</ul><p><b>{q2}</b></p>"
        opts = sorted(rng.sample([p for p in ppl if p != sol[k]], 3) + [sol[k]])
        exp = "Only one order fits every clue: " + " → ".join(sol) + f". So the answer is {sol[k]}."
        return {"type": "mc", "stem": None, "q": q, "opts": opts, "ans": opts.index(sol[k]), "exp": exp}
    raise RuntimeError("order generation failed")


# ---------------------------------------------------------------- DM: Venn
VENN_THEMES = [
    ("A group of Year 12 students", ["Biology", "Chemistry", "Maths"], "study"),
    ("Volunteers at a care home", ["weekdays", "weekends", "evenings"], "help on"),
    ("Patients at a clinic", ["smokers", "over 50", "diabetic"], "are"),
]

def _venn_svg(labels, r):
    # r: dict of region tuple -> count; tuple = (in A, in B, in C)
    cx = [(150, 120), (230, 120), (190, 190)]
    circ = "".join(f'<circle cx="{x}" cy="{y}" r="82" fill="none" stroke="#888" stroke-width="1.5"/>' for x, y in cx)
    pos = {(1, 0, 0): (110, 100), (0, 1, 0): (270, 100), (0, 0, 1): (190, 240), (1, 1, 0): (190, 92),
           (1, 0, 1): (140, 180), (0, 1, 1): (240, 180), (1, 1, 1): (190, 148)}
    nums = "".join(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="15" font-weight="700">{r[k]}</text>' for k, (x, y) in pos.items())
    labs = (f'<text x="70" y="36" font-size="13">{labels[0]}</text><text x="250" y="36" font-size="13">{labels[1]}</text>'
            f'<text x="190" y="300" text-anchor="middle" font-size="13">{labels[2]}</text>')
    outside = f'<text x="360" y="292" text-anchor="end" font-size="12">Neither/none: {r[(0,0,0)]}</text>'
    return f'<svg viewBox="0 0 380 310" role="img" aria-label="Venn diagram">{circ}{nums}{labs}{outside}</svg>'

def dm_venn(rng):
    who, labels, verb = rng.choice(VENN_THEMES)
    r = {k: rng.randint(2, 18) for k in REGIONS}
    A, B, C = labels
    qs = [
        (f"How many {verb} {A} and {B} but not {C}?", r[(1, 1, 0)]),
        (f"How many {verb} exactly two of the three?", r[(1, 1, 0)] + r[(1, 0, 1)] + r[(0, 1, 1)]),
        (f"How many {verb} {C} in total?", sum(v for k, v in r.items() if k[2])),
        (f"How many {verb} only one of the three?", r[(1, 0, 0)] + r[(0, 1, 0)] + r[(0, 0, 1)]),
        (f"How many {verb} {A} or {B} (or both)?", sum(v for k, v in r.items() if k[0] or k[1])),
        (f"How many are in the group altogether?", sum(r.values())),
    ]
    q, ans = rng.choice(qs)
    wrongs = {ans + d for d in (r[(1, 1, 1)], -r[(1, 1, 1)], r[(0, 0, 0)], 3, -3, 5)} - {ans}
    wrongs = [w for w in wrongs if w > 0]
    k = 1
    while len(wrongs) < 3:
        if ans + k not in wrongs: wrongs.append(ans + k)
        k += 1
    rng.shuffle(wrongs)
    opts = sorted([ans] + wrongs[:3])
    stem = f"<p>{who}: the diagram shows how many {verb} each combination.</p>" + _venn_svg(labels, r)
    return {"type": "mc", "stem": stem, "q": q, "opts": [str(o) for o in opts], "ans": opts.index(ans),
            "exp": f"Add the right regions of the diagram: the answer is {ans}. Check which regions are inside or outside each circle before adding."}


# ---------------------------------------------------------------- DM: probability
def _fr(f):
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else str(f.numerator)

def dm_prob(rng):
    t = rng.randrange(4)
    if t == 0:
        r, b = rng.randint(3, 7), rng.randint(2, 6); n = r + b
        p = Fraction(r, n) * Fraction(r - 1, n - 1)
        wrong = [Fraction(r, n) ** 2, Fraction(r, n), Fraction(r - 1, n - 1)]
        q = f"A box holds {r} red and {b} blue mouthguards. Two are taken at random without replacement. What is the probability both are red?"
        exp = f"{r}/{n} × {r-1}/{n-1} = {_fr(p)}. With replacement it would be ({r}/{n})² = {_fr(Fraction(r,n)**2)}."
    elif t == 1:
        s = rng.choice([4, 5, 6, 7, 8, 9, 10])
        ways = sum(1 for a in range(1, 7) for c in range(1, 7) if a + c == s)
        p = Fraction(ways, 36)
        wrong = [Fraction(1, 11), Fraction(1, 6), Fraction(ways, 12)]
        q = f"Two fair six-sided dice are rolled. What is the probability that the total is {s}?"
        exp = f"There are {ways} ways to make {s} out of 36 equally likely outcomes: {_fr(p)}."
    elif t == 2:
        pa, pb = rng.choice([Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(3, 5)]), rng.choice([Fraction(1, 3), Fraction(2, 5), Fraction(1, 4), Fraction(1, 2)])
        p = 1 - (1 - pa) * (1 - pb)
        wrong = [pa * pb, pa + pb if pa + pb < 1 else Fraction(9, 10), (1 - pa) * (1 - pb)]
        q = f"The probability that Sam passes the UCAT practice target is {_fr(pa)}, and independently the probability that Priya does is {_fr(pb)}. What is the probability that at least one of them does?"
        exp = f"P(at least one) = 1 − P(neither) = 1 − {_fr(1-pa)} × {_fr(1-pb)} = {_fr(p)}."
    else:
        n = rng.choice([3, 4]);
        p = Fraction(1, 2) ** n
        wrong = [Fraction(1, 2 * n), Fraction(n, 2 ** n), Fraction(1, n)]
        q = f"A fair coin is tossed {n} times. What is the probability of getting heads every time?"
        exp = f"(1/2)^{n} = {_fr(p)}."
    w = []
    for x in wrong:
        if x != p and x not in w and 0 < x <= 1: w.append(x)
    extra = [Fraction(1, 3), Fraction(1, 5), Fraction(2, 9), Fraction(5, 12), Fraction(1, 8)]
    for x in extra:
        if len(w) >= 3: break
        if x != p and x not in w: w.append(x)
    opts = [p] + w[:3]
    opts.sort()
    return {"type": "mc", "stem": None, "q": q, "opts": [_fr(o) for o in opts], "ans": opts.index(p), "exp": exp}


# ---------------------------------------------------------------- DM: interpreting a table (yes/no)
def dm_interpret(rng):
    groups = ["Under 18", "18–39", "40–64", "65+"]
    days = ["Mon", "Tue", "Wed"]
    d = [[rng.randint(4, 30) for _ in days] for _ in groups]
    stem = _table(["Age group"] + days, [[g] + r for g, r in zip(groups, d)], "Patients seen at an urgent dental clinic")
    tot_day = [sum(d[g][k] for g in range(4)) for k in range(3)]
    tot_grp = [sum(r) for r in d]
    cands = []
    for k in range(3):
        cands.append((f"More patients were seen on {days[k]} than on any other day.", tot_day[k] == max(tot_day) and tot_day.count(max(tot_day)) == 1))
    for g in range(4):
        for h in range(4):
            if g < h: cands.append((f"Over the three days, more {groups[g]} patients were seen than {groups[h]} patients.", tot_grp[g] > tot_grp[h]))
    g = rng.randrange(4); k = rng.randrange(3)
    share = d[g][k] / tot_day[k]
    cands.append((f"{groups[g]} patients made up more than a quarter of {days[k]}'s patients.", share > 0.25))
    cands.append((f"The clinic saw more than {sum(tot_day)-rng.choice([-3,4])} patients in total.", sum(tot_day) > sum(tot_day) - 4 if False else None))
    cands = [c for c in cands if c[1] is not None]
    tv = rng.choice([sum(tot_day) - 5, sum(tot_day) + 5])
    cands.append((f"The clinic saw more than {tv} patients over the three days.", sum(tot_day) > tv))
    rng.shuffle(cands)
    yes = [c for c in cands if c[1]]; no = [c for c in cands if not c[1]]
    if len(yes) < 2 or len(no) < 2:
        return dm_interpret(rng)
    ny = rng.choice([2, 3])
    ny = max(5 - len(no), min(ny, len(yes)))
    pick = yes[:ny] + no[:5 - ny]
    if len(pick) < 5:
        return dm_interpret(rng)
    rng.shuffle(pick)
    exp = (f"Day totals: {', '.join(f'{x} {t}' for x, t in zip(days, tot_day))} (all {sum(tot_day)}). "
           f"Group totals: {', '.join(f'{x} {t}' for x, t in zip(groups, tot_grp))}.")
    return {"type": "yn", "stem": stem, "q": "Place 'Yes' if the statement is supported by the table, or 'No' if it is not.",
            "statements": [p[0] for p in pick], "answers": [p[1] for p in pick], "exp": exp}


def dm_generated(counts, seed):
    """counts: dict kind -> number. Returns list of items."""
    rng = random.Random(seed)
    fn = {"syll": dm_syllogism, "order": dm_order, "venn": dm_venn, "prob": dm_prob, "interp": dm_interpret}
    out = []
    for k, n in counts.items():
        seen = set()
        while n:
            it = fn[k](rng)
            sig = it["q"] + str(it.get("statements"))
            if sig in seen: continue
            seen.add(sig); out.append(it); n -= 1
    return out
