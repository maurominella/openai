# filename: ytd_comparison.py
import yfinance as yf

def fetch_ytd_gain(ticker):
    # Fetch historical data from the start of the year until today
    stock_data = yf.download(ticker, start='2024-01-01', end='2024-03-28')
    
    # Calculate the YTD gain
    if not stock_data.empty:
        start_price = stock_data['Open'].iloc[0]
        end_price = stock_data['Close'].iloc[-1]
        ytd_gain = ((end_price - start_price) / start_price) * 100
    else:
        ytd_gain = None
    
    return ytd_gain

# Tickers for Meta Platforms, Inc. and Tesla, Inc.
tickers = ['META', 'TSLA']

# Fetch and print YTD gains
for ticker in tickers:
    ytd_gain = fetch_ytd_gain(ticker)
    if ytd_gain is not None:
        print(f"{ticker} YTD Gain: {ytd_gain:.2f}%")
    else:
        print(f"Could not fetch data for {ticker}")
