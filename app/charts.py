# ==========================================================
# charts.py
# All Plotly Chart Functions
# ==========================================================

import plotly.express as px


# ==========================================================
# SALES BY CATEGORY
# ==========================================================

def category_sales_chart(df):

    fig = px.bar(
        df,
        x="Category",
        y="Sales",
        color="Category",
        title="📦 Sales by Category",
        text_auto=".2s"
    )

    fig.update_layout(
        xaxis_title="Category",
        yaxis_title="Sales",
        title_x=0.5
    )

    return fig


# ==========================================================
# SALES BY REGION
# ==========================================================

def region_sales_chart(df):

    fig = px.pie(
        df,
        names="Region",
        values="Sales",
        title="🌍 Sales by Region",
        hole=0.4
    )

    fig.update_layout(
        title_x=0.5
    )

    return fig


# ==========================================================
# MONTHLY SALES
# ==========================================================

def monthly_sales_chart(df):

    fig = px.line(
        df,
        x="Month",
        y="Sales",
        title="📈 Monthly Sales Trend",
        markers=True
    )

    fig.update_layout(
        title_x=0.5
    )

    return fig


# ==========================================================
# TOP STATES
# ==========================================================

def state_sales_chart(df):

    fig = px.bar(
        df.head(10),
        x="State",
        y="Sales",
        color="Sales",
        title="🏆 Top 10 States by Sales",
        text_auto=".2s"
    )

    fig.update_layout(
        title_x=0.5,
        xaxis_tickangle=-45
    )

    return fig


# ==========================================================
# TOP CUSTOMERS
# ==========================================================

def customer_sales_chart(df):

    fig = px.bar(
        df.head(10),
        x="Customer Name",
        y="Sales",
        color="Sales",
        title="👤 Top 10 Customers",
        text_auto=".2s"
    )

    fig.update_layout(
        title_x=0.5,
        xaxis_tickangle=-45
    )

    return fig


# ==========================================================
# TOP PRODUCTS
# ==========================================================

def product_sales_chart(df):

    fig = px.bar(
        df.head(10),
        x="Product Name",
        y="Sales",
        color="Sales",
        title="📦 Top 10 Products",
        text_auto=".2s"
    )

    fig.update_layout(
        title_x=0.5,
        xaxis_tickangle=-45
    )

    return fig


# ==========================================================
# PROFIT BY CATEGORY
# ==========================================================

def category_profit_chart(df):

    fig = px.bar(
        df,
        x="Category",
        y="Profit",
        color="Profit",
        title="💰 Profit by Category",
        text_auto=".2s"
    )

    fig.update_layout(
        title_x=0.5
    )

    return fig