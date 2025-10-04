# admin.py
from django.contrib import admin
from .models import AccountModel

@admin.register(AccountModel)
class EmployeeUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'manager')
    search_fields = ('name', 'role', 'email', 'manager')
    list_filter = ('role',)
