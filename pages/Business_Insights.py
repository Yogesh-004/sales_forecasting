import streamlit as st

st.set_page_config(
    page_title="Business Insights",
    layout="wide"
)

st.title("💡 Executive Business Insights")

st.success("""

### Key Findings

• XGBoost delivered the best forecasting performance.

• Product demand is concentrated in a small number of high-performing products.

• Several unusual sales spikes were detected that may correspond to promotional campaigns.

• Sales exhibit clear seasonal and weekly patterns.

• High-demand products should receive inventory priority.

""")

st.warning("""

### Recommendations

1. Deploy XGBoost for demand forecasting.

2. Increase inventory for high-demand products.

3. Monitor anomaly days weekly.

4. Focus marketing on medium-demand products.

5. Continuously retrain forecasting models with new data.

""")

st.info("""

### Project Summary

This dashboard integrates

✔ Sales Analytics

✔ Forecasting

✔ Anomaly Detection

✔ Product Segmentation

into a unified Business Intelligence platform.

""")