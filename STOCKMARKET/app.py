import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import streamlit as st


start = '2010-01-01'
end = '2019-12-31'


st.title('Stock Trend Prediction')

user_input = st.text_input('Enter Stock Ticker', 'AAPL')
df = data.DataReader(user_input , 'yahoo',start,end)

#Describing Data
st.subheader('Data from 2010 - 2019')
st.write(df.describe())    