from estoque_saida.models import EstoqueSaida
from produto.api.serializers import ProdutoSerializer
from produto.models import Produto
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import EstoqueSaidaSerializer


class EstoqueSaidaViewSet(ModelViewSet):
    queryset = EstoqueSaida.objects.all()
    serializer_class = EstoqueSaidaSerializer

    def create(self, request, *args, **kwargs):

        produto_queryset = Produto.objects.filter(id=request.data['produto'])
        quantidade_saida = int(request.data['quantidade_saida'])
        quantidade_produto = produto_queryset[0].quantidade_estoque

        if quantidade_saida > quantidade_produto:
            return Response({"Operação não permitida": "A quantidade de saída é maior do que a quantidade em estoque!"})

        quantidade_produto = quantidade_produto - quantidade_saida
        produto_serializer = ProdutoSerializer(produto_queryset, many=True)
        produto_data = produto_serializer.data
        produto_data[0]['quantidade_estoque'] = quantidade_produto
        produto = Produto.objects.get(id=request.data['produto'])
        produto.quantidade_estoque = produto_data[0]['quantidade_estoque']
        produto.save()

        saida_serializer = self.get_serializer(data=request.data)
        saida_serializer.is_valid(raise_exception=True)
        self.perform_create(saida_serializer)
        headers = self.get_success_headers(saida_serializer.data)
        return Response(saida_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
