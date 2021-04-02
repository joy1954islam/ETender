from django.shortcuts import render, redirect, reverse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from holder.models import ApplyTender
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


def list_of_apply_tender(request, tender_id):
    apply_tender = ApplyTender.objects.filter(tender=tender_id)
    context = {
        'apply_tender': apply_tender,
    }
    return render(request, 'government_employee/ApplyTender/apply_tender_list.html', context=context)


def apply_tender_holder_details(request, tender_id):
    tender = TenderUpload.objects.get(id=tender_id)
    apply_tender = ApplyTender.objects.get(tender=tender)

    context = {
        'apply_tender': apply_tender
    }
    return render(request, 'government_employee/ApplyTender/apply_tender_details.html', context=context)


def change_status_of_apply_tender_holder(request, tender_id):
    tender = TenderUpload.objects.get(id=tender_id)
    apply_tender = ApplyTender.objects.get(tender=tender)
    print(apply_tender)
    form = ApplyTenderHolderUpdateForm()
    if request.method == "POST":
        form = ApplyTenderHolderUpdateForm(request.POST or None, instance=apply_tender)
        if form.is_valid():
            form.save()
            return redirect('list_of_apply_tender', tender_id)
    if request.method == "GET":
        context = {
            'form': form
        }
        return render(request, 'government_employee/ApplyTender/apply_tender_status_change.html', context=context)


def short_list_of_apply_tender_holder(request, tender_id, user_id):
    tender = TenderUpload.objects.get(id=tender_id)
    apply_tender = ApplyTender.objects.get(tender=tender)
    user = User.objects.get(id=user_id)
    short_list = ApplyTenderHolderShortList()
    short_list.tender = apply_tender
    short_list.username = user
    exists_user = ApplyTenderHolderShortList.objects.filter(tender=apply_tender, username=user)
    if exists_user.exists():
        messages.add_message(request, messages.INFO, 'This User Is Already Short Listed')
        return redirect('list_of_apply_tender', tender_id)
    else:
        short_list.save()
        return redirect('list_of_apply_tender', tender_id)


def list_of_holder_short_list(request, tender_id):
    tender = TenderUpload.objects.get(id=tender_id)
    apply_tender = ApplyTender.objects.get(tender=tender)
    short_list = ApplyTenderHolderShortList.objects.filter(tender=apply_tender)
    context = {
        'short_list': short_list
    }
    return render(request, 'government_employee/ApplyTender/apply_tender_holder_short_list.html', context=context)
