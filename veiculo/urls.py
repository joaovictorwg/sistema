from django.urls import path
from veiculo.views import ListarVeiculos, CriarVeiculos, EditarVeiculo, DeletarVeiculo, FotoVeiculo, APIListarVeiculos, APIDeletarVeiculos

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar-veiculos'),
    path('novo/', CriarVeiculos.as_view(), name='novo-veiculo'),
    path('edit/<int:pk>/', EditarVeiculo.as_view(), name='editar-veiculo'),
    path('delete/<int:pk>/', DeletarVeiculo.as_view(), name='deletar-veiculo'),
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='fotos-veiculo'),
    path('api/', APIListarVeiculos.as_view(), name='api-listar-veiculo'),
    path('delete/<int:pk>/', APIDeletarVeiculos.as_view(), name='api-deletar-veiculo'),

]

