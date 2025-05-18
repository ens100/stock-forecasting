import pandas as pd
import numpy as np
import plotly.express as px

stock_df = pd.read_csv("../data/aapl.csv", parse_dates=["Date"], index_col="Date")

### Summary Stats

stock_df.info()
stock_df.describe()
stock_df.head()
stock_df.tail()

stock_df.isnull().sum()  # re-confirming there are no null values in dataset

### Adding Day, month, year coluuns

stock_df["day"] = stock_df.index.day
stock_df["month"] = stock_df.index.month
stock_df["year"] = stock_df.index.year

stock_df.head()

### Finding max close value
stock_df["Close"].max()  # Max value is 258.39666748046875
stock_df.query("Close == @stock_df['Close'].max()")
stock_df.loc[stock_df["Close"] == stock_df["Close"].max()]

# Or the above in a one liner
stock_df.loc[stock_df["Close"].idxmax()]  # returns all the data from the max value
stock_df["Close"].idxmax()  # this will just return the date from the index"

stock_df["Close"].idxmin()

monthly_df = stock_df.resample("ME").mean()
monthly_df.head()

###  VISUAL

fig = px.line(stock_df[["Close", "Volume"]], title="Apple Daily Closing Price and Volume Traded")
fig.show()

fig_yoy = px.line(
    monthly_df.query("year >= 2020"), x="month", y="Close", color="year", title="Apple Monthly Average Price Y-o-Y"
)
fig_yoy.show()
