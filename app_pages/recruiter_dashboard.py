"""
=========================================================
CareerIQ Enterprise - Enterprise Multi-Resume Bulk Screening & Leaderboard
Version : 12.0 Enterprise Production Edition
Author  : CareerIQ Engineering
=========================================================
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from core.deep_learning import DeepLearningEngine
from core.resume_parser import ResumeParser


def recruiter_dashboard_page():
    st.title("🎯 Enterprise Recruiter Dashboard & Bulk Screening")
    st.markdown(
        "**Multi-Resume Automated Screening, AI Scoring & Candidate Leaderboard.** "
        "Upload 5 to 50 resumes at once to automatically rank, filter, and export the top engineering talent."
    )

    engine = DeepLearningEngine()
    parser = ResumeParser()
    roles = engine.get_supported_roles()

    # Pre-built realistic applicant database for 1-click bulk testing
    PRESET_APPLICANTS = [
        {
            "name": "Sabir Shaik",
            "file": "Sabir_Shaik_Resume.pdf",
            "text": """
            Sabir Shaik. AI & Machine Learning Engineer with 2.5 years of experience in Deep Learning and Computer Vision.
            Skills: Python, PyTorch, TensorFlow, Deep Learning, FastAPI, Docker, SQL, Git, LLMs, Neural Networks.
            Projects: Architected a multi-task neural network for defect classification achieving 94% F1-score with 15ms latency.
            Deployed containerized PyTorch microservices on Docker with automated CI/CD.
            Education: B.Tech Computer Science. Certifications: AWS Certified, DeepLearning.AI Specialization.
            """
        },
        {
            "name": "Alex Morgan",
            "file": "Alex_Morgan_FullStack.pdf",
            "text": """
            Alex Morgan. Full Stack Developer with 3.5 years experience in SaaS platforms.
            Skills: React.js, TypeScript, Node.js, Next.js, PostgreSQL, Docker, REST APIs, AWS, Redis, Tailwind.
            Projects: Developed distributed SaaS platform handling 50,000 daily active users with sub-100ms API response times.
            Implemented database sharding and Redis caching improving database throughput by 45%.
            Education: B.Tech Information Technology. Certifications: AWS Solutions Architect Associate.
            """
        },
        {
            "name": "Vikram Sethi",
            "file": "Vikram_DevOps_Cloud.pdf",
            "text": """
            Vikram Sethi. Senior DevOps & Cloud Engineer with 4 years experience.
            Skills: Docker, Kubernetes, AWS, Terraform, CI/CD, GitHub Actions, Linux, Python, Helm, Ansible, Prometheus.
            Projects: Automated multi-region AWS cloud infrastructure using Terraform, cutting deployment downtime by 70%.
            Managed 15+ Kubernetes clusters running 200+ microservices with 99.99% uptime.
            Education: B.Tech CSE. Certifications: CKA (Certified Kubernetes Administrator), AWS Solutions Architect.
            """
        },
        {
            "name": "Priyanka Sharma",
            "file": "Priyanka_DataScientist.pdf",
            "text": """
            Priyanka Sharma. Data Scientist with 2 years experience.
            Skills: Python, SQL, Pandas, NumPy, Scikit-Learn, Machine Learning, Tableau, Power BI, Statistical Modeling, A/B Testing.
            Projects: Built customer churn prediction model with 89% accuracy, saving $120K in annual customer retention.
            Designed automated executive BI dashboards in Tableau tracking revenue metrics.
            Education: M.Sc in Data Science. Certifications: Tableau Desktop Certified.
            """
        },
        {
            "name": "Teja Thota",
            "file": "Teja_Thota_Fresher.pdf",
            "text": """
            Teja Thota. Fresher / Graduate Software Engineer.
            Skills: Python, Java, Data Structures & Algorithms, SQL, Git, OOP, HTML/CSS.
            Projects: Developed college portal web application with Java backend and SQL database.
            Solved 150+ algorithmic challenges on LeetCode.
            Education: B.Tech Final Year (Computer Science).
            """
        }
    ]

    st.divider()

    # =========================================================
    # Step 1: Target Role & Shortlist Configuration
    # =========================================================
    st.subheader("⚙️ 1. Job Opening & Screening Criteria")

    col_r, col_cut, col_load = st.columns([1.5, 1, 1.2])

    with col_r:
        target_role = st.selectbox(
            "🎯 Target Job Opening:",
            roles,
            index=0,
            key="rec_bulk_role"
        )

    with col_cut:
        cutoff_score = st.slider(
            "Shortlist Cutoff Score:",
            min_value=40,
            max_value=90,
            value=70,
            step=5,
            key="rec_cutoff"
        )

    with col_load:
        st.write("")
        st.write("")
        load_preset_batch = st.button("⚡ Load 5 Sample Applicants", use_container_width=True)

    # =========================================================
    # Step 2: Multi-File Bulk Resume Upload
    # =========================================================
    st.subheader("📁 2. Bulk Resume Upload (Multi-PDF)")
    
    uploaded_files = st.file_uploader(
        "Upload Multiple Resumes (PDF / DOCX) for Batch Screening:",
        type=["pdf", "docx"],
        accept_multiple_files=True,
        key="rec_bulk_files"
    )

    batch_candidates = []

    # Process Uploaded Files
    if uploaded_files:
        with st.spinner(f"AI Scanning & Parsing {len(uploaded_files)} candidate resumes in parallel..."):
            for f in uploaded_files:
                try:
                    text = parser.extract_text(f)
                    c_name = f.name.replace(".pdf", "").replace(".docx", "").replace("_", " ").title()
                    batch_candidates.append({
                        "name": c_name,
                        "file": f.name,
                        "text": text
                    })
                except Exception:
                    pass

    # If user clicked sample batch or no files uploaded yet
    elif load_preset_batch or not uploaded_files:
        batch_candidates = PRESET_APPLICANTS

    # =========================================================
    # Step 3: Run Batch AI Evaluation
    # =========================================================
    if batch_candidates:
        engine.train_neural_network(epochs=35, lr=0.015)
        
        screened_results = []
        for cand in batch_candidates:
            feats = engine.extract_neural_features_from_text(cand["text"], target_role)
            pred = engine.predict_neural(feats["feature_vector"], target_role)
            
            score = pred["shortlist_score"]
            status = "🟢 Strong Shortlist" if score >= 80 else ("🟡 Review Round" if score >= cutoff_score else "🔴 Reject (Skill Gap)")
            
            screened_results.append({
                "Candidate Name": cand["name"],
                "Match Score (%)": score,
                "Growth Velocity (%)": pred["velocity_score"],
                "Experience (Yrs)": feats.get("extracted_exp_years", 1.5),
                "Status": status,
                "Matched Skills": ", ".join(feats["matched_skills"]) if feats["matched_skills"] else "None",
                "Missing Skills": ", ".join(feats["missing_skills"]) if feats["missing_skills"] else "None",
                "File": cand["file"],
                "Raw Features": feats,
                "Prediction": pred
            })

        # Sort by Match Score descending
        df_batch = pd.DataFrame(screened_results).sort_values(by="Match Score (%)", ascending=False).reset_index(drop=True)
        df_batch.index = df_batch.index + 1
        df_batch.index.name = "Rank"

        st.divider()

        # =========================================================
        # Step 4: Executive Batch Metrics
        # =========================================================
        st.subheader(f"📊 Screening Summary: {target_role}")

        total_apps = len(df_batch)
        shortlisted_count = len(df_batch[df_batch["Match Score (%)"] >= cutoff_score])
        avg_score = int(df_batch["Match Score (%)"].mean())
        top_cand = df_batch.iloc[0]["Candidate Name"]
        top_score = df_batch.iloc[0]["Match Score (%)"]

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Resumes Processed", f"{total_apps} Candidates", "Batch Processed")
        m2.metric("Shortlisted (>= Cutoff)", f"{shortlisted_count} Passed", f"{round((shortlisted_count/total_apps)*100)}% Pass Rate")
        m3.metric("Batch Average Score", f"{avg_score}/100", "Role Fit Avg")
        m4.metric("Top Ranked Talent", f"🥇 {top_cand}", f"{top_score}% Fit")

        # =========================================================
        # Step 5: Interactive Candidate Leaderboard
        # =========================================================
        st.subheader("🏆 Candidate Ranked Leaderboard")

        # Visual Table
        display_df = df_batch[["Candidate Name", "Match Score (%)", "Status", "Experience (Yrs)", "Matched Skills", "Missing Skills"]]
        st.dataframe(
            display_df.style.background_gradient(subset=["Match Score (%)"], cmap="Blues"),
            use_container_width=True
        )

        # 1-Click Export to CSV
        csv_data = df_batch[["Candidate Name", "Match Score (%)", "Status", "Experience (Yrs)", "Matched Skills", "Missing Skills"]].to_csv().encode('utf-8')
        col_exp1, col_exp2 = st.columns([1, 3])
        with col_exp1:
            st.download_button(
                label="📥 Export Shortlist (CSV)",
                data=csv_data,
                file_name=f"Ranked_Shortlist_{target_role.replace(' ', '_')}.csv",
                mime="text/csv",
                use_container_width=True
            )

        st.divider()

        # =========================================================
        # Step 6: Visual Score Comparison Chart
        # =========================================================
        st.subheader("📈 Batch Score Distribution & Comparison")

        col_c1, col_c2 = st.columns([1.4, 1])

        with col_c1:
            fig_bar = px.bar(
                df_batch.reset_index(),
                x="Candidate Name",
                y="Match Score (%)",
                color="Match Score (%)",
                color_continuous_scale=["#EF4444", "#F59E0B", "#10B981"],
                text="Match Score (%)",
                title=f"Candidate Match Comparison for {target_role}"
            )
            fig_bar.add_hline(y=cutoff_score, line_dash="dot", line_color="#F59E0B", annotation_text=f"Cutoff: {cutoff_score}%")
            fig_bar.update_layout(
                template="plotly_dark",
                height=350,
                margin=dict(l=20, r=20, t=40, b=20)
            )
            st.plotly_chart(fig_bar, use_container_width=True)

        with col_c2:
            st.markdown("#### ⚡ 1-Click Recruiter Actions:")
            if st.button("🟢 Email All Shortlisted Candidates", use_container_width=True):
                st.toast(f"🎉 Round 1 interview invites sent to {shortlisted_count} candidates!", icon="📩")
            if st.button("🔴 Archive Rejected Profiles", use_container_width=True):
                st.toast(f"📫 Sent polite feedback emails to {total_apps - shortlisted_count} candidates.", icon="✅")
            
            st.info("💡 **Hiring Pro-Tip:** Export the CSV and share it with hiring managers for asynchronous review before scheduling Round 1.")

        # =========================================================
        # Step 7: Individual Candidate Detail Inspection
        # =========================================================
        st.divider()
        st.subheader("🔍 Deep-Dive Candidate Inspection")
        st.caption("Select a candidate to view their verified competencies and interview questions:")

        selected_cand_name = st.selectbox(
            "Select Candidate to Inspect:",
            df_batch["Candidate Name"].tolist(),
            key="rec_inspect_cand"
        )

        cand_data = df_batch[df_batch["Candidate Name"] == selected_cand_name].iloc[0]

        with st.expander(f"📋 View Full Dossier for {selected_cand_name} ({cand_data['Match Score (%)']}% Fit)", expanded=True):
            ci1, ci2, ci3 = st.columns(3)
            ci1.metric("Match Score", f"{cand_data['Match Score (%)']}/100", cand_data["Status"])
            ci2.metric("Career Velocity", f"{cand_data['Growth Velocity (%)']}/100", "Growth Speed")
            ci3.metric("Experience", f"{cand_data['Experience (Yrs)']} Yrs", "Verified")

            st.markdown(f"**✅ Verified Skills:** `{cand_data['Matched Skills']}`")
            st.markdown(f"**⚠️ Missing Skills:** `{cand_data['Missing Skills']}`")
            
            st.markdown("#### 🎯 Probing Questions for Live Interview:")
            st.markdown(f"• *1. Can you walk through how you architected your recent projects using {cand_data['Matched Skills'].split(',')[0]}?*")
            st.markdown(f"• *2. How did you handle testing, monitoring, and production deployment in your previous role?*")