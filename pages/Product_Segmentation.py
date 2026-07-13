import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Product Segmentation",
    layout="wide"
)

st.title("📦 Product Demand Segmentation")

@st.cache_data
def load():

    return pd.read_csv(
        "outputs/product_segments.csv"
    )

df = load()

# KPIs

c1,c2,c3 = st.columns(3)

c1.metric(
    "Products",
    len(df)
)

c2.metric(
    "Segments",
    df["Segment"].nunique()
)

c3.metric(
    "Revenue",
    f"${df['Total_Sales'].sum():,.0f}"
)

st.divider()

fig = px.bar(

    df.groupby("Segment")["Total_Sales"]

    .sum()

    .reset_index(),

    x="Segment",

    y="Total_Sales",

    color="Segment",

    title="Revenue by Segment"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig = px.pie(

    df,

    names="Segment",

    title="Product Distribution"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(
    df,
    use_container_width=True
)

st.info("""

Business Insight

High-demand products should receive inventory priority.

Medium-demand products should be promoted.

Low-demand products should be reviewed for optimization.

""")