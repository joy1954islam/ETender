from django import forms
from .models import *


class ApplyTenderForm(forms.ModelForm):
    number = forms.CharField(required=True)
    trx_id = forms.CharField(required=True)

    class Meta:
        model = ApplyTender
        fields = ['number', 'trx_id', 'bank_trx_id', 'proposal_pdf', 'working_exprience']
