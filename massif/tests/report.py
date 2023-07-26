import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf_report(pdf_file_path, report_data):
    # Create a PDF document
    doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)

    # Create a list to store the report content
    elements = []

    # Add a title to the report
    title_style = getSampleStyleSheet()["Title"]
    text_style = getSampleStyleSheet()["BodyText"]
    title_text = "Report Title"
    elements.append(Paragraph(title_text, title_style))
    elements.append(Paragraph("clksndklnclknsldkc slkndcklnsd, sldknclksdnc\n", text_style))
    elements.append(Paragraph("\n", text_style))
    # Add a table with the report data
    data = [
        ["Name", "Age", "Email"],
        ["John Doe", "30", "john@example.com"],
        ["Jane Smith", "25", "jane@example.com"],
        # Add more rows with data from the report_data dictionary
    ]

    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    table = Table(data)
    table.setStyle(table_style)
    times = 3
    for i in range(times): 
      elements.append(table)

    # Add other content to the report as needed

    # Build the PDF document
    doc.build(elements)

if __name__ == "__main__":
  # Example usage
  report_data = {...}  # Your report data goes here
  filename='report.pdf'
  pdf_file_path = os.getcwd() + f'\\{filename}'
  create_pdf_report(pdf_file_path, report_data)
