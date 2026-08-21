"""
=========================================================
CareerIQ Enterprise
Enterprise GitHub Portfolio Analyzer
Author : CareerIQ Engineering
Version : 11.0 Enterprise
=========================================================
"""

import streamlit as st
import plotly.express as px
import pandas as pd
from core.github_analyzer import GitHubAnalyzer


def github_portfolio_page():
    st.title("💻 Enterprise GitHub Portfolio Analyzer")
    st.markdown(
        "Analyze any developer's GitHub portfolio, assess code quality, language versatility, "
        "repository impact, and generate actionable recruiter intelligence."
    )

    st.divider()

    # =========================================================
    # Input Section
    # =========================================================
    st.subheader("🔍 Analyze GitHub Profile")

    col_input, col_btn = st.columns([3, 1])

    with col_input:
        target_username = st.text_input(
            "Enter GitHub Username or Profile URL",
            placeholder="e.g. torvalds or https://github.com/your-username",
            key="github_user_input"
        )

    with col_btn:
        st.write("")
        st.write("")
        analyze_btn = st.button("🚀 Analyze Portfolio", use_container_width=True)

    # Quick demo buttons
    st.caption("💡 Quick Demo Examples:")
    demo_cols = st.columns(4)
    if demo_cols[0].button("phani-kartheek", use_container_width=True):
        st.session_state["github_user_input"] = "phani-kartheek"
        st.rerun()
    if demo_cols[1].button("torvalds (Linux)", use_container_width=True):
        st.session_state["github_user_input"] = "torvalds"
        st.rerun()
    if demo_cols[2].button("tiangolo (FastAPI)", use_container_width=True):
        st.session_state["github_user_input"] = "tiangolo"
        st.rerun()
    if demo_cols[3].button("karpathy (AI/ML)", use_container_width=True):
        st.session_state["github_user_input"] = "karpathy"
        st.rerun()

    current_query = target_username or st.session_state.get("github_user_input", "")

    if (analyze_btn or current_query) and current_query.strip():
        analyzer = GitHubAnalyzer()

        with st.spinner(f"🔍 Fetching and analyzing GitHub data for '{current_query}'..."):
            data = analyzer.analyze_portfolio(current_query)

        if "error" in data:
            st.error(f"❌ {data['error']}")
            return

        st.success(f"✅ Successfully analyzed GitHub profile for **{data['name']}** (@{data['username']})!")

        st.divider()

        # =========================================================
        # Profile Header Card
        # =========================================================
        p_col1, p_col2 = st.columns([1, 3])

        with p_col1:
            if data.get("avatar_url"):
                st.image(data["avatar_url"], width=160)
            st.markdown(f"### [{data['name']}]({data['html_url']})")
            st.caption(f"@{data['username']}")

        with p_col2:
            st.markdown(f"**Bio:** {data['bio']}")
            st.markdown(f"📍 **Location:** {data['location']} | 🏢 **Company:** {data['company'] or 'Independent'}")
            if data.get("blog"):
                st.markdown(f"🌐 **Website / Portfolio:** [{data['blog']}]({data['blog']})")
            
            st.markdown("**Identified Specializations:**")
            arch_badges = " ".join([f"`{arch}`" for arch in data["archetypes"]])
            st.markdown(arch_badges)

        st.divider()

        # =========================================================
        # Core Metrics Dashboard
        # =========================================================
        st.subheader("📊 Portfolio Performance Metrics")

        m1, m2, m3, m4, m5 = st.columns(5)
        m1.metric("Portfolio Score", f"{data['portfolio_score']}/100", data["grade"])
        m2.metric("Public Repos", data["public_repos"])
        m3.metric("Total Stars ⭐", data["total_stars"])
        m4.metric("Followers", data["followers"])
        m5.metric("Account Age", f"{data['account_age_years']} Yrs")

        # Health Progress Bar
        st.markdown(f"**Overall Portfolio Strength:** {data['status']}")
        st.progress(data["portfolio_score"] / 100)

        st.divider()

        # =========================================================
        # Visual Analytics: Languages & Top Repos
        # =========================================================
        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            st.subheader("🌐 Tech Stack Distribution")
            if data["languages"]:
                lang_df = pd.DataFrame(
                    list(data["languages"].items()),
                    columns=["Language", "Percentage"]
                )
                fig_pie = px.pie(
                    lang_df,
                    names="Language",
                    values="Percentage",
                    hole=0.45,
                    title="Codebase Language Share (%)",
                    color_discrete_sequence=px.colors.qualitative.Prism
                )
                fig_pie.update_layout(template="plotly_dark", height=350)
                st.plotly_chart(fig_pie, use_container_width=True)
            else:
                st.info("No explicit languages detected in repositories.")

        with chart_col2:
            st.subheader("⭐ Most Starred Repositories")
            starred_repos = [r for r in data["top_repos"] if r["stars"] > 0]
            if starred_repos:
                stars_df = pd.DataFrame(starred_repos[:6])
                fig_bar = px.bar(
                    stars_df,
                    x="name",
                    y="stars",
                    color="language",
                    text="stars",
                    title="Top Repositories by Stars",
                    labels={"name": "Repository", "stars": "Stars"}
                )
                fig_bar.update_layout(template="plotly_dark", height=350)
                st.plotly_chart(fig_bar, use_container_width=True)
            else:
                # Show recent repos by language if 0 stars
                recent_df = pd.DataFrame(data["top_repos"][:6])
                if not recent_df.empty:
                    fig_bar = px.bar(
                        recent_df,
                        x="name",
                        y=[1]*len(recent_df),
                        color="language",
                        title="Recent Active Repositories",
                        labels={"name": "Repository", "y": "Active"}
                    )
                    fig_bar.update_layout(template="plotly_dark", height=350, yaxis_visible=False)
                    st.plotly_chart(fig_bar, use_container_width=True)
                else:
                    st.info("No repositories available to display.")

        st.divider()

        # =========================================================
        # Top Repositories Showcase
        # =========================================================
        st.subheader("📁 Featured Repositories")

        if data["top_repos"]:
            for repo in data["top_repos"][:6]:
                with st.container():
                    st.markdown(
                        f"""
                        <div style="background-color: #1E293B; padding: 16px; border-radius: 8px; margin-bottom: 12px; border: 1px solid #334155;">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <h4 style="margin: 0; color: #38BDF8;">
                                    <a href="{repo['url']}" target="_blank" style="color: #38BDF8; text-decoration: none;">📦 {repo['name']}</a>
                                </h4>
                                <span style="background-color: #0F172A; padding: 4px 10px; border-radius: 12px; font-size: 12px; color: #94A3B8;">
                                    {repo['language']} | ⭐ {repo['stars']} | 🍴 {repo['forks']}
                                </span>
                            </div>
                            <p style="margin: 8px 0; color: #CBD5E1; font-size: 14px;">{repo['description']}</p>
                            <small style="color: #64748B;">Last updated: {repo['updated_at']}</small>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
        else:
            st.info("No public repositories found for this account.")

        st.divider()

        # =========================================================
        # Recruiter Recommendations & AI Action Items
        # =========================================================
        st.subheader("🎯 AI Recruiter & ATS Optimization Advice")

        rec_col1, rec_col2 = st.columns(2)

        with rec_col1:
            st.markdown("### 💡 Recommended Portfolio Upgrades")
            for rec in data["recommendations"]:
                st.info(f"📌 {rec}")

        with rec_col2:
            st.markdown("### 📋 Recruiter Summary Note")
            st.success(
                f"""
                **Candidate:** {data['name']} (@{data['username']})  
                **Primary Focus:** {', '.join(data['archetypes'])}  
                **Portfolio Status:** {data['status']} (Score: {data['portfolio_score']}/100)  
                **Public Codebase:** {data['public_repos']} repositories analyzed with focus on {', '.join(list(data['languages'].keys())[:3]) or 'modern development'}.
                """
            )

        st.divider()

        # Raw JSON Export
        with st.expander("📑 View Complete JSON Analysis"):
            st.json(data)
