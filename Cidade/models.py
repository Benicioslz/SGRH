from django.db import models
from Estado.models import Estado


class Cidade(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=32)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, related_name='cidade_estado')

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
