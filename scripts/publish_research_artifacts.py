from __future__ import annotations

from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]

DETAILS = {
    "research/does-taxing-wealth-harm-workers.html": {
        "source": "Recovered final PDF · August 2026",
        "headline": "The repeal episodes do not show the investment-and-wage boom the simple worker-incidence story would predict.",
        "metrics": [
            ("+0.48 pp", "Investment-share change", "95% CI −1.15 to 2.10 pp"),
            ("+0.04 pp", "Capital/worker growth", "95% CI −0.52 to 0.60 pp"),
            ("−2.69%", "Labour compensation/worker", "95% CI −6.68% to 1.30%"),
            ("+0.56%", "Employment", "95% CI −2.95% to 4.08%"),
        ],
        "note": "Six-country wealth-tax repeal event study plus causal-evidence synthesis. The intervals are deliberately shown because the exercise is informative precisely when it refuses to convert imprecision into certainty.",
    },
    "research/when-r-beats-g.html": {
        "source": "Latest recovered long-form draft · July 2026 · 17 pages",
        "headline": "The return of concentration is most pronounced at the extreme tail, while conventional poverty measures can tell a much more optimistic story than a living-cost-aware standard.",
        "metrics": [
            ("9.70%", "US top 0.01% wealth share", "2024"),
            ("3.43%", "UK top 0.01% wealth share", "2024"),
            ("12.36%", "US conditional 2040 scenario", "Trend continuation, not unconditional forecast"),
            ("4.52%", "UK conditional 2040 scenario", "Trend continuation, not unconditional forecast"),
        ],
        "note": "Uses World Inequality Database, US Census and UK DWP evidence. The paper separates wealth stocks, wealth shares, income and material living standards instead of treating them as interchangeable nouns for 'the economy'.",
    },
    "research/beyond-fairness-inequality-efficiency-failure.html": {
        "source": "Recovered final PDF · August 2026",
        "headline": "The paper asks when inequality becomes a problem of resource allocation and foregone output, not merely a question of who receives the output.",
        "metrics": [
            ("24", "Advanced economies", "Panel evidence"),
            ("1975–2023", "Panel span", "Long-run macro evidence"),
            ("2.19 pp", "Diagnostic compensation/productivity gap", "Rent-shift episode association"),
            ("p = .031", "Wild-cluster bootstrap", "Diagnostic, not causal identification"),
        ],
        "note": "Mechanisms include talent misallocation, unequal access to innovation, housing constraints, market power, debt-financed demand and political feedback. Identification strength is stated mechanism by mechanism rather than blended into one heroic coefficient.",
    },
    "research/non-austerity-fiscal-savings-state-balance-sheet-reform.html": {
        "source": "Recovered revised final White Paper I · 9 August 2026",
        "headline": "The fiscal-capacity exercise moves away from generic austerity and toward institution-specific balance-sheet and leakage reforms.",
        "metrics": [
            ("£8bn", "Central annual package", "Around 2030"),
            ("£5bn", "Conservative case", "Approximate annual capacity"),
            ("£12bn", "Upper case", "Approximate annual capacity"),
            ("£4.5bn", "Tiered reserve remuneration", "Central 2030 estimate"),
        ],
        "note": "Quantitative tightening is explicitly not scored as permanent fiscal space. The revised paper distinguishes recurring savings from balance-sheet timing effects, a surprisingly useful habit when dealing with government arithmetic.",
    },
    "research/progressive-wealth-taxation-enforcement-asset-transparency.html": {
        "source": "Recovered revised final White Paper II · 9 August 2026",
        "headline": "The revised design cuts the earlier headline revenue estimate and builds enforcement, valuation and behavioural response into the tax base itself.",
        "metrics": [
            ("£6bn", "Central wealth-tax yield", "High-threshold design"),
            ("£4–9bn", "Revenue range", "Behaviour and enforcement uncertainty"),
            ("£8.4bn", "Revised broader package", "Net 2030 central estimate"),
            ("Revised", "Scoring status", "Earlier revenue estimate reduced materially"),
        ],
        "note": "The point of the revision is credibility rather than maximal yield. Avoidance and asset transparency are treated as part of the policy mechanism, not as awkward paragraphs appended after the number everyone screenshots.",
    },
    "research/productivity-enhancing-public-investment-policy.html": {
        "source": "Recovered final White Paper III · 10 August 2026",
        "headline": "The programme separates what government spends today from uncertain future productivity effects, then models those effects as scenarios rather than free financing.",
        "metrics": [
            ("£20bn", "Central additional investment", "Annual level by 2030"),
            ("£35bn", "Ambitious case", "Annual level"),
            ("+0.25%", "Real GDP level", "Central scenario, 2030"),
            ("+1.2%", "Real GDP level", "Central scenario, 2036"),
        ],
        "note": "Project selection, implementation constraints and financing are kept separate from the modelled growth dividend. Future GDP is not treated as a cheque that has already cleared.",
    },
    "research/new-uk-fiscal-and-investment-programme.html": {
        "source": "Recovered final consolidated policy brief · 10 August 2026",
        "headline": "The three-policy programme is assembled into one explicit financing identity rather than a stack of individually attractive announcements.",
        "metrics": [
            ("£15.5bn", "Net fiscal capacity", "Central 2030 estimate"),
            ("£20bn", "Additional public investment", "Central annual programme"),
            ("£4.5bn", "Direct borrowing", "Explicit residual financing"),
            ("3", "Integrated policy strands", "Balance sheet, tax, investment"),
        ],
        "note": "The consolidated brief makes sequencing and financing visible. That matters because policy packages have an unfortunate tendency to add the benefits together and quietly misplace the constraints.",
    },
    "research/inequality-is-not-just-unfair-it-is-expensive.html": {
        "source": "Recovered final public-facing essay · 2026",
        "headline": "A readable synthesis of the efficiency case: unequal access can waste talent and inventions, rents can suppress dynamism, and concentrated saving can weaken demand rather than mechanically funding productive investment.",
        "metrics": [
            ("Talent", "Allocation channel", "Who gets to become an inventor"),
            ("Rents", "Market-power channel", "Markup and dynamism evidence"),
            ("Housing", "Spatial channel", "Access and misallocation"),
            ("Demand", "Macro-finance channel", "Saving concentration and debt"),
        ],
        "note": "This is the public-facing companion to the empirical paper. It keeps normative arguments and efficiency evidence distinct, because shouting 'fairness' at a regression has historically produced limited identification gains.",
    },
    "research/deep-hedging-privileged-factor-composition.html": {
        "source": "Recovered complete research draft · 17 August 2026",
        "headline": "Giving the hedge exact latent Lifted-Heston factor composition did not improve the policy. It made the hedge worse and more expensive to trade.",
        "metrics": [
            ("+6.95%", "Paired MSE", "Factor policy vs scalar policy"),
            ("5 / 5", "Maturity buckets", "Factor policy worse at 1 bp"),
            ("Higher", "Turnover", "Factor policy"),
            ("Higher", "Trading cost", "Factor policy"),
        ],
        "note": "The result is intentionally simulator-conditional. Exact Lifted-Heston factors are privileged states, not observable market inputs. The negative result is useful evidence about representation, not a failed attempt to produce a prettier neural-network story.",
    },
    "research/professional-quant-literature-review.html": {
        "source": "Standalone final artefact not confidently recovered · integrated into final dissertation",
        "headline": "The review survives inside the final dissertation as the conceptual bridge from continuous replication to stochastic volatility, rough/lifted representations, deep hedging, transaction costs and maturity sharing.",
        "metrics": [
            ("BS", "Classical baseline", "Continuous replication"),
            ("Heston", "Scalar stochastic volatility", "Markov benchmark"),
            ("Lifted", "Memory-rich volatility", "Finite-factor approximation"),
            ("Costs", "Empirical object", "Dynamic hedging under frictions"),
        ],
        "note": "Rather than inventing a standalone 'final' file because the portfolio wants one, this page records that the recoverable final version is integrated into the submitted dissertation research programme.",
    },
    "reports/observable-deep-hedging-spx-straddles.html": {
        "source": "Recovered final dissertation PDF · August 2026",
        "headline": "Simulation pretraining and maturity sharing produce the strongest risk-control point estimate, but the statistical evidence does not support advertising a confirmed neural edge.",
        "metrics": [
            ("0.154984", "Premium-normalised MSE", "Best pooled Lifted-Heston sim-only policy"),
            ("0.185212", "Black-Scholes delta MSE", "1 bp stock cost"),
            ("−16.3%", "Point-estimate MSE reduction", "Vs Black-Scholes delta"),
            ("719,370", "Audited result rows", "Float64 accounting export"),
        ],
        "note": "The paired MSE contrast is nominally favourable but no neural-versus-baseline contrast survives Holm adjustment. The dissertation therefore reports a reproducible candidate risk-control policy, not a deployable trading strategy.",
    },
}

WORK_ORDER = [
    ("Quantitative finance", "reports/observable-deep-hedging-spx-straddles.html", "Observable Deep Hedging of SPX Straddles"),
    ("Quantitative finance", "research/deep-hedging-privileged-factor-composition.html", "Deep Hedging under Lifted Heston: Privileged Factor Composition"),
    ("Market microstructure", "reports/quote-replenishment-hysteresis.html", "Quote-Replenishment Hysteresis"),
    ("Political economy", "research/does-taxing-wealth-harm-workers.html", "Does Taxing Wealth Harm Workers?"),
    ("Political economy", "research/when-r-beats-g.html", "When r Beats g"),
    ("Political economy", "research/beyond-fairness-inequality-efficiency-failure.html", "Beyond Fairness: Inequality as an Efficiency Failure"),
    ("UK fiscal programme", "research/non-austerity-fiscal-savings-state-balance-sheet-reform.html", "White Paper I · Non-Austerity Fiscal Reform"),
    ("UK fiscal programme", "research/progressive-wealth-taxation-enforcement-asset-transparency.html", "White Paper II · Progressive Wealth Taxation"),
    ("UK fiscal programme", "research/productivity-enhancing-public-investment-policy.html", "White Paper III · Productivity-Enhancing Public Investment"),
    ("UK fiscal programme", "research/new-uk-fiscal-and-investment-programme.html", "A New UK Fiscal and Investment Programme"),
    ("Political economy", "research/inequality-is-not-just-unfair-it-is-expensive.html", "Inequality Is Not Just Unfair. It Is Expensive."),
]

ACADEMIC = [
    ("WSJ Sentiment → Cross-Sectional Alpha", "/reports/wsj-sentiment-analysis.html", "Financial NLP · roughly 146k headlines · FinBERT / TF-IDF / factor diagnostics"),
    ("Systematic Strategy Allocation Review", "/reports/systematic-strategy-allocation-review.html", "Institutional due diligence · factor attribution · tail and regime risk"),
    ("Lending Club Credit Risk Research", "/reports/lending-club-credit-risk.html", "XGBoost · leakage-safe validation · economically optimised threshold"),
    ("Market Prediction & Dynamic Allocation", "/reports/market-prediction-dynamic-allocation.html", "Time-aware validation · linear / recurrent models · allocation under non-stationarity"),
    ("Asset Pricing, Trading & Portfolio Construction", "/reports/asset-pricing-trading-portfolio-construction.html", "Factor regressions · Fama-MacBeth · rolling long-short construction"),
    ("Advanced Asset Pricing & Modelling", "/reports/advanced-asset-pricing-modelling.html", "Assessed research page; original university submission remains private"),
    ("Big Data Applications for Finance", "/reports/big-data-applications-finance.html", "Assessed research page; original university submission remains private"),
    ("Economic Growth × Income Inequality", "/reports/growth-inequality.html", "BSc dissertation · cross-country panel econometrics"),
    ("UK Public Debt: How Much Is Too Much?", "/reports/uk-public-debt.html", "Interactive public-finance data project"),
    ("Abenomics", "/reports/abenomics.html", "Earlier political-economy research on Japan's macro policy mix"),
]

MICROSTRUCTURE = {
    "source": "Public research report · 2026",
    "headline": "The path of displayed-liquidity recovery contains information that the endpoint Level-1 state throws away on the fixed ETHUSDT benchmark.",
    "metrics": [
        ("11,874", "OOS forecasts", "Four chronological folds"),
        ("−1.15%", "Pooled log loss", "Snapshot + recovery path"),
        ("4 / 4", "Fold wins", "Log-loss comparison"),
        ("66.8→95.5%", "Continuation probability", "Across SRA deciles"),
    ],
    "note": "The report interprets this as a microstructure mechanism on the benchmark, not executable alpha. Apparently even a successful backtest can be denied the right to cosplay as a hedge fund.",
}


def evidence_html(detail: dict[str, object]) -> str:
    metrics = "".join(
        f'<div class="evidence-metric"><strong>{escape(str(value))}</strong><span>{escape(label)}</span><small>{escape(context)}</small></div>'
        for value, label, context in detail["metrics"]
    )
    return f'''<section class="section frame evidence-section"><span class="section-no">04 / Recovered evidence</span><div><h2>What the final work actually says.</h2><p class="lead">{escape(str(detail["headline"]))}</p><div class="recovered-source">{escape(str(detail["source"]))}</div><div class="evidence-grid">{metrics}</div><div class="note"><span>READING NOTE</span><p>{escape(str(detail["note"]))}</p></div></div></section>'''


def patch_page(path: str, detail: dict[str, object]) -> None:
    target = ROOT / path
    if not target.exists():
        return
    html = target.read_text(encoding="utf-8")
    if "04 / Recovered evidence" in html:
        return
    insert = evidence_html(detail)
    marker = "</main>"
    if marker in html:
        html = html.replace(marker, insert + "\n" + marker, 1)
    target.write_text(html, encoding="utf-8")


def add_evidence_css() -> None:
    css = ROOT / "assets" / "research-page.css"
    if not css.exists():
        return
    text = css.read_text(encoding="utf-8")
    token = ".evidence-grid{"
    if token in text:
        return
    text += '''\n.evidence-section{background:linear-gradient(180deg,rgba(184,255,101,.018),transparent 70%)}.recovered-source{margin:24px 0 14px;color:#b8ff65;font:600 10px/1.4 ui-monospace,SFMono-Regular,Menlo,monospace;text-transform:uppercase;letter-spacing:.09em}.evidence-grid{display:grid;grid-template-columns:repeat(4,1fr);border:1px solid #2b2e32;margin:0 0 28px}.evidence-metric{padding:18px;border-right:1px solid #2b2e32}.evidence-metric:last-child{border-right:0}.evidence-metric strong{display:block;color:#f3f5ee;font:500 24px/1.1 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:-.04em}.evidence-metric span,.evidence-metric small{display:block}.evidence-metric span{margin-top:9px;color:#9ca29a;font:600 9px/1.35 ui-monospace,SFMono-Regular,Menlo,monospace;text-transform:uppercase;letter-spacing:.07em}.evidence-metric small{margin-top:5px;color:#6f756e;font-size:10px;line-height:1.4}@media(max-width:760px){.evidence-grid{grid-template-columns:1fr 1fr}.evidence-metric:nth-child(2){border-right:0}.evidence-metric{border-bottom:1px solid #2b2e32}}\n'''
    css.write_text(text, encoding="utf-8")


def render_card(group: str, path: str, title: str, detail: dict[str, object]) -> str:
    first = detail["metrics"][0]
    return f'''<article class="work-card"><div class="work-main"><div class="eyebrow">{escape(group)} · {escape(str(detail["source"]))}</div><h2>{escape(title)}</h2><p class="summary">{escape(str(detail["headline"]))}</p><div class="finding"><span>Evidence</span><p>{escape(str(detail["note"]))}</p></div><div class="actions"><a class="button primary" href="/{escape(path, quote=True)}">Open research page →</a></div></div><aside class="metric"><strong>{escape(str(first[0]))}</strong><span>{escape(str(first[1]))}</span><small>{escape(str(first[2]))}</small></aside></article>'''


def render_work_page() -> str:
    chunks = []
    last_group = None
    for group, path, title in WORK_ORDER:
        detail = MICROSTRUCTURE if path == "reports/quote-replenishment-hysteresis.html" else DETAILS[path]
        if group != last_group:
            chunks.append(f'<div class="group-label"><span>{escape(group)}</span></div>')
            last_group = group
        chunks.append(render_card(group, path, title, detail))
    rows = "".join(f'<a class="archive-row" href="{escape(url, quote=True)}"><strong>{escape(title)}</strong><span>{escape(desc)}</span><b>→</b></a>' for title, url, desc in ACADEMIC)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Selected Work · Hikari Kawase Kennedy</title><meta name="description" content="Recovered research papers, quantitative reports and academic project pages by Hikari Kawase Kennedy."><meta name="theme-color" content="#0a0b0d"><style>
*{{box-sizing:border-box}}html{{background:#0a0b0d;scroll-behavior:smooth}}body{{margin:0;background:#0a0b0d;color:#f0f1ec;font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}a{{color:inherit;text-decoration:none}}::selection{{background:#b8ff65;color:#0a0b0d}}.frame{{width:min(1260px,calc(100% - 56px));margin:auto}}.nav{{height:74px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #25282d;font:600 10px/1 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.1em;text-transform:uppercase}}.nav div{{display:flex;gap:24px;color:#8d938b}}.nav a:hover{{color:#b8ff65}}.hero{{padding:96px 0 82px;border-bottom:1px solid #25282d}}.kicker,.eyebrow,.group-label{{font:600 10px/1.3 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.12em;text-transform:uppercase;color:#8a9088}}.kicker{{color:#b8ff65}}h1{{max-width:1040px;margin:22px 0 28px;font-size:clamp(58px,8vw,116px);line-height:.88;letter-spacing:-.065em;font-weight:580}}.hero p{{max-width:840px;margin:0;color:#a0a59e;font-size:clamp(18px,2vw,26px);line-height:1.45;letter-spacing:-.02em}}.hero-stats{{margin-top:52px;display:grid;grid-template-columns:repeat(3,1fr);border:1px solid #2b2e32;max-width:760px}}.hero-stats div{{padding:18px;border-right:1px solid #2b2e32}}.hero-stats div:last-child{{border-right:0}}.hero-stats strong{{display:block;color:#b8ff65;font:500 28px/1 ui-monospace,SFMono-Regular,Menlo,monospace}}.hero-stats span{{display:block;margin-top:8px;color:#727970;font:600 9px/1.3 ui-monospace,SFMono-Regular,Menlo,monospace;text-transform:uppercase;letter-spacing:.08em}}.library{{padding:86px 0 120px}}.intro{{display:grid;grid-template-columns:1.1fr .9fr;gap:80px;align-items:end;margin-bottom:64px}}.intro h2,.archive h2{{margin:12px 0 0;font-size:clamp(38px,5vw,72px);line-height:.98;letter-spacing:-.05em;font-weight:540}}.intro p{{margin:0;color:#899087;font-size:14px;line-height:1.75}}.group-label{{padding:38px 0 14px;color:#b8ff65;border-bottom:1px solid #2a2d31}}.work-card{{display:grid;grid-template-columns:1fr 220px;gap:54px;padding:46px 0;border-bottom:1px solid #2a2d31}}.work-main h2{{max-width:920px;margin:12px 0 18px;font-size:clamp(28px,3.3vw,48px);line-height:1.03;letter-spacing:-.04em;font-weight:540}}.summary{{max-width:850px;margin:0;color:#a0a59d;font-size:14px;line-height:1.7}}.finding{{max-width:920px;margin:27px 0 30px;padding-top:18px;border-top:1px solid #272b2e;display:grid;grid-template-columns:90px 1fr;gap:18px}}.finding span{{color:#b8ff65;font:600 9px/1.3 ui-monospace,SFMono-Regular,Menlo,monospace;text-transform:uppercase;letter-spacing:.1em}}.finding p{{margin:0;color:#d1d4ce;font-size:13px;line-height:1.65}}.button{{display:inline-block;padding:11px 13px;border:1px solid #596b49;color:#b8ff65;font:600 9px/1 ui-monospace,SFMono-Regular,Menlo,monospace;text-transform:uppercase;letter-spacing:.06em;transition:.2s ease}}.button:hover{{background:#b8ff65;border-color:#b8ff65;color:#0a0b0d}}.metric{{align-self:center;border-left:1px solid #2d3135;padding:12px 0 12px 30px}}.metric strong{{display:block;color:#f2f4ed;font:500 clamp(28px,3vw,42px)/1 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:-.05em}}.metric span,.metric small{{display:block}}.metric span{{margin-top:9px;color:#8b9189;font:600 9px/1.4 ui-monospace,SFMono-Regular,Menlo,monospace;text-transform:uppercase;letter-spacing:.08em}}.metric small{{margin-top:6px;color:#656b64;font-size:10px;line-height:1.4}}.archive{{padding:100px 0;border-top:1px solid #25282d}}.archive h2{{margin-bottom:44px}}.archive-list{{border-top:1px solid #2a2d31}}.archive-row{{display:grid;grid-template-columns:minmax(240px,.9fr) 1.5fr 24px;gap:28px;align-items:center;min-height:82px;border-bottom:1px solid #2a2d31;transition:.2s ease}}.archive-row:hover{{background:#111316}}.archive-row strong{{font-size:14px;font-weight:560}}.archive-row span{{color:#858b83;font-size:12px;line-height:1.5}}.archive-row b{{color:#b8ff65;font-weight:500}}.note{{margin-top:36px;padding:18px 20px;border:1px solid #303438;color:#8d938b;font-size:12px;line-height:1.7}}.footer{{height:94px;border-top:1px solid #25282d;display:flex;justify-content:space-between;align-items:center;color:#6d736c;font:600 9px/1 ui-monospace,SFMono-Regular,Menlo,monospace;text-transform:uppercase;letter-spacing:.09em}}.footer a{{color:#b8ff65}}@media(max-width:800px){{.frame{{width:calc(100% - 28px)}}.nav div{{display:none}}.hero{{padding-top:68px}}.hero-stats{{grid-template-columns:1fr}}.hero-stats div{{border-right:0;border-bottom:1px solid #2b2e32}}.intro{{grid-template-columns:1fr;gap:28px}}.work-card{{grid-template-columns:1fr;gap:24px}}.metric{{border-left:0;border-top:1px solid #2d3135;padding:22px 0 0}}.finding{{grid-template-columns:1fr;gap:8px}}.archive-row{{grid-template-columns:1fr 24px;padding:18px 0}}.archive-row span{{grid-column:1/3;grid-row:2}}}}
</style></head><body><header class="nav frame"><a href="/">HKK / Portfolio</a><div><a href="#work">Recovered work</a><a href="#archive">Project archive</a><a href="https://github.com/lhkkennedy" target="_blank" rel="noreferrer">GitHub ↗</a></div></header><main><section class="hero frame"><div class="kicker">Selected work / recovered research archive</div><h1>The work,<br>not just the bullet point.</h1><p>Research pages grounded in the final or latest recoverable artefacts from my research archive, with the methods, caveats and headline evidence brought onto the web rather than left hiding behind a portfolio title.</p><div class="hero-stats"><div><strong>10</strong><span>Recovered research artefacts</span></div><div><strong>4</strong><span>Research strands</span></div><div><strong>10+</strong><span>Additional project pages</span></div></div></section><section class="library frame" id="work"><div class="intro"><div><div class="kicker">01 / Recovered work</div><h2>Research with<br>evidence attached.</h2></div><p>The underlying ChatGPT research archive was used to recover the latest defensible version of each item and restore the actual results to its public research page. Where only a draft or an integrated dissertation section could be recovered, that status is stated explicitly.</p></div>{''.join(chunks)}</section><section class="archive" id="archive"><div class="frame"><div class="kicker">02 / Academic & project archive</div><h2>The wider<br>portfolio.</h2><div class="archive-list">{rows}</div><div class="note">Assessed university submissions that were not already public remain private. Their public research pages show the question, methodology and contribution without uploading assessment files that were never intended for open distribution.</div></div></section></main><footer class="footer frame"><span>Hikari Kawase Kennedy · Quantitative Research</span><a href="/">Portfolio ↑</a></footer></body></html>'''


def patch_home() -> None:
    index = ROOT / "index.html"
    if not index.exists():
        return
    html = index.read_text(encoding="utf-8")
    old = '<nav aria-label="Primary navigation"><a href="#research">Research</a>'
    new = '<nav aria-label="Primary navigation"><a href="/work/">Work</a><a href="#research">Research</a>'
    if old in html and 'href="/work/"' not in html:
        html = html.replace(old, new, 1)
    index.write_text(html, encoding="utf-8")


def main() -> None:
    add_evidence_css()
    for path, detail in DETAILS.items():
        patch_page(path, detail)
    work = ROOT / "work" / "index.html"
    work.parent.mkdir(parents=True, exist_ok=True)
    work.write_text(render_work_page(), encoding="utf-8")
    patch_home()


if __name__ == "__main__":
    main()
