from django.db import models
from django.utils import timezone

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100, choices=[
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('entertainment', 'Entertainment'),
    ])

    def __str__(self):
        return self.get_name_display()  

class Child(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Budget(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)  
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_1 = models.DateField(default=timezone.now)
    month = models.CharField(max_length=7, default=timezone.now().strftime('%Y-%m'))  

    def __str__(self):
        return f"{self.child.name} - {self.category.name} - {self.month}: {self.amount}"

class Expense(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)  
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)  
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_spent = models.DateField(default=timezone.now)
    month = models.CharField(max_length=7, default=timezone.now().strftime('%Y-%m')) 

    def __str__(self):
        return f"{self.child.name} - {self.category.name} - {self.month}: {self.amount}"
