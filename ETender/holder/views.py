from django.shortcuts import render
from government_employee.models import TenderUpload


def home_tender_list(request):
    tender = TenderUpload.objects.all()[:5]
    context = {
        'tender': tender
    }
    return render(request, 'index.html', context=context)
