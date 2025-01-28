from django import forms
from .models import Orden

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['marca_vehiculo', 'modelo_vehiculo', 'patente_vehiculo', 'cliente', 'imagenes', 'modalidad']