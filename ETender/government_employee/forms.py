from django import forms
from .models import *


class TenderUploadForm(forms.ModelForm):
    publish_date = forms.DateField(widget=forms.SelectDateWidget)
    end_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = TenderUpload
        fields = ['title', 'ministry_name', 'publish_date', 'end_date', 'pdf']
