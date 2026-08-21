import streamlit as st
from core.email_generator import EmailGenerator


def email_generator_page():
    """
    AI Email Generator Page
    """

    st.header("📧 AI Email Generator")

    candidate_name = st.text_input("Candidate Name")

    company_name = st.text_input("Company Name")

    job_role = st.text_input("Job Role")

    email_type = st.selectbox(
        "Email Type",
        [
            "Job Application",
            "Follow Up",
            "Thank You"
        ]
    )

    if st.button("Generate Email"):

        if not (candidate_name and company_name and job_role):
            st.warning("Please fill all fields.")
            return

        generator = EmailGenerator()

        with st.spinner("Generating Email..."):

            if email_type == "Job Application":
                email = generator.application_email(
                    candidate_name,
                    company_name,
                    job_role
                )
            else:
                email = generator.application_email(
                    candidate_name,
                    company_name,
                    job_role
                )

        st.success("Email Generated Successfully!")

        st.text_area(
            "Generated Email",
            value=email,
            height=300
        )