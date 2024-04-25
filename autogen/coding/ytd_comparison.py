# filename: ytd_comparison.py
import yfinance as yf
from datetime import datetime

# Function to fetch the closing price of a stock on a given date
def get_stock_price_on_date(ticker_symbol, date):
    stock = yf.Ticker(ticker_symbol)
    hist = stock.history(start=date, end=date)
    if not hist.empty:
        return hist['Close'][0]
    return None

# Function to calculate YTD gain
def calculate_ytd_gain(ticker_symbol):
    # Define the start of the year
    start_of_year = datetime.now().year - 1
    start_of_year_date = f"{start_of_year}-01-01"
    # Define today's date
    today_date = datetime.now().strftime('%Y-%m-%d')
    
    # Fetch the stock prices
    start_price = get_stock_price_on_date(ticker_symbol, start_of_year_date)
    current_price = get_stock_price_on_date(ticker_symbol, today_date)
    
    # Calculate YTD gain
    if start_price and current_price:
        ytd_gain = ((current_price - start_price) / start_price) * 100
        return ytd_gain
    else:
        return "Data not available"

# Calculate YTD gains for META and TESLA
meta_ytd_gain = calculate_ytd_gain("META")
tesla_ytd_gain = calculate_ytd_gain("TSLA")

# Print the YTD gains
print(f"META YTD Gain: {meta_ytd_gain:.2f}%")
print(f"TESLA YTD Gain: {tesla_ytd_gain:.2f}%")