from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from SuperAdmin.models import Ministry


class Holder(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lisence_number = models.CharField(max_length=150, verbose_name='Lisence Number')

    def __str__(self):
        return self.lisence_number


class TenderUpload(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ministry_name = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name='Tender Title')
    amount = models.IntegerField(verbose_name='Tender/Proposal security(Amount in BDT)')
    publish_date = models.DateField(verbose_name='Tender Publish Date')
    end_date = models.DateField(verbose_name='Tender Publish Date End')
    pdf = models.FileField(verbose_name='Tender Details Pdf')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
