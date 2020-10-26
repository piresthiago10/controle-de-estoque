from estoque_saida.models import EstoqueSaida
from rest_framework.serializers import ModelSerializer


class EstoqueSaidaSerializer(ModelSerializer):

    class Meta:
        model = EstoqueSaida
        fields = ('id', 'produto', 'data', 'quantidade_saida', 'justificativa', 'usuario')
