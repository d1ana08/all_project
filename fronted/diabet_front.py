import streamlit as st
import requests


def diabet_check():
    st.title('Diabet')

    api_url = 'http://127.0.0.1:8000/diabetes'

    Pregnancies = st.number_input('pregnancies', min_value=0)
    Glucose = st.number_input('glucose', min_value=0.0, step=10.0)
    BloodPressure = st.number_input('BloodPressure', min_value=0.0, step=10.0)
    SkinThickness = st.number_input('SkinThickness', min_value=0.0)
    Insulin = st.number_input('Insulin', min_value=0.0, step=10.0)
    BMI = st.number_input('BMI', min_value=0.0, step=0.10)
    DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction', min_value=0.1, step=10.0)
    Age = st.number_input('Age', min_value=0, max_value=100, step=10)

    diabet_data = {
        "Pregnancies": Pregnancies,
        "Glucose": Glucose,
        "BloodPressure": BloodPressure,
        "SkinThickness": SkinThickness,
        "Insulin": Insulin,
        "BMI": BMI,
        "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
        "Age": Age
    }

    if st.button('Результат'):
        try:
            answer = requests.post(api_url, json=diabet_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.json(result)
            else:
                st.error(f"Error: {answer.status_code} - {answer.text}")
        except requests.exceptions.RequestException:
            st.error("Не удалось подключится к Api")
