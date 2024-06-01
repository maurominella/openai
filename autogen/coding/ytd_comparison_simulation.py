# filename: ytd_comparison_simulation.py
# Simulated script to compare YTD gains for META and TESLA

# Simulated stock prices at the beginning of the year
stock_prices_start_of_year = {
    "META": 135.00,  # Simulated opening price of META at the start of 2024
    "TSLA": 250.00,  # Simulated opening price of TSLA at the start of 2024
}

# Simulated current stock prices
current_stock_prices = {
    "META": 155.00,  # Simulated current price of META
    "TSLA": 300.00,  # Simulated current price of TSLA
}

# Calculate and print YTD gains
for ticker, start_price in stock_prices_start_of_year.items():
    current_price = current_stock_prices[ticker]
    ytd_gain = ((current_price - start_price) / start_price) * 100
    print(f"{ticker} YTD Gain: {ytd_gain:.2f}%")