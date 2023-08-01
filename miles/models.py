from django.db import models


class Depoimento(models.Model):
    foto = models.ImageField()
    depoimento = models.TextField(max_length=500)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
