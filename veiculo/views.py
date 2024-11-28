from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.generic import View, CreateView, ListView, DeleteView, UpdateView
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from veiculo.forms import FormularioVeiculo
from veiculo.models import Veiculo
from veiculo.serializers import SerializadorVeiculo

# Create your views here.
class ListarVeiculos(LoginRequiredMixin, ListView):
    # Views para listar veiculos cadastrados
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'


class FotoVeiculo(LoginRequiredMixin, View):
    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo)) 
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist as exc:
            raise Http404("Foto não encontrada") from exc
        except Exception as exception:
            raise exception

class CriarVeiculos(LoginRequiredMixin, CreateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')

class EditarVeiculo(LoginRequiredMixin, UpdateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/edit.html'
    success_url = reverse_lazy('listar-veiculos')

class DeletarVeiculo(LoginRequiredMixin, DeleteView):
    model = Veiculo
    template_name = 'veiculo/delete.html'
    success_url = reverse_lazy('listar-veiculos')

    def get_object(self):
        return get_object_or_404(Veiculo, pk=self.kwargs['pk'])
    
class APIListarVeiculos(ListAPIView):
    """
    view para listar instancias de veiculos (por meio da API REST)
    """
    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()
    
class APIDeletarVeiculos(DestroyAPIView):
    """
    View para deletar instâncias de veículos (por meio da API REST)
    """
    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()