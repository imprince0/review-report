from reportlab.lib import colors
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import Table, TableStyle
from utilis import wrap_and_draw_text

def create_front_page(pdf, page_width, page_height, participantDetails, surveyDetails):
    margin = 50
    logo_path = "logo.png"  
    logo_width = 200
    logo_height = 150
    pdf.drawImage(logo_path, margin-30, page_height - 150, width=logo_width, height=logo_height, mask='auto')

    pdf.setFillColor(HexColor("#A020F0")) 
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawCentredString(page_width / 2, page_height - 120, "Gurukul Manager Effectiveness Certification Program")

    pdf.setFont("Helvetica-Bold", 14)
    pdf.setFillColor(HexColor("#000000")) 
    pdf.drawString(margin, page_height - 200, "Individual Self-Assessment Report")

    pdf.setFillColor(HexColor("#A020F0")) 
    bg_height = 120 
    pdf.rect(margin, page_height - 360, page_width - 2 * margin, bg_height, fill=True, stroke=False)
    
    pdf.setFillColor(HexColor("#FFFFFF")) 
    pdf.setFont("Helvetica-Bold", 12)
    
    text_y_start = page_height - 240
    line_spacing = 20
    pdf.drawString(margin + 10, text_y_start, f"Name: {participantDetails['Name']}")
    pdf.drawString(margin + 10, text_y_start - line_spacing, f"Title: {participantDetails['Title']}")
    pdf.drawString(margin + 10, text_y_start - 2 * line_spacing, f"Job Level: {participantDetails['JobLevel']}")
    pdf.drawString(margin + 10, text_y_start - 3 * line_spacing, f"Manager Name: {participantDetails['ManagerName']}")
    pdf.drawString(margin + 10, text_y_start - 4 * line_spacing, f"Tower Director: {participantDetails['TowerDirector']}")
    pdf.drawString(margin + 10, text_y_start - 5 * line_spacing, f"Stream: {participantDetails['Stream']}")

    bg_height = 360 
    pdf.setFillColor(HexColor("#003366")) 
    pdf.rect(margin, page_height - 720, page_width - 2 * margin, bg_height, fill=True, stroke=False)

    pdf.setFillColor(white) 
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(margin + 10, page_height - 380, "Survey Overview")
    pdf.setFont("Helvetica", 11)
    welcome_text = "Welcome to your personalized self-assessment report for the Gurukul Manager Effectiveness Certification Program. This survey is designed to provide insights into your managerial practices across key competencies essential for effective leadership."
    wrap_and_draw_text(welcome_text, max_line_length=500, pdf=pdf, x=margin + 10, y=page_height - 400, font="Helvetica", font_size=11, line_height=14)

    pdf.setFillColor(white) 
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(margin + 10, page_height - 480, "Survey Structure")
    pdf.setFont("Helvetica", 11)
    pdf.drawString(margin + 10, page_height - 500, f"Total Questions: {surveyDetails['TotalQuestions']}")
    pdf.drawString(margin + 10, page_height - 515, f"Areas assessed: {len(surveyDetails['AreasAssessed'])}")

    areas_text = " ,   ".join(surveyDetails['AreasAssessed'])
    wrap_and_draw_text(areas_text, max_line_length=500, pdf=pdf, x=margin + 10, y=page_height - 530)

    pdf.setFillColor(white)  
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(margin + 10, page_height - 580, "Rating Scale for Manager Effectiveness")
    data = [
        ["Scale", "Rating"],  
        ["Strongly Agree", "10 or 9"],
        ["Agree", "8 or 7"],
        ["Neutral", "6 or 5"],
        ["Disagree", "4 or 3"],
        ["Strongly Disagree", "2 or 1"],
    ]

    table = Table(data, colWidths=[200, 100])

    style = TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, -1), white),  
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'), 
        ('FONTSIZE', (0, 0), (-1, -1), 11), 
        ('TEXTCOLOR', (0, 0), (-1, 0), white),  
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),  
    ])
    table.setStyle(style)

    table.wrapOn(pdf, page_width, page_height)
    table.drawOn(pdf, margin+10, page_height - 700)