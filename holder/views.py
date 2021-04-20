from django.shortcuts import render
from government_employee.models import TenderUpload
from .forms import *
from django.contrib.auth.decorators import login_required
from government_employee.models import ApplyTenderHolderShortList, WinnerHolder
from .filters import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def home_tender_list(request):
    tender = TenderUpload.objects.all()
    MyFilter = TenderUploadFilter(request.GET, queryset=tender)
    tender = MyFilter.qs
    page = request.GET.get('page', 1)
    paginator = Paginator(tender, 10)
    try:
        tender = paginator.page(page)
    except PageNotAnInteger:
        tender = paginator.page(1)
    except EmptyPage:
        tender = paginator.page(paginator.num_pages)

    context = {
        'tender': tender,
        'MyFilter': MyFilter
    }
    return render(request, 'index.html', context=context)


def list_of_apply_tender(request):
    apply_tender = ApplyTender.objects.filter(username=request.user)
    page = request.GET.get('page', 1)
    paginator = Paginator(apply_tender, 10)
    try:
        apply_tender = paginator.page(page)
    except PageNotAnInteger:
        apply_tender = paginator.page(1)
    except EmptyPage:
        apply_tender = paginator.page(paginator.num_pages)

    context = {
        'apply_tender': apply_tender
    }
    return render(request, 'Holder/ApplyHolder/apply_tender_list.html', context=context)


@login_required(login_url='log_in')
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


def holder_list_of_holder_short_list(request, tender_id):
    short_list = ApplyTenderHolderShortList.objects.filter(tender_id=tender_id)
    context = {
        'short_list': short_list
    }
    return render(request, 'Holder/ApplyHolder/apply_tender_holder_short_list.html', context=context)


def holder_winner_holder_list(request, tender_id):
    winner_holder = WinnerHolder.objects.filter(tender=tender_id)
    context = {
        'winner_holder': winner_holder
    }
    return render(request, 'Holder/ApplyHolder/winner_holder_list.html', context=context)


def user_winner_holder_list(request):
    winner_holder = WinnerHolder.objects.filter(username=request.user)
    page = request.GET.get('page', 1)
    paginator = Paginator(winner_holder, 10)
    try:
        winner_holder = paginator.page(page)
    except PageNotAnInteger:
        winner_holder = paginator.page(1)
    except EmptyPage:
        winner_holder = paginator.page(paginator.num_pages)

    context = {
        'winner_holder': winner_holder
    }
    return render(request, 'Holder/ApplyHolder/my_tender_list.html', context=context)
