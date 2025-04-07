import streamlit as st
import pickle
import yfinance as yf
import numpy as np

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

ticker = 'AAPL'  
stock_data = yf.download(ticker, period="3mo", interval="1d")  

# Display Stock Data
st.title("Stock Market Prediction Dashboard")
st.subheader("Stock Data")
st.write(stock_data)  

# Check the number of rows in stock_data
st.write(f"Number of rows in the stock data: {len(stock_data)}")

sentiment_data = np.random.rand(len(stock_data), 1) 
window_size = 30

if len(stock_data) >= window_size:

    last_30_stock = stock_data[['Open']].tail(window_size).values 
    last_30_sentiment = sentiment_data[-window_size:] 

    
    X_last = np.column_stack((last_30_stock[:, 0], last_30_sentiment[:, 0]))  
    X_last = X_last.reshape(1, window_size, 2)  

    if st.button('Predict'):
        prediction = model.predict(X_last)
        st.write(f"Predicted Stock Price for {ticker}: {prediction[0]}")
else:
    st.write("Not enough data to make a prediction.")
