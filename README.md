# 🚀 CareerIQ Enterprise

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.62+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-Models-EB6100?style=for-the-badge&logo=xgboost&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-DL-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)

### 🤖 Next-Generation AI Talent, Resume & Recruitment Intelligence Platform

**AI Resume Screening • ATS Score Optimization • Multi-Model ML/DL Predictions • Recruiter Intelligence • Automated Executive PDF Reports**

[Explore Features](#-key-features) • [Installation & Setup](#-installation--quickstart) • [Architecture](#-system-architecture) • [Live Dashboard](#-dashboard--ui-modules) • [Author](#-author--creator)

</div>

---

## 📖 Executive Summary

**CareerIQ Enterprise** is an AI-powered talent intelligence and recruitment automation system built for recruiters, hiring managers, talent acquisition teams, and job seekers. 

Powered by **Machine Learning (Random Forest, XGBoost, Linear Regression)**, **Natural Language Processing (spaCy, Sentence Transformers, NLTK)**, and **Deep Neural Networks**, CareerIQ automates candidate evaluation, score calibration, skill gap identification, salary forecasting, and executive PDF reporting in real-time.

---

## ✨ Key Platform Capabilities

### 📄 1. Advanced Resume Intelligence Engine
- **Multi-Format Parsing:** High-accuracy extraction from PDF and DOCX files.
- **Entity Extraction:** Contact details, email, phone, location, work history, education, projects, and social profiles.
- **Skill Categorization:** Maps technical, soft, domain-specific, and leadership competencies against an enterprise dataset of **5,000+ industry skills**.

### 🎯 2. ATS Intelligence & Scoring
- **Automated ATS Compatibility Score (0–100%):** Weighted scoring across section completeness, keyword presence, experience alignment, and formatting.
- **Missing Keyword Detection:** Identifies critical keywords absent from the candidate profile.
- **Formatting & Section Validation:** Verifies essential sections (Summary, Experience, Education, Skills, Projects).

### 🧠 3. NLP Semantic Matcher
- **Deep Semantic Similarity:** Uses Sentence Transformers and TF-IDF for contextual role matching beyond simple keyword matching.
- **Role Alignment Index:** Compares candidate profiles against **450+ standardized job titles** across **30 enterprise departments**.

### 🤖 4. Machine Learning & Predictive Analytics
- **Candidate Hiring Likelihood:** Evaluates candidate qualification using trained Random Forest and XGBoost classifiers.
- **Model Comparison Dashboard:** Real-time benchmark metrics (Precision, Recall, F1-Score, ROC-AUC) across algorithms.

### 🧬 5. Deep Learning Candidate Classification
- Multi-layer neural network architecture for complex multi-attribute candidate grading and classification.

### 📊 6. Recruiter Intelligence & Batch Screening
- **Multi-Resume Bulk Processing:** Upload and rank dozens of resumes simultaneously against a target Job Description.
- **Leaderboard & Shortlisting:** Automated tiered candidate ranking (*Highly Recommended, Recommended, Needs Review, Rejected*).

### 💼 7. AI Compensation & Salary Intelligence
- **Market CTC Range Estimator:** Predicts fair compensation based on experience, company tier, location, and skill premium boosts.
- **10-Year Growth Trajectory:** Forecasts long-term career earnings based on skill acquisition.

### 📚 8. Zero-to-Pro Learning Roadmaps
- **Phase-by-Phase Skill Acquisition:** Step-by-step career transition blueprints with curated industry projects, certifications, and resources.

### 🎤 9. AI Interview & Application Suite
- **Custom Interview Generator:** Generates role-tailored technical, behavioral, and situational interview questions with ideal response rubrics.
- **Cover Letter & Email Generators:** Personalized cold outreach, interview invitations, follow-ups, and recruiter communications.

### 📑 10. Executive PDF Report Generation
- **Presentation-Ready Reports:** Generates branded, executive-level PDF dossiers containing complete candidate scorecards, skill gap charts, ATS audits, and AI hiring recommendations.

---

## 🏗 System Architecture & Workflow

```
                             ┌─────────────────────────┐
                             │   Candidate Resume      │
                             │     (PDF / DOCX)        │
                             └────────────┬────────────┘
                                          │
                                          ▼
                             ┌─────────────────────────┐
                             │  Resume Parser Engine   │
                             │ (PDFPlumber, docx, NLP) │
                             └────────────┬────────────┘
                                          │
                  ┌───────────────────────┼───────────────────────┐
                  ▼                       ▼                       ▼
       ┌────────────────────┐  ┌────────────────────┐  ┌────────────────────┐
       │   ATS Validator    │  │  NLP Similarity    │  │  Skill & Keyword   │
       │  & Section Engine  │  │ (Sentence Embed.)  │  │  Extraction Engine │
       └──────────┬─────────┘  └──────────┬─────────┘  └──────────┬─────────┘
                  │                       │                       │
                  └───────────────────────┼───────────────────────┘
                                          │
                                          ▼
                       ┌─────────────────────────────────────┐
                       │    ML & Deep Learning Evaluator     │
                       │ (Random Forest, XGBoost, Neural Net)│
                       └──────────────────┬──────────────────┘
                                          │
                                          ▼
                       ┌─────────────────────────────────────┐
                       │      Unified AI Hiring Score        │
                       │     & Recruiter Decision Engine     │
                       └──────────────────┬──────────────────┘
                                          │
                  ┌───────────────────────┴───────────────────────┐
                  ▼                                               ▼
       ┌────────────────────────┐                    ┌────────────────────────┐
       │ Recruiter Dashboard UI │                    │  Executive PDF Report  │
       │ (Streamlit + Plotly)   │                    │     (ReportLab)        │
       └────────────────────────┘                    └────────────────────────┘
```

---

## ⚙ Technology Stack

| Component | Technologies |
|---|---|
| **Frontend UI** | Streamlit, HTML5, Custom CSS, Plotly Express, Altair |
| **Backend & Runtime** | Python 3.10+ |
| **Machine Learning** | Scikit-Learn, XGBoost, Joblib, Scipy, NumPy, Pandas |
| **Deep Learning** | PyTorch, Neural Networks |
| **Natural Language Processing** | Sentence Transformers, spaCy, NLTK, TF-IDF |
| **Document Processing** | PDFPlumber, python-docx, ReportLab |
| **Data & Benchmarking** | 5,000+ Skills Master Dataset, 450+ Job Roles Database |

---

## 📂 Project Structure

```text
CareerIQ-Enterprise/
│
├── app.py                          # Main Streamlit Application Entrypoint
├── config.py                       # Global Enterprise Configuration & Settings
├── requirements.txt                # Production Dependencies
├── train_models.py                 # Automated Model Training Pipeline
│
├── app_pages/                      # Interactive Application Pages
│   ├── dashboard.py                # Executive KPI Dashboard & Platform Overview
│   ├── resume_analyzer.py          # Single Resume Deep Analyzer
│   ├── ats_analysis.py             # ATS Optimization & Scoring
│   ├── nlp_analysis.py             # Semantic Similarity & Role Matcher
│   ├── ml_prediction.py            # ML Hiring Predictor & Model Comparison
│   ├── deep_learning.py            # Neural Network Candidate Classifier
│   ├── recruiter_dashboard.py      # Bulk Resume Screening & Candidate Leaderboard
│   ├── salary_prediction.py        # AI Market CTC & Compensation Forecast
│   ├── learning_roadmap.py         # Zero-to-Pro Career Learning Roadmaps
│   ├── interview_generator.py      # AI Tailored Interview Question Generator
│   ├── cover_letter.py             # AI Cover Letter Generator
│   ├── email_generator.py          # Recruiter & Candidate Email Suite
│   ├── linkedin_optimizer.py       # Enterprise LinkedIn Profile Optimizer
│   ├── github_portfolio.py         # GitHub Tech Portfolio Analyzer
│   ├── executive_report.py         # PDF Dossier Generator
│   ├── analytics.py                # Talent & Market Analytics
│   └── settings.py                 # Platform Information & System Settings
│
├── core/                           # AI & Business Logic Engines
│   ├── ai_engine.py                # Central AI Orchestrator
│   ├── ats_engine.py               # ATS Scoring Algorithms
│   ├── resume_parser.py            # Multi-format Resume Parser
│   ├── keyword_engine.py           # Keyword & Skill Matching Engine
│   ├── ml_prediction.py            # Machine Learning Inference
│   ├── deep_learning.py            # Deep Neural Network Engine
│   ├── similarity_engine.py        # Semantic Embedding Matcher
│   ├── salary_prediction.py        # Compensation Models
│   ├── learning_recommender.py     # Roadmap & Curriculum Engine
│   ├── interview_generator.py      # Question & Rubric Generator
│   ├── linkedin_optimizer.py       # Profile Optimization Engine
│   ├── github_analyzer.py          # GitHub API Code & Repo Analyzer
│   └── report_generator.py         # ReportLab PDF Dossier Builder
│
├── data/                           # Standardized Datasets
│   ├── skills_master.csv           # 5,000+ Master Skills Database
│   ├── job_roles.csv               # 450+ Industry Roles
│   ├── learning_paths.csv          # Curated Learning Resources & Roadmaps
│   └── salary_data.csv             # Compensation Benchmarks
│
├── models/                         # Pretrained ML & DL Models
│   ├── random_forest.pkl           # Random Forest Classifier
│   ├── xgboost.pkl                 # XGBoost Classifier
│   └── linear_regression.pkl       # Salary & Score Regressor
│
├── assets/                         # Styling & UI Resources
│   └── style.css                   # Custom Enterprise Dark Theme CSS
│
└── reports/                        # Auto-generated Executive PDF Reports
```

---

## 🚀 Installation & Quickstart

### 1. Clone the Repository
```bash
git clone https://github.com/Phanikartheek/CareerIQ-Enterprise.git
cd CareerIQ-Enterprise
```

### 2. Create and Activate Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Platform
```bash
streamlit run app.py
```

Open your browser and navigate to **`http://localhost:8501`**.

---

## 📊 Modules & Features Overview

| Module | Description |
|---|---|
| 🏠 **Dashboard** | High-level platform health, active AI modules, and talent intelligence metrics. |
| 📄 **Resume Analyzer** | Comprehensive resume breakdown with entity extraction and section audits. |
| 📊 **ATS Analysis** | ATS score calculation, missing keyword discovery, and optimization checklist. |
| 🧠 **NLP Analysis** | Semantic similarity scores against role benchmarks using embeddings. |
| 🤖 **Machine Learning** | Random Forest, XGBoost, and Decision Tree candidate evaluations. |
| 🧬 **Deep Learning** | Neural network classification with confidence percentiles. |
| 🎯 **Recruiter Dashboard** | Bulk resume screening, ranked leaderboards, and candidate filtering. |
| 💼 **Salary Prediction** | Industry compensation models, experience multiplier, and skill ROI. |
| 📚 **Learning Roadmap** | Customized milestone-based learning plans from Beginner to Expert. |
| 🎤 **Interview Generator** | Role-tailored questions covering coding, system design, and behavioral traits. |
| 👤 **LinkedIn Optimizer** | Recruiter search visibility audit, headline generators, and About section blueprints. |
| 💻 **GitHub Portfolio** | Analyzes public repositories, commit cadence, and language proficiency. |
| 📑 **Executive Report** | Export comprehensive PDF reports ready for executive hiring boards. |

---

## 👨‍💻 Author & Creator

<div align="center">

### **Vellanki Phanikartheek**
**AI Engineer | Python Developer | Talent Intelligence Architect**

[![GitHub](https://img.shields.io/badge/GitHub-Phanikartheek-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Phanikartheek)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com)
[![Repository](https://img.shields.io/badge/Repository-CareerIQ--Enterprise-2563EB?style=for-the-badge&logo=git&logoColor=white)](https://github.com/Phanikartheek/CareerIQ-Enterprise)

</div>

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

---

<div align="center">

### ⭐ Star the Repository if you find this project valuable! ⭐

**© 2026 CareerIQ Enterprise • Engineered by Vellanki Phanikartheek**

</div>