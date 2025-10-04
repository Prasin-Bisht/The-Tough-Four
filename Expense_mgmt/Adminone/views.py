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


<<<<<<< HEAD
=======

>>>>>>> ae2de2b1c007357b800af2b29d3f609326ba8291
def singup(request):
    if request.method == 'POST':
        f = AccountForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect('login')
    else:
        f = AccountForm()
<<<<<<< HEAD
    return render(request, 'signup.html', {'f': f})


def table(request):
    p = AccountModel.objects.all()
    return render(request,'table.html',{'p':p})
=======
    return render(request, 'signup.html',{'f': f})
>>>>>>> ae2de2b1c007357b800af2b29d3f609326ba8291
