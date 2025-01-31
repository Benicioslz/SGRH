from django import forms
from . import models


class SetorForm(forms.ModelForm):

    class Meta:
        model = models.Setor
        fields = ['nome',]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome',
        }
