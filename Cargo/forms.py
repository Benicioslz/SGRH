from django import forms
from . import models


class CargoForm(forms.ModelForm):

    class Meta:
        model = models.Cargo
        fields = ['nome',]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome',
        }
