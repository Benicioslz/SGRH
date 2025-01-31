from django import forms
from . import models


class LotacaoForm(forms.ModelForm):

    class Meta:
        model = models.Lotacao
        fields = ['pessoa', 'setor', 'cargo', 'matricula', 'data_admissao', 'data_demissional']
        widgets = {
            'pessoa': forms.Select(attrs={'class': 'form-control'}),
            'setor': forms.Select(attrs={'class': 'form-control'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'data_admissao': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_demissional': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

        labels = {
            'pessoa': 'Pessoa',
            'setor': 'Setor',
            'cargo': 'Cargo',
            'matricula': 'Matrícula',
            'data_admissao': 'Data de Admissão',
            'data_demissional': 'Data Demissional',
        }
