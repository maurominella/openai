# filename: plot_stock_prices.py
import pandas as pd
import matplotlib.pyplot as plt

# Simulated stock prices for META and TESLA (YTD)
data = {
    'Date': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-03-29'],
    'META': [150, 155, 160, 165.2],
    'TESLA': [100, 105, 110, 118.7]
}

# Create a DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])  # Convert Date column to datetime

# Save the DataFrame to CSV
df.to_csv('stock_price_ytd.csv', index=False)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['META'], label='META', marker='o')
plt.plot(df['Date'], df['TESLA'], label='TESLA', marker='o')

# Adding titles and labels
plt.title('Stock Price Change YTD for META and TESLA')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend()

# Save the plot to a PNG file
plt.savefig('stock_price_ytd.png')

# Show the plot
plt.show()