from django import forms
from .models import *


class ApplyTenderForm(forms.ModelForm):
    number = forms.CharField(required=True, label='Payment Phone Number')
    trx_id = forms.CharField(required=True)

    class Meta:
        model = ApplyTender
        fields = ['payment_method', 'number', 'trx_id', 'bank_trx_id', 'bank_check_image', 'proposed_amount',
                  'proposal_pdf', 'working_experience']
