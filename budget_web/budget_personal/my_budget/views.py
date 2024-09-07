
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BudgetForm, ExpenseForm
from .models import Budget, Expense

def create_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('budget_list') 
    else:
        form = BudgetForm()
    return render(request, 'create_budget.html', {'form': form})

def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list') 
        form = ExpenseForm()
    return render(request, 'create_expense.html', {'form': form})

def budget_list(request):
    budgets = Budget.objects.all()
    return render(request, 'budget_list.html', {'budgets': budgets})

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})

def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')  
    return render(request, 'delete_expense.html', {'expense': expense})
