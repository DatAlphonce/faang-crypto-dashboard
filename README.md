# FAANG & Crypto Dashboard

An interactive financial analytics application built with Python and Streamlit for exploring historical stock and cryptocurrency performance.
https://faang-crypto-dashboard-ar5u9mdpeevnangnvdm2in.streamlit.app/

## Features

- Select multiple stocks and cryptocurrencies.
- Choose a historical date range.
- Retrieve market data using Yahoo Finance through `yfinance`.
- Calculate cumulative returns from historical prices.
- Compare asset performance using an interactive line chart.

## Technology Stack

- Python
- Streamlit
- Pandas
- yfinance

## Run Locally

1. Clone this repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Start the application using `streamlit run app.py`.

## Data and Limitations

Market data is retrieved from Yahoo Finance through the `yfinance` library. Data availability and coverage may vary by asset.

This project is for educational and analytical purposes. It does not provide personalized investment advice or guarantee future investment performance.

## Future Improvements

- Portfolio volatility and drawdown analysis
- Asset correlation matrix
- Value at Risk (VaR) and Expected Shortfall (ES)
- Portfolio optimization
- Downloadable analysis reports