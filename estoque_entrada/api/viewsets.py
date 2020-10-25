from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from estoque_entrada.models import EstoqueEntrada
from produto.models import Produto
from .serializers import EstoqueEntradaSerializer


class EstoqueEntradaViewSet(ModelViewSet):
    queryset = EstoqueEntrada.objects.all()
    serializer_class = EstoqueEntradaSerializer

    def create(self, request, *args, **kwargs):

        produto_queryset = Produto.objects.filter(id=request.data['produto'])
        quantidade_entrada = int(request.data['quantidade_entrada'])
        quantidade_produto = produto_queryset[0].quantidade_estoque
        print(type(quantidade_entrada), type(quantidade_produto))
        quantidade_produto = quantidade_produto + quantidade_entrada
        produto_serializer = self.get_serializer(data=dict(produto_queryset))
        produto_serializer.is_valid(raise_exception=True)
        self.perform_create(produto_serializer)

        entrada_serializer = self.get_serializer(data=request.data)
        entrada_serializer.is_valid(raise_exception=True)
        self.perform_create(entrada_serializer)
        headers = self.get_success_headers(entrada_serializer.data)
        return Response(entrada_serializer.data, status=status.HTTP_201_CREATED, headers=headers)