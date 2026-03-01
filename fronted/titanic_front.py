import streamlit as st
import requests


def check_titanic():
    st.title('Titanic')

    api_url = 'http://127.0.0.1:8000/titanic'

    Pclass = st.number_input('Pclass', min_value=1, max_value=3, value=3)
    Sex = st.selectbox('Gender', ['male', 'female'])
    age = st.number_input('Age', min_value=0, max_value=100,
                          value=20, step=1)
    SibSp = st.number_input('SibSp', min_value=0)
    Parch = st.number_input('Parch', min_value=0)
    Fare = st.number_input('fare', min_value=0, value=7, step=1)
    embarked = st.selectbox('embarked', ['Embarked_Q', 'Embarked_S', 'Embarked_C'])

    titanic_data = {
        "Pclass": Pclass,
        "Sex": Sex,
        "age": age,
        "SibSp": SibSp,
        "Parch": Parch,
        "Fare": Fare,
        "embarked": embarked
    }

    if st.button('Result'):
        try:
            answer = requests.post(api_url, json=titanic_data, timeout=20)
            if answer.status_code == 200:
                result = answer.json()
                st.json(result)
            else:
                st.error(f'Ошибка: {answer.status_code}')
        except requests.exceptions.RequestException:
            st.error('Не удалось подключиться к Api')