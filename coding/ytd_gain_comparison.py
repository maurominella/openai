# filename: ytd_gain_comparison.py

import yfinance as yf
from datetime import datetime

# Define the tickers for Meta Platforms and Tesla
tickers = ["META", "TSLA"]

# Define the start of the current year
start_of_year = datetime(2024, 1, 1)

# Get the current date
current_date = datetime.now()

# Initialize a dictionary to store YTD gains
ytd_gains = {}

# Retrieve and calculate the YTD gain for each ticker
for ticker in tickers:
    stock = yf.Ticker(ticker)
    
    # Get historical data from the start of the year until now
    hist = stock.history(start=start_of_year.strftime('%Y-%m-%d'), end=current_date.strftime('%Y-%m-%d'))
    
    # Get the opening price of the first trading day of the year and the latest closing price
    opening_price = hist.iloc[0]['Open']
    latest_price = hist.iloc[-1]['Close']
    
    # Calculate the YTD gain
    ytd_gain = ((latest_price - opening_price) / opening_price) * 100
    
    # Store the YTD gain in the dictionary
    ytd_gains[ticker] = ytd_gain

# Print the YTD gains for comparison
print(f"YTD gain for META: {ytd_gains['META']:.2f}%")
print(f"YTD gain for TSLA: {ytd_gains['TSLA']:.2f}%")

# Compare the YTD gains and print which one is higher
if ytd_gains['META'] > ytd_gains['TSLA']:
    print("META has a higher YTD gain than TESLA.")
elif ytd_gains['META'] < ytd_gains['TSLA']:
    print("TESLA has a higher YTD gain than META.")
else:
    print("META and TESLA have the same YTD gain.")