from __future__ import annotations

from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PAGES = [
    {
        "path": "research/does-taxing-wealth-harm-workers.html",
        "title": "Does Taxing Wealth Harm Workers?",
        "type": "Independent research paper",
        "year": "2026",
        "domain": "Public economics · taxation · investment · labour incidence",
        "deck": "Capital Flight, Productive Investment and Wage Incidence: a causal-evidence synthesis and OECD wealth-tax repeal study.",
        "question": "Do recurrent claims that wealth taxation harms workers survive scrutiny once the argument is decomposed into capital flight, productive investment, capital deepening, productivity, wages and employment?",
        "approach": "The paper combines a causal-evidence synthesis with a public-data event study around six European wealth-tax repeals. The design treats repeal episodes as evidence to interrogate transmission channels rather than assuming the incidence of a wealth tax in advance.",
        "takeaway": "The contribution is the structure of the test: worker effects must be demonstrated through observable investment and labour-market mechanisms, not inferred mechanically from a tax being levied on wealth.",
        "status": "Independent paper · research page",
    },
    {
        "path": "research/when-r-beats-g.html",
        "title": "When r Beats g",
        "type": "Independent research paper / long-form draft",
        "year": "2026",
        "domain": "Wealth inequality · living standards · poverty",
        "deck": "Wealth concentration, living standards and poverty in the United States and United Kingdom.",
        "question": "How does rising concentration at the top of the wealth distribution relate to living standards and poverty outcomes in the US and UK?",
        "approach": "The research combines World Inequality Database series with US Census and UK Department for Work and Pensions evidence, keeping wealth concentration, income conditions and poverty measures conceptually separate before connecting them.",
        "takeaway": "The paper is designed to prevent aggregate prosperity from standing in for household welfare. Distribution, living standards and poverty are treated as linked but distinct empirical objects.",
        "status": "Independent paper · long-form draft",
    },
    {
        "path": "research/beyond-fairness-inequality-efficiency-failure.html",
        "title": "Beyond Fairness: Inequality as an Efficiency Failure",
        "type": "Independent research paper · Part II",
        "year": "2026",
        "domain": "Inequality · productivity · political economy",
        "deck": "When inequality stops being only a distributional outcome and starts becoming an efficiency problem.",
        "question": "Under what conditions does inequality reduce economic efficiency rather than merely alter who receives the gains from growth?",
        "approach": "A 24-country advanced-economy panel is paired with a mechanism review covering channels through productivity, human capital, demand, political economy and the allocation of opportunity.",
        "takeaway": "The project reframes the debate from fairness alone to testable macroeconomic mechanisms through which concentration can affect the level and quality of economic performance.",
        "status": "Independent paper · Part II",
    },
    {
        "path": "research/non-austerity-fiscal-savings-state-balance-sheet-reform.html",
        "title": "New Non-Austerity Fiscal Savings and State Balance-Sheet Reform",
        "type": "White Paper I · Independent UK Fiscal and Economic Policy Agenda",
        "year": "2026",
        "domain": "Fiscal policy · monetary-fiscal institutions · public-sector balance sheet",
        "deck": "Finding fiscal capacity without treating broad public-service cuts as the default adjustment mechanism.",
        "question": "What credible sources of UK fiscal capacity exist outside conventional broad-based austerity?",
        "approach": "The paper examines reserve remuneration, the treatment of quantitative tightening, commercial leakage, PFI and subsidy reform as balance-sheet and institutional levers. Financing arithmetic is kept distinct from any wider macroeconomic effects.",
        "takeaway": "The paper's core contribution is a menu of institutionally specific savings and balance-sheet reforms that can be assessed individually rather than bundled into a generic spending-cut target.",
        "status": "White Paper I",
    },
    {
        "path": "research/progressive-wealth-taxation-enforcement-asset-transparency.html",
        "title": "Progressive Wealth Taxation, Enforcement and Global Asset Transparency",
        "type": "White Paper II · Independent UK Fiscal and Economic Policy Agenda",
        "year": "2026",
        "domain": "Wealth taxation · enforcement · asset transparency",
        "deck": "A wealth-tax design that treats enforcement, avoidance and behavioural response as first-order constraints.",
        "question": "How can a progressive wealth tax be designed so that the headline rate, tax base and expected revenue remain credible once avoidance and enforcement are taken seriously?",
        "approach": "The framework develops the tax alongside valuation, behavioural response, enforcement, avoidance and asset-transparency constraints instead of appending those issues after the revenue estimate.",
        "takeaway": "The design principle is implementation realism: the policy is judged by the enforceable base and behavioural system around it, not by a frictionless statutory schedule.",
        "status": "White Paper II",
    },
    {
        "path": "research/productivity-enhancing-public-investment-policy.html",
        "title": "Productivity-Enhancing Public Investment Policy",
        "type": "White Paper III · Independent UK Fiscal and Economic Policy Agenda",
        "year": "2026",
        "domain": "Public investment · productivity · fiscal policy",
        "deck": "Designing additional public investment while separating financing arithmetic from modelled growth effects.",
        "question": "How should an additional UK public-investment programme be structured if the objective is persistent productivity improvement rather than simply a larger capital budget?",
        "approach": "The paper separates project selection and implementation constraints from financing, then treats any medium-run growth dividend as a modelled effect rather than immediate budgetary cash.",
        "takeaway": "The work insists on a useful accounting distinction: investment can be justified by productivity and welfare effects without pretending uncertain future growth has already financed today's programme.",
        "status": "White Paper III",
    },
    {
        "path": "research/new-uk-fiscal-and-investment-programme.html",
        "title": "A New UK Fiscal and Investment Programme",
        "type": "Consolidated policy brief",
        "year": "2026",
        "domain": "Fiscal strategy · taxation · investment · political economy",
        "deck": "A single financing and implementation framework linking non-austerity fiscal reform, progressive taxation and additional public investment.",
        "question": "Can the separate fiscal-capacity, tax and investment proposals be assembled into one internally coherent UK policy programme?",
        "approach": "The brief consolidates the three white-paper strands into one sequencing, financing and implementation framework, making the interaction between savings, taxation and investment explicit.",
        "takeaway": "Its value is synthesis: each policy lever is presented as part of a joined-up balance-sheet and implementation programme rather than as a standalone revenue headline.",
        "status": "Independent policy brief",
    },
    {
        "path": "research/inequality-is-not-just-unfair-it-is-expensive.html",
        "title": "Inequality Is Not Just Unfair. It Is Expensive.",
        "type": "Public-facing economics essay · Part II",
        "year": "2026",
        "domain": "Inequality · productivity · political economy",
        "deck": "A long-form synthesis translating the inequality-efficiency research programme into an accessible economics argument.",
        "question": "Can the empirical case that inequality may carry efficiency costs be explained clearly without collapsing the evidence into a slogan?",
        "approach": "The essay translates the mechanism and cross-country evidence from the wider research programme into public-facing prose while preserving the distinction between normative claims and empirical efficiency effects.",
        "takeaway": "The piece is deliberately communicative rather than model-heavy: it makes the research legible without pretending that accessibility removes uncertainty or identification problems.",
        "status": "Public-facing research essay",
    },
    {
        "path": "research/deep-hedging-privileged-factor-composition.html",
        "title": "Deep Hedging under Lifted Heston: Does Privileged Factor Composition Improve Stock-Only Hedging?",
        "type": "Dissertation companion research draft",
        "year": "2026",
        "domain": "Derivatives · stochastic volatility · information sets · machine learning",
        "deck": "A simulator-conditional experiment on whether lifted-Heston factor composition adds hedging information beyond aggregate observable state.",
        "question": "If two simulated states look identical in aggregate observables, does privileged knowledge of lifted-Heston factor composition improve a stock-only hedge?",
        "approach": "The experiment is deliberately simulator-conditional. It augments the observable hedging state with latent factor-composition information inside the lifted-Heston environment and asks whether that privileged information changes hedge quality.",
        "takeaway": "This is an information-set experiment, not evidence that latent simulator states are available in live markets. Its purpose is to diagnose whether factor composition contains incremental hedging information.",
        "status": "Companion research draft",
        "external_url": "https://github.com/lhkkennedy/Deep-Hedging-under-Lifted-Heston-MSc-Dissertation-",
        "external_label": "Related dissertation repository",
    },
    {
        "path": "research/professional-quant-literature-review.html",
        "title": "Professional Quant Literature Review",
        "type": "Technical literature review",
        "year": "2026",
        "domain": "Derivatives · stochastic volatility · deep hedging",
        "deck": "From Black–Scholes and Heston through rough and lifted volatility to transaction-cost-aware deep hedging.",
        "question": "What parts of the option-hedging literature matter most when moving from continuous-time theory to observable, transaction-cost-aware empirical hedging?",
        "approach": "The review synthesises classical delta hedging, stochastic volatility, rough and lifted-Heston approximations, deep hedging, market frictions and empirical implementation choices.",
        "takeaway": "The review functions as the conceptual spine of the dissertation programme: it identifies where model assumptions, information sets and trading frictions change the economic meaning of a hedging result.",
        "status": "Technical literature review",
    },
    {
        "path": "reports/observable-deep-hedging-spx-straddles.html",
        "title": "Observable Deep Hedging of SPX Straddles under Transaction Costs",
        "type": "MSc dissertation · ECOM107",
        "year": "2026",
        "domain": "Derivatives · machine learning · volatility · transaction costs",
        "deck": "Simulation pretraining, market learning and maturity pooling for observable-only stock hedging of short near-ATM SPX straddles.",
        "question": "Can observable-only neural policies improve cost-aware stock hedging of SPX straddles, and when do simulation pretraining and cross-maturity parameter sharing help?",
        "approach": "The dissertation studies five maturity buckets with daily stock rebalancing, transaction costs, observable state variables and Heston / lifted-Heston simulation sources. Neural policies are compared with vendor and Black–Scholes delta baselines under chronological evaluation.",
        "takeaway": "At 1 bp, the leading all-bucket point estimate has premium-normalised MSE 0.154984 versus 0.185212 for Black–Scholes delta, a 16.3% reduction. The dissertation explicitly treats this as a candidate risk-control effect: neural-versus-baseline contrasts do not survive Holm adjustment.",
        "status": "MSc dissertation · final research",
        "external_url": "https://github.com/lhkkennedy/Deep-Hedging-under-Lifted-Heston-MSc-Dissertation-",
        "external_label": "Research repository",
    },
    {
        "path": "reports/wsj-sentiment-analysis.html",
        "title": "WSJ Sentiment Analysis: State-Dependent Contrarian Returns",
        "type": "Group assignment · ECOM217",
        "year": "2026",
        "domain": "NLP · asset pricing · systematic investing",
        "deck": "Turning roughly 146,000 Wall Street Journal headlines into firm-level sentiment signals and testing where those signals actually survive.",
        "question": "Does financial-news sentiment predict cross-sectional equity returns consistently, or is the useful signal conditional on market state and attention?",
        "approach": "The project maps WSJ headlines to S&P 500 firms, compares TF-IDF + PCA + logistic regression with FinBERT sentiment and evaluates resulting stock-selection signals with out-of-sample performance and factor diagnostics.",
        "takeaway": "The research does not assume one stable sentiment premium. The strongest interpretation is state-dependent and contrarian, with attention and volatility conditioning the usefulness of the signal.",
        "status": "3,500-word group research assignment",
        "external_url": "https://github.com/lhkkennedy/WSJ-Sentiment-Driven-Trading-Strategy-Research",
        "external_label": "Research repository",
    },
    {
        "path": "reports/asset-pricing-trading-portfolio-construction.html",
        "title": "Asset Pricing, Trading & Portfolio Construction",
        "type": "Portfolio assignment · ECOM155",
        "year": "2026",
        "domain": "Asset pricing · factor models · portfolio construction",
        "deck": "Empirical asset-pricing tests and time-aware long-short strategy evaluation across industry portfolios.",
        "question": "How well do factor exposures explain cross-sectional industry returns, and how stable are momentum-beta portfolio rules when evaluated through time?",
        "approach": "The submission combines time-series factor regressions, Fama–MacBeth cross-sectional tests across 49 industry portfolios and rolling / expanding evaluation of a momentum-beta long-short strategy.",
        "takeaway": "The work connects asset-pricing inference to portfolio implementation instead of treating factor estimation and strategy construction as separate exercises.",
        "status": "Private assessed portfolio · research page only",
        "private_note": "The assessed university submission is intentionally not published. This page documents its research scope without exposing the original assessment file.",
    },
    {
        "path": "reports/systematic-strategy-allocation-review.html",
        "title": "Systematic Strategy Allocation Review",
        "type": "Written coursework · ECOM123",
        "year": "2026",
        "domain": "Systematic investing · risk · factor attribution",
        "deck": "Institutional-style due diligence on a decade-long live strategy track record against equity and macro CTA benchmarks.",
        "question": "Does the strategy add a sufficiently differentiated and robust return stream to justify an allocation once benchmark exposure, regimes and tail behaviour are examined?",
        "approach": "The report analyses 2,976 daily observations using S&P 500 and HFRI Macro CTA benchmarks, rolling risk, drawdowns, crisis regimes and trend, carry and VIX factor attribution.",
        "takeaway": "The strategy shows near-zero S&P beta and meaningful trend/carry exposure with a Sharpe around 0.57, but unstable volatility, negative skew and tail risk weaken the allocation case.",
        "status": "2,000-word written report",
        "external_url": "https://github.com/lhkkennedy/Systematic-Trading-Strategy-Review/blob/main/strategy_analysis.pdf",
        "external_label": "Open public PDF",
        "repo_url": "https://github.com/lhkkennedy/Systematic-Trading-Strategy-Review",
    },
    {
        "path": "reports/lending-club-credit-risk.html",
        "title": "Lending Club Credit Risk Research",
        "type": "Assignment / research report",
        "year": "2026",
        "domain": "Credit risk · machine learning · decision thresholds",
        "deck": "Leakage-safe default modelling where the decision threshold is evaluated as an economic choice rather than a classification afterthought.",
        "question": "Which credit model and decision threshold best separate default risk when class imbalance, leakage and lending economics are handled explicitly?",
        "approach": "Logistic regression, random forest and XGBoost are compared under leakage-safe preprocessing and class imbalance. Hyperparameters and the operating threshold are evaluated against discrimination metrics and a simplified lending-profit objective.",
        "takeaway": "Optuna-tuned XGBoost reached 0.7195 AUC. Threshold optimisation materially changed the economic objective, with the simplified analysis favouring a 0.40 operating threshold rather than the default classifier cut-off.",
        "status": "Financial ML research report",
        "external_url": "https://github.com/lhkkennedy/Lending-Club-Credit-Risk-Research/blob/main/credit_risk_research_report.pdf",
        "external_label": "Open public PDF",
        "repo_url": "https://github.com/lhkkennedy/Lending-Club-Credit-Risk-Research",
    },
    {
        "path": "reports/market-prediction-dynamic-allocation.html",
        "title": "Market Prediction & Dynamic Allocation under Non-Stationarity",
        "type": "Group project · ECOM197",
        "year": "2025–26",
        "domain": "Financial prediction · validation · allocation",
        "deck": "A market-prediction project that increasingly became a study of validation discipline and allocation under non-stationary noise.",
        "question": "Can noisy forward market returns be forecast robustly enough to support a dynamic allocation rule?",
        "approach": "The project compares OLS, LSTM and NTS-NOTEARS-informed specifications and moves from one-shot validation toward expanding-window time-series evaluation.",
        "takeaway": "The final lesson is methodological: robust evaluation and the allocation rule contributed more to credible performance than progressively more elaborate predictors.",
        "status": "Group project · financial ML",
        "external_url": "https://github.com/lhkkennedy/Hull-Tactical---Market-Prediction-Kaggle-Competition-2025",
        "external_label": "Research repository",
    },
    {
        "path": "reports/advanced-asset-pricing-modelling.html",
        "title": "Advanced Asset Pricing & Modelling — Written Coursework",
        "type": "Written coursework · ECOM044",
        "year": "2026",
        "domain": "Advanced empirical asset pricing and modelling",
        "deck": "Assessed written work in advanced empirical asset pricing and financial modelling.",
        "question": "How should advanced asset-pricing models be specified, interpreted and evaluated when the empirical assumptions matter as much as the fitted result?",
        "approach": "The submission applies the module's advanced empirical asset-pricing and modelling toolkit in written research form. The portfolio records the assessed work while keeping the university submission private.",
        "takeaway": "This page exists to make the written research visible as part of the portfolio without publishing an assessment file that was not intended for public distribution.",
        "status": "Private assessed coursework · research page only",
        "private_note": "The original assessed submission is intentionally not published.",
    },
    {
        "path": "reports/big-data-applications-finance.html",
        "title": "Big Data Applications for Finance — Individual Project",
        "type": "Individual project · ECOM151",
        "year": "2026",
        "domain": "Financial data science · machine learning",
        "deck": "Assessed individual work applying large-scale data and machine-learning methods to a finance problem.",
        "question": "How can large-scale data and machine-learning methods be turned into a defensible finance research workflow rather than a model-selection exercise?",
        "approach": "The project is retained as a distinct assessed research item. Its public portfolio description is deliberately conservative until the final submission title is defensibly matched to a public project or report.",
        "takeaway": "The important portfolio signal is the end-to-end financial data-science workflow. Specific claims are withheld here rather than guessed from adjacent repositories.",
        "status": "Private assessed individual project · research page only",
        "private_note": "The original assessed submission is intentionally not published and has not been force-matched to an unrelated public repository.",
    },
    {
        "path": "reports/growth-inequality.html",
        "title": "Economic Growth × Income Inequality",
        "type": "BSc dissertation · University of Bristol",
        "year": "Earlier research",
        "domain": "Macroeconomics · inequality · panel econometrics",
        "deck": "Cross-country panel research on the relationship between income inequality and economic growth.",
        "question": "What relationship between inequality and economic growth remains after accounting for persistent cross-country differences?",
        "approach": "The dissertation uses large cross-country datasets and fixed-effects panel econometrics to study the growth–inequality relationship.",
        "takeaway": "The project is the earlier econometric foundation of the later inequality research programme: it treats distribution as an empirical macroeconomic variable rather than only a normative concern.",
        "status": "BSc dissertation · research page",
        "private_note": "The original dissertation document is not currently published.",
    },
    {
        "path": "reports/uk-public-debt.html",
        "title": "UK Public Debt: How Much Is Too Much?",
        "type": "Data science submission · University of Bristol",
        "year": "2021",
        "domain": "Public finance · macroeconomics · fiscal policy",
        "deck": "An interactive public-finance project combining automated data collection, APIs and macroeconomic visualisation.",
        "question": "How should the scale and sustainability of UK public debt be understood through debt, deficits, borrowing, interest rates and the wider macroeconomic environment?",
        "approach": "The project combines APIs, scraping, automated data processing and interactive Vega visualisation with a narrative interpretation of UK fiscal sustainability.",
        "takeaway": "This was an early attempt to make economic research reproducible and explorable rather than leaving the evidence trapped in a static essay.",
        "status": "BSc data-science project",
        "external_url": "https://lhkkennedy.github.io/html/Debt/projectPage.html",
        "external_label": "Open original interactive project",
    },
    {
        "path": "reports/abenomics.html",
        "title": "Abenomics: Fiscal Stimulus, Quantitative Easing & Japan's Economic Policy",
        "type": "Economics extended essay / earlier research",
        "year": "Earlier research",
        "domain": "Political economy · macroeconomic policy · Japan",
        "deck": "An early policy study of Japan's attempt to escape stagnation through fiscal stimulus and unconventional monetary policy.",
        "question": "How coherent and effective was the Abenomics policy mix when fiscal expansion, quantitative easing and structural objectives are considered together?",
        "approach": "The essay studies the macroeconomic logic of the Abenomics programme through fiscal stimulus, unconventional monetary policy and their interaction with Japan's long-running growth and inflation problem.",
        "takeaway": "The work marks the beginning of the portfolio's political-economy strand: policy is analysed as a system of interacting institutions rather than a single instrument.",
        "status": "Earlier economics research · research page",
        "private_note": "The original extended essay document is not currently published.",
    },
]

LINKS = {
    "Does Taxing Wealth Harm Workers?": "/research/does-taxing-wealth-harm-workers.html",
    "When r Beats g": "/research/when-r-beats-g.html",
    "Beyond Fairness: Inequality as an Efficiency Failure": "/research/beyond-fairness-inequality-efficiency-failure.html",
    "New Non-Austerity Fiscal Savings and State Balance-Sheet Reform": "/research/non-austerity-fiscal-savings-state-balance-sheet-reform.html",
    "Progressive Wealth Taxation, Enforcement and Global Asset Transparency": "/research/progressive-wealth-taxation-enforcement-asset-transparency.html",
    "Productivity-Enhancing Public Investment Policy": "/research/productivity-enhancing-public-investment-policy.html",
    "A New UK Fiscal and Investment Programme": "/research/new-uk-fiscal-and-investment-programme.html",
    "Inequality Is Not Just Unfair. It Is Expensive.": "/research/inequality-is-not-just-unfair-it-is-expensive.html",
    "Deep Hedging under Lifted Heston: Does Privileged Factor Composition Improve Stock-Only Hedging?": "/research/deep-hedging-privileged-factor-composition.html",
    "Professional Quant Literature Review": "/research/professional-quant-literature-review.html",
    "Observable Deep Hedging of SPX Straddles under Transaction Costs": "/reports/observable-deep-hedging-spx-straddles.html",
    "Systematic Strategy Allocation Review": "/reports/systematic-strategy-allocation-review.html",
    "WSJ Sentiment Analysis / Alpha Hunter": "/reports/wsj-sentiment-analysis.html",
    "Credit Risk Machine Learning Research Report": "/reports/lending-club-credit-risk.html",
    "Hull Tactical Market Prediction": "/reports/market-prediction-dynamic-allocation.html",
    "Advanced Asset Pricing & Modelling — Written Coursework": "/reports/advanced-asset-pricing-modelling.html",
    "Big Data Applications for Finance — Individual Project": "/reports/big-data-applications-finance.html",
    "Asset Pricing, Trading & Portfolio Construction — Portfolio Submission": "/reports/asset-pricing-trading-portfolio-construction.html",
    "Growth × Inequality": "/reports/growth-inequality.html",
    "UK Public Debt": "/reports/uk-public-debt.html",
    "Abenomics — Economics Extended Essay": "/reports/abenomics.html",
}

CARD_LINKS = {
    "Deep Hedging SPX Straddles": ("/reports/observable-deep-hedging-spx-straddles.html", "https://github.com/lhkkennedy/Deep-Hedging-under-Lifted-Heston-MSc-Dissertation-"),
    "WSJ Sentiment → Cross-Sectional Alpha": ("/reports/wsj-sentiment-analysis.html", "https://github.com/lhkkennedy/WSJ-Sentiment-Driven-Trading-Strategy-Research"),
    "Systematic Strategy Allocation Review": ("/reports/systematic-strategy-allocation-review.html", "https://github.com/lhkkennedy/Systematic-Trading-Strategy-Review"),
    "Credit Risk Under Decision Costs": ("/reports/lending-club-credit-risk.html", "https://github.com/lhkkennedy/Lending-Club-Credit-Risk-Research"),
    "Hull Tactical Market Prediction": ("/reports/market-prediction-dynamic-allocation.html", "https://github.com/lhkkennedy/Hull-Tactical---Market-Prediction-Kaggle-Competition-2025"),
}

def link_button(url: str, label: str) -> str:
    return f'<a class="button" href="{escape(url, quote=True)}" target="_blank" rel="noreferrer">{escape(label)} ↗</a>'

def render_page(item: dict[str, str]) -> str:
    buttons = []
    if item.get("external_url"):
        buttons.append(link_button(item["external_url"], item.get("external_label", "Open source")))
    if item.get("repo_url"):
        buttons.append(link_button(item["repo_url"], "Repository"))
    buttons_html = "".join(buttons)
    private_html = ""
    if item.get("private_note"):
        private_html = f'<div class="note"><span>ACCESS</span><p>{escape(item["private_note"])}</p></div>'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(item["title"])} · Hikari Kawase Kennedy</title>
<meta name="description" content="{escape(item["deck"], quote=True)}">
<meta name="theme-color" content="#0a0b0d">
<link rel="stylesheet" href="/assets/research-page.css">
</head>
<body>
<header class="nav frame"><a href="/">HKK / Research</a><nav><a href="/#papers">Independent</a><a href="/#reports">Reports</a></nav></header>
<main>
<section class="hero frame">
<div class="kicker">{escape(item["type"])}</div>
<h1>{escape(item["title"])}</h1>
<p class="deck">{escape(item["deck"])}</p>
<div class="meta-grid">
<div><span>Year</span><strong>{escape(item["year"])}</strong></div>
<div><span>Domain</span><strong>{escape(item["domain"])}</strong></div>
<div><span>Status</span><strong>{escape(item["status"])}</strong></div>
</div>
<div class="actions">{buttons_html}<a class="button secondary" href="/">Portfolio ↑</a></div>
</section>
<section class="section frame"><span class="section-no">01 / Research question</span><div><h2>What is being tested?</h2><p class="lead">{escape(item["question"])}</p></div></section>
<section class="section frame"><span class="section-no">02 / Approach</span><div><h2>How the work is structured.</h2><p>{escape(item["approach"])}</p></div></section>
<section class="section frame"><span class="section-no">03 / Contribution</span><div><h2>What the work adds.</h2><p class="lead">{escape(item["takeaway"])}</p>{private_html}</div></section>
</main>
<footer class="footer frame"><span>Hikari Kawase Kennedy · Quantitative Research</span><a href="/">Portfolio ↑</a></footer>
</body>
</html>'''

def link_document_rows(html: str) -> str:
    for title, href in LINKS.items():
        muted = re.compile(
            r'<div class="document-row muted-row">(?P<body>.*?<strong>' + re.escape(title) +
            r'</strong>.*?<span class="arrow">—</span>)</div>'
        )
        def muted_repl(match, href=href):
            body = match.group("body").replace('<span class="arrow">—</span>', '<span class="arrow">↗</span>')
            return f'<a class="document-row link" href="{href}">{body}</a>'
        html = muted.sub(muted_repl, html, count=1)

        linked = re.compile(
            r'<a class="document-row link" href="[^"]+"(?: target="_blank" rel="noreferrer")?>'
            r'(?P<body>.*?<strong>' + re.escape(title) + r'</strong>.*?)</a>'
        )
        def linked_repl(match, href=href):
            return f'<a class="document-row link" href="{href}">{match.group("body")}</a>'
        html = linked.sub(linked_repl, html, count=1)
    return html

def link_project_cards(html: str) -> str:
    for title, (page_url, repo_url) in CARD_LINKS.items():
        article_pattern = re.compile(
            r'<article class="project-card[^"]*">(?P<body>.*?<h3>' + re.escape(title) + r'</h3>.*?)</article>'
        )
        def article_repl(match, page_url=page_url, repo_url=repo_url):
            block = match.group(0)
            if 'class="project-actions"' in block:
                return block
            bottom = re.compile(
                r'<div class="project-bottom">(?P<tags><div class="tags">.*?</div>)'
                r'<a href="[^"]+" target="_blank" rel="noreferrer">↗</a></div>'
            )
            replacement = (
                r'<div class="project-bottom">\g<tags><div class="project-actions">'
                f'<a href="{page_url}">Read ↗</a>'
                f'<a href="{repo_url}" target="_blank" rel="noreferrer">Repo ↗</a>'
                '</div></div>'
            )
            return bottom.sub(replacement, block, count=1)
        html = article_pattern.sub(article_repl, html, count=1)
    return html

def main() -> None:
    for item in PAGES:
        output = ROOT / item["path"]
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(render_page(item), encoding="utf-8")

    index = ROOT / "index.html"
    html = index.read_text(encoding="utf-8")
    html = link_document_rows(html)
    html = link_project_cards(html)
    index.write_text(html, encoding="utf-8")

if __name__ == "__main__":
    main()
