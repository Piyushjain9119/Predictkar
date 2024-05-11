import streamlit as st 
from streamlit_option_menu  import option_menu

import model1.car_prediction as car
import model2.house_pred as home
import home_page.home as hm
# from streamlit_extras.app_logo import add_logo
import about.about as ab

st.set_page_config(
    page_title= "PredictoHub",
    page_icon="🤖",
)



# st.title("Home")

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self,title,function):
        self.apps.append({
            'title':title,
            'function':function
        })

    
    def run():

        with st.sidebar:
            app = option_menu(

                menu_title ='PredictoHub',
                options=['Home','Car Price Prediction','House Price Prediction','About'],
                icons=['house', 'car-front','house-heart-fill','info-circle-fill'], 
                menu_icon="robot", 
                default_index=0
                )
            
        

             

        if app=='Home':
            hm.app()
        elif app=='Car Price Prediction':
            car.car_pred()
        
        elif app=='House Price Prediction':
            home.app()
        elif app=='About':
            ab.app()

    run()
    
    st.sidebar.success("select a page above")

    