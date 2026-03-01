from django.db import models


class House(models.Model):
    GrLivArea = models.IntegerField()
    YearBuilt = models.IntegerField()
    GarageCars = models.IntegerField()
    TotalBsmtSF = models.IntegerField()
    FullBath = models.IntegerField()
    OverallQual = models.IntegerField()
    Neighborhood = models.CharField(max_length=50)
    predicted_price = models.FloatField(null=True, blank=True)

class DiabetesPrediction(models.Model):
    Pregnancies = models.IntegerField()
    Glucose = models.IntegerField()
    BloodPressure = models.IntegerField()
    SkinThickness = models.IntegerField()
    Insulin = models.IntegerField()
    BMI = models.FloatField()
    DiabetesPedigreeFunction = models.FloatField()
    Age = models.IntegerField()
    predicted_label = models.CharField(max_length=10, blank=True)
    probability = models.FloatField(null=True, blank=True)

class Bank(models.Model):
    person_age = models.FloatField()
    person_gender = models.CharField(max_length=20)
    person_education = models.CharField(max_length=50)
    person_income = models.FloatField()
    person_emp_exp = models.IntegerField()
    person_home_ownership = models.CharField(max_length=20)
    loan_famnt = models.FloatField()
    loan_intent = models.CharField(max_length=50)
    loan_int_rate = models.FloatField()
    loan_percent_income = models.FloatField()
    cb_person_cred_hist_length = models.FloatField()
    credit_score = models.IntegerField()
    previous_loan_defaults_on_file = models.CharField(max_length=10)
    predicted_result = models.CharField(max_length=20, null=True, blank=True)



class Titanic(models.Model):
    Pclass = models.IntegerField()
    Sex = models.CharField(max_length=10)
    age = models.IntegerField()
    Fare = models.FloatField()
    SibSp = models.IntegerField(default=0)
    Parch = models.IntegerField(default=0)
    embarked = models.CharField(max_length=20)
    predicted_result = models.CharField(max_length=20, null=True, blank=True)


class Avocado(models.Model):
    firmness = models.FloatField()
    hue = models.IntegerField()
    saturation = models.IntegerField()
    brightness = models.IntegerField()
    color_category = models.CharField(max_length=20)
    sound_db = models.IntegerField()
    weight_g = models.IntegerField()
    size_cm3 = models.IntegerField()
    predicted_label = models.CharField(max_length=30, null=True, blank=True)



class Telco(models.Model):
    gender = models.CharField(max_length=20)
    SeniorCitizen = models.IntegerField()
    Partner = models.CharField(max_length=10)
    Dependents = models.CharField(max_length=10)
    tenure = models.IntegerField()
    PhoneService = models.CharField(max_length=10)
    MultipleLines = models.CharField(max_length=20)
    InternetService = models.CharField(max_length=20)
    OnlineSecurity = models.CharField(max_length=30)
    OnlineBackup = models.CharField(max_length=30)
    DeviceProtection = models.CharField(max_length=30)
    TechSupport = models.CharField(max_length=30)
    StreamingTV = models.CharField(max_length=30)
    StreamingMovies = models.CharField(max_length=30)
    Contract = models.CharField(max_length=20)
    PaperlessBilling = models.CharField(max_length=10)
    PaymentMethod = models.CharField(max_length=50)
    MonthlyCharges = models.IntegerField()
    TotalCharges = models.IntegerField()
    predicted_label = models.CharField(max_length=20, null=True, blank=True)
    probability = models.FloatField(null=True, blank=True)

class Student(models.Model):
    math_score = models.IntegerField()
    reading_score = models.IntegerField()
    gender = models.CharField(max_length=10)
    race_ethnicity = models.CharField(max_length=20)
    parent_education = models.CharField(max_length=50)
    lunch = models.CharField(max_length=20)
    test_preparation = models.CharField(max_length=20)

    predicted_score = models.FloatField(null=True, blank=True)