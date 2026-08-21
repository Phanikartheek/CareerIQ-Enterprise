"""
=====================================================
Resume Intelligence AI
Visualization Engine
Version : 5.0
=====================================================
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


class DashboardCharts:

    # ---------------------------------------
    # ATS Gauge
    # ---------------------------------------

    def ats_gauge(self, score):

        fig = go.Figure(

            go.Indicator(

                mode="gauge+number",

                value=score,

                title={"text":"ATS Score"},

                gauge={

                    "axis":{"range":[0,100]},

                    "bar":{"color":"royalblue"},

                    "steps":[

                        {"range":[0,40],"color":"#ffcccc"},

                        {"range":[40,70],"color":"#ffe680"},

                        {"range":[70,100],"color":"#ccffcc"}

                    ]

                }

            )

        )

        fig.update_layout(height=350)

        return fig

    # ---------------------------------------
    # Skill Comparison
    # ---------------------------------------

    def skill_bar(self, matched, missing):

        df = pd.DataFrame({

            "Category":[

                "Matched",

                "Missing"

            ],

            "Count":[

                len(matched),

                len(missing)

            ]

        })

        fig = px.bar(

            df,

            x="Category",

            y="Count",

            text="Count",

            color="Category"

        )

        fig.update_layout(

            title="Matched vs Missing Skills",

            height=400

        )

        return fig

    # ---------------------------------------
    # Resume Quality Radar
    # ---------------------------------------

    def radar_chart(self, features):

        categories=[

            "Experience",

            "Projects",

            "Certifications",

            "Resume Words",

            "Quality"

        ]

        values=[

            min(features["Experience"]*10,100),

            min(features["Projects"]*15,100),

            min(features["Certifications"]*20,100),

            min(features["Resume Words"]/8,100),

            features["Resume Quality Score"]

        ]

        fig=go.Figure()

        fig.add_trace(

            go.Scatterpolar(

                r=values,

                theta=categories,

                fill='toself',

                name="Resume"

            )

        )

        fig.update_layout(

            polar=dict(

                radialaxis=dict(

                    visible=True,

                    range=[0,100]

                )

            ),

            showlegend=False,

            height=450

        )

        return fig

    # ---------------------------------------
    # Pie Chart
    # ---------------------------------------

    def pie_chart(self, matched, missing):

        fig = px.pie(

            names=["Matched","Missing"],

            values=[

                len(matched),

                len(missing)

            ],

            hole=0.45

        )

        fig.update_layout(height=400)

        return fig

    # ---------------------------------------
    # Resume KPI
    # ---------------------------------------

    def kpi_cards(

            self,

            ats,

            similarity,

            quality,

            experience

    ):

        return {

            "ATS":ats,

            "Similarity":similarity,

            "Quality":quality,

            "Experience":experience

        }