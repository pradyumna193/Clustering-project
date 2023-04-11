# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:13:33 2023

@author: PRADYUMNA PS
"""

import streamlit as st
import pickle
model = pickle.load(open('model.pkl', 'rb'))


def main():
  st.title('Marketing Campaign')
  st.sidebar.header('Customer Data')
    
  Marital_Status = st.checkbox('Marital Status', ("Yes", "No") )
  Income = st.number_input('Income','Insert a number')
  Age = st.number_input('Age', 'Insert a number' )
  NumDealsPurchases = st.number_input('NumDealsPurchases', 'Insert a number' )
  NumWebPurchases = st.number_input('NumWebPurchases', 'Insert a number' )
  NumStorePurchases = st.number_input('NumStorePurchases','Insert a number')
  NumWebVisitsMonth = st.number_input('NumWebVisitsMonth', 'Insert a number')
  Days_since_enrolment = st.number_input('Days_since_enrolment','Insert a number')
  Family_Size = st.number_input('Family_Size','Insert a number')
  Spent = st.number_input('Spent','Insert a number') 
  
  if st.button('Predict'):
      makeprediction = model.predict([[Marital_Status,Income,Age,NumDealsPurchases,NumWebPurchases,NumStorePurchases,NumWebVisitsMonth,Days_since_enrolment,Family_Size,Spent]])
      output = model(makeprediction[0],2)
      st.success('Type of customer {}'.format(output))
      
  if __name__=='__main__':
      main()
      
