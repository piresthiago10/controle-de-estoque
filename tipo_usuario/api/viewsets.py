from rest_framework.viewsets import ModelViewSet
from tipo_usuario.models import TipoUsuario
from .serializers import TipoUsuarioSerializer


class TipoUsuarioViewSet(ModelViewSet):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer