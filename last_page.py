from utilis import  wrap_and_draw_text


def create_last_page(pdf,page_height):
    margin = 50
    pdf.setFont("Helvetica-Bold", 32)
    pdf.setFillColorRGB(0.54, 0.17, 0.89)
    pdf.drawString(margin, page_height - 100, "Conclusion")
    pdf.setFillColorRGB(0, 0, 0)
    pdf.setFont("Helvetica", 12)

    y_position = page_height - 150

    regular_paragraphs = [
        "The self-assessment survey serves as a valuable tool for reflecting on your managerial practices "
        "across key competencies essential for effective leadership. The insights gained highlight both your "
        "strengths and potential areas for development. Recognizing these aspects is a crucial step towards "
        "personal and professional growth.",

        "Your commitment to excellence is evident in the areas where you have demonstrated strong "
        "performance. These strengths contribute significantly to your team's success and the overall "
        "objectives of the organization. By continuing to build on these foundations, you set a positive "
        "example and foster a productive work environment.",

        "Simultaneously, the survey has identified opportunities for improvement. Embracing these areas as "
        "avenues for development will not only enhance your effectiveness as a manager but also contribute "
        "to your team's growth and the organization's success.",

        "Embracing the insights from your self-assessment is a proactive step towards enhancing your "
        "leadership capabilities. By focusing on both your strengths and areas for development, you position "
        "yourself to make a significant positive impact on your team and organization.",

        "Remember, effective leadership is an ongoing journey that involves continuous reflection, learning, "
        "and adaptation. Your commitment to personal growth not only benefits you but also sets a powerful "
        "example for those around you."
    ]

    for paragraph in regular_paragraphs:
        wrap_and_draw_text(
            text=paragraph,
            max_line_length=480,
            pdf=pdf,
            x=margin,
            y=y_position,
            font="Helvetica",
            font_size=12,
            line_height=14
        )
        y_position -= 30 + 14 * (len(paragraph) // 90)  

    # Bold paragraphs
    pdf.setFont("Helvetica-Bold", 12)
    bold_paragraphs = [
        "Thank you, for your dedication to continuous improvement and excellence in leadership. "
        "Your proactive approach to personal development sets a strong example for your team and "
        "contributes significantly to the success of the organization.",

        "For any further assistance or to discuss this report in detail, please feel free to reach out "
        "to the Gurukul Program Team."
    ]

    for paragraph in bold_paragraphs:
        wrap_and_draw_text(
            text=paragraph,
            max_line_length=480,
            pdf=pdf,
            x=margin,
            y=y_position,
            font="Helvetica-Bold",
            font_size=12,
            line_height=14
        )
        y_position -= 30 + 14 * (len(paragraph) // 90)