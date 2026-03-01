from django.urls import path, include

from .views import HousePredict, DiabetesPredict, AvocadoPredict, BankPredict, TitanicPredict, TelcoPredict, StudentPredict
from rest_framework import routers

router = routers.SimpleRouter()
urlpatterns = [
    path('house', HousePredict.as_view(), name='house_model'),
    path('diabetes', DiabetesPredict.as_view(), name='diabetes_model'),
    path('avocado', AvocadoPredict.as_view(), name='avocado_model'),
    path('bank', BankPredict.as_view(), name='bank_model'),
    path('titanic', TitanicPredict.as_view(), name='titanic_model'),
    path('telecom', TelcoPredict.as_view(), name='telco_model'),
    path('student', StudentPredict.as_view(), name='student_model')
]

