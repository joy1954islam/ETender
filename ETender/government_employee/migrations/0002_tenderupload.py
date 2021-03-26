# Generated by Django 2.2.5 on 2021-03-26 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SuperAdmin', '0002_ministry_username'),
        ('government_employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TenderUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Tender Title')),
                ('publish_date', models.DateField(auto_now_add=True, verbose_name='Tender Publish Date')),
                ('end_date', models.DateField(verbose_name='Tender Publish Date End')),
                ('pdf', models.FileField(upload_to='', verbose_name='Tender Details Pdf')),
                ('ministry_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SuperAdmin.Ministry')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
