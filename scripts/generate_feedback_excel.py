import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def generate_excel():
    os.makedirs("docs", exist_ok=True)
    wb = openpyxl.Workbook()
    
    # Setup Sheet 1: User Feedback Database
    ws1 = wb.active
    ws1.title = "User Feedback & Mapping"
    ws1.views.sheetView[0].showGridLines = True

    # Styling Palettes
    header_fill = PatternFill(start_color="0B192C", end_color="0B192C", fill_type="solid") # Dark Navy
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    
    section_fill = PatternFill(start_color="1E3E62", end_color="1E3E62", fill_type="solid")
    section_font = Font(name="Calibri", size=12, bold=True, color="FFD700")

    summary_head_fill = PatternFill(start_color="000000", end_color="000000", fill_type="solid")
    summary_head_font = Font(name="Calibri", size=11, bold=True, color="00FFCC")

    thin_border = Border(
        left=Side(style='thin', color='D3D3D3'),
        right=Side(style='thin', color='D3D3D3'),
        top=Side(style='thin', color='D3D3D3'),
        bottom=Side(style='thin', color='D3D3D3')
    )

    # Title block
    ws1.merge_cells("A1:N1")
    title_cell = ws1["A1"]
    title_cell.value = "GASCHAIN — STELLAR LEVEL 5 USER ONBOARDING & FEEDBACK DATABASE (SEPTEMBER 2026)"
    title_cell.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    title_cell.fill = section_fill
    title_cell.alignment = Alignment(horizontal="center", vertical="center")
    ws1.row_dimensions[1].height = 32

    # Column Headers
    headers = [
        "User ID",
        "Name",
        "Email",
        "Wallet Address",
        "Onboarding Date",
        "Feature Used",
        "Transaction Hash",
        "Product Rating",
        "Feedback Summary",
        "Problem Identified",
        "Improvement Made",
        "Git Commit ID",
        "Git Commit Link",
        "Improvement Date"
    ]

    for col_num, header in enumerate(headers, 1):
        cell = ws1.cell(row=2, column=col_num)
        cell.value = header
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border
    ws1.row_dimensions[2].height = 28

    # We provide a clean template with instructions and verified schema.
    # Note: As per Zero Fabrication rules, real data rows from Google Form will be populated by the user.
    # We include formatted empty rows with formulas and styling ready for 50+ users.
    for r in range(3, 53):
        user_num = r - 2
        ws1.cell(row=r, column=1, value=f"USR-{user_num:03d}").alignment = Alignment(horizontal="center")
        for col_num in range(1, 15):
            cell = ws1.cell(row=r, column=col_num)
            cell.border = thin_border
            if col_num in [1, 5, 8, 12, 14]:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            elif col_num in [4, 7]:
                cell.alignment = Alignment(horizontal="left", vertical="center")
                cell.font = Font(name="Consolas", size=9)
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center")

    # Sheet 2: Executive Summary & Metrics
    ws2 = wb.create_sheet(title="Executive Summary & KPIs")
    ws2.views.sheetView[0].showGridLines = True

    ws2.merge_cells("A1:F1")
    s_title = ws2["A1"]
    s_title.value = "GASCHAIN USER FEEDBACK & PRODUCT ITERATION KPI DASHBOARD"
    s_title.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    s_title.fill = section_fill
    s_title.alignment = Alignment(horizontal="center", vertical="center")
    ws2.row_dimensions[1].height = 30

    # Summary Metrics Table
    kpis = [
        ("Total Onboarded Users", '=COUNTA(\'User Feedback & Mapping\'!B3:B52)', "Minimum 50 required for Level 5"),
        ("Average Product Rating (1-5)", '=AVERAGE(\'User Feedback & Mapping\'!H3:H52)', "Target: >= 4.0 / 5.0"),
        ("5-Star Ratings Count", '=COUNTIF(\'User Feedback & Mapping\'!H3:H52, 5)', "Outstanding satisfaction"),
        ("4-Star Ratings Count", '=COUNTIF(\'User Feedback & Mapping\'!H3:H52, 4)', "Good satisfaction"),
        ("3-Star Ratings Count", '=COUNTIF(\'User Feedback & Mapping\'!H3:H52, 3)', "Neutral satisfaction"),
        ("2-Star Ratings Count", '=COUNTIF(\'User Feedback & Mapping\'!H3:H52, 2)', "Action required"),
        ("1-Star Ratings Count", '=COUNTIF(\'User Feedback & Mapping\'!H3:H52, 1)', "Critical action required"),
        ("Completed Feedback Improvements", '=COUNTA(\'User Feedback & Mapping\'!K3:K52)', "Mapped to Git commits"),
        ("Pending Improvements", '=COUNTA(\'User Feedback & Mapping\'!B3:B52) - COUNTA(\'User Feedback & Mapping\'!K3:K52)', "In backlog roadmap"),
    ]

    ws2.cell(row=3, column=1, value="Metric").font = summary_head_font
    ws2.cell(row=3, column=1).fill = summary_head_fill
    ws2.cell(row=3, column=2, value="Current Value").font = summary_head_font
    ws2.cell(row=3, column=2).fill = summary_head_fill
    ws2.cell(row=3, column=3, value="Notes & Benchmarks").font = summary_head_font
    ws2.cell(row=3, column=3).fill = summary_head_fill

    for i, (metric, formula, note) in enumerate(kpis, 4):
        c1 = ws2.cell(row=i, column=1, value=metric)
        c2 = ws2.cell(row=i, column=2, value=formula)
        c3 = ws2.cell(row=i, column=3, value=note)
        c1.font = Font(name="Calibri", size=11, bold=True)
        c2.font = Font(name="Calibri", size=11, bold=True, color="00008B")
        c2.alignment = Alignment(horizontal="center")
        c3.font = Font(name="Calibri", size=10, italic=True, color="555555")
        c1.border = thin_border
        c2.border = thin_border
        c3.border = thin_border

    # Adjust column widths for Sheet 1
    col_widths = {
        "A": 12, "B": 22, "C": 26, "D": 58, "E": 16,
        "F": 22, "G": 58, "H": 15, "I": 35, "J": 30,
        "K": 35, "L": 18, "M": 45, "N": 16
    }
    for col, width in col_widths.items():
        ws1.column_dimensions[col].width = width

    ws2.column_dimensions["A"].width = 35
    ws2.column_dimensions["B"].width = 20
    ws2.column_dimensions["C"].width = 40

    out_file = os.path.join("docs", "user-feedback.xlsx")
    wb.save(out_file)
    print(f"Feedback Excel template generated at {out_file}")

if __name__ == "__main__":
    generate_excel()
