# This will display a candlestick chart of stocks using mplfinance

import mplfinance as mpf

def plot_candlestick(df, ticker):
    print(f"Plotting candlestick chart for {ticker}...")
    mpf.plot(df, type='candle', style='charles', title=f"{ticker} Candlestick Chart", volume=True)
    