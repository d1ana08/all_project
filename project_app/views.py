import os
import joblib
from django.conf import settings
from rest_framework import views, status
from rest_framework.response import Response
from .serializers import (
    HousePredictSerializer, DiabetesPredictSerializer,
    AvocadoSerializer, BankPredictSerializer, TitanicSerializer,
    TelcoSerializer, StudentPredictSerializer
)

house_model_path = os.path.join(settings.BASE_DIR, 'models/house_model.pkl')
house_model = joblib.load(house_model_path)

house_scaler_path = os.path.join(settings.BASE_DIR, 'models/house_scaler.pkl')
house_scaler = joblib.load(house_scaler_path)

Neighborhoods = [
    'Blueste', 'BrDale', 'BrkSide', 'ClearCr', 'CollgCr', 'Crawfor', 'Edwards',
    'Gilbert', 'IDOTRR', 'MeadowV', 'Mitchel', 'NAmes', 'NPkVill', 'NWAmes',
    'NoRidge', 'NridgHt', 'OldTown', 'SWISU', 'Sawyer', 'SawyerW', 'Somerst',
    'StoneBr', 'Timber', 'Veenker'
]

class HousePredict(views.APIView):
    def post(self, request):
        instance = HousePredictSerializer(data=request.data)
        if instance.is_valid():
            data = instance.validated_data
            new_neighborhood = data.get('Neighborhood')
            neighborhood1_0 = [1 if new_neighborhood == i else 0 for i in Neighborhoods]

            features = [
                data['GrLivArea'],
                data['YearBuilt'],
                data['GarageCars'],
                data['TotalBsmtSF'],
                data['FullBath'],
                data['OverallQual'],
            ] + neighborhood1_0

            scaled = house_scaler.transform([features])
            pred = house_model.predict(scaled)[0]

            return Response({
                'PredictPrice': round(float(pred), 2),
                'input': data
            }, status=status.HTTP_200_OK)

        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)


diabet_model_path = os.path.join(settings.BASE_DIR, 'models/diabet_model.pkl')
diabet_model = joblib.load(diabet_model_path)

diabet_scaler_path = os.path.join(settings.BASE_DIR, 'models/diabet_scaler.pkl')
diabet_scaler = joblib.load(diabet_scaler_path)

class DiabetesPredict(views.APIView):
    def post(self, request):
        instance = DiabetesPredictSerializer(data=request.data)
        if instance.is_valid():
            data = instance.validated_data

            features = [
                data['Pregnancies'],
                data['Glucose'],
                data['BloodPressure'],
                data['SkinThickness'],
                data['Insulin'],
                data['BMI'],
                data['DiabetesPedigreeFunction'],
                data['Age'],
            ]

            scaled = diabet_scaler.transform([features])
            pred_proba = diabet_model.predict_proba(scaled)[0][1]
            result = 'Yes' if pred_proba > 0.5 else 'No'

            return Response({
                'Diabetes': result,
                'Probability': round(float(pred_proba), 2),
                'input': data
            }, status=status.HTTP_200_OK)

        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)


avocado_model_path = os.path.join(settings.BASE_DIR, 'models/avocado_model.pkl')
avocado_model = joblib.load(avocado_model_path)

avocado_scaler_path = os.path.join(settings.BASE_DIR, 'models/avocado_scaler.pkl')
avocado_scaler = joblib.load(avocado_scaler_path)

class AvocadoPredict(views.APIView):
    def post(self, request):
        instance = AvocadoSerializer(data=request.data)
        if instance.is_valid():
            data = instance.validated_data

            avacado_color = data.get('color_category')
            avacado_color_1_0 = [
                1 if avacado_color == 'dark_green' else 0,
                1 if avacado_color == 'green' else 0,
                1 if avacado_color == 'purple' else 0
            ]

            features = [
                data['firmness'],
                data['hue'],
                data['saturation'],
                data['brightness'],
                data['sound_db'],
                data['weight_g'],
                data['size_cm3'],
            ] + avacado_color_1_0

            scaled = avocado_scaler.transform([features])
            pred = avocado_model.predict(scaled)[0]

            labels = {
                "hard": "hard",
                "pre-conditioned": "pre-conditioned",
                "breaking": "breaking",
                "firm-ripe": "firm-ripe",
                "ripe": "ripe",
            }
            pred_label = labels.get(str(pred), str(pred))

            return Response({
                'predict': pred_label,
                'input': data
            }, status=status.HTTP_200_OK)

        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)


bank_model_path = os.path.join(settings.BASE_DIR, 'models/bank_model.pkl')
bank_model = joblib.load(bank_model_path)

bank_scaler_path = os.path.join(settings.BASE_DIR, 'models/bank_scaler.pkl')
bank_scaler = joblib.load(bank_scaler_path)

bank_gender_list = ['male']
bank_education_list = ['Bachelor', 'Doctorate', 'High School', 'Master']
bank_ownership_list = ['OTHER', 'OWN', 'RENT']
bank_loan_intent_list = ['EDUCATION', 'HOMEIMPROVEMENT', 'MEDICAL', 'PERSONAL', 'VENTURE']
bank_previous_loan_defaults_on_file_list = ['Yes']

class BankPredict(views.APIView):
    def post(self, request):
        instance = BankPredictSerializer(data=request.data)
        if instance.is_valid():
            data = instance.validated_data

            person_gender = data.get('person_gender')
            person_gender_1_0 = [1 if person_gender == i else 0 for i in bank_gender_list]

            person_education = data.get('person_education')
            person_education_1_0 = [1 if person_education == i else 0 for i in bank_education_list]

            person_home_ownership = data.get('person_home_ownership')
            person_home_ownership_1_0 = [1 if person_home_ownership == i else 0 for i in bank_ownership_list]

            loan_intent = data.get('loan_intent')
            loan_intent_1_0 = [1 if loan_intent == i else 0 for i in bank_loan_intent_list]

            previous_loan_defaults_on_file = data.get('previous_loan_defaults_on_file')
            previous_loan_defaults_on_file_1_0 = [
                1 if previous_loan_defaults_on_file == i else 0
                for i in bank_previous_loan_defaults_on_file_list
            ]

            features = [
                data['person_age'],
                data['person_income'],
                data['person_emp_exp'],
                data['loan_famnt'],
                data['loan_int_rate'],
                data['loan_percent_income'],
                data['cb_person_cred_hist_length'],
                data['credit_score'],
            ] + person_gender_1_0 + person_education_1_0 + person_home_ownership_1_0 + loan_intent_1_0 + previous_loan_defaults_on_file_1_0

            scaled = bank_scaler.transform([features])
            pred = bank_model.predict(scaled)[0]
            answer = 'Approve' if int(pred) == 1 else 'Rejected'

            return Response({
                'Answer': answer,
                'input': data
            }, status=status.HTTP_200_OK)

        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)


titanic_model_path = os.path.join(settings.BASE_DIR, 'models/titanic_model.pkl')
titanic_model = joblib.load(titanic_model_path)

titanic_scaler_path = os.path.join(settings.BASE_DIR, 'models/titanic_scaler.pkl')
titanic_scaler = joblib.load(titanic_scaler_path)

class TitanicPredict(views.APIView):
    def post(self, request):
        instance = TitanicSerializer(data=request.data)
        if instance.is_valid():
            data = instance.validated_data

            person_sex = data.get('Sex')
            person_sex_1_0 = [1 if person_sex == 'male' else 0]

            person_embarked = data.get('embarked')
            person_embarked_1_0 = [
                1 if person_embarked == 'Q' else 0,
                1 if person_embarked == 'S' else 0
            ]

            features = [
                data['Pclass'],
                data['SibSp'],
                data['Parch'],
                data['age'],
                data['Fare'],
            ] + person_sex_1_0 + person_embarked_1_0

            scaled = titanic_scaler.transform([features])
            pred = titanic_model.predict(scaled)[0]
            answer = 'alive' if int(pred) == 1 else 'drowed'

            return Response({
                'Answer': answer,
                'input': data
            }, status=status.HTTP_200_OK)

        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)


telco_model_path = os.path.join(settings.BASE_DIR, 'models/telco_model.pkl')
telco_model = joblib.load(telco_model_path)

telco_scaler_path = os.path.join(settings.BASE_DIR, 'models/telco_scaler.pkl')
telco_scaler = joblib.load(telco_scaler_path)

gender_list = ['Male']
Partner_list = ['No']
Dependents_list = ['Yes']
PhoneService_list = ['Yes']
MultipleLines_list = ['No', 'Yes']
InternetService_list = ['Fiber optic', 'No']
OnlineSecurity_list = ['Yes', 'No internet service']
OnlineBackup_list = ['No', 'No internet service']
DeviceProtection_list = ['Yes', 'No internet service']
TechSupport_list = ['Yes', 'No internet service']
StreamingTV_list = ['Yes', 'No internet service']
StreamingMovies_list = ['Yes', 'No internet service']
Contract_list = ['One year', 'Two year']
PaperlessBilling_list = ['No']
PaymentMethod_list = ['Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']

class TelcoPredict(views.APIView):
    def post(self, request):
        instance = TelcoSerializer(data=request.data)
        if instance.is_valid():
            data = instance.validated_data

            gender = [1 if data['gender'] == i else 0 for i in gender_list]
            Partner = [1 if data['Partner'] == i else 0 for i in Partner_list]
            Dependents = [1 if data['Dependents'] == i else 0 for i in Dependents_list]
            PhoneService = [1 if data['PhoneService'] == i else 0 for i in PhoneService_list]
            MultipleLines = [1 if data['MultipleLines'] == i else 0 for i in MultipleLines_list]
            InternetService = [1 if data['InternetService'] == i else 0 for i in InternetService_list]
            OnlineSecurity = [1 if data['OnlineSecurity'] == i else 0 for i in OnlineSecurity_list]
            OnlineBackup = [1 if data['OnlineBackup'] == i else 0 for i in OnlineBackup_list]
            DeviceProtection = [1 if data['DeviceProtection'] == i else 0 for i in DeviceProtection_list]
            TechSupport = [1 if data['TechSupport'] == i else 0 for i in TechSupport_list]
            StreamingTV = [1 if data['StreamingTV'] == i else 0 for i in StreamingTV_list]
            StreamingMovies = [1 if data['StreamingMovies'] == i else 0 for i in StreamingMovies_list]
            Contract = [1 if data['Contract'] == i else 0 for i in Contract_list]
            PaperlessBilling = [1 if data['PaperlessBilling'] == i else 0 for i in PaperlessBilling_list]
            PaymentMethod = [1 if data['PaymentMethod'] == i else 0 for i in PaymentMethod_list]

            features = [
                data['tenure'],
                data['MonthlyCharges'],
                data['TotalCharges']
            ] + gender + Partner + Dependents + PhoneService + MultipleLines + InternetService + OnlineSecurity + OnlineBackup + DeviceProtection + TechSupport + StreamingTV + StreamingMovies + Contract + PaperlessBilling + PaymentMethod

            scaled = telco_scaler.transform([features])
            proba = telco_model.predict_proba(scaled)[0][1]
            label = "Stay" if proba > 0.5 else "Don't stay"

            return Response({
                "Answer": label,
                "Probability": round(float(proba), 2),
                "input": data
            }, status=status.HTTP_200_OK)

        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)


student_model_path = os.path.join(settings.BASE_DIR, 'models/student_model_2.pkl')
student_model = joblib.load(student_model_path)

student_scaler_path = os.path.join(settings.BASE_DIR, 'models/student_scaler_2.pkl')
student_scaler = joblib.load(student_scaler_path)

gender_list = ['male', 'female']
race_ethnicity_list = ['group B', 'group C', 'group D', 'group E', 'group A']
parent_education_list = [
    "bachelor's degree", "hist school", "master's degree", "some college",
    "some high school", "associate's degree"
]
lunch_list = ['standard', 'free/reduced']
test_preparation_list = ['none', 'completed']

class StudentPredict(views.APIView):
    def post(self, request):
        instance = StudentPredictSerializer(data=request.data)
        if instance.is_valid():
            data = instance.validated_data

            gender = [1 if data['gender'] == i else 0 for i in gender_list]
            race_ethnicity = [1 if data['race_ethnicity'] == i else 0 for i in race_ethnicity_list]
            parent_education = [1 if data['parent_education'] == i else 0 for i in parent_education_list]
            lunch = [1 if data['lunch'] == i else 0 for i in lunch_list]
            test_preparation = [1 if data['test_preparation'] == i else 0 for i in test_preparation_list]

            features = [
                data['math_score'],
                data['reading_score'],
            ] + gender + parent_education + lunch + test_preparation

            scaled = student_scaler.transform([features])
            pred = float(student_model.predict(scaled)[0])

            return Response({
                "Prediction": round(pred, 2),
                "input": data
            }, status=status.HTTP_200_OK)

        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)