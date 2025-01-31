from django.db import models
from Pessoa.models import Pessoa
from Bairro.models import Bairro


class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    logradouro = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    numero = models.IntegerField(blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, related_name='endereco_pessoa')
    bairro = models.ForeignKey(Bairro, on_delete=models.PROTECT, related_name='endereco_bairro')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.logradouro
