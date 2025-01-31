from django import forms
from . import models


class CidadeForm(forms.ModelForm):

    class Meta:
        model = models.Cidade
        fields = ['nome', 'estado']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome',
            'estado': 'Estado',
        }
