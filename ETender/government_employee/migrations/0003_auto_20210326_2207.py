# Generated by Django 2.2.5 on 2021-03-26 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('government_employee', '0002_tenderupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenderupload',
            name='publish_date',
            field=models.DateField(verbose_name='Tender Publish Date'),
        ),
    ]
