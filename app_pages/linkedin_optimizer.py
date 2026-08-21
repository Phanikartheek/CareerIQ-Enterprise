"""
=========================================================
CareerIQ Enterprise - Enterprise LinkedIn Profile Optimizer
Version : 12.0 Enterprise Production Edition
Author  : CareerIQ Engineering
=========================================================
"""

import streamlit as st
import plotly.graph_objects as go
import re
from core.linkedin_optimizer import LinkedInOptimizer


def linkedin_optimizer_page():
    st.title("👤 Enterprise LinkedIn Profile Optimizer & Recruiter Intelligence")
    st.markdown(
        "Analyze any candidate's **actual LinkedIn profile** against **Recruiter Search Algorithms** & **Target Role Benchmarks**. "
        "Get explainable, section-by-section optimizations to dramatically boost inbound recruiter outreach."
    )

    optimizer = LinkedInOptimizer()

    # Pre-packaged verified test profiles for easy review & testing
    SAMPLE_PROFILES = {
        "Custom / Enter Any URL": {
            "headline": "",
            "about": "",
            "skills": "",
            "experience_title": "",
            "experience_company": "",
            "experience_desc": "",
            "years_exp": 1.0
        },
        "👤 Sabir Shaik (AI / ML Engineer)": {
            "url": "https://www.linkedin.com/in/sabir-shaik-0b5832235/",
            "headline": "AI & Machine Learning Engineer | Python, PyTorch, FastAPI, NLP",
            "about": "Aspiring AI Engineer with hands-on experience building neural networks, predictive models, and microservice APIs. Passionate about machine learning pipelines and deep learning.",
            "skills": "Python, Machine Learning, Deep Learning, PyTorch, FastAPI, scikit-learn, Docker, SQL, Git",
            "experience_title": "AI Intern",
            "experience_company": "Tech Innovations Lab",
            "experience_desc": "Built machine learning classification models using scikit-learn and deployed REST APIs with FastAPI.",
            "years_exp": 1.5,
            "role": "AI / Machine Learning Engineer"
        },
        "💻 Alex Morgan (Full Stack Developer)": {
            "url": "https://www.linkedin.com/in/alex-morgan-dev/",
            "headline": "Full Stack Developer | React.js, Node.js, TypeScript, PostgreSQL",
            "about": "Full Stack Engineer experienced in designing end-to-end web applications, responsive user interfaces, and scalable backend services with PostgreSQL and Express.",
            "skills": "JavaScript, TypeScript, React.js, Node.js, Express.js, PostgreSQL, REST APIs, Git, Tailwind CSS",
            "experience_title": "Software Developer",
            "experience_company": "CloudScale Solutions",
            "experience_desc": "Developed customer dashboards using React and Express.js with PostgreSQL backend.",
            "years_exp": 2.5,
            "role": "Full Stack Developer"
        },
        "🎓 Teja Thota (Fresher / Software Engineer - Weak Buzzwords)": {
            "url": "https://www.linkedin.com/in/teja-thota-87825b389/",
            "headline": "Hardworking Student @ ABC College | Seeking opportunities | Quick learner",
            "about": "I am a hardworking, passionate, and detail-oriented computer science student looking for immediate opportunities. Team player with great problem solving mindset.",
            "skills": "Java, Python, C++, HTML/CSS, Problem Solving",
            "experience_title": "Academic Project Lead",
            "experience_company": "University Project",
            "experience_desc": "Worked on college management web application using Java and HTML.",
            "years_exp": 0.5,
            "role": "Software Engineer / Fresher"
        }
    }

    st.divider()

    # =========================================================
    # Step 1: Input Profile URL & Role Selection
    # =========================================================
    st.subheader("🔗 1. LinkedIn Profile & Role Configuration")

    col_url, col_role = st.columns([2, 1])

    with col_url:
        linkedin_url = st.text_input(
            "Enter Any LinkedIn Profile URL or Username",
            value="https://www.linkedin.com/in/phanikartheek",
            placeholder="e.g. https://www.linkedin.com/in/username/ or username",
            key="li_profile_url",
            help="Paste any developer, student, or professional's LinkedIn URL (e.g. linkedin.com/in/name or in.linkedin.com/in/name)"
        )

    # Validate URL robustly
    url_validation = optimizer.validate_linkedin_url(linkedin_url)
    extracted_name = optimizer.parse_name_from_url(linkedin_url) if url_validation["valid"] else "Candidate"

    # Detect if URL changed to automatically refresh candidate state
    if "last_li_url" not in st.session_state or st.session_state["last_li_url"] != linkedin_url:
        st.session_state["last_li_url"] = linkedin_url
        st.session_state["li_inp_name"] = extracted_name
        # Clear previous custom text inputs so the new candidate gets fresh dynamic analysis
        for k in ["li_inp_hl", "li_inp_about", "li_inp_skills", "li_inp_exp_title", "li_inp_exp_comp", "li_inp_exp_desc"]:
            if k in st.session_state:
                del st.session_state[k]

    with col_role:
        target_role = st.selectbox(
            "Target Industry Domain / Role",
            list(optimizer.ROLE_DATA.keys()),
            index=0,
            key="li_target_role"
        )

    # Status indicator
    if url_validation["valid"]:
        st.success(f"✅ **Recognized Candidate:** {extracted_name} (`{url_validation['normalized_url']}`)")
    else:
        st.error(f"❌ {url_validation.get('message', 'Please enter a valid LinkedIn URL')}")

    # Optional preset loader or manual customization
    col_opt1, col_opt2 = st.columns(2)
    with col_opt1:
        with st.expander("⚡ Quick Test Profiles / Presets"):
            st.caption("Load verified sample candidates for rapid evaluation:")
            for preset_label, pdata in SAMPLE_PROFILES.items():
                if "url" in pdata:
                    if st.button(f"Load {preset_label}", key=f"btn_load_{preset_label}", use_container_width=True):
                        st.session_state["li_profile_url"] = pdata["url"]
                        st.session_state["last_li_url"] = pdata["url"]
                        st.session_state["li_inp_name"] = optimizer.parse_name_from_url(pdata["url"])
                        st.session_state["li_inp_hl"] = pdata.get("headline", "")
                        st.session_state["li_inp_about"] = pdata.get("about", "")
                        st.session_state["li_inp_skills"] = pdata.get("skills", "")
                        st.session_state["li_inp_exp_title"] = pdata.get("experience_title", "")
                        st.session_state["li_inp_exp_comp"] = pdata.get("experience_company", "")
                        st.session_state["li_inp_exp_desc"] = pdata.get("experience_desc", "")
                        st.rerun()

    with col_opt2:
        with st.expander("📄 Optional: Match Against a Specific Job Description"):
            jd_input = st.text_area(
                "Paste Job Description text to analyze match score:",
                placeholder="Paste requirements, qualifications, and tech stack here...",
                height=90,
                key="li_jd_text"
            )

    # Optional Manual Profile Details Verification
    with st.expander("✏️ Customize / Add Specific Profile Details (Optional)"):
        st.caption("CareerIQ Enterprise automatically analyzes the profile URL above. If you want to supply or edit specific resume text, do so below:")
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            input_name = st.text_input("Candidate Full Name", value=extracted_name, key="li_inp_name")
            input_headline = st.text_input("Headline", placeholder="e.g. Software Engineer | Python, React", key="li_inp_hl")
            input_skills = st.text_input("Skills (Comma-separated)", placeholder="e.g. Python, SQL, Docker, Git", key="li_inp_skills")
            input_years = st.number_input("Years of Experience", min_value=0.0, max_value=30.0, value=1.0, step=0.5, key="li_inp_exp_yrs")
        with col_p2:
            input_about = st.text_area("About Summary", placeholder="Paste candidate's About section...", height=70, key="li_inp_about")
            col_e1, col_e2 = st.columns(2)
            with col_e1:
                input_exp_title = st.text_input("Recent Title", placeholder="e.g. Software Engineer", key="li_inp_exp_title")
            with col_e2:
                input_exp_company = st.text_input("Company", placeholder="e.g. Tech Corp", key="li_inp_exp_comp")
            input_exp_desc = st.text_area("Experience Description", placeholder="e.g. Built backend APIs using Python...", height=50, key="li_inp_exp_desc")

    optimize_btn = st.button("⚡ Run Enterprise Profile Intelligence Analysis", use_container_width=True, type="primary")

    # Proceed if button pressed or default valid state
    if optimize_btn or linkedin_url:
        st.divider()

        if not url_validation["valid"]:
            st.error(f"⚠️ {url_validation.get('message', 'Please enter a valid LinkedIn Profile URL.')}")
            return

        # Build verified profile object
        skills_parsed = [s.strip() for s in input_skills.split(",") if s.strip()]
        exp_list = []
        if input_exp_title or input_exp_desc:
            exp_list.append({
                "title": input_exp_title or f"{target_role.split('/')[0].strip()} Practitioner",
                "company": input_exp_company or "Engineering Projects",
                "duration": f"{input_years} yrs",
                "description": input_exp_desc
            })

        # If user didn't enter custom details, automatically infer baseline from URL & Target Role
        if not input_headline and not input_about and not skills_parsed and not exp_list:
            base_profile = optimizer.infer_profile_from_url(linkedin_url, target_role)
            profile_obj = optimizer.build_profile_object(
                name=input_name if input_name and input_name != "Candidate" else base_profile["name"],
                profile_url=linkedin_url,
                headline=base_profile["headline"],
                about=base_profile["about"],
                experience=base_profile["experience"],
                skills=base_profile["skills"],
                current_role=base_profile["current_role"],
                years_of_experience=input_years
            )
            has_number_slug = base_profile.get("has_number_slug", False)
        else:
            profile_obj = optimizer.build_profile_object(
                name=input_name or extracted_name,
                profile_url=linkedin_url,
                headline=input_headline,
                about=input_about,
                experience=exp_list,
                skills=skills_parsed,
                current_role=input_exp_title or (input_headline.split("|")[0].strip() if input_headline else ""),
                years_of_experience=input_years
            )
            has_number_slug = bool(re.search(r"[-_.]?[0-9]{4,}", linkedin_url))

        # Execute Multi-Engine Intelligence
        relevance_data = optimizer.audit_recruiter_relevance(profile_obj, target_role)
        role_match_data = optimizer.match_target_role(profile_obj, target_role)
        completeness_data = optimizer.calculate_completeness(profile_obj)
        before_after_data = optimizer.calculate_before_after(profile_obj, target_role)
        headline_data = optimizer.optimize_headline(profile_obj, target_role)
        about_data = optimizer.optimize_about_section(profile_obj, target_role)
        exp_opt_data = optimizer.optimize_experience(profile_obj)
        action_plan_data = optimizer.generate_action_plan(profile_obj, target_role)
        jd_match_data = optimizer.match_job_description(profile_obj, jd_input) if jd_input else None

        # Notice regarding analysis mode
        if not input_headline and not input_about and not skills_parsed:
            st.info(
                f"⚡ **Dynamic URL Intelligence Active for {profile_obj['name']}** • Target: **{target_role}**  \n"
                f"*(Analyzed from profile URL: `{linkedin_url}`. Open 'Profile Data Verification' box above if you want to paste full resume/About text.)*"
            )
        else:
            st.success(f"🎯 **Verified Custom Analysis Active for {profile_obj['name']}** • Target: **{target_role}**")

        if has_number_slug:
            st.warning(f"⚠️ **SEO Branding Tip for {profile_obj['name']}:** Your profile URL contains trailing numbers (`{linkedin_url}`). Go to LinkedIn *Settings ➔ Edit public profile & URL* to set a clean custom URL: `https://www.linkedin.com/in/{profile_obj['name'].lower().replace(' ', '-')}`.")

        # =========================================================
        # 1. Executive Intelligence Overview Scorecards
        # =========================================================
        st.markdown(f"### 📊 Profile Intelligence Dashboard — {profile_obj['name']}")

        m1, m2, m3, m4 = st.columns(4)
        recruiter_score = relevance_data["estimated_search_relevance_score"]
        m1.metric("Estimated Recruiter Search Score", f"{recruiter_score}/100", f"{'🔥 High Rank' if recruiter_score>=75 else '⚠️ Needs SEO'}")
        m2.metric("Target Role Match", f"{role_match_data['role_match_score']}%", f"Tech: {role_match_data['tech_skills_match']}%")
        m3.metric("Profile Completeness", f"{completeness_data['completeness_score']}%", f"{len(completeness_data['checklist'])} criteria")
        if jd_match_data:
            m4.metric("Job Description Match", f"{jd_match_data['job_match_score']}%", f"{len(jd_match_data['matched_skills'])} matched")
        else:
            m4.metric("Keyword Density Rank", f"{len(relevance_data['strong_keywords'])} Terms", f"{len(relevance_data['missing_keywords'])} missing")

        st.progress(recruiter_score / 100.0)

        st.caption(f"ℹ️ *{relevance_data['disclaimer']}*")

        st.divider()

        # =========================================================
        # 2. Tabbed Section-by-Section Deep Dive
        # =========================================================
        tabs = st.tabs([
            "📊 1. Overview & Before/After",
            "🔍 2. Recruiter Search Relevance",
            "🎯 3. Role & JD Match",
            "🏷️ 4. Headline Optimizer",
            "📝 5. 'About' Optimizer",
            "💼 6. Experience (STAR)",
            "🔑 7. Skills & SEO Cloud",
            "✅ 8. Completeness & Action Plan",
            "📥 9. Export Report"
        ])

        # ---------------------------------------------------------
        # TAB 1: Overview & Before vs After
        # ---------------------------------------------------------
        with tabs[0]:
            st.subheader("📈 Multi-Dimensional Score Breakdown & Comparison")

            b_col1, b_col2 = st.columns([1, 1])

            with b_col1:
                st.markdown("#### 🎯 Score Component Breakdown")
                st.write(f"• **Headline Score:** {headline_data['current_score']}/100")
                st.progress(headline_data['current_score'] / 100)
                st.write(f"• **Technical Skills Match:** {role_match_data['tech_skills_match']}%")
                st.progress(role_match_data['tech_skills_match'] / 100)
                st.write(f"• **Keyword Relevance:** {relevance_data['estimated_search_relevance_score']}/100")
                st.progress(relevance_data['estimated_search_relevance_score'] / 100)
                st.write(f"• **Experience Match:** {role_match_data['experience_match']}%")
                st.progress(role_match_data['experience_match'] / 100)
                st.write(f"• **Project Demonstration:** {role_match_data['project_match']}%")
                st.progress(role_match_data['project_match'] / 100)

            with b_col2:
                st.markdown(f"#### ⚡ Before vs After ({before_after_data['label']})")
                ba_c1, ba_c2 = st.columns(2)
                with ba_c1:
                    st.info(
                        f"**BEFORE OPTIMIZATION**  \n\n"
                        f"• Headline Score: **{before_after_data['before']['headline_score']}/100**  \n"
                        f"• Keyword Relevance: **{before_after_data['before']['keyword_relevance']}/100**  \n"
                        f"• Role Alignment: **{before_after_data['before']['role_alignment']}%**  \n"
                        f"• Completeness: **{before_after_data['before']['completeness']}%**"
                    )
                with ba_c2:
                    st.success(
                        f"**AFTER OPTIMIZATION**  \n\n"
                        f"• Headline Score: **{before_after_data['after']['headline_score']}/100** 🚀  \n"
                        f"• Keyword Relevance: **{before_after_data['after']['keyword_relevance']}/100** 🚀  \n"
                        f"• Role Alignment: **{before_after_data['after']['role_alignment']}%** 🚀  \n"
                        f"• Completeness: **{before_after_data['after']['completeness']}%** 🚀"
                    )

            # Radar Chart Visualization
            categories = ['Headline', 'Technical Skills', 'Keyword Search', 'Experience Depth', 'Completeness']
            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(
                r=[
                    before_after_data['before']['headline_score'],
                    role_match_data['tech_skills_match'],
                    before_after_data['before']['keyword_relevance'],
                    role_match_data['experience_match'],
                    before_after_data['before']['completeness']
                ],
                theta=categories,
                fill='toself',
                name='Current Profile',
                line=dict(color='#EF4444')
            ))
            fig.add_trace(go.Scatterpolar(
                r=[
                    before_after_data['after']['headline_score'],
                    min(100, role_match_data['tech_skills_match'] + 25),
                    before_after_data['after']['keyword_relevance'],
                    min(100, role_match_data['experience_match'] + 20),
                    before_after_data['after']['completeness']
                ],
                theta=categories,
                fill='toself',
                name='After Recommended Blueprint',
                line=dict(color='#10B981')
            ))
            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                showlegend=True,
                title="Profile Competency Radar (Current vs Optimized)",
                template="plotly_dark",
                height=350,
                margin=dict(l=40, r=40, t=40, b=30)
            )
            st.plotly_chart(fig, use_container_width=True)

        # ---------------------------------------------------------
        # TAB 2: Recruiter Search Relevance
        # ---------------------------------------------------------
        with tabs[1]:
            st.subheader(f"🔍 Recruiter Search Relevance Analysis for {target_role}")
            st.caption(f"Domain Focus: **{relevance_data['role_focus']}**")

            k_col1, k_col2, k_col3 = st.columns(3)

            with k_col1:
                st.markdown("#### ✅ Strong Keywords Found")
                if relevance_data["strong_keywords"]:
                    for kw in relevance_data["strong_keywords"]:
                        st.success(f"✓ {kw}")
                else:
                    st.warning("No high-volume search keywords detected yet.")

            with k_col2:
                st.markdown("#### ❌ Missing Search Keywords")
                if relevance_data["missing_keywords"]:
                    for kw in relevance_data["missing_keywords"]:
                        st.error(f"+ {kw}")
                else:
                    st.success("All core role keywords present!")

            with k_col3:
                st.markdown("#### ⚠️ Weak / Generic Terms Flagged")
                if relevance_data["weak_terms_found"]:
                    for wt in relevance_data["weak_terms_found"]:
                        st.warning(f"⚠️ \"{wt}\"")
                else:
                    st.info("No generic buzzwords detected. Great professional tone!")

            st.markdown("---")
            st.markdown("#### 💡 Explainable AI: Why These Terms Matter to Recruiters")
            st.markdown(
                """
                - **Strong Keywords:** LinkedIn Recruiter matches candidate profiles using exact boolean search strings (e.g. `Python AND FastAPI AND (Docker OR AWS)`).
                - **Missing Keywords:** If a primary skill is absent from your headline, skills, or experience text, your profile will be filtered out before the recruiter sees it.
                - **Weak / Generic Buzzwords:** Terms like *'hardworking'*, *'passionate'*, or *'quick learner'* waste valuable headline character space without providing searchable proof of technical skill.
                """
            )

        # ---------------------------------------------------------
        # TAB 3: Role & JD Match
        # ---------------------------------------------------------
        with tabs[2]:
            st.subheader(f"🎯 Target Role Alignment: {target_role}")

            st.markdown(f"**Overall Role Match:** `{role_match_data['role_match_score']}%`")

            col_str, col_gap = st.columns(2)
            with col_str:
                st.markdown("#### 💪 Verified Strengths")
                for s in role_match_data["strengths"]:
                    st.success(f"🔹 {s}")

            with col_gap:
                st.markdown("#### ⚠️ Identified Gaps")
                for g in role_match_data["gaps"]:
                    st.error(f"🔸 {g}")

            if jd_match_data:
                st.divider()
                st.subheader("📄 Job Description Deep Match")
                jd_c1, jd_c2 = st.columns([1, 2])
                with jd_c1:
                    st.metric("Custom JD Match Score", f"{jd_match_data['job_match_score']}%")
                with jd_c2:
                    st.markdown("**Matched Technologies:** " + (", ".join(jd_match_data["matched_skills"]) if jd_match_data["matched_skills"] else "None"))
                    st.markdown("**Missing Technologies:** " + (", ".join(jd_match_data["missing_skills"]) if jd_match_data["missing_skills"] else "None"))

                st.markdown("##### 📌 Recommended Profile Tweaks for this JD:")
                for ch in jd_match_data["recommended_profile_changes"]:
                    st.info(f"👉 {ch}")

        # ---------------------------------------------------------
        # TAB 4: Headline Optimizer
        # ---------------------------------------------------------
        with tabs[3]:
            st.subheader(f"🏷️ Headline Optimizer for {profile_obj['name']}")

            st.markdown(f"**Current Headline:** `{headline_data['current_headline']}` (Score: `{headline_data['current_score']}/100`)")

            st.markdown("#### 💡 3 AI-Optimized Headline Variations (Based on Verified Skills):")

            for opt in headline_data["options"]:
                with st.container():
                    st.markdown(f"##### {opt['type']}")
                    st.code(opt["headline"], language="text")
                    st.caption(f"**Why this works:** {opt['why']}")
                    st.write("")

        # ---------------------------------------------------------
        # TAB 5: About Section Optimizer
        # ---------------------------------------------------------
        with tabs[4]:
            st.subheader("📝 6-Pillar Story-Driven 'About' Section")
            st.markdown(
                "Structured using **Hook + Technical Identity + Core Toolbox + Key Projects + Career Vision + Call-to-Action** "
                "strictly using verified candidate info."
            )

            st.text_area(
                "Optimized LinkedIn 'About' Text (Ready to Copy & Paste):",
                value=about_data["optimized_about"],
                height=340
            )

            st.download_button(
                "📥 Download About Section (.txt)",
                data=about_data["optimized_about"],
                file_name=f"linkedin_about_{profile_obj['name'].lower().replace(' ', '_')}.txt",
                mime="text/plain",
                use_container_width=True
            )

        # ---------------------------------------------------------
        # TAB 6: Experience & STAR Bullets
        # ---------------------------------------------------------
        with tabs[5]:
            st.subheader("💼 Experience Section Audit & STAR Rewrite")
            st.markdown(
                "Recruiters look for **Action Verb + Technology Stack + Quantified Impact (STAR Framework)**."
            )

            for exp in exp_opt_data:
                with st.expander(f"📌 {exp.get('title', 'Role')} @ {exp.get('company', 'Organization')}", expanded=True):
                    st.markdown(f"**Current Text:** *{exp.get('current_description', 'N/A')}*")
                    st.warning(f"**Critique:** {exp.get('critique', 'N/A')}")
                    st.markdown("**Suggested STAR Achievement Bullet:**")
                    st.code(exp.get("recommended_bullet") or exp.get("recommendation", "N/A"), language="text")

        # ---------------------------------------------------------
        # TAB 7: Skills Intelligence & SEO Cloud
        # ---------------------------------------------------------
        with tabs[6]:
            st.subheader(f"🔑 Skills Intelligence & Prioritized SEO for {target_role}")

            st.markdown("#### 🏷️ Priority Missing Skills (Ranked by Recruiter Search Volume)")
            ps = role_match_data["priority_skills"]

            p_col1, p_col2, p_col3 = st.columns(3)
            with p_col1:
                st.error("🔥 **High Priority (Must Add)**")
                for s in ps["High Priority"]:
                    st.write(f"• **{s}**")
            with p_col2:
                st.warning("⚡ **Medium Priority (Add Soon)**")
                for s in ps["Medium Priority"]:
                    st.write(f"• {s}")
            with p_col3:
                st.info("💡 **Low Priority (Elective)**")
                for s in ps["Low Priority"]:
                    st.write(f"• {s}")

            st.divider()
            st.markdown("#### 📋 Existing Candidate Skills")
            if profile_obj["skills"]:
                st.write(" • ".join(profile_obj["skills"]))
            else:
                st.warning("No existing skills explicitly listed.")

        # ---------------------------------------------------------
        # TAB 8: Completeness & Action Plan
        # ---------------------------------------------------------
        with tabs[7]:
            st.subheader("✅ Profile Completeness & Prioritized Action Plan")

            st.markdown(f"**Profile Completeness: `{completeness_data['completeness_score']}%`**")

            chk_c1, chk_c2 = st.columns(2)
            with chk_c1:
                st.markdown("#### 📋 Profile Section Checklist")
                for chk in completeness_data["checklist"]:
                    if chk["status"]:
                        st.success(f"✓ **{chk['item']}** — {chk['detail']}")
                    else:
                        st.warning(f"⚠️ **{chk['item']}** — {chk['detail']}")

            with chk_c2:
                st.markdown("#### 🚀 Prioritized Action Plan")
                for tier, items in action_plan_data.items():
                    st.markdown(f"##### {tier}")
                    for it in items:
                        st.info(f"**{it['action']}**  \n*Why:* {it['why']}")

        # ---------------------------------------------------------
        # TAB 9: Export Report
        # ---------------------------------------------------------
        with tabs[8]:
            st.subheader("📥 Export Complete Profile Optimization Report")
            st.markdown("Generate a presentation-ready executive report for college demos, interviews, or personal records.")

            report_text = optimizer.generate_export_report(
                profile=profile_obj,
                target_role=target_role,
                jd_text=jd_input
            )

            st.text_area("Audit Report Preview:", value=report_text, height=350)

            st.download_button(
                "📥 Download Complete Optimization Report (.txt)",
                data=report_text,
                file_name=f"linkedin_optimization_report_{profile_obj['name'].lower().replace(' ', '_')}.txt",
                mime="text/plain",
                type="primary",
                use_container_width=True
            )
