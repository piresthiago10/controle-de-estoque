from rest_framework.serializers import ModelSerializer
from tipo_usuario.models import TipoUsuario


class TipoUsuarioSerializer(ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = ('id', 'funcao', 'descricao')