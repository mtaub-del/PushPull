import pandas as pd
import yfinance as yf
import numpy as np 
df_apple = yf.download("AAPL", start="2024-01-01", end= "2024-12-31")
df_apple["Daily_Return"] = df_apple["Close"].pct_change() 

df_apple["Log_Return"] = np.log(df_apple["Close"] / df_apple["Close"].shift(1))
print(df_apple["Log_Return"].head())
print(df_apple["Log_Return"].max())
print(df_apple["Daily_Return"].mean())