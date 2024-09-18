from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

class Login(View):

    def get(self, request):

        contexto =  {'mensagem': ''}

        return render(request, 'autenticacao.html', contexto)