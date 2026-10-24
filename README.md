# Indian Equity Mutual Fund Performance Analysis (2022–2025)

An empirical study evaluating the risk, return, and downside profiles of 15 actively managed Indian equity mutual funds across Large-Cap, Mid-Cap, and Small-Cap categories. 

The study covers 4 full calendar years (January 3, 2022 to December 31, 2025), capturing the post-pandemic recovery, central bank rate hikes (RBI repo rate moving from 4.00% to 6.50%), and heavy domestic retail SIP inflows. All data is based on daily Net Asset Values (NAVs) of Direct Plan, Growth Options sourced from AMFI disclosures and individual AMC records.

---

## The Core Question

Conventional market wisdom says taking on higher risk in smaller companies yields higher returns over time. But does that risk premium actually show up over a multi-year rate hike cycle? 

This project tests whether Indian Mid-Cap and Small-Cap funds compensated investors for their higher volatility and deeper drawdowns compared to steady Large-Caps, using standardized quantitative metrics: CAGR, annualized volatility, maximum peak-to-trough drawdown, and the Sharpe ratio.

---

## Key Findings

1. **Mid-Caps delivered the best overall risk-adjusted returns.**  
   Mid-cap funds led both nominal growth (16.87% CAGR average) and risk efficiency (0.7422 category Sharpe; 0.7658 for an equal-weighted basket), beating both large and small caps.
2. **Small-Caps experienced a risk-return inversion.**  
   Despite taking on the deepest peak-to-trough drawdowns (-22.67% average) and high volatility (14.59%), Small-Caps delivered the lowest average CAGR (14.94%) and the weakest Sharpe ratio (0.6451).
3. **Large-Caps offered superior downside protection without giving up return.**  
   Large-cap funds posted an average CAGR of 15.27%—slightly higher than small caps—with significantly lower volatility (13.04%) and milder drawdowns (-16.85%), yielding a solid Sharpe ratio of 0.7310.
4. **Manager selection drove massive dispersion in Mid-Caps and Small-Caps.**  
   - In mid-caps, HDFC Mid-Cap Opportunities stood out with 22.74% CAGR and a 1.09 Sharpe, while Axis Midcap trailed at 13.71% CAGR.
   - In small-caps, Nippon India Small Cap delivered 18.04% CAGR (0.77 Sharpe), whereas Kotak Small Cap lagged at 11.62% CAGR and a -24.67% drawdown.

---

## Category Comparison (2022 – 2025)

| Category | Funds Analyzed | Avg. Observations | Avg. CAGR | Annualized Volatility | Max Drawdown | Sharpe Ratio ($R_f = 6.0\%$) | Equal-Weight Portfolio Sharpe |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Mid Cap** | 5 | ~986 | **16.87%** | 15.00% | -20.10% | **0.7422** | **0.7658** |
| **Large Cap** | 5 | ~986 | 15.27% | **13.04%** | **-16.85%** | 0.7310 | 0.7489 |
| **Small Cap** | 5 | ~981 | 14.94% | 14.59% | -22.67% | 0.6451 | 0.6726 |

*Notes: Risk-free rate hurdle is set at 6.0% p.a. based on prevailing Indian sovereign 91-day T-Bill / repo yields. Annualized trading days = 252.*

---

## Detailed Fund Performance

### Large-Cap Funds
| Fund | Period | Obs. | Start NAV (₹) | End NAV (₹) | CAGR | Volatility | Max Drawdown | Sharpe Ratio |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Nippon India Large Cap** | Jan 2022 – Dec 2025 | 985 | 54.40 | 105.34 | 18.00% | 13.67% | -15.37% | 0.8806 |
| **ICICI Prudential Large Cap** | Jan 2022 – Dec 2025 | 985 | 71.08 | 127.17 | 15.69% | 12.40% | -15.39% | 0.7939 |
| **HDFC Large Cap** | Jan 2022 – Dec 2025 | 985 | 732.75 | 1279.95 | 15.00% | 13.16% | -16.36% | 0.7090 |
| **DSP Large Cap** | Jan 2022 – Dec 2025 | 985 | 312.61 | 534.94 | 14.40% | 12.44% | -17.68% | 0.6998 |
| **Bandhan Large Cap** | Jan 2022 – Dec 2025 | 991 | 56.45 | 92.77 | 13.25% | 13.53% | -19.42% | 0.5717 |

### Mid-Cap Funds
| Fund | Period | Obs. | Start NAV (₹) | End NAV (₹) | CAGR | Volatility | Max Drawdown | Sharpe Ratio |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **HDFC Mid-Cap Opportunities** | Jan 2022 – Dec 2025 | 985 | 99.18 | 224.75 | 22.74% | 14.89% | -16.76% | 1.0907 |
| **Mahindra Manulife Mid Cap** | Jan 2022 – Dec 2025 | 985 | 19.00 | 38.50 | 19.35% | 16.11% | -20.92% | 0.8421 |
| **Aditya Birla Sun Life Midcap** | Jan 2022 – Dec 2025 | 985 | 521.91 | 899.26 | 14.60% | 15.03% | -21.87% | 0.6149 |
| **DSP Midcap** | Jan 2022 – Dec 2025 | 985 | 98.95 | 166.52 | 13.93% | 14.75% | -21.41% | 0.5830 |
| **Axis Midcap** | Jan 2022 – Dec 2025 | 990 | 79.09 | 132.07 | 13.71% | 14.22% | -19.52% | 0.5805 |

### Small-Cap Funds
| Fund | Period | Obs. | Start NAV (₹) | End NAV (₹) | CAGR | Volatility | Max Drawdown | Sharpe Ratio |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Nippon India Small Cap** | Jan 2022 – Dec 2025 | 980 | 96.45 | 187.02 | 18.04% | 16.25% | -24.21% | 0.7726 |
| **HDFC Small Cap** | Jan 2022 – Dec 2025 | 980 | 85.02 | 157.89 | 16.78% | 15.86% | -22.61% | 0.7173 |
| **Axis Small Cap** | Jan 2022 – Dec 2025 | 985 | 69.66 | 121.63 | 14.98% | 13.72% | -19.43% | 0.6847 |
| **SBI Small Cap** | Jan 2022 – Dec 2025 | 986 | 117.83 | 193.77 | 13.27% | 13.30% | -22.42% | 0.5856 |
| **Kotak Small Cap** | Jan 2022 – Dec 2025 | 980 | 189.92 | 294.54 | 11.62% | 13.81% | -24.67% | 0.4655 |

---

## Repository Structure

The project is structured by asset category, with separate directories for raw files, cleaned time-series data, and analytical outputs.

```text
├── Category_Comparison/
│   ├── category_summary.csv                  # Aggregated benchmark metrics across categories
│   ├── equal_weighted_portfolio_results.csv  # Equal-weight portfolio returns and risk metrics
│   └── charts/                               # Cross-category comparison charts (CAGR, Risk-Return, Drawdown)
│
├── Large_cap/
│   ├── clean/                                # Cleaned daily NAV CSVs (2022-2025)
│   ├── analysis/                             # Per-fund analysis CSVs and large_cap_fund_results.csv
│   │   └── charts/                           # Heatmaps, radar, CAGR, and drawdown plots
│   ├── ICICI.xlsx, hdfc.xlsx, ...            # Raw source Excel files
│   └── MF Comparative Analysis...pptx        # Academic presentation deck
│
├── Mid_cap/
│   ├── clean/                                # Cleaned daily NAV CSVs (2022-2025)
│   ├── csv/                                  # Intermediate converted CSVs
│   ├── analysis/                             # Per-fund analysis CSVs and mid_cap_fund_results.csv
│   │   └── charts/                           # Heatmaps, radar, CAGR, and drawdown plots
│   └── *.xlsx                                # Raw AMC Excel datasets
│
├── Small_cap/
│   ├── clean/                                # Cleaned daily NAV CSVs (2022-2025)
│   ├── analysis/                             # Per-fund analysis CSVs and small_cap_fund_results.csv
│   │   └── charts/                           # Heatmaps, radar, CAGR, and drawdown plots
│   └── *.xlsx                                # Raw AMC Excel datasets
│
├── cleaned_data/                             # Intermediate cleaned datasets used in pipelines
├── Mutual_Fund_Comparative_Analysis_Report.md# Complete formal research report
├── build_report_doc.py                       # Python script to compile the Word report (.docx)
│
├── Notebooks:
│   ├── large_cap_cleaning.ipynb              # Large-cap extraction & validation
│   ├── large_cap_fund_analysis.ipynb         # Large-cap returns, drawdown & risk metrics
│   ├── mid_cap_cleaning.ipynb                # Mid-cap extraction & validation
│   ├── mid_cap_fund_analysis.ipynb           # Mid-cap returns, drawdown & risk metrics
│   ├── small_cap_cleaning.ipynb              # Small-cap extraction & validation
│   ├── small_cap_fund_analysis.ipynb         # Small-cap returns, drawdown & risk metrics
│   ├── overall_analysis.ipynb                # Combined cross-category analysis & portfolio comparison
│   ├── mid_cap_excel_to_csv.ipynb            # Excel-to-CSV parser for mid-cap data
│   └── small_cap_excel_to_csv.ipynb          # Excel-to-CSV parser for small-cap data
│
└── .gitignore                                # Excludes checkpoints, temp files, and large parquet dumps
```

---

## Methodology & Calculation Standards

1. **Filtering Criteria:**  
   Only **Direct Plan, Growth Option** series are used to remove distributor commission distortions (TER differentials) and dividend reinvestment timing discrepancies.
2. **Annualized Return (CAGR):**
   $$\text{CAGR} = \left(\frac{\text{NAV}_{\text{end}}}{\text{NAV}_{\text{start}}}\right)^{\frac{365.25}{\text{Days}}} - 1$$
3. **Annualized Volatility:**
   $$\sigma_{\text{ann}} = \sigma_{\text{daily}} \times \sqrt{252}$$
4. **Maximum Drawdown:**
   $$\text{Drawdown}_t = \frac{\text{NAV}_t - \max_{0 \le s \le t} \text{NAV}_s}{\max_{0 \le s \le t} \text{NAV}_s}$$
   $$\text{Max Drawdown} = \min_t(\text{Drawdown}_t)$$
5. **Sharpe Ratio:**
   $$R_{f,\text{daily}} = (1 + 0.06)^{1/252} - 1$$
   $$\text{Sharpe} = \frac{\text{Mean}(\text{Daily Excess Return})}{\text{StdDev}(\text{Daily Returns})} \times \sqrt{252}$$

---

## How to Run

### 1. Requirements
Install required Python libraries:
```bash
pip install pandas numpy matplotlib seaborn openpyxl python-docx
```

### 2. Running Analysis Notebooks
Open the root directory in Jupyter Notebook or VS Code:
- For category-specific data processing: run `large_cap_cleaning.ipynb`, `mid_cap_cleaning.ipynb`, or `small_cap_cleaning.ipynb`.
- For category-specific metrics and chart exports: run `large_cap_fund_analysis.ipynb`, `mid_cap_fund_analysis.ipynb`, or `small_cap_fund_analysis.ipynb`.
- For cross-category comparison and equal-weighted portfolio models: run `overall_analysis.ipynb`.

### 3. Compiling the Word Report
To generate the formatted academic `.docx` report with embedded charts and tables:
```bash
python build_report_doc.py
```
