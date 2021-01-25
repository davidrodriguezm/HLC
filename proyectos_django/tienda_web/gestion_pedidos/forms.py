from django import forms

class Formulario_cliente( forms.Form ):
    nombre = forms.CharField()
    direccion = forms.CharField()
    email = forms.EmailField()
    telefono = forms.CharField()