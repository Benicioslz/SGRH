from django.db import models
from Pessoa.models import Pessoa
from Tipo_Contato.models import TipoContato


class TipoContatoPessoa(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_contato = models.ForeignKey(TipoContato, on_delete=models.PROTECT, related_name='tcp_tc')
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, related_name='tcp_pessoa')
    contato = models.CharField(max_length=45)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.contato
