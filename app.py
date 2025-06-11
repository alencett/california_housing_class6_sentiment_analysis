import streamlit as st
import pickle

st.title("Web app to predict the housing prices")

#read model file

model = pickle.load(open("cal_model_rf.pkl", "rb"))

#input features
st.header("Input Features")

#add the input fields based on the models columns 

l=['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup',
       'Latitude', 'Longitude']

user_input = {}

for i in l: 
    user_input[i] = st.number_input(i)

#convert user input to dataframe
import pandas as pd

input_df = pd.DataFrame([user_input])

#get the prediction through the model

result = model.predict(input_df)

#display the result

if st.button("Predict"):
    st.success(f"The predicted house price is ${result[0]:,.2f}")
