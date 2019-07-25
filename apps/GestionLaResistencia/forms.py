from django import forms

class RegForm(forms.Form):
    Cédula = forms.IntegerField(max_value=9999999999)
    Nombre = forms.CharField(max_length=40)
    Apellido = forms.CharField(max_length=40)
    Edad = forms.IntegerField(max_value=99)
    Nacimiento = forms.DateField()