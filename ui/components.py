"""
=========================================================
CareerIQ Enterprise
UI Components
Author : Vellanki phanikartheek
=========================================================
"""

import streamlit as st


def metric_card(title, value, delta=None, help_text=None):
    """
    Display a metric card.
    """

    st.metric(
        label=title,
        value=value,
        delta=delta,
        help=help_text
    )


def section_title(title):
    """
    Display a section heading.
    """

    st.subheader(title)


def info_card(message):
    """
    Display an information box.
    """

    st.info(message)


def success_card(message):
    """
    Display a success message.
    """

    st.success(message)


def warning_card(message):
    """
    Display a warning message.
    """

    st.warning(message)


def error_card(message):
    """
    Display an error message.
    """

    st.error(message)


def divider():
    """
    Display a horizontal divider.
    """

    st.divider()