"""
=========================================================
CareerIQ Enterprise - Enterprise Multi-Role ML Prediction (Automated)
Version : 12.0 Enterprise Production Edition
Author  : CareerIQ Engineering
=========================================================
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from core.ml_prediction import MLPredictor
from core.resume_parser import ResumeParser


def ml_prediction_page():
    st.title("🤖 Enterprise Machine Learning Hiring Prediction (Automated)")
    st.markdown(
        "Upload your **Resume PDF** or paste profile text. CareerIQ Enterprise **automatically extracts** your competencies, "
        "runs supervised **Random Forest / XGBoost ML models**, and predicts your **Hiring Shortlist Probability (0-100%)**."
    )

    predictor = MLPredictor()
    parser = ResumeParser()
    roles = predictor.get_supported_roles()

    SAMPLE_CANDIDATES = {
        "Custom Upload / Paste Below": "",
        "👤 Sabir Shaik (AI / ML Engineer Resume)": """
Sabir Shaik
Email: sabir.shaik@example.com | Phone: +91 9876543210 | LinkedIn: https://linkedin.com/in/sabir-shaik
Experience: 2+ years of experience as AI Developer.
Skills: Python, Machine Learning, Deep Learning, PyTorch, TensorFlow, FastAPI, Docker, SQL, Git, NLP, HuggingFace.
Projects:
• Developed an enterprise conversational AI agent using LangChain and FastAPI with sub-200ms latency.
• Built production fraud detection system using PyTorch and XGBoost on 100K+ records with 93% precision.
• Deployed containerized ML microservices on Docker with automated CI/CD pipelines.
Education: Bachelor of Technology in Computer Science (B.Tech).
Certifications: DeepLearning.AI Generative AI Specialist, AWS Certified Cloud Practitioner.
        """,
        "💻 Alex Morgan (Full Stack Developer Resume)": """
Alex Morgan
Email: alex.morgan@example.com | LinkedIn: https://linkedin.com/in/alex-morgan
Experience: 3 years as Full Stack Engineer.
Skills: JavaScript, TypeScript, React.js, Next.js, Node.js, Express.js, PostgreSQL, Docker, REST APIs, Tailwind CSS.
Projects:
• Built multi-tenant SaaS dashboard using Next.js 14 App Router, TypeScript, and Prisma ORM.
• Architected high-throughput backend APIs with Node.js, Redis caching, and PostgreSQL database indexing.
Education: B.Tech in Information Technology.
Certifications: Meta Certified Front-End Developer.
        """,
        "🎓 Teja Thota (Fresher / Software Engineer Resume)": """
Teja Thota
Email: teja.thota@example.com | Phone: +91 8765432109
Experience: 0.5 years (Academic Intern).
Skills: Python, Java, Data Structures & Algorithms, SQL, Git, HTML/CSS, OOP.
Projects:
• Developed college management web system with Java and SQL database.
• Solved 150+ algorithmic problem challenges on LeetCode.
Education: B.Tech Computer Science (Final Year).
        """
    }

    st.divider()

    # =========================================================
    # Step 1: Input Candidate Resume & Target Role
    # =========================================================
    st.subheader("📄 1. Upload Resume or Load Profile (Zero Manual Sliders)")

    c_role, c_preset = st.columns([1.2, 1])

    with c_role:
        target_role = st.selectbox(
            "Target Job Role",
            roles,
            index=0,
            key="ml_role_select",
            help="The ML model will evaluate candidate attributes specifically against this role's hiring weights."
        )

    with c_preset:
        preset_choice = st.selectbox(
            "⚡ Quick Load Sample Resume",
            list(SAMPLE_CANDIDATES.keys()),
            index=1,
            key="ml_sample_preset"
        )

    # File Uploader or Text Area
    col_upload, col_text = st.columns(2)

    extracted_resume_text = ""

    with col_upload:
        uploaded_file = st.file_uploader(
            "Upload Resume (PDF / DOCX)",
            type=["pdf", "docx"],
            key="ml_resume_file"
        )
        if uploaded_file:
            with st.spinner("Extracting text from uploaded resume..."):
                extracted_resume_text = parser.extract_text(uploaded_file)
                st.success(f"✓ Extracted {len(extracted_resume_text.split())} words from `{uploaded_file.name}`")

    with col_text:
        default_preset_text = SAMPLE_CANDIDATES[preset_choice] if not extracted_resume_text else ""
        pasted_text = st.text_area(
            "Or Paste Resume / Candidate Profile Text:",
            value=default_preset_text,
            height=140,
            key="ml_pasted_text",
            placeholder="Paste candidate resume, experience, skills, and projects here..."
        )

    active_resume_text = extracted_resume_text or pasted_text or SAMPLE_CANDIDATES["👤 Sabir Shaik (AI / ML Engineer Resume)"]

    # Model Algorithm Choice
    comparison_df = predictor.train_models_for_role(target_role)

    col_algo, col_btn = st.columns([2, 1])
    with col_algo:
        model_choice = st.selectbox(
            "Machine Learning Inference Algorithm",
            comparison_df["Model Algorithm"].tolist(),
            index=0,
            key="ml_algo_choice"
        )

    # =========================================================
    # Step 2: Automatic Feature Extraction & ML Prediction
    # =========================================================
    # Extract features mathematically from resume text
    auto_features = predictor.extract_features_from_text(active_resume_text, target_role)
    feature_values = auto_features["feature_values"]
    feature_names = auto_features["feature_names"]

    # Run ML Inference
    pred_res = predictor.predict_candidate_score(
        role=target_role,
        feature_values=feature_values,
        model_name=model_choice
    )

    st.divider()

    # =========================================================
    # Step 3: Executive Scorecards & Live Results
    # =========================================================
    st.subheader(f"📊 ML Hiring Intelligence Scorecard: {target_role}")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Predicted Shortlist Score", f"{pred_res['hiring_score']}/100", pred_res['verdict_badge'])
    m2.metric("Extracted Experience", f"{auto_features['extracted_exp_years']} Yrs", "Auto-Detected")
    m3.metric("Matched Core Skills", f"{len(auto_features['matched_skills'])} Skills", f"{len(auto_features['missing_skills'])} missing")
    m4.metric("Inference Algorithm", model_choice.split()[0], "Supervised ML")

    st.progress(pred_res['hiring_score'] / 100.0)

    st.markdown(
        f"""
        <div style="background-color: #1E293B; padding: 14px; border-radius: 8px; margin: 15px 0; border-left: 5px solid {pred_res['status_color']};">
            <h4 style="color: {pred_res['status_color']}; margin: 0 0 5px 0;">Decision Verdict: {pred_res['verdict']}</h4>
            <p style="color: #94A3B8; font-size: 14px; margin: 0;">Automated prediction generated by {model_choice} without manual sliders.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # =========================================================
    # Step 4: Deep-Dive Analysis Tabs
    # =========================================================
    t1, t2, t3, t4, t5 = st.tabs([
        "📊 1. Extracted Radar & Features",
        "🔑 2. Skills Match & Missing Tags",
        "💡 3. Why is My Score Low? (Diagnosis)",
        "🚀 4. Score Booster Simulator (+25%)",
        "🛠️ 5. Recommended Projects to Add"
    ])

    # ---------------------------------------------------------
    # TAB 1: Radar & Feature Scores
    # ---------------------------------------------------------
    with t1:
        st.subheader("🎯 Auto-Calculated Competency Radar")
        st.caption("Feature scores calculated automatically from your uploaded resume:")

        col_r1, col_r2 = st.columns([1.2, 1])

        with col_r1:
            fig_radar = go.Figure()
            fig_radar.add_trace(go.Scatterpolar(
                r=feature_values,
                theta=feature_names,
                fill='toself',
                name='Extracted from Resume',
                line=dict(color='#38BDF8')
            ))
            fig_radar.add_trace(go.Scatterpolar(
                r=[85, 80, 80, 75, 75],
                theta=feature_names,
                fill='toself',
                name='Senior Benchmark (Top 5%)',
                line=dict(color='#10B981', dash='dot')
            ))
            fig_radar.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                template="plotly_dark",
                height=340,
                margin=dict(l=30, r=30, t=30, b=30),
                showlegend=True
            )
            st.plotly_chart(fig_radar, use_container_width=True)

        with col_r2:
            st.markdown("#### 📋 Extracted Feature Breakdown")
            for fb in pred_res["feature_breakdown"]:
                st.write(f"• **{fb['feature']}:** `{int(fb['score'])}/100` *(Importance: {fb['importance']})*")
                st.progress(fb['score'] / 100)

    # ---------------------------------------------------------
    # TAB 2: Skills Match
    # ---------------------------------------------------------
    with t2:
        st.subheader(f"🔑 Core Role Skills Analysis for {target_role}")

        sk_col1, sk_col2 = st.columns(2)
        with sk_col1:
            st.markdown("#### ✅ Matched Skills (Detected in Resume)")
            if auto_features["matched_skills"]:
                for s in auto_features["matched_skills"]:
                    st.success(f"✓ {s}")
            else:
                st.warning("No primary skills detected for this role.")

        with sk_col2:
            st.markdown("#### ❌ Missing Core Skills (Needed for Shortlist)")
            if auto_features["missing_skills"]:
                for s in auto_features["missing_skills"]:
                    st.error(f"+ {s}")
            else:
                st.success("All core role skills detected in resume!")

    # ---------------------------------------------------------
    # TAB 3: Why is My Score Low? (Explainable Diagnosis)
    # ---------------------------------------------------------
    with t3:
        st.subheader("💡 Why is Your Score at this Level? (Score Diagnosis)")
        st.markdown("Here is the exact mathematical breakdown of **why points were deducted** and **how to fix each item**:")

        for diag in pred_res.get("detailed_diagnostics", []):
            with st.container():
                if diag["type"] == "gap":
                    st.markdown(
                        f"""
                        <div style="background-color: #1E293B; padding: 14px; border-radius: 8px; margin-bottom: 12px; border-left: 4px solid #EF4444;">
                            <p style="color: #F8FAFC; margin: 0 0 6px 0; font-size: 15px;">{diag['reason']}</p>
                            <span style="color: #38BDF8; font-size: 14px;">{diag['fix']}</span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"""
                        <div style="background-color: #1E293B; padding: 14px; border-radius: 8px; margin-bottom: 12px; border-left: 4px solid #10B981;">
                            <p style="color: #F8FAFC; margin: 0 0 6px 0; font-size: 15px;">{diag['reason']}</p>
                            <span style="color: #94A3B8; font-size: 14px;">{diag['fix']}</span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

    # ---------------------------------------------------------
    # TAB 4: Score Booster Simulator
    # ---------------------------------------------------------
    with t4:
        st.subheader("🚀 Score Booster Simulator: How to Reach 90%+ Shortlist Score")
        st.markdown("See how making targeted improvements to your resume will mathematically boost your Machine Learning hiring probability:")

        b_c1, b_c2 = st.columns([1, 1.2])

        with b_c1:
            st.info(
                f"**CURRENT ML SCORE:**  \n# {pred_res['hiring_score']}/100 ({pred_res['verdict_badge']})  \n\n"
                f"**POTENTIAL PROJECTED SCORE:**  \n# {pred_res['total_potential_score']}/100 (🚀 Top Tier Shortlist!)"
            )

        with b_c2:
            st.markdown("#### 🎯 Impact of Individual Improvements:")
            for b in pred_res.get("boost_actions", []):
                st.success(f"**{b['action']}** ➔ *Gain: `{b['potential_gain']}` (Raises score to ~{b['projected_score']}%)*")

    # ---------------------------------------------------------
    # TAB 5: Recommended Projects to Add
    # ---------------------------------------------------------
    with t5:
        st.subheader(f"🛠️ Top 2 High-Impact Projects to Add for {target_role}")
        st.markdown(
            "Recruiters shortlisting for **" + target_role + "** want to see these exact project architectures on your resume:"
        )

        role_info_box = predictor.ROLE_BENCHMARKS.get(target_role, predictor.ROLE_BENCHMARKS["Software Engineer / Fresher"])

        st.info(
            f"📌 **Project 1: Production {target_role.split('/')[0].strip()} System**  \n"
            f"• **Tech Stack:** {', '.join(role_info_box['required_skills'][:5])}  \n"
            f"• **Key Architecture:** Containerized API microservice with sub-200ms response time and automated GitHub Actions CI/CD deployment."
        )

        st.info(
            f"📌 **Project 2: Scalable Real-Time Cloud Application**  \n"
            f"• **Tech Stack:** {', '.join(role_info_box['required_skills'][3:])}, Docker, Cloud (AWS)  \n"
            f"• **Key Architecture:** Cloud-hosted dashboard with database indexing, caching, and automated testing achieving 90%+ code coverage."
        )

    st.divider()
    st.markdown("#### 📊 Real-Time ML Model Benchmarks for this Role:")
    st.dataframe(comparison_df, use_container_width=True, hide_index=True)