from django import forms

from .models import Vehiculo


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
        # fields = "__all__" -> incluir todos los atributos del modelo
        # exclude = ['direccion'] -> no incluir los atributos que queremos
        widgets = {
            'marca': forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'serial_carroceria': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'serial_motor': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'categoria': forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'required': 'required', 'value': 9999999, 'min': 1}),
        }

    # marca = models.CharField(max_length=20, choices=MARCAS, default='Ford')
    # modelo = models.CharField(max_length=100)
    # serial_carroceria = models.CharField(max_length=50)
    # categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='Particular')
    # precio = models.IntegerField()

        