# filename: fetch_stock_data.py
import yfinance as yf

# Define the tickers for Meta Platforms, Inc. and Tesla, Inc.
tickers = ["META", "TSLA"]

# Define the start and end dates for YTD
start_date = "2024-01-01"
end_date = "2024-06-01"

# Fetch the stock data
meta_data = yf.download("META", start=start_date, end=end_date)
tesla_data = yf.download("TSLA", start=start_date, end=end_date)

# Calculate the YTD gain for each stock
meta_ytd_gain = ((meta_data['Close'][-1] - meta_data['Open'][0]) / meta_data['Open'][0]) * 100
tesla_ytd_gain = ((tesla_data['Close'][-1] - tesla_data['Open'][0]) / tesla_data['Open'][0]) * 100

# Print the YTD gains
print(f"META YTD Gain: {meta_ytd_gain:.2f}%")
print(f"TESLA YTD Gain: {tesla_ytd_gain:.2f}%")