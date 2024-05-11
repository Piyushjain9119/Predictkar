import pandas as pd
import numpy as np 
import streamlit as st
import pickle


def prediction(dataframe):

    model = pickle.load(open('model.pkl','rb'))
    
    price = model.predict(dataframe)

    
    st.header(":red[House Price]" ,divider = 'rainbow')
    header_color = 'orange'

    st.markdown(f"<h1 style='color:{header_color}'> {price[0]//1} lakh</h1>", unsafe_allow_html=True)
    st.success("Thanks for using")
   

    
