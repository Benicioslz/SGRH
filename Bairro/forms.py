from django import forms
from . import models


class BairroForm(forms.ModelForm):

    class Meta:
        model = models.Bairro
        fields = ['nome', 'cidade']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'nome': 'Nome',
            'cidade': 'Cidade',
        }
