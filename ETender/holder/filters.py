from django.contrib.auth.models import User
import django_filters
from government_employee.models import TenderUpload
from django.contrib.auth import get_user_model
User = get_user_model()


class TenderUploadFilter(django_filters.FilterSet):
    class Meta:
        model = TenderUpload
        fields = ['ministry_name']
