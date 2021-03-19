from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib import auth


from django.db import models
from django.urls import reverse


class Ministry(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    MinistryName = models.CharField(max_length=100)
    MinisterName = models.CharField(max_length=100)
    Email = models.EmailField()

    def __str__(self):
        return self.MinistryName


