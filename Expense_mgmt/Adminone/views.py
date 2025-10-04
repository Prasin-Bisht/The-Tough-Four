from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import AccountModel
from .forms import AccountForm,LoginForm
# Create your views here.

def singup(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created successfully!')
            return redirect('singup')
    else:
        form = AccountForm()
    return render(request,'login.html',{'form':form})


@login_required
def login(request):
    if request.method == 'POST':
        f = LoginForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect('login')
    else:
        f = AccountForm()
    return render(request, 'login.html', {'f': f})


