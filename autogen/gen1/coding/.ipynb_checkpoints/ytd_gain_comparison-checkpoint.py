import yfinance as yf
from datetime import datetime

# Get the current date
current_date = datetime.now().strftime('%Y-%m-%d')
print(f"Current Date: {current_date}")

# Define the stock symbols
stocks = ['META', 'TSLA']

# Get the stock data for the beginning of the year and the current date
start_of_year = f"{datetime.now().year}-01-01"

# Fetch stock data
data = yf.download(stocks, start=start_of_year, end=current_date)

# Get the opening price at the start of the year and the latest closing price
start_prices = data['Open'].iloc[0]
end_prices = data['Close'].iloc[-1]

# Calculate the YTD gain
ytd_gain = ((end_prices - start_prices) / start_prices) * 100

# Print the YTD gain for each stock
for stock in stocks:
    print(f"YTD Gain for {stock}: {ytd_gain[stock]:.2f}%")
