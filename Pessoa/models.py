from django.db import models
from Genero.models import Genero


class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    rg = models.CharField(max_length=15, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    ctps = models.CharField(max_length=30, unique=True)
    data_nascimento = models.DateField()
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, related_name='pessoa_genero')

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
