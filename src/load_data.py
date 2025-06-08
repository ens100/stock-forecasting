import yfinance as yf

data = yf.download("TSLA", start="2010-01-01")

data.columns = data.columns.get_level_values(0)

data.to_csv("data/tsla.csv")
