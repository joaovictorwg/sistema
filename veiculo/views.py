from django.shortcuts import render
from veiculo.models import Veiculo
from django.views.generic import ListView

# Create your views here.
class ListarVeiculos(ListView):
    # Views para listar veiculos cadastrados
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

