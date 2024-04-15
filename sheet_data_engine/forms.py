from django import forms

class SheetForm(forms.Form):
    name = forms.CharField(label="Nombre del Sheet", widget=forms.TextInput(attrs={"input_type": "text", "placeholder":"Ejemplo: Mi primer sheet", "autocomplete":"off"}))
    url = forms.CharField(label="Url del Sheet (Formato CSV)", widget=forms.TextInput(attrs={"input_type": "text", "placeholder":"Ejemplo: https://docs.google.com/spreadsheets/d/e/2PACX-1vTsguMxjTn6cgROHODYdLOhnDlEFjCOkglShKEtfvi27sn6dh3bQv1dJOcWtqAVXg/pub?output=csv", "autocomplete":"off"}))

class ApiForm(forms.Form):
    url_api = forms.CharField(label="Url de la API", widget=forms.TextInput(attrs={"input_type": "text", "autocomplete":"off", "readonly": ""}))
    api_password = forms.CharField(label="Contraseña de la API", widget=forms.PasswordInput(attrs={"input_type": "password", "placeholder":"Ejemplo: password", "autocomplete":"off"}))