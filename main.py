from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import json
from Front_page import create_front_page
from last_page import create_last_page
from third_page import third_page
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

with open('question.json', 'r') as q_file:
    questions_data = json.load(q_file)

with open('rating.json', 'r') as r_file:
    ratings_data = json.load(r_file)

questions = questions_data.get("Questions", {})
ratings = ratings_data.get("Rating", {})
surveyDetails = ratings_data.get("SurveyDetails", {})
participantDetails = ratings_data.get("ParticipantDetails", {})
avgRatings = {key: sum(values) / len(values) for key, values in ratings.items()}

def draw_line(pdf, x_start, y_start, width):
    pdf.line(x_start, y_start, x_start + width, y_start)

def create_middle_pages(pdf, questions, ratings, page_width, page_height, page_number):
    margin = 50
    count=0
    category_spacing = 30
    current_y = page_height - 80

    for category in questions:
        if current_y < 100:
            add_header(pdf, "Managerial Effectiveness Report")
            add_footer(pdf, page_number)
            pdf.showPage()
            current_y = page_height - 80
            page_number += 1

        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(margin, current_y, f"Category: {category}")
        current_y -= 20
        draw_line(pdf, margin, current_y, page_width - 2 * margin)
        current_y -= 20

        pdf.setFont("Helvetica", 12)
        category_questions = questions.get(category, [])
        category_ratings = ratings.get(category, [])

        table_data = []
        for idx, question in enumerate(category_questions):
            rating = category_ratings[idx] if idx < len(category_ratings) else "N/A"
            table_data.append([f"{idx + 1}. {question[0:65]}", f"{rating}"])

        table = Table(table_data, colWidths=[400, 100], rowHeights=20)
        table.setStyle(TableStyle([ 
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ]))
        
        table.wrapOn(pdf, page_width, page_height)
        table.drawOn(pdf, margin, current_y - len(table_data) * 20)

        current_y -= len(table_data) * 20
        current_y -= category_spacing

    return page_number

def add_header(pdf, header_text=""):
    logo_path = "logo.png"
    pdf.setFont("Helvetica-Bold", 10)
    pdf.setFillColor(colors.grey)
    pdf.drawString(50, 750, header_text)
    pdf.drawImage(logo_path, 400, 720, width=100, height=75, mask='auto')

def add_footer(pdf, page_number):
    footer_text = f"Page {page_number}"
    pdf.setFont("Helvetica", 10)
    pdf.setFillColor(colors.grey)
    pdf.drawString(500, 30, footer_text)

def generate_pdf(output_filename, questions, ratings):
    pdf = canvas.Canvas(output_filename, pagesize=letter)
    page_width, page_height = letter
    page_num = 1
    create_front_page(pdf, page_width, page_height, participantDetails, surveyDetails)
    add_footer(pdf, page_num)
    page_num += 1
    pdf.showPage()
    add_header(pdf, "Managerial Effectiveness Report")
    third_page(pdf, avgRatings, page_width, page_height)
    add_footer(pdf, page_num)
    page_num += 1
    pdf.showPage()

    page_num = create_middle_pages(pdf, questions, ratings, page_width, page_height, page_num)
    add_header(pdf, "Managerial Effectiveness Report")
    add_footer(pdf, page_num)
    pdf.showPage()
    page_num+=1
    add_header(pdf, "Managerial Effectiveness Report")
    create_last_page(pdf, page_height)
    add_footer(pdf, page_num)
    pdf.showPage()
    pdf.save()
    print(f"PDF report generated: {output_filename}")

output_file = "Managerial_Effectiveness_Report.pdf"
generate_pdf(output_file, questions, ratings)
