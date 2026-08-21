"""
=========================================================
CareerIQ Enterprise
Intelligent Talent Intelligence Platform
Author : Vellanki phanikartheek
Version : 11.0 Enterprise
=========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import streamlit as st

from config import (
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
)

from ui.sidebar import render_sidebar

# ==========================================================
# App_Page Imports
# ==========================================================

from app_pages.dashboard import dashboard_page
from app_pages.resume_analyzer import resume_analyzer_page
from app_pages.ats_analysis import ats_analysis_page
from app_pages.nlp_analysis import nlp_analysis_page
from app_pages.analytics import analytics_page
from app_pages.ml_prediction import ml_prediction_page
from app_pages.recruiter_dashboard import recruiter_dashboard_page
from app_pages.salary_prediction import salary_prediction_page
from app_pages.learning_roadmap import learning_roadmap_page
from app_pages.interview_generator import interview_generator_page
from app_pages.cover_letter import cover_letter_page
from app_pages.email_generator import email_generator_page
from app_pages.executive_report import executive_report_page
from app_pages.settings import settings_page
from app_pages.deep_learning import deep_learning_page
from app_pages.github_portfolio import github_portfolio_page
from app_pages.linkedin_optimizer import linkedin_optimizer_page

# ==========================================================
# Streamlit Configuration
# ==========================================================

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state="expanded"
)

# ==========================================================
# Load Custom CSS
# ==========================================================

def load_css():

    try:

        with open(
            "assets/style.css",
            "r",
            encoding="utf-8"
        ) as css:

            st.markdown(
                f"<style>{css.read()}</style>",
                unsafe_allow_html=True
            )

    except FileNotFoundError:

        pass


load_css()

# ==========================================================
# Sidebar
# ==========================================================

menu = render_sidebar()

# ==========================================================
# Routing Dictionary
# ==========================================================

PAGE_ROUTES = {

    "🏠 Dashboard":
        dashboard_page,

    "📄 Resume Analyzer":
        resume_analyzer_page,

    "📊 ATS Analysis":
        ats_analysis_page,

    "🧠 NLP Analysis":
        nlp_analysis_page,

    "📈 EDA Dashboard":
        analytics_page,

    "🤖 Machine Learning":
        ml_prediction_page,

    "🧬 Deep Learning":
        deep_learning_page,

    "🎯 Recruiter Dashboard":
        recruiter_dashboard_page,

    "💼 Salary Prediction":
        salary_prediction_page,

    "📚 Learning Roadmap":
        learning_roadmap_page,

    "🎤 Interview Generator":
        interview_generator_page,

    "📜 Cover Letter":
        cover_letter_page,

    "📧 Email Generator":
        email_generator_page,

    "👤 LinkedIn Optimizer":
        linkedin_optimizer_page,

    "💻 GitHub Portfolio":
        github_portfolio_page,

    "📑 Executive Report":
        executive_report_page,

    "⚙️ Settings":
        settings_page,
}

# ==========================================================
# Run Selected Page
# ==========================================================

if menu in PAGE_ROUTES:

    PAGE_ROUTES[menu]()



# ==========================================================
# Unknown Route
# ==========================================================

else:

    st.error(
        "Unknown page selected."
    )
