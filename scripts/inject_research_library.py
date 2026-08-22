from pathlib import Path

path = Path("index.html")
html = path.read_text(encoding="utf-8")

# Idempotent: once the research library is present there is nothing to do.
if 'id="papers"' in html:
    raise SystemExit(0)

html = html.replace(
    '<a href="#research">Research</a><a href="#profile">Profile</a><a href="#archive">Archive</a>',
    '<a href="#research">Projects</a><a href="#papers">Papers</a><a href="#profile">Profile</a><a href="#archive">Archive</a>'
)

paper_css = r'''
.papers-list{border-top:1px solid #2a2d31}.paper-row{min-height:128px;display:grid;grid-template-columns:72px 160px minmax(260px,1.25fr) minmax(280px,1.45fr) auto 34px;gap:22px;align-items:center;border-bottom:1px solid #2a2d31;transition:background .2s ease}.paper-row:hover{background:#111316}.paper-year,.paper-kind{font:600 10px/1.4 ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace;text-transform:uppercase;letter-spacing:.08em}.paper-year{color:#b8ff65}.paper-kind{color:#747a73}.paper-title strong{display:block;font-size:17px;line-height:1.25;font-weight:560}.paper-title span{display:block;margin-top:7px;color:#767c74;font:600 9px/1.4 ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace;text-transform:uppercase;letter-spacing:.06em}.paper-row>p{margin:0;color:#91978f;font-size:12px;line-height:1.65}.paper-link{justify-self:end;color:#b8ff65;font:600 11px/1 ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace;text-transform:uppercase;letter-spacing:.06em}.paper-row.no-link .paper-link{color:#555b55}.paper-count{display:inline-flex;align-items:center;gap:9px;margin-top:22px;color:#747a73;font:600 10px/1 ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace;text-transform:uppercase;letter-spacing:.09em}.paper-count b{color:#b8ff65;font-weight:600}
'''
html = html.replace(
    '.profile-grid{display:grid;grid-template-columns:1.02fr .98fr;gap:clamp(60px,9vw,150px)}',
    paper_css + '.profile-grid{display:grid;grid-template-columns:1.02fr .98fr;gap:clamp(60px,9vw,150px)}'
)

html = html.replace(
    '@media(max-width:980px){.frame{width:min(100% - 36px,900px)}',
    '@media(max-width:980px){.frame{width:min(100% - 36px,900px)}.paper-row{grid-template-columns:56px 130px 1fr auto;padding:20px 0}.paper-row>p{grid-column:3 / 5}.paper-link{grid-column:4;grid-row:1}.paper-title{grid-column:3}.paper-kind{grid-column:2}'
)
html = html.replace(
    '@media(max-width:620px){.frame{width:calc(100% - 28px)}',
    '@media(max-width:620px){.frame{width:calc(100% - 28px)}.paper-row{grid-template-columns:48px 1fr 28px;gap:12px}.paper-year{grid-column:1}.paper-kind{grid-column:2}.paper-title{grid-column:2 / 4;grid-row:2}.paper-row>p{grid-column:2 / 4;grid-row:3}.paper-link{grid-column:3;grid-row:1}.paper-row .status{grid-column:2;grid-row:4;justify-self:start}'
)

papers = r'''<section class="section frame" id="papers"><div class="section-heading"><div><span class="index">02 / PAPERS &amp; REPORTS</span><h2>The written<br>research record.</h2><div class="paper-count"><b>09</b> dissertations · submissions · research reports</div></div><p>Code shows how I build. These documents show how I frame questions, use evidence, challenge results and communicate conclusions across finance, economics and political economy. Team submissions are labelled as such rather than quietly absorbing everyone else's labour into my personal mythology.</p></div><div class="papers-list">
<a class="paper-row" href="https://github.com/lhkkennedy/Deep-Hedging-under-Lifted-Heston-MSc-Dissertation-" target="_blank" rel="noreferrer"><span class="paper-year">2026</span><span class="paper-kind">MSc dissertation</span><div class="paper-title"><strong>Deep Hedging SPX Straddles: Simulation Pretraining, Market Fine-tuning and Maturity Pooling</strong><span>ECOM107 · Queen Mary University of London</span></div><p>Observable-only neural hedging of short near-ATM SPX straddles under transaction costs, testing simulation transfer, Heston versus Lifted Heston dynamics, market fine-tuning and cross-maturity parameter sharing.</p><span class="status">Finance · ML</span><span class="paper-link">↗</span></a>
<a class="paper-row" href="https://github.com/lhkkennedy/WSJ-Sentiment-Driven-Trading-Strategy-Research" target="_blank" rel="noreferrer"><span class="paper-year">2026</span><span class="paper-kind">Group submission</span><div class="paper-title"><strong>WSJ Sentiment Analysis: State-Dependent Contrarian Returns</strong><span>ECOM217 · Large Language Models for Finance</span></div><p>Maps roughly 146k WSJ headlines to S&amp;P 500 firms, tests NLP sentiment signals and shows the strongest effect as a high-volatility, attention-dependent contrarian sleeve rather than a broad stable sentiment factor.</p><span class="status">NLP · Asset pricing</span><span class="paper-link">↗</span></a>
<div class="paper-row no-link"><span class="paper-year">2026</span><span class="paper-kind">Portfolio assignment</span><div class="paper-title"><strong>Asset Pricing, Trading &amp; Portfolio Construction</strong><span>ECOM155 · Queen Mary University of London</span></div><p>Time-series factor regressions and Fama–MacBeth cross-sectional tests across 49 industry portfolios, followed by rolling and expanding momentum-beta long-short strategy evaluation.</p><span class="status">Asset pricing</span><span class="paper-link">—</span></div>
<a class="paper-row" href="https://github.com/lhkkennedy/Systematic-Trading-Strategy-Review/blob/main/strategy_analysis.pdf" target="_blank" rel="noreferrer"><span class="paper-year">2026</span><span class="paper-kind">Research report</span><div class="paper-title"><strong>Systematic Strategy Allocation Review / MasterFOF</strong><span>QMUL coursework · expanded practitioner report</span></div><p>Institutional-style allocation due diligence using equity and CTA benchmarks, rolling risk, crisis regimes, tail diagnostics and trend/carry/VIX factor attribution.</p><span class="status">Systematic · Risk</span><span class="paper-link">PDF ↗</span></a>
<a class="paper-row" href="https://github.com/lhkkennedy/Lending-Club-Credit-Risk-Research/blob/main/credit_risk_research_report.pdf" target="_blank" rel="noreferrer"><span class="paper-year">2026</span><span class="paper-kind">Assignment report</span><div class="paper-title"><strong>Lending Club Credit Risk Research</strong><span>Machine learning coursework</span></div><p>Leakage-safe default modelling with logistic regression, random forests and XGBoost, with class imbalance, tuning and decision thresholds evaluated against lending economics rather than accuracy theatre.</p><span class="status">Credit · ML</span><span class="paper-link">PDF ↗</span></a>
<a class="paper-row" href="https://github.com/lhkkennedy/Hull-Tactical---Market-Prediction-Kaggle-Competition-2025" target="_blank" rel="noreferrer"><span class="paper-year">2025–26</span><span class="paper-kind">Group report</span><div class="paper-title"><strong>Market Prediction &amp; Dynamic Allocation under Non-Stationarity</strong><span>Introduction to Machine Learning · Hull Tactical challenge</span></div><p>Forward excess-return prediction under heavy-tailed noise, evolving from one-shot validation to 12-fold expanding-window testing and showing that allocation design contributed more than increasingly elaborate predictors.</p><span class="status">Markets · ML</span><span class="paper-link">↗</span></a>
<div class="paper-row no-link"><span class="paper-year">BSc</span><span class="paper-kind">Dissertation</span><div class="paper-title"><strong>Economic Growth × Income Inequality</strong><span>University of Bristol · Applied Economics</span></div><p>Cross-country macroeconomic research using panel data and fixed-effects econometrics to study the relationship between inequality and economic growth.</p><span class="status">Economics</span><span class="paper-link">—</span></div>
<a class="paper-row" href="/html/Debt/projectPage.html" target="_blank" rel="noreferrer"><span class="paper-year">2021</span><span class="paper-kind">Data science submission</span><div class="paper-title"><strong>UK Public Debt: How Much Is Too Much?</strong><span>University of Bristol · Economic data project</span></div><p>Public-finance research combining automated data collection, APIs, visualisation and macroeconomic interpretation of debt, deficits, borrowing, interest rates and fiscal sustainability.</p><span class="status">Economics · Policy</span><span class="paper-link">Live ↗</span></a>
<div class="paper-row no-link"><span class="paper-year">Earlier</span><span class="paper-kind">Extended essay</span><div class="paper-title"><strong>Abenomics: Fiscal Stimulus, Quantitative Easing &amp; Japan's Economic Policy</strong><span>Political economy research</span></div><p>An earlier policy research essay examining Japan's Abenomics programme through fiscal stimulus, unconventional monetary policy and their macroeconomic effects.</p><span class="status">Political economy</span><span class="paper-link">—</span></div>
</div></section>
'''

marker = '<section class="section profile frame" id="profile">'
if marker not in html:
    raise SystemExit("Profile marker missing; refusing to modify page")
html = html.replace(marker, papers + marker)
html = html.replace('<span class="index">02 / PROFILE</span>', '<span class="index">03 / PROFILE</span>')
html = html.replace('<span class="index">03 / RESEARCH ARCHIVE</span>', '<span class="index">04 / RESEARCH ARCHIVE</span>')
html = html.replace('<span class="index">04 / CONTACT</span>', '<span class="index">05 / CONTACT</span>')

path.write_text(html, encoding="utf-8")
