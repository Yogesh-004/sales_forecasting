import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Anomaly Detection", layout="wide")

st.title("🚨 Sales Anomaly Detection")

st.markdown(
"""
Identify unusual sales patterns that may indicate promotions,
seasonal demand, or unexpected business events.
"""
)

# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("outputs/anomalies.csv")

anomaly_df = load_data()

# ---------------------------------------------------------
# KPI
# ---------------------------------------------------------

total = len(anomaly_df)

anomalies = anomaly_df["Anomaly"].sum()

high = (anomaly_df["Anomaly Type"]=="High Sales").sum()

low = (anomaly_df["Anomaly Type"]=="Low Sales").sum()

c1,c2,c3,c4 = st.columns(4)

c1.metric("Days",total)

c2.metric("Anomalies",anomalies)

c3.metric("High Sales",high)

c4.metric("Low Sales",low)

st.divider()

# ---------------------------------------------------------
# CHART
# ---------------------------------------------------------

fig = px.line(
    anomaly_df,
    x="Date",
    y="Sales",
    title="Daily Sales"
)

fig.add_scatter(

    x=anomaly_df[anomaly_df["Anomaly"]]["Date"],

    y=anomaly_df[anomaly_df["Anomaly"]]["Sales"],

    mode="markers",

    marker=dict(color="red",size=10),

    name="Anomaly"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------------
# TABLE
# ---------------------------------------------------------

st.subheader("Detected Anomalies")

st.dataframe(

    anomaly_df[
        anomaly_df["Anomaly"]
    ],

    use_container_width=True

)

# ---------------------------------------------------------
# BUSINESS INSIGHT
# ---------------------------------------------------------

st.success("""

Business Insight

• High sales anomalies may indicate successful promotions.

• Low sales anomalies may indicate supply issues or weak demand.

• Monitoring anomalies helps improve inventory planning.

""")