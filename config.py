"""
=========================================================
CareerIQ Enterprise
Enterprise AI Career Intelligence Platform
Configuration File
Author : Vellanki phanikartheek
Version : 11.0
=========================================================
"""

# ==========================================================
# APPLICATION
# ==========================================================

APP_NAME = "CareerIQ"
APP_VERSION = "12.0 Enterprise"

PAGE_TITLE = "CareerIQ Enterprise"
PAGE_ICON = "🤖"
LAYOUT = "wide"

AUTHOR = "Vellanki phanikartheek"
THEME = "Dark"

# ==========================================================
# FILE UPLOAD
# ==========================================================

SUPPORTED_FILES = [
    "pdf",
    "docx"
]

MAX_FILE_SIZE = 25  # MB

# ==========================================================
# THEME COLORS
# ==========================================================

PRIMARY_COLOR = "#2563EB"
SECONDARY_COLOR = "#0F172A"

SUCCESS_COLOR = "#22C55E"
WARNING_COLOR = "#F59E0B"
ERROR_COLOR = "#EF4444"

BACKGROUND = "#F8FAFC"

# ==========================================================
# RESUME LIMITS
# ==========================================================

MIN_WORDS = 100
MAX_WORDS = 5000

# ==========================================================
# ATS CONFIGURATION
# ==========================================================

ATS_PASS_SCORE = 70

SIMILARITY_WEIGHT = 0.30
SKILL_WEIGHT = 0.40
EXPERIENCE_WEIGHT = 0.20
EDUCATION_WEIGHT = 0.10

# ==========================================================
# MODEL PATHS
# ==========================================================

MODEL_PATH = "models/"

LINEAR_MODEL = MODEL_PATH + "regression_model.pkl"
RANDOM_FOREST_MODEL = MODEL_PATH + "random_forest.pkl"
XGBOOST_MODEL = MODEL_PATH + "xgboost.pkl"

SCALER = MODEL_PATH + "scaler.pkl"
LABEL_ENCODER = MODEL_PATH + "label_encoder.pkl"
TFIDF = MODEL_PATH + "tfidf_vectorizer.pkl"

DEEP_MODEL = MODEL_PATH + "deep_learning_model.joblib"

# ==========================================================
# DATA FILES
# ==========================================================

JOB_DATA = "data/job_roles.csv"
SKILLS = "data/skills_master.csv"
LEARNING = "data/learning_paths.csv"
SALARY = "data/salary_data.csv"

# ==========================================================
# DASHBOARD METRICS
# ==========================================================

TOTAL_DEPARTMENTS = 30
TOTAL_JOB_ROLES = 450
TOTAL_SKILLS = 5000
TOTAL_AI_MODULES = 15

# ==========================================================
# VISUALIZATION
# ==========================================================

CHART_HEIGHT = 450
PIE_HOLE = 0.55

# ==========================================================
# RECRUITER
# ==========================================================

MAX_RESUMES = 20
TOP_CANDIDATES = 5

# ==========================================================
# FEATURE FLAGS
# ==========================================================

ENABLE_EDA = True
ENABLE_ML = True
ENABLE_DL = True
ENABLE_GENAI = True
ENABLE_INTERVIEW = True
ENABLE_EMAIL = True
ENABLE_COVER = True
ENABLE_ROADMAP = True
ENABLE_RECRUITER = True

# ==========================================================
# AI CONFIGURATION
# ==========================================================

OLLAMA_MODEL = "llama3"
OPENAI_MODEL = "gpt-4o-mini"

TEMPERATURE = 0.3
MAX_TOKENS = 1000

# ==========================================================
# FOOTER
# ==========================================================

FOOTER = "Developed with ❤️ by Vellanki phanikartheek"

COPYRIGHT = "© 2026 CareerIQ Enterprise"

# ==========================================================
# SIDEBAR MENU
# ==========================================================

SIDEBAR_MENU = [

    "🏠 Dashboard",

    "📄 Resume Analyzer",

    "📊 ATS Analysis",

    "🧠 NLP Analysis",

    "📈 EDA Dashboard",

    "🤖 Machine Learning",

    "🧬 Deep Learning",

    "🎯 Recruiter Dashboard",

    "💼 Salary Prediction",

    "📚 Learning Roadmap",

    "🎤 Interview Generator",

    "📜 Cover Letter",

    "📧 Email Generator",

    "👤 LinkedIn Optimizer",

    "💻 GitHub Portfolio",

    "📑 Executive Report",

    "⚙️ Settings"
]
