# Generated by Django 3.0.10 on 2024-09-07 18:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_budget', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='month',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
