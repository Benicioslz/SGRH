from django import forms
from . import models


class TipoContatoPessoaForm(forms.ModelForm):

    class Meta:
        model = models.TipoContatoPessoa
        fields = ['tipo_contato', 'pessoa', 'contato']
        widgets = {
            'tipo_contato': forms.Select(attrs={'class': 'form-control'}),
            'pessoa': forms.Select(attrs={'class': 'form-control'}),
            'contato': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'tipo_contato': 'Tipo de Contato',
            'pessoa': 'Pessoa',
            'contato': 'Contato',
        }
