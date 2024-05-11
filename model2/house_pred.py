import streamlit as st
import pickle
import warnings
import pandas as pd
import model2.predict_home as predict

# def app():
#     st.write("hello this is car page")

# model = pickle.load(open('model2\model.pkl','rb'))


def app():
    # model = pickle.load(open('car\Model.pkl','rb'))  

        

    page_bg_img = """
    <style>

    [data-testid="stAppViewContainer"]{
    background-image :url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRAXXd3-4PwnXra5Ib1BfMffpzfCoBnB1g6g&s');

    background-size :cover;
    }

    </style>

    """




    st.markdown(page_bg_img,unsafe_allow_html=True)

    st.title('HOUSE PRICE PREDICTION')
    




    UNDER_CONSTRUCTIO= ['YES',"NO"]
   
    name = st.selectbox("UNDER CONSTRUCTION BUILDING?",UNDER_CONSTRUCTIO)

    if name == 'YES':
        UNDER_CONSTRUCTION = 1
    else:
        UNDER_CONSTRUCTION= 0


    RER= ['YES',"NO"]
    
    name1 = st.selectbox(" Real Estate Regulatory Authority",RER)

    if name1 == 'YES':
        RERA = 1
    else:
        RERA= 0


    BHK= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 20]
    # # model3 = []
    BHK_NO = st.selectbox(" BHK NUMBER",BHK)

    BHK_OR= ['BHK','RK']
    # # model3 = []
    BHK_OR_RK	= st.selectbox(" select one of Two	",BHK_OR)



    



    



    SQUARE_FT= st.number_input(
        label = "SQUARE FT",
        min_value=10,
        max_value=10000,
        value = 50,
        step = 1
    )



    READY= ['YES',"NO"]
    # # model3 = []
    name4 = st.selectbox(" READY TO MOVE?",READY)

    if name4 == 'YES':
        READY_TO_MOVE = 1
    else:
        READY_TO_MOVE= 0


    READY2= ['YES',"NO"]
    # # model3 = []
    name5 = st.selectbox(" RESALED HOME",READY2)

    if name5 == 'YES':
        RESALE = 1
    else:
        RESALE= 0


    list_city = ['Bangalore', 'Mysore', 'Ghaziabad', 'Kolkata', 'Kochi', 'Jaipur',
       'Mohali', 'Chennai', 'Siliguri', 'Noida', 'Raigad', 'Bhubaneswar',
       'Wardha', 'Pune', 'Mumbai', 'Nagpur', 'Deoghar', 'Bhiwadi',
       'Faridabad', 'Lalitpur', 'Maharashtra', 'Vadodara',
       'Visakhapatnam', 'Vapi', 'Mangalore', 'Aurangabad', 'Ottapalam',
       'Vijayawada', 'Belgaum', 'Bhopal', 'Lucknow', 'Kanpur',
       'Gandhinagar', 'Pondicherry', 'Agra', 'Ranchi', 'Gurgaon', 'Udupi',
       'Indore', 'Jodhpur', 'Coimbatore', 'Valsad', 'Palghar', 'Surat',
       'Varanasi', 'Guwahati', 'Amravati', 'Anand', 'Tirupati',
       'Secunderabad', 'Raipur', 'Vizianagaram', 'Thrissur', 'Satna',
       'Madurai', 'Chandigarh', 'Shimla', 'Gwalior', 'Rajkot', 'Sonipat',
       'Allahabad', 'Berhampur', 'Roorkee', 'Dharuhera', 'Latur',
       'Durgapur', 'Panchkula', 'Solapur', 'Durg', 'Goa', 'Jamshedpur',
       'Hazaribagh', 'Jabalpur', 'Hosur', 'Morbi', 'Hubli', 'Karnal',
       'Patna', 'Bilaspur', 'Ratnagiri', 'Meerut', 'Kotdwara',
       'Jalandhar', 'Amritsar', 'Patiala', 'Ludhiana', 'Alwar', 'Kota',
       'Panaji', 'Kolhapur', 'Ernakulam', 'Bhavnagar', 'Bharuch',
       'Asansol', 'Jhansi', 'Margao', 'Anantapur', 'Eluru', 'Bhilai',
       'Dehradun', 'Guntur', 'Jalgaon', 'Udaipur', 'Gurdaspur',
       'Neemrana', 'Hassan', 'Sindhudurg', 'Hoshangabad', 'Kottayam',
       'Dhanbad', 'Navsari', 'Bahadurgarh', 'Nellore', 'Dhule',
       'Tirunelveli', 'Cuttack', 'Haridwar', 'Nainital', 'Jamnagar',
       'Kanchipuram', 'Kadi', 'Karad', 'Jagdalpur', 'Panipat',
       'Muzaffarpur', 'Salem', 'Jhunjhunu', 'Gandhidham', 'Junagadh','Moradabad', 'Ahmednagar', 'Jalna', 'Bhiwani',
       'Palakkad', 'Kannur', 'Karjat', 'Akola', 'Jind', 'Gaya', 'Ambala',
       'Ajmer', 'Hajipur', 'Dharwad', 'Pudukkottai', 'Kollam', 'Ooty',
       'Bhandara', 'Barabanki', 'Rajpura', 'Palwal', 'Aligarh', 'Erode',
       'Rudrapur', 'Tenali', 'Ongole', 'Nizamabad', 'Puri', 'Dalhousie',
       'Siddipet', 'Solan', 'Darbhanga', 'Kadapa', 'Kakinada', 'Agartala',
       'Warangal', 'Haldwani', 'Osmanabad', 'Bhagalpur', 'Bardhaman',
       'Rishikesh', 'Chandrapur', 'Bokaro', 'Jharsuguda', 'Bhimavaram',
       'Kurnool', 'Amroha', 'Hapur', 'Sabarkantha', 'Harda', 'Ujjain',
       'Thoothukudi', 'Karaikudi', 'Mathura', 'Gadhinglaj', 'Rewari',
       'Godhra', 'Kharagpur', 'Srikakulam', 'Srinagar', 'Midnapore',
       'Rayagada', 'Banswara', 'Shirdi', 'Rohtak', 'Pali', 'Hathras',
       'Yavatmal', 'Balasore', 'Chhindwara', 'Bareilly', 'Vidisha',
       'Thanjavur', 'Kangra', 'Bikaner', 'Rewa', 'Porbandar', 'Nagaur',
       'Nanded', 'Rourkela', 'Nadiad', 'Gulbarga', 'Palanpur', 'Bhadrak',
       'Kurukshetra', 'Dibrugarh', 'Sagar', 'Machilipatnam',
       'Pathanamthitta', 'Bankura', 'Jammu', 'Idukki', 'Korba', 'Raigarh',
       'Silchar', 'Arrah', 'Nagaon', 'Karwar', 'Dahod', 'Nagapattinam',
       'Sikar', 'Angul', 'Baddi', 'Darjeeling', 'Raisen', 'Hoshiarpur',
       'Beed', 'Gadarwara', 'Jajpur', 'Haldia', 'Chittoor', 'Faizabad',
       'Malappuram', 'Betul', 'Surendranagar', 'Phagwara', 'Visnagar',
       'Rajnandgaon', 'Cuddalore', 'Raichur', 'Sambalpur', 'Gondia',
       'Vellore', 'Bharatpur', 'Bhuj', 'Siwan', 'Washim']
    
    ADDRESS1 = st.selectbox(" select the city  ",list_city)

    if ADDRESS1 in  ['Bangalore','Kolkata','Jaipur','Chennai','Dehradun','Shimla','Mumbai','Pune','Goa','Maharashtra']:
        ADDRESS = 'Tier_1'

    elif ADDRESS1 in ['Faridabad', 'Lalitpur', 'Vadodara',
       'Visakhapatnam', 'Vapi', 'Mangalore', 'Aurangabad', 'Ottapalam',
       'Vijayawada', 'Belgaum', 'Bhopal', 'Lucknow', 'Kanpur',
       'Gandhinagar', 'Pondicherry', 'Agra', 'Ranchi', 'Gurgaon', 'Udupi',
       'Indore', 'Jodhpur', 'Coimbatore', 'Valsad', 'Palghar', 'Surat',
       'Varanasi', 'Guwahati', 'Amravati', 'Anand', 'Tirupati',
       'Secunderabad', 'Raipur', 'Vizianagaram', 'Thrissur', 'Satna',
       'Madurai', 'Chandigarh', 'Shimla', 'Gwalior', 'Rajkot', 'Sonipat',
       'Allahabad', 'Berhampur', 'Roorkee', 'Dharuhera', 'Latur',
       'Durgapur', 'Panchkula', 'Solapur', 'Durg', 'Jamshedpur',
       'Hazaribagh', 'Jabalpur', 'Hosur', 'Morbi', 'Hubli', 'Karnal',
       'Patna', 'Bilaspur', 'Ratnagiri', 'Meerut', 'Kotdwara',
       'Jalandhar', 'Amritsar', 'Patiala', 'Ludhiana', 'Alwar', 'Kota',
       'Panaji', 'Kolhapur', 'Ernakulam', 'Bhavnagar', 'Bharuch']:
        
        ADDRESS = 'Tier_2'

    else:
        ADDRESS = 'Tier_3'

    



    user_given_data = {
        'UNDER_CONSTRUCTION' :UNDER_CONSTRUCTION,
        'RERA' :RERA,
        'BHK_NO.' :BHK_NO,
        'BHK_OR_RK' :BHK_OR_RK,
        'SQUARE_FT':SQUARE_FT,
        'READY_TO_MOVE' :READY_TO_MOVE,
        'RESALE' :RESALE,
        'ADDRESS':ADDRESS
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


    # st.header("Given Information")
    # st.write(given_data)


    #st.header("lac")
    # st.header(':rainbow[THE ABOVE VALUE IS IN LAKH, THANKS FOR USING] :sunglasses:')

    if st.button('PREDICT'):
        predict.prediction(given_data)

