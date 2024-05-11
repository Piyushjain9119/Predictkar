import streamlit as st
from PIL import Image

def app():
    
    page_bg_img = """
    <style>

    [data-testid="stAppViewContainer"]{
    background-image :url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQd6AmpteWbLhB5kirmjmzNzDxF3fwH17_l1hylP5xCeg&s');

    background-size :cover;
    }

    </style>

    """




    st.markdown(page_bg_img,unsafe_allow_html=True)
    st.title('DESCRIPTION')

    st.header(":orange[OVERVIEW]",divider = 'rainbow')
    st.write('Machine learning (ML) has emerged as a transformative technology, revolutionizing various industries by enabling computers to learn from data and make predictions or decisions without being explicitly programmed. Its applications span across diverse domains, addressing complex challenges and unlocking new opportunities. Below, we explore the need for machine learning, its applications, advantages, and three notable projects exemplifying its capabilities.')


    st.header(":orange[Need for Machine Learning]",divider = 'rainbow')
    
    st.write('The exponential growth of data in todays digital age has necessitated advanced tools and techniques to extract meaningful insights and derive actionable intelligence. Traditional programming approaches often fall short in handling the sheer volume, variety, and velocity of data. Machine learning algorithms, on the other hand, excel in uncovering hidden patterns, making accurate predictions, and automating decision-making processes, thereby addressing the need for scalable and efficient data-driven solutions')

    st.header(":orange[Applications of Machine Learning]",divider = 'rainbow')
    st.write('Machine learning finds applications across various sectors, including healthcare, finance, e-commerce, manufacturing, and more. Some notable applications include:')
    st.write('1.Healthcare: Predictive modeling for disease diagnosis and prognosis, personalized treatment recommendation systems, and drug discovery.')
    st.write('2.Finance: Fraud detection, credit scoring, algorithmic trading, and risk management.')
    st.write('3.E-commerce: Recommender systems, customer segmentation, demand forecasting, and personalized marketing.')
    st.write('4.Manufacturing: Predictive maintenance, quality control, supply chain optimization, and process automation.')
    
    
    st.header(":orange[Advantages of Machine Learning]",divider = 'rainbow')
    st.write('1.Automation: ML enables automation of repetitive tasks, reducing manual effort and operational costs.')
    st.write('2.Scalability: ML algorithms can handle large-scale data processing and analysis efficiently.')
    st.write('3.Accuracy: ML models can make predictions with high accuracy, leading to better decision-making.')
    st.write('4.Adaptability: ML models can adapt and improve over time as they encounter new data, enhancing their performance.')
    
    
    
    st.header(":orange[Project Descriptions]",divider = 'rainbow')
    
    st.header(":blue[1.Old Car Price Prediction]",divider = 'rainbow')
        
    col1,col2 = st.columns(2)
    
    with col1:
        
        st.write('This project utilizes historical data on various car attributes such as model year, mileage, brand, and condition to predict the resale price of used cars. By employing regression techniques, it helps prospective buyers and sellers make informed decisions about pricing.')
        st.write("The car price prediction model is a sophisticated algorithm designed to estimate the value of a vehicle based on various features and market trends. ")
    with col2:
      
    
        image = Image.open("home_page/download.jpeg")
        st.image(image,'')
        
       
    st.header(":blue[2.House Price Prediction ]",divider = 'rainbow')
    col3,col4= st.columns(2)
    
    with col4:
        
    
        st.write('The house price prediction model is an advanced analytical tool that forecasts the value of residential properties based on a multitude of factors. It utilizes machine learning algorithms to analyze historical real estate data, including property features, location attributes, market trends, economic indicators, and demographic information.Using techniques like regression analysis, random forests, or gradient boosting, this model learns complex relationships between housing characteristics (such as size, number of bedrooms, amenities) and their corresponding market values')
    
    with col3:
        

        image1 = Image.open("house-middleclass.jpg ")
        st.image(image1,'')
    
