from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

class Login(View):

    def get(self, request):
        contexto = {'mensagem': ''}
        if request.user.is_authenticated:
            return redirect('/veiculos')
        else:
            return render(request, 'autenticacao.html', contexto)

    def post(self, request):
        # Obtem as credenciais de autenticação do form
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/veiculo")
            return render(request, 'autenticacao.html', {'mensagem': 'Usuário inativo'})
        
        return render(request, 'autenticacao.html', {'mensagem': 'Usuário ou senha incorretos'})

class Logout(View):
    
    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)
    
