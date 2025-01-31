from django import forms
from . import models


class HistoricoSalarialForm(forms.ModelForm):

    class Meta:
        model = models.HistoricoSalarial
        fields = ['pessoa', 'carga_horaria', 'salario']
        widgets = {
            'pessoa': forms.Select(attrs={'class': 'form-control'}),
            'carga_horaria': forms.TextInput(attrs={'class': 'form-control'}),
            'salario': forms.TextInput(attrs={'class': 'form-control'}),
            'data_cadastro': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'pessoa': 'Pessoa',
            'carga_horaria': 'Carga Horária',
            'salario': 'Salário',
            'data_cadastro': 'Data de Cadastro',
        }
