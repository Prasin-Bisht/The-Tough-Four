from django.shortcuts import render,redirect
from django.contrib import messages
from .models import AccountModel
from .forms import AccountForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect('login')
    else:
        form = AccountForm()
    return render(request, 'singup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = AccountModel.objects.get(email=email, password=password)
            # Store user id in session
            request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            return redirect('home')  # redirect to a home/dashboard page
        except AccountModel.DoesNotExist:
            messages.error(request, "Invalid email or password")
            return redirect('login')
    return render(request, 'login.html')
