"""
=========================================================
CareerIQ Enterprise
Enterprise Resume Analytics Engine
Author : Vellanki phanikartheek
Version : 9.0
=========================================================
"""

import pandas as pd
import plotly.express as px


class ResumeAnalytics:

    def __init__(self):
        pass

    # --------------------------------------------------
    # Resume Summary
    # --------------------------------------------------

    def summary(self, features):

        return pd.DataFrame({

            "Metric": [

                "Experience",

                "Projects",

                "Certifications",

                "Resume Words",

                "Resume Score"

            ],

            "Value": [

                features.get("Experience", 0),

                features.get("Projects", 0),

                features.get("Certifications", 0),

                features.get("Resume Words", 0),

                features.get("Resume Quality Score", 0)

            ]

        })

    # --------------------------------------------------
    # Skill Distribution
    # --------------------------------------------------

    def skill_distribution(

        self,

        matched,

        missing

    ):

        return pd.DataFrame({

            "Category": [

                "Matched Skills",

                "Missing Skills"

            ],

            "Count": [

                len(matched),

                len(missing)

            ]

        })

    # --------------------------------------------------
    # Pie Chart
    # --------------------------------------------------

    def pie_chart(

        self,

        matched,

        missing

    ):

        df = self.skill_distribution(

            matched,

            missing

        )

        fig = px.pie(

            df,

            names="Category",

            values="Count",

            hole=0.45,

            title="Skill Distribution"

        )

        return fig

    # --------------------------------------------------
    # Bar Chart
    # --------------------------------------------------

    def bar_chart(

        self,

        matched,

        missing

    ):

        df = self.skill_distribution(

            matched,

            missing

        )

        fig = px.bar(

            df,

            x="Category",

            y="Count",

            text="Count",

            title="Matched vs Missing Skills"

        )

        return fig

    # --------------------------------------------------
    # Experience Level
    # --------------------------------------------------

    def experience_level(

        self,

        years

    ):

        if years <= 1:

            return "Fresher"

        elif years <= 3:

            return "Junior"

        elif years <= 7:

            return "Mid Level"

        elif years <= 12:

            return "Senior"

        else:

            return "Leadership"

    # --------------------------------------------------
    # Resume Strength
    # --------------------------------------------------

    def resume_strength(

        self,

        score

    ):

        if score >= 90:

            return "Excellent"

        elif score >= 75:

            return "Strong"

        elif score >= 60:

            return "Average"

        elif score >= 40:

            return "Weak"

        else:

            return "Very Weak"

    # --------------------------------------------------
    # Candidate Grade
    # --------------------------------------------------

    def grade(

        self,

        score

    ):

        if score >= 95:

            return "A+"

        elif score >= 85:

            return "A"

        elif score >= 75:

            return "B+"

        elif score >= 65:

            return "B"

        else:

            return "C"

    # --------------------------------------------------
    # Skill Gap Risk
    # --------------------------------------------------

    def skill_gap_risk(

        self,

        matched,

        missing

    ):

        total = len(matched) + len(missing)

        if total == 0:

            return "Unknown"

        gap = len(missing) / total

        if gap < 0.20:

            return "Low"

        elif gap < 0.50:

            return "Medium"

        else:

            return "High"

    # --------------------------------------------------
    # Hiring Recommendation
    # --------------------------------------------------

    def hiring_status(

        self,

        score

    ):

        if score >= 95:

            return "🟢 Outstanding Candidate"

        elif score >= 85:

            return "🟢 Highly Recommended"

        elif score >= 75:

            return "🟡 Recommended"

        elif score >= 60:

            return "🟠 Consider After Review"

        else:

            return "🔴 Not Recommended"

    # --------------------------------------------------
    # Dashboard Metrics
    # --------------------------------------------------

    def dashboard_metrics(

        self,

        ats,

        similarity,

        quality

    ):

        overall = round(

            (ats + similarity + quality) / 3,

            2

        )

        return {

            "ATS Score": ats,

            "Similarity": similarity,

            "Resume Quality": quality,

            "Overall Score": overall,

            "Grade": self.grade(overall),

            "Recommendation": self.hiring_status(overall)

        }