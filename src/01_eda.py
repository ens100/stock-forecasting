import pandas as pd
import numpy as np
import plotly.express as px

# Import the data, drop the two first headers and rename any headers
stock_df = pd.read_csv("../data/tsla.csv", parse_dates=["Date"], index_col=["Date"])

### Summary Stats
stock_df.info()
stock_df.describe()
stock_df.head()
stock_df.tail()

# Confirm there are no null values in dataset
stock_df.isnull().sum()

### Adding Day, month, year coluuns
stock_df["day"] = stock_df.index.day
stock_df["month"] = stock_df.index.month
stock_df["year"] = stock_df.index.year

stock_df.head()

### Finding max / min close value
stock_df["Close"].max()
stock_df.loc[stock_df["Close"] == stock_df["Close"].max()]
stock_df.loc[stock_df["Close"] == stock_df["Close"].min()]

# Or can use
stock_df.loc[stock_df["Close"].idxmax()]

# Convert the data from daily to monthly averages
monthly_df = stock_df.resample("ME").mean()
monthly_df.head()

###  VISUAL

fig = px.line(stock_df["Close"], title="Tesla Daily Closing Price")
fig.show()

# Create a Year over Year graph starting from 2020
fig_yoy = px.line(
    monthly_df.query("year >= 2020"), x="month", y="Close", color="year", title="Tesla Monthly Average Price Y-o-Y"
)
fig_yoy.show()
