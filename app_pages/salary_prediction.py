"""
=========================================================
CareerIQ Enterprise - Enterprise AI Salary & Compensation Intelligence
Version : 12.0 Enterprise Production Edition
Author  : CareerIQ Engineering
=========================================================
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from core.salary_prediction import SalaryPredictor


def salary_prediction_page():
    st.title("💼 Enterprise AI Salary & Compensation Intelligence")
    st.markdown(
        "Predict your **real-world market compensation value** using machine learning regression models. "
        "Analyze base pay, variable bonuses, equity grants, and discover **high-ROI skills** that maximize your CTC."
    )

    predictor = SalaryPredictor()

    st.divider()

    # =========================================================
    # Step 1: Input Candidate Profile & Market Parameters
    # =========================================================
    st.subheader("🎯 1. Candidate Experience & Compensation Parameters")

    col_role, col_exp = st.columns([1.5, 1])

    with col_role:
        role = st.selectbox(
            "Target Engineering Role",
            list(predictor.ROLE_BASELINES.keys()),
            index=0,
            key="sal_role_select"
        )

    with col_exp:
        experience = st.slider(
            "Years of Professional Experience",
            min_value=0.0,
            max_value=18.0,
            value=2.5,
            step=0.5,
            key="sal_exp_slider"
        )

    col_loc, col_comp, col_edu = st.columns(3)

    with col_loc:
        location = st.selectbox(
            "Job Location / Market Hub",
            list(predictor.LOCATION_MULTIPLIERS.keys()),
            index=0,
            key="sal_loc_select"
        )

    with col_comp:
        company_tier = st.selectbox(
            "Target Company Category",
            list(predictor.COMPANY_TIER_MULTIPLIERS.keys()),
            index=1,
            key="sal_comp_select"
        )

    with col_edu:
        education = st.selectbox(
            "Education Background",
            list(predictor.EDUCATION_MULTIPLIERS.keys()),
            index=2,
            key="sal_edu_select"
        )

    skills_input = st.text_input(
        "Candidate Tech Stack (Comma-separated)",
        value="Python, PyTorch, FastAPI, Docker, SQL, Machine Learning",
        placeholder="e.g. Python, React, AWS, Docker, Kubernetes, Kafka",
        key="sal_skills_input",
        help="Add skills to see real-time skill multiplier bonuses on your compensation."
    )

    skills_list = [s.strip() for s in skills_input.split(",") if s.strip()]

    predict_btn = st.button("⚡ Calculate Machine Learning Compensation Intelligence", use_container_width=True, type="primary")

    # Run Prediction
    comp_result = predictor.predict_compensation(
        role=role,
        experience_years=experience,
        skills_list=skills_list,
        education_tier=education,
        company_tier=company_tier,
        location=location
    )

    st.divider()

    # =========================================================
    # Step 2: Executive Compensation Scorecard
    # =========================================================
    st.subheader(f"📊 Market Compensation Intelligence: {role}")
    st.caption(f"Location: **{location}** • Company Tier: **{company_tier.split('(')[0].strip()}** • Experience: **{experience} Years**")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Estimated Median CTC", f"₹ {comp_result['ctc_median_lpa']} LPA", f"Top {100 - comp_result['percentile']}% Bracket")
    m2.metric("Expected CTC Range", comp_result["ctc_range_str"], "88% - 115% Band")
    m3.metric("Global US Equivalent", comp_result["usd_equivalent"], "Normalized USD")
    m4.metric("Market Percentile Rank", f"{comp_result['percentile']}th Percentile", "vs Industry Peers")

    st.progress(comp_result["percentile"] / 100.0)

    st.divider()

    # =========================================================
    # Step 3: Deep-Dive Analysis Tabs
    # =========================================================
    t1, t2, t3, t4, t5 = st.tabs([
        "💰 1. CTC Breakdown & Components",
        "🚀 2. Skill ROI & Value Calculator",
        "📈 3. 10-Year Growth Trajectory",
        "🏢 4. Company & City Benchmarks",
        "📥 5. Export Compensation Report"
    ])

    # ---------------------------------------------------------
    # TAB 1: CTC Breakdown & Components
    # ---------------------------------------------------------
    with t1:
        st.subheader("💵 Total Compensation (CTC) Structure Breakdown")

        col_b1, col_b2 = st.columns([1, 1])

        with col_b1:
            st.markdown("#### 📋 Annual Compensation Components")
            st.success(f"🔹 **Fixed Base Salary:** `{comp_result['breakdown']['base_salary']}` (Guaranteed Monthly Pay)")
            st.info(f"🔹 **Variable / Performance Bonus:** `{comp_result['breakdown']['variable_bonus']}` (Annual Target Incentive)")
            st.warning(f"🔹 **Stock Grants / ESOPs:** `{comp_result['breakdown']['stocks_esops']}` (Long-Term Wealth Multiplier)")

            st.markdown("---")
            st.markdown("#### 💡 Detected Skill Premiums on Current Profile:")
            if comp_result["detected_premiums"]:
                for dp in comp_result["detected_premiums"]:
                    st.write(f"✓ **{dp['skill']}** ➔ *+ ₹ {dp['boost_lpa']} LPA Market Boost*")
            else:
                st.caption("No Tier-1 premium skills detected yet. Add skills like LLMs, Kubernetes, or System Design to boost your base.")

        with col_b2:
            # Donut Chart for CTC Breakdown
            labels = ['Base Salary (Fixed)', 'Performance Bonus', 'Stock Grants / ESOPs']
            values = [70, 15, 15]
            colors = ['#10B981', '#38BDF8', '#F59E0B']

            fig_donut = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.55, marker=dict(colors=colors))])
            fig_donut.update_layout(
                title="CTC Split (Standard Product Company)",
                template="plotly_dark",
                height=300,
                margin=dict(l=20, r=20, t=40, b=20),
                showlegend=True
            )
            st.plotly_chart(fig_donut, use_container_width=True)

    # ---------------------------------------------------------
    # TAB 2: Skill ROI & Value Calculator
    # ---------------------------------------------------------
    with t2:
        st.subheader("🚀 High-ROI Skills to Maximize Your Compensation")
        st.markdown(
            "Not all skills pay equally. Adding these high-demand technical capabilities can significantly increase your CTC negotiation leverage:"
        )

        roi_c1, roi_c2 = st.columns(2)
        for idx, roi in enumerate(comp_result["high_roi_skills"]):
            target_col = roi_c1 if idx % 2 == 0 else roi_c2
            with target_col:
                st.markdown(
                    f"""
                    <div style="background-color: #1E293B; padding: 14px; border-radius: 8px; margin-bottom: 12px; border-left: 4px solid #10B981;">
                        <h4 style="color: #F8FAFC; margin: 0 0 6px 0;">⚡ Learn {roi['skill']}</h4>
                        <span style="color: #10B981; font-weight: bold; font-size: 15px;">Projected CTC Increase: {roi['projected_boost']}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.info("💡 **Negotiation Tip:** Having production projects demonstrating these skills gives you 2x more bargaining power during compensation discussions.")

    # ---------------------------------------------------------
    # TAB 3: 10-Year Career Growth Trajectory
    # ---------------------------------------------------------
    with t3:
        st.subheader(f"📈 10-Year Estimated Salary Progression for {role}")
        st.markdown("Forecasted compensation curve based on continuous learning and progression from Junior to Staff/Principal Engineer:")

        traj_df = pd.DataFrame(comp_result["trajectory"])

        fig_traj = px.area(
            traj_df,
            x="years",
            y="salary_lpa",
            title=f"Predicted Compensation Growth Curve ({role})",
            labels={"years": "Career Milestone", "salary_lpa": "Estimated CTC (₹ LPA)"},
            template="plotly_dark",
            markers=True
        )
        fig_traj.update_traces(line_color="#38BDF8", fillcolor="rgba(56, 189, 248, 0.2)")
        fig_traj.update_layout(height=340, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig_traj, use_container_width=True)

    # ---------------------------------------------------------
    # TAB 4: Company Tier & Location Comparison
    # ---------------------------------------------------------
    with t4:
        st.subheader("🏢 Market Compensation Matrix across Company Types")

        comp_tiers = {
            "FAANG / Top Tier-1 Tech": comp_result['ctc_median_lpa'] * 1.35,
            "Top Unicorn Startup": comp_result['ctc_median_lpa'] * 1.15,
            "Mid-Size Product Tech": comp_result['ctc_median_lpa'] * 0.95,
            "IT Services / Enterprise": comp_result['ctc_median_lpa'] * 0.65
        }

        tier_df = pd.DataFrame({
            "Company Tier": list(comp_tiers.keys()),
            "Estimated CTC (₹ LPA)": [round(v, 1) for v in comp_tiers.values()]
        })

        fig_bar = px.bar(
            tier_df,
            x="Company Tier",
            y="Estimated CTC (₹ LPA)",
            color="Estimated CTC (₹ LPA)",
            color_continuous_scale="Viridis",
            template="plotly_dark",
            text="Estimated CTC (₹ LPA)"
        )
        fig_bar.update_layout(height=340, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig_bar, use_container_width=True)

    # ---------------------------------------------------------
    # TAB 5: Export Compensation Report
    # ---------------------------------------------------------
    with t5:
        st.subheader("📥 Export Executive Compensation Report")
        st.markdown("Download a formatted market value compensation summary for interview preparation or salary negotiations.")

        report_txt = predictor.generate_compensation_report(comp_result)

        st.text_area("Compensation Report Preview:", value=report_txt, height=340)

        st.download_button(
            "📥 Download Compensation Report (.txt)",
            data=report_txt,
            file_name=f"compensation_report_{role.lower().replace(' ', '_')}.txt",
            mime="text/plain",
            type="primary",
            use_container_width=True
        )