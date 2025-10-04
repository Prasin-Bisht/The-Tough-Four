from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import EmployeeExpense
from .forms import EmployeeExpenseForm



def expenses(request):
    expense = EmployeeExpense.objects.all()
    return render(request, 'expenses.html', {'expenses': expense})

def receipt(request):
    if request.method == 'POST':
        form = EmployeeExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.employee = request.user
            expense.status = 'Pending'
            expense.save()
            return redirect('review')
    else:
        form = EmployeeExpenseForm()
    return render(request, 'receipt.html', {'form': form})


def register(request):
    if request.method == 'POST':
        v = EmployeeExpenseForm(request.POST,request.FILES)
        if v.is_valid():
            v.save()
            return redirect('expenses')
    else:
        v = EmployeeExpenseForm()
    return render(request, 'review.html', {'v': v})