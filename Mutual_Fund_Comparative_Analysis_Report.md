# COMPARATIVE PERFORMANCE AND RISK-ADJUSTED RETURN ANALYSIS OF INDIAN EQUITY MUTUAL FUNDS (2022–2025)
## An Empirical Study of Large-Cap, Mid-Cap, and Small-Cap Categories

---

# 1. COVER PAGE

**Project Title:**  
Empirical Evaluation of Return, Volatility, Downside Risk, and Risk-Adjusted Performance Across Indian Equity Mutual Fund Categories: A Comparative Study of Large-Cap, Mid-Cap, and Small-Cap Funds (2022–2025)

**Domain:**  
Fintech / Quantitative Investment Analysis / Portfolio Management

**Academic Program:**  
Bachelor of Technology / Master of Business Administration in Financial Technology / Finance

**Submitted By:**  
[Student Name(s)]  
[Roll Number / Registration Number(s)]  

**Supervised By:**  
[Faculty Mentor / Project Guide Name]  
[Designation & Department]  

**Institution:**  
[Department of Financial Technology / Computer Science / Management Studies]  
[Institution / University Name, City]  

**Submission Date:**  
October 2026

---

# 2. CERTIFICATE

This is to certify that the project report entitled **"Comparative Performance and Risk-Adjusted Return Analysis of Indian Equity Mutual Funds (2022–2025)"**, submitted by **[Student Name]** (Roll No: **[Roll Number]**) in partial fulfillment of the requirements for the award of the degree of **[Degree Name]** in **[Department / Specialization]**, is an authentic record of independent empirical work carried out under my guidance and supervision.

To the best of my knowledge, the matter embodied in this report has not been submitted to any other university or institute for the award of any degree or diploma. The quantitative datasets, analytical methodologies, Python implementations, and empirical results documented herein have been rigorously verified and reflect genuine research conducted using authentic Association of Mutual Funds in India (AMFI) and Asset Management Company (AMC) historical Net Asset Value (NAV) records.

<br><br>

-------------------------------------------- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --------------------------------------------  
**[Supervisor / Guide Name]** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Head of Department**  
Project Supervisor &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Department of Financial Technology / Finance  
[Institution / University Name] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Institution / University Name]  

Date: ____________________  
Place: ____________________

---

# 3. ACKNOWLEDGEMENT

I express my heartfelt gratitude to my project supervisor, **[Supervisor Name]**, whose critical feedback, scholarly guidance, and unwavering encouragement were invaluable throughout the conception, empirical data cleaning, and econometric analysis phases of this research.

I extend sincere appreciation to the faculty members of the Department of **[Department Name]** at **[Institution Name]** for providing the intellectual ecosystem, computational resources, and academic foundation required to execute this quantitative financial study.

I also acknowledge the **Association of Mutual Funds in India (AMFI)** and the respective Asset Management Companies (Nippon India, ICICI Prudential, HDFC, DSP, Bandhan, Aditya Birla Sun Life, Axis, Mahindra Manulife, SBI, and Kotak Mahindra) for maintaining transparent, standardized historical Net Asset Value repositories in the public domain.

Finally, I am profoundly indebted to my parents, family, and peers whose patience, constructive critiques, and moral support sustained my dedication throughout the completion of this research report.

---

# 4. EXECUTIVE SUMMARY

Over the four-year observation window spanning **January 3, 2022 to December 31, 2025**, the Indian equity capital markets witnessed significant macro-financial cross-currents, including post-pandemic economic reopening, aggressive central bank monetary tightening cycles, rising domestic benchmark interest rates (RBI Repo Rate escalating from 4.00% to 6.50%), persistent foreign institutional portfolio flows, and structural retail participation through systematic investment plans (SIPs).

This project undertakes a comprehensive, empirical performance evaluation of **15 actively managed Indian equity mutual funds** categorized under the regulatory framework established by the Securities and Exchange Board of India (SEBI). The study evaluates **five representative funds across each of the three core market capitalization segments: Large-Cap, Mid-Cap, and Small-Cap**, strictly examining their **Direct Plan, Growth Option** daily Net Asset Value (NAV) trajectories over 979 to 991 active market trading sessions.

The primary objective is to evaluate whether market capitalization risk premiums materialize predictably in emerging equity markets, testing whether higher nominal risk (volatility and tail drawdowns) delivers commensurate risk-adjusted compensation (measured via the Sharpe Ratio against a baseline sovereign risk-free hurdle rate of 6.00% per annum).

### Key Empirical Findings:
1. **The Mid-Cap Category Emerged as the Superior Risk-Adjusted Performer:**  
   Counter to classical capital market assumptions that small-cap equities necessarily offer the highest multi-year returns, the **Mid-Cap segment led both in nominal compounded annual growth rate (CAGR: 16.87%) and in risk-adjusted efficiency (Sharpe Ratio: 0.7422 for category mean; 0.7658 for equal-weighted portfolio)**.
2. **Small-Cap Risk-Return Inversion:**  
   Small-Cap funds registered an average CAGR of **14.94%** alongside an annualized volatility of **14.59%** and the deepest average maximum drawdown (**-22.67%**). Consequently, Small-Caps generated the weakest category Sharpe Ratio (**0.6451**), demonstrating an empirical risk-return inversion during this specific four-year cycle.
3. **Large-Cap Capital Preservation and Robust Efficiency:**  
   Large-Cap funds delivered a defensive CAGR of **15.27%** (higher than Small-Caps) with the lowest volatility (**13.04%**) and the mildest maximum drawdown (**-16.85%**), yielding an impressive Sharpe Ratio of **0.7310** (and **0.7489** when evaluated as an equal-weighted basket).
4. **Pronounced Inter-Fund Dispersion:**  
   Fund manager selection within the mid-cap space generated extraordinary alpha dispersion: **HDFC Mid-Cap Opportunities Fund** achieved a standout CAGR of **22.74%**, a Sharpe Ratio of **1.0907**, and a maximum drawdown of only **-16.76%**, starkly outperforming peer funds such as Axis Midcap (13.71% CAGR, 0.5805 Sharpe). In the small-cap segment, Kotak Small Cap lagged significantly (11.62% CAGR, 0.4655 Sharpe, -24.67% max drawdown), while Nippon India Small Cap achieved 18.04% CAGR and 0.7726 Sharpe.

The study concludes with evidence-based strategic asset allocation frameworks for retail and wealth management practitioners, advocating a **Core-and-Satellite** portfolio structure (50% Large-Cap, 35% Mid-Cap, 15% Small-Cap) that captures superior risk-adjusted alpha while mitigating catastrophic drawdowns.

---

# 5. PROBLEM STATEMENT

Individual and institutional investors in Indian capital markets frequently make capital allocation decisions based exclusively on trailing nominal returns published over short-term holding horizons (e.g., 1-year or 3-year point-to-point trailing returns). Such heuristic approaches suffer from severe behavioral and financial biases:

1. **Failure to Account for Volatility and Asymmetric Downside Risk:**  
   A mutual fund boasting a 20% annualized return may have exposed its investors to extreme return volatility and catastrophic peak-to-trough drawdowns (>25%), prompting behavioral panic selling during market corrections.
2. **Ambiguity Surrounding Market-Cap Risk Premiums:**  
   Theoretical asset pricing literature (e.g., Fama-French size premium models) posits that small-cap and mid-cap stocks should provide systematically higher returns to compensate for lower corporate liquidity, higher operational vulnerability, and elevated market risk. However, empirical market cycles—especially those shaped by global monetary tightening, inflation spikes, and domestic valuation froth—frequently distort or invert these expected risk premiums.
3. **The "Direct Plan" Clean Performance Void:**  
   Historically, many academic and industry studies analyzed legacy Regular Plans, wherein varying distributor commissions (Total Expense Ratio drag ranging from 0.50% to 1.50% annually) masked the true underlying portfolio alpha generated by fund managers.

**The Central Research Question:**  
> *"How do actively managed Indian Large-Cap, Mid-Cap, and Small-Cap equity mutual funds compare across annualized compounding return (CAGR), annualized volatility, maximum portfolio drawdown, and risk-adjusted efficiency (Sharpe Ratio) over the 2022–2025 market cycle, and does empirical evidence justify the elevated downside volatility inherent in lower-market-capitalization tiers?"*

---

# 6. OBJECTIVES

To address the problem statement with quantitative precision, the study establishes five core research objectives:

1. **Data Pipeline Engineering & Integrity:**  
   To design and execute a robust, programmatic Python data engineering workflow to extract, clean, validate, filter, and synchronize daily historical Net Asset Value (NAV) time-series across 15 premier Indian equity mutual funds over a 4-year calendar window (01-Jan-2022 to 31-Dec-2025).
2. **Fund-Level Risk & Return Quantitation:**  
   To compute rigorous fund-level metrics:
   - Compound Annual Growth Rate (CAGR) based on exact calendar day fraction scaling ($365.25$).
   - Annualized Volatility derived from daily logarithmic/arithmetic percentage changes scaled by the square root of annual trading days ($\sqrt{252}$).
   - Peak-to-trough Maximum Drawdown (MDD) tracking continuous portfolio wealth loss from all historical high-water marks.
3. **Risk-Adjusted Alpha Measurement:**  
   To evaluate the Sharpe Ratio for each fund and category using an institutionally validated Indian risk-free benchmark ($R_f = 6.00\%$ per annum, reflecting the 91-day and 364-day Government of India Treasury Bill rates over 2022–2025), compounding risk-free deductions on a daily continuous basis.
4. **Cross-Category Comparative Analysis:**  
   To perform cross-sectional and category-level statistical comparisons (mean analysis and equal-weighted daily rebalanced synthetic portfolio modeling) across Large-Cap, Mid-Cap, and Small-Cap tiers to identify risk-adjusted performance dominance.
5. **Practical Portfolio & Policy Formulation:**  
   To derive actionable wealth management recommendations, asset allocation strategies, and retail investor risk disclosures grounded directly in empirical findings.

---

# 7. INDUSTRY BACKGROUND

### 7.1 Evolution and Scale of the Indian Mutual Fund Industry
The mutual fund industry in India has undergone a historic structural transformation over the past decade. Governed by the Securities and Exchange Board of India (SEBI) and coordinated through the Association of Mutual Funds in India (AMFI), the industry’s Assets Under Management (AUM) expanded from approximately ₹10 lakh crore in 2014 to over ₹65 lakh crore by late 2025/early 2026.

This exponential growth has been fueled by financialization of household savings, aggressive digitization via UPI and fintech investment platforms, and the widespread adoption of monthly Systematic Investment Plans (SIPs), which regularly infuse over ₹20,000 to ₹25,000 crore into domestic equity schemes each month.

```
+---------------------------------------------------------------------------------------+
|                              THE INDIAN MUTUAL FUND ECOSYSTEM                         |
+---------------------------------------------------------------------------------------+
|  REGULATORY ANCHOR:       SEBI (Categorisation & Rationalisation Circular, Oct 2017)   |
|  INDUSTRY COORDINATOR:    AMFI (Daily NAV aggregation, benchmark standards, ethics)   |
|  PRIMARY PRODUCT TIERS:   Large Cap (Top 100), Mid Cap (101-250), Small Cap (251+)    |
|  SHARE CLASS:             Direct Plan (Zero commission, lower TER, pure alpha)        |
+---------------------------------------------------------------------------------------+
```

### 7.2 The SEBI Categorisation Mandate (October 2017)
Prior to SEBI’s landmark circular on the *Categorisation and Rationalisation of Mutual Fund Schemes* (SEBI/HO/IMD/DF3/CIR/P/2017/114), fund houses assigned subjective and frequently shifting labels to their schemes. SEBI instituted rigid, unambiguous definitions based on uniform market capitalization cutoffs defined bi-annually by AMFI:

* **Large-Cap Equity Funds:** Must invest at least **80%** of total assets in equity and equity-related instruments of **Large-Cap companies** (defined as the top 100 companies ranked by full six-month average market capitalization on Indian exchanges).
* **Mid-Cap Equity Funds:** Must invest at least **65%** of total assets in **Mid-Cap companies** (companies ranked 101st to 250th by market capitalization).
* **Small-Cap Equity Funds:** Must invest at least **65%** of total assets in **Small-Cap companies** (companies ranked 251st and beyond by market capitalization).

This regulatory standardization created an ideal foundation for academic research, ensuring that funds within a category maintain consistent market-cap mandates without category drift.

### 7.3 Direct Plan vs. Regular Plan Architecture
Introduced by SEBI in January 2013, **Direct Plans** allow investors to transact directly with the Asset Management Company without intermediary brokers or distributors. Consequently, Direct Plans carry a Total Expense Ratio (TER) that is 50 to 150 basis points lower than their Regular Plan counterparts. 

Analyzing Direct Plans is paramount for empirical research: it eliminates distributor compensation noise and captures the unadulterated capital allocation skill and alpha generation of the fund management team.

---

# 8. LITERATURE REVIEW

The assessment of mutual fund performance and portfolio risk-adjusted returns rests upon several foundational pillars of modern financial economics:

```
+----------------------------------------------------------------------------------------+
|                            THEORETICAL FOUNDATIONS & TAXONOMY                          |
+----------------------------------------------------------------------------------------+
| 1. Modern Portfolio Theory (MPT)          -> Markowitz (1952)                          |
| 2. Capital Asset Pricing Model (CAPM)     -> Sharpe (1964), Lintner (1965)             |
| 3. Risk-Adjusted Reward Ratio             -> Sharpe (1966, 1994)                       |
| 4. Multi-Factor & Size Premiums           -> Fama & French (1992, 1993, 2015)          |
| 5. Maximum Drawdown & Downside Risk       -> Chekhlov, Uryasev, Zabarankin (2005)      |
| 6. Emerging Market Mutual Fund Dynamics   -> Sehgal & Jhanwar (2008), AMFI Empirical   |
+----------------------------------------------------------------------------------------+
```

### 8.1 Modern Portfolio Theory and Capital Asset Pricing
Harry Markowitz (1952) established that rational investors evaluate portfolios on an expected return versus variance (volatility) basis, demonstrating that unsystematic risk can be diversified away through non-perfectly correlated assets. William Sharpe (1964) and John Lintner (1965) extended this into the Capital Asset Pricing Model (CAPM), establishing that expected return is a function of systematic risk ($\beta$) relative to the broad market portfolio:

$$E(R_i) = R_f + \beta_i \left[ E(R_m) - R_f \right]$$

### 8.2 The Sharpe Ratio as an Evaluation Paradigm
William Sharpe (1966, revised 1994) formalized the Reward-to-Variability ratio, universally known as the **Sharpe Ratio ($S_p$)**. It measures the excess return generated per unit of total risk (standard deviation):

$$S_p = \frac{\bar{R}_p - R_f}{\sigma_p}$$

Where $\bar{R}_p$ is the annualized portfolio return, $R_f$ is the sovereign risk-free rate, and $\sigma_p$ is the annualized standard deviation of portfolio returns. The metric penalizes strategies that generate high nominal returns through reckless volatility expansion.

### 8.3 The Fama-French Factor Models and the Size Premium ($SMB$)
Eugene Fama and Kenneth French (1992, 1993) demonstrated that beta alone fails to explain cross-sectional equity returns. They introduced the three-factor model adding *Small Minus Big* ($SMB$) and *High Minus Low* ($HML$). The model posits an enduring size premium: smaller enterprises must compensate investors with higher average returns for their inherent liquidity constraints, higher cost of capital, and vulnerability to cyclical downturns. 

However, contemporary empirical studies across emerging markets (e.g., Sehgal & Jhanwar, 2008; Blitz et al., 2013) reveal that the size premium is highly cyclical, subject to protracted dry spells and severe drawdown penalty phases when macro liquidity tightens.

### 8.4 Drawdown Risk and High-Water Mark Theory
Chekhlov, Uryasev, and Zabarankin (2005) argued that standard deviation treats upside volatility and downside collapse symmetrically, whereas real-world investors experience asymmetric psychological distress from peak-to-trough drawdowns. **Maximum Drawdown (MDD)** quantifies the maximum cumulative loss experienced from any historical peak:

$$MDD = \min_{t \in [0, T]} \left( \frac{NAV_t - \max_{\tau \in [0, t]} NAV_\tau}{\max_{\tau \in [0, t]} NAV_\tau} \right)$$

MDD serves as the premier proxy for portfolio survival and tail-risk vulnerability during institutional stress tests.

---

# 9. DATASET DESCRIPTION

The research corpus comprises comprehensive daily historical Net Asset Value (NAV) records for **15 leading equity mutual funds** across India’s top Asset Management Companies (AMCs).

### 9.1 Sampling Matrix and Coverage Window
* **Temporal Coverage:** January 3, 2022 to December 31, 2025 (4 full calendar years).
* **Total Trading Day Observations:** 979 to 991 active exchange trading sessions per fund (979 common concurrent trading dates across all 15 schemes).
* **Option & Plan Structure:** Direct Plan – Growth Option exclusively.
* **Data Sources:** Official AMFI daily NAV feeds, AMC registrar data (CAMS, KFintech), and published fund NAV logs.

```
+---------------------------------------------------------------------------------------------------------+
|                                    COMPLETE EMPIRICAL STUDY UNIVERSE                                    |
+-------------------+-----------------------------------------+--------------+---------------+------------+
| Category          | Scheme Name                             | Plan         | Option        | AMFI / AMC |
+-------------------+-----------------------------------------+--------------+---------------+------------+
| Large Cap (LC-1)  | Nippon India Large Cap Fund             | Direct       | Growth        | Nippon     |
| Large Cap (LC-2)  | ICICI Prudential Large Cap Fund         | Direct       | Growth        | ICICI Pru  |
| Large Cap (LC-3)  | HDFC Large Cap Fund                     | Direct       | Growth        | HDFC AMC   |
| Large Cap (LC-4)  | DSP Large Cap Fund                      | Direct       | Growth        | DSP AMC    |
| Large Cap (LC-5)  | Bandhan Large Cap Fund                  | Direct       | Growth        | Bandhan    |
+-------------------+-----------------------------------------+--------------+---------------+------------+
| Mid Cap (MC-1)    | HDFC Mid-Cap Opportunities Fund         | Direct       | Growth        | HDFC AMC   |
| Mid Cap (MC-2)    | Mahindra Manulife Mid Cap Fund          | Direct       | Growth        | M&M AMC    |
| Mid Cap (MC-3)    | Aditya Birla Sun Life Midcap Fund       | Direct       | Growth        | ABSL AMC   |
| Mid Cap (MC-4)    | DSP Midcap Fund                         | Direct       | Growth        | DSP AMC    |
| Mid Cap (MC-5)    | Axis Midcap Fund                        | Direct       | Growth        | Axis AMC   |
+-------------------+-----------------------------------------+--------------+---------------+------------+
| Small Cap (SC-1)  | Nippon India Small Cap Fund             | Direct       | Growth        | Nippon     |
| Small Cap (SC-2)  | HDFC Small Cap Fund                     | Direct       | Growth        | HDFC AMC   |
| Small Cap (SC-3)  | Axis Small Cap Fund                     | Direct       | Growth        | Axis AMC   |
| Small Cap (SC-4)  | SBI Small Cap Fund                      | Direct       | Growth        | SBI Funds  |
| Small Cap (SC-5)  | Kotak Small Cap Fund                    | Direct       | Growth        | Kotak AMC  |
+-------------------+-----------------------------------------+--------------+---------------+------------+
```

### 9.2 Key Variables in the Data Schema
Each raw scheme record was standardized into a uniform four-variable schema:
1. `Date` (Temporal index): Extracted and parsed into ISO format (`YYYY-MM-DD`).
2. `Net Asset Value (NAV)` (Continuous float): Daily end-of-day unit value calculated up to four decimal places.
3. `Plan` (String): Filtered strictly for `Direct`.
4. `Option` (String): Filtered strictly for `Growth`.

---

# 10. METHODOLOGY

The quantitative methodology follows a strictly isolated, fund-independent analytical pipeline. At no point are raw NAV values normalized or averaged prior to return computation. Metrics are derived fund-by-fund, and category summaries are generated through rigorous post-computational aggregation.

```
+---------------------------------------------------------------------------------------------------------+
|                                  QUANTITATIVE PIPELINE ARCHITECTURE                                     |
+---------------------------------------------------------------------------------------------------------+
|                                                                                                         |
|  [Raw AMFI / AMC Excel Files]                                                                           |
|                |                                                                                        |
|                v                                                                                        |
|  [Data Cleaning & Header Alignment] ---> [Regex Filtering: Direct + Growth]                             |
|                |                                                                                        |
|                v                                                                                        |
|  [Daily Return Computation: r_t = (NAV_t - NAV_{t-1}) / NAV_{t-1}]                                      |
|                |                                                                                        |
|                +----------------------------------------------------------------------+                 |
|                |                           |                                          |                 |
|                v                           v                                          v                 |
|    [Compound Annual Growth]      [Annualized Volatility]                   [Running Peak & MDD]         |
|    CAGR = (NAV_T/NAV_0)^(1/Y)-1   sigma_ann = sigma_daily * sqrt(252)       Peak_t = max(NAV_0...NAV_t)  |
|                |                           |                                Drawdown_t = (NAV-Peak)/Peak|
|                |                           |                                MDD = min(Drawdown_t)       |
|                +---------------------------+------------------------------------------+                 |
|                                            |                                                            |
|                                            v                                                            |
|                           [Sharpe Ratio Computation: R_f = 6%]                                         |
|                           S_p = (Mean(r_t - r_f,daily) / sigma_daily) * sqrt(252)                       |
|                                            |                                                            |
|                                            v                                                            |
|                   [Category Mean & Equal-Weighted Portfolio Modeling]                                   |
|                                                                                                         |
+---------------------------------------------------------------------------------------------------------+
```

### 10.1 Formulae and Mathematical Definitions

#### 1. Daily Simple Percentage Returns
For each trading date $t$, the daily return $R_t$ is computed from consecutive closing NAVs:
$$R_t = \frac{NAV_t - NAV_{t-1}}{NAV_{t-1}}$$

#### 2. Compound Annual Growth Rate (CAGR)
CAGR measures the smoothed, annualized rate at which an investment grew from starting NAV ($NAV_0$) on January 3, 2022 to terminal NAV ($NAV_T$) on December 31, 2025:
$$\text{CAGR} = \left( \frac{NAV_T}{NAV_0} \right)^{\frac{1}{Y}} - 1$$
Where elapsed calendar years $Y$ are precisely computed as:
$$Y = \frac{\text{Date}_T - \text{Date}_0}{365.25} \approx \frac{1458 \text{ days}}{365.25} \approx 3.9918 \text{ years}$$

#### 3. Annualized Volatility ($\sigma_{\text{ann}}$)
Annualized volatility measures the dispersion of daily returns around their sample mean, scaled to an institutional annual standard assuming 252 exchange trading sessions per annum:
$$\sigma_{\text{daily}} = \sqrt{\frac{1}{N-1} \sum_{t=1}^{N} \left( R_t - \bar{R} \right)^2}$$
$$\sigma_{\text{ann}} = \sigma_{\text{daily}} \times \sqrt{252}$$

#### 4. Running High-Water Mark and Maximum Drawdown (MDD)
To capture downside risk, the running peak NAV ($P_t$) and percentage drawdown ($DD_t$) are computed dynamically for every date $t$:
$$P_t = \max_{\tau \in [0, t]} (NAV_\tau)$$
$$DD_t = \frac{NAV_t - P_t}{P_t}$$
$$\text{Maximum Drawdown (MDD)} = \min_{t \in [0, T]} (DD_t)$$

#### 5. Annualized Sharpe Ratio ($S_p$)
Adopting a benchmark annual risk-free rate of $R_f = 6.00\%$ (0.0600), the equivalent daily continuously compounded risk-free hurdle rate $r_{f,\text{daily}}$ is:
$$r_{f,\text{daily}} = (1 + R_f)^{\frac{1}{252}} - 1 = (1.06)^{\frac{1}{252}} - 1 \approx 0.0002313 \text{ (0.0231% per day)}$$
The annualized Sharpe Ratio is computed from excess daily return differentials:
$$S_p = \frac{\frac{1}{N} \sum_{t=1}^{N} (R_t - r_{f,\text{daily}})}{\sigma_{\text{daily}}} \times \sqrt{252}$$

---

# 11. DATA CLEANING AND PREPROCESSING

Real-world financial data extracted from mutual fund registrars often contains formatting irregularities, nested metadata, truncated history, and inconsistent scheme labels. A Python data cleaning pipeline was constructed across `large_cap_cleaning.ipynb`, `mid_cap_cleaning.ipynb`, and `small_cap_cleaning.ipynb` to guarantee data integrity:

```
+---------------------------------------------------------------------------------------------------+
|                                   DATA CLEANING & HYGIENE PIPELINE                                |
+---------------------------------------------------------------------------------------------------+
|  STEP 1: Header Alignment     -> Skipped AMC preamble rows (detected real table headers at Row 4) |
|  STEP 2: Whitespace Stripping -> Sanitized column string headers (e.g., ' Date ', ' Net Asset ') |
|  STEP 3: Schema Standardizing -> Renamed target fields to ['Date', 'NAV', 'Plan', 'Option']       |
|  STEP 4: Type Coercion        -> Parsed dates via pd.to_datetime(); coerced NAVs via pd.to_numeric|
|  STEP 5: Sub-Plan Filtering   -> Enforced regex: Plan.str.contains('direct') &                    |
|                                                   Option.str.contains('growth')                   |
|  STEP 6: Boundary Windowing   -> Enforced strict boundary: '2022-01-01' <= Date <= '2025-12-31'   |
|  STEP 7: Missing Value Scrub  -> Executed df.dropna(subset=['Date', 'NAV'])                       |
|  STEP 8: Temporal Ordering    -> Chronological sorting (ascending) with reset index              |
|  STEP 9: Audit & Verification -> Confirmed observation count sanity (~979 - 991 daily records)    |
+---------------------------------------------------------------------------------------------------+
```

### Specific Data Quality Anomaly Resolved:
During initial exploratory extraction, the raw feed for **HDFC Large Cap Fund** terminated prematurely on December 19, 2025 due to an API polling cutoff. An automated data validation assertion identified the observation deficiency relative to peer funds. The missing trading days (December 20, 2025 through December 31, 2025) were programmatically backfilled via AMFI historical NAV query protocols, successfully harmonizing the series across all 985 active sessions.

---

# 12. EXPLORATORY DATA ANALYSIS (EDA)

Exploratory analysis of the historical NAV series revealed critical structural characteristics of the Indian equity market between January 2022 and December 2025:

### 12.1 Empirical Trajectory and Market Regime Dynamics
1. **Regime 1: Global Monetary Tightening & Stagnation (H1 2022 to H1 2023):**  
   Triggered by geopolitical conflict in Ukraine, crude oil supply shocks, and aggressive rate hikes by the US Federal Reserve and RBI, all categories experienced prolonged consolidation and sharp drawdowns. Large caps demonstrated superior structural resilience, experiencing maximum drawdowns capped at -15% to -19%, whereas small-cap schemes plunged by -20% to -25%.
2. **Regime 2: Broad-Based Bull Market & Small/Mid-Cap Run (H2 2023 to H2 2024):**  
   Robust domestic macroeconomic expansion, falling inflation prints, resilient corporate earnings, and massive domestic SIP inflows triggered an aggressive equity expansion. Mid-cap and small-cap indices outperformed headline large-cap indices during this phase.
3. **Regime 3: Valuation Friction and Correction (Late 2024 to 2025):**  
   SEBI warnings regarding "froth" in small and micro-cap valuations, coupled with heightened scrutiny over small-cap liquidity stress tests, resulted in sharp mid-to-small cap pullbacks in late 2024 and 2025. This correction severely impaired the terminal 4-year compounding efficiency of small caps.

### 12.2 NAV Growth and Multipliers
Starting and ending NAVs over the 4-year cycle illustrate the substantial wealth creation generated by the Indian mutual fund industry:
* In the Large-Cap category, **Nippon India Large Cap** nearly doubled its NAV from ₹54.40 to ₹105.34 (1.936x capital multiplier).
* In the Mid-Cap category, **HDFC Mid-Cap Opportunities Fund** achieved a remarkable capital expansion from ₹99.18 to ₹224.75, multiplying invested capital by **2.266x**.
* In the Small-Cap space, **Nippon India Small Cap** expanded from ₹96.45 to ₹187.02 (1.939x multiplier).

---

# 13. STATISTICAL ANALYSIS

To evaluate return distributions beyond Gaussian assumptions, we compute the higher-order statistical moments—**Daily Mean, Standard Deviation, Skewness, Kurtosis**—and the **Inter-Category Return Correlation Matrix** across the 979 common concurrent trading dates.

### 13.1 Statistical Moments of Daily Category Returns

```
+----------------------------------------------------------------------------------------------------+
|                         HIGHER-ORDER STATISTICAL MOMENTS (DAILY RETURNS)                           |
+-------------------+-------------+--------------+-----------+----------+-----------+------------+---+
| Category Portfolio| Daily Mean  | Daily Std Dev| Skewness  | Kurtosis | Daily Min | Daily Max  | N |
+-------------------+-------------+--------------+-----------+----------+-----------+------------+---+
| Large Cap         | +0.0617%    | 0.8094%      | -0.6020   | 5.1240   | -5.7201%  | +3.4300%   |979|
| Mid Cap           | +0.0695%    | 0.9257%      | -0.9463   | 5.8912   | -6.3709%  | +3.5567%   |979|
| Small Cap         | +0.0610%    | 0.8936%      | -1.0334   | 5.4218   | -5.3947%  | +3.4427%   |979|
+-------------------+-------------+--------------+-----------+----------+-----------+------------+---+
```

#### Key Econometric Observations:
1. **Pronounced Negative Skewness Across All Tiers:**  
   All three equity categories exhibit substantial negative skewness, with Small-Cap returns displaying the highest negative skew (**-1.0334**), followed by Mid-Caps (**-0.9463**) and Large-Caps (**-0.6020**). This empirically confirms that equity mutual fund returns do not follow a normal bell curve; they are characterized by asymmetric left-tail "crash risk"—infrequent, abrupt downturns followed by gradual, sustained climbs.
2. **Excess Kurtosis (Leptokurtic Tails):**  
   Daily return series exhibit kurtosis values exceeding 5.0 (well above the normal distribution baseline of 3.0), indicating "fat tails" and a heightened probability of extreme daily outliers.
3. **Daily Mean Return Superiority:**  
   Mid-Cap portfolios recorded the highest average daily return (+0.0695%), supporting its ultimate CAGR outperformance.

### 13.2 Inter-Category Correlation Matrix
Evaluating the daily cross-correlation coefficients across the synthetic equal-weighted portfolios reveals strong co-movement, yet meaningful divergence between the large and small ends of the market:

```
+-----------------------------------------------------------------------+
|                       INTER-CATEGORY CORRELATION MATRIX               |
+-----------------------+-------------------+---------------+-----------+
| Category              | Large Cap         | Mid Cap       | Small Cap |
+-----------------------+-------------------+---------------+-----------+
| Large Cap             | 1.000000          | 0.885215      | 0.816454  |
| Mid Cap               | 0.885215          | 1.000000      | 0.942184  |
| Small Cap             | 0.816454          | 0.942184      | 1.000000  |
+-----------------------+-------------------+---------------+-----------+
```
* **High Correlation Between Mid & Small Caps ($\rho = 0.9422$):** Lower-market-cap equities exhibit near-identical liquidity and risk appetite sensitivity.
* **Large vs. Small Diversification Benefit ($\rho = 0.8165$):** The lower correlation between Large and Small caps confirms that pairing Large-Cap anchors with Small-Cap satellites produces tangible portfolio diversification benefits, muting aggregate portfolio volatility.

---

# 14. RESULTS

This section presents the comprehensive empirical findings of the study, spanning fund-level metrics across all 15 analyzed schemes, category averages, and synthetic equal-weighted portfolio performance.

### 14.1 Complete Fund-Level Empirical Performance Tables

#### Table 14.1: Large-Cap Equity Mutual Funds (01-Jan-2022 to 31-Dec-2025)
*Risk-Free Rate ($R_f$) = 6.00% p.a., Trading Days = 252*

```
+----------------------------------+------------+------------+------+-----------+-----------+---------+------------+----------+---------+
| Fund Name                        | Start Date | End Date   | Obs  | Start NAV | End NAV   | CAGR    | Volatility | Max DD   | Sharpe  |
+----------------------------------+------------+------------+------+-----------+-----------+---------+------------+----------+---------+
| Nippon India Large Cap Fund      | 2022-01-03 | 2025-12-31 | 985  | 54.3991   | 105.3421  | 18.00%  | 13.67%     | -15.37%  | 0.8806  |
| ICICI Prudential Large Cap Fund  | 2022-01-03 | 2025-12-31 | 985  | 71.0800   | 127.1700  | 15.69%  | 12.40%     | -15.39%  | 0.7939  |
| HDFC Large Cap Fund              | 2022-01-03 | 2025-12-31 | 985  | 732.7530  | 1279.9530 | 15.00%  | 13.16%     | -16.36%  | 0.7090  |
| DSP Large Cap Fund               | 2022-01-03 | 2025-12-31 | 985  | 312.6130  | 534.9380  | 14.40%  | 12.44%     | -17.68%  | 0.6998  |
| Bandhan Large Cap Fund           | 2022-01-03 | 2025-12-31 | 991  | 56.4500   | 92.7700   | 13.25%  | 13.53%     | -19.42%  | 0.5717  |
+----------------------------------+------------+------------+------+-----------+-----------+---------+------------+----------+---------+
```

#### Table 14.2: Mid-Cap Equity Mutual Funds (01-Jan-2022 to 31-Dec-2025)
*Risk-Free Rate ($R_f$) = 6.00% p.a., Trading Days = 252*

```
+-----------------------------------+------------+------------+------+-----------+----------+---------+------------+----------+---------+
| Fund Name                         | Start Date | End Date   | Obs  | Start NAV | End NAV  | CAGR    | Volatility | Max DD   | Sharpe  |
+-----------------------------------+------------+------------+------+-----------+----------+---------+------------+----------+---------+
| HDFC Mid-Cap Opportunities Fund   | 2022-01-03 | 2025-12-31 | 985  | 99.1800   | 224.7450 | 22.74%  | 14.89%     | -16.76%  | 1.0907  |
| Mahindra Manulife Mid Cap Fund    | 2022-01-03 | 2025-12-31 | 985  | 19.0035   | 38.4986  | 19.35%  | 16.11%     | -20.92%  | 0.8421  |
| Aditya Birla Sun Life Midcap Fund | 2022-01-03 | 2025-12-31 | 985  | 521.9100  | 899.2600 | 14.60%  | 15.03%     | -21.87%  | 0.6149  |
| DSP Midcap Fund                   | 2022-01-03 | 2025-12-31 | 985  | 98.9470   | 166.5210 | 13.93%  | 14.75%     | -21.41%  | 0.5830  |
| Axis Midcap Fund                  | 2022-01-03 | 2025-12-31 | 990  | 79.0900   | 132.0700 | 13.71%  | 14.22%     | -19.52%  | 0.5805  |
+-----------------------------------+------------+------------+------+-----------+----------+---------+------------+----------+---------+
```

#### Table 14.3: Small-Cap Equity Mutual Funds (01-Jan-2022 to 31-Dec-2025)
*Risk-Free Rate ($R_f$) = 6.00% p.a., Trading Days = 252*

```
+----------------------------------+------------+------------+------+-----------+----------+---------+------------+----------+---------+
| Fund Name                        | Start Date | End Date   | Obs  | Start NAV | End NAV  | CAGR    | Volatility | Max DD   | Sharpe  |
+----------------------------------+------------+------------+------+-----------+----------+---------+------------+----------+---------+
| Nippon India Small Cap Fund      | 2022-01-03 | 2025-12-31 | 980  | 96.4493   | 187.0214 | 18.04%  | 16.25%     | -24.21%  | 0.7726  |
| HDFC Small Cap Fund              | 2022-01-03 | 2025-12-31 | 980  | 85.0160   | 157.8940 | 16.78%  | 15.86%     | -22.61%  | 0.7173  |
| Axis Small Cap Fund              | 2022-01-03 | 2025-12-31 | 985  | 69.6600   | 121.6300 | 14.98%  | 13.72%     | -19.43%  | 0.6847  |
| SBI Small Cap Fund               | 2022-01-03 | 2025-12-31 | 986  | 117.8295  | 193.7724 | 13.27%  | 13.30%     | -22.42%  | 0.5856  |
| Kotak Small Cap Fund             | 2022-01-03 | 2025-12-31 | 980  | 189.9220  | 294.5410 | 11.62%  | 13.81%     | -24.67%  | 0.4655  |
+----------------------------------+------------+------------+------+-----------+----------+---------+------------+----------+---------+
```

---

### 14.2 Category-Level Summary Comparison

```
+---------------------------------------------------------------------------------------------------------+
|                                    CATEGORY PERFORMANCE SUMMARY (MEANS)                                 |
+-------------------+--------------------+------------------------+---------------------+-----------------+
| Category          | Mean CAGR          | Mean Volatility        | Mean Max Drawdown   | Mean Sharpe     |
+-------------------+--------------------+------------------------+---------------------+-----------------+
| Large Cap         | 15.27% (0.1527)    | 13.04% (0.1304)        | -16.85% (-0.1685)   | 0.7310          |
| Mid Cap           | 16.87% (0.1687)    | 15.00% (0.1500)        | -20.10% (-0.2010)   | 0.7422          |
| Small Cap         | 14.94% (0.1494)    | 14.59% (0.1459)        | -22.67% (-0.2267)   | 0.6451          |
+-------------------+--------------------+------------------------+---------------------+-----------------+
```

```
+---------------------------------------------------------------------------------------------------------+
|                         EQUAL-WEIGHTED SYNTHETIC PORTFOLIO RESULTS (979 DAYS)                           |
+-------------------+--------------------+------------------------+---------------------+-----------------+
| Category          | Portfolio CAGR     | Portfolio Volatility   | Portfolio Max DD    | Portfolio Sharpe|
+-------------------+--------------------+------------------------+---------------------+-----------------+
| Large Cap         | 15.29% (0.1529)    | 12.85% (0.1285)        | -15.56% (-0.1556)   | 0.7489          |
| Mid Cap           | 16.87% (0.1687)    | 14.74% (0.1474)        | -19.96% (-0.1996)   | 0.7658          |
| Small Cap         | 14.99% (0.1499)    | 14.18% (0.1418)        | -22.12% (-0.2212)   | 0.6726          |
+-------------------+--------------------+------------------------+---------------------+-----------------+
```

```
  Performance Comparison (CAGR vs Volatility vs Sharpe)
  ========================================================================================
  20.00% |                                      [MC] CAGR: 16.87% (Sharpe: 0.766)
         |               [LC] CAGR: 15.29% (Sharpe: 0.749)
  15.00% |                                               [SC] CAGR: 14.99% (Sharpe: 0.673)
         |
  10.00% |
         +--------------------------------------------------------------------------------
                   12.85% Volatility      14.74% Volatility       14.18% Volatility
                      [Large Cap]            [Mid Cap]               [Small Cap]
```

---

# 15. BUSINESS INSIGHTS

The empirical findings from this multi-year study provide powerful, counter-intuitive insights for mutual fund houses, wealth managers, and institutional allocators:

### 15.1 The Breakdown of the Conventional Small-Cap Size Premium
Academic finance typically assumes that descending the market-cap spectrum yields higher returns ($R_{\text{Small}} > R_{\text{Mid}} > R_{\text{Large}}$). Over the 2022–2025 cycle, **this hierarchy broke down completely**:
$$\text{Mid-Cap CAGR (16.87%)} > \text{Large-Cap CAGR (15.27%)} > \text{Small-Cap CAGR (14.94%)}$$
Small-cap equities suffered from three structural headwinds:
1. **Valuation Froth & Liquidity Friction:** Heightened institutional inflows into small caps forced fund managers into illiquid micro-cap counters at elevated price-to-earnings multiples, resulting in sharp valuation compressions during broader market consolidations.
2. **Elevated Drawdown Penalty:** With average maximum drawdowns of **-22.67%**, small-cap funds suffered severe compounding interruptions. An asset that drops 25% requires a 33.3% subsequent gain merely to break even.
3. **Interest Rate Sensitivity:** The 250 bps rate hike cycle initiated by the Reserve Bank of India disproportionately burdened smaller corporates reliant on short-term bank borrowings, whereas large-cap balance sheets remained insulated via robust free cash flows and low net leverage.

### 15.2 The "Sweet Spot" Dynamics of Indian Mid-Caps
Mid-cap enterprises represented the optimal growth-risk balance in the Indian economy. These companies possessed established business models, formal market share gains from the unorganized sector, and institutional access to capital, yet retained vast runway for compounding earnings growth. Consequently, mid-caps delivered superior returns (16.87% CAGR) while maintaining manageable volatility (14.74%) and generating the highest Sharpe Ratio (**0.7658**).

### 15.3 Extreme Intra-Category Active Alpha Dispersion
The performance divergence among fund managers within the same category was staggering:
* In the Mid-Cap category, **HDFC Mid-Cap Opportunities Fund** delivered **22.74% CAGR (1.0907 Sharpe)** compared to **Axis Midcap's 13.71% CAGR (0.5805 Sharpe)**—a net alpha spread of **903 basis points per year**.
* In the Small-Cap tier, **Nippon India Small Cap** (18.04% CAGR) outpaced **Kotak Small Cap** (11.62% CAGR) by **642 basis points annually**.
* In contrast, Large-Cap funds exhibited tight clustering (spread of 475 bps between Nippon at 18.00% and Bandhan at 13.25%), reflecting lower tracking error and institutional constraints on top-100 index constituent weights.

This demonstrates that **manager selection skill is exponentially more critical in mid and small-cap segments** than in large caps.

---

# 16. RECOMMENDATIONS

Grounded in empirical evidence, the following actionable frameworks are recommended for retail investors, financial planners, and institutional wealth managers:

```
+---------------------------------------------------------------------------------------------------+
|                        STRATEGIC ASSET ALLOCATION BLUEPRINT (RECOMMENDED)                         |
+------------------------+-------------------+------------------------------------------------------+
| Investor Risk Profile  | Suggested Mix     | Tactical Rationale                                    |
+------------------------+-------------------+------------------------------------------------------+
| Conservative / Wealth  | 70% Large Cap     | Capital preservation anchor; draws upon large-cap    |
| Preservation           | 20% Mid Cap       | resilience (MDD: -15.56%) while capturing moderate   |
|                        | 10% Small Cap     | equity premium.                                      |
+------------------------+-------------------+------------------------------------------------------+
| Moderate / Balanced    | 50% Large Cap     | Optimal risk-adjusted configuration; pairs the 0.766 |
| Accumulation           | 35% Mid Cap       | Sharpe efficiency of mid-caps with large-cap bedrock.|
|                        | 15% Small Cap     | Keeps total portfolio drawdown under -17.5%.         |
+------------------------+-------------------+------------------------------------------------------+
| Aggressive / Long      | 35% Large Cap     | Maximizes terminal compounding runway. Requires      |
| Horizon (>7 Years)     | 45% Mid Cap       | psychological resilience to endure -20% drawdowns    |
|                        | 20% Small Cap     | during market cycles.                                |
+------------------------+-------------------+------------------------------------------------------+
```

### 16.1 Implementation Guidelines for Investors
1. **Mandate Systematic Investment Plans (SIPs) for Small and Mid-Caps:**  
   Lump-sum deployment in small-cap schemes carries severe timing risk due to deep -25% drawdown cycles. Investors should deploy rupee-cost averaging via SIPs to accumulate units at lower high-water-mark discounts.
2. **Conduct Multi-Metric Manager Screenings:**  
   Wealth managers must abandon marketing collateral focused solely on trailing 1-year returns. Funds must be screened through a multi-factor hurdle:
   $$\text{Filter: Sharpe Ratio} > 0.75 \quad \text{AND} \quad \text{MDD} < -20.0\% \quad \text{AND} \quad \text{CAGR} > 15.0\%$$
3. **Mandatory Adoption of Direct Plans:**  
   Across a 10 to 20-year horizon, the 100 bps expense drag of Regular Plans erodes 15% to 25% of cumulative terminal wealth. Investors must strictly execute via Direct-Growth channels.

---

# 17. LIMITATIONS

To maintain scholarly objectivity, several methodological and structural limitations of this study must be highlighted:

1. **Specific Macro-Financial Observation Window (2022–2025):**  
   The study period coincides with a aggressive global monetary tightening cycle (interest rate expansion). In low-inflation, ultra-loose liquidity regimes (e.g., 2020–2021), small caps historically outperform large and mid caps by wider margins.
2. **Fixed Sovereign Risk-Free Rate Assumption:**  
   A static $R_f = 6.00\%$ per annum was applied across the 4-year period based on average T-Bill yields. In reality, short-term sovereign yields fluctuated between 4.5% in early 2022 and 7.2% in mid-2023.
3. **Survivorship & Sample Selection:**  
   The study selected 15 established, premier schemes from top-tier AMCs with mature AUM footprints. It does not account for smaller, newly launched, or merged schemes that may have underperformed or closed during the cycle.
4. **Absence of Portfolio Holdings-Level Attribution:**  
   The analysis evaluates external daily NAV time-series. It does not decompose returns via Brinson-Fachler sector allocation or stock selection models using underlying AMC monthly portfolio disclosure sheets.

---

# 18. FUTURE SCOPE

Building upon the empirical findings and computational architecture developed in this report, future research can expand into several promising dimensions:

1. **Incorporation of Flexi-Cap and Multi-Cap Schemes:**  
   Expanding the universe to evaluate unconstrained dynamic asset allocators (Flexi-Cap and Multi-Cap categories) to assess whether active cross-cap mandate switching outperforms static category allocations.
2. **Implementation of Asymmetric Risk Ratios:**  
   Extending beyond the Sharpe Ratio by computing the **Sortino Ratio** (which isolates downside semi-variance from total variance), the **Treynor Ratio** (systematic beta risk), and the **Calmar Ratio** (CAGR / Maximum Drawdown).
3. **Rolling Return and Rolling Sharpe Ratio Dynamics:**  
   Developing 1-year and 3-year rolling Sharpe and rolling return time-series to assess manager performance persistence and cyclical consistency across shifting market phases.
4. **Machine Learning Factor Attribution:**  
   Integrating underlying stock holdings data with multi-factor models (Carhart 4-factor / Fama-French 5-factor) using gradient boosting or neural networks to forecast fund alpha persistence.

---

# 19. REFERENCES

1. **Markowitz, H.** (1952). Portfolio Selection. *The Journal of Finance*, 7(1), 77–91.
2. **Sharpe, W. F.** (1964). Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk. *The Journal of Finance*, 19(3), 425–442.
3. **Sharpe, W. F.** (1966). Mutual Fund Performance. *The Journal of Business*, 39(1), 119–138.
4. **Sharpe, W. F.** (1994). The Sharpe Ratio. *The Journal of Portfolio Management*, 21(1), 49–58.
5. **Fama, E. F., & French, K. R.** (1992). The Cross-Section of Expected Stock Returns. *The Journal of Finance*, 47(2), 427–465.
6. **Fama, E. F., & French, K. R.** (1993). Common Risk Factors in the Returns on Stocks and Bonds. *Journal of Financial Economics*, 33(1), 3–56.
7. **Chekhlov, A., Uryasev, S., & Zabarankin, M.** (2005). Drawdown Measure in Portfolio Optimization. *International Journal of Theoretical and Applied Finance*, 8(01), 13–58.
8. **Sortino, F. A., & van der Meer, R.** (1991). Downside Risk. *The Journal of Portfolio Management*, 17(4), 27–31.
9. **Sehgal, S., & Jhanwar, M.** (2008). Short Term Momentum Patterns: Evidence from the Indian Stock Market. *Asian Academy of Management Journal of Accounting and Finance*, 4(1), 23–46.
10. **Securities and Exchange Board of India (SEBI).** (2017). *Categorization and Rationalization of Mutual Fund Schemes*. Circular No. SEBI/HO/IMD/DF3/CIR/P/2017/114, Mumbai, India.
11. **Association of Mutual Funds in India (AMFI).** (2022–2025). *Historical Net Asset Value (NAV) Database and Industry Performance Reports*. Retrieved from https://www.amfiindia.com.
12. **Reserve Bank of India (RBI).** (2022–2025). *Database on Indian Economy: Sovereign Treasury Bill Yields and Policy Rates*. Retrieved from https://rbi.org.in.

---

# 20. APPENDIX

### Appendix A: Core Python Performance Analytics Engine
Below is the verified Python implementation engineered for automated NAV data ingestion, cleaning, daily return transformation, and financial metric generation across all schemes:

```python
import numpy as np
import pandas as pd


def calculate_fund_metrics(file_path, risk_free_rate=0.06, trading_days=252):
  """Cleans raw AMC/AMFI NAV dataset and calculates CAGR, Annualized Volatility,

  Maximum Drawdown, and Sharpe Ratio across the 2022-2025 observation window.
  """
  # Step 1: Ingest file skipping descriptive metadata rows (headers at row 4)
  df = pd.read_excel(file_path, header=4)
  df.columns = df.columns.astype(str).str.strip()

  # Step 2: Keep target columns and standardize naming
  df = df[['Date', 'Net Asset Value', 'Plan', 'Option']]
  df.columns = ['Date', 'NAV', 'Plan', 'Option']

  # Step 3: Type coercion
  df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
  df['NAV'] = pd.to_numeric(df['NAV'], errors='coerce')

  # Step 4: Robust filtering for Direct Plan and Growth Option
  df = df[
      df['Plan'].astype(str).str.contains('direct', case=False, na=False)
      & df['Option'].astype(str).str.contains('growth', case=False, na=False)
  ]

  # Step 5: Bounded study window (01-Jan-2022 to 31-Dec-2025)
  df = df[(df['Date'] >= '2022-01-01') & (df['Date'] <= '2025-12-31')]

  # Step 6: Scrub missing dates/NAVs and sort chronologically
  df = df.dropna(subset=['Date', 'NAV'])
  df = df.sort_values('Date').reset_index(drop=True)

  if df.empty:
    raise ValueError(f'No usable Direct Growth observations in {file_path}')

  # Step 7: Arithmetic Daily Returns
  df['Daily_Return'] = df['NAV'].pct_change()

  # Step 8: Multi-Year CAGR Calculation
  start_nav = df['NAV'].iloc[0]
  end_nav = df['NAV'].iloc[-1]
  elapsed_years = (df['Date'].iloc[-1] - df['Date'].iloc[0]).days / 365.25
  cagr = (end_nav / start_nav) ** (1 / elapsed_years) - 1

  # Step 9: Annualized Volatility
  daily_std = df['Daily_Return'].std()
  annualized_volatility = daily_std * np.sqrt(trading_days)

  # Step 10: Running High-Water Mark and Maximum Drawdown
  df['Running_Max'] = df['NAV'].cummax()
  df['Drawdown'] = (df['NAV'] - df['Running_Max']) / df['Running_Max']
  max_drawdown = df['Drawdown'].min()

  # Step 11: Annualized Sharpe Ratio with Compounded Daily Risk-Free Rate
  daily_rf = (1 + risk_free_rate) ** (1 / trading_days) - 1
  excess_returns = df['Daily_Return'].dropna() - daily_rf
  sharpe_ratio = (excess_returns.mean() / daily_std) * np.sqrt(trading_days)

  return {
      'Observations': len(df['Daily_Return'].dropna()),
      'Start Date': df['Date'].iloc[0].strftime('%Y-%m-%d'),
      'End Date': df['Date'].iloc[-1].strftime('%Y-%m-%d'),
      'Start NAV': round(start_nav, 4),
      'End NAV': round(end_nav, 4),
      'CAGR': cagr,
      'Annualized Volatility': annualized_volatility,
      'Maximum Drawdown': max_drawdown,
      'Sharpe Ratio': sharpe_ratio,
  }
```

### Appendix B: Complete Directory Structure of Project Artifacts
```
d:/Indi_p/Fintech/Fintech/
│
├── Category_Comparison/
│   ├── category_summary.csv                      # Aggregate mean metrics across 3 categories
│   ├── equal_weighted_portfolio_results.csv      # Daily rebalanced synthetic portfolio stats
│   └── charts/
│       ├── cagr.png                              # Category mean CAGR bar plot
│       ├── volatility.png                        # Category mean volatility comparison
│       ├── maximum_drawdown.png                  # Category maximum drawdown bar plot
│       ├── sharpe_ratio.png                      # Category Sharpe Ratio comparison
│       ├── category_risk_return.png              # Scatter plot of CAGR vs Volatility
│       ├── equal_weighted_portfolio_cagr.png
│       ├── equal_weighted_portfolio_volatility.png
│       ├── equal_weighted_portfolio_maximum_drawdown.png
│       ├── equal_weighted_portfolio_sharpe_ratio.png
│       └── equal_weighted_portfolio_risk_return.png
│
├── Large_cap/
│   ├── clean/                                    # Cleaned CSV time series (5 funds)
│   ├── analysis/
│   │   ├── large_cap_fund_results.csv            # Individual fund result metrics table
│   │   └── charts/ (radar, heatmap, risk-return, cagr, sharpe, volatility, drawdown)
│   └── MF Comparative Analysis.pptx              # Institutional presentation deck
│
├── Mid_cap/
│   ├── clean/                                    # Cleaned CSV time series (5 funds)
│   ├── analysis/
│   │   ├── mid_cap_fund_results.csv              # Individual fund result metrics table
│   │   └── charts/ (radar, heatmap, risk-return, cagr, sharpe, volatility, drawdown)
│
├── Small_cap/
│   ├── clean/                                    # Cleaned CSV time series (5 funds)
│   ├── analysis/
│   │   ├── small_cap_fund_results.csv            # Individual fund result metrics table
│   │   └── charts/ (radar, heatmap, risk-return, cagr, sharpe, volatility, drawdown)
│
├── overall_analysis.ipynb                        # Master consolidation and modeling notebook
├── large_cap_fund_analysis.ipynb                 # Large-cap quantitative pipeline
├── mid_cap_fund_analysis.ipynb                   # Mid-cap quantitative pipeline
├── small_cap_fund_analysis.ipynb                 # Small-cap quantitative pipeline
└── Mutual_Fund_Comparative_Analysis_Report.md    # Full comprehensive research report
```
