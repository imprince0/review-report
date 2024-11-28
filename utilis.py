from reportlab.lib import colors
from reportlab.lib.pagesizes import letter


def wrap_and_draw_text(text, max_line_length, pdf, x, y, font="Helvetica", font_size=11, line_height=14):
    wrapped_lines = []
    current_line = ""
    words = text.split(" ")
    for word in words:
        test_line = current_line + " " + word if current_line else word
        text_width = pdf.stringWidth(test_line, font, font_size)

        if text_width <= max_line_length:
            current_line = test_line 
        else:
            if current_line: 
                wrapped_lines.append(current_line)
            current_line = word 

    if current_line:  
        wrapped_lines.append(current_line)

    # Draw each line of wrapped text
    for line in wrapped_lines:
        pdf.drawString(x, y, line)
        y -= line_height

    return len(wrapped_lines)  # Return the number of lines drawn


def add_header(pdf, header_text=""):
    logo_path="logo.png"
    pdf.setFont("Helvetica-Bold", 10)
    pdf.setFillColor(colors.grey)
    pdf.drawString(50, 750, header_text)
    pdf.drawImage(logo_path, 400, 720, width=100, height=75, mask='auto')  



def add_footer(pdf, page_number):
    footer_text = f"page {page_number}"
    pdf.setFont("Helvetica", 10)
    pdf.setFillColor(colors.grey)
    pdf.drawString(500, 30, footer_text)