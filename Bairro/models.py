from django.db import models
from Cidade.models import Cidade


class Bairro(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, related_name='bairro_cidade')

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
