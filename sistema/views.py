from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class Login(View):

    def get(self, request):
        contexto = {'mensagem': ''}
        if request.user.is_authenticated:
            return redirect('/veiculo')
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
    
class LoginAPI(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={
                'request': request
            }
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'id': user.id, 
            'nome': user.first_name,
            'email': user.email,
            'token': token.key
        })