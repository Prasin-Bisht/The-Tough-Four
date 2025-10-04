from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import ExpenseRequest
from employee.models import EmployeeExpense
from django.contrib.auth.decorators import login_required


def manager_dashboard(request):
    expenses = ExpenseRequest.objects.all()
    return render(request, 'review.html', {'expenses': expenses})

def approve_expense(request, expense_id):
    expense = ExpenseRequest.objects.get(id=expense_id)
    expense.status = 'Approved'
    expense.save()
    return redirect('manager_dashboard')


def reject_expense(request, expense_id):
    expense = ExpenseRequest.objects.get(id=expense_id)
    expense.status = 'Rejected'
    expense.save()
    return redirect('manager_dashboard')

def review(request):
    t=loader.get_template('review.html')
    return HttpResponse(t.render())

