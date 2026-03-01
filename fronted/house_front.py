import streamlit as st
import requests

def check_house():
    st.title('House')
    api_url = 'http://127.0.0.1:8000/house'

    Neighborhood = st.selectbox('neighborhood',
                                ['Veenker', 'Timber', 'StoneBr', 'Somerst', 'SawyerW', 'Sawyer', 'SWISU', 'OldTown',
                                 'NridgHt', 'NoRidge', 'NWAmes', 'NPkVill', 'NAmes', 'Mitchel', 'MeadowV', 'IDOTRR',
                                 'Gilbert', 'Edwards', 'Crawfor', 'CollgCr', 'ClearCr', 'BrkSide', 'BrDale',
                                 'Blueste'])
    GrLivArea = st.number_input('Area', min_value=0, step=1000)
    YearBuilt = st.number_input('yearbuilt', min_value=0, step=1000)
    GarageCars = st.number_input('GarageCars', min_value=0)
    TotalBsmtSF = st.number_input('TotalbsmtSF', min_value=0, step=100)
    FullBath = st.number_input('fullbath', min_value=0)
    OverallQual = st.number_input('Overallqual', min_value=0)

    house_data = {
        "GrLivArea": GrLivArea,
        "YearBuilt": YearBuilt,
        "GarageCars": GarageCars,
        "TotalBsmtSF": TotalBsmtSF,
        "FullBath": FullBath,
        "OverallQual": OverallQual,
        "Neighborhood": Neighborhood
    }

    if st.button('Result'):
        try:
            price = requests.post(api_url, json=house_data, timeout=10)
            if price.status_code == 200:
                result = price.json()
                st.json(result)
            else:
                st.error(f"Error: {price.status_code} - {price.text}")
        except requests.exceptions.RequestException:
            st.error("Couldn't connect to Api")