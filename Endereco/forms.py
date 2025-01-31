from django import forms
from . import models


class EnderecoForm(forms.ModelForm):

    class Meta:
        model = models.Endereco
        fields = ['logradouro', 'cep', 'numero', 'complemento', 'pessoa', 'bairro']
        widgets = {
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'pessoa': forms.Select(attrs={'class': 'form-control'}),
            'bairro': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'logradouro': 'Logradouro',
            'cep': 'CEP',
            'numero': 'Número',
            'complemento': 'Complemento',
            'pessoa': 'Pessoa',
            'bairro': 'Bairro',
        }
