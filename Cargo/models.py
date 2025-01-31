from django.db import models


class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
