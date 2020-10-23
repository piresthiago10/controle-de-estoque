from django.db import models
from categoria.models import Categoria

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET('Categoria Excluída'))
    quantidade_estoque = models.IntegerField(null=True, blank=True)
    imagem = models.ImageField(upload_to='produto', null=True, blank=True)
    
    def __str__(self):
        return self.nome
