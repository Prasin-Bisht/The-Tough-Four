from django import forms
from .models import AccountModel


class AccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmpassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = AccountModel
        fields = ['name', 'email', 'password', 'confirmpassword', 'countrySelection']

    # validate password match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmpassword = cleaned_data.get("confirmpassword")

        if password and confirmpassword and password != confirmpassword:
            self.add_error("confirmpassword", "Passwords do not match")
        return cleaned_data
