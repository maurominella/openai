import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
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

# Save the data to a CSV file
data.to_csv('stock_price_ytd.csv')

# Plot the stock price changes YTD
plt.figure(figsize=(10, 6))
for stock in stocks:
    plt.plot(data['Close'][stock], label=stock)

plt.title('Stock Price Change YTD')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend()
plt.grid(True)
plt.savefig('stock_price_ytd.png')
plt.show()
