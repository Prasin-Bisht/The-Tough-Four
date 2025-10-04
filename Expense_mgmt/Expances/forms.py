from django import forms
from .models import Expense


# Employee submits an expense
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = [
            'amount',
            'currency',
            'category',
            'description',
            'date',
            'receipt',
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }


# Manager/Admin updates expense status
class ExpenseApprovalForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['status']
