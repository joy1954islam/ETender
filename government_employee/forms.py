from django import forms
from .models import *
from holder.models import ApplyTender


class TenderUploadForm(forms.ModelForm):

    publish_date = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date"}))
    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date"}))

    class Meta:
        model = TenderUpload
        fields = ['title', 'ministry_name', 'publish_date', 'end_date', 'pdf']


class ApplyTenderHolderUpdateForm(forms.ModelForm):
    class Meta:
        model = ApplyTender
        fields = ['payment_status', 'is_apply']


class TenderNoticeForm(forms.ModelForm):
    class Meta:
        model = TenderNotice
        fields = ['notice']
