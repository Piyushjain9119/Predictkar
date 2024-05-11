import streamlit as st
import pickle
import warnings
import pandas as pd
import model1.predict as predict

# def app():
#     st.write("hello this is car page")

# model = pickle.load(open('model1\model_training\model.pkl','rb'))


def car_pred():
    # model = pickle.load(open('car\Model.pkl','rb'))  

        

    page_bg_img = """
    <style>

    [data-testid="stAppViewContainer"]{
    background-image :url('https://media.istockphoto.com/id/1290469465/photo/sportscar-silhouette-on-black-background.jpg?s=612x612&w=0&k=20&c=sR1rq2_r-V3A2IY3TZoUn3-40Wq3zy6CrG4eIKbyDLc=');

    background-size :cover;
    }

    </style>

    """




    st.markdown(page_bg_img,unsafe_allow_html=True)

    st.title('CAR PRICE PREDICTION')
    # st.sidebar.header("Car Data")
    # # image = Image.open('ggs.jpg')
    # # st.image(image,'')




    # Name = st.text_input(
    #     label = "Enter the name of the car",
    #     max_chars= 15,
    #     placeholder="NAME"
    # )

    model1 = ['Maruti' ,'Skoda' ,'Honda' ,'Hyundai' ,'Toyota' ,'Ford' ,'Renault', 'Mahindra','Tata' ,'Chevrolet', 'Datsun' ,'Jeep', 'Mercedes-Benz', 'Mitsubishi', 'Audi','Volkswagen' ,'BMW', 'Nissan' ,'Lexus' ,'Jaguar', 'Land' ,'MG' ,'Volvo', 'Daewoo','Kia' ,'Fiat' ,'Force' ,'Ambassador', 'Ashok' ,'Isuzu' ,'Opel']
    # model2 = []
    # # model3 = []
    name = st.selectbox("Enter the name of the car",model1)


    # if Name in model1:
    #     Name = 'Tier1'
    # elif Name in model2:
    #     Name = 'Tier2'
    # else:
    #     Name = 'Tier3'

    # st.write(Name)



    # loc = ['Mumbai', 'Pune', 'Chennai', 'Coimbatore', 'Hyderabad', 'Jaipur','Kochi', 'Kolkata', 'Delhi', 'Bangalore', 'Ahmedabad']

    # Location= st.selectbox("SELECT LOCATION" , loc )




    year= st.number_input(
        label = "Enter the Model Year",
        min_value=2002,
        max_value=2020,
        value = 2014,
        step = 1
    )



    km_driven = st.slider(
        label = "Enter the approx range of Kilometers_Driven",
        min_value=1000,
        max_value=1000000,
        value = 145500,
        step = 1000
    )



    ft = ['Diesel', 'Petrol', 'LPG', 'CNG']
    fuel = st.selectbox("Select fuel type" , ft)


    ss =['Individual', 'Dealer', 'Trustmark Dealer']
    seller_type = st.selectbox("Select seller type" , ss)


    Trans = ['Manual', 'Automatic']
    transmission = st.selectbox("Select Type",Trans)


    Ot= ['First Owner', 'Second Owner', 'Third Owner',
       'Fourth & Above Owner', 'Test Drive Car']
    owner = st.selectbox("Select Owner Type" , Ot)

    mileage = st.number_input(
        label = "Mileage",
        min_value=8.0,
        max_value=35.0,
        value = 23.40,
        step = 1.0,
        format="%.2f"
    )

    engine = st.number_input(
        label = "Engine",
        min_value=700.0,
        max_value=1999.0,
        value = 1248.0,
        step = 1.0,
        format="%.2f"
    )

    max_power = st.number_input(
        label = "Max_Power",
        min_value=0.0,
        max_value=5000.0,
        value = 74.0,
        step = 1.0,
        format="%.2f"
    )

    seat = [ 5.0,  4.0 , 7.0 , 8.0 , 6.0,  9.0, 10.0, 14.0,  2.0]
    seats = st.selectbox("Select Number of seats",seat)






# name', 'year', 'selling_price', 'km_driven', 'fuel', 'seller_type',
#        'transmission', 'owner', 'mileage', 'engine', 'seats



    user_given_data = {
        'name' :name,
        'year' :year,
        'km_driven' :km_driven,
        'fuel' :fuel,
        'seller_type':seller_type,
        'transmission' :transmission,
        'owner' :owner,
        'mileage':mileage,
        'engine':engine,
        'max_power':max_power,
        'seats':seats
    }
    




    
    # user_given_data = {
    #     'Name' :'Tier3',
    #     'Location':'Mumbai',
    #     'Year' :2015,
    #     'Kilometers_Driven' :73000,
    #     'Fuel_Type' :'Petrol',
    #     'Transmission' :'Automatic',
    #     'Owner_Type' :'Second'

    # }

    given_data = pd.DataFrame(user_given_data,index = [0])


    st.header("Given Information")
    st.write(given_data)


    #st.header("lac")
    # st.header(':rainbow[THE ABOVE VALUE IS IN LAKH, THANKS FOR USING] :sunglasses:')

    if st.button('PREDICT'):
        predict.prediction(given_data)

