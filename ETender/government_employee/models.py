from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Holder(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lisence_number = models.CharField(max_length=150, verbose_name='Lisence Number')

    def __str__(self):
        return self.lisence_number
