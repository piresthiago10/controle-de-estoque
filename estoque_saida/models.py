from django.db import models
from produto.models import Produto
from usuario.models import Usuario

class EstoqueSaida(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET('Produto descontinuado'))
    justificativa = models.TextField()
    data = models.DateField()
    quantidade_saida = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.SET('Usuário Excluído'))

    def __str__(self):
        return self.produto.nome

