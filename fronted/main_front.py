import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from mysite.fronted.house_front import check_house
from mysite.fronted.bank_front import check_bank
from mysite.fronted.student_front import student_check
from mysite.fronted.avocado_front import avocado_check
from mysite.fronted.diabet_front import diabet_check
from mysite.fronted.titanic_front import check_titanic
from mysite.fronted.telco_front import check_telco



with st.sidebar:
    name = st.radio('ML Models', ['Info', 'House', 'Student', 'Titanic', 'Bank',
                                  'Diabetes', 'Avocado', 'Telco'])

if name == 'Info':
    st.title('Welcome')
    st.text('House - предсказание стоимости недвижимости')
    st.text('Bank - банковская аналитика')
    st.text('Student - предсказание успеваемости студентов')
    st.text('Avocado - предсказание цен авокадо')
    st.text('Diabetes - диагностика')
    st.text('Titanic - Выживаемость на титанике')
    st.text('Telco - клиенты телекома')


elif name == 'House':
    check_house()

elif name == 'Bank':
    check_bank()

elif name == 'Student':
    student_check()

elif name == 'Avocado':
    avocado_check()

elif name == 'Diabetes':
    diabet_check()

elif name == 'Titanic':
    check_titanic()

elif name == 'Telco':
    check_telco()
