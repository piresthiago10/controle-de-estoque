from estoque_entrada.models import EstoqueEntrada
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class EstoqueEntradaSerializer(ModelSerializer):
    usuario = User.objects.all()

    class Meta:
        model = EstoqueEntrada
        fields = ('id', 'produto', 'data', 'quantidade_entrada', 'valor_pago', 'usuario')
