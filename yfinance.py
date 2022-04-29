import yfinance as yf
import numpy as np
from pandas_datareader import data
import pandas as pd
import pandas_datareader as web

from yahoo_fin.stock_info import get_data
import yahoo_fin.stock_info as si
import matplotlib.pyplot as plt

#print(web.get_quote_yahoo("AAPL")['marketCap'])
#print(web.get_quote_yahoo("AAPL")['marketCap'].iloc[0])

sp500_list = si.tickers_sp500()
market_caps = []

for ticker in sp500_list:
    cap = web.get_quote_yahoo(ticker)['marketCap'].iloc[0]
    market_caps.append(cap)

labels = sp500_list
sizes = market_caps

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
