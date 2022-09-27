#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 23:39:34 2022

@author: faisal
"""

import numpy as np
import pickle
import streamlit as st

# loading the model
loaded_model = pickle.load(open("/home/faisal/Downloads/diabetes_trained_model.sav", 'rb'))
loaded_scaler = pickle.load(open("/home/faisal/Downloads/diabetes_scalar.sav", 'rb'))

# create function for prediction

def diabetes_prediction(input_data):
    
    input_data_arr= np.asarray(input_data)
    
    input_data_reshaped = input_data_arr.reshape(1, -1)
    
    # standardize input data
    
    standard_data = loaded_scaler.transform(input_data_reshaped)
    
    prediction = loaded_model.predict(standard_data)
    
    if prediction[0] == 0:
        return 'Non-Diabetic'
    else:
        return 'Diabetic'

def main():
    
    # title for webpage
    st.title("Diabates Prediction Web App")
    
    # getting input data from user
    Pregnancies = st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Blood Glucose Level")
    BloodPressure = st.text_input("Blood Pressure")
    SkinThickness = st.text_input("Skin Thickness")
    Insulin = st.text_input("Insulin")
    BMI = st.text_input("BMI")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
    Age = st.text_input("Age")
    
    # code for prediction
    diagnosis = ""
    
    # create a button
    if st.button("Diabetes Test"):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, 
                                         SkinThickness, Insulin, BMI, DiabetesPedigreeFunction,
                                         Age])
    st.success(diagnosis)

if __name__ == "__main__":
    main()