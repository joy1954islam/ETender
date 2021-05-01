from django.db import models
from django.conf import settings
from government_employee.models import TenderUpload


class ApplyTender(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tender = models.ForeignKey(TenderUpload, on_delete=models.CASCADE)
    number = models.CharField(max_length=15, null=True, blank=True, verbose_name='Your Phone Number')
    trx_id = models.CharField(max_length=35, null=True, blank=True, verbose_name='Tender Free Trx ID')
    bank_trx_id = models.CharField(max_length=135, verbose_name='Security Money Trx ID')
    proposal_pdf = models.FileField(verbose_name='Proposal PDF')
    working_exprience = models.TextField(verbose_name='Working Experience')
    Payment = (
        ('Pending', 'Pending'),
        ('Accept', 'Accept'),
    )
    payment_status = models.CharField(max_length=7, choices=Payment, default='Pending', verbose_name='Payment Status')
    is_apply = models.BooleanField(default=False, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.tender)
