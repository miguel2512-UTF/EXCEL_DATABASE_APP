from django import forms

class ExcelForm(forms.Form):
    name = forms.CharField(label="Nombre del Excel", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ejemplo: Mi primer hoja de Excel", "autocomplete":"off"}))
    url = forms.CharField(label="Url del Excel (Formato CSV)", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ejemplo: https://docs.google.com/spreadsheets/d/e/2PACX-1vTsguMxjTn6cgROHODYdLOhnDlEFjCOkglShKEtfvi27sn6dh3bQv1dJOcWtqAVXg/pub?output=csv", "autocomplete":"off"}))
    load_images = forms.BooleanField(label="Las imagenes se cargan al abrir el excel (Se recomienda desactivar esta opción)", widget=forms.TextInput(attrs={"type":"checkbox", "class": "form-check-input"}), required=False)