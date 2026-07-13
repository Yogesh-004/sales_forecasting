import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(page_title="Sales Overview", layout="wide")

st.title("📊 Sales Overview Dashboard")

# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():

    df = pd.read_csv("train.csv")

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        dayfirst=True,
        errors="coerce"
    )

    # Create time features
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    df["Month Name"] = df["Order Date"].dt.month_name()
    df["Quarter"] = df["Order Date"].dt.quarter

    return df

df = load_data()

# ==========================================================
# SIDEBAR FILTERS
# ==========================================================

st.sidebar.header("Filters")

year = st.sidebar.multiselect(
    "Year",
    sorted(df["Year"].unique()),
    default=sorted(df["Year"].unique())
)

region = st.sidebar.multiselect(
    "Region",
    sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

category = st.sidebar.multiselect(
    "Category",
    sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

filtered = df[
    (df["Year"].isin(year)) &
    (df["Region"].isin(region)) &
    (df["Category"].isin(category))
]

# ==========================================================
# KPI CARDS
# ==========================================================

total_sales = filtered["Sales"].sum()

total_orders = filtered["Order ID"].nunique()

total_products = filtered["Product Name"].nunique()

avg_order = filtered["Sales"].mean()

c1, c2, c3, c4 = st.columns(4)

c1.metric("💰 Total Sales", f"${total_sales:,.0f}")

c2.metric("📦 Orders", total_orders)

c3.metric("🛍 Products", total_products)

c4.metric("📈 Avg Order Value", f"${avg_order:,.2f}")

st.divider()

# ==========================================================
# MONTHLY SALES
# ==========================================================

monthly = (
    filtered
    .groupby(["Year", "Month"])["Sales"]
    .sum()
    .reset_index()
)

monthly["Period"] = (
    monthly["Year"].astype(str)
    + "-"
    + monthly["Month"].astype(str)
)

fig = px.line(
    monthly,
    x="Period",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# CATEGORY & REGION
# ==========================================================

left, right = st.columns(2)

with left:

    category_sales = (
        filtered
        .groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        category_sales,
        x="Category",
        y="Sales",
        title="Sales by Category"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    region_sales = (
        filtered
        .groupby("Region")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        region_sales,
        names="Region",
        values="Sales",
        title="Regional Sales Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# TOP PRODUCTS
# ==========================================================

top_products = (
    filtered
    .groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top 10 Products by Sales"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# DATA TABLE
# ==========================================================

st.subheader("Filtered Dataset")

st.dataframe(filtered, use_container_width=True)