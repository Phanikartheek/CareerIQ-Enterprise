"""
=========================================================
CareerIQ Enterprise - Enterprise AI Learning Roadmap (Zero-to-Pro)
Version : 12.0 Enterprise Production Edition
Author  : CareerIQ Engineering
=========================================================
"""

import streamlit as st
import plotly.graph_objects as go
from core.learning_recommender import LearningRecommender


def learning_roadmap_page():
    st.title("📚 Enterprise AI Learning Roadmap (Zero to Pro)")
    st.markdown(
        "Enter **any target engineering role** (e.g. *AI Engineer*, *Data Scientist*, *Full Stack Developer*, *DevOps*, etc.). "
        "CareerIQ Enterprise will generate a comprehensive, **phase-by-phase Zero-to-Pro blueprint** with core topics, hands-on projects, industry tools, and certified milestones."
    )

    recommender = LearningRecommender()
    supported_roles = recommender.get_supported_roles()

    st.divider()

    # =========================================================
    # Step 1: Target Role & Timeline Configuration
    # =========================================================
    st.subheader("🎯 1. Career Goal & Learning Configuration")

    c1, c2, c3 = st.columns([1.5, 1, 1])

    with c1:
        role_options = supported_roles + ["✍️ Custom Role (Enter Any Role Below)"]
        selected_role_option = st.selectbox(
            "Select Target Role or Choose Custom",
            role_options,
            index=0,
            key="lr_role_select"
        )

        if selected_role_option == "✍️ Custom Role (Enter Any Role Below)":
            custom_role_input = st.text_input(
                "Enter Custom Target Role Name",
                value="Robotics Software Engineer",
                placeholder="e.g. Embedded Systems Engineer, Blockchain Developer, MLOps Specialist...",
                key="lr_custom_role"
            )
            active_role = custom_role_input.strip() or "Software Engineer"
        else:
            active_role = selected_role_option

    with c2:
        level_option = st.selectbox(
            "Current Starting Level",
            [
                "🌱 Beginner / College Student (From Scratch)",
                "⚡ Intermediate / Working Professional (Upskilling)",
                "🔄 Career Switcher / Non-Tech to Tech"
            ],
            index=0,
            key="lr_level_select"
        )

    with c3:
        timeline_option = st.selectbox(
            "Target Learning Timeline",
            [
                "🎯 6 Months (Recommended Standard • 10-15 hrs/wk)",
                "⚡ 3 Months (Fast Track Intensive • 20+ hrs/wk)",
                "🏆 12 Months (Deep Mastery • 5-10 hrs/wk)"
            ],
            index=0,
            key="lr_timeline_select"
        )

    # Calculate weeks based on selection
    if "3 Months" in timeline_option:
        timeline_weeks = 12
    elif "12 Months" in timeline_option:
        timeline_weeks = 48
    else:
        timeline_weeks = 24

    generate_btn = st.button("⚡ Generate Zero-to-Pro Learning Roadmap", use_container_width=True, type="primary")

    # Generate Roadmap Data
    roadmap_data = recommender.generate_custom_roadmap_for_role(
        role_name=active_role,
        current_level=level_option.split("(")[0].strip(),
        timeline_weeks=timeline_weeks
    )

    st.divider()

    # =========================================================
    # Step 2: Roadmap Dashboard Overview
    # =========================================================
    st.subheader(f"🗺️ Zero-to-Pro Roadmap: {roadmap_data['title']}")
    st.caption(f"💡 {roadmap_data['tagline']}")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Mastery Phases", f"{len(roadmap_data['phases'])} Phases", "Foundations to Pro")
    m2.metric("Estimated Timeline", f"{roadmap_data['duration_weeks']} Weeks", f"{timeline_option.split('•')[1].strip() if '•' in timeline_option else 'Flexible'}")
    m3.metric("Capstone Projects", f"{len(roadmap_data['projects'])} Real-World", "Resume-Ready")
    m4.metric("Target Mastery Level", "Senior / Pro Level", "100% Industry Aligned")

    st.progress(1.0)

    st.divider()

    # =========================================================
    # Step 3: Deep-Dive Roadmap Tabs
    # =========================================================
    t1, t2, t3, t4, t5, t6 = st.tabs([
        "🗺️ 1. Phase-by-Phase Roadmap",
        "🛠️ 2. Project Blueprints",
        "📖 3. Curated Resources & Certs",
        "🎯 4. Weekly Milestone Checklist",
        "💡 5. Pro Hiring Strategy",
        "📥 6. Export Roadmap"
    ])

    # ---------------------------------------------------------
    # TAB 1: Phase-by-Phase Roadmap
    # ---------------------------------------------------------
    with t1:
        st.subheader(f"🚀 5-Stage Step-by-Step Learning Timeline for {roadmap_data['title']}")
        st.markdown("Follow this structured roadmap phase by phase. Do not skip foundations to ensure long-term senior mastery.")

        for idx, phase in enumerate(roadmap_data["phases"], 1):
            with st.container():
                st.markdown(
                    f"""
                    <div style="background-color: #1E293B; padding: 18px; border-radius: 10px; margin-bottom: 15px; border-left: 5px solid #38BDF8;">
                        <h4 style="color: #38BDF8; margin: 0 0 8px 0;">{phase['phase']} <span style="color: #94A3B8; font-size: 14px; font-weight: normal;">({phase['duration']})</span></h4>
                        <p style="color: #E2E8F0; font-size: 15px; margin: 0 0 10px 0;"><strong>🎯 Focus:</strong> {phase['focus']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                col_top, col_tools = st.columns([2, 1])

                with col_top:
                    st.markdown("**📌 Key Topics to Master:**")
                    for topic in phase["topics"]:
                        st.write(f"• {topic}")

                with col_tools:
                    st.markdown("**🛠️ Essential Tools:**")
                    st.write(" • ".join(phase["tools"]))
                    st.markdown("**🏆 Practical Milestone Project:**")
                    st.info(f"👉 {phase['milestone_project']}")

                st.write("")

    # ---------------------------------------------------------
    # TAB 2: Industry Project Blueprints
    # ---------------------------------------------------------
    with t2:
        st.subheader("🛠️ Resume-Ready Industry Project Blueprints")
        st.markdown(
            "Recruiters prioritize **practical execution over certificates**. Build these 3 portfolio-defining projects to demonstrate "
            "production engineering capabilities."
        )

        for prj in roadmap_data["projects"]:
            with st.expander(f"📌 [{prj['tier']}] {prj['name']}", expanded=True):
                st.markdown(f"**Tech Stack:** `{prj['stack']}`")
                st.markdown(f"**Project Scope & Architecture:**  \n{prj['description']}")
                st.markdown(
                    """
                    **⭐ How to showcase on LinkedIn / Resume:**
                    1. Deploy with a live URL (Vercel, Streamlit, AWS EC2).
                    2. Write a comprehensive GitHub `README.md` with system architecture diagram, setup instructions, and benchmark metrics.
                    3. Record a 60-second video demo walkthrough and attach it to your LinkedIn Featured section.
                    """
                )

    # ---------------------------------------------------------
    # TAB 3: Curated Resources & Certifications
    # ---------------------------------------------------------
    with t3:
        st.subheader("📖 Curated Free/Paid Learning Resources & Industry Certifications")

        col_res, col_cert = st.columns(2)

        with col_res:
            st.markdown("#### 🌐 Top Recommended Learning Platforms")
            for res in roadmap_data.get("resources", []):
                st.markdown(
                    f"""
                    <div style="background-color: #0F172A; padding: 12px; border-radius: 8px; margin-bottom: 10px; border: 1px solid #334155;">
                        <span style="color: #10B981; font-weight: bold;">[{res['type']}]</span> 
                        <strong style="color: #F8FAFC;">{res['name']}</strong><br/>
                        <a href="{res['link']}" target="_blank" style="color: #38BDF8; font-size: 13px;">🔗 Open Resource Website</a>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        with col_cert:
            st.markdown("#### 🏆 High-Impact Industry Certifications")
            st.caption("Certifications that recruiters actively search for on LinkedIn filters:")
            for cert in roadmap_data.get("certifications", []):
                st.success(f"✓ **{cert}**")

    # ---------------------------------------------------------
    # TAB 4: Weekly Milestone Checklist
    # ---------------------------------------------------------
    with t4:
        st.subheader("🎯 Interactive Progress & Milestone Tracker")
        st.markdown("Check off competencies as you master them to track your progression toward pro level:")

        total_topics = sum(len(p["topics"]) for p in roadmap_data["phases"])
        completed_count = 0

        for p_idx, phase in enumerate(roadmap_data["phases"]):
            st.markdown(f"##### 📌 {phase['phase']}")
            for t_idx, topic in enumerate(phase["topics"]):
                chk = st.checkbox(topic, key=f"chk_{p_idx}_{t_idx}")
                if chk:
                    completed_count += 1

        st.divider()
        progress_pct = completed_count / max(total_topics, 1)
        st.markdown(f"#### 📊 Current Completion: `{int(progress_pct * 100)}%` ({completed_count}/{total_topics} topics completed)")
        st.progress(progress_pct)
        if progress_pct >= 0.8:
            st.balloons()
            st.success("🎉 You are ready to crack top-tier technical interviews for this role!")

    # ---------------------------------------------------------
    # TAB 5: Pro Hiring Strategy & Pitfalls
    # ---------------------------------------------------------
    with t5:
        st.subheader("💡 How to Stand Out & Land High-Paying Offers")

        s1, s2 = st.columns(2)

        with s1:
            st.markdown("#### 🚀 4 Pro Tactics to Get Shortlisted:")
            st.markdown(
                """
                1. **Build in Public & Share Code:** Post weekly updates on LinkedIn explaining architectural decisions or debugging lessons from your projects.
                2. **Deploy Live Demos:** 90% of applicants only submit GitHub links with no live demo. A live URL gets 5x more clicks from recruiters.
                3. **Master System Design Early:** Even for junior/mid roles, understanding caching, API latency, and database indexing puts you in the top 5% of candidates.
                4. **Quantify Resume Bullets:** Use the STAR framework (*'Engineered X using Y, improving latency by 35% across 10K requests'*).
                """
            )

        with s2:
            st.markdown("#### ❌ Common Traps to Avoid (Tutorial Hell):")
            st.markdown(
                """
                - **❌ Endless Tutorial Watching:** Don't watch 50-hour courses without writing code from scratch. Build your own version after every 2-3 lessons.
                - **❌ Copying Generic Clone Projects:** Don't build generic Todo apps or Netflix clones that 10,000 others have on their resume.
                - **❌ Neglecting Git & Documentation:** Sloppy commit histories and missing README files signal low professional maturity.
                - **❌ Ignoring Fundamentals for Shiny Frameworks:** Frameworks change every 2 years; strong algorithmic and system fundamentals last forever.
                """
            )

    # ---------------------------------------------------------
    # TAB 6: Export Roadmap
    # ---------------------------------------------------------
    with t6:
        st.subheader("📥 Export Complete Zero-to-Pro Learning Blueprint")
        st.markdown("Download this comprehensive roadmap document to keep on your desktop or track in your Notion workspace.")

        export_text = recommender.generate_export_text(roadmap_data)

        st.text_area("Roadmap Document Preview:", value=export_text, height=350)

        st.download_button(
            "📥 Download Complete Learning Roadmap (.txt)",
            data=export_text,
            file_name=f"learning_roadmap_{active_role.lower().replace(' ', '_')}.txt",
            mime="text/plain",
            type="primary",
            use_container_width=True
        )