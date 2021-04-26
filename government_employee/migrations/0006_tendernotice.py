# Generated by Django 2.2.5 on 2021-04-26 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('government_employee', '0005_auto_20210405_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='TenderNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.TextField(verbose_name='Tender Notice')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('tender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='government_employee.TenderUpload')),
            ],
        ),
    ]
