import streamlit as st
import requests

def hremployee_check():
    st.title('HREmployee')

    api_url = 'http://127.0.0.1:8000/employee'

    Age = st.number_input('Age', min_value=0, max_value=100)
    BusinessTravel = st.selectbox('BusinessTravel', ['Travel_Rarely', 	'Travel_Frequently'])
    DailyRate = st.number_input('DailyRate', min_value=0, step=100)
    Department = st.selectbox('Department', ['Sales', 'Research & Development'])
    DistanceFromHome = st.number_input('DistanceFromHome', min_value=0, max_value=60)
    Education = st.number_input('Education', min_value=0, max_value=50)
    EducationField = st.selectbox('EducationField', ['Life Sciences', 'Other', 'Medical'])
    EnvironmentSatisfaction = st.number_input('EnvironmentSatisfaction', min_value=0, max_value=40)
    Gender = st.selectbox("Gender", ["Male"])
    HourlyRate = st.number_input('HourlyRate', min_value=0, max_value=100)
    JobInvolvement = st.number_input('JobInvolvement', min_value=0, max_value=40)
    JobLevel = st.number_input('JobLevel', min_value=0)
    JobRole = st.selectbox('JobRole', ['Sales Executive', 'Research Scientist','Laboratory Technician', 'Healthcare Representative',
               'Manufacturing Director'])
    JobSatisfaction = st.number_input('JobSatisfaction', min_value=0, max_value=50)
    MaritalStatus = st.selectbox('MaritalStatus', ['Single', 'Married'])
    MonthlyIncome = st.number_input('MonthlyIncome', min_value=0, step=100)
    MonthlyRate = st.number_input('MonthlyRate', min_value=0, step=100)
    NumCompaniesWorked = st.number_input('NumCompaniesWorked', min_value=0, max_value=50)
    OverTime = st.selectbox("OverTime", ["No", "Yes"])
    PercentSalaryHike = st.number_input('PercentSalaryHike', min_value=0, max_value=100)
    PerformanceRating = st.number_input('PerformanceRating', min_value=0, max_value=5)
    RelationshipSatisfaction = st.number_input('RelationshipSatisfaction', min_value=0, max_value=10)
    StockOptionLevel = st.number_input('StockOptionLevel', min_value=0, max_value=10)
    TotalWorkingYears = st.number_input('TotalWorkingYears', min_value=0, max_value=50)
    TrainingTimesLastYear = st.number_input('TrainingTimesLastYear', min_value=0, max_value=50)
    WorkLifeBalance = st.number_input('WorkLifeBalance', min_value=0, max_value=50)
    YearsAtCompany = st.number_input('YearsAtCompany', min_value=0, max_value=50)
    YearsInCurrentRole = st.number_input('YearsInCurrentRole', min_value=0, max_value=30)
    YearsSinceLastPromotion = st.number_input('YearsSinceLastPromotion', min_value=0, max_value=10)
    YearsWithCurrManager = st.number_input('YearsWithCurrManager', min_value=0, max_value=20)

    employee_data = {
    "Age": Age,
    "BusinessTravel": BusinessTravel,
    "DailyRate": DailyRate,
    "Department": Department,
    "DistanceFromHome": DistanceFromHome,
    "Education": Education,
    "EducationField": EducationField,
    "EnvironmentSatisfaction": EnvironmentSatisfaction,
    "Gender": Gender,
    "HourlyRate": HourlyRate,
    "JobInvolvement": JobInvolvement,
    "JobLevel": JobLevel,
    "JobRole": JobRole,
    "JobSatisfaction": JobSatisfaction,
    "MaritalStatus": MaritalStatus,
    "MonthlyIncome": MonthlyIncome,
    "MonthlyRate": MonthlyRate,
    "NumCompaniesWorked": NumCompaniesWorked,
    "OverTime": OverTime,
    "PercentSalaryHike": PercentSalaryHike,
    "PerformanceRating": PerformanceRating,
    "RelationshipSatisfaction": RelationshipSatisfaction,
    "StockOptionLevel": StockOptionLevel,
    "TotalWorkingYears": TotalWorkingYears,
    "TrainingTimesLastYear": TrainingTimesLastYear,
    "WorkLifeBalance": WorkLifeBalance,
    "YearsAtCompany": YearsAtCompany,
    "YearsInCurrentRole": YearsInCurrentRole,
    "YearsSinceLastPromotion": YearsSinceLastPromotion,
    "YearsWithCurrManager": YearsWithCurrManager
    }

    if st.button('Result'):
        try:
            attrition = requests.post(api_url, json=employee_data, timeout=10)
            if attrition.status_code == 200:
                result = attrition.json()
                st.json(result)
            else:
                st.error(f'Error: {attrition.status_code} - {attrition.text}')
        except requests.exceptions.RequestException:
            st.error("Couldn't connect to Api")
