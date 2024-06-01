# filename: plot_and_save_stock_data.py
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the tickers and the time period for YTD
tickers = ["META", "TSLA"]
start_date = "2024-01-01"
end_date = "2024-06-01"

# Fetch the stock data
data = yf.download(tickers, start=start_date, end=end_date)['Close']

# Save the data to CSV
data.to_csv('stock_price_ytd.csv')

# Plot the data
plt.figure(figsize=(10, 6))
for ticker in tickers:
    plt.plot(data.index, data[ticker], label=ticker)

plt.title('YTD Stock Price Change for META and TESLA')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)

# Save the plot to a PNG file
plt.savefig('stock_price_ytd.png')
plt.show()