from django import forms
from . import models


class GeneroForm(forms.ModelForm):

    class Meta:
        model = models.Genero
        fields = ['nome',]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome',
        }
