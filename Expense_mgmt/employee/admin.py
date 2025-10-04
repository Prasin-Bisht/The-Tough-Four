from django.contrib import admin
from .models import EmployeeExpense

@admin.register(EmployeeExpense)
class EmployeeExpenseAdmin(admin.ModelAdmin):
    list_display = ('employee', 'category', 'amount', 'status', 'date')
    list_filter = ('status', 'category', 'date')
    search_fields = ('employee__username', 'category', 'remarks')
