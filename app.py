import streamlit as st
import pandas as pd
from prophet import Prophet

st.set_page_config(page_title="Smart Lab AI", layout="wide")

st.title("AI-Driven Diagnostic Reagent Demand Predictor")

with st.sidebar:
    st.header("Configuration")
    uploaded_file = st.file_uploader("Upload historical lab data (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    test_columns = [col for col in df.columns if col != "Date"]

    with st.sidebar:
        selected_test = st.selectbox("Select a test to analyze", options=test_columns)

    # Run Prophet forecast
    prophet_df = df[["Date", selected_test]].rename(columns={"Date": "ds", selected_test: "y"})
    prophet_df["ds"] = pd.to_datetime(prophet_df["ds"])

    model = Prophet()
    model.fit(prophet_df)

    future = model.make_future_dataframe(periods=14)
    forecast = model.predict(future)

    future_forecast = forecast.tail(14)
    total_kits = int(round(future_forecast["yhat"].sum()))
    daily_avg = round(df[selected_test].mean(), 1)

    first_day = future_forecast["yhat"].iloc[0]
    last_day = future_forecast["yhat"].iloc[-1]
    surge = last_day > first_day * 1.20

    # 3-column metrics row
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Historical Daily Average", value=daily_avg)

    with col2:
        st.metric(label=f"Recommended Kits to Order (Next 14 Days)", value=total_kits)

    with col3:
        st.subheader("AI Surge Alert")
        if surge:
            st.error("⚠️ High Demand Surge Predicted!")
        else:
            st.success("✅ Stable Demand Expected")

    # Tabs
    tab1, tab2 = st.tabs(["📈 AI Forecast Analysis", "📊 Historical Raw Data"])

    with tab1:
        st.subheader(f"14-Day AI Demand Forecast: {selected_test}")
        st.line_chart(future_forecast.set_index("ds")["yhat"])

    with tab2:
        st.subheader("Raw Data")
        st.dataframe(df)

        st.subheader(f"Historical Trend: {selected_test}")
        st.line_chart(df.set_index("Date")[selected_test])

else:
    st.info("👈 Upload a CSV file from the sidebar to get started.")

