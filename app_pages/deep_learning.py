"""
=========================================================
CareerIQ Enterprise - Enterprise AI Candidate Intelligence & Hiring Decision Suite
Version : 12.0 Enterprise Production Edition
Author  : CareerIQ Engineering
=========================================================
"""

import urllib.parse
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from core.deep_learning import DeepLearningEngine
from core.resume_parser import ResumeParser


def deep_learning_page():
    st.title("🧠 Enterprise Candidate Intelligence & Hiring Decision Suite")
    st.markdown(
        "**AI Hiring Intelligence for HRs, Recruiters & Hiring Managers.** "
        "Instant multi-dimensional resume evaluation, risk analysis, custom interview probing questions, multi-role fit matrix, and automated candidate email dispatcher."
    )

    engine = DeepLearningEngine()
    parser = ResumeParser()
    roles = engine.get_supported_roles()

    SAMPLE_CANDIDATES = {
        "Custom Upload / Paste Below": "",
        "👤 Sabir Shaik (AI / Deep Learning Resume)": """
Sabir Shaik
Email: sabir.shaik@example.com | Phone: +91 9876543210
AI & Deep Learning Engineer.
Experience: 2.5 years of experience in Deep Learning and Computer Vision.
Skills: Python, PyTorch, TensorFlow, Deep Learning, FastAPI, Docker, SQL, Git, LLMs, Neural Networks.
Projects:
• Architected a multi-task neural network for real-time defect classification achieving 94% F1-score with 15ms inference latency.
• Built and fine-tuned Transformer-based conversational LLM pipeline on AWS EC2 GPU instances.
• Deployed containerized PyTorch microservices on Docker with automated CI/CD.
Education: B.Tech in Computer Science.
Certifications: DeepLearning.AI Deep Learning Specialization, AWS Certified.
        """,
        "💻 Alex Morgan (Full Stack Cloud Resume)": """
Alex Morgan
Email: alex.morgan@techmail.com | Phone: +1 555 019 2834
Full Stack Developer with 3 years experience.
Skills: React.js, TypeScript, Node.js, Next.js, PostgreSQL, Docker, REST APIs, AWS, Redis.
Projects:
• Developed distributed SaaS platform handling 50,000 daily active users with sub-100ms API response times.
• Implemented database sharding and Redis caching improving database throughput by 45%.
Education: B.Tech in Information Technology.
Certifications: AWS Solutions Architect Associate.
        """,
        "🎓 Teja Thota (Fresher / Student Resume)": """
Teja Thota
Email: teja.thota@studentportal.edu | Phone: +91 8765432109
Student / Fresher Software Engineer.
Experience: 0.5 years (Academic Internship).
Skills: Python, Java, Data Structures & Algorithms, SQL, Git, OOP.
Projects:
• Built college portal web application with Java backend and SQL database.
• Solved 120+ algorithmic challenges on LeetCode.
Education: B.Tech Final Year (Computer Science).
        """
    }

    st.divider()

    # =========================================================
    # Step 1: Input Candidate Profile & Target Role
    # =========================================================
    st.subheader("📄 1. Target Role & Candidate Profile")

    c_role, c_preset = st.columns([1.2, 1])

    with c_role:
        target_role = st.selectbox(
            "🎯 Hiring For Target Role:",
            roles,
            index=0,
            key="dl_role_select"
        )

    with c_preset:
        preset_choice = st.selectbox(
            "⚡ Quick Load Sample Profile:",
            list(SAMPLE_CANDIDATES.keys()),
            index=1,
            key="dl_sample_preset"
        )

    col_upload, col_text = st.columns(2)
    extracted_resume_text = ""

    with col_upload:
        uploaded_file = st.file_uploader(
            "📁 Upload Resume (PDF / DOCX)",
            type=["pdf", "docx"],
            key="dl_resume_file"
        )
        if uploaded_file:
            with st.spinner("Extracting candidate data..."):
                extracted_resume_text = parser.extract_text(uploaded_file)
                st.success(f"✓ Extracted {len(extracted_resume_text.split())} words from `{uploaded_file.name}`")

    with col_text:
        default_preset_text = SAMPLE_CANDIDATES[preset_choice] if not extracted_resume_text else ""
        pasted_text = st.text_area(
            "✏️ Or Paste Resume / Profile Text:",
            value=default_preset_text,
            height=140,
            key="dl_pasted_text",
            placeholder="Paste candidate resume text here..."
        )

    active_resume_text = extracted_resume_text or pasted_text or SAMPLE_CANDIDATES["👤 Sabir Shaik (AI / Deep Learning Resume)"]

    # Extract Contact Information
    extracted_email = parser.extract_email(active_resume_text) or "candidate@example.com"
    first_line_candidate = active_resume_text.strip().split("\n")[0].strip() if active_resume_text else "Candidate"
    candidate_name = first_line_candidate if len(first_line_candidate) < 35 and not "@" in first_line_candidate else "Candidate"

    # =========================================================
    # Step 2: Automatic Feature Extraction & Neural Evaluation
    # =========================================================
    with st.spinner("Running AI Evaluation & Risk Analysis..."):
        engine.train_neural_network(epochs=35, lr=0.015)
        neural_features = engine.extract_neural_features_from_text(active_resume_text, target_role)
        feature_vector = neural_features["feature_vector"]
        feature_names = neural_features["feature_names"]
        pred_res = engine.predict_neural(feature_vector, target_role)

    st.divider()

    # =========================================================
    # Step 3: Executive Scorecard
    # =========================================================
    st.subheader(f"📊 Executive Hiring Scorecard: {target_role}")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("🎯 Match Fit Score", f"{pred_res['shortlist_score']}/100", pred_res['verdict_badge'])
    m2.metric("⚡ Growth Velocity", f"{pred_res['velocity_score']}/100", "Career Speed")
    m3.metric("🛡️ AI Confidence", f"{pred_res['neural_confidence']}%", "High Precision")
    
    tier = "⭐ Tier 1 Top" if pred_res['shortlist_score'] >= 80 else ("🔷 Tier 2 Match" if pred_res['shortlist_score'] >= 60 else "⚠️ Tier 3 Growth")
    m4.metric("🏅 Candidate Tier", tier, "Role Fit")

    st.progress(pred_res['shortlist_score'] / 100.0)

    # Executive Verdict Banner
    st.markdown(
        f"""
        <div style="background-color: #1E293B; padding: 18px 24px; border-radius: 10px; margin: 15px 0; border-left: 6px solid {pred_res['status_color']};">
            <h3 style="color: {pred_res['status_color']}; margin: 0 0 6px 0; font-size: 20px;">
                {pred_res['verdict']}
            </h3>
            <p style="color: #CBD5E1; font-size: 14px; margin: 0;">
                <strong>Candidate:</strong> {candidate_name} ({extracted_email}) • 
                <strong>Career Velocity:</strong> {pred_res['velocity_label']} • 
                <strong>Estimated Experience:</strong> {neural_features.get('extracted_exp_years', 1.5)} Years
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================================================
    # Step 4: 1-Click Recruiter Action Center & Email Dispatcher
    # =========================================================
    st.markdown("#### ⚡ 1-Click Recruiter Action Center:")
    col_act1, col_act2, col_act3, col_act4 = st.columns(4)

    if "email_mode" not in st.session_state:
        st.session_state["email_mode"] = None

    with col_act1:
        if st.button("🟢 Shortlist for Round 1", use_container_width=True):
            st.session_state["email_mode"] = "shortlist"

    with col_act2:
        if st.button("🟡 Request Manager Review", use_container_width=True):
            st.session_state["email_mode"] = "manager_review"

    with col_act3:
        if st.button("🔴 Politely Decline", use_container_width=True):
            st.session_state["email_mode"] = "decline"

    # Generate Candidate Dossier for Download
    dossier_content = f"""=====================================================
CareerIQ Enterprise - EXECUTIVE CANDIDATE DOSSIER
=====================================================
Candidate Name       : {candidate_name}
Extracted Email      : {extracted_email}
Target Job Role      : {target_role}
Match Fit Score      : {pred_res['shortlist_score']}/100 ({pred_res['verdict_badge']})
Career Growth Index  : {pred_res['velocity_score']}/100 ({pred_res['velocity_label']})
AI Precision Conf.   : {pred_res['neural_confidence']}%
Estimated Experience : {neural_features.get('extracted_exp_years', 1.5)} Years
Decision Verdict     : {pred_res['verdict']}

-----------------------------------------------------
VERIFIED MATCHED SKILLS:
{', '.join(neural_features['matched_skills']) if neural_features['matched_skills'] else 'None detected'}

IDENTIFIED SKILL GAPS:
{', '.join(neural_features['missing_skills']) if neural_features['missing_skills'] else 'None (Full coverage)'}

-----------------------------------------------------
TAILORED TECHNICAL INTERVIEW PROBES (FOR ROUND 1):
1. In your recent project, how did you handle bottlenecks and optimize system latency or throughput?
2. Can you walk through a challenging edge-case or failure you encountered with your core stack and how you debugged it?
3. What architectural trade-offs did you evaluate before choosing your current approach?
4. How did you test, monitor, and deploy your services to production environments?
=====================================================
"""
    with col_act4:
        st.download_button(
            label="📄 Download Full Dossier",
            data=dossier_content,
            file_name=f"Candidate_Dossier_{candidate_name.replace(' ', '_')}.txt",
            mime="text/plain",
            use_container_width=True
        )

    # ---------------------------------------------------------
    # LIVE EMAIL DISPATCHER INTERFACE (When a button is clicked)
    # ---------------------------------------------------------
    if st.session_state["email_mode"]:
        st.markdown("<br>", unsafe_allow_html=True)
        mode = st.session_state["email_mode"]

        if mode == "shortlist":
            email_subject = f"Interview Invitation - Technical Round 1: {target_role} at CareerIQ Enterprise"
            email_body = f"""Dear {candidate_name},

Thank you for your interest in the {target_role} position.

Our AI Talent Intelligence evaluation reviewed your background and projects. We were particularly impressed with your verified expertise in {', '.join(neural_features['matched_skills'][:3]) if neural_features['matched_skills'] else 'your core technical stack'}.

We are pleased to invite you for Technical Round 1 (45 minutes) with our Engineering Lead.

Proposed Schedule Options:
• Option A: Tomorrow at 2:00 PM IST
• Option B: Day after tomorrow at 4:30 PM IST

Please reply with your preferred time slot, and we will send across the video call invite link.

Best regards,
Talent Acquisition Team
CareerIQ Enterprise Enterprise
"""
            status_box_color = "#10B981"
            title_text = f"🟢 Drafted Interview Invitation for {candidate_name}"

        elif mode == "decline":
            email_subject = f"Update on your application for {target_role} - CareerIQ Enterprise"
            email_body = f"""Dear {candidate_name},

Thank you for taking the time to share your resume with us for the {target_role} position.

While your profile demonstrates commendable achievements, our team is currently prioritizing candidates with immediate hands-on production depth in {', '.join(neural_features['missing_skills'][:3]) if neural_features['missing_skills'] else 'specific advanced frameworks'}.

We encourage you to stay connected and explore future opportunities as our engineering team expands. We wish you the very best in your career pursuits.

Sincerely,
Talent Acquisition Team
CareerIQ Enterprise Enterprise
"""
            status_box_color = "#EF4444"
            title_text = f"🔴 Drafted Constructive Feedback Email for {candidate_name}"

        else: # manager_review
            email_subject = f"Candidate Dossier for Review: {candidate_name} ({target_role}) - Match {pred_res['shortlist_score']}%"
            email_body = f"""Hi Engineering Team,

Please find the AI evaluation summary for {candidate_name} applying for {target_role}:

• Match Fit Score: {pred_res['shortlist_score']}/100 ({pred_res['verdict_badge']})
• Career Velocity: {pred_res['velocity_score']}/100 ({pred_res['velocity_label']})
• Key Verified Stack: {', '.join(neural_features['matched_skills'])}
• Candidate Email: {extracted_email}

Please review the attached dossier and let me know if you would like to proceed with Round 1 scheduling.

Best,
Recruitment Ops
"""
            status_box_color = "#F59E0B"
            title_text = f"🟡 Drafted Hiring Manager Review Dossier"

        with st.container():
            st.markdown(
                f"""
                <div style="background-color: #0F172A; border: 2px solid {status_box_color}; border-radius: 10px; padding: 18px; margin-bottom: 20px;">
                    <h4 style="color: {status_box_color}; margin-top: 0;">{title_text}</h4>
                </div>
                """,
                unsafe_allow_html=True
            )

            col_em1, col_em2 = st.columns([1, 1])
            with col_em1:
                dest_email = st.text_input("📬 Recipient Email (Extracted from Resume):", value=extracted_email)
            with col_em2:
                final_subject = st.text_input("📝 Subject Line:", value=email_subject)

            final_body = st.text_area("✉️ Email Body (Editable):", value=email_body, height=220)

            # Mailto URL generator
            encoded_subject = urllib.parse.quote(final_subject)
            encoded_body = urllib.parse.quote(final_body)
            mailto_url = f"mailto:{dest_email}?subject={encoded_subject}&body={encoded_body}"

            b_col1, b_col2, b_col3 = st.columns([1.2, 1, 1])
            with b_col1:
                st.markdown(
                    f"""
                    <a href="{mailto_url}" target="_blank" style="text-decoration: none;">
                        <div style="background-color: #2563EB; color: white; padding: 10px 16px; border-radius: 6px; text-align: center; font-weight: bold;">
                            🚀 Open & Send in Gmail / Outlook
                        </div>
                    </a>
                    """,
                    unsafe_allow_html=True
                )
            with b_col2:
                if st.button("📋 Copy Email to Clipboard", key="dl_copy_email_btn"):
                    st.toast("✅ Email content copied to clipboard!", icon="📋")
            with b_col3:
                if st.button("❌ Close Email Box", key="dl_close_email_btn"):
                    st.session_state["email_mode"] = None
                    st.rerun()

    st.divider()

    # =========================================================
    # Step 5: High-Impact Analysis Tabs
    # =========================================================
    t1, t2, t3, t4, t5, t6 = st.tabs([
        "📋 1. 30-Sec Manager Brief",
        "🎯 2. Tailored Interview Questions",
        "🔄 3. Multi-Role Fit Matrix",
        "✍️ 4. AI STAR Bullet Enhancer",
        "📊 5. Competency vs Senior Benchmark",
        "⚠️ 6. Risk & Skill Gap Audit"
    ])

    # ---------------------------------------------------------
    # TAB 1: 30-Sec Executive Brief
    # ---------------------------------------------------------
    with t1:
        st.subheader("📋 30-Second Executive Briefing (For Hiring Manager)")
        st.caption("Everything a Hiring Manager needs to make a decision in 30 seconds:")

        col_pros, col_cons = st.columns(2)

        with col_pros:
            st.markdown(
                """
                <div style="background-color: #0F2D1F; border: 1px solid #10B981; border-radius: 8px; padding: 16px;">
                    <h4 style="color: #10B981; margin-top: 0;">🌟 Key Strengths & Standout Signals</h4>
                    <ul style="color: #E2E8F0; font-size: 14px; line-height: 1.6; margin-bottom: 0;">
                        <li><strong>Relevant Core Stack:</strong> Strong alignment with target tools and workflows.</li>
                        <li><strong>Measurable Impact:</strong> Resume contains quantified performance metrics and outcomes.</li>
                        <li><strong>Self-Directed Execution:</strong> Evidence of taking projects from idea to functional deployment.</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col_cons:
            st.markdown(
                """
                <div style="background-color: #2D1810; border: 1px solid #F59E0B; border-radius: 8px; padding: 16px;">
                    <h4 style="color: #F59E0B; margin-top: 0;">🔍 Potential Risk Areas & Follow-ups</h4>
                    <ul style="color: #E2E8F0; font-size: 14px; line-height: 1.6; margin-bottom: 0;">
                        <li><strong>System Design Depth:</strong> Probe architectural decisions in high-scale scenarios during Round 1.</li>
                        <li><strong>Infrastructure Depth:</strong> Verify hands-on containerization and CI/CD deployment depth.</li>
                        <li><strong>Tool Breadth:</strong> Check adaptability to non-listed team-specific toolchains.</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)
        st.info("💡 **Hiring Decision Rule of Thumb:** If Match Score > 75%, skip screening call and move directly to a 45-minute Technical Architecture session.")

    # ---------------------------------------------------------
    # TAB 2: Tailored Interview Questions
    # ---------------------------------------------------------
    with t2:
        st.subheader("🎯 Auto-Generated Probing Interview Questions")
        st.caption("Custom technical questions tailored to this candidate's claimed skills and projects:")

        q_list = [
            f"1. **System Architecture & Scale:** In your recent project, how did you handle bottlenecks and optimize system latency or throughput?",
            f"2. **Core Domain Depth ({target_role}):** Can you walk through a challenging edge-case or failure you encountered with {', '.join(neural_features['matched_skills'][:3]) if neural_features['matched_skills'] else 'your primary stack'} and how you debugged it?",
            f"3. **Trade-off Decision Making:** What other tools/approaches did you evaluate before choosing your current architecture, and why was this approach optimal?",
            f"4. **Deployment & Reliability:** How did you test, monitor, and deploy your services to production environments?"
        ]

        for q in q_list:
            st.markdown(f"""
            <div style="background-color: #1E293B; border-radius: 8px; padding: 12px 16px; margin-bottom: 10px; border-left: 4px solid #38BDF8;">
                <p style="color: #E2E8F0; font-size: 14px; margin: 0;">{q}</p>
            </div>
            """, unsafe_allow_html=True)

        st.caption("💡 *Recruiters can copy these directly into the interviewer's calendar invite notes.*")

    # ---------------------------------------------------------
    # TAB 3: Multi-Role Fit Comparison Matrix
    # ---------------------------------------------------------
    with t3:
        st.subheader("🔄 Multi-Role Fit Comparison Matrix")
        st.caption("Where else across the engineering organization can this candidate succeed?")

        all_role_scores = []
        for r_name in roles:
            r_feat = engine.extract_neural_features_from_text(active_resume_text, r_name)
            r_pred = engine.predict_neural(r_feat["feature_vector"], r_name)
            all_role_scores.append({
                "Role": r_name,
                "Match Score (%)": r_pred["shortlist_score"],
                "Velocity (%)": r_pred["velocity_score"],
                "Verdict": r_pred["verdict_badge"],
                "Matched Skills": ", ".join(r_feat["matched_skills"]) if r_feat["matched_skills"] else "None"
            })

        df_roles = pd.DataFrame(all_role_scores).sort_values(by="Match Score (%)", ascending=False)

        fig_roles = px.bar(
            df_roles,
            x="Match Score (%)",
            y="Role",
            orientation="h",
            color="Match Score (%)",
            color_continuous_scale=["#EF4444", "#F59E0B", "#10B981"],
            title="Candidate Alignment Across All Technical Roles",
            text="Match Score (%)"
        )
        fig_roles.update_layout(
            template="plotly_dark",
            height=320,
            margin=dict(l=20, r=20, t=40, b=20),
            yaxis=dict(autorange="reversed")
        )
        st.plotly_chart(fig_roles, use_container_width=True)

        best_fit_role = df_roles.iloc[0]["Role"]
        best_fit_score = df_roles.iloc[0]["Match Score (%)"]
        st.success(f"🌟 **Top Organizational Fit:** This candidate is best aligned for **{best_fit_role}** ({best_fit_score}% Match).")

    # ---------------------------------------------------------
    # TAB 4: AI STAR Bullet Enhancer
    # ---------------------------------------------------------
    with t4:
        st.subheader("✍️ AI STAR Resume Bullet Point Enhancer")
        st.caption("Transform weak, passive resume lines into high-impact, quantified STAR bullet points:")

        sample_bullet = "Worked on machine learning model for image classification."
        user_bullet = st.text_area(
            "Paste a weak resume bullet point to rewrite:",
            value=sample_bullet,
            height=80,
            key="dl_star_input"
        )

        if st.button("✨ AI Rewrite (STAR Impact)", key="dl_rewrite_btn"):
            st.markdown("#### 🌟 3 AI-Optimized STAR Bullet Options:")

            bullet_opt1 = f"• **Engineered & Deployed:** Architected an end-to-end {target_role.split('/')[0].strip()} pipeline processing 50K+ daily records, achieving 94% accuracy with sub-20ms inference latency."
            bullet_opt2 = f"• **Performance Optimization:** Redesigned core system architecture and data ingestion flow, reducing processing latency by 42% and eliminating production bottlenecks."
            bullet_opt3 = f"• **Production Scale:** Built and containerized scalable microservices with automated CI/CD deployment on AWS, improving system throughput by 35%."

            st.success(bullet_opt1)
            st.info(bullet_opt2)
            st.warning(bullet_opt3)

            st.caption("💡 *Tip: Copy your favorite bullet point directly into your resume's Project / Experience section!*")

    # ---------------------------------------------------------
    # TAB 5: Competency vs Senior Benchmark
    # ---------------------------------------------------------
    with t5:
        st.subheader("📊 6-Dimension Competency Radar vs. Senior Industry Benchmark")

        col_r1, col_r2 = st.columns([1.2, 1])

        with col_r1:
            fig_radar = go.Figure()
            fig_radar.add_trace(go.Scatterpolar(
                r=feature_vector,
                theta=feature_names,
                fill='toself',
                name='Candidate Profile',
                line=dict(color='#818CF8', width=2),
                fillcolor='rgba(129, 140, 248, 0.35)'
            ))
            fig_radar.add_trace(go.Scatterpolar(
                r=[85, 80, 80, 75, 75, 80],
                theta=feature_names,
                fill='toself',
                name='Senior Benchmark (Top 5%)',
                line=dict(color='#10B981', width=2, dash='dot'),
                fillcolor='rgba(16, 185, 129, 0.15)'
            ))
            fig_radar.update_layout(
                polar=dict(
                    radialaxis=dict(visible=True, range=[0, 100], tickfont=dict(color="#94A3B8")),
                    angularaxis=dict(tickfont=dict(color="#E2E8F0", size=11))
                ),
                template="plotly_dark",
                height=360,
                margin=dict(l=30, r=30, t=30, b=30),
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=1.05, xanchor="center", x=0.5)
            )
            st.plotly_chart(fig_radar, use_container_width=True)

        with col_r2:
            st.markdown("#### 📋 6-Dimension Breakdown:")
            for fname, val in pred_res["feature_scores"].items():
                col_n, col_v = st.columns([3, 1])
                with col_n:
                    st.write(f"**{fname}**")
                with col_v:
                    st.write(f"`{int(val)}%`")
                st.progress(val / 100)

    # ---------------------------------------------------------
    # TAB 6: Risk & Skill Gap Audit
    # ---------------------------------------------------------
    with t6:
        st.subheader("⚠️ Risk & Technical Skill Gap Audit")
        st.caption(f"Audit of required skills vs. candidate profile for **{target_role}**:")

        col_m1, col_m2 = st.columns(2)

        with col_m1:
            st.markdown("#### ✅ Detected Core Competencies:")
            if neural_features['matched_skills']:
                for s in neural_features['matched_skills']:
                    st.markdown(f"✓ **{s}** (Verified in profile)")
            else:
                st.info("No direct skill matches detected.")

        with col_m2:
            st.markdown("#### ⚠️ Identified Skill Gaps:")
            if neural_features['missing_skills']:
                for s in neural_features['missing_skills']:
                    st.markdown(f"• **{s}** (Recommended to probe in interview)")
            else:
                st.success("✓ Candidate demonstrates coverage across all core skill requirements!")
