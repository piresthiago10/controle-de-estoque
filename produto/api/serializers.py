from categoria.models import Categoria
from produto.models import Produto
from rest_framework.serializers import ModelSerializer


class ProdutoSerializer(ModelSerializer):

    class Meta:
        model = Produto
        fields = ('id', 'nome', 'descricao', 'categoria',
                  'quantidade_estoque', 'imagem')
