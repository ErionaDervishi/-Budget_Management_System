from django import forms
from .models import Budget, Expense

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['child', 'category', 'amount', 'date_1', 'month']
        widgets = {
            'date_1': forms.DateInput(attrs={'type': 'date'}),
            'month': forms.TextInput(attrs={'placeholder': 'YYYY-MM'}),
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['child', 'category', 'amount', 'date_spent', 'month']
        widgets = {
            'date_spent': forms.DateInput(attrs={'type': 'date'}),
            'month': forms.TextInput(attrs={'placeholder': 'YYYY-MM'}),
        }
