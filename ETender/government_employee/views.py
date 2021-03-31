from django.shortcuts import render, redirect, reverse
from .models import *
from django.contrib.auth.models import User
from .forms import *
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


def tender_upload_list(request):
    tender = TenderUpload.objects.all()
    context = {
        'tender': tender
    }
    return render(request, 'government_employee/TenderUpload/tender_list.html', context=context)


def tender_upload_create(request):
    if request.method == "POST":
        form = TenderUploadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            t = form.save(commit=False)
            t.username = request.user
            t.save()
            return redirect(reverse('tender_upload_list'))
        context = {
            'form': form
        }
        return render(request, 'government_employee/TenderUpload/tender_create.html', context=context)
    if request.method == "GET":
        form = TenderUploadForm()
        context = {
            'form': form
        }
        return render(request, 'government_employee/TenderUpload/tender_create.html', context=context)


def tender_upload_update(request, tender_id):
    tender = TenderUpload.objects.get(id=tender_id)
    if request.method == "POST":
        form = TenderUploadForm(request.POST or None, request.FILES or None, instance=tender)
        if form.is_valid():
            form.save()
            return redirect(reverse('tender_upload_list'))
        context = {
                'form': form
            }
        return render(request, 'government_employee/TenderUpload/tender_upload.html', context=context)
    if request.method == "GET":
        form = TenderUploadForm(instance=tender)
        context = {
            'form': form
        }
        return render(request, 'government_employee/TenderUpload/tender_upload.html', context=context)


def tender_upload_delete(request, tender_id):
    tender = TenderUpload.objects.get(id=tender_id)
    if request.method == "POST":
        tender.delete()
        context = {
            'tender': tender
        }
        return render(request, 'government_employee/TenderUpload/tender_delete.html', context=context)
    if request.method == "GET":
        context = {
            'tender': tender
        }
        return render(request, 'government_employee/TenderUpload/tender_delete.html', context=context)


def tender_upload_details(request, tender_id):
    tender = TenderUpload.objects.get(id=tender_id)
    context = {
        'tender': tender
    }
    return render(request, 'government_employee/TenderUpload/tender_details.html', context=context)
