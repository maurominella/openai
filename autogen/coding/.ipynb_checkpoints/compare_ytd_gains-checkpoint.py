# filename: compare_ytd_gains.py
import yfinance as yf
from datetime import datetime

# Define the tickers for Meta Platforms, Inc. and Tesla, Inc.
tickers = ["META", "TSLA"]

# Define the start and end dates for the YTD period
start_date = "2024-01-01"
end_date = "2024-04-09"  # Today's date

# Function to calculate YTD gain
def calculate_ytd_gain(ticker):
    # Fetch the historical data for the ticker
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Get the closing prices at the start and end of the period
    start_price = data['Close'].iloc[0]
    end_price = data['Close'].iloc[-1]
    
    # Calculate the YTD gain
    ytd_gain = ((end_price - start_price) / start_price) * 100
    
    return ytd_gain

# Calculate and print the YTD gains for both stocks
for ticker in tickers:
    ytd_gain = calculate_ytd_gain(ticker)
    print(f"{ticker} YTD Gain: {ytd_gain:.2f}%")