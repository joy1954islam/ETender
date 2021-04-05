# Generated by Django 2.2.5 on 2021-04-05 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('government_employee', '0004_winnerholder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winnerholder',
            name='tender',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='holder.ApplyTender'),
        ),
        migrations.AlterField(
            model_name='winnerholder',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
