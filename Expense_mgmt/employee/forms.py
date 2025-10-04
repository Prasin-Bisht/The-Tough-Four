from django import forms
from .models import EmployeeExpense

class EmployeeExpenseForm(forms.ModelForm):
    class Meta:
        model = EmployeeExpense
        fields = ['description', 'date', 'category', 'paid_by', 'remarks', 'amount',]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }