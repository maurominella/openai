# filename: stock_comparison.py
import datetime
import yfinance as yf

def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    today = datetime.date.today()
    start_of_year = datetime.date(today.year, 1, 1)
    hist = stock.history(start=start_of_year, end=today)
    first_open = hist.iloc[0]['Open']
    last_close = hist.iloc[-1]['Close']
    ytd_gain = (last_close - first_open) / first_open * 100
    return today, first_open, last_close, ytd_gain

def main():
    today, meta_first_open, meta_last_close, meta_ytd_gain = get_stock_info('META')
    _, tesla_first_open, tesla_last_close, tesla_ytd_gain = get_stock_info('TSLA')
    
    print(f"Today's date: {today}")
    print(f"META - Open price on the first trading day of the year: ${meta_first_open:.2f}")
    print(f"META - Most recent closing price: ${meta_last_close:.2f}")
    print(f"META - Year-to-date gain: {meta_ytd_gain:.2f}%")
    print(f"TESLA - Open price on the first trading day of the year: ${tesla_first_open:.2f}")
    print(f"TESLA - Most recent closing price: ${tesla_last_close:.2f}")
    print(f"TESLA - Year-to-date gain: {tesla_ytd_gain:.2f}%")

if __name__ == "__main__":
    main()