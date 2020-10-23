from django.db import models

class TipoUsuario(models.Model):
    funcao = models.CharField(max_length=60)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.funcao
