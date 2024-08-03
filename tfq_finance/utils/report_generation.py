from fpdf import FPDF

def generate_report(title, content, filename):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=title, ln=True, align='C')

    pdf.set_font("Arial", size=10)
    for line in content.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True, align='L')

    pdf.output(filename)

if __name__ == "__main__":
    title = "Monthly Report"
    content = """
    This is the monthly report of the company's performance.
    It includes various metrics and analysis of the financial health.
    """
    filename = "monthly_report.pdf"

    generate_report(title, content, filename)
    print("Report generated successfully!")