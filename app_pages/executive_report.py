"""
=========================================================
CareerIQ Enterprise
Enterprise Executive Report
Version : 11.0 Enterprise
Author : Vellanki phanikartheek
=========================================================
"""

import streamlit as st

from core.report_generator import ReportGenerator
from core.hiring_score import HiringScoreEngine


def executive_report_page():

    st.title("📑 Executive AI Report")

    st.markdown(
        """
Generate a complete AI-powered executive hiring report
including ATS, Machine Learning, Deep Learning,
Hiring Score and PDF Export.
"""
    )

    st.divider()

    report = ReportGenerator()

    hiring_engine = HiringScoreEngine()

    st.subheader("Candidate Information")

    col1, col2 = st.columns(2)

    with col1:

        candidate_name = st.text_input(
            "Candidate Name",
            "John Doe"
        )

        department = st.text_input(
            "Department",
            "Information Technology"
        )

        job_role = st.text_input(
            "Target Role",
            "AI Engineer"
        )

    with col2:

        ats_score = st.slider(
            "ATS Score",
            0,
            100,
            82
        )

        ml_score = st.slider(
            "Machine Learning Score",
            0,
            100,
            84
        )

        dl_score = st.slider(
            "Deep Learning Score",
            0,
            100,
            86
        )

    st.divider()

    st.subheader("Skill Analysis")

    matched = st.text_area(
        "Matched Skills (comma separated)",
        "Python, SQL, Machine Learning, Pandas"
    )

    missing = st.text_area(
        "Missing Skills (comma separated)",
        "Docker, Kubernetes"
    )

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

    st.divider()

    st.subheader("Resume Statistics")

    col1, col2 = st.columns(2)

    with col1:

        words = st.number_input(
            "Words",
            value=520
        )

        characters = st.number_input(
            "Characters",
            value=3450
        )

    with col2:

        sentences = st.number_input(
            "Sentences",
            value=38
        )

        lines = st.number_input(
            "Lines",
            value=64
        )

    statistics = {

        "Words": words,

        "Characters": characters,

        "Sentences": sentences,

        "Lines": lines

    }

    st.divider()

    if st.button(

        "🚀 Generate Executive Report",

        use_container_width=True

    ):

        result = hiring_engine.report(

            ats=ats_score,

            similarity=ats_score,

            ml=ml_score,

            dl=dl_score,

            technical=min(len(matched_skills) * 10, 100),

            soft_skills=80,

            experience=50

        )

        final_score = result["Hiring Score"]

        recommendation = result["Recommendation"]
        st.success("Executive Report Generated Successfully")

        st.metric(
            "Final Hiring Score",
            f"{final_score}%"
        )

        st.progress(final_score / 100)

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "ATS Score",
                f"{ats_score}%"
            )

            st.metric(
                "Machine Learning",
                f"{ml_score}%"
            )

        with col2:

            st.metric(
                "Deep Learning",
                f"{dl_score}%"
            )

            st.metric(
                "Recommendation",
                recommendation
            )

        pdf_path = report.generate_report(

            candidate_name=candidate_name,

            department=department,

            job_role=job_role,

            ats_score=ats_score,

            matched_skills=matched_skills,

            missing_skills=missing_skills,

            ml_score=ml_score,

            dl_score=dl_score,

            recommendation=recommendation,

            statistics=statistics

        )

        st.success("PDF Report Generated")

        with open(pdf_path, "rb") as pdf:

            st.download_button(

                label="📥 Download Executive Report",

                data=pdf,

                file_name=pdf_path.split("/")[-1],

                mime="application/pdf",

                use_container_width=True

            )

        st.divider()

        st.subheader("Executive Summary")

        st.json(

            {

                "Candidate": candidate_name,

                "Department": department,

                "Role": job_role,

                "ATS Score": ats_score,

                "ML Score": ml_score,

                "DL Score": dl_score,

                "Final Hiring Score": final_score,

                "Matched Skills": matched_skills,

                "Missing Skills": missing_skills,

                "Recommendation": recommendation,

                "Statistics": statistics

            }

        )
