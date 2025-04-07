# This program will start by pulling stock data from Yahoo Finance

import yfinance as yf


def get_stock_data(ticker: str, period: str, interval: str):
    print(f"Fetching data for {ticker}...")
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)
    return df
