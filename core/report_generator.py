"""
=========================================================
Resume Intelligence AI
Professional PDF Report Generator
Version : 9.0 Enterprise
Author : Vellanki phanikartheek
=========================================================
"""

import os
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib.units import inch


class ReportGenerator:

    def __init__(self):

        self.styles = getSampleStyleSheet()

        os.makedirs("reports", exist_ok=True)

    # --------------------------------------------------
    # Generate PDF Report
    # --------------------------------------------------

    def generate_report(

        self,

        candidate_name,

        department,

        job_role,

        ats_score,

        matched_skills,

        missing_skills,

        ml_score,

        dl_score,

        recommendation,

        statistics

    ):

        filename = os.path.join(

            "reports",

            f"{candidate_name.replace(' ','_')}_Report.pdf"

        )

        pdf = SimpleDocTemplate(

            filename,

            rightMargin=40,

            leftMargin=40,

            topMargin=40,

            bottomMargin=40

        )

        elements = []

        # --------------------------------------------------
        # Title
        # --------------------------------------------------

        title_style = self.styles["Title"]

        title_style.alignment = TA_CENTER

        title = Paragraph(

            "<font size=24><b>CareerIQ Enterprise</b></font>",

            title_style

        )

        elements.append(title)

        elements.append(Spacer(1, 0.15 * inch))

        subtitle = Paragraph(

            "<b>Enterprise Resume Intelligence Report</b>",

            self.styles["Heading2"]

        )

        elements.append(subtitle)

        elements.append(Spacer(1, 0.25 * inch))

        # --------------------------------------------------
        # Candidate Information
        # --------------------------------------------------

        info = [

            ["Candidate Name", candidate_name],

            ["Department", department],

            ["Target Role", job_role],

            [

                "Generated On",

                datetime.now().strftime("%d-%m-%Y %I:%M %p")

            ]

        ]

        info_table = Table(

            info,

            colWidths=[2.2 * inch, 4.2 * inch]

        )

        info_table.setStyle(

            TableStyle([

                ("GRID", (0,0), (-1,-1), 0.5, colors.grey),

                ("BACKGROUND", (0,0), (0,-1), colors.HexColor("#E8F1FD")),

                ("FONTNAME", (0,0), (-1,-1), "Helvetica"),

                ("BOTTOMPADDING", (0,0), (-1,-1), 8),

                ("TOPPADDING", (0,0), (-1,-1), 8)

            ])

        )

        elements.append(info_table)

        elements.append(Spacer(1, 0.30 * inch))

        # --------------------------------------------------
        # Resume Statistics
        # --------------------------------------------------

        elements.append(

            Paragraph(

                "<b>Resume Statistics</b>",

                self.styles["Heading2"]

            )

        )

        stats_table = Table([

            [

                "Words",

                statistics.get("Words", 0)

            ],

            [

                "Characters",

                statistics.get("Characters", 0)

            ],

            [

                "Sentences",

                statistics.get("Sentences", 0)

            ],

            [

                "Lines",

                statistics.get("Lines", 0)

            ]

        ])

        stats_table.setStyle(

            TableStyle([

                ("GRID", (0,0), (-1,-1), 0.5, colors.grey),

                ("BACKGROUND", (0,0), (0,-1), colors.beige),

                ("BOTTOMPADDING", (0,0), (-1,-1), 6)

            ])

        )

        elements.append(stats_table)

        elements.append(Spacer(1, 0.30 * inch))

        # --------------------------------------------------
        # AI Scores
        # --------------------------------------------------

        elements.append(

            Paragraph(

                "<b>AI Evaluation Scores</b>",

                self.styles["Heading2"]

            )

        )

        score_table = Table([

            ["ATS Score", f"{ats_score}%"],

            ["Machine Learning", f"{ml_score}%"],

            ["Deep Learning", f"{dl_score}%"]

        ])

        score_table.setStyle(

            TableStyle([

                ("GRID", (0,0), (-1,-1), 0.5, colors.black),

                ("BACKGROUND", (0,0), (0,-1), colors.lightgrey),

                ("BOTTOMPADDING", (0,0), (-1,-1), 7)

            ])

        )

        elements.append(score_table)

        elements.append(Spacer(1, 0.30 * inch))
        # --------------------------------------------------
        # Skills Summary
        # --------------------------------------------------

        elements.append(

            Paragraph(

                "<b>Skills Analysis</b>",

                self.styles["Heading2"]

            )

        )

        matched_text = (

            ", ".join(matched_skills)

            if matched_skills

            else "No matched skills found."

        )

        missing_text = (

            ", ".join(missing_skills)

            if missing_skills

            else "No missing skills."

        )

        skills_table = Table([

            ["Matched Skills", matched_text],

            ["Missing Skills", missing_text]

        ], colWidths=[2.0 * inch, 4.4 * inch])

        skills_table.setStyle(

            TableStyle([

                ("GRID", (0,0), (-1,-1), 0.5, colors.grey),

                ("BACKGROUND", (0,0), (0,-1), colors.HexColor("#E8F5E9")),

                ("BOTTOMPADDING", (0,0), (-1,-1), 8),

                ("TOPPADDING", (0,0), (-1,-1), 8),

                ("VALIGN", (0,0), (-1,-1), "TOP")

            ])

        )

        elements.append(skills_table)

        elements.append(Spacer(1, 0.30 * inch))

        # --------------------------------------------------
        # Overall AI Decision
        # --------------------------------------------------

        final_score = round(

            (ats_score + ml_score + dl_score) / 3,

            2

        )

        if final_score >= 95:

            grade = "A+"

            decision = "🟢 Outstanding Candidate"

        elif final_score >= 85:

            grade = "A"

            decision = "🟢 Highly Recommended"

        elif final_score >= 75:

            grade = "B+"

            decision = "🟡 Recommended"

        elif final_score >= 60:

            grade = "B"

            decision = "🟠 Consider After Review"

        else:

            grade = "C"

            decision = "🔴 Not Recommended"

        decision_table = Table([

            ["Overall Score", f"{final_score}%"],

            ["Grade", grade],

            ["Hiring Decision", decision]

        ])

        decision_table.setStyle(

            TableStyle([

                ("GRID", (0,0), (-1,-1), 0.5, colors.black),

                ("BACKGROUND", (0,0), (0,-1), colors.HexColor("#FFF3CD")),

                ("BOTTOMPADDING", (0,0), (-1,-1), 8)

            ])

        )

        elements.append(

            Paragraph(

                "<b>Overall Assessment</b>",

                self.styles["Heading2"]

            )

        )

        elements.append(decision_table)

        elements.append(Spacer(1, 0.30 * inch))

        # --------------------------------------------------
        # AI Recommendation
        # --------------------------------------------------

        elements.append(

            Paragraph(

                "<b>AI Recommendation</b>",

                self.styles["Heading2"]

            )

        )

        elements.append(

            Paragraph(

                recommendation.replace("\n", "<br/>"),

                self.styles["BodyText"]

            )

        )

        elements.append(Spacer(1, 0.35 * inch))

        # --------------------------------------------------
        # Footer
        # --------------------------------------------------

        footer = Paragraph(

            """
            <font size=10 color='grey'>
            Generated by <b>CareerIQ Enterprise</b><br/>
            Enterprise Resume Intelligence Platform<br/><br/>
            Author : Vellanki phanikartheek<br/>
            © 2026 All Rights Reserved
            </font>
            """,

            self.styles["BodyText"]

        )

        elements.append(footer)

        # --------------------------------------------------
        # Build PDF
        # --------------------------------------------------

        pdf.build(elements)

        return filename