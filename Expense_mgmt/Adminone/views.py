from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import AccountModel
from .forms import AccountForm,LoginForm
# Create your views here.

def login(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your acccount')
            return redirect('table')
    else:
        form = AccountForm()
    return render(request,'login.html',{'form':form})



def singup(request):
    if request.method == 'POST':
        f_1 = LoginForm(request.POST)
        if f_1.is_valid():
            f.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect('login')
    else:
        f = AccountForm()
    return render(request, 'singup.html', {'f': f})


def table(request):
    p = AccountModel.objects.all()
    return render(request,'table.html',{'u':p})

def newuser(request):
    if request.method == 'POST':
        u = AccountForm(request.POST , request.FILES)
        if u.is_valid():
            u.save()
            messages.success(request, "New user created successfully!")
            return redirect('table')
    else:
        u = AccountForm()
    return render(request, 'newuser.html', {'u': u})

