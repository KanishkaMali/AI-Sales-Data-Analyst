# ==========================================================
# data_loader.py
# Responsible for loading and preparing data
# ==========================================================

import pandas as pd
import streamlit as st

from config import DATA_FILE


@st.cache_data
def load_data():
    """
    Loads the Superstore dataset.

    Returns
    -------
    DataFrame
    """

    df = pd.read_csv(
        DATA_FILE,
        encoding="cp1252"
    )

    # Convert date columns
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    # Create Year
    df["Year"] = df["Order Date"].dt.year

    # Create Month
    df["Month"] = (
        df["Order Date"]
        .dt.to_period("M")
        .astype(str)
    )

    return df