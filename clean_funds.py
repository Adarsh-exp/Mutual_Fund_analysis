import os
import numpy as np
import pandas as pd

def clean_midcap_funds():
    print("=" * 70)
    print("MID CAP MUTUAL FUND DATASET CLEANING PIPELINE")
    print("=" * 70)

    # Directories
    clean_dir = "Mid_cap/clean"
    analysis_dir = "Mid_cap/analysis"
    os.makedirs(clean_dir, exist_ok=True)
    os.makedirs(analysis_dir, exist_ok=True)

    # Load source data
    source_file = "combined_midcap_nav.csv"
    if not os.path.exists(source_file):
        raise FileNotFoundError(f"Source file {source_file} not found.")

    df_all = pd.read_csv(source_file)
    df_all["date"] = pd.to_datetime(df_all["date"])
    df_all["nav"] = pd.to_numeric(df_all["nav"], errors="coerce")

    funds_map = {
        "Axis Midcap Fund": "axis_midcap",
        "Bandhan Midcap Fund": "bandhan_midcap",
        "Edelweiss Mid Cap Fund": "edelweiss_midcap",
        "Kotak Emerging Equity Fund": "kotak_emerging_equity",
        "Mahindra Manulife Mid Cap Fund": "mahindra_manulife_midcap"
    }

    # Also save raw Edelweiss file if missing for consistency
    edelweiss_raw_path = "Edelweiss_Mid_Cap_Fund.csv"
    if not os.path.exists(edelweiss_raw_path):
        df_edel = df_all[df_all["fund_label"] == "Edelweiss Mid Cap Fund"].copy()
        df_edel[["date", "nav", "scheme_name", "fund_label"]].to_csv(edelweiss_raw_path, index=False)
        print(f"Generated raw file: {edelweiss_raw_path}")

    cleaned_data = {}
    analysis_data = {}
    results = []

    TRADING_DAYS = 252
    RISK_FREE_RATE = 0.06
    daily_rf = (1 + RISK_FREE_RATE) ** (1 / TRADING_DAYS) - 1

    for fund_name, slug in funds_map.items():
        df_fund = df_all[df_all["fund_label"] == fund_name].copy()
        df_fund = df_fund.rename(columns={"date": "Date", "nav": "NAV"})
        
        # 1. Filter valid positive NAV and study period: 2022-01-01 to 2025-12-31
        df_clean = df_fund[
            (df_fund["Date"] >= "2022-01-01") & 
            (df_fund["Date"] <= "2025-12-31") & 
            (df_fund["NAV"] > 0)
        ].copy()

        # 2. Drop missing values, remove duplicate dates, and sort chronologically
        df_clean = (
            df_clean[["Date", "NAV", "scheme_name"]]
            .dropna(subset=["Date", "NAV"])
            .drop_duplicates(subset=["Date"])
            .sort_values("Date")
            .reset_index(drop=True)
        )

        # Save cleaned dataset
        clean_file = os.path.join(clean_dir, f"{slug}.csv")
        df_clean.to_csv(clean_file, index=False)
        cleaned_data[fund_name] = df_clean
        print(f"[{fund_name}] -> Saved cleaned dataset: {clean_file} ({len(df_clean)} records)")

        # 3. Compute returns, cumulative max, and drawdowns
        df_an = df_clean.copy()
        df_an["Daily_Return"] = df_an["NAV"].pct_change()
        df_an["Running_Max"] = df_an["NAV"].cummax()
        df_an["Drawdown"] = (df_an["NAV"] - df_an["Running_Max"]) / df_an["Running_Max"]

        analysis_file = os.path.join(analysis_dir, f"{slug}_analysis.csv")
        df_an.to_csv(analysis_file, index=False)
        analysis_data[fund_name] = df_an
        print(f"[{fund_name}] -> Saved analysis dataset: {analysis_file}")

        # 4. Calculate key metrics
        start_date = df_an["Date"].iloc[0]
        end_date = df_an["Date"].iloc[-1]
        start_nav = float(df_an["NAV"].iloc[0])
        end_nav = float(df_an["NAV"].iloc[-1])

        years = (end_date - start_date).days / 365.25
        cagr = ((end_nav / start_nav) ** (1 / years)) - 1

        daily_rets = df_an["Daily_Return"].dropna()
        volatility = float(daily_rets.std() * np.sqrt(TRADING_DAYS))
        max_dd = float(df_an["Drawdown"].min())

        excess_returns = daily_rets - daily_rf
        sharpe = float((excess_returns.mean() / daily_rets.std()) * np.sqrt(TRADING_DAYS))

        results.append({
            "Fund": fund_name,
            "Start Date": start_date.strftime("%Y-%m-%d"),
            "End Date": end_date.strftime("%Y-%m-%d"),
            "Observations": len(df_an),
            "Start NAV": round(start_nav, 4),
            "End NAV": round(end_nav, 4),
            "CAGR": round(cagr, 6),
            "Volatility": round(volatility, 6),
            "Maximum Drawdown": round(max_dd, 6),
            "Sharpe Ratio": round(sharpe, 6)
        })

    # Save summary results
    results_df = pd.DataFrame(results)
    results_path = os.path.join(analysis_dir, "mid_cap_fund_results.csv")
    results_df.to_csv(results_path, index=False)
    print(f"\nSaved Performance Summary: {results_path}")

    # Create combined pivot dataset for multi-fund comparison
    combined_navs = []
    for fund_name, df in cleaned_data.items():
        sub = df[["Date", "NAV"]].copy().rename(columns={"NAV": fund_name})
        combined_navs.append(sub)

    combined_df = combined_navs[0]
    for sub in combined_navs[1:]:
        combined_df = pd.merge(combined_df, sub, on="Date", how="outer")

    combined_df = combined_df.sort_values("Date").reset_index(drop=True)
    combined_clean_path = os.path.join(clean_dir, "combined_cleaned_midcap.csv")
    combined_df.to_csv(combined_clean_path, index=False)
    print(f"Saved Combined Comparison Dataset: {combined_clean_path}")

    print("\n" + "=" * 70)
    print("CLEANING COMPLETE - PERFORMANCE SUMMARY (2022 - 2025):")
    print("=" * 70)
    print(results_df.to_string(index=False))

if __name__ == "__main__":
    clean_midcap_funds()
