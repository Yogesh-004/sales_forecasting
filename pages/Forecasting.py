import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Forecasting",
    layout="wide"
)

st.title("📈 Sales Forecasting Dashboard")

st.markdown("""
This page compares multiple forecasting models and visualizes
future sales trends to support business planning.
""")

# ==========================================================
# LOAD FORECAST RESULTS
# ==========================================================

@st.cache_data
def load_forecast():

    actual = pd.read_csv("outputs/actual_sales.csv")

    baseline = pd.read_csv("outputs/baseline_forecast.csv")

    xgb = pd.read_csv("outputs/xgboost_forecast.csv")

    prophet = pd.read_csv("outputs/prophet_forecast.csv")

    sarima = pd.read_csv("outputs/sarima_forecast.csv")

    comparison = pd.read_csv("outputs/model_comparison.csv")

    future = pd.read_csv("outputs/future_forecast.csv")

    return (
        actual,
        baseline,
        xgb,
        prophet,
        sarima,
        comparison,
        future
    )

(
actual,
baseline,
xgb,
prophet,
sarima,
comparison,
future
)=load_forecast()

# ==========================================================
# FORECAST COMPARISON
# ==========================================================

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=actual["Date"],
        y=actual["Sales"],
        name="Actual"
    )
)

fig.add_trace(
    go.Scatter(
        x=baseline["Date"],
        y=baseline["Prediction"],
        name="Baseline"
    )
)

fig.add_trace(
    go.Scatter(
        x=xgb["Date"],
        y=xgb["Prediction"],
        name="XGBoost"
    )
)

fig.add_trace(
    go.Scatter(
        x=prophet["Date"],
        y=prophet["Prediction"],
        name="Prophet"
    )
)

fig.add_trace(
    go.Scatter(
        x=sarima["Date"],
        y=sarima["Prediction"],
        name="SARIMA"
    )
)

fig.update_layout(
    title="Actual vs Forecast",
    xaxis_title="Date",
    yaxis_title="Sales"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("🏆 Model Performance")

st.dataframe(
    comparison,
    use_container_width=True
)

best = comparison.sort_values(
    "RMSE"
).iloc[0]

st.success(

f"""
Best Performing Model

Model : {best['Model']}

RMSE : {best['RMSE']:.2f}

MAE : {best['MAE']:.2f}

R² : {best['R²']:.3f}
"""

)

fig = go.Figure()

fig.add_trace(

go.Scatter(

x=future["Date"],

y=future["Forecast"],

name="Forecast"

)

)

fig.update_layout(

title="30-Day Sales Forecast",

xaxis_title="Date",

yaxis_title="Predicted Sales"

)

st.plotly_chart(

fig,

use_container_width=True

)

st.info("""

### Business Recommendation

• Use XGBoost for operational sales forecasting.

• Review inventory before expected sales peaks.

• Monitor demand changes regularly.

• Update the forecasting model monthly using new sales data.

""")