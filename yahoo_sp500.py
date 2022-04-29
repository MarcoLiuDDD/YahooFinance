# https://algotrading101.com/learn/yahoo-finance-api-guide/

from yahoo_fin.stock_info import get_data
import yahoo_fin.stock_info as si
import matplotlib.pyplot as plt
# Pie chart, where the slices will be ordered and plotted counter-clockwise:

dow_list = si.tickers_dow()
print("Tickers in Dow Jones:", len(dow_list))
print(dow_list[0:10])

dow_historical = {}
dow_close = {}
dow_price = []

for ticker in dow_list:
    market_cap = si.get_quote_table(ticker)["Market Cap"]
    dow_historical[ticker] = si.get_data(ticker, start_date="01/01/2019", end_date="01/03/2020", interval="1d")
    dow_close[ticker] = dow_historical[ticker]["close"]
    price = float(dow_close[ticker].loc["2020-01-02"])
    dow_price.append(price)

labels = dow_list
sizes = dow_price

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
