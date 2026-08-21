"""
=========================================================
CareerIQ Enterprise
Enterprise Resume Analytics Dashboard
Author : Vellanki phanikartheek
Version : 9.1 Enterprise
=========================================================
"""

import streamlit as st
from core.ai_engine import AIEngine


def analytics_page():

    st.title("📈 Resume Analytics Dashboard")

    st.markdown(
        "Enterprise Resume Analytics powered by the AI Engine."
    )

    engine = AIEngine()

    st.divider()

    # =====================================================
    # Candidate Information
    # =====================================================

    st.subheader("Candidate Information")

    col1, col2 = st.columns(2)

    with col1:

        experience = st.slider(
            "Years of Experience",
            0,
            20,
            0,
            key="analytics_experience"
        )

        projects = st.number_input(
            "Projects",
            0,
            50,
            3,
            key="analytics_projects"
        )

        certifications = st.number_input(
            "Certifications",
            0,
            20,
            6,
            key="analytics_certifications"
        )

    with col2:

        resume_words = st.number_input(
            "Resume Word Count",
            100,
            5000,
            600,
            key="analytics_words"
        )

        resume_score = st.slider(
            "Resume Quality Score",
            0,
            100,
            90,
            key="analytics_score"
        )

    st.divider()

    # =====================================================
    # Skill Analysis
    # =====================================================

    st.subheader("Skill Analysis")

    matched = st.multiselect(

        "Matched Skills",

        [
            # Programming
            "Python", "JavaScript", "Java", "Go", "TypeScript",
            # Web / Full Stack
            "React.js", "Next.js", "Node.js", "Express.js", "HTML5", "CSS3",
            "MERN Stack", "REST API",
            # AI / ML
            "Machine Learning", "Deep Learning", "XGBoost", "scikit-learn",
            "TensorFlow", "PyTorch", "LLM", "Gemini API", "OpenAI",
            "Prompt Engineering", "Agentic AI", "NLP", "SMOTE",
            "Supervised Learning", "Feature Engineering", "Hyperparameter Tuning",
            "GridSearchCV", "k-fold Cross Validation",
            # Backend / APIs
            "FastAPI", "Flask", "Django",
            # Data
            "Pandas", "NumPy", "SQL", "MySQL", "MongoDB", "Redis",
            "Vector Databases", "RAG",
            # Cloud / DevOps
            "AWS", "AWS EC2", "OCI", "Oracle Cloud", "Azure", "GCP",
            "Docker", "Kubernetes", "CI/CD", "GitHub Actions", "Git",
            # Tools
            "Postman", "Power BI", "Excel", "Tableau",
        ],

        default=[
            "Python", "JavaScript", "React.js", "FastAPI", "Flask",
            "XGBoost", "Machine Learning", "Deep Learning",
            "Docker", "AWS", "Git", "MongoDB", "Gemini API",
            "Prompt Engineering",
        ],

        key="analytics_matched"

    )

    missing = st.multiselect(

        "Missing Skills",

        [
            "Kubernetes", "TensorFlow", "PyTorch", "Azure", "GCP",
            "Power BI", "Tableau", "Kafka", "Spark", "Hadoop",
            "GraphQL", "PostgreSQL", "Redis", "TypeScript",
        ],

        default=[],

        key="analytics_missing"

    )

    st.divider()

    # =====================================================
    # Generate Analytics
    # =====================================================

    if st.button(
        "🚀 Generate Analytics",
        use_container_width=True
    ):

        analytics = engine.analytics

        features = {

            "Experience": experience,

            "Projects": projects,

            "Certifications": certifications,

            "Resume Words": resume_words,

            "Resume Quality Score": resume_score

        }

        # ------------------------------------------------

        st.subheader("📋 Resume Summary")

        summary = analytics.summary(features)

        st.dataframe(
            summary,
            use_container_width=True,
            hide_index=True
        )

        # ------------------------------------------------

        st.subheader("🛠 Skill Distribution")

        skill_df = analytics.skill_distribution(
            matched,
            missing
        )

        st.dataframe(
            skill_df,
            use_container_width=True,
            hide_index=True
        )

        # ------------------------------------------------

        pie = analytics.pie_chart(
            matched,
            missing
        )

        st.plotly_chart(
            pie,
            use_container_width=True,
            key="analytics_pie"
        )

        # ------------------------------------------------

        bar = analytics.bar_chart(
            matched,
            missing
        )

        st.plotly_chart(
            bar,
            use_container_width=True,
            key="analytics_bar"
        )

        st.divider()

        # =====================================================
        # Analytics Metrics
        # =====================================================

        st.subheader("📊 Analytics Metrics")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Experience Level",
            analytics.experience_level(experience)
        )

        c2.metric(
            "Resume Strength",
            analytics.resume_strength(resume_score)
        )

        c3.metric(
            "Matched Skills",
            len(matched)
        )

        st.divider()

        # =====================================================
        # Dashboard Metrics
        # =====================================================

        metrics = analytics.dashboard_metrics(

            ats=resume_score,

            similarity=85,

            quality=resume_score

        )

        st.subheader("📈 Dashboard Metrics")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Overall Score",
            metrics["Overall Score"]
        )

        col2.metric(
            "Grade",
            metrics["Grade"]
        )

        col3.metric(
            "Recommendation",
            metrics["Recommendation"]
        )

        st.divider()

        st.json(metrics)