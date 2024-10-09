from django.contrib import admin
from django.urls import path

from veiculo.views import *

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar-veiculos'),
    path('novo/', CriarVeiculos.as_view(), name='novo-veiculo'),
    path('edit/<int:pk>/', EditarVeiculo.as_view(), name='editar-veiculo'),
    path('delete/<int:pk>/', DeletarVeiculo.as_view(), name='deletar-veiculo'),
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='fotos-veiculo'),

]

