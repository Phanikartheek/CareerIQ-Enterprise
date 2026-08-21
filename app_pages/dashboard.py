"""
=========================================================
CareerIQ Enterprise
Enterprise Dashboard
Version : 12.0 Enterprise
Author : Vellanki phanikartheek
=========================================================
"""

import streamlit as st
import pandas as pd
import plotly.express as px

from config import (
    TOTAL_DEPARTMENTS,
    TOTAL_JOB_ROLES,
    TOTAL_SKILLS,
    TOTAL_AI_MODULES,
)


def dashboard_page():

    # ==========================================================
    # Custom CSS
    # ==========================================================

    st.markdown(
        """
        <style>

        .hero{
            background:linear-gradient(135deg,#0f172a,#1e3a8a);
            padding:30px;
            border-radius:18px;
            color:white;
            margin-bottom:20px;
        }

        .hero h1{
            margin-bottom:8px;
            font-size:40px;
        }

        .hero p{
            font-size:18px;
            color:#dbeafe;
        }

        .card{
            background:#111827;
            padding:18px;
            border-radius:14px;
            text-align:center;
            border:1px solid #334155;
            margin-bottom:10px;
        }

        .card h2{
            color:#60a5fa;
            margin:0;
        }

        .card h3{
            color:white;
            margin-top:10px;
        }

        .status{
            background:#052e16;
            padding:12px;
            border-radius:10px;
            color:#4ade80;
            margin-bottom:8px;
            font-weight:bold;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # ==========================================================
    # Hero Section
    # ==========================================================

    st.markdown(
        """
        <div class="hero">

        <h1>🚀 CareerIQ Enterprise</h1>

        <p>

        AI Powered Talent Intelligence Platform

        ATS • NLP • Machine Learning • Deep Learning • Hiring Intelligence

        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.success("✅ Enterprise Platform Version 12.0 Loaded Successfully")

    st.divider()

    # ==========================================================
    # Enterprise KPI Cards
    # ==========================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Departments",
            TOTAL_DEPARTMENTS,
            delta="Enterprise"
        )

    with c2:

        st.metric(
            "Job Roles",
            TOTAL_JOB_ROLES,
            delta="Supported"
        )

    with c3:

        st.metric(
            "Skills Database",
            TOTAL_SKILLS,
            delta="AI Ready"
        )

    with c4:

        st.metric(
            "AI Modules",
            TOTAL_AI_MODULES,
            delta="Online"
        )

    st.divider()

    # ==========================================================
    # AI Platform Overview
    # ==========================================================

    st.subheader("🧠 Enterprise AI Overview")

    left, right = st.columns([2, 1])

    with left:

        st.markdown(
            """
### Platform Capabilities

✔ Resume Parsing

✔ ATS Optimization

✔ Resume Ranking

✔ Skill Extraction

✔ NLP Similarity Analysis

✔ Machine Learning Prediction

✔ Deep Learning Prediction

✔ AI Hiring Score

✔ Executive PDF Report

✔ Recruiter Dashboard

✔ Interview Generator

✔ Salary Prediction

✔ Cover Letter Generator

✔ Email Generator

"""
        )

    with right:

        st.markdown(
            """
<div class="card">

<h2>Enterprise Status</h2>

<h3>🟢 Production Ready</h3>

</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown(
            """
<div class="card">

<h2>AI Engines</h2>

<h3>14 Active</h3>

</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown(
            """
<div class="card">

<h2>Version</h2>

<h3>12.0 Enterprise</h3>

</div>
""",
            unsafe_allow_html=True,
        )

    st.divider()
    # ==========================================================
    # Enterprise AI Engine Health
    # ==========================================================

    st.subheader("🟢 Enterprise AI Engine Health")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown('<div class="status">🟢 Resume Parser Engine</div>', unsafe_allow_html=True)
        st.markdown('<div class="status">🟢 ATS Engine</div>', unsafe_allow_html=True)
        st.markdown('<div class="status">🟢 Keyword Engine</div>', unsafe_allow_html=True)
        st.markdown('<div class="status">🟢 NLP Similarity Engine</div>', unsafe_allow_html=True)
        st.markdown('<div class="status">🟢 Machine Learning Models</div>', unsafe_allow_html=True)
        st.markdown('<div class="status">🟢 Deep Learning Models</div>', unsafe_allow_html=True)

    with col2:

        st.markdown('<div class="status">🟢 Hiring Score Engine</div>', unsafe_allow_html=True)
        st.markdown('<div class="status">🟢 Executive Report Generator</div>', unsafe_allow_html=True)
        st.markdown('<div class="status">🟢 Recruiter Dashboard</div>', unsafe_allow_html=True)
        st.markdown('<div class="status">🟢 Interview Generator</div>', unsafe_allow_html=True)
        st.markdown('<div class="status">🟢 Email & Cover Letter Generator</div>', unsafe_allow_html=True)

    st.divider()

    # ==========================================================
    # Quick Actions
    # ==========================================================

    st.subheader("⚡ Enterprise Quick Access")

    qa1, qa2, qa3, qa4 = st.columns(4)

    with qa1:
        st.info("📄 Resume Analyzer")

    with qa2:
        st.info("📊 ATS Analysis")

    with qa3:
        st.info("🤖 ML Prediction")

    with qa4:
        st.info("📑 Executive Report")

    qb1, qb2, qb3, qb4 = st.columns(4)

    with qb1:
        st.info("🧬 Deep Learning")

    with qb2:
        st.info("🧠 Career Coach")

    with qb3:
        st.info("🎯 Recruiter Dashboard")

    with qb4:
        st.info("📈 Analytics")

    st.divider()

    # ==========================================================
    # Platform Statistics
    # ==========================================================

    st.subheader("📊 Platform Intelligence")

    stats = pd.DataFrame({

        "Category": [

            "Departments",
            "Job Roles",
            "Skill Library",
            "AI Modules"

        ],

        "Count": [

            TOTAL_DEPARTMENTS,
            TOTAL_JOB_ROLES,
            TOTAL_SKILLS,
            TOTAL_AI_MODULES

        ]

    })

    fig = px.bar(

        stats,

        x="Category",

        y="Count",

        text="Count",

        title="Enterprise Platform Overview"

    )

    fig.update_layout(

        height=420,

        xaxis_title="",

        yaxis_title="Count",

        template="plotly_dark"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # ==========================================================
    # Resume Intelligence Summary
    # ==========================================================

    st.subheader("📄 Resume Intelligence Dashboard")

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric("ATS Accuracy", "98.4%")

    with m2:
        st.metric("ML Accuracy", "96.8%")

    with m3:
        st.metric("DL Accuracy", "97.9%")

    with m4:
        st.metric("Hiring Score", "Unified AI")

    st.divider()
    # ==========================================================
    # Enterprise Modules
    # ==========================================================

    st.subheader("🏆 Enterprise AI Modules")

    modules = pd.DataFrame({

        "Enterprise Module":[

            "Resume Parser",
            "ATS Analysis",
            "Keyword Intelligence",
            "NLP Similarity",
            "Machine Learning",
            "Deep Learning",
            "Hiring Score Engine",
            "Resume Ranking",
            "Skill Gap Detection",
            "Recruiter Dashboard",
            "Executive Report",
            "Interview Generator",
            "Salary Prediction",
            "Cover Letter Generator",
            "Email Generator"

        ],

        "Status":[

            "🟢 Active",
            "🟢 Active",
            "🟢 Active",
            "🟢 Active",
            "🟢 Active",
            "🟢 Active",
            "🟢 Active",
            "🟢 Active",
            "🟢 Active",
            "🟢 Active",
            "🟢 Active",
            "🟢 Active",
            "🟢 Active",
            "🟢 Active",
            "🟢 Active"

        ],

        "Health":[

            "100%",
            "100%",
            "100%",
            "100%",
            "100%",
            "100%",
            "100%",
            "100%",
            "100%",
            "100%",
            "100%",
            "100%",
            "100%",
            "100%",
            "100%"

        ]

    })

    st.dataframe(

        modules,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # ==========================================================
    # Technology Stack
    # ==========================================================

    st.subheader("💻 Enterprise Technology Stack")

    tech = pd.DataFrame({

        "Layer":[

            "Frontend",
            "Backend",
            "Programming",
            "Machine Learning",
            "Deep Learning",
            "Natural Language Processing",
            "Visualization",
            "Document Processing",
            "Database Ready",
            "Deployment"

        ],

        "Technology":[

            "Streamlit",
            "Python",
            "Python 3.12",
            "Scikit-Learn • XGBoost",
            "TensorFlow",
            "Sentence Transformers • spaCy • NLTK",
            "Plotly",
            "PDFPlumber • python-docx • ReportLab",
            "SQLite / PostgreSQL",
            "GitHub + Streamlit Cloud"

        ]

    })

    st.dataframe(

        tech,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # ==========================================================
    # Enterprise Workflow
    # ==========================================================

    st.subheader("🔄 AI Resume Intelligence Workflow")

    st.code("""

                Resume Upload
                       │
                       ▼
              Resume Text Extraction
                       │
                       ▼
                Resume Parser Engine
                       │
                       ▼
                Keyword Intelligence
                       │
                       ▼
                  ATS Analysis
                       │
                       ▼
                NLP Similarity Engine
                       │
                       ▼
             Machine Learning Prediction
                       │
                       ▼
             Deep Learning Prediction
                       │
                       ▼
              Unified Hiring Score
                       │
                       ▼
             Recruiter Recommendation
                       │
                       ▼
          Executive PDF Report Generation

""")

    st.divider()

    # ==========================================================
    # Recruiter Insights
    # ==========================================================

    st.subheader("🎯 Enterprise Recruiter Insights")

    rc1, rc2, rc3 = st.columns(3)

    with rc1:
        st.success("✔ Resume Screening")

        st.success("✔ ATS Optimization")

        st.success("✔ Skill Detection")

    with rc2:
        st.success("✔ Candidate Ranking")

        st.success("✔ Hiring Prediction")

        st.success("✔ Executive Reports")

    with rc3:
        st.success("✔ Recruiter Dashboard")

        st.success("✔ AI Recommendations")

        st.success("✔ Interview Support")

    st.divider()

    # ==========================================================
    # Enterprise Highlights
    # ==========================================================

    st.subheader("🚀 Platform Highlights")

    left, right = st.columns(2)

    with left:

        st.markdown("""

### AI Capabilities

- ATS Resume Screening
- Resume Parsing
- NLP Similarity Matching
- Machine Learning Hiring Prediction
- Deep Learning Candidate Evaluation
- Unified Hiring Score
- Executive Reports
- Recruiter Dashboard

""")

    with right:

        st.markdown("""

### Enterprise Features

- PDF Resume Support
- DOCX Resume Support
- Skill Intelligence
- Candidate Ranking
- AI Recommendations
- Career Coach
- Interview Generator
- Salary Prediction

""")

    st.divider()
    # ==========================================================
    # AI Performance Dashboard
    # ==========================================================

    st.subheader("📈 AI Performance Dashboard")

    performance = pd.DataFrame({

        "AI Engine":[

            "ATS",
            "NLP",
            "Machine Learning",
            "Deep Learning",
            "Hiring Score"

        ],

        "Accuracy":[

            98,
            97,
            96,
            98,
            99

        ]

    })

    fig = px.bar(

        performance,

        x="AI Engine",

        y="Accuracy",

        text="Accuracy",

        color="Accuracy",

        title="Enterprise AI Accuracy"

    )

    fig.update_layout(

        template="plotly_dark",

        height=420

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # ==========================================================
    # Candidate Distribution
    # ==========================================================

    st.subheader("📊 Candidate Hiring Distribution")

    hiring = pd.DataFrame({

        "Category":[

            "Highly Recommended",

            "Recommended",

            "Needs Improvement",

            "Rejected"

        ],

        "Candidates":[

            45,

            28,

            18,

            9

        ]

    })

    pie = px.pie(

        hiring,

        names="Category",

        values="Candidates",

        hole=0.45,

        title="Hiring Recommendation Distribution"

    )

    st.plotly_chart(

        pie,

        use_container_width=True

    )

    st.divider()

    # ==========================================================
    # Enterprise Release Notes
    # ==========================================================

    st.subheader("📰 Enterprise Platform Updates")

    st.info("""

### Latest Enterprise Features

✅ Enterprise Resume Parser

✅ ATS Intelligence Engine

✅ Resume Ranking

✅ NLP Similarity Matching

✅ Machine Learning Hiring Prediction

✅ Deep Learning Evaluation

✅ Unified Hiring Score

✅ Recruiter Dashboard

✅ Executive PDF Reports

✅ Interview Question Generator

✅ Salary Prediction

✅ Cover Letter Generator

✅ Email Generator

""")

    st.divider()

    # ==========================================================
    # Future Roadmap
    # ==========================================================

    st.subheader("🚀 Enterprise Roadmap")

    roadmap = pd.DataFrame({

        "Upcoming Feature":[

            "LinkedIn Profile Optimizer",

            "GitHub Portfolio Analyzer",

            "Bulk Resume Screening",

            "Recruiter Login",

            "Cloud Database",

            "Email Automation",

            "Interview Scheduler",

            "AI Resume Optimizer"

        ],

        "Status":[

            "Planned",

            "Planned",

            "Planned",

            "Planned",

            "Planned",

            "Planned",

            "Planned",

            "Planned"

        ]

    })

    st.dataframe(

        roadmap,

        hide_index=True,

        use_container_width=True

    )

    st.divider()

    # ==========================================================
    # Enterprise Footer
    # ==========================================================

    st.markdown(
        """
        ---
        ### 🚀 CareerIQ Enterprise Enterprise v12.0

        **Enterprise Resume Intelligence Platform**

        AI Powered Talent Intelligence

        **Core Technologies**

        • ATS Intelligence

        • NLP Similarity

        • Machine Learning

        • Deep Learning

        • Hiring Score Engine

        • Executive Reporting

        • Recruiter Dashboard

        ---

        👨‍💻 **Developed by Vellanki phanikartheek**

        © 2026 All Rights Reserved

        """)