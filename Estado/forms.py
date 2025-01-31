from django import forms
from . import models


class EstadoForm(forms.ModelForm):

    class Meta:
        model = models.Estado
        fields = ['sigla', 'nome']
        widgets = {
            'sigla': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'sigla': 'Sigla',
            'nome': 'Nome',
        }
