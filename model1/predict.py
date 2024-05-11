import pandas as pd
import numpy as np 
import streamlit as st
import pickle
from streamlit_option_menu import option_menu


def prediction(dataframe):

    model = pickle.load(open('model1.pkl','rb'))
    
    price = model.predict(dataframe)

    
    st.header(":red[Car Price]" ,divider = 'rainbow')
    header_color = 'orange'

    st.markdown(f"<h1 style='color:{header_color}'> {price[0]//1}</h1>", unsafe_allow_html=True)
    st.success("Thanks for using")

   


