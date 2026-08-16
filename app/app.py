# ==========================================================
# AI Sales Data Analyst
# app.py
# ==========================================================

# -----------------------------
# Imports
# -----------------------------
from utils import dataframe_to_csv
from ai_explainer import explain_result
import streamlit as st
import pandas as pd

from dotenv import load_dotenv
import os

from google import genai

from config import (
    APP_TITLE,
    PAGE_ICON,
    LAYOUT
)

from data_loader import load_data
from analysis import BusinessAnalyzer
from ai_router import route_question

from charts import (
    category_sales_chart,
    region_sales_chart,
    monthly_sales_chart,
    state_sales_chart,
    customer_sales_chart,
    product_sales_chart,
    category_profit_chart
)

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT
)

# ==========================================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================================

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:

    st.error("GOOGLE_API_KEY not found inside .env file")

    st.stop()

# ==========================================================
# GEMINI CLIENT
# ==========================================================

client = genai.Client(
    api_key=GOOGLE_API_KEY
)

# ==========================================================
# TITLE
# ==========================================================

st.title("📊 AI Sales Data Analyst")

st.caption(
    "Python • Pandas • Power BI • Streamlit • Gemini AI"
)

# ==========================================================
# LOAD DATA
# ==========================================================

try:

    df = load_data()

except Exception as e:

    st.error(e)

    st.stop()

# ==========================================================
# PREPROCESS
# ==========================================================

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Ship Date"] = pd.to_datetime(df["Ship Date"])

df["Year"] = df["Order Date"].dt.year

df["Month"] = (
    df["Order Date"]
    .dt.to_period("M")
    .astype(str)
)

# ==========================================================
# ANALYZER
# ==========================================================

analyzer = BusinessAnalyzer(df)

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("📌 Dashboard")

st.sidebar.success(
    "Dataset Loaded Successfully"
)

st.sidebar.markdown("---")

st.sidebar.subheader("Dataset")

st.sidebar.write(f"Rows : {len(df):,}")

st.sidebar.write(f"Columns : {len(df.columns)}")

st.sidebar.markdown("---")

st.sidebar.subheader("Quick Filters")

selected_year = st.sidebar.selectbox(

    "Select Year",

    options=["All"] + sorted(
        df["Year"].unique().tolist()
    )

)

selected_region = st.sidebar.selectbox(

    "Select Region",

    options=["All"] + sorted(
        df["Region"].unique().tolist()
    )

)

# ==========================================================
# APPLY FILTERS
# ==========================================================

filtered_df = df.copy()

if selected_year != "All":

    filtered_df = filtered_df[
        filtered_df["Year"] == selected_year
    ]

if selected_region != "All":

    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

# ==========================================================
# NEW ANALYZER
# ==========================================================

analyzer = BusinessAnalyzer(filtered_df)

# ==========================================================
# KPI SECTION
# ==========================================================

total_sales = analyzer.total_sales()

total_profit = analyzer.total_profit()

total_orders = analyzer.total_orders()

total_customers = analyzer.total_customers()

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "💰 Total Sales",
    f"${total_sales:,.2f}"
)

c2.metric(
    "📈 Total Profit",
    f"${total_profit:,.2f}"
)

c3.metric(
    "📦 Orders",
    total_orders
)

c4.metric(
    "👥 Customers",
    total_customers
)

st.divider()

# ==========================================================
# DASHBOARD
# ==========================================================

st.header("📈 Business Dashboard")

# ----------------------------------------------------------
# ROW 1
# ----------------------------------------------------------

left, right = st.columns(2)

with left:

    st.plotly_chart(
        category_sales_chart(
            analyzer.sales_by_category()
        ),
        use_container_width=True
    )

with right:

    st.plotly_chart(
        region_sales_chart(
            analyzer.sales_by_region()
        ),
        use_container_width=True
    )

# ----------------------------------------------------------
# ROW 2
# ----------------------------------------------------------

left, right = st.columns(2)

with left:

    st.plotly_chart(
        monthly_sales_chart(
            analyzer.monthly_sales()
        ),
        use_container_width=True
    )

with right:

    st.plotly_chart(
        state_sales_chart(
            analyzer.sales_by_state()
        ),
        use_container_width=True
    )

# ----------------------------------------------------------
# ROW 3
# ----------------------------------------------------------

left, right = st.columns(2)

with left:

    st.plotly_chart(
        customer_sales_chart(
            analyzer.top_customers()
        ),
        use_container_width=True
    )

with right:

    st.plotly_chart(
        product_sales_chart(
            analyzer.top_products()
        ),
        use_container_width=True
    )

# ----------------------------------------------------------
# ROW 4
# ----------------------------------------------------------

st.plotly_chart(

    category_profit_chart(

        analyzer.profit_by_category()

    ),

    use_container_width=True

)

st.divider()


# ==========================================================
# BUSINESS HIGHLIGHTS
# ==========================================================

st.header("📌 Business Highlights")

sales_state = analyzer.sales_by_state()

sales_category = analyzer.sales_by_category()

sales_region = analyzer.sales_by_region()

top_state = sales_state.iloc[0]["State"]

top_category = sales_category.iloc[0]["Category"]

top_region = sales_region.iloc[0]["Region"]

col1, col2, col3 = st.columns(3)

col1.success(
    f"🏆 Top State\n\n{top_state}"
)

col2.info(
    f"📦 Top Category\n\n{top_category}"
)

col3.warning(
    f"🌍 Top Region\n\n{top_region}"
)

st.divider()

st.header("💡 Suggested Questions")

questions = [

    "Which state generated the highest sales?",

    "Top 5 customers by sales",

    "Top 10 products by sales",

    "Which category made highest profit?",

    "Average discount by segment",

    "Lowest profit state",

    "Top region by sales"

]

for q in questions:

    st.markdown(f"• {q}")

st.divider()

# ==========================================================
# AI ANALYST
# ==========================================================

st.header("🤖 AI Business Analyst")

# Session History
if "history" not in st.session_state:
    st.session_state.history = []

question = st.text_input(
    "Ask anything about your sales data",
    placeholder="Example: Which state generated the highest sales?"
)

if st.button("Analyze"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("🧠 AI is understanding your question..."):

            # Route Question
            router = route_question(question)

            # Analyze Data
            analysis = analyzer.analyze(router)

            # AI Explanation
            explanation = explain_result(
                question,
                analysis
            )

            # Save History
            st.session_state.history.append({
                "Question": question,
                "Router": router,
                "Result": analysis,
                "Explanation": explanation
            })

        # -----------------------------
        # Router Output
        # -----------------------------
        st.subheader("🧠 Router Output")
        st.json(router)

        # -----------------------------
        # Analysis Result
        # -----------------------------
        if analysis["success"]:

            result_df = analysis["result"].reset_index()

            st.subheader("📊 Analysis Result")

            st.dataframe(result_df)

            st.metric(
                "Rows Returned",
                len(result_df)
            )

            # CSV Download
            csv = dataframe_to_csv(result_df)

            st.download_button(
                "📥 Download CSV",
                data=csv,
                file_name="analysis_result.csv",
                mime="text/csv"
            )

            # -----------------------------
            # AI Explanation
            # -----------------------------
            st.subheader("🤖 AI Explanation")

            st.success(explanation)

            # -----------------------------
            # AI Report
            # -----------------------------
            report = f"""
AI SALES REPORT
==============================

Question:
{question}

------------------------------

Router Output:
{router}

------------------------------

Analysis Result:

{result_df.to_string(index=False)}

------------------------------

AI Explanation:

{explanation}
"""

            st.download_button(
                "📄 Download AI Report",
                data=report,
                file_name="AI_Report.txt",
                mime="text/plain"
            )

        else:

            st.error(analysis["message"])


# ==========================================================
# CHAT HISTORY
# ==========================================================

st.divider()

st.header("🕓 Previous Questions")

for item in reversed(st.session_state.history):

    with st.expander(item["Question"]):

        st.subheader("🧠 Router")

        st.json(item["Router"])

        if item["Result"]["success"]:

            st.dataframe(
                item["Result"]["result"].reset_index()
            )

        else:

            st.error(item["Result"]["message"])

        st.subheader("🤖 AI Explanation")

        st.write(item["Explanation"])