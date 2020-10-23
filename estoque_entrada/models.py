from django.db import models
from produto.models import Produto
from usuario.models import Usuario

class EstoqueEntrada(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET('Produto descontinuado'))
    data = models.DateField()
    quantidade_entrada = models.IntegerField()
    valor_pago = models.DecimalField(max_digits=5, decimal_places=2)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET('Usuário Excluído'))

    def __str__(self):
        return self.produto.nome

