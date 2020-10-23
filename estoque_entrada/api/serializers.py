from rest_framework.serializers import ModelSerializer
from estoque_entrada.models import EstoqueEntrada


class EstoqueEntradaSerializer(ModelSerializer):
    class Meta:
        model = EstoqueEntrada
        fields = ('id', 'produto', 'data', 'quantidade_entrada', 'valor_pago', 'usuario')