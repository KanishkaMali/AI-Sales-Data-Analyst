# ==========================================================
# analysis.py
# Dynamic Business Analysis Engine
# ==========================================================

import pandas as pd


class BusinessAnalyzer:

    def __init__(self, df):
        self.df = df.copy()

    # ======================================================
    # KPI FUNCTIONS
    # ======================================================

    def total_sales(self):
        return self.df["Sales"].sum()

    def total_profit(self):
        return self.df["Profit"].sum()

    def total_orders(self):
        return self.df["Order ID"].nunique()

    def total_customers(self):
        return self.df["Customer ID"].nunique()

    # ======================================================
    # FILTER DATA
    # ======================================================

    def apply_filters(self, data, filters):

        if not filters:
            return data

        for column, value in filters.items():

            if column not in data.columns:
                continue

            if column == "Year":

                data = data[data["Year"] == int(value)]

            else:

                data = data[
                    data[column].astype(str).str.lower()
                    ==
                    str(value).lower()
                ]

        return data

    # ======================================================
    # GENERIC ANALYSIS ENGINE
    # ======================================================

    def analyze(self, router):

        metric = router.get("metric")
        dimension = router.get("dimension")
        operation = router.get("operation")
        filters = router.get("filters", {})
        top_n = router.get("top_n", 1)

        data = self.apply_filters(self.df.copy(), filters)

        # ----------------------------
        # Validate
        # ----------------------------

        if metric not in data.columns:
            return {
                "success": False,
                "message": f"Metric '{metric}' not found."
            }

        if dimension not in data.columns:
            return {
                "success": False,
                "message": f"Dimension '{dimension}' not found."
            }

        grouped = (
            data
            .groupby(dimension)[metric]
            .sum()
            .sort_values(ascending=False)
        )

        # ----------------------------
        # MAX
        # ----------------------------

        if operation == "max":

            result = grouped.head(1)

        # ----------------------------
        # MIN
        # ----------------------------

        elif operation == "min":

            result = grouped.tail(1)

        # ----------------------------
        # TOP
        # ----------------------------

        elif operation == "top":

            result = grouped.head(top_n)

        # ----------------------------
        # BOTTOM
        # ----------------------------

        elif operation == "bottom":

            result = grouped.tail(top_n)

        # ----------------------------
        # SUM
        # ----------------------------

        elif operation == "sum":

            result = grouped

        # ----------------------------
        # AVERAGE
        # ----------------------------

        elif operation == "average":

            result = (
                data
                .groupby(dimension)[metric]
                .mean()
                .sort_values(ascending=False)
            )

        else:

            return {
                "success": False,
                "message": "Unknown operation."
            }

        return {
            "success": True,
            "metric": metric,
            "dimension": dimension,
            "operation": operation,
            "filters": filters,
            "result": result
        }

    # ======================================================
    # CHART DATA
    # ======================================================

    def sales_by_category(self):

        return (
            self.df
            .groupby("Category")["Sales"]
            .sum()
            .reset_index()
        )

    def sales_by_region(self):

        return (
            self.df
            .groupby("Region")["Sales"]
            .sum()
            .reset_index()
        )

    def sales_by_state(self):

        return (
            self.df
            .groupby("State")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

    def monthly_sales(self):

        return (
            self.df
            .groupby("Month")["Sales"]
            .sum()
            .reset_index()
        )

    def top_customers(self):

        return (
            self.df
            .groupby("Customer Name")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

    def top_products(self):

        return (
            self.df
            .groupby("Product Name")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

    def profit_by_category(self):

        return (
            self.df
            .groupby("Category")["Profit"]
            .sum()
            .reset_index()
        )