# Generated by Django 3.0.10 on 2024-09-07 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_budget', '0006_auto_20240907_1400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='budget',
            old_name='date_allocated',
            new_name='date_1',
        ),
    ]
