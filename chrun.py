import streamlit as st
import joblib
st.title('Chrun preduction')
st.write('Reasons why customers leave a company or organization based on demographic and financial data')
st.image('1.png')
a=st.number_input("age")
b=st.number_input('balance')
btn=st.button('exit prediction')
if btn==True:
    model = joblib.load('model.pkl')
    result=model.predict([[a,b]])
    if    result==1:
          st.write('the custoer still with us')
    elif  result==0:
          st.write('the customer left')
   
   