from django.shortcuts import render, redirect, reverse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


def government_employee_home(request):
    return render(request, 'government_employee/Home.html')


def register_holder_list(request):
    holder = Holder.objects.all()
    context = {
        'holder': holder
    }
    return render(request, '', context=context)