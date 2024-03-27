# filename: calculate_ytd_gain.py

# Replace these variables with the actual prices
meta_beginning_of_year_price = 0  # Replace 0 with the META price at the beginning of the year
meta_current_price = 0            # Replace 0 with the current META price

tesla_beginning_of_year_price = 0 # Replace 0 with the TESLA price at the beginning of the year
tesla_current_price = 0           # Replace 0 with the current TESLA price

# Ensure that the beginning of year prices are not zero to avoid division by zero
if meta_beginning_of_year_price == 0 or tesla_beginning_of_year_price == 0:
    print("Please make sure to replace the beginning of year prices with actual non-zero values.")
else:
    # Calculate YTD gains
    meta_ytd_gain = (meta_current_price - meta_beginning_of_year_price) / meta_beginning_of_year_price * 100
    tesla_ytd_gain = (tesla_current_price - tesla_beginning_of_year_price) / tesla_beginning_of_year_price * 100

    # Print YTD gains
    print(f"META YTD Gain: {meta_ytd_gain:.2f}%")
    print(f"TESLA YTD Gain: {tesla_ytd_gain:.2f}%")

    # Compare YTD gains
    if meta_ytd_gain > tesla_ytd_gain:
        print("META has a higher YTD gain than TESLA.")
    elif meta_ytd_gain < tesla_ytd_gain:
        print("TESLA has a higher YTD gain than META.")
    else:
        print("META and TESLA have the same YTD gain.")