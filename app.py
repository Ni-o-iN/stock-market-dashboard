import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Stock Market Dashboard", layout="wide")

# ===== Configuration =====
tickers = ["AAPL", "MSFT", "GOOGL", "TSLA", "NVDA", "META", "AMZN", "NFLX"]

# ===== Streamlit Dashboard =====
st.title("📈 Stock Market Dashboard")

# User selects time period
period = st.selectbox(
    "Time Period:",
    ["1mo", "3mo", "6mo", "1y", "5y", "max"]
)

st.markdown("---")

# ===== Data Fetching =====
all_data = {}

for ticker in tickers:
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    all_data[ticker] = data

# ===== Data Normalization =====
# Normalize all stocks to start at 100% for fair comparison
normalized_data = pd.DataFrame()

for ticker, data in all_data.items():
    close_prices = data["Close"]
    normalized = (close_prices / close_prices.iloc[0]) * 100
    normalized_data[ticker] = normalized

# ===== Visualization =====
st.subheader("📊 Stock Performance Comparison (Normalized)")

fig = px.line(
    normalized_data,
    title="Performance Comparison (Start = 100%)",
    labels={
        "value": "Performance (%)", 
        "index": "Date", 
        "variable": "Stocks"
    }
)

st.plotly_chart(fig, use_container_width=True)
