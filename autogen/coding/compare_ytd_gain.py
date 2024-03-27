# filename: compare_ytd_gain.py
import yfinance as yf
from datetime import datetime

# Function to calculate YTD gain
def calculate_ytd_gain(ticker):
    # Get data for the current year
    now = datetime.now()
    start_of_year = datetime(now.year, 1, 1)
    stock_data = yf.download(ticker, start=start_of_year, end=now)
    
    # Calculate YTD gain
    if not stock_data.empty:
        start_price = stock_data['Open'].iloc[0]
        current_price = stock_data['Close'].iloc[-1]
        ytd_gain = ((current_price - start_price) / start_price) * 100
        return ytd_gain
    else:
        return None

# Get YTD gain for META and TESLA
meta_ytd_gain = calculate_ytd_gain('META')
tesla_ytd_gain = calculate_ytd_gain('TSLA')

# Print the YTD gains
print(f"META YTD Gain: {meta_ytd_gain:.2f}%")
print(f"TESLA YTD Gain: {tesla_ytd_gain:.2f}%")