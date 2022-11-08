from django import forms
from .models import Apuntes, Contacto

class Formulario(forms.ModelForm):
    class Meta:
        model = Contacto
        fields=["nombre", "apellido","celular","cedula","email"]

class FormularioNotas(forms.ModelForm):
    class Meta:
        model = Apuntes
        fields=('email', 'nombre','contenido')

