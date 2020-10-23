from django.db import models
from tipo_usuario.models import TipoUsuario

class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    login = models.CharField(max_length=60)
    senha = models.CharField(max_length=32)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.SET('Classificação Excluída'))

    def __str__(self):
        return self.nome
 