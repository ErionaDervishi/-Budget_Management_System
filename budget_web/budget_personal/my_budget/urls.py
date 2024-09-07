from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_budget, name='create_budget'),
    path('create-expense/', views.create_expense, name='create_expense'),
    path('budgets/', views.budget_list, name='budget_list'),
    path('expenses/', views.expense_list, name='expense_list'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'), 
]
