from django.urls import path
from . import views

urlpatterns = [
    path('manager_dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('approve/<int:expense_id>/', views.approve_expense, name='approve_expense'),
    path('reject/<int:expense_id>/', views.reject_expense, name='reject_expense'),
    path('review/', views.review, name='review'),
]