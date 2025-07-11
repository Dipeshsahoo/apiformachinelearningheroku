# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 12:30:22 2025

@author: Dipesh Sahoo
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle

import json

app=FastAPI()

#this code is used for which domains can acessing the api
origins=['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
#it is the format in which the api needs the data

class model_input(BaseModel):
    Pregnancies :int
    Glucose :int
    BloodPressure:int
    SkinThickness :int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age :int
 
    
#loading the saved model

diabetes_model=pickle.load(open('diabetes_model.sav','rb'))

#Creating the api 

@app.post('/diabetes_prediction')


def diabetes_pred(input_parameters : model_input):
    input_data=input_parameters.json()
    input_dictionary=json.loads(input_data)
    preg=input_dictionary['Pregnancies']
    glu=input_dictionary['Glucose']
    bp=input_dictionary['BloodPressure']
    skin=input_dictionary['SkinThickness']
    insulin=input_dictionary['Insulin']
    bmi=input_dictionary['BMI']
    dpf=input_dictionary['DiabetesPedigreeFunction']
    age=input_dictionary['Age']
    
    input_list=[preg,glu,bp,skin,insulin,bmi,dpf,age]   
    
    prediction=diabetes_model.predict([input_list])
    
    if prediction[0]==0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    