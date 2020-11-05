from estoque_entrada.models import EstoqueEntrada
from produto.api.serializers import ProdutoSerializer
from produto.api.viewsets import ProdutoViewSet
from produto.models import Produto
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import EstoqueEntradaSerializer


class EstoqueEntradaViewSet(ModelViewSet):
    queryset = EstoqueEntrada.objects.all()
    serializer_class = EstoqueEntradaSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def create(self, request, *args, **kwargs):

        produto_queryset = Produto.objects.filter(id=request.data['produto'])
        quantidade_entrada = int(request.data['quantidade_entrada'])
        quantidade_produto = produto_queryset[0].quantidade_estoque
        quantidade_produto = quantidade_produto + quantidade_entrada
        produto_serializer = ProdutoSerializer(produto_queryset, many=True)
        produto_data = produto_serializer.data
        produto_data[0]['quantidade_estoque'] = quantidade_produto
        produto = Produto.objects.get(id=request.data['produto'])
        produto.quantidade_estoque = produto_data[0]['quantidade_estoque']
        produto.save()
        print(request.data['usuario'])
        # request.data[0]['usuario'] = request.user.pk
        entrada_serializer = self.get_serializer(data=request.data)
        entrada_serializer.is_valid(raise_exception=True)
        self.perform_create(entrada_serializer)
        headers = self.get_success_headers(entrada_serializer.data)
        return Response(entrada_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
