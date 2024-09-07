# Generated by Django 3.0.10 on 2024-09-07 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_budget', '0005_auto_20240907_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_budget.Child'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_budget.ExpenseCategory'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_budget.Child'),
        ),
    ]