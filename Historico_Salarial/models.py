from django.db import models
from Pessoa.models import Pessoa


class HistoricoSalarial(models.Model):
    id = models.AutoField(primary_key=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, related_name='hs_pessoa')
    carga_horaria = models.IntegerField()
    salario = models.DecimalField(max_digits=18, decimal_places=2)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data_cadastro']

    def __str__(self):
        return self.salario
