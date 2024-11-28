from django.contrib import admin
from anuncio.models import Anuncio


# Register your models here.
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'descricao', 'veiculo', 'usuario', 'preco']
    search_fields = ['descricao','veiculo_modelo','usuario']

admin.site.register(Anuncio, AnuncioAdmin)