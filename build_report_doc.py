import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def create_report_docx(output_path):
    doc = Document()

    # Define color palette
    COLOR_PRIMARY = RGBColor(27, 54, 93)     # Deep Navy
    COLOR_SECONDARY = RGBColor(43, 84, 126)  # Slate Blue
    COLOR_DARK = RGBColor(33, 37, 41)        # Charcoal Body Text
    COLOR_MUTED = RGBColor(108, 117, 125)    # Gray
    HEX_PRIMARY = "1B365D"
    HEX_SECONDARY = "2B547E"
    HEX_LIGHT_BG = "F4F6F9"
    HEX_ZEBRA = "F8F9FA"
    HEX_BORDER = "D1D5DB"

    # Configure 1-inch margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)

    # Base Normal Style
    style_normal = doc.styles['Normal']
    font_normal = style_normal.font
    font_normal.name = 'Calibri'
    font_normal.size = Pt(11)
    font_normal.color.rgb = COLOR_DARK
    style_normal.paragraph_format.line_spacing = 1.15
    style_normal.paragraph_format.space_after = Pt(6)

    # XML Helper functions
    def set_cell_background(cell, hex_color):
        tc_pr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
        tc_pr.append(shd)

    def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
        tc_pr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
        tc_pr.append(tcMar)

    def set_table_borders(table, border_color=HEX_BORDER):
        tblPr = table._tbl.tblPr
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>'
            f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="{HEX_PRIMARY}"/>'
            f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>'
            f'<w:insideV w:val="none"/>'
            f'<w:left w:val="none"/>'
            f'<w:right w:val="none"/>'
            f'</w:tblBorders>'
        )
        tblPr.append(borders)

    def add_p(text, bold=False, italic=False, size=11, color=COLOR_DARK, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=6):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(text)
        run.bold = bold
        run.italic = italic
        run.font.size = Pt(size)
        run.font.color.rgb = color
        return p

    def add_h1(title, page_break=True):
        if page_break:
            doc.add_page_break()
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(10)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title)
        run.bold = True
        run.font.size = Pt(18)
        run.font.color.rgb = COLOR_PRIMARY
        return p

    def add_h2(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title)
        run.bold = True
        run.font.size = Pt(13)
        run.font.color.rgb = COLOR_SECONDARY
        return p

    def add_h3(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title)
        run.bold = True
        run.font.size = Pt(11.5)
        run.font.color.rgb = COLOR_DARK
        return p

    def add_bullet(bold_prefix, text):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            run_b = p.add_run(bold_prefix)
            run_b.bold = True
            run_b.font.color.rgb = COLOR_DARK
        run_t = p.add_run(text)
        run_t.font.color.rgb = COLOR_DARK
        return p

    def add_callout(text, bold_prefix="Key Takeaway: "):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = table.cell(0, 0)
        cell.width = Inches(6.5)
        set_cell_background(cell, HEX_LIGHT_BG)
        set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
        tcPr = cell._tc.get_or_add_tcPr()
        borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="{HEX_PRIMARY}"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
        tcPr.append(borders)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        run_bp = p.add_run(bold_prefix)
        run_bp.bold = True
        run_bp.font.color.rgb = COLOR_PRIMARY
        run_t = p.add_run(text)
        run_t.font.color.rgb = COLOR_DARK
        p_after = doc.add_paragraph()
        p_after.paragraph_format.space_before = Pt(0)
        p_after.paragraph_format.space_after = Pt(4)

    def add_custom_table(headers, data, col_widths=None, alignments=None):
        num_rows = len(data) + 1
        num_cols = len(headers)
        table = doc.add_table(rows=num_rows, cols=num_cols)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(table)

        # Header Row
        hdr_row = table.rows[0]
        tblPr = table._tbl.tblPr
        for i, h_text in enumerate(headers):
            cell = hdr_row.cells[i]
            set_cell_background(cell, HEX_PRIMARY)
            set_cell_margins(cell, top=120, bottom=120, left=120, right=120)
            if col_widths and i < len(col_widths):
                cell.width = Inches(col_widths[i])
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            align = alignments[i] if alignments and i < len(alignments) else WD_ALIGN_PARAGRAPH.LEFT
            p.alignment = align
            run = p.add_run(h_text)
            run.bold = True
            run.font.size = Pt(9.5)
            run.font.color.rgb = RGBColor(255, 255, 255)

        # Data Rows
        for r_idx, row_data in enumerate(data):
            row = table.rows[r_idx + 1]
            bg_color = HEX_ZEBRA if r_idx % 2 == 1 else "FFFFFF"
            for c_idx, val in enumerate(row_data):
                cell = row.cells[c_idx]
                if bg_color != "FFFFFF":
                    set_cell_background(cell, bg_color)
                set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
                if col_widths and c_idx < len(col_widths):
                    cell.width = Inches(col_widths[c_idx])
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                p = cell.paragraphs[0]
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                align = alignments[c_idx] if alignments and c_idx < len(alignments) else WD_ALIGN_PARAGRAPH.LEFT
                p.alignment = align
                run = p.add_run(str(val))
                run.font.size = Pt(9)
                run.font.color.rgb = COLOR_DARK

        p_spacer = doc.add_paragraph()
        p_spacer.paragraph_format.space_before = Pt(0)
        p_spacer.paragraph_format.space_after = Pt(6)

    def add_image_if_exists(img_path, caption=None, width=Inches(5.8)):
        if os.path.exists(img_path):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(2)
            run = p.add_run()
            run.add_picture(img_path, width=width)
            if caption:
                p_cap = doc.add_paragraph()
                p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_cap.paragraph_format.space_before = Pt(0)
                p_cap.paragraph_format.space_after = Pt(8)
                run_cap = p_cap.add_run(f"Figure: {caption}")
                run_cap.italic = True
                run_cap.font.size = Pt(9)
                run_cap.font.color.rgb = COLOR_MUTED

    # =========================================================================
    # 1. COVER PAGE
    # =========================================================================
    add_p("1. COVER PAGE", bold=True, size=11, color=COLOR_MUTED, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=12, space_after=6)
    add_p("ACADEMIC & INDUSTRY RESEARCH REPORT", bold=True, size=12, color=COLOR_SECONDARY, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=12, space_after=12)
    add_p("COMPARATIVE PERFORMANCE AND RISK-ADJUSTED RETURN ANALYSIS OF INDIAN EQUITY MUTUAL FUNDS (2022–2025)", bold=True, size=22, color=COLOR_PRIMARY, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=12, space_after=12)
    add_p("An Empirical Investigation of Return, Volatility, Downside Risk, and Portfolio Efficiency Across Large-Cap, Mid-Cap, and Small-Cap Categories", italic=True, size=12, color=COLOR_DARK, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=36)

    # Metadata Box
    cov_table = doc.add_table(rows=1, cols=1)
    cov_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cov_cell = cov_table.cell(0, 0)
    cov_cell.width = Inches(6.0)
    set_cell_background(cov_cell, HEX_LIGHT_BG)
    set_cell_margins(cov_cell, top=160, bottom=160, left=200, right=200)
    tcPr = cov_cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="18" w:space="0" w:color="{HEX_PRIMARY}"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
    tcPr.append(borders)

    cp = cov_cell.paragraphs[0]
    cp.paragraph_format.space_before = Pt(2)
    cp.paragraph_format.space_after = Pt(2)
    cp.paragraph_format.line_spacing = 1.3
    
    def add_meta_line(label, val):
        r1 = cp.add_run(f"{label}: ")
        r1.bold = True
        r1.font.size = Pt(10)
        r1.font.color.rgb = COLOR_PRIMARY
        r2 = cp.add_run(f"{val}\n")
        r2.font.size = Pt(10)
        r2.font.color.rgb = COLOR_DARK

    add_meta_line("Domain", "Fintech / Quantitative Investment Analysis / Portfolio Management")
    add_meta_line("Program", "B.Tech / MBA in Financial Technology / Finance")
    add_meta_line("Candidate Name", "[Student Name(s)]")
    add_meta_line("Roll / Reg. No.", "[Roll Number / Registration ID]")
    add_meta_line("Faculty Supervisor", "[Supervisor / Project Guide Name], [Designation]")
    add_meta_line("Department", "Department of Financial Technology / Finance")
    add_meta_line("Institution", "[Institution / University Name, City]")
    add_meta_line("Academic Year", "2025–2026")
    add_meta_line("Date of Submission", "October 2026")

    # =========================================================================
    # 2. CERTIFICATE
    # =========================================================================
    add_h1("2. CERTIFICATE", page_break=True)
    add_p(
        "This is to certify that the project report entitled \"Comparative Performance and Risk-Adjusted Return Analysis of Indian Equity Mutual Funds (2022–2025)\", "
        "submitted by [Student Name] (Roll No: [Roll Number]) in partial fulfillment of the requirements for the award of the degree in [Degree / Specialization], "
        "is an authentic record of independent empirical research carried out under my supervision and guidance."
    )
    add_p(
        "To the best of my knowledge, the matter embodied in this report has not been submitted to any other university or institute for the award of any degree or diploma. "
        "The quantitative data pipelines, daily Net Asset Value (NAV) records, mathematical formulations, and empirical findings documented herein have been verified "
        "and reflect genuine scientific investigation utilizing verified public datasets from the Association of Mutual Funds in India (AMFI) and respective Asset Management Companies."
    )
    add_p("", space_before=36, space_after=12)

    # Signature Table
    sig_table = doc.add_table(rows=1, cols=2)
    sig_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    c1, c2 = sig_table.rows[0].cells
    c1.width = Inches(3.25)
    c2.width = Inches(3.25)
    
    p1 = c1.paragraphs[0]
    p1.paragraph_format.line_spacing = 1.2
    p1.add_run("_______________________________\n").bold = True
    p1.add_run("[Supervisor Name]\n").bold = True
    p1.add_run("Project Supervisor\nDepartment of Financial Technology\n[Institution Name]")

    p2 = c2.paragraphs[0]
    p2.paragraph_format.line_spacing = 1.2
    p2.add_run("_______________________________\n").bold = True
    p2.add_run("Head of Department\n").bold = True
    p2.add_run("Department of Financial Technology\n[Institution Name]")

    add_p("Date: ____________________\nPlace: ____________________", space_before=24, space_after=6)

    # =========================================================================
    # 3. ACKNOWLEDGEMENT
    # =========================================================================
    add_h1("3. ACKNOWLEDGEMENT", page_break=True)
    add_p(
        "I express my deepest gratitude to my project supervisor, [Supervisor Name], whose rigorous feedback, academic guidance, and constructive critiques "
        "shaped the methodology, data sanitation standards, and econometric structure of this study. Their support in ensuring analytical rigor was instrumental throughout the project."
    )
    add_p(
        "I extend sincere appreciation to the faculty members and administrative staff of the Department of [Department Name] at [Institution Name] for providing the computational infrastructure, "
        "Python data engineering environment, and intellectual ecosystem necessary to execute this quantitative study."
    )
    add_p(
        "I also express sincere thanks to the Association of Mutual Funds in India (AMFI) and the respective Asset Management Companies—Nippon India, ICICI Prudential, HDFC, DSP, Bandhan, "
        "Aditya Birla Sun Life, Axis, Mahindra Manulife, SBI, and Kotak Mahindra—for maintaining transparent, publicly accessible daily historical NAV archives that made this empirical study possible."
    )
    add_p(
        "Finally, I am profoundly indebted to my family and peers for their continuous encouragement, patience, and moral support throughout the completion of this research report."
    )

    # =========================================================================
    # 4. EXECUTIVE SUMMARY
    # =========================================================================
    add_h1("4. EXECUTIVE SUMMARY", page_break=True)
    add_p(
        "Between January 3, 2022 and December 31, 2025, Indian equity capital markets weathered significant macroeconomic shifts: rapid post-COVID economic normalisation, "
        "global supply chain shocks, aggressive monetary policy tightening by the Reserve Bank of India (RBI Repo Rate increasing from 4.00% to 6.50%), and record domestic "
        "retail inflows channelled through Systematic Investment Plans (SIPs exceeding ₹25,000 crore monthly)."
    )
    add_p(
        "This project presents a rigorous empirical investigation into the performance of 15 actively managed Indian equity mutual funds across three core market-capitalization tiers: "
        "Large-Cap, Mid-Cap, and Small-Cap (5 representative funds per category). All funds were evaluated using Direct Plan, Growth Option daily Net Asset Value (NAV) time series "
        "across 979 to 991 active trading sessions."
    )
    add_h2("Key Empirical Findings:")
    add_bullet("Mid-Caps Outperformed in Nominal and Risk-Adjusted Terms: ", "Mid-Cap funds delivered both the highest annualized compounding growth rate (Category Mean CAGR: 16.87%) and the highest risk-adjusted efficiency (Category Mean Sharpe Ratio: 0.7422; Equal-Weighted Portfolio Sharpe: 0.7658 against a 6.00% risk-free hurdle rate).")
    add_bullet("Small-Cap Risk-Return Inversion: ", "Despite taking on higher volatility (14.59%) and suffering the deepest maximum drawdowns (Category Mean: -22.67%), Small-Cap funds generated a lower 4-year CAGR (14.94%) than both Mid-Caps and Large-Caps, producing the lowest category Sharpe Ratio (0.6451).")
    add_bullet("Large-Cap Capital Preservation: ", "Large-Cap funds proved exceptionally defensive, delivering a 15.27% CAGR with the lowest volatility (13.04%) and shallowest maximum drawdown (-16.85%), yielding a strong Sharpe Ratio of 0.7310 (Equal-Weighted: 0.7489).")
    add_bullet("Significant Intra-Category Manager Dispersion: ", "Active fund selection drove dramatic performance divergence: HDFC Mid-Cap Opportunities Fund led all 15 schemes with a 22.74% CAGR, 1.0907 Sharpe Ratio, and -16.76% maximum drawdown, whereas peers like Axis Midcap achieved 13.71% CAGR (0.5805 Sharpe). In Small-Caps, Nippon India Small Cap achieved 18.04% CAGR (0.7726 Sharpe), while Kotak Small Cap lagged at 11.62% CAGR (0.4655 Sharpe, -24.67% drawdown).")
    
    add_callout(
        "Over the 2022–2025 cycle, the conventional size premium broke down: Mid-Caps (16.87% CAGR, 0.742 Sharpe) offered superior returns and efficiency over Small-Caps (14.94% CAGR, 0.645 Sharpe), "
        "while Large-Caps (15.27% CAGR, 0.731 Sharpe) demonstrated outstanding downside protection.",
        bold_prefix="Core Conclusion: "
    )

    # =========================================================================
    # 5. PROBLEM STATEMENT
    # =========================================================================
    add_h1("5. PROBLEM STATEMENT", page_break=True)
    add_p(
        "Individual and institutional investors frequently make mutual fund capital allocation decisions based on trailing 1-year or 3-year point-to-point nominal returns. "
        "This heuristic approach exhibits critical analytical vulnerabilities:"
    )
    add_bullet("Insensitivity to Volatility and Downside Drawdowns: ", "A fund delivering an attractive headline CAGR may expose investors to severe -20% to -25% drawdowns, triggering behavioral panic and premature wealth destruction during corrections.")
    add_bullet("Ambiguity in Lower-Cap Risk Premiums: ", "Theoretical asset pricing models (e.g., Fama-French size factor) assume small-cap equities systematically yield higher returns to compensate for illiquidity and operational risk. However, real-world monetary cycles and valuation froth frequently disrupt this relationship.")
    add_bullet("Distortion from Distribution Commissions: ", "Historical studies evaluating Regular Plans conflated distribution fees (TER drag of 0.50% to 1.50% p.a.) with intrinsic portfolio management alpha. Direct Plan analysis is mandatory to isolate genuine manager skill.")
    add_callout(
        "\"How do actively managed Indian Large-Cap, Mid-Cap, and Small-Cap equity mutual funds compare across CAGR, annualized volatility, maximum drawdown, and the Sharpe Ratio over the 2022–2025 market cycle, and does empirical evidence justify the elevated downside volatility inherent in lower-cap allocations?\"",
        bold_prefix="Central Research Question: "
    )

    # =========================================================================
    # 6. OBJECTIVES
    # =========================================================================
    add_h1("6. OBJECTIVES", page_break=True)
    add_p("To resolve the problem statement with quantitative rigor, the study executes five core objectives:")
    add_bullet("1. Clean Data Engineering Pipeline: ", "Extract, clean, validate, and synchronize daily historical NAV records for 15 prominent Indian equity schemes over 2022–2025.")
    add_bullet("2. Comprehensive Fund-Level Metrics: ", "Calculate multi-year Compound Annual Growth Rate (CAGR), annualized standard deviation (volatility, scaled by √252), and continuous high-water-mark peak-to-trough Maximum Drawdown (MDD).")
    add_bullet("3. Rigorous Risk-Adjusted Alpha Measurement: ", "Compute the annualized Sharpe Ratio using an institutionally validated Indian risk-free benchmark (Rf = 6.00% p.a., reflecting the 91-day/364-day Treasury Bill rate), compounding deductions on a daily continuous basis.")
    add_bullet("4. Category and Portfolio Benchmarking: ", "Perform cross-sectional category mean evaluations and simulate daily rebalanced, equal-weighted synthetic category portfolios over 979 common trading days.")
    add_bullet("5. Actionable Asset Allocation Formulations: ", "Translate empirical risk-return profiles into practical asset allocation recommendations and risk management guidelines for wealth managers and individual investors.")

    # =========================================================================
    # 7. INDUSTRY BACKGROUND
    # =========================================================================
    add_h1("7. INDUSTRY BACKGROUND", page_break=True)
    add_h2("7.1 Structural Scale and Transformation")
    add_p(
        "Governed by the Securities and Exchange Board of India (SEBI) and coordinated through the Association of Mutual Funds in India (AMFI), "
        "India's mutual fund industry has grown rapidly under SEBI's regulatory stewardship. Industry Assets Under Management (AUM) expanded from ~₹10 lakh crore in 2014 "
        "to over ₹65 lakh crore by 2025/2026. This exponential growth has been fueled by domestic household financialisation, zero-commission fintech platforms, and disciplined monthly SIP flows."
    )
    add_h2("7.2 The SEBI Categorisation Framework (October 2017)")
    add_p(
        "Prior to SEBI's landmark circular (SEBI/HO/IMD/DF3/CIR/P/2017/114), fund houses assigned arbitrary labels to their funds. "
        "SEBI instituted rigid, standardized portfolio allocation rules based on bi-annually updated AMFI market capitalization rankings:"
    )
    add_bullet("Large-Cap Equity Funds: ", "Must maintain at least 80% investment in the top 100 companies by full market capitalization.")
    add_bullet("Mid-Cap Equity Funds: ", "Must maintain at least 65% investment in companies ranked 101st to 250th.")
    add_bullet("Small-Cap Equity Funds: ", "Must maintain at least 65% investment in companies ranked 251st and beyond.")
    add_h2("7.3 Direct Plan Architecture")
    add_p(
        "Mandated by SEBI in January 2013, Direct Plans bypass distributors, eliminating distribution commissions and lowering Total Expense Ratios (TER) "
        "by 50 to 150 basis points annually. Evaluating Direct Plans isolates the pure investment management skill of the portfolio team."
    )

    # =========================================================================
    # 8. LITERATURE REVIEW
    # =========================================================================
    add_h1("8. LITERATURE REVIEW", page_break=True)
    add_p("This empirical evaluation builds upon foundational theoretical frameworks in modern financial economics:")
    add_bullet("Markowitz (1952) – Modern Portfolio Theory: ", "Established that rational investors evaluate portfolios along an efficient frontier of expected return versus portfolio variance, maximizing diversification benefits across non-perfectly correlated assets.")
    add_bullet("Sharpe (1964, 1966, 1994) – CAPM & Sharpe Ratio: ", "Formulated the Capital Asset Pricing Model and the Reward-to-Variability ratio (Sharpe Ratio), measuring excess return earned above a sovereign risk-free rate per unit of total annualized standard deviation: Sp = (Rp - Rf) / σp.")
    add_bullet("Fama & French (1992, 1993) – The Size Factor (SMB): ", "Posited that smaller market-cap equities should systematically generate higher returns (Small Minus Big premium) to compensate for liquidity constraints and cyclical sensitivity. However, empirical studies in emerging markets (Sehgal & Jhanwar, 2008) indicate the size premium experiences protracted cyclical compressions.")
    add_bullet("Chekhlov, Uryasev, & Zabarankin (2005) – Drawdown Optimization: ", "Demonstrated that variance treats upside and downside price swings symmetrically, whereas investors experience asymmetric psychological distress from peak-to-trough drawdowns, making Maximum Drawdown (MDD) the gold standard for downside tail-risk assessment.")

    # =========================================================================
    # 9. DATASET DESCRIPTION
    # =========================================================================
    add_h1("9. DATASET DESCRIPTION", page_break=True)
    add_p(
        "The empirical corpus comprises daily historical Net Asset Value (NAV) records for 15 leading equity mutual funds across India's top Asset Management Companies (AMCs). "
        "All funds were analyzed strictly in their Direct Plan, Growth Option share classes across the 4-year calendar window from January 3, 2022 to December 31, 2025."
    )
    
    headers_ds = ["Category", "Scheme Name", "Plan", "Option", "AMC Entity"]
    data_ds = [
        ["Large Cap", "Nippon India Large Cap Fund", "Direct", "Growth", "Nippon Life India AM"],
        ["Large Cap", "ICICI Prudential Large Cap Fund", "Direct", "Growth", "ICICI Prudential AMC"],
        ["Large Cap", "HDFC Large Cap Fund", "Direct", "Growth", "HDFC AMC"],
        ["Large Cap", "DSP Large Cap Fund", "Direct", "Growth", "DSP Investment Managers"],
        ["Large Cap", "Bandhan Large Cap Fund", "Direct", "Growth", "Bandhan AMC"],
        ["Mid Cap", "HDFC Mid-Cap Opportunities Fund", "Direct", "Growth", "HDFC AMC"],
        ["Mid Cap", "Mahindra Manulife Mid Cap Fund", "Direct", "Growth", "Mahindra Manulife AMC"],
        ["Mid Cap", "Aditya Birla Sun Life Midcap Fund", "Direct", "Growth", "Aditya Birla Sun Life AMC"],
        ["Mid Cap", "DSP Midcap Fund", "Direct", "Growth", "DSP Investment Managers"],
        ["Mid Cap", "Axis Midcap Fund", "Direct", "Growth", "Axis AMC"],
        ["Small Cap", "Nippon India Small Cap Fund", "Direct", "Growth", "Nippon Life India AM"],
        ["Small Cap", "HDFC Small Cap Fund", "Direct", "Growth", "HDFC AMC"],
        ["Small Cap", "Axis Small Cap Fund", "Direct", "Growth", "Axis AMC"],
        ["Small Cap", "SBI Small Cap Fund", "Direct", "Growth", "SBI Funds Management"],
        ["Small Cap", "Kotak Small Cap Fund", "Direct", "Growth", "Kotak Mahindra AMC"]
    ]
    add_custom_table(headers_ds, data_ds, col_widths=[1.1, 2.5, 0.8, 0.8, 1.8])

    # =========================================================================
    # 10. METHODOLOGY
    # =========================================================================
    add_h1("10. METHODOLOGY", page_break=True)
    add_p("The quantitative pipeline follows an isolated, fund-by-fund computational protocol. Raw NAV records are never pooled prior to metric derivation.")
    add_h2("Mathematical Formulations:")
    add_bullet("1. Daily Percentage Return (Rt): ", "Rt = (NAVt - NAVt-1) / NAVt-1")
    add_bullet("2. Compound Annual Growth Rate (CAGR): ", "CAGR = (NAVT / NAV0)^(1 / Y) - 1, where elapsed years Y = (DateT - Date0) / 365.25 ≈ 3.9918 years.")
    add_bullet("3. Annualized Volatility (σann): ", "σann = StdDev(Rt) × √252, assuming 252 active trading sessions per annum.")
    add_bullet("4. Running Peak (Pt) and Maximum Drawdown (MDD): ", "Pt = max(NAV0 ... NAVt), Drawdownt = (NAVt - Pt) / Pt, MDD = min(Drawdownt).")
    add_bullet("5. Annualized Sharpe Ratio (Sp): ", "With an annual risk-free rate Rf = 6.00% (0.06), the daily compounded rate is rf,daily = (1.06)^(1/252) - 1 ≈ 0.02313% per day. Sp = [Mean(Rt - rf,daily) / StdDev(Rt)] × √252.")

    # =========================================================================
    # 11. DATA CLEANING
    # =========================================================================
    add_h1("11. DATA CLEANING AND PREPROCESSING", page_break=True)
    add_p(
        "Raw registrar files often contain metadata rows, whitespace errors, and inconsistent plan designations. "
        "A Python cleaning pipeline was executed across large_cap_cleaning.ipynb, mid_cap_cleaning.ipynb, and small_cap_cleaning.ipynb:"
    )
    add_bullet("Header Alignment: ", "Skipped AMC preamble descriptive rows to detect actual column headers at row 4.")
    add_bullet("String Sanitization: ", "Stripped leading/trailing whitespaces from column names and text entries.")
    add_bullet("Regex Sub-Plan Filtering: ", "Retained records satisfying Plan =~ /direct/i and Option =~ /growth/i.")
    add_bullet("Temporal Bounding: ", "Enforced exact observation boundary: 2022-01-01 <= Date <= 2025-12-31.")
    add_bullet("Missing Value Scrub: ", "Executed dropna(subset=['Date', 'NAV']) and sorted records in ascending chronological order.")
    add_bullet("Quality Fix: ", "Identified that HDFC Large Cap initially ended prematurely on 19-Dec-2025. Programmatically queried and backfilled missing trading sessions through 31-Dec-2025 from AMFI, harmonizing all 985 records.")

    # =========================================================================
    # 12. EXPLORATORY DATA ANALYSIS
    # =========================================================================
    add_h1("12. EXPLORATORY DATA ANALYSIS (EDA)", page_break=True)
    add_p(
        "Exploratory analysis revealed three macro-regimes over the 2022–2025 window:\n"
        "• 2022–Early 2023: Global rate hikes and geopolitical shocks produced sideways equity consolidation. Large-Caps acted as defensive buffers (drawdowns limited to -15% to -19%), while Small-Caps dropped -20% to -25%.\n"
        "• Mid 2023–Mid 2024: Robust domestic economic growth and record retail SIP flows fueled an aggressive rally led by Mid and Small-Caps.\n"
        "• Late 2024–2025: SEBI warnings regarding small-cap valuation froth and subsequent regulatory stress tests precipitated corrections in micro and small-cap stocks, impairing their terminal 4-year compounding."
    )
    add_image_if_exists("Category_Comparison/charts/category_risk_return.png", caption="Category Risk-Return Scatter Plot (CAGR vs. Volatility)")

    # =========================================================================
    # 13. STATISTICAL ANALYSIS
    # =========================================================================
    add_h1("13. STATISTICAL ANALYSIS", page_break=True)
    add_p("To evaluate return behavior beyond standard normal assumptions, higher-order statistical moments and correlations were evaluated across the 979 common concurrent trading dates:")
    add_h2("13.1 Statistical Moments of Daily Category Returns")
    
    headers_moments = ["Category Portfolio", "Daily Mean", "Daily Std Dev", "Skewness", "Kurtosis", "Daily Min", "Daily Max", "Obs"]
    data_moments = [
        ["Large Cap", "+0.0617%", "0.8094%", "-0.6020", "5.1240", "-5.7201%", "+3.4300%", "979"],
        ["Mid Cap", "+0.0695%", "0.9257%", "-0.9463", "5.8912", "-6.3709%", "+3.5567%", "979"],
        ["Small Cap", "+0.0610%", "0.8936%", "-1.0334", "5.4218", "-5.3947%", "+3.4427%", "979"]
    ]
    add_custom_table(headers_moments, data_moments, col_widths=[1.2, 0.8, 0.9, 0.8, 0.8, 0.8, 0.8, 0.4], alignments=[WD_ALIGN_PARAGRAPH.LEFT] + [WD_ALIGN_PARAGRAPH.RIGHT]*7)
    
    add_bullet("Pronounced Negative Skewness: ", "All categories display left-tail skewness, highest in Small-Caps (-1.0334) and Mid-Caps (-0.9463). This demonstrates asymmetric downside crash risk.")
    add_bullet("Leptokurtosis (Fat Tails): ", "Kurtosis values exceed 5.0 across all categories, indicating higher outlier probability than a standard Gaussian distribution.")

    add_h2("13.2 Inter-Category Correlation Matrix")
    headers_corr = ["Category", "Large Cap", "Mid Cap", "Small Cap"]
    data_corr = [
        ["Large Cap", "1.0000", "0.8852", "0.8165"],
        ["Mid Cap", "0.8852", "1.0000", "0.9422"],
        ["Small Cap", "0.8165", "0.9422", "1.0000"]
    ]
    add_custom_table(headers_corr, data_corr, col_widths=[1.8, 1.5, 1.5, 1.5], alignments=[WD_ALIGN_PARAGRAPH.LEFT] + [WD_ALIGN_PARAGRAPH.RIGHT]*3)
    add_bullet("High Mid-to-Small Correlation (ρ = 0.9422): ", "Confirms shared liquidity sensitivity between lower-market-cap tiers.")
    add_bullet("Diversification Benefit (ρ = 0.8165): ", "The lower correlation between Large and Small-Caps confirms significant portfolio volatility dampening when combining both segments.")

    # =========================================================================
    # 14. RESULTS
    # =========================================================================
    add_h1("14. RESULTS", page_break=True)
    add_p("Comprehensive fund-level metrics and category aggregations are presented below:")
    
    add_h2("14.1 Large-Cap Equity Mutual Funds (2022–2025)")
    headers_lc = ["Fund Name", "Start Date", "End Date", "Obs", "Start NAV", "End NAV", "CAGR", "Volatility", "Max Drawdown", "Sharpe"]
    data_lc = [
        ["Nippon India Large Cap", "2022-01-03", "2025-12-31", "985", "₹54.40", "₹105.34", "18.00%", "13.67%", "-15.37%", "0.8806"],
        ["ICICI Prudential Large Cap", "2022-01-03", "2025-12-31", "985", "₹71.08", "₹127.17", "15.69%", "12.40%", "-15.39%", "0.7939"],
        ["HDFC Large Cap", "2022-01-03", "2025-12-31", "985", "₹732.75", "₹1279.95", "15.00%", "13.16%", "-16.36%", "0.7090"],
        ["DSP Large Cap", "2022-01-03", "2025-12-31", "985", "₹312.61", "₹534.94", "14.40%", "12.44%", "-17.68%", "0.6998"],
        ["Bandhan Large Cap", "2022-01-03", "2025-12-31", "991", "₹56.45", "₹92.77", "13.25%", "13.53%", "-19.42%", "0.5717"]
    ]
    add_custom_table(headers_lc, data_lc, col_widths=[1.8, 0.7, 0.7, 0.4, 0.6, 0.6, 0.5, 0.6, 0.7, 0.5], alignments=[WD_ALIGN_PARAGRAPH.LEFT] + [WD_ALIGN_PARAGRAPH.RIGHT]*9)

    add_h2("14.2 Mid-Cap Equity Mutual Funds (2022–2025)")
    headers_mc = ["Fund Name", "Start Date", "End Date", "Obs", "Start NAV", "End NAV", "CAGR", "Volatility", "Max Drawdown", "Sharpe"]
    data_mc = [
        ["HDFC Mid-Cap Opportunities", "2022-01-03", "2025-12-31", "985", "₹99.18", "₹224.75", "22.74%", "14.89%", "-16.76%", "1.0907"],
        ["Mahindra Manulife Mid Cap", "2022-01-03", "2025-12-31", "985", "₹19.00", "₹38.50", "19.35%", "16.11%", "-20.92%", "0.8421"],
        ["Aditya Birla Sun Life Midcap", "2022-01-03", "2025-12-31", "985", "₹521.91", "₹899.26", "14.60%", "15.03%", "-21.87%", "0.6149"],
        ["DSP Midcap", "2022-01-03", "2025-12-31", "985", "₹98.95", "₹166.52", "13.93%", "14.75%", "-21.41%", "0.5830"],
        ["Axis Midcap", "2022-01-03", "2025-12-31", "990", "₹79.09", "₹132.07", "13.71%", "14.22%", "-19.52%", "0.5805"]
    ]
    add_custom_table(headers_mc, data_mc, col_widths=[1.8, 0.7, 0.7, 0.4, 0.6, 0.6, 0.5, 0.6, 0.7, 0.5], alignments=[WD_ALIGN_PARAGRAPH.LEFT] + [WD_ALIGN_PARAGRAPH.RIGHT]*9)

    add_h2("14.3 Small-Cap Equity Mutual Funds (2022–2025)")
    headers_sc = ["Fund Name", "Start Date", "End Date", "Obs", "Start NAV", "End NAV", "CAGR", "Volatility", "Max Drawdown", "Sharpe"]
    data_sc = [
        ["Nippon India Small Cap", "2022-01-03", "2025-12-31", "980", "₹96.45", "₹187.02", "18.04%", "16.25%", "-24.21%", "0.7726"],
        ["HDFC Small Cap", "2022-01-03", "2025-12-31", "980", "₹85.02", "₹157.89", "16.78%", "15.86%", "-22.61%", "0.7173"],
        ["Axis Small Cap", "2022-01-03", "2025-12-31", "985", "₹69.66", "₹121.63", "14.98%", "13.72%", "-19.43%", "0.6847"],
        ["SBI Small Cap", "2022-01-03", "2025-12-31", "986", "₹117.83", "₹193.77", "13.27%", "13.30%", "-22.42%", "0.5856"],
        ["Kotak Small Cap", "2022-01-03", "2025-12-31", "980", "₹189.92", "₹294.54", "11.62%", "13.81%", "-24.67%", "0.4655"]
    ]
    add_custom_table(headers_sc, data_sc, col_widths=[1.8, 0.7, 0.7, 0.4, 0.6, 0.6, 0.5, 0.6, 0.7, 0.5], alignments=[WD_ALIGN_PARAGRAPH.LEFT] + [WD_ALIGN_PARAGRAPH.RIGHT]*9)

    add_h2("14.4 Category Aggregations")
    add_h3("Category Arithmetic Means")
    headers_cat = ["Category", "Mean CAGR", "Mean Volatility", "Mean Max Drawdown", "Mean Sharpe Ratio"]
    data_cat = [
        ["Large Cap", "15.27%", "13.04%", "-16.85%", "0.7310"],
        ["Mid Cap", "16.87%", "15.00%", "-20.10%", "0.7422"],
        ["Small Cap", "14.94%", "14.59%", "-22.67%", "0.6451"]
    ]
    add_custom_table(headers_cat, data_cat, col_widths=[1.5, 1.2, 1.2, 1.4, 1.2], alignments=[WD_ALIGN_PARAGRAPH.LEFT] + [WD_ALIGN_PARAGRAPH.RIGHT]*4)

    add_h3("Equal-Weighted Synthetic Portfolio Results (979 Common Sessions)")
    headers_port = ["Category Portfolio", "Portfolio CAGR", "Portfolio Volatility", "Portfolio Max DD", "Portfolio Sharpe"]
    data_port = [
        ["Large Cap", "15.29%", "12.85%", "-15.56%", "0.7489"],
        ["Mid Cap", "16.87%", "14.74%", "-19.96%", "0.7658"],
        ["Small Cap", "14.99%", "14.18%", "-22.12%", "0.6726"]
    ]
    add_custom_table(headers_port, data_port, col_widths=[1.5, 1.2, 1.2, 1.4, 1.2], alignments=[WD_ALIGN_PARAGRAPH.LEFT] + [WD_ALIGN_PARAGRAPH.RIGHT]*4)

    add_image_if_exists("Category_Comparison/charts/cagr.png", caption="Category Mean CAGR Comparison", width=Inches(5.0))
    add_image_if_exists("Category_Comparison/charts/sharpe_ratio.png", caption="Category Mean Sharpe Ratio Comparison", width=Inches(5.0))
    add_image_if_exists("Category_Comparison/charts/maximum_drawdown.png", caption="Category Mean Maximum Drawdown Comparison", width=Inches(5.0))

    # =========================================================================
    # 15. BUSINESS INSIGHTS
    # =========================================================================
    add_h1("15. BUSINESS INSIGHTS", page_break=True)
    add_bullet("1. Inversion of the Size Premium: ", "The empirical performance order contradicted textbook expectations: Mid-Cap (16.87%) > Large-Cap (15.27%) > Small-Cap (14.94%). Lower market-cap equities suffered from elevated borrowing costs, liquidity discounts, and late-cycle valuation compressions.")
    add_bullet("2. Mid-Caps Represented the Market Sweet Spot: ", "Mid-cap enterprises achieved optimal balance: established market presence and corporate balance sheets combined with high operational scalability, generating superior alpha (0.766 Sharpe).")
    add_bullet("3. Extreme Active Alpha Dispersion: ", "Manager selection was crucial in Mid-Caps (903 bps spread between HDFC at 22.74% and Axis at 13.71%) and Small-Caps (642 bps spread between Nippon at 18.04% and Kotak at 11.62%). In contrast, Large-Cap funds exhibited tight clustering (spread of 475 bps).")

    # =========================================================================
    # 16. RECOMMENDATIONS
    # =========================================================================
    add_h1("16. RECOMMENDATIONS", page_break=True)
    add_p("Based on empirical findings, the following asset allocation frameworks are recommended:")
    
    headers_rec = ["Investor Risk Profile", "Recommended Allocation", "Tactical Rationale"]
    data_rec = [
        ["Conservative / Capital Preservation", "70% Large Cap | 20% Mid Cap | 10% Small Cap", "Anchored in Large-Cap drawdown resistance (-15.56% MDD) with modest growth kicker."],
        ["Moderate / Balanced Wealth Accumulation", "50% Large Cap | 35% Mid Cap | 15% Small Cap", "Optimizes overall portfolio Sharpe efficiency while maintaining maximum drawdown < -17.5%."],
        ["Aggressive / Long Horizon (>7 Years)", "35% Large Cap | 45% Mid Cap | 20% Small Cap", "Maximizes compounding runway via mid-cap earnings growth, accepting -20% drawdowns."]
    ]
    add_custom_table(headers_rec, data_rec, col_widths=[2.0, 2.0, 2.5])

    add_bullet("Mandate SIPs for Lower-Cap Tiers: ", "Discourage lump-sum deployment in small-cap schemes to mitigate the impact of -25% drawdowns through rupee-cost averaging.")
    add_bullet("Multi-Metric Fund Screening: ", "Screen funds based on multi-factor hurdles (Sharpe > 0.75, MDD > -20%) rather than marketing collateral based purely on 1-year returns.")
    add_bullet("Direct-Growth Plan Execution: ", "Eliminate the 50–150 bps annual TER drag of Regular Plans, preserving 15–25% higher wealth over long investment horizons.")

    # =========================================================================
    # 17. LIMITATIONS
    # =========================================================================
    add_h1("17. LIMITATIONS", page_break=True)
    add_bullet("Observation Cycle Bias (2022–2025): ", "The study took place during an active rate-hiking cycle. In loose liquidity and low-rate environments, small caps historically experience wider outperformance margins.")
    add_bullet("Static Risk-Free Rate Assumption: ", "A constant Rf = 6.00% p.a. was applied, whereas 91-day T-Bill yields fluctuated between 4.5% in early 2022 and 7.2% in 2023.")
    add_bullet("Survivorship of Established Schemes: ", "The sample evaluated 15 large, seasoned schemes and did not capture smaller or newly launched funds.")
    add_bullet("External NAV Scope: ", "Analysis was conducted on external NAV series without factor attribution on underlying stock holdings.")

    # =========================================================================
    # 18. FUTURE SCOPE
    # =========================================================================
    add_h1("18. FUTURE SCOPE", page_break=True)
    add_bullet("Expand Universe to Multi-Cap and Flexi-Cap Funds: ", "Evaluate dynamic asset allocation schemes to test whether active cross-cap mandate switching beats static allocations.")
    add_bullet("Incorporate Asymmetric Downside Ratios: ", "Calculate the Sortino Ratio (downside semi-variance) and Calmar Ratio (CAGR / Maximum Drawdown).")
    add_bullet("Rolling Return and Rolling Sharpe Modeling: ", "Evaluate 1-year and 3-year rolling metrics to test performance persistence across changing market regimes.")
    add_bullet("Machine Learning Holdings Attribution: ", "Decompose historical monthly stock portfolio sheets using Fama-French multi-factor regressions to predict alpha persistence.")

    # =========================================================================
    # 19. REFERENCES
    # =========================================================================
    add_h1("19. REFERENCES", page_break=True)
    refs = [
        "Markowitz, H. (1952). Portfolio Selection. The Journal of Finance, 7(1), 77–91.",
        "Sharpe, W. F. (1964). Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk. The Journal of Finance, 19(3), 425–442.",
        "Sharpe, W. F. (1966). Mutual Fund Performance. The Journal of Business, 39(1), 119–138.",
        "Sharpe, W. F. (1994). The Sharpe Ratio. The Journal of Portfolio Management, 21(1), 49–58.",
        "Fama, E. F., & French, K. R. (1992). The Cross-Section of Expected Stock Returns. The Journal of Finance, 47(2), 427–465.",
        "Fama, E. F., & French, K. R. (1993). Common Risk Factors in the Returns on Stocks and Bonds. Journal of Financial Economics, 33(1), 3–56.",
        "Chekhlov, A., Uryasev, S., & Zabarankin, M. (2005). Drawdown Measure in Portfolio Optimization. International Journal of Theoretical and Applied Finance, 8(01), 13–58.",
        "Sortino, F. A., & van der Meer, R. (1991). Downside Risk. The Journal of Portfolio Management, 17(4), 27–31.",
        "Sehgal, S., & Jhanwar, M. (2008). Short Term Momentum Patterns: Evidence from the Indian Stock Market. Asian Academy of Management Journal of Accounting and Finance, 4(1), 23–46.",
        "Securities and Exchange Board of India (SEBI). (2017). Categorization and Rationalization of Mutual Fund Schemes. Circular No. SEBI/HO/IMD/DF3/CIR/P/2017/114, Mumbai, India.",
        "Association of Mutual Funds in India (AMFI). (2022–2025). Historical Net Asset Value (NAV) Database and Industry Performance Reports. Retrieved from https://www.amfiindia.com.",
        "Reserve Bank of India (RBI). (2022–2025). Database on Indian Economy: Sovereign Treasury Bill Yields and Policy Rates. Retrieved from https://rbi.org.in."
    ]
    for r in refs:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(r)
        run.font.size = Pt(10)
        run.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 20. APPENDIX
    # =========================================================================
    add_h1("20. APPENDIX", page_break=True)
    add_h2("Appendix A: Verified Python Metric Calculation Pipeline")
    
    code_text = (
        "import pandas as pd\n"
        "import numpy as np\n\n"
        "def calculate_fund_metrics(file_path, risk_free_rate=0.06, trading_days=252):\n"
        "    df = pd.read_excel(file_path, header=4)\n"
        "    df.columns = df.columns.astype(str).str.strip()\n"
        "    df = df[['Date', 'Net Asset Value', 'Plan', 'Option']]\n"
        "    df.columns = ['Date', 'NAV', 'Plan', 'Option']\n"
        "    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')\n"
        "    df['NAV'] = pd.to_numeric(df['NAV'], errors='coerce')\n"
        "    df = df[\n"
        "        df['Plan'].astype(str).str.contains('direct', case=False, na=False) &\n"
        "        df['Option'].astype(str).str.contains('growth', case=False, na=False)\n"
        "    ]\n"
        "    df = df[(df['Date'] >= '2022-01-01') & (df['Date'] <= '2025-12-31')]\n"
        "    df = df.dropna(subset=['Date', 'NAV']).sort_values('Date').reset_index(drop=True)\n\n"
        "    df['Daily_Return'] = df['NAV'].pct_change()\n"
        "    years = (df['Date'].iloc[-1] - df['Date'].iloc[0]).days / 365.25\n"
        "    cagr = (df['NAV'].iloc[-1] / df['NAV'].iloc[0]) ** (1 / years) - 1\n"
        "    volatility = df['Daily_Return'].std() * np.sqrt(trading_days)\n\n"
        "    df['Running_Max'] = df['NAV'].cummax()\n"
        "    df['Drawdown'] = (df['NAV'] - df['Running_Max']) / df['Running_Max']\n"
        "    max_drawdown = df['Drawdown'].min()\n\n"
        "    daily_rf = (1 + risk_free_rate) ** (1 / trading_days) - 1\n"
        "    excess_returns = df['Daily_Return'].dropna() - daily_rf\n"
        "    sharpe_ratio = (excess_returns.mean() / df['Daily_Return'].std()) * np.sqrt(trading_days)\n\n"
        "    return {\n"
        "        'CAGR': cagr, 'Volatility': volatility,\n"
        "        'Max_Drawdown': max_drawdown, 'Sharpe_Ratio': sharpe_ratio\n"
        "    }"
    )

    tbl_code = doc.add_table(rows=1, cols=1)
    tbl_code.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_code = tbl_code.cell(0, 0)
    c_code.width = Inches(6.5)
    set_cell_background(c_code, HEX_LIGHT_BG)
    set_cell_margins(c_code, top=120, bottom=120, left=150, right=150)
    p_code = c_code.paragraphs[0]
    p_code.paragraph_format.space_before = Pt(0)
    p_code.paragraph_format.space_after = Pt(0)
    run_code = p_code.add_run(code_text)
    run_code.font.name = 'Consolas'
    run_code.font.size = Pt(8.5)
    run_code.font.color.rgb = COLOR_DARK

    add_h2("Appendix B: Radar Performance Charts")
    add_image_if_exists("Large_cap/analysis/charts/large_cap_radar.png", caption="Large-Cap Funds Performance Radar Chart", width=Inches(4.8))
    add_image_if_exists("Mid_cap/analysis/charts/mid_cap_radar.png", caption="Mid-Cap Funds Performance Radar Chart", width=Inches(4.8))
    add_image_if_exists("Small_cap/analysis/charts/small_cap_radar.png", caption="Small-Cap Funds Performance Radar Chart", width=Inches(4.8))

    doc.save(output_path)
    print(f"Report successfully saved to {output_path}")

if __name__ == "__main__":
    out_file = r"d:\Indi_p\Fintech\Fintech\Mutual_Fund_Comparative_Analysis_Report.docx"
    create_report_docx(out_file)
