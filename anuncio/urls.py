from django.urls import path
from anuncio.views import ListarAnuncios, CriarAnuncios, EditarAnuncios, DeletarAnuncios #<FotoVeiculo, CriarVeiculos, EditarVeiculos, DeletarVeiculos-->


urlpatterns = [
    path('', ListarAnuncios.as_view(), name='listar-anuncios'),
    path('novo/', CriarAnuncios.as_view(), name='criar-anuncios'),
    path('<int:pk>/', EditarAnuncios.as_view(), name='editar-anuncios'),
    path('deletar/<int:pk>/', DeletarAnuncios.as_view(), name='deletar-anuncios')
]