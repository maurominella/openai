# filename: plot_stock_price_ytd.py
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the tickers and the YTD period
tickers = ["META", "TSLA"]
start_date = "2024-01-01"
end_date = "2024-04-09"

# Fetch the historical data for both tickers
data = yf.download(tickers, start=start_date, end=end_date)['Close']

# Save the data to CSV
data.to_csv('stock_price_ytd.csv')

# Plot the normalized stock price change YTD
(data / data.iloc[0] * 100).plot(figsize=(10, 6))

# Title and labels
plt.title('YTD Stock Price Change for META and TESLA')
plt.ylabel('Normalized Price (%)')
plt.xlabel('Date')

# Save the plot to a PNG file
plt.savefig('stock_price_ytd.png')

# Show the plot
plt.show()