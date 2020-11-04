from django.db import models
from produto.models import Produto
from django.contrib.auth.models import User

class EstoqueSaida(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET('Produto descontinuado'))
    justificativa = models.TextField()
    data = models.DateField()
    quantidade_saida = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.produto.nome

