# Generated by Django 2.2.5 on 2021-04-01 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('government_employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenderupload',
            name='amount',
        ),
    ]
