import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('prediksi_diabetes.sav', 'rb'))

st.title('PREDIKSI DIABETES')

col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.number_input('Nilai Pregnancies', step=1)
with col2:
    Glucose = st.number_input('Nilai Glucose', step=1)
with col1:
    BloodPressure = st.number_input('Nilai Blood Preesure', step=1)
with col2:
    SkinThickness = st.number_input('Nilai Skin Thickness', step=1)
with col1:
    Insulin = st.number_input('Nilai Insulin', step=1)
with col2:
    BMI = st.number_input('Nilai BMI', step=0.1)
with col1:
    DiabetesPedigreeFunction = st.number_input('Nilai Diabetes Pedigree Function', step=0.1)
with col2:
    Age = st.number_input('Nilai Age', step=1)

diabetes_diagnosis = ''

if st.button('Prediksi Penyakit Diabetes'):
    diabetes_prediction = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diabetes_prediction[0]==1):
        diabetes_diagnosis = 'PASIEN TERKENA DIABETES'
    else:
        diabetes_diagnosis = 'PASIEN TIDAK TERKENA DIABETES'

st.success(diabetes_diagnosis)
