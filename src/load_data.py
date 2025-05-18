import yfinance as yf

data = yf.download("AAPL", start="2010-01-01", end="2025-04-30")

data.to_csv("../../data/aapl.csv")
