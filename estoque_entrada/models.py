from django.contrib.auth.models import User
from django.db import models
from produto.models import Produto


class EstoqueEntrada(models.Model):
    produto = models.ForeignKey(
        Produto, on_delete=models.SET('Produto descontinuado'))
    data = models.DateField()
    quantidade_entrada = models.IntegerField()
    valor_pago = models.DecimalField(max_digits=5, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.produto.nome
