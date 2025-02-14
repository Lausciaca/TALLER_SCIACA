from django import forms
from .models import Orden


class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['nombre_cliente', 'telefono_cliente', 'marca_vehiculo', 'modelo_vehiculo', 'patente_vehiculo', 'imagenes', 'modalidad', 'trabajos_a_realizar']
        widgets = {
            'nombre_cliente': forms.TextInput(attrs={'class': 'input-container-input', 'id': 'nombre_cliente'}),
            'telefono_cliente': forms.TextInput(attrs={'class': 'input-container-input', 'id': 'telefono_cliente'}),
            'marca_vehiculo': forms.TextInput(attrs={'class': 'input-container-input', 'id': 'marca_vehiculo'}),
            'modelo_vehiculo': forms.TextInput(attrs={'class': 'input-container-input', 'id': 'modelo_vehiculo'}),
            'patente_vehiculo': forms.TextInput(attrs={'class': 'input-container-input', 'id': 'patente_vehiculo'}),
            'imagenes': forms.ClearableFileInput(attrs={'class': 'input-container-input', 'id': ''}),
            'modalidad': forms.Select(attrs={'class': 'input-container-input', 'id': 'modalidad'}),
            'trabajos_a_realizar': forms.Textarea(attrs={'class': 'input-container-input', 'id': 'trabajos'})
        }


