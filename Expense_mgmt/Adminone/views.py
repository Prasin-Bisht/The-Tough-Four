from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AccountModel
from .forms import AccountForm, ExpenseForm, ApprovalRuleForm


def account_login(request):   # ✅ renamed to avoid conflict
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')   # ✅ fixed username issue
            messages.success(request, f'Account for {name} created successfully!')
            return redirect('table')
    else:
        form = AccountForm()
    return render(request, 'login.html', {'form': form})


def signup(request):   # ✅ corrected name
    if request.method == 'POST':
        f = AccountForm(request.POST)   # ✅ use AccountForm instead of LoginForm
        if f.is_valid():
            f.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect('account_login')
    else:
        f = AccountForm()
    return render(request, 'signup.html', {'f': f})


def table(request):
    p = AccountModel.objects.all()
    return render(request, 'table.html', {'u': p})


def newuser(request):
    if request.method == 'POST':
        u = AccountForm(request.POST, request.FILES)
        if u.is_valid():
            u.save()
            messages.success(request, "New user created successfully!")
            return redirect('table')
    else:
        u = AccountForm()
    return render(request, 'newuser.html', {'u': u})
