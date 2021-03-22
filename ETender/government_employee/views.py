from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


def government_employee_home(request):
    return render(request, 'government_employee/Home.html')

