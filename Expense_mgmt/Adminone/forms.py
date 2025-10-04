from django import forms
from .models import AccountModel, Expense, ApprovalRule
from django.contrib.auth.models import User


class AccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmpassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = AccountModel
        fields = ['name', 'email', 'password', 'confirmpassword', 'countrySelection', 'manager', 'role']

    # validate password match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirmpassword")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data


class ExpenseForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})  # HTML5 date picker
    )

    class Meta:
        model = Expense
        fields = ['employee', 'amount', 'currency', 'category', 'description', 'date', 'status']


class ApprovalRuleForm(forms.ModelForm):
    approvers = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # allows multiple checkboxes for approvers
        required=True
    )

    class Meta:
        model = ApprovalRule
        fields = ['user', 'approvers', 'is_manager_approver', 'min_approval_percentage']
