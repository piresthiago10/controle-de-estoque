from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from produto.api.viewsets import ProdutoViewSet
from categoria.api.viewsets import CategoriaViewSet
from usuario.api.viewsets import UsuarioViewSet
from tipo_usuario.api.viewsets import TipoUsuarioViewSet
from estoque_entrada.api.viewsets import EstoqueEntradaViewSet
from estoque_saida.api.viewsets import EstoqueSaidaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'produto', ProdutoViewSet, basename='Produto')
router.register(r'categoria', CategoriaViewSet)
router.register(r'usuario', UsuarioViewSet)
router.register(r'tipo_usuario', TipoUsuarioViewSet)
router.register(r'estoque_entrada', EstoqueEntradaViewSet)
router.register(r'estoque_saida', EstoqueSaidaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
