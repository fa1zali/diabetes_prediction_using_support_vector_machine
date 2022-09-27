# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle

# loading the saved model

loaded_model = pickle.load(open("/home/faisal/Downloads/diabetes_trained_model.sav", 'rb'))
loaded_scaler = pickle.load(open("/home/faisal/Downloads/diabetes_scalar.sav", 'rb'))

input_data = (5,78,48,0,0,33.7,0.654,25)

# changing data to numpy array

input_data_arr= np.asarray(input_data)

input_data_reshaped = input_data_arr.reshape(1, -1)

# standardize input data

standard_data = loaded_scaler.transform(input_data_reshaped)

prediction = loaded_model.predict(standard_data)

if prediction[0] == 0:
    print('Non-Diabetic')
else:
    print('Diabetic')