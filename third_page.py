from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import matplotlib.pyplot as plt
import numpy as np
import os


guidelines_content = [
    {
        "title": "Understanding the Radar Chart Structure",
        "subcomponents": [
            "Axes Representation: Each axis corresponds to a category of managerial effectiveness.",
            "Data Points: Your average score for each category is plotted along its axis."
        ]
    },
    {
        "title": "Interpreting the Chart",
        "subcomponents": [
            "Outer Edges (Higher Scores): Areas where the shape extends towards the outer edge indicate stronger performance.",
            "Inner Areas (Lower Scores): Areas closer to the center suggest opportunities for improvement."
        ]
    },
    {
        "title": "Balance and Symmetry",
        "subcomponents": [
            "Balanced Shape: A symmetrical shape suggests consistent performance across categories.",
            "Irregular Shape: Asymmetry may highlight specific strengths or development needs."
        ]
    },
    {
        "title": "Identifying Patterns",
        "subcomponents": [
            "Consistent High Scores: Uniformly high scores across axes reflect well-rounded effectiveness.",
            "Variations in Scores: Significant differences between categories can indicate where to focus development efforts."
        ]
    },
    {
        "title": "Acting on Insights from the Radar Chart",
        "subcomponents": [
            "Gain Insight: Understand your performance profile at a glance.",
            "Identify Opportunities: Recognize areas where focused development can enhance your effectiveness.",
            "Take Action: Implement strategies to build on strengths and address development needs.",
            "Track Improvement: Use the radar chart as a tool for ongoing personal and professional growth."
        ]
    }
]

def create_radar_chart(data, categories, output_path):
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))
    ax.fill(angles, data, color='blue', alpha=0.25)
    ax.plot(angles, data, color='blue', linewidth=2)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10)
    plt.savefig(output_path, format='png', bbox_inches='tight')
    plt.close()


def third_page(pdf, avg_ratings, page_width, page_height):
    try:
        categories = list(avg_ratings.keys())
        scores = list(avg_ratings.values())

        radar_chart_path = "radar_chart.png"
        create_radar_chart(scores, categories, radar_chart_path)

        margin = 50
        column_gap = 20
        chart_height = 200
        chart_width = (page_width - 2 * margin - column_gap) * 0.6
        table_width = (page_width - 2 * margin - column_gap) * 0.4
        current_y = page_height - 100
        
        pdf.setFont("Helvetica-Bold", 16)
        title = "Managerial Effectiveness Assessment"
        pdf.drawString(margin, current_y, title)
        current_y -= 40

        pdf.drawImage(radar_chart_path, margin, current_y - chart_height, width=chart_width, height=chart_height)

        table_data = [["Parameter", "Score"]] + [[cat, f"{score:.1f}"] for cat, score in avg_ratings.items()]
        table = Table(table_data, colWidths=[table_width * 0.7, table_width * 0.3])
        table.setStyle(TableStyle([
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 1), 'Helvetica-Bold'),
            ('FONTNAME', (0, 2), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('INNERGRID', (0, 0), (-1, -1), 0, colors.white),
            ('BOX', (0, 0), (-1, -1), 0, colors.white),
        ]))

        table.wrapOn(pdf, page_width, page_height)
        table.drawOn(pdf, margin + chart_width + column_gap, current_y - chart_height + 40)

        current_y -= chart_height + 30
        pdf.setFont("Helvetica-Bold", 18)
        pdf.drawString(margin, current_y, "General Guidelines for Interpreting the Radar Chart")

        current_y -= 35

        styles = getSampleStyleSheet()
        body_style = styles['BodyText']

        for section in guidelines_content:
            title = section["title"]
            subcomponents = section["subcomponents"]

            title_paragraph = Paragraph(f'<b>{title}</b>', styles['Heading2'])
            title_paragraph.fontSize = 12
            title_paragraph.wrapOn(pdf, page_width, page_height)
            title_paragraph.drawOn(pdf, margin, current_y)
            current_y -= 20

            for subcomponent in subcomponents:
                subcomponent_paragraph = Paragraph(f'• {subcomponent}', body_style)
                subcomponent_paragraph.wrapOn(pdf, page_width, page_height)
                subcomponent_paragraph.drawOn(pdf, margin, current_y)
                current_y -= 18

        current_y -= 20

    finally:
        if os.path.exists(radar_chart_path):
            os.remove(radar_chart_path)
