from django.urls import path
from . import views

urlpatterns = [
    path('expenses/', views.expenses, name='expenses'),
    path('receipt/', views.receipt, name='receipt'),
]
