import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
# Simple Stock Price App

show are the stock closing price and volume of Google!

""")

# we can (customize the style)modify the display using markdown, we can add list,
# links, images, tables, headings, text style etc

tickerSymbol = "GOOL"

tickerData = yf.Ticker(tickerSymbol)

tickerOf=tickerData.histroy(period='id', start='2010-5-31', end='2020-5-21')


# charts for the website
st.wrtie("Closing price")
st.line_chart(tickerOf.Close)
st.write("Volume")
st.line_chart(tickerOf.Volume)