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
loaded_model = pickle.load(open("saved_model/diabetes_trained_model.sav", 'rb'))
loaded_scaler = pickle.load(open("saved_model/diabetes_scalar.sav", 'rb'))

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
    
    # tite for the app
    st.set_page_config(page_title="Diabates Prediction", page_icon="🍭", layout="centered")
    st.title("🍭 Diabates Prediction")
    
    # getting input data from user
    form = st.form(key="annotation")

    with form:
        cols = st.columns((1, 1))
        Pregnancies = cols[0].text_input("Number of Pregnancies:")
        Glucose = cols[1].text_input("Blood Glucose Level:")
        BloodPressure = cols[0].text_input("Blood Pressure:")
        SkinThickness = cols[1].text_input("Skin Thickness:")
        Insulin = cols[0].text_input("Insulin:")
        BMI = cols[1].text_input("BMI:")
        DiabetesPedigreeFunction = cols[0].text_input("Diabetes Pedigree Function:")
        Age = cols[1].text_input("Age:")
        submitted = st.form_submit_button(label="Diabetes Test")

    # code for prediction
    diagnosis = ""
    
    # create a button
    if submitted:
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, 
                                         SkinThickness, Insulin, BMI, DiabetesPedigreeFunction,
                                         Age])
        st.success(diagnosis)

if __name__ == "__main__":
    main()