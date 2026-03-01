import streamlit as st
import requests

def avocado_check():
    st.title('Avocado')

    api_url = 'http://127.0.0.1:8000/avocado'

    color_category = st.selectbox('Color', ['purple', 'green', 'dark green', 'black'])
    firmness = st.number_input('Firmness', min_value=0.0, step=10.0)
    hue = st.number_input('Hue', min_value=0, value=10)
    saturation = st.number_input('Saturation', min_value=1, value=20)
    brightness = st.number_input('Brightness', min_value=1, value=20)
    sound_db = st.number_input('Sound', min_value=1, value=10)
    weight_g = st.number_input('Weight', min_value=1, value=100)
    size_cm3 = st.number_input('Size', min_value=0, value=100)

    avocado_data = {
        "firmness": firmness,
        "hue": hue,
        "saturation": saturation,
        "brightness": brightness,
        "sound_db": sound_db,
        "weight_g": weight_g,
        "size_cm3": size_cm3,
        "color_category": color_category
    }

    if st.button('Result'):
        try:
            ripeness = requests.post(api_url, json=avocado_data, timeout=10)
            if ripeness.status_code == 200:
                result = ripeness.json()
                st.json(result)
            else:
                st.error(f'Error: {ripeness.status_code} - {ripeness.text}')
        except requests.exceptions.RequestException:
            st.error("Couldn't connect to Api")