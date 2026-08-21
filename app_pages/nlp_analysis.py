"""
=========================================================
CareerIQ Enterprise
Enterprise NLP Resume Similarity Analysis
Version : 11.0 Enterprise
Author : Vellanki phanikartheek
=========================================================
"""

import streamlit as st

from core.similarity_engine import SimilarityEngine
from core.hiring_score import HiringScoreEngine


def nlp_analysis_page():

    st.title("🧠 Enterprise NLP Resume Similarity")

    st.markdown(
        """
Compare a Resume with a Job Description using
TF-IDF, Cosine Similarity and Enterprise Hiring Intelligence.
"""
    )

    st.divider()

    resume = st.text_area(

        "📄 Resume Text",

        height=250,

        placeholder="Paste Resume Text Here..."

    )

    job = st.text_area(

        "💼 Job Description",

        height=250,

        placeholder="Paste Job Description Here..."

    )

    st.divider()

    if st.button(

        "🚀 Analyze Resume",

        use_container_width=True

    ):

        if resume.strip() == "" or job.strip() == "":

            st.warning(

                "Please provide both Resume and Job Description."

            )

            return

        similarity_engine = SimilarityEngine()

        hiring = HiringScoreEngine()

        with st.spinner(

            "Running Enterprise NLP Analysis..."

        ):

            report = similarity_engine.analyze(

                resume,

                job

            )

        similarity = report["Similarity Score"]
        overall   = report["Overall Match"]
        skill_cov = report["Skill Coverage"]
        keyword   = report["Keyword Match"]

        hiring_report = hiring.report(

            ats=overall,

            similarity=similarity,

            ml=overall,

            dl=overall,

            technical=skill_cov,

            soft_skills=80,

            experience=60

        )

        st.success(

            "Enterprise NLP Analysis Completed Successfully."

        )

        st.divider()
        # =====================================================
        # Enterprise Dashboard
        # =====================================================

        st.subheader("📊 Enterprise Similarity Dashboard")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(

            "Similarity Score",

            f"{similarity}%"

        )

        c2.metric(

            "Hiring Score",

            f'{hiring_report["Hiring Score"]}%'

        )

        c3.metric(

            "Grade",

            hiring_report["Grade"]

        )

        c4.metric(

            "Hiring Probability",

            f'{hiring_report["Hiring Probability"]}%'

        )

        st.progress(

            hiring_report["Hiring Score"] / 100

        )

        st.divider()

        # =====================================================
        # Similarity Summary
        # =====================================================

        st.subheader("📈 Similarity Summary")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(

                "Resume Similarity",

                f"{similarity}%"

            )

            st.success(

                report["Grade"]

            )

        with col2:

            st.metric(

                "Risk Level",

                hiring_report["Risk"]

            )

            st.info(

                report["Recommendation"]

            )

        st.divider()

        # =====================================================
        # Recruiter Recommendation
        # =====================================================

        st.subheader("🎯 Recruiter Recommendation")

        st.success(

            hiring_report["Recommendation"]

        )

        st.warning(

            f'Risk Level : {hiring_report["Risk"]}'

        )

        st.info(

            f'Hiring Probability : {hiring_report["Hiring Probability"]}%'

        )

        st.divider()
        # =====================================================
        # Detailed Analysis
        # =====================================================

        st.subheader("📄 Detailed Similarity Analysis")

        st.json(report)

        st.divider()

        # =====================================================
        # Skill Analysis
        # =====================================================

        st.subheader("🛠 Skill Analysis")

        col1, col2 = st.columns(2)

        with col1:

            st.write("### ✅ Matched Skills")

            matched = report.get("Matched Skills", [])

            if matched:

                for skill in matched:

                    st.success(skill)

            else:

                st.info("No matched skills found.")

        with col2:

            st.write("### ❌ Missing Skills")

            missing = report.get("Missing Skills", [])

            if missing:

                for skill in missing:

                    st.error(skill)

            else:

                st.success("No missing skills.")

        st.divider()

        # =====================================================
        # AI Interpretation
        # =====================================================

        st.subheader("🤖 AI Interpretation")

        if overall >= 85:

            st.success(
                """
Excellent match.

Your resume is highly aligned with the Job Description.

Recruiters are likely to shortlist this profile.
"""
            )

        elif overall >= 75:

            st.success(
                """
Strong match.

Only minor improvements are required before applying.
"""
            )

        elif overall >= 60:

            st.warning(
                """
Good match.

Your skills align well. Add more JD-specific keywords to improve ATS score.
"""
            )

        elif overall >= 45:

            st.warning(
                """
Moderate match.

Improve missing keywords and technical skills to increase ATS performance.
"""
            )

        else:

            st.error(
                """
Low match.

Your resume needs additional optimization and relevant skills.
"""
            )

        st.divider()

        # =====================================================
        # Technology Stack
        # =====================================================

        st.subheader("⚙ Technology Used")

        st.dataframe(

            {

                "Component": [

                    "Vectorization",

                    "Similarity Metric",

                    "NLP Library",

                    "Enterprise Engine",

                    "Hiring Intelligence"

                ],

                "Technology": [

                    "TF-IDF",

                    "Cosine Similarity",

                    "Scikit-Learn",

                    "Similarity Engine v11",

                    "HiringScore Engine"

                ]

            },

            hide_index=True,

            use_container_width=True

        )

        st.divider()

        # =====================================================
        # Enterprise JSON Report
        # =====================================================

        st.subheader("📑 Enterprise Report")

        st.json({

            "Similarity Report": report,

            "Hiring Report": hiring_report

        })

        st.divider()

        st.caption(

            "CareerIQ Enterprise Enterprise Resume Intelligence Platform • Version 11.0"

        )