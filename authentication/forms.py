from django.contrib.auth.forms import AuthenticationForm
from django import forms

class LoginAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"input_type": "text", "autocomplete": "off"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"input_type": "password", "autocomplete": "off"}))