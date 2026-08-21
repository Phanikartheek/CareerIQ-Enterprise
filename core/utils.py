"""
=========================================================
Resume Intelligence AI
Utility Functions
Version : 8.0
Author : Vellanki phanikartheek
=========================================================
"""

import os
import re
import pandas as pd
import streamlit as st
from datetime import datetime

# ==========================================================
# Date & Time
# ==========================================================

def current_datetime():
    """Return current date and time."""
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# ==========================================================
# File Validation
# ==========================================================

def validate_file(uploaded_file):

    if uploaded_file is None:
        return False, "No file uploaded."

    extension = uploaded_file.name.split(".")[-1].lower()

    if extension not in ["pdf", "docx"]:
        return False, "Only PDF and DOCX files are supported."

    return True, "Valid File"


# ==========================================================
# Resume Statistics
# ==========================================================

def resume_statistics(text):

    words = len(text.split())

    characters = len(text)

    sentences = len(re.findall(r"[.!?]", text))

    lines = len(text.splitlines())

    return {
        "Words": words,
        "Characters": characters,
        "Sentences": sentences,
        "Lines": lines
    }


# ==========================================================
# Progress Color
# ==========================================================

def score_color(score):

    if score >= 80:
        return "green"

    elif score >= 60:
        return "orange"

    return "red"


# ==========================================================
# Resume Grade
# ==========================================================

def grade(score):

    if score >= 90:
        return "A+"

    elif score >= 80:
        return "A"

    elif score >= 70:
        return "B"

    elif score >= 60:
        return "C"

    return "Needs Improvement"


# ==========================================================
# Experience Formatter
# ==========================================================

def experience_label(years):

    if years < 1:
        return "Fresher"

    elif years <= 3:
        return "Junior"

    elif years <= 7:
        return "Mid-Level"

    elif years <= 12:
        return "Senior"

    return "Expert"


# ==========================================================
# Percentage Formatter
# ==========================================================

def percentage(value):

    return f"{round(value,2)}%"


# ==========================================================
# CSV Export
# ==========================================================

def dataframe_to_csv(df):

    return df.to_csv(index=False).encode("utf-8")


# ==========================================================
# Download Button
# ==========================================================

def download_csv(df, filename):

    st.download_button(

        "⬇ Download CSV",

        dataframe_to_csv(df),

        filename,

        "text/csv"

    )


# ==========================================================
# Report Filename
# ==========================================================

def report_filename(prefix="Resume_Report"):

    now = datetime.now().strftime("%Y%m%d_%H%M%S")

    return f"{prefix}_{now}.pdf"


# ==========================================================
# Skill Coverage
# ==========================================================

def skill_coverage(matched, required):

    if required == 0:
        return 0

    return round((matched / required) * 100, 2)


# ==========================================================
# Missing Skills
# ==========================================================

def missing_skills(required, matched):

    return list(set(required) - set(matched))


# ==========================================================
# Match Skills
# ==========================================================

def matched_skills(required, resume):

    matched = []

    resume = resume.lower()

    for skill in required:

        if skill.lower() in resume:

            matched.append(skill)

    return matched


# ==========================================================
# Resume Strength
# ==========================================================

def resume_strength(score):

    if score >= 90:

        return "Excellent Resume"

    elif score >= 80:

        return "Very Good Resume"

    elif score >= 70:

        return "Good Resume"

    elif score >= 60:

        return "Average Resume"

    return "Needs Improvement"


# ==========================================================
# Empty DataFrame
# ==========================================================

def empty_dataframe():

    return pd.DataFrame()


# ==========================================================
# Create Folder
# ==========================================================

def create_folder(folder):

    if not os.path.exists(folder):

        os.makedirs(folder)