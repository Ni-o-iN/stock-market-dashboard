import yfinance as yf 
import streamlit as st
import plotly.express as px
import pandas as pd


st.set_page_config(page_title="Stock Market Dashboard", layout="wide")

st.title("📈 Stock Market Dashboard")

tickers = ["AAPL", "MSFT", "GOOGL", "TSLA", "NVDA", "META", "AMZN", "NFLX"]

period = st.selectbox(
    "Period",
    ["1mo", "3mo", "6mo", "1y", "5y", "max"]
)

st.markdown("---")

all_data = {}
for ticker in tickers:
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    all_data[ticker] = data

normalized_data = pd.DataFrame()

for ticker, data in all_data.items():
    close_prices = data["Close"]
    normalized = (close_prices / close_prices.iloc[0]) * 100
    normalized_data[ticker] = normalized

st.subheader("📊 All stocks (normalized)")

fig = px.line(
    normalized_data,
    title="Performance comparison (Start = 100%)",
    labels={"value": "Performance (%)", "index": "Date", "variable": "stocks"}
)

st.plotly_chart(fig, use_container_width=True)