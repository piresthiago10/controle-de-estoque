from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from produto.models import Produto
from .serializers import ProdutoSerializer


class ProdutoViewSet(ModelViewSet):
    # queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get_queryset(self):
        return Produto.objects.all()



    