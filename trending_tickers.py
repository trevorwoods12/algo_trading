import pandas as pd
import yahooquery as yq
from yahooquery import Ticker
import datetime
'''
This code creates a trending_ticker.csv file of the trending tickers on yahoo finance and their post-market percent change.
,ticker,pct_change
0, UBER, 0.002312
'''
# Get the list of trending tickers
data = yq.get_trending()
today = datetime.date.today()
print(today)

# Create empty lists
tickers = []
pct_change = []

# Iterate for every item in the trending ticker list
for item in data['quotes']:
    # Store symbol in format 'AAPL'
    symbol = str(item['symbol'])
    if '^' not in symbol:
        # Create ticker object for each symbol in trending stock data
        ticker = Ticker(symbol)
        # Store value of each ticker
        values = ticker.price[symbol]
        # Append symbol and post market percent change to lists
        tickers.append(symbol)
        pct_change.append(values['postMarketChangePercent'])


dict = {'ticker': tickers, 'pct_change' : pct_change}
df = pd.DataFrame(dict)
df.to_csv('trending_tickers.csv', mode='w', header=True)
print(df)