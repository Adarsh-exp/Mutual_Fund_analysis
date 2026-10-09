# Mutual Fund Analysis (Mid Cap Funds)

A comprehensive quantitative analysis of Indian Mid Cap Mutual Funds covering the period from **2022 to 2025**.

---

## 📊 Funds Analyzed

1. **Axis Midcap Fund** (Direct Plan - Growth)
2. **Bandhan Midcap Fund** (Direct Plan - Growth)
3. **Edelweiss Mid Cap Fund** (Direct Plan - Growth)
4. **Kotak Emerging Equity Fund** (Direct Plan - Growth)
5. **Mahindra Manulife Mid Cap Fund** (Direct Plan - Growth)

---

## 📈 Key Performance Summary (2022 – 2025)

| Fund Name | Observations | Start NAV (₹) | End NAV (₹) | CAGR | Volatility (Ann.) | Max Drawdown | Sharpe Ratio ($R_f=6\%$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Bandhan Midcap Fund** | 834 | 10.01 | 18.25 | **19.52%** | 14.42% | -22.71% | **0.9288** |
| **Mahindra Manulife Mid Cap Fund** | 984 | 19.00 | 38.50 | **19.35%** | 16.12% | -20.92% | **0.8429** |
| **Edelweiss Mid Cap Fund** | 985 | 59.55 | 106.85 | **15.77%** | 14.51% | **-18.17%** | **0.7032** |
| **Axis Midcap Fund** | 989 | 79.09 | 132.07 | **13.71%** | 14.23% | -19.52% | **0.5812** |
| **Kotak Emerging Equity Fund** | 952 | 23.64 | 33.45 | **9.09%** | 15.87% | -24.27% | **0.2919** |

---

## 📁 Repository Structure

```text
├── .gitignore
├── README.md
├── clean_funds.py                             # Automated data cleaning & KPI calculation pipeline
├── combined_midcap_nav.csv                    # Consolidated raw NAV dataset
├── Axis_Midcap_Fund.csv                       # Raw NAV dataset
├── Bandhan_Midcap_Fund.csv                    # Raw NAV dataset
├── Edelweiss_Mid_Cap_Fund.csv                 # Raw NAV dataset
├── Kotak_Emerging_Equity_Fund.csv             # Raw NAV dataset
├── Mahindra_Manulife_Mid_Cap_Fund.csv         # Raw NAV dataset
├── mid_cap_cleaning.ipynb                     # Data cleaning & verification notebook
├── mid_cap_fund_analysis.ipynb                # Analysis, visualization & risk metrics notebook
└── Mid_cap/
    ├── clean/                                 # Cleaned time-series NAVs (2022-2025)
    │   ├── axis_midcap.csv
    │   ├── bandhan_midcap.csv
    │   ├── edelweiss_midcap.csv
    │   ├── kotak_emerging_equity.csv
    │   ├── mahindra_manulife_midcap.csv
    │   └── combined_cleaned_midcap.csv
    └── analysis/                              # Returns, drawdowns & performance summary
        ├── axis_midcap_analysis.csv
        ├── bandhan_midcap_analysis.csv
        ├── edelweiss_midcap_analysis.csv
        ├── kotak_emerging_equity_analysis.csv
        ├── mahindra_manulife_midcap_analysis.csv
        ├── mid_cap_fund_results.csv
        └── charts/                            # Exported charts & visualizations
            ├── mid_cap_cagr.png
            ├── mid_cap_volatility.png
            ├── mid_cap_max_drawdown.png
            ├── mid_cap_sharpe.png
            ├── mid_cap_risk_return.png
            ├── mid_cap_heatmap.png
            └── mid_cap_radar.png
```

---

## ⚙️ How to Run

1. **Clean Datasets & Generate Metrics:**
   ```bash
   python clean_funds.py
   ```
2. **Run Notebooks:**
   - Launch Jupyter and open `mid_cap_fund_analysis.ipynb` for full interactive analysis and charts.
