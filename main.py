# Entry point of the program. Handles user input and uses helper modules.

from fetch_data import get_stock_data
from charting import plot_candlestick
from forecasting import forecast_stock

def main():
    print("Welcome to the S&P 500 tracker and forecaster program")
    symbol = input("Enter stock ticker/symbol(eg., AAPL, TSLA or ^GSPC for S&P 500):")
    interval = input("Enter interval(1d, 1h, 15m, etc):")
    period = input("Enter period (1mo, 6mo, 1y, etc):")

    df = get_stock_data(symbol, period, interval)
    plot_candlestick(df, symbol)
    forecast_stock(df, symbol)

if __name__ == "__main__":
    main()