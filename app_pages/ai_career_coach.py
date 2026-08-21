"""
=========================================================
CareerIQ Enterprise
Enterprise AI Career Coach
Version : 11.0 Enterprise
Author : Vellanki phanikartheek
=========================================================
"""

import streamlit as st

from core.ai_engine import AIEngine
from core.hiring_score import HiringScoreEngine


def ai_career_coach_page():

    st.title("💬 Enterprise AI Career Coach")

    st.markdown(
        """
Get AI-powered resume feedback, recruiter insights,
career recommendations and hiring probability.
"""
    )

    engine = AIEngine()

    hiring = HiringScoreEngine()

    st.divider()

    # =====================================================
    # Resume Metrics
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        ats = st.slider(

            "ATS Score",

            0,

            100,

            75

        )

        similarity = st.slider(

            "Job Similarity",

            0,

            100,

            72

        )

    with col2:

        quality = st.slider(

            "Resume Quality",

            0,

            100,

            80

        )

        experience = st.slider(

            "Experience (Years)",

            0,

            20,

            3

        )

    st.divider()

    # =====================================================
    # Skills
    # =====================================================

    matched = st.text_input(

        "Matched Skills",

        "Python, SQL, Machine Learning"

    )

    missing = st.text_input(

        "Missing Skills",

        "AWS, Docker"

    )

    st.divider()

    # =====================================================
    # Generate AI Review
    # =====================================================

    if st.button(

        "🚀 Generate AI Review",

        use_container_width=True

    ):

        coach = engine.llm

        matched_skills = [

            x.strip()

            for x in matched.split(",")

            if x.strip()

        ]

        missing_skills = [

            x.strip()

            for x in missing.split(",")

            if x.strip()

        ]

        with st.spinner(

            "Generating Enterprise AI Report..."

        ):

            report = coach.generate(

                ats=ats,

                similarity=similarity,

                quality=quality,

                experience=experience,

                matched=matched_skills,

                missing=missing_skills

            )

        hiring_report = hiring.report(

            ats=ats,

            similarity=similarity,

            ml=quality,

            dl=quality,

            technical=quality,

            soft_skills=80,

            experience=min(

                experience * 10,

                100

            )

        )

        st.success(

            "Enterprise AI Report Generated Successfully!"

        )

        st.divider()
        # =====================================================
        # Hiring Summary
        # =====================================================

        st.subheader("📊 Enterprise Hiring Summary")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Hiring Score",
            f'{hiring_report["Hiring Score"]}%'
        )

        c2.metric(
            "Grade",
            hiring_report["Grade"]
        )

        c3.metric(
            "Risk",
            hiring_report["Risk"]
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
        # Executive Summary
        # =====================================================

        st.subheader("📝 Executive Summary")

        st.info(
            report["Executive Summary"]
        )

        st.divider()

        # =====================================================
        # AI Review
        # =====================================================

        st.subheader("🤖 AI Resume Review")

        for item in report["AI Review"]:

            st.success(item)

        st.divider()

        # =====================================================
        # Strengths
        # =====================================================

        st.subheader("💪 Candidate Strengths")

        for item in report["Strengths"]:

            st.write(f"✅ {item}")

        st.divider()

        # =====================================================
        # Weaknesses
        # =====================================================

        st.subheader("⚠ Areas for Improvement")

        for item in report["Weaknesses"]:

            st.write(f"• {item}")

        st.divider()

        # =====================================================
        # Recruiter Decision
        # =====================================================

        st.subheader("🎯 Recruiter Decision")

        st.success(
            hiring_report["Recommendation"]
        )

        st.info(
            report["Recruiter Decision"]
        )

        st.divider()

        # =====================================================
        # Career Advice
        # =====================================================

        st.subheader("📚 Career Advice")

        for advice in report["Career Advice"]:

            st.write(f"• {advice}")

        st.divider()

        # =====================================================
        # Complete Enterprise Report
        # =====================================================

        st.subheader("📄 Enterprise JSON Report")

        st.json({

            "Hiring Report": hiring_report,

            "AI Career Coach": report

        })