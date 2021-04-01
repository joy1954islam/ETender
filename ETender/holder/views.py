from django.shortcuts import render
from government_employee.models import TenderUpload
from .forms import *


def home_tender_list(request):
    tender = TenderUpload.objects.all()[:5]
    context = {
        'tender': tender
    }
    return render(request, 'index.html', context=context)


def apply_tender_create(request, tender_id):
    tender = TenderUpload.objects.get(id=tender_id)
    form = ApplyTenderForm()
    if request.method == "POST":
        form = ApplyTenderForm(request.POST or None, request.FILES or None, instance=tender)
        if form.is_valid():
            ta = form.save(commit=False)
            tender_apply = ApplyTender()
            tender_apply.tender = tender
            tender_apply.username = request.user
            tender_apply.number = form.cleaned_data['number']
            tender_apply.trx_id = form.cleaned_data['trx_id']
            tender_apply.bank_trx_id = form.cleaned_data['bank_trx_id']
            tender_apply.proposal_pdf = form.cleaned_data['proposal_pdf']
            tender_apply.working_exprience = form.cleaned_data['working_exprience']
            tender_apply.save()
        context = {
            'form': form
        }
        return render(request, 'Holder/ApplyHolder/apply_holder_create.html', context=context)
    if request.method == "GET":
        context = {
            'form': form
        }
        return render(request, 'Holder/ApplyHolder/apply_holder_create.html', context=context)
