from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('accounts/login/?next=/singup/', views.singup, name='singup'),
]
