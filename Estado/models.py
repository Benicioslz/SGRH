from django.db import models


class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=21)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
