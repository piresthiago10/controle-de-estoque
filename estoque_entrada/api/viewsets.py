from rest_framework.viewsets import ModelViewSet
from estoque_entrada.models import EstoqueEntrada
from .serializers import EstoqueEntradaSerializer


class EstoqueEntradaViewSet(ModelViewSet):
    queryset = EstoqueEntrada.objects.all()
    serializer_class = EstoqueEntradaSerializer