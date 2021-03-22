from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', government_employee_home, name='government_employee_home')

]
