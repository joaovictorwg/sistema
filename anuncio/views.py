from django.shortcuts import render
from anuncio.models import Anuncio
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from anuncio.forms import FormularioAnuncio
# Create your views here.

class ListarAnuncios(LoginRequiredMixin, ListView):
    """
    View para listar anuncios cadastrados.
    """
    
    model = Anuncio
    context_object_name = 'anuncios'
    template_name = 'anuncio/listar.html'


class CriarAnuncios(LoginRequiredMixin, CreateView):
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/novo.html'
    success_url = reverse_lazy('listar-anuncios')


class EditarAnuncios(LoginRequiredMixin, UpdateView):
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/editar.html'
    success_url = reverse_lazy('listar-anuncios')


class DeletarAnuncios(LoginRequiredMixin, DeleteView):
    model = Anuncio
    template_name = 'anuncio/deletar.html'
    success_url = reverse_lazy('listar-anuncios')