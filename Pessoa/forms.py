from django import forms
from . import models


class PessoaForm(forms.ModelForm):

    class Meta:
        model = models.Pessoa
        fields = ['nome', 'rg', 'cpf', 'ctps', 'data_nascimento', 'genero']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'ctps': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateField(widget=forms.DateInput(format='%dd/%mm/%YYYY')),
            'genero': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'nome': 'Nome',
            'rg': 'RG',
            'cpf': 'CPF',
            'ctps': 'CTPS',
            'data_nascimento': 'Data de Nascimento',
            'genero': 'Gênero',
        }
