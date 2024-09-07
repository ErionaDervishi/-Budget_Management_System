from django.contrib import admin
from .models import Budget, Expense, Child, ExpenseCategory
from .forms import BudgetForm, ExpenseForm

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    form = BudgetForm
    list_display = ('child', 'category', 'amount', 'month', 'date_1')
    list_filter = ('child', 'category', 'month')
    search_fields = ('child__name', 'category__name')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    form = ExpenseForm
    list_display = ('child', 'category', 'amount', 'month', 'date_spent')
    list_filter = ('child', 'category', 'month')
    search_fields = ('child__name', 'category__name')

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
