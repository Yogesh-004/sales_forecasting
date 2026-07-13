import streamlit as st

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Intelligent Sales Forecasting & Demand Analytics Dashboard")

st.markdown("""
Welcome to the **Intelligent Sales Forecasting and Demand Analytics Dashboard**.

This application provides an end-to-end business intelligence solution built using machine learning and time series forecasting techniques.

### Features

- 📊 Sales Performance Analysis
- 📈 Sales Forecasting
- 🚨 Anomaly Detection
- 📦 Product Demand Segmentation
- 💡 Business Recommendations

Use the navigation menu on the left to explore each module.
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Forecasting Models", "4")

with col2:
    st.metric("Business Modules", "5")

with col3:
    st.metric("Dataset", "Superstore Sales")

st.success("Dashboard initialized successfully. Use the sidebar to navigate through the analytics modules.")