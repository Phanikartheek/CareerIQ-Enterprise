"""
=========================================================
CareerIQ Enterprise
Sidebar Navigation
Author : Vellanki phanikartheek
=========================================================
"""

import streamlit as st

from config import (
    APP_NAME,
    APP_VERSION,
    SIDEBAR_MENU,
    FOOTER
)


def render_sidebar():
    """
    Render application sidebar
    Returns:
        str : Selected menu item
    """

    st.sidebar.image(
        "https://img.icons8.com/color/96/artificial-intelligence.png",
        width=90
    )

    st.sidebar.title(APP_NAME)

    st.sidebar.caption(APP_VERSION)

    st.sidebar.markdown("---")

    menu = st.sidebar.radio(
        "📂 Navigation",
        SIDEBAR_MENU,
        label_visibility="visible"
    )

    st.sidebar.markdown("---")

    st.sidebar.success("🚀 Enterprise Edition")

    st.sidebar.caption(FOOTER)

    return menu