from django.db import models
from Pessoa.models import Pessoa
from Setor.models import Setor
from Cargo.models import Cargo


class Lotacao(models.Model):
    id = models.AutoField(primary_key=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, related_name='lotacao_pessoa')
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT, related_name='lotacao_setor')
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, related_name='lotacao_cargo')
    matricula = models.CharField(max_length=5)
    data_admissao = models.DateField()
    data_demissional = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.pessoa
