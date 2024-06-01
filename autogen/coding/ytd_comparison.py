# filename: ytd_comparison.py
import yfinance as yf
from datetime import datetime

# Function to calculate YTD return
def calculate_ytd_return(ticker):
    # Get data from the start of the year until today
    start_date = datetime(datetime.now().year, 1, 1)
    end_date = datetime.now()
    
    # Fetch historical market data
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Calculate the YTD return
    ytd_return = ((data['Close'][-1] - data['Open'][0]) / data['Open'][0]) * 100
    return ytd_return

# Tickers for META and TESLA
tickers = ['META', 'TSLA']

# Calculate and print YTD returns
for ticker in tickers:
    ytd_return = calculate_ytd_return(ticker)
    print(f"{ticker} YTD Return: {ytd_return:.2f}%")
