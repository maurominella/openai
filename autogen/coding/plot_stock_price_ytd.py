# filename: plot_stock_price_ytd.py
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Define the tickers and their labels
tickers = ["META", "TSLA"]
labels = ["Meta Platforms, Inc.", "Tesla, Inc."]

# Define the start date for the YTD period and today's date
start_date = "2024-01-01"
end_date = "2024-04-09"  # Today's date

# Initialize a DataFrame to store the closing prices
closing_prices = pd.DataFrame()

# Fetch and store the closing prices for each ticker
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    closing_prices[ticker] = data['Close']

# Save the closing prices data to CSV
closing_prices.to_csv('stock_price_ytd.csv')

# Plot the stock price changes YTD
plt.figure(figsize=(14, 7))
for ticker, label in zip(tickers, labels):
    plt.plot(closing_prices.index, closing_prices[ticker], label=label)

# Formatting the plot
plt.title('Stock Price Change YTD for META and TESLA')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)

# Save the plot to a PNG file
plt.savefig('stock_price_ytd.png')

# Show the plot
plt.show()