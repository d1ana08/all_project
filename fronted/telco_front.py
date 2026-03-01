import streamlit as st
import requests

def check_telco():
    st.title('Telco')

    api_url = 'http://127.0.0.1:8000/telecom'

    tenure = st.number_input('Tenure')
    MonthlyCharges = st.number_input('MonthlyCharges')
    TotalCharges = st.number_input('TotalCharges')
    gender = st.selectbox('gender', ['Male', 'Female'])
    SeniorCitizen = st.number_input('SeniorCitizen')
    Partner = st.number_input('Partner')
    Dependents = st.number_input('Dependents')
    PhoneService = st.number_input('PhoneService')
    MultipleLines = st.selectbox('MultipleLines', ['No', 'Yes'])
    InternetService = st.selectbox('InternetService', ['Fiber', 'No'])
    OnlineSecurity = st.selectbox('OnlineSecurity', ['No', 'Yes'])
    OnlineBackup = st.selectbox('OnlineBackup', ['Yes', 'No'])
    DeviceProtection = st.selectbox('DeviceProtection', ['Yes', 'No'])
    TechSupport = st.selectbox('TechSupport', ['Yes', 'No'])
    StreamingTV = st.selectbox('StreamingTV', ['Yes', 'No'])
    StreamingMovies = st.selectbox('StreamingMovies', ['Yes', 'No'])
    Contract = st.selectbox('Contract', ['One year', 'Two year'])
    PaperlessBilling = st.number_input('PaperlessBilling')
    PaymentMethod = st.selectbox('PaymentMethod', ['Electronic check', 'Mailed check'])

    teleco_data = {
        'tenure': tenure,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges,
        'gender': gender,
        'SeniorCitizen': SeniorCitizen,
        'Partner': Partner,
        'Dependents': Dependents,
        'PhoneService': PhoneService,
        'MultipleLines': MultipleLines,
        'InternetService': InternetService,
        'OnlineSecurity': OnlineSecurity,
        'OnlineBackup': OnlineBackup,
        'DeviceProtection': DeviceProtection,
        'TechSupport': TechSupport,
        'StreamingTV': StreamingTV,
        'StreamingMovies': StreamingMovies,
        'Contract': Contract,
        'PaperlessBilling': PaperlessBilling,
        'PaymentMethod': PaymentMethod
    }

    if st.button('Result'):
        try:
            r = requests.post(api_url, json=teleco_data, timeout=10)
            if r.status_code == 200:
                st.json(r.json())
            else:
                st.error(f'Error: {r.status_code}')
                st.text(r.text)
        except requests.exceptions.RequestException as e:
            st.error(f'Не удалось подключиться к API: {e}')