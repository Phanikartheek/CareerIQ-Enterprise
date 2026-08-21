import streamlit as st
from core.interview_generator import InterviewGenerator


def interview_generator_page():
    """
    Interview Question Generator Page
    """

    st.header("🎤 AI Interview Generator")

    role = st.text_input(
        "Target Job Role",
        placeholder="e.g. Data Scientist"
    )

    if st.button("Generate Interview Questions"):

        if not role.strip():
            st.warning("Please enter a job role.")
            return

        generator = InterviewGenerator()

        with st.spinner("Generating Questions..."):
            interview_kit = generator.generate(
                matched_skills=[role],
                missing_skills=[],
                experience=0,
            )

        questions = interview_kit["Questions"]

        st.success("Questions Generated Successfully!")

        for i, question in enumerate(questions, start=1):
            st.write(f"**{i}.** {question}")
