from rest_framework.serializers import ModelSerializer
from produto.models import Produto


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ('id', 'nome', 'descricao', 'categoria', 'quantidade_estoque', 'imagem')