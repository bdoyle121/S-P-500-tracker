# Uses Prophet to forecast future stock prices

from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt

def forecast_stock(df, ticker):
    print(f"Generating forecast for {ticker}...")
    data = df.reset_index()[['Date', 'Close']].rename(colums={'Date': 'ds', 'Close': 'y'})
    model = Prophet()
    model.fit(data)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)


    fig = model.plot(forecast)
    plt.title(f"30-Day Forecast for {ticker}")
    plt.show()
