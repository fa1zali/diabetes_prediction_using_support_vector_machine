#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 13:15:20 2022

@author: faisal
"""

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int 
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int
    
# load the saved model
loaded_model = pickle.load(open("diabetes_trained_model.sav", 'rb'))
loaded_scaler = pickle.load(open("diabetes_scalar.sav", 'rb'))

@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    preg = input_dictionary["Pregnancies"]
    gluc = input_dictionary["Glucose"]
    bp = input_dictionary["BloodPressure"]
    st = input_dictionary["SkinThickness"]
    ins = input_dictionary["Insulin"]
    bmi = input_dictionary["BMI"]
    dpf = input_dictionary["DiabetesPedigreeFunction"]
    age = input_dictionary["Age"]
    
    input_list = [preg, gluc, bp, st, ins, bmi, dpf, age]

    input_data_arr= np.asarray(input_list)
    
    input_data_reshaped = input_data_arr.reshape(1, -1)
    
    # standardize input data
    
    standard_data = loaded_scaler.transform(input_data_reshaped)
    
    prediction = loaded_model.predict(standard_data)
    
    if prediction[0] == 0:
        return 'Non-Diabetic'
    else:
        return 'Diabetic'