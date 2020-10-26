from rest_framework.serializers import ModelSerializer
from produto.api.serializers import ProdutoSerializer
from estoque_entrada.models import EstoqueEntrada



class EstoqueEntradaSerializer(ModelSerializer):
    # produto = ProdutoSerializer()

    class Meta:
        model = EstoqueEntrada
        fields = ('id', 'produto', 'data', 'quantidade_entrada', 'valor_pago', 'usuario')