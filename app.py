import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(
    page_title="FAANG & Crypto Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title('FAANG & CRYPTO Dashboard')
st.write(
    "Explore historical price performance and cumulative returns "
    "for selected stocks and cryptocurrencies."
)

tickers = ('TSLA', 'AAPL', 'MSFT','META' ,'AMZN', 'GOOGL', 'NFLX', 'BTC-USD', 'ETH-USD', 'XRP-USD', 'LTC-USD', 'BCH-USD')

dropdown = st.multiselect('Pick your assets', tickers)

start = st.date_input('Start', value=pd.to_datetime('2020-01-01'))
end = st.date_input('End', value=pd.to_datetime('today'))

def relativeret(df):
    rel = df.pct_change()
    cumret = (1 + rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret

if start >= end:
    st.error("The start date must be earlier than the end date.")


elif len(dropdown) == 0:
    with st.spinner("Downloading market data..."):
        try:
            df = yf.download(
                dropdown,
                start=start,
                end=end,
                auto_adjust=False,
                progress=False
            )

            if df.empty:
                st.warning(
                    "No market data was returned. "
                    "Check the selected assets and dates."
                )
        except Exception as e:
            st.error(f"Failed to download market data: {e}")

elif len(dropdown) > 0:
    df = relativeret(yf.download(dropdown, start, end, auto_adjust=False)['Adj Close'])
    st.header('Returns of {}'.format(dropdown))
    st.line_chart(df)





