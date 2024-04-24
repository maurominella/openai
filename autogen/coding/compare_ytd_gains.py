# filename: compare_ytd_gains.py
import yfinance as yf
from datetime import datetime

# Function to calculate YTD gain
def calculate_ytd_gain(ticker):
    # Get data from the start of the year to today
    start_date = datetime.now().strftime('%Y-01-01')
    end_date = datetime.now().strftime('%Y-%m-%d')
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Calculate the percentage change from the first available price this year to the latest
    start_price = data['Open'].iloc[0]
    end_price = data['Close'].iloc[-1]
    ytd_gain = ((end_price - start_price) / start_price) * 100
    
    return ytd_gain

# Calculate YTD gains
meta_ytd_gain = calculate_ytd_gain('META')
tesla_ytd_gain = calculate_ytd_gain('TSLA')

# Print the results
print(f"META YTD Gain: {meta_ytd_gain:.2f}%")
print(f"TESLA YTD Gain: {tesla_ytd_gain:.2f}%")