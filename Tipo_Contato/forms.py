from django import forms
from . import models


class TipoContatoForm(forms.ModelForm):

    class Meta:
        model = models.TipoContato
        fields = ['nome',]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome',
        }
