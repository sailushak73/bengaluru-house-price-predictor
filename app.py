import pandas as pd
import pickle as pk
import streamlit as st

model = pk.load(open("House_Prediction_model.pk1", "rb"))
st.header("House Price Prediction")

data= pd.read_csv("Cleaned_data.csv")

loc=st.selectbox("choose the location", data['location'].unique())
sqft=st.number_input("Enter the total sqft area")
bedrooms=st.number_input("Enter the number of bedrooms")
bath=st.number_input("Enter the number of bathrooms")
balcony=st.number_input("Enter the number of balconies")

input=pd.DataFrame([[loc, sqft, bedrooms, bath, balcony]], columns=['location', 'total_sqft', 'bedrooms', 'bath', 'balcony'])

if st.button("Predict Price"):
    output=model.predict(input)
    out_str='price of House is : ' + str(output[0]*100000) 
    st.success(out_str)
  